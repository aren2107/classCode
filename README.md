# ClassCode 3.4.3 — Concurrent-User Hardening

> This package applies the curriculum educational audit revisions: topic-specific practice contracts, guided/independent practice, diagnostic tasks, objective-to-assessment mapping, spaced review metadata, stronger mastery evidence, and expanded validation.


The learning system now uses lesson-owned educational content and lesson-owned mastery quizzes.

- C++: 58 structured lessons
- Java: 55 structured lessons
- Exact lesson ID mapping for navigation and progress
- Five-question mastery bank per lesson
- Automated curriculum validation
- Supabase PostgreSQL is the only application database; the bot has no local database mode
- Mobile-friendly Discord mastery UI

See `LEARNING_ARCHITECTURE.md` for the audit and architecture details.

# ClassCode Academy — 5-Star Learning Edition

ClassCode is a Discord-based programming academy focused on a complete learning path from beginner fundamentals to advanced programming and practical projects.

## Learning path

The current release contains 58 C++ lessons and 55 Java lessons across six learning stages:

1. Foundation
2. Core Problem Solving
3. Data & Design
4. Object-Oriented Programming
5. Advanced Language Skills
6. Algorithms & Engineering

Tracks:
- C++: 58 lessons
- Java: 55 lessons

The curriculum intentionally moves from syntax and basic logic into data structures, algorithms, software design, testing, debugging, and capstone work.

## Lesson experience

Every lesson provides:

- 🎯 learning objective
- 💡 why the concept matters
- 📖 concept explanation
- 🔑 key rules
- ⚠️ common mistakes
- 💻 worked example
- 🔎 line-by-line explanation
- 👀 output prediction / transfer thinking
- 🧪 coding challenge
- 🧭 implementation plan
- 💡 hint
- 🐛 debugging guidance
- 🧠 five-question mastery check
- 🚀 extension challenge
- ⭐ XP and progress tracking

A lesson must score at least 4/5 on its mastery check before it can be completed and the next lesson unlocked.

## Placement

`/placement` provides a short 10-question check for C++ or Java. It recommends a starting stage for learners who already have experience. It does not claim that a quiz proves professional or advanced competence.

Earlier lessons remain available as review material.

## Main student flow

Join → Verify → Questionnaire → `/start` → optional `/placement` → Lesson → Practice → Mastery → Next Lesson → Projects → Practical Exams → Capstone

## Practice and projects

The bot includes:
- `/code-review` for AI-assisted C++/Java feedback without handing students a full replacement solution
- `/hint`
- `/explain`
- `/explain-error`
- `/code-review`
- quizzes
- daily challenges
- debugging puzzles
- project lab
- practical exam forums with administrator/teacher review (student code is not automatically run)
- XP, levels, streaks, badges, and progress
- support tickets

## Practical exams

Practical exams are code-only submissions. Students submit source code against the stated problem and requirements, and an administrator/teacher reviews and grades the submission. AI feedback may be used as supplementary feedback.

## Setup

See `HOKAS_SETUP.md` and `BOT_HOSTING_SETUP.md`.

Startup command:

```bash
python -m bot
```

Required environment variables:

```env
DISCORD_TOKEN=your_bot_token
GUILD_ID=your_test_server_id
GEMINI_API_KEY=your_gemini_key
GEMINI_MODEL=gemini-3.8-flash
# Primary database (Supabase PostgreSQL). Keep the actual value private.
DATABASE_URL=postgresql://...
CODE_RUNNER_URL=https://ce.judge0.com
CODE_RUNNER_API_KEY=
CODE_RUNNER_AUTH_USER=
```

## Verification performed for Step 4.1

- `python -m unittest discover -s tests -v`: 49 tests passed, including the opt-in integration rehearsal against a disposable local PostgreSQL `classcode_test` database.
- `python -m compileall -q bot tools tests`: passed.
- Curriculum validation: C++ 58/58 and Java 55/55 lessons passed.
- Mastery validation: passed for all 58 C++ and 55 Java lessons.
- Educational-quality validation: passed for all 58 C++ and 55 Java lessons.
- The HOKAS release package excludes tests, private environment files, Python caches/bytecode, database snapshots, SQLite/database files, and nested archives.
- The local rehearsal did not connect to Supabase, Neon, HOKAS, staging, or production. No cloud migration, backup, restore, or deployment was performed. A separate approved Supabase staging rehearsal and hosting smoke test remain future steps.

