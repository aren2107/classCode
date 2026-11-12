# 🌐 HOKAS Hosting Setup

1. Upload the **contents** of this ZIP to the bot root (do not create a nested ClassCode folder).
2. Set these environment variables:
   - `DISCORD_TOKEN` = your Discord bot token
   - `GUILD_ID` = your test server ID
   - `GEMINI_API_KEY` = your Gemini API key
   - `GEMINI_MODEL` = `gemini-3.8-flash` (or another currently supported Gemini model)
   - `DATABASE_URL` = Supabase PostgreSQL connection string (primary database; keep it private)
   - `CODE_RUNNER_URL` = `https://ce.judge0.com`
   - `CODE_RUNNER_API_KEY` = leave blank unless your runner requires it
   - `CODE_RUNNER_AUTH_USER` = leave blank unless your runner requires it
   - Do not put `NEON_DATABASE_URL` in the bot runtime. Neon is reserved for separately invoked backup/recovery jobs.
3. Startup command:

```bash
pip install -r requirements.txt && python -m bot
```

4. Enable **Server Members Intent** and **Message Content Intent** in the Discord Developer Portal.
5. Give the bot `Manage Roles`, `Manage Channels`, and the required message/thread permissions. Put the bot's highest role above `Admin`, `Student`, and `Unverified`. The ClassCode `Admin` role is a label only; privileged commands and restricted channels require Discord's real Administrator permission.
6. Review any existing `Admin` role before deploying: remove its Discord `Administrator` permission unless you intentionally want that role to grant full server control, and remove it from non-administrators. The bot does not rewrite an existing role's permissions automatically.

## Code execution

ClassCode uses the shared runner in `bot/services/code_runner.py` for daily challenges. Practical exam submissions are stored for manual review; they are not sent to Judge0. The student-facing `/run` command and lesson execution button are not enabled; students use **Review My Code** / `/code-review` for feedback. `https://ce.judge0.com` is a public Judge0 CE instance and should be treated as a testing/default endpoint, not a reliability guarantee for production. Before relying on daily challenges, run a live C++ and Java submission from HOKAS. If the endpoint is unavailable, rate-limited, or requires authentication, set `CODE_RUNNER_URL` and the optional auth variables to a compatible dedicated instance. Judge0 supports token authentication through the `X-Auth-Token` header.


## Pre-launch integrity checks
- `/event-points` is staff-only; students cannot award themselves event points.
- Re-running `/setup` refreshes the verification and questionnaire panels instead of creating duplicates.
- The final ZIP must not contain database snapshots, environment files, credentials, or Python cache files. The bot has no local database mode.
