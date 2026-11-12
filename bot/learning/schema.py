from __future__ import annotations

REQUIRED_FIELDS = {
    'id','title','description','stage','difficulty','introduction','learning_objectives',
    'terminology','explanation','syntax','syntax_breakdown','example1','example1_explanation',
    'example2','example2_explanation','practical_example','common_mistakes','beginner_tips',
    'exercise','practice_problem','expected_output','mastery_quiz','summary','next_lesson',
    'prerequisites','step_sequence','mastery_pass_score','mastery_question_count','review_threshold',
    'why_it_matters','guided_practice','independent_practice','debug_task','transfer_task',
    'assessment_contract','objective_assessment_map','test_cases','review_plan','quality_tags','content_version'
}


def validate_lesson(lesson: dict, language: str, position: int, total: int, ids: set[str] | None = None) -> list[str]:
    errors=[]
    missing=REQUIRED_FIELDS-set(lesson)
    if missing: errors.append(f"{lesson.get('id','<missing-id>')}: missing fields: {sorted(missing)}")
    lid=lesson.get('id','')
    prefix=f'{language}_'
    if not lid.startswith(prefix): errors.append(f'{lid}: ID must start with {prefix}')
    if not lesson.get('title','').strip(): errors.append(f'{lid}: empty title')
    if not lesson.get('description','').strip(): errors.append(f'{lid}: empty description')
    for field in ('learning_objectives','terminology','syntax_breakdown','common_mistakes','beginner_tips','step_sequence','guided_practice','quality_tags'):
        if not isinstance(lesson.get(field), list) or len(lesson.get(field)) < 3:
            errors.append(f'{lid}: {field} must contain at least 3 items')
    quiz=lesson.get('mastery_quiz')
    if not isinstance(quiz,list) or len(quiz) < 5:
        errors.append(f'{lid}: mastery_quiz must contain at least 5 questions')
    else:
        seen_questions=set()
        for qidx,q in enumerate(quiz,1):
            if not isinstance(q,(list,tuple)) or len(q)!=4:
                errors.append(f'{lid}: mastery question {qidx} must be (question, options, correct_index, explanation)')
                continue
            question,options,answer,explanation=q
            normalized=str(question).strip().lower()
            if normalized in seen_questions: errors.append(f'{lid}: duplicate mastery question {qidx}')
            seen_questions.add(normalized)
            if not str(question).strip(): errors.append(f'{lid}: mastery question {qidx} has no question')
            if not isinstance(options,(list,tuple)) or len(options)!=4: errors.append(f'{lid}: mastery question {qidx} must have 4 options')
            if not isinstance(answer,int) or not 0 <= answer < 4: errors.append(f'{lid}: mastery question {qidx} has invalid answer index')
            if not str(explanation).strip(): errors.append(f'{lid}: mastery question {qidx} has no explanation')
    if not isinstance(lesson.get('prerequisites'), list): errors.append(f'{lid}: prerequisites must be a list')
    if ids is not None:
        for dep in lesson.get('prerequisites', []):
            if dep not in ids: errors.append(f'{lid}: unknown prerequisite {dep}')

    if not str(lesson.get('why_it_matters','')).strip(): errors.append(f'{lid}: why_it_matters is empty')
    for field in ('independent_practice','debug_task','transfer_task'):
        if not str(lesson.get(field,'')).strip(): errors.append(f'{lid}: {field} is empty')
    contract=lesson.get('assessment_contract')
    if not isinstance(contract, dict): errors.append(f'{lid}: assessment_contract must be a dict')
    else:
        if contract.get('mastery_skills') != ['Core concept','Syntax & usage','Code reading','Debugging','Application']:
            errors.append(f'{lid}: assessment_contract mastery_skills are invalid')
        if contract.get('demonstration_required') is not True: errors.append(f'{lid}: practical demonstration requirement missing')
    if not isinstance(lesson.get('objective_assessment_map'), list) or len(lesson.get('objective_assessment_map',[])) != len(lesson.get('learning_objectives',[])):
        errors.append(f'{lid}: objective_assessment_map must map every learning objective')
    tests=lesson.get('test_cases')
    if not isinstance(tests,list) or len(tests) < 3 or any(not isinstance(t,dict) or not all(k in t for k in ('name','input','expected')) for t in tests):
        errors.append(f'{lid}: test_cases must contain at least 3 named cases with input and expected behavior')
    if not isinstance(lesson.get('review_plan'), dict): errors.append(f'{lid}: review_plan must be a dict')
    if lesson.get('content_version') != '3.4.0': errors.append(f'{lid}: content_version must be 3.4.0')

    if lesson.get('mastery_pass_score') != 4: errors.append(f'{lid}: mastery_pass_score must be 4/5')
    if lesson.get('mastery_question_count') != 5: errors.append(f'{lid}: mastery_question_count must be 5')
    if position < total-1 and not lesson.get('next_lesson'): errors.append(f'{lid}: missing next_lesson')
    return errors


def validate_curriculum(curriculum: list[dict], language: str) -> None:
    errors=[]
    ids=[x.get('id') for x in curriculum]
    titles=[x.get('title') for x in curriculum]
    idset=set(ids)
    for value, label in ((ids,'lesson ID'),(titles,'lesson title')):
        seen=set()
        for item in value:
            if item in seen: errors.append(f'{language}: duplicate {label}: {item}')
            seen.add(item)
    for i,lesson in enumerate(curriculum): errors.extend(validate_lesson(lesson,language,i,len(curriculum),idset))
    for i,lesson in enumerate(curriculum[:-1]):
        if lesson.get('next_lesson') != curriculum[i+1].get('title'):
            errors.append(f"{lesson.get('id')}: next_lesson does not point to curriculum[{i+1}]")
        expected = [] if i == 0 else [curriculum[i-1]['id']]
        if lesson.get('prerequisites') != expected:
            errors.append(f"{lesson.get('id')}: prerequisites must be {expected}")
    if curriculum and curriculum[0].get('prerequisites') != []:
        errors.append(f"{curriculum[0].get('id')}: first lesson cannot require a prerequisite")
    # Flag suspiciously generic practice/output content.
    for lesson in curriculum:
        if 'additional requirement related specifically to' in lesson.get('practice_problem','').lower():
            errors.append(f"{lesson.get('id')}: practice_problem still uses generic fallback wording")
        if 'your exact output depends on your chosen input' in lesson.get('expected_output','').lower():
            errors.append(f"{lesson.get('id')}: expected_output still uses generic fallback wording")
        if lesson.get('title','').lower() not in lesson.get('practice_problem','').lower():
            errors.append(f"{lesson.get('id')}: practice_problem must name its lesson topic")
        if lesson.get('title','').lower() not in lesson.get('why_it_matters','').lower():
            errors.append(f"{lesson.get('id')}: why_it_matters must be topic-specific")
    if errors: raise ValueError('Curriculum validation failed:\n'+'\n'.join(errors))
    return None
