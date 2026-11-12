-- NEW replacement migration; designed from current Step 2 source, not recovered history.
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

ALTER TABLE public.user_progress ADD CONSTRAINT fk_cc_user_progress_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.user_progress VALIDATE CONSTRAINT fk_cc_user_progress_user_id_users;

ALTER TABLE public.quiz_attempts ADD CONSTRAINT fk_cc_quiz_attempts_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.quiz_attempts VALIDATE CONSTRAINT fk_cc_quiz_attempts_user_id_users;

ALTER TABLE public.practice_quiz_xp_rewards ADD CONSTRAINT fk_cc_practice_quiz_xp_rewards_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.practice_quiz_xp_rewards VALIDATE CONSTRAINT fk_cc_practice_quiz_xp_rewards_user_id_users;

ALTER TABLE public.user_badges ADD CONSTRAINT fk_cc_user_badges_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.user_badges VALIDATE CONSTRAINT fk_cc_user_badges_user_id_users;

ALTER TABLE public.daily_submissions ADD CONSTRAINT fk_cc_daily_submissions_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.daily_submissions VALIDATE CONSTRAINT fk_cc_daily_submissions_user_id_users;

ALTER TABLE public.xp_history ADD CONSTRAINT fk_cc_xp_history_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.xp_history VALIDATE CONSTRAINT fk_cc_xp_history_user_id_users;

ALTER TABLE public.daily_goals ADD CONSTRAINT fk_cc_daily_goals_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.daily_goals VALIDATE CONSTRAINT fk_cc_daily_goals_user_id_users;

ALTER TABLE public.project_progress ADD CONSTRAINT fk_cc_project_progress_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.project_progress VALIDATE CONSTRAINT fk_cc_project_progress_user_id_users;

