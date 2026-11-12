"""Shared sandboxed code-execution client.

ClassCode uses Judge0-compatible HTTP execution instead of the retired public
Piston endpoint. The URL and optional authentication token are configurable
through environment variables so the bot can move to another Judge0 instance
without changing the cogs.
"""
from __future__ import annotations

import asyncio
import base64
import json
import logging
import time
from dataclasses import dataclass
from typing import Any

import aiohttp

from bot.config import Config

logger = logging.getLogger("ClassCodeBot.code_runner")
MAX_RUNNER_RESPONSE_BYTES = 1_000_000


class CodeRunnerError(RuntimeError):
    """The execution service could not accept or complete a submission."""


@dataclass(slots=True)
class RunResult:
    stdout: str = ""
    stderr: str = ""
    compile_output: str = ""
    status_id: int | None = None
    status: str = ""
    time: str | None = None
    memory: int | None = None

    @property
    def successful(self) -> bool:
        return self.status_id == 3 and not self.stderr and not self.compile_output


class CodeRunner:
    LANGUAGE_NAMES = {
        "cpp": ("C++", "C++ (GCC"),
        "java": ("Java", "Java (OpenJDK"),
    }

    @staticmethod
    def _extract_status_id(data: dict[str, Any]) -> int | None:
        """Pull the numeric Judge0 status id out of a submission payload.

        Judge0's default response fields do NOT include a flat "status_id"
        key \u2014 the id only appears nested inside a "status" object, e.g.
        {"status": {"id": 2, "description": "Processing"}}. Relying only on
        a flat "status_id" (which is usually absent) meant every poll read
        None, which is not in (1, 2), so the poll loop always exited on its
        very first pass and treated a still-queued/still-running submission
        as finished \u2014 reporting empty output while the judge was still
        working. Check both shapes so we actually wait for completion.
        """
        status_id = data.get("status_id")
        if isinstance(status_id, int):
            return status_id
        status_obj = data.get("status")
        if isinstance(status_obj, dict):
            inner = status_obj.get("id")
            if isinstance(inner, int):
                return inner
        return None

    def __init__(self) -> None:
        self.base_url = Config.CODE_RUNNER_URL.rstrip("/")
        self.api_token = Config.CODE_RUNNER_API_KEY.strip()
        self.auth_user = Config.CODE_RUNNER_AUTH_USER.strip()
        self._language_ids: dict[str, int] = {}
        self._language_lock = asyncio.Lock()
        self._language_loaded_at = 0.0
        # Bound simultaneous submissions to protect shared runner capacity.
        self._run_semaphore = asyncio.Semaphore(5)

    def _headers(self) -> dict[str, str]:
        headers = {"Content-Type": "application/json"}
        if self.api_token:
            headers["X-Auth-Token"] = self.api_token
        if self.auth_user:
            headers["X-Auth-User"] = self.auth_user
        return headers

    async def _request_json(
        self,
        session: aiohttp.ClientSession,
        method: str,
        url: str,
        **kwargs: Any,
    ) -> tuple[int, dict[str, Any]]:
        try:
            async with session.request(method, url, headers=self._headers(), **kwargs) as response:
                raw_bytes = await response.content.read(MAX_RUNNER_RESPONSE_BYTES + 1)
                if len(raw_bytes) > MAX_RUNNER_RESPONSE_BYTES:
                    raise CodeRunnerError("The code execution service returned an oversized response.")
                raw = raw_bytes.decode("utf-8", errors="replace")
                try:
                    data = json.loads(raw) if raw else {}
                except Exception:
                    data = {"error": "The execution service returned an invalid response."}
                if not isinstance(data, dict):
                    data = {"data": data}
                return response.status, data
        except asyncio.TimeoutError as exc:
            raise CodeRunnerError("The code execution service timed out.") from exc
        except aiohttp.ClientError as exc:
            raise CodeRunnerError(f"Could not connect to the code execution service: {type(exc).__name__}.") from exc

    async def _load_languages(self, session: aiohttp.ClientSession) -> None:
        async with self._language_lock:
            if self._language_ids and time.monotonic() - self._language_loaded_at < 3600:
                return
            status, data = await self._request_json(session, "GET", f"{self.base_url}/languages/")
            if status != 200:
                logger.warning("Runner language list request failed with HTTP %s", status)
                raise CodeRunnerError(f"Runner language list unavailable (HTTP {status}).")
            languages = data.get("data", data)
            if not isinstance(languages, list):
                raise CodeRunnerError("Runner returned an invalid language list.")

            found: dict[str, int] = {}
            for item in languages:
                if not isinstance(item, dict):
                    continue
                name = str(item.get("name", ""))
                try:
                    language_id = int(item["id"])
                except (KeyError, TypeError, ValueError):
                    continue
                low = name.lower()
                if "c++" in low and "gcc" in low and "cpp" not in found:
                    found["cpp"] = language_id
                if low.startswith("java ") and "java" not in found:
                    found["java"] = language_id

            missing = [key for key in ("cpp", "java") if key not in found]
            if missing:
                raise CodeRunnerError("Runner does not provide the required language(s): " + ", ".join(missing))
            self._language_ids = found
            self._language_loaded_at = time.monotonic()

    async def run(
        self,
        language: str,
        code: str,
        stdin: str = "",
        *,
        timeout_seconds: float = 25,
        cpu_time_limit: float = 3.0,
        memory_limit: int = 128000,
    ) -> RunResult:
        async with self._run_semaphore:
            return await self._run_one(
                language, code, stdin,
                timeout_seconds=timeout_seconds,
                cpu_time_limit=cpu_time_limit,
                memory_limit=memory_limit,
            )

    async def _run_one(
        self,
        language: str,
        code: str,
        stdin: str = "",
        *,
        timeout_seconds: float = 25,
        cpu_time_limit: float = 3.0,
        memory_limit: int = 128000,
    ) -> RunResult:
        language = language.lower().strip()
        if language not in self.LANGUAGE_NAMES:
            raise CodeRunnerError("Only C++ and Java are enabled in ClassCode.")
        if not code.strip():
            raise CodeRunnerError("No code was provided.")
        if len(code) > 8000:
            raise CodeRunnerError("Code is too large. Maximum is 8000 characters.")

        timeout = aiohttp.ClientTimeout(total=timeout_seconds)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            await self._load_languages(session)
            payload = {
                "source_code": code,
                "language_id": self._language_ids[language],
                "stdin": stdin,
                "cpu_time_limit": cpu_time_limit,
                "wall_time_limit": min(max(timeout_seconds - 2, 5), 30),
                "memory_limit": memory_limit,
            }
            # Judge0 CE officially documents wait=false as the portable path;
            # polling also works when an instance disables wait=true.
            status, data = await self._request_json(
                session,
                "POST",
                f"{self.base_url}/submissions/?base64_encoded=false&wait=false",
                json=payload,
            )
            if status not in (200, 201):
                logger.warning("Runner rejected a submission with HTTP %s", status)
                raise CodeRunnerError(f"Runner rejected the submission (HTTP {status}).")

            token = data.get("token")
            if not token:
                # Some compatible instances return a completed result directly.
                return self._result_from_payload(data)

            deadline = time.monotonic() + max(timeout_seconds - 1, 5)
            while time.monotonic() < deadline:
                await asyncio.sleep(0.8)
                status, result = await self._request_json(
                    session,
                    "GET",
                    f"{self.base_url}/submissions/{token}?base64_encoded=false",
                )
                if status != 200:
                    logger.warning("Runner status request failed with HTTP %s", status)
                    raise CodeRunnerError(f"Runner status request failed (HTTP {status}).")
                status_id = self._extract_status_id(result)
                # Judge0 status IDs 1/2 are In Queue/Processing.
                if status_id in (1, 2):
                    continue
                return self._result_from_payload(result)

            raise CodeRunnerError("The code execution service took too long to finish.")

    @staticmethod
    def _result_from_payload(data: dict[str, Any]) -> RunResult:
        def decode(value: Any) -> str:
            if not value:
                return ""
            text = str(value)
            # Judge0 may return encoded fields when a compatible instance
            # enables base64 responses despite the query parameter.
            try:
                if data.get("base64_encoded") is True:
                    return base64.b64decode(text).decode("utf-8", errors="replace")
            except Exception:
                pass
            return text

        status = data.get("status") or {}
        return RunResult(
            stdout=decode(data.get("stdout")),
            stderr=decode(data.get("stderr")),
            compile_output=decode(data.get("compile_output")),
            status_id=CodeRunner._extract_status_id(data),
            status=str(status.get("description", "")) if isinstance(status, dict) else str(status),
            time=str(data.get("time")) if data.get("time") is not None else None,
            memory=data.get("memory") if isinstance(data.get("memory"), int) else None,
        )


runner = CodeRunner()