See `STEP4_1_RELEASE_FIX_REPORT.md` for the verification details and limits.


### Code runner

ClassCode uses a shared Judge0-compatible execution service for daily challenges. Practical exam submissions are stored for manual review and are not automatically executed. Students use **Review My Code** and `/code-review` for learning feedback rather than a bot-hosted interactive terminal. Event points are staff-awarded only so students cannot manipulate event rankings. The default is `https://ce.judge0.com` for initial testing; the public instance is not a production reliability guarantee. `CODE_RUNNER_URL` can be changed to another compatible HTTPS instance. Optional authentication is supported with `CODE_RUNNER_API_KEY` and `CODE_RUNNER_AUTH_USER`.

The runner is intentionally centralized in `bot/services/code_runner.py`, so execution backend changes do not require rewriting the learning, challenge, or exam features.

## 3.3.0 Learning Quality Upgrade

This build adds explicit lesson prerequisites, topic-specific practice contracts, 5-question mastery with a 4/5 passing score, a `/review` command for weak completed lessons, and a visible **🧭 Step-by-step** instruction on every lesson screen. The guidance always tells the learner which button to click next.

Run the offline curriculum audit with:

```bash
python tools/validate_curriculum.py
```


## Admin lesson assignment

Admins can set a student's active lesson without wiping or falsifying their progress:

- `/student-set-java student:@Student lesson:<Java lesson>`
- `/student-set-cpp student:@Student lesson:<C++ lesson>`

Choose the lesson from Discord's autocomplete. The assigned lesson is granted access and becomes the focus of that student's matching quiz command. Existing completion records are preserved; earlier lessons are **not** automatically marked completed. A new quiz attempt uses a different mix of questions tied to the same lesson.

## PostgreSQL primary database (Supabase)

- Set `DATABASE_URL` to the Supabase **PostgreSQL connection string** in the hosting environment. This is the primary database used by the bot.
- `DATABASE_URL` is mandatory for every bot run and must point to Supabase PostgreSQL. There is no local database mode or database fallback.
- Install dependencies with `pip install -r requirements.txt`; PostgreSQL access uses Psycopg 3.
- `bot/postgres_schema.sql` is the base PostgreSQL schema. Startup performs a read-only required-table check and never creates tables or applies migrations. Operators must apply reviewed schema changes separately to an explicitly identified staging project.
- `NEON_DATABASE_URL` is reserved for the separate backup target. Setting it alone does not automatically create backups; backup scheduling and restore verification must be configured separately.

### Clean PostgreSQL initialization

The Supabase deployment starts with a fresh PostgreSQL project. Operators apply the approved base schema and the newly authored, tracked replacement SQL migrations before starting the bot. The historical migration SQL files were not recoverable from the available source package or backup; the replacement files are documented in `migrations/README.md` and must not be described as recovered originals. The bot creates no database or imports historical records. Neon receives backups only from the Supabase primary and is never a runtime database.

Never commit connection strings, `.env` files, or database backups containing student records.

### Neon backup and schema setup

- Set `NEON_DATABASE_URL` to the Neon PostgreSQL connection string in the private environment used for backup jobs. It is not used for normal bot reads/writes.
- Apply the schema to Neon once with `python tools/apply_postgres_schema.py --target neon` after setting both database URL variables securely.
- To make a one-off snapshot, run `python tools/backup_supabase_to_neon.py --confirm-overwrite` in a secure environment with both URLs set. This replaces the ClassCode tables on Neon inside one transaction; a failed transaction rolls back. The command prints UTC start/completion timestamps, verifies per-table row counts, and restores IDENTITY/SERIAL sequences. Review the target connection string carefully before confirming.
- Schedule this script with an external scheduler/CI task or a trusted host cron job. It is intentionally not run by the Discord bot at startup. Set a cadence appropriate for student data, monitor job failures, and periodically rehearse restoring Neon to a separate test database.
- The backup script only targets tables defined in `bot/postgres_schema.sql`; it does not truncate unrelated public tables.
