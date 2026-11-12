# ClassCode PostgreSQL Schema Relationship and Migration Review

**Status:** Prepared from the current source and release archive. No database was connected and no migration was applied. The application has no user/table deletion commands; the only database delete found is removal from the transient `pair_queue`. Ticket deletion removes a Discord channel, not database rows.

## Relationship decisions

The user table is the root for student-owned records. Proposed FKs use `ON DELETE RESTRICT`/default `NO ACTION`; no `CASCADE` is proposed because the application has no account-erasure workflow and the affected tables include historical XP, attendance, mastery, submissions, certificates, and work artifacts.

| Child table.column | Parent table.column | Notes |
|---|---|---|
| `user_progress.user_id` | `users.user_id` | Student progress; current primary key already makes the full identity unique. |
| `quiz_attempts.user_id` | `users.user_id` | Attempts are historical and may repeat. |
| `practice_quiz_xp_rewards.user_id` | `users.user_id` | One-time claim belongs to a student; the integrity migration uses `ON DELETE RESTRICT`. |
| `user_badges.user_id` | `users.user_id` | Existing `(user_id,badge_id)` primary key. |
| `daily_submissions.user_id` | `users.user_id` | Existing one-row-per-user/challenge unique key. **No challenge FK:** runtime challenge IDs come from the cog's in-code challenge list; `daily_challenges` is not populated by the current flow. |
| `xp_history.user_id` | `users.user_id` | Preserve history. |
| `daily_goals.user_id` | `users.user_id` | Existing `(user_id,goal_date)` primary key. |
| `project_progress.user_id` | `users.user_id` | Existing `(user_id,project_id)` primary key. |
| `project_progress.project_id` | `projects.project_id` | Project definitions are seeded before completion writes. |
| `classes.teacher_id` | `users.user_id` | Class owner. |
| `class_members.class_id` | `classes.class_id` | Existing `(class_id,user_id)` primary key. |
| `class_members.user_id` | `users.user_id` | Student/teacher membership. |
| `assignments.class_id` | `classes.class_id` | Assignment belongs to a class. |
| `assignment_submissions.assignment_id` | `assignments.assignment_id` | Existing `(assignment_id,user_id)` primary key provides one rewardable submission per student/assignment. |
| `assignment_submissions.user_id` | `users.user_id` | Student owner. |
| `code_snippets.user_id`, `personal_notes.user_id` | `users.user_id` | Student-owned work and notes. |
| `user_titles.user_id`, `user_stats.user_id` | `users.user_id` | Existing primary keys cover owner lookups. |
| `daily_missions.user_id` | `users.user_id` | Existing `(user_id,mission_date,kind)` unique key. |
| `bug_attempts.user_id` | `users.user_id` | Existing `(user_id,puzzle_id)` primary key. |
| `bug_attempts.puzzle_id` | `bug_puzzles.puzzle_id` | Puzzle rows are seeded by the academy cog before normal use. |
| `study_groups.owner_id` | `users.user_id` | Group owner. |
| `study_group_members.group_id` | `study_groups.group_id` | Existing `(group_id,user_id)` primary key. |
| `study_group_members.user_id` | `users.user_id` | Member identity. |
| `pair_queue.user_id` | `users.user_id` | Ephemeral queue state; removing a queue entry is not account deletion. |
| `event_progress.user_id` | `users.user_id` | Event points. |
| `portfolio_projects.user_id` | `users.user_id` | Student portfolio. |
| `portfolio_projects.project_id` | `projects.project_id` | Project definition. Do not add `(user_id,project_id)` uniqueness without a product decision; the current table permits multiple portfolio entries per project. |
| `certificates.user_id` | `users.user_id` | Do not add `(user_id,language)` uniqueness without a certificate re-issue policy. |
| `practical_exams.created_by` | `users.user_id` | Exam creator. Discord channel/thread IDs are external references, not FKs. |
| `practical_exam_submissions.exam_id` | `practical_exams.exam_id` | Multiple submissions per exam/user are permitted by current code; preserve retry/history behavior. |
| `practical_exam_submissions.user_id` | `users.user_id` | Student owner. |
| `attendance_records.user_id` | `users.user_id` | Existing `(user_id,attendance_date)` primary key prevents duplicate daily check-ins. |
| `lesson_mastery.user_id` | `users.user_id` | Existing `(user_id,language,topic_id)` primary key. |

