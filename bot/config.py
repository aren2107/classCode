import os
from urllib.parse import urlsplit
from dotenv import load_dotenv

load_dotenv()


class Config:
    DISCORD_TOKEN: str = os.getenv("DISCORD_TOKEN", "").strip()
    GUILD_ID: int | None = int(os.getenv("GUILD_ID")) if os.getenv("GUILD_ID") else None
    # Supabase is the only application database. Neon is never read by the bot.
    DATABASE_URL: str = os.getenv("DATABASE_URL", "").strip()
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
    CODE_RUNNER_URL: str = os.getenv("CODE_RUNNER_URL", "https://ce.judge0.com")
    CODE_RUNNER_API_KEY: str = os.getenv("CODE_RUNNER_API_KEY", "")
    CODE_RUNNER_AUTH_USER: str = os.getenv("CODE_RUNNER_AUTH_USER", "")

    @classmethod
    def validate(cls):
        if not cls.DISCORD_TOKEN:
            raise ValueError("DISCORD_TOKEN is missing. Configure it in the environment or .env file.")
        if os.getenv("NEON_DATABASE_URL", "").strip():
            raise ValueError("NEON_DATABASE_URL must not be configured in the bot runtime; Neon is backup/recovery-only.")
        if not cls.DATABASE_URL:
            raise ValueError("DATABASE_URL is required. Configure the Supabase PostgreSQL connection string.")
        parsed = urlsplit(cls.DATABASE_URL)
        if parsed.scheme not in {"postgres", "postgresql"} or not parsed.hostname:
            raise ValueError("DATABASE_URL must be a valid PostgreSQL connection URL.")
        host = parsed.hostname.lower()
        if host.endswith(".neon.tech"):
            raise ValueError("DATABASE_URL must point to Supabase. Neon is reserved for backups and recovery.")
        if not (host.endswith(".supabase.com") or host.endswith(".supabase.co")):
            raise ValueError("DATABASE_URL must use an approved Supabase PostgreSQL hostname.")

        runner_url = urlsplit(cls.CODE_RUNNER_URL)
        runner_host = (runner_url.hostname or "").lower()
        local_runner = runner_host in {"localhost", "127.0.0.1", "::1"}
        if not runner_host or (runner_url.scheme != "https" and not (local_runner and runner_url.scheme == "http")):
            raise ValueError("CODE_RUNNER_URL must use HTTPS (HTTP is allowed only for a local loopback service).")
        if runner_url.username or runner_url.password:
            raise ValueError("Do not put credentials in CODE_RUNNER_URL; use the dedicated runner auth variables.")
