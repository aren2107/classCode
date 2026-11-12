-- NEW replacement rollback for the exact integrity DDL above.
-- Removes only named ClassCode constraints/indexes; never changes rows.
BEGIN;
SET LOCAL lock_timeout = '5s';
SET LOCAL statement_timeout = '60s';
DO $$
BEGIN
    IF lower(coalesce(current_setting('classcode.environment', true), '')) <> 'staging' THEN
        RAISE EXCEPTION 'ClassCode rollback is restricted to classcode.environment=staging';
    END IF;
    IF nullif(current_setting('classcode.project_id', true), '') IS NULL THEN
        RAISE EXCEPTION 'ClassCode rollback requires classcode.project_id to identify the connected staging project';
    END IF;
    IF nullif(current_setting('classcode.expected_project_id', true), '') IS NULL THEN
        RAISE EXCEPTION 'ClassCode rollback requires classcode.expected_project_id supplied independently by the operator';
    END IF;
    IF current_setting('classcode.project_id', true) IS DISTINCT FROM current_setting('classcode.expected_project_id', true) THEN
        RAISE EXCEPTION 'ClassCode rollback refused: connected project ID does not match the independently confirmed expected project ID';
    END IF;
END $$;

ALTER TABLE public.lesson_mastery DROP CONSTRAINT IF EXISTS fk_cc_lesson_mastery_user_id_users;
ALTER TABLE public.attendance_records DROP CONSTRAINT IF EXISTS fk_cc_attendance_records_user_id_users;
ALTER TABLE public.practical_exam_submissions DROP CONSTRAINT IF EXISTS fk_cc_practical_exam_submissions_user_id_users;
ALTER TABLE public.practical_exam_submissions DROP CONSTRAINT IF EXISTS fk_cc_practical_exam_submissions_exam_id_practical_exams;
ALTER TABLE public.practical_exams DROP CONSTRAINT IF EXISTS fk_cc_practical_exams_created_by_users;
ALTER TABLE public.certificates DROP CONSTRAINT IF EXISTS fk_cc_certificates_user_id_users;
ALTER TABLE public.portfolio_projects DROP CONSTRAINT IF EXISTS fk_cc_portfolio_projects_project_id_projects;
ALTER TABLE public.portfolio_projects DROP CONSTRAINT IF EXISTS fk_cc_portfolio_projects_user_id_users;
ALTER TABLE public.event_progress DROP CONSTRAINT IF EXISTS fk_cc_event_progress_user_id_users;
ALTER TABLE public.pair_queue DROP CONSTRAINT IF EXISTS fk_cc_pair_queue_user_id_users;
ALTER TABLE public.study_group_members DROP CONSTRAINT IF EXISTS fk_cc_study_group_members_user_id_users;
ALTER TABLE public.study_group_members DROP CONSTRAINT IF EXISTS fk_cc_study_group_members_group_id_study_groups;
ALTER TABLE public.study_groups DROP CONSTRAINT IF EXISTS fk_cc_study_groups_owner_id_users;
ALTER TABLE public.bug_attempts DROP CONSTRAINT IF EXISTS fk_cc_bug_attempts_puzzle_id_bug_puzzles;
ALTER TABLE public.bug_attempts DROP CONSTRAINT IF EXISTS fk_cc_bug_attempts_user_id_users;
ALTER TABLE public.daily_missions DROP CONSTRAINT IF EXISTS fk_cc_daily_missions_user_id_users;
ALTER TABLE public.user_stats DROP CONSTRAINT IF EXISTS fk_cc_user_stats_user_id_users;
ALTER TABLE public.user_titles DROP CONSTRAINT IF EXISTS fk_cc_user_titles_user_id_users;
ALTER TABLE public.personal_notes DROP CONSTRAINT IF EXISTS fk_cc_personal_notes_user_id_users;
ALTER TABLE public.code_snippets DROP CONSTRAINT IF EXISTS fk_cc_code_snippets_user_id_users;
ALTER TABLE public.assignment_submissions DROP CONSTRAINT IF EXISTS fk_cc_assignment_submissions_user_id_users;
ALTER TABLE public.assignment_submissions DROP CONSTRAINT IF EXISTS fk_cc_assignment_submissions_assignment_id_assignments;
ALTER TABLE public.assignments DROP CONSTRAINT IF EXISTS fk_cc_assignments_class_id_classes;
ALTER TABLE public.class_members DROP CONSTRAINT IF EXISTS fk_cc_class_members_user_id_users;
ALTER TABLE public.class_members DROP CONSTRAINT IF EXISTS fk_cc_class_members_class_id_classes;
ALTER TABLE public.classes DROP CONSTRAINT IF EXISTS fk_cc_classes_teacher_id_users;
ALTER TABLE public.project_progress DROP CONSTRAINT IF EXISTS fk_cc_project_progress_project_id_projects;
ALTER TABLE public.project_progress DROP CONSTRAINT IF EXISTS fk_cc_project_progress_user_id_users;
ALTER TABLE public.daily_goals DROP CONSTRAINT IF EXISTS fk_cc_daily_goals_user_id_users;
ALTER TABLE public.xp_history DROP CONSTRAINT IF EXISTS fk_cc_xp_history_user_id_users;
ALTER TABLE public.daily_submissions DROP CONSTRAINT IF EXISTS fk_cc_daily_submissions_user_id_users;
ALTER TABLE public.user_badges DROP CONSTRAINT IF EXISTS fk_cc_user_badges_user_id_users;
ALTER TABLE public.practice_quiz_xp_rewards DROP CONSTRAINT IF EXISTS fk_cc_practice_quiz_xp_rewards_user_id_users;
ALTER TABLE public.quiz_attempts DROP CONSTRAINT IF EXISTS fk_cc_quiz_attempts_user_id_users;
ALTER TABLE public.user_progress DROP CONSTRAINT IF EXISTS fk_cc_user_progress_user_id_users;
DROP INDEX IF EXISTS public.ix_cc_practical_exam_submissions_user_submitted;
DROP INDEX IF EXISTS public.ix_cc_practical_exam_submissions_exam_submission;
DROP INDEX IF EXISTS public.ix_cc_practical_exams_creator_exam;
DROP INDEX IF EXISTS public.ix_cc_certificates_user_certificate;
DROP INDEX IF EXISTS public.ix_cc_portfolio_projects_project_user;
DROP INDEX IF EXISTS public.ix_cc_study_group_members_user_group;
DROP INDEX IF EXISTS public.ix_cc_study_groups_owner_group;
DROP INDEX IF EXISTS public.ix_cc_bug_attempts_puzzle_user;
DROP INDEX IF EXISTS public.ix_cc_personal_notes_user_title_note;
DROP INDEX IF EXISTS public.ix_cc_code_snippets_user_snippet;
DROP INDEX IF EXISTS public.ix_cc_assignment_submissions_user_assignment;
DROP INDEX IF EXISTS public.ix_cc_assignments_class_assignment;
DROP INDEX IF EXISTS public.ix_cc_class_members_user_class;
DROP INDEX IF EXISTS public.ix_cc_classes_teacher_class;
DROP INDEX IF EXISTS public.ix_cc_project_progress_project_user;
DROP INDEX IF EXISTS public.ix_cc_xp_history_user_id;
DROP INDEX IF EXISTS public.ix_cc_quiz_attempts_user_attempted;
COMMIT;
