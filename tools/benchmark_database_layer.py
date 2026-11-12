"""Read-only staging benchmark for fresh connections, serialization, and concurrency."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import os
import statistics
import threading
import time
import sys
from urllib.parse import urlsplit


def _summary(label: str, samples: list[float]) -> None:
    ordered = sorted(samples)
    p95 = ordered[min(len(ordered) - 1, int(len(ordered) * 0.95))]
    print(
        f"{label}: n={len(samples)} mean_ms={statistics.fmean(samples)*1000:.2f} "
        f"p50_ms={statistics.median(samples)*1000:.2f} p95_ms={p95*1000:.2f} "
        f"max_ms={max(samples)*1000:.2f}"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-host", required=True)
    parser.add_argument("--confirm-staging-target", action="store_true")
    parser.add_argument("--confirm-connection-headroom", action="store_true", help="Confirm provider dashboard allows the bounded benchmark connection count")
    parser.add_argument("--operations", type=int, default=30)
    parser.add_argument("--concurrency", type=int, default=4)
    args = parser.parse_args()
    dsn = os.getenv("STAGING_DATABASE_URL", "").strip()
    if not dsn:
        parser.error("Set STAGING_DATABASE_URL in a private environment")
    host = (urlsplit(dsn).hostname or "").lower()
    if host != args.expected_host.strip().lower():
        parser.error("STAGING_DATABASE_URL does not match --expected-host")
    if not (host.endswith(".supabase.co") or host.endswith(".supabase.com")):
        parser.error("Only a dedicated Supabase staging host is accepted")
    if not args.confirm_staging_target:
        parser.error("Pass --confirm-staging-target after verifying the host is isolated")
    if not args.confirm_connection_headroom:
        parser.error("Check the Supabase plan/pooler limits and pass --confirm-connection-headroom")
    if not 5 <= args.operations <= 1000:
        parser.error("--operations must be between 5 and 1000")
    if not 1 <= args.concurrency <= 8:
        parser.error("--concurrency must be between 1 and 8 to limit connection load")
    try:
        import psycopg
    except ImportError:
        print("Install requirements.txt before running the benchmark.", file=sys.stderr)
        return 2

    try:
        with psycopg.connect(dsn, connect_timeout=5, sslmode="require") as conn:
            conn.execute("SET TRANSACTION READ ONLY")
            max_connections = int(conn.execute("SHOW max_connections").fetchone()[0])
            numbackends = int(conn.execute(
                "SELECT COALESCE(sum(numbackends),0) FROM pg_stat_database"
            ).fetchone()[0])
            try:
                reserved = int(conn.execute("SHOW reserved_connections").fetchone()[0])
            except psycopg.errors.UndefinedObject:
                conn.rollback()
                reserved = int(conn.execute("SHOW superuser_reserved_connections").fetchone()[0])
        available_estimate = max_connections - numbackends - reserved
        required_headroom = args.concurrency + 2
        print(f"Staging benchmark host={host} max_connections={max_connections} observed_database_backends={numbackends} reserved={reserved} estimated_headroom={available_estimate}")
        if available_estimate < required_headroom:
            raise RuntimeError(
                f"Refusing benchmark: estimated headroom {available_estimate} is below required {required_headroom}"
            )

        query_samples = []
        with psycopg.connect(dsn, connect_timeout=5, sslmode="require") as conn:
            for _ in range(args.operations):
                started = time.perf_counter()
                conn.execute("SELECT 1").fetchone()
                query_samples.append(time.perf_counter() - started)

        def fresh_connection(_index: int) -> float:
            started = time.perf_counter()
            with psycopg.connect(dsn, connect_timeout=5, sslmode="require") as conn:
                conn.execute("SELECT 1").fetchone()
            return time.perf_counter() - started

        fresh_serial = [fresh_connection(i) for i in range(args.operations)]
        lock = threading.Lock()

        def serialized_connection(index: int) -> float:
            with lock:
                return fresh_connection(index)

        with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
            serialized = list(executor.map(serialized_connection, range(args.operations)))
        with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
            concurrent_fresh = list(executor.map(fresh_connection, range(args.operations)))

        _summary("reused_connection_select_1", query_samples)
        _summary("fresh_connection_serial", fresh_serial)
        _summary("current_process_lock_shape", serialized)
        _summary(f"fresh_connections_concurrency_{args.concurrency}", concurrent_fresh)
        print("No rows were read beyond catalog counters, and no database writes were made.")
        print("Compare provider limits and workload before considering a pool; results are staging-only measurements.")
        return 0
    except Exception as exc:
        print(f"Benchmark failed or was refused ({type(exc).__name__}); no connection string was logged.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
