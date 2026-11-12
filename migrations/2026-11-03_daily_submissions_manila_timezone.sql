-- Future daily challenge timestamps use Manila local wall time.
-- Existing rows are deliberately not rewritten because their original session
-- timezone may be unknown.

SET LOCAL lock_timeout = '5s';
SET LOCAL statement_timeout = '30s';

DO $$
BEGIN
    IF lower(coalesce(current_setting('classcode.environment', true), '')) <> 'staging' THEN
        RAISE EXCEPTION 'ClassCode migration requires classcode.environment=staging';
    END IF;

    IF nullif(btrim(current_setting('classcode.project_id', true)), '') IS NULL THEN
        RAISE EXCEPTION 'ClassCode migration requires a non-empty project marker';
    END IF;
END
$$;

ALTER TABLE public.daily_submissions
    ALTER COLUMN submitted_at
    SET DEFAULT timezone('Asia/Manila', CURRENT_TIMESTAMP);