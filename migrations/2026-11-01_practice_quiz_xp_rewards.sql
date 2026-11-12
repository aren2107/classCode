-- NEW replacement migration; not recovered historical SQL.
-- tools/migration_runner.py executes this entire file inside one transaction.
-- Creates an empty, idempotent one-time practice reward claim ledger.
SET LOCAL lock_timeout = '5s';
SET LOCAL statement_timeout = '30s';
DO $$
BEGIN
    IF lower(coalesce(current_setting('classcode.environment', true), '')) <> 'staging' THEN
        RAISE EXCEPTION 'ClassCode migrations are restricted to classcode.environment=staging';
    END IF;
    IF nullif(current_setting('classcode.project_id', true), '') IS NULL THEN
        RAISE EXCEPTION 'ClassCode migration requires classcode.project_id to identify the confirmed staging project';
    END IF;
END $$;

CREATE TABLE IF NOT EXISTS public.practice_quiz_xp_rewards (
    user_id BIGINT NOT NULL,
    language TEXT NOT NULL,
    topic_id TEXT NOT NULL,
    xp_awarded BIGINT NOT NULL,
    recorded_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT practice_quiz_xp_rewards_pkey PRIMARY KEY (user_id, language, topic_id)
);