ALTER TABLE public.project_progress ADD CONSTRAINT fk_cc_project_progress_project_id_projects FOREIGN KEY (project_id) REFERENCES public.projects (project_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.project_progress VALIDATE CONSTRAINT fk_cc_project_progress_project_id_projects;

ALTER TABLE public.classes ADD CONSTRAINT fk_cc_classes_teacher_id_users FOREIGN KEY (teacher_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.classes VALIDATE CONSTRAINT fk_cc_classes_teacher_id_users;

ALTER TABLE public.class_members ADD CONSTRAINT fk_cc_class_members_class_id_classes FOREIGN KEY (class_id) REFERENCES public.classes (class_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.class_members VALIDATE CONSTRAINT fk_cc_class_members_class_id_classes;

ALTER TABLE public.class_members ADD CONSTRAINT fk_cc_class_members_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.class_members VALIDATE CONSTRAINT fk_cc_class_members_user_id_users;

ALTER TABLE public.assignments ADD CONSTRAINT fk_cc_assignments_class_id_classes FOREIGN KEY (class_id) REFERENCES public.classes (class_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.assignments VALIDATE CONSTRAINT fk_cc_assignments_class_id_classes;

ALTER TABLE public.assignment_submissions ADD CONSTRAINT fk_cc_assignment_submissions_assignment_id_assignments FOREIGN KEY (assignment_id) REFERENCES public.assignments (assignment_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.assignment_submissions VALIDATE CONSTRAINT fk_cc_assignment_submissions_assignment_id_assignments;

ALTER TABLE public.assignment_submissions ADD CONSTRAINT fk_cc_assignment_submissions_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.assignment_submissions VALIDATE CONSTRAINT fk_cc_assignment_submissions_user_id_users;

ALTER TABLE public.code_snippets ADD CONSTRAINT fk_cc_code_snippets_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.code_snippets VALIDATE CONSTRAINT fk_cc_code_snippets_user_id_users;

ALTER TABLE public.personal_notes ADD CONSTRAINT fk_cc_personal_notes_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.personal_notes VALIDATE CONSTRAINT fk_cc_personal_notes_user_id_users;

ALTER TABLE public.user_titles ADD CONSTRAINT fk_cc_user_titles_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.user_titles VALIDATE CONSTRAINT fk_cc_user_titles_user_id_users;

ALTER TABLE public.user_stats ADD CONSTRAINT fk_cc_user_stats_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.user_stats VALIDATE CONSTRAINT fk_cc_user_stats_user_id_users;

ALTER TABLE public.daily_missions ADD CONSTRAINT fk_cc_daily_missions_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.daily_missions VALIDATE CONSTRAINT fk_cc_daily_missions_user_id_users;

ALTER TABLE public.bug_attempts ADD CONSTRAINT fk_cc_bug_attempts_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.bug_attempts VALIDATE CONSTRAINT fk_cc_bug_attempts_user_id_users;

ALTER TABLE public.bug_attempts ADD CONSTRAINT fk_cc_bug_attempts_puzzle_id_bug_puzzles FOREIGN KEY (puzzle_id) REFERENCES public.bug_puzzles (puzzle_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.bug_attempts VALIDATE CONSTRAINT fk_cc_bug_attempts_puzzle_id_bug_puzzles;

ALTER TABLE public.study_groups ADD CONSTRAINT fk_cc_study_groups_owner_id_users FOREIGN KEY (owner_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.study_groups VALIDATE CONSTRAINT fk_cc_study_groups_owner_id_users;

ALTER TABLE public.study_group_members ADD CONSTRAINT fk_cc_study_group_members_group_id_study_groups FOREIGN KEY (group_id) REFERENCES public.study_groups (group_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.study_group_members VALIDATE CONSTRAINT fk_cc_study_group_members_group_id_study_groups;

ALTER TABLE public.study_group_members ADD CONSTRAINT fk_cc_study_group_members_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.study_group_members VALIDATE CONSTRAINT fk_cc_study_group_members_user_id_users;

ALTER TABLE public.pair_queue ADD CONSTRAINT fk_cc_pair_queue_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.pair_queue VALIDATE CONSTRAINT fk_cc_pair_queue_user_id_users;

ALTER TABLE public.event_progress ADD CONSTRAINT fk_cc_event_progress_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.event_progress VALIDATE CONSTRAINT fk_cc_event_progress_user_id_users;

ALTER TABLE public.portfolio_projects ADD CONSTRAINT fk_cc_portfolio_projects_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.portfolio_projects VALIDATE CONSTRAINT fk_cc_portfolio_projects_user_id_users;

ALTER TABLE public.portfolio_projects ADD CONSTRAINT fk_cc_portfolio_projects_project_id_projects FOREIGN KEY (project_id) REFERENCES public.projects (project_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.portfolio_projects VALIDATE CONSTRAINT fk_cc_portfolio_projects_project_id_projects;

ALTER TABLE public.certificates ADD CONSTRAINT fk_cc_certificates_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.certificates VALIDATE CONSTRAINT fk_cc_certificates_user_id_users;

ALTER TABLE public.practical_exams ADD CONSTRAINT fk_cc_practical_exams_created_by_users FOREIGN KEY (created_by) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.practical_exams VALIDATE CONSTRAINT fk_cc_practical_exams_created_by_users;

ALTER TABLE public.practical_exam_submissions ADD CONSTRAINT fk_cc_practical_exam_submissions_exam_id_practical_exams FOREIGN KEY (exam_id) REFERENCES public.practical_exams (exam_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.practical_exam_submissions VALIDATE CONSTRAINT fk_cc_practical_exam_submissions_exam_id_practical_exams;

ALTER TABLE public.practical_exam_submissions ADD CONSTRAINT fk_cc_practical_exam_submissions_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.practical_exam_submissions VALIDATE CONSTRAINT fk_cc_practical_exam_submissions_user_id_users;

ALTER TABLE public.attendance_records ADD CONSTRAINT fk_cc_attendance_records_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.attendance_records VALIDATE CONSTRAINT fk_cc_attendance_records_user_id_users;

ALTER TABLE public.lesson_mastery ADD CONSTRAINT fk_cc_lesson_mastery_user_id_users FOREIGN KEY (user_id) REFERENCES public.users (user_id) ON DELETE RESTRICT NOT VALID;
ALTER TABLE public.lesson_mastery VALIDATE CONSTRAINT fk_cc_lesson_mastery_user_id_users;

CREATE INDEX ix_cc_quiz_attempts_user_attempted ON public.quiz_attempts (user_id, attempted_at);

CREATE INDEX ix_cc_xp_history_user_id ON public.xp_history (user_id, id);

CREATE INDEX ix_cc_project_progress_project_user ON public.project_progress (project_id, user_id);

CREATE INDEX ix_cc_classes_teacher_class ON public.classes (teacher_id, class_id);

CREATE INDEX ix_cc_class_members_user_class ON public.class_members (user_id, class_id);

CREATE INDEX ix_cc_assignments_class_assignment ON public.assignments (class_id, assignment_id);

CREATE INDEX ix_cc_assignment_submissions_user_assignment ON public.assignment_submissions (user_id, assignment_id);

CREATE INDEX ix_cc_code_snippets_user_snippet ON public.code_snippets (user_id, snippet_id);

CREATE INDEX ix_cc_personal_notes_user_title_note ON public.personal_notes (user_id, title, note_id);

CREATE INDEX ix_cc_bug_attempts_puzzle_user ON public.bug_attempts (puzzle_id, user_id);

CREATE INDEX ix_cc_study_groups_owner_group ON public.study_groups (owner_id, group_id);

CREATE INDEX ix_cc_study_group_members_user_group ON public.study_group_members (user_id, group_id);

CREATE INDEX ix_cc_portfolio_projects_project_user ON public.portfolio_projects (project_id, user_id);

CREATE INDEX ix_cc_certificates_user_certificate ON public.certificates (user_id, certificate_id);

CREATE INDEX ix_cc_practical_exams_creator_exam ON public.practical_exams (created_by, exam_id);

CREATE INDEX ix_cc_practical_exam_submissions_exam_submission ON public.practical_exam_submissions (exam_id, submission_id);

CREATE INDEX ix_cc_practical_exam_submissions_user_submitted ON public.practical_exam_submissions (user_id, submitted_at);
