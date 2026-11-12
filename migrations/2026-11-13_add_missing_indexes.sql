-- NEW migration; adds query-supporting indexes identified during production audit.
-- tools/migration_runner.py executes this entire file inside one transaction.
SET LOCAL lock_timeout = '5s';
SET LOCAL statement_timeout = '60s';
DO $$
BEGIN
    IF lower(coalesce(current_setting('classcode.environment', true), '')) <> 'staging' THEN
        RAISE EXCEPTION 'ClassCode migrations are restricted to classcode.environment=staging';
    END IF;
    IF nullif(current_setting('classcode.project_id', true), '') IS NULL THEN
        RAISE EXCEPTION 'ClassCode migration requires classcode.project_id to identify the confirmed staging project';
    END IF;
END $$;

-- lesson_mastery: review_due_at queried in get_review_recommendations
CREATE INDEX IF NOT EXISTS ix_cc_lesson_mastery_review_due
ON public.lesson_mastery (review_due_at)
WHERE review_due_at IS NOT NULL;

-- user_progress: status filtering in sync_progress
CREATE INDEX IF NOT EXISTS ix_cc_user_progress_status
ON public.user_progress (status);

-- quiz_attempts: topic_id + language for lesson-aware quiz queries
CREATE INDEX IF NOT EXISTS ix_cc_quiz_attempts_topic_language
ON public.quiz_attempts (topic_id, language);