`event_id`, curriculum topic IDs, badges, titles, and exam Discord IDs are application/external identifiers with no authoritative parent table in this schema. A database FK would be inappropriate without introducing and maintaining catalog tables.

## Practice quiz XP reward ledger

The approved one-time practice reward uses `practice_quiz_xp_rewards` with primary key `(user_id, language, topic_id)`. The language and topic values are stable application identifiers (`cpp`/`java` and curriculum topic IDs), never lesson display titles. Its uniqueness key makes simultaneous claims conflict safely. The integrity migration adds a restricted user FK; quiz submissions ensure the student row before recording the claim.

The intended `migrations/2026-11-01_practice_quiz_xp_rewards.sql` staging migration creates an empty ledger. Its authoritative SQL file is absent from the current release archive and must be recovered from project history before use; do not reconstruct it from this report. Bot startup performs no schema initialization. First successful attempts under the new policy insert `xp_awarded=50` in the same transaction as the attempt and XP update.

## Existing uniqueness and candidate uniqueness

The schema already has primary/unique keys for users, per-topic progress/mastery, badges, goals, project progress, memberships, assignments/submissions, missions, bug attempts, queue membership, event progress, and one daily submission per user/challenge. The new reward ledger adds only the policy-required unique key `(user_id,language,topic_id)`; quiz and exam attempt histories remain repeatable, and portfolio duplicates/certificate re-issues remain unchanged.

## Checks and required values proposed

After the read-only preflight passes, the migration proposes nonnegative XP/counters/scores; quiz score within total and binary pass flags; valid progress/review states; valid boolean-like flags; practical-exam score in 0–100 and passed test count not exceeding total; and `NOT NULL` on nullable owner IDs/defaulted counters that are required by the application. It does not constrain free-form notes, code, feedback, external IDs, or dates beyond existing keys. Status values are enumerated only where the current write paths define a closed set; review the report and migration as a unit.

## Indexes

Primary/unique indexes already cover several FK/query prefixes. Candidate additions cover missing FK/query prefixes: `quiz_attempts(user_id,attempted_at)`, `xp_history(user_id,id)`, `project_progress(project_id,user_id)`, `classes(teacher_id,class_id)`, `class_members(user_id,class_id)`, `assignments(class_id,assignment_id)`, `assignment_submissions(user_id,assignment_id)`, `code_snippets(user_id,snippet_id)`, `personal_notes(user_id,title,note_id)`, `bug_attempts(puzzle_id,user_id)`, `study_groups(owner_id,group_id)`, `study_group_members(user_id,group_id)`, `portfolio_projects(project_id,user_id)`, `certificates(user_id,certificate_id)`, `practical_exams(created_by,exam_id)`, and `practical_exam_submissions(exam_id,submission_id)` plus `(user_id,submitted_at)`. Validate query plans and index size on staging before production approval.

## Preflight and rollback

Run `tools/validate_schema_migration.py` with an explicit staging URL, exact expected hostname, and confirmation flag. It opens a read-only transaction and prints aggregate missing-table, null-key, orphan, candidate-check, and duplicate-candidate counts only. Resolve every blocking finding without deleting student records, then take a verified backup and rehearse the migration on a disposable PostgreSQL database and a new Supabase staging project.

The migration requires the session setting `classcode.environment=staging`. It adds constraints `NOT VALID`, validates them before commit, and applies indexes/`NOT NULL` only after the same guards. The companion rollback drops only the new indexes and constraints and relaxes the new `NOT NULL` attributes; it does not alter or delete rows. Keep rollback SQL and a pre-migration backup available. A rollback after future code starts relying on constraints should be treated as a coordinated code/schema rollback.

**Unverified:** No PostgreSQL server, `psql`, `pg_dump`, `pg_restore`, Docker, or Podman executable is installed in this environment. Therefore neither this migration nor rollback has been executed against PostgreSQL. The SQL remains a staging candidate, not production-approved migration material.
