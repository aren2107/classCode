from __future__ import annotations

CPP_CURRICULUM = [ { 'id': 'cpp_01',
    'title': 'Programming Fundamentals',
    'description': 'Understand how C++ source code becomes an executable and how main(), statements, headers, '
                   'comments, and return values fit together.',
    'stage': 'Foundation',
    'difficulty': 'Beginner',
    'introduction': 'In this lesson you will learn **Programming Fundamentals**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what programming fundamentals means and why it exists.',
                             'Read and write the core syntax used for programming fundamentals.',
                             'Predict the behavior of a small programming fundamentals example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['source file', 'compiler', 'entry point', 'statement'],
    'explanation': 'Understand how C++ source code becomes an executable and how main(), statements, headers, '
                   'comments, and return values fit together. C++ syntax is shown with the standard library names used '
                   'in this lesson. Read the declaration from left to right: identify the type or template, the name, '
                   'the operation, and the terminating punctuation.',
    'syntax': '#include <iostream>\n'
              'using namespace std;\n'
              '\n'
              'int main() {\n'
              '    cout << "Hello, ClassCode!" << "\\n";\n'
              '    return 0;\n'
              '}',
    'syntax_breakdown': [ 'Focus on source file: identify what it represents and what role it plays in the statement.',
                          'Next inspect compiler: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '#include <iostream>\n'
                'using namespace std;\n'
                '\n'
                'int main() {\n'
                '    cout << "Hello, ClassCode!" << "\\n";\n'
                '    return 0;\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': '#include <iostream>\n'
                'using namespace std;\n'
                'int main() {\n'
                '    cout << "Name: Ren\\n";\n'
                '    cout << "Goal: Learn C++";\n'
                '    return 0;\n'
                '}',
    'example2_explanation': 'Change one meaningful input or rule related to programming fundamentals, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small programming fundamentals feature in a student or inventory program. Decide '
                         'what data enters the feature, what rule the feature applies, and what result it should '
                         'produce.',
    'common_mistakes': [ 'Memorizing source file syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make source file behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each source file before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Write a program that prints your name, school, and one programming goal on separate lines.',
    'practice_problem': '**Programming Fundamentals independent practice:** Write a program that prints your name, '
                        'school, and one programming goal on separate lines. You must also add one clearly different '
                        "variation and test it. Your work should demonstrate the lesson's main rule, not merely "
                        'reproduce Example 1.',
    'expected_output': '**Test contract for Programming Fundamentals:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'Programming Fundamentals: Which function is the normal C++ program entry point?',
                        ['main()', 'start()', 'run()', 'begin()'],
                        0,
                        'Execution begins in main().'],
                      [ 'What does #include <iostream> provide?',
                        [ 'Standard console stream facilities',
                          'A database connection',
                          'A GUI window',
                          'A compiler executable'],
                        0,
                        'iostream provides facilities such as cin and cout.'],
                      [ 'Why is a semicolon used after a statement such as return 0;?',
                        [ 'It terminates the statement',
                          'It starts a loop',
                          'It declares a class',
                          'It imports a library'],
                        0,
                        'The semicolon terminates the statement.'],
                      [ 'What does return 0; from main commonly communicate?',
                        ['Successful program termination', 'A request for input', 'A loop count', 'A new variable'],
                        0,
                        'Zero is conventionally used to indicate successful termination.'],
                      [ 'Which error category can the compiler usually catch before the program runs?',
                        [ 'Syntax/type errors',
                          'Every logic error',
                          'Every wrong business rule',
                          'Every performance problem'],
                        0,
                        'Compilation catches many syntax and type errors, but not every logic mistake.']],
    'summary': 'You should now be able to explain programming fundamentals, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Variables & Data Types',
    'rules': [ 'Name and trace the role of each source file before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the programming '
            'fundamentals exercise.',
    'extension': 'Add one realistic requirement to the programming fundamentals exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain programming fundamentals without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': [],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Programming Fundamentals gives you the foundation needed to read, change, and reason about a '
                      'program before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Programming Fundamentals** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Programming '
                         'Fundamentals**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Programming Fundamentals** task: Write a program that prints '
                            'your name, school, and one programming goal on separate lines. Then create one small '
                            'variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Programming Fundamentals** program that exhibits this common mistake: '
                  '**Memorizing source file syntax without being able to explain what changes in the program.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Programming Fundamentals** to a small real-world feature. Keep the same core rule, '
                     'but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what programming fundamentals means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for programming fundamentals.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small programming fundamentals example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Programming Fundamentals.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Programming Fundamentals without violating the '
                                  'stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Programming '
                                  'Fundamentals.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_02',
    'title': 'Variables & Data Types',
    'description': 'Learn how C++ represents numbers, characters, Boolean values, and text, and how a variable '
                   'declaration combines a type, name, and optional initial value.',
    'stage': 'Foundation',
    'difficulty': 'Beginner',
    'introduction': 'In this lesson you will learn **Variables & Data Types**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what variables & data types means and why it exists.',
                             'Read and write the core syntax used for variables & data types.',
                             'Predict the behavior of a small variables & data types example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['declaration', 'initialization', 'type', 'identifier'],
    'explanation': 'Learn how C++ represents numbers, characters, Boolean values, and text, and how a variable '
                   'declaration combines a type, name, and optional initial value. C++ syntax is shown with the '
                   'standard library names used in this lesson. Read the declaration from left to right: identify the '
                   'type or template, the name, the operation, and the terminating punctuation.',
    'syntax': 'int age = 18;\n'
              'double average = 91.5;\n'
              'char grade = static_cast<char>(65);\n'
              'bool enrolled = true;\n'
              'std::string name = "Alex";',
    'syntax_breakdown': [ 'Focus on declaration: identify what it represents and what role it plays in the statement.',
                          'Next inspect initialization: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '#include <iostream>\n'
                '#include <string>\n'
                'using namespace std;\n'
                '\n'
                'int main() {\n'
                '    int age = 18;\n'
                '    double average = 91.5;\n'
                '    char grade = static_cast<char>(65);\n'
                '    bool enrolled = true;\n'
                '    string name = "Alex";\n'
                '    cout << name << " " << age << " " << average << " " << grade << " " << enrolled;\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'unsigned int count = 12;\n'
                'long long population = 8000000LL;\n'
                'float ratio = 0.5f;\n'
                'cout << count << " " << population << " " << ratio;',
    'example2_explanation': 'Change one meaningful input or rule related to variables & data types, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small variables & data types feature in a student or inventory program. Decide '
                         'what data enters the feature, what rule the feature applies, and what result it should '
                         'produce.',
    'common_mistakes': [ 'Memorizing declaration syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make declaration behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each declaration before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Create a student profile using a sensible type for each piece of information and print it clearly.',
    'practice_problem': '**Variables & Data Types independent practice:** Create a student profile using a sensible '
                        'type for each piece of information and print it clearly. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Variables & Data Types:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'Variables & Data Types: Which type naturally stores a whole-number age?',
                        ['int', 'double', 'string', 'bool'],
                        0,
                        'A typical age is an integer.'],
                      [ 'Which type is suitable for 91.75?',
                        ['double', 'bool', 'char', 'int'],
                        0,
                        'double represents floating-point values.'],
                      [ 'Which type stores a single character such as A?',
                        ['char', 'string', 'bool', 'double'],
                        0,
                        'char stores one character.'],
                      [ 'What does static_cast<int>(9.8) produce?',
                        ['9', '9.8', '98', 'A compile-time error'],
                        0,
                        'The explicit conversion produces the integer value 9, discarding the fractional part.'],
                      [ 'Why can choosing an unsigned type be risky for values that may become negative?',
                        [ 'It cannot represent negative values',
                          'It always uses floating point',
                          'It stores text only',
                          'It prevents arithmetic'],
                        0,
                        'Unsigned integer types represent zero and positive values, not negative values.']],
    'summary': 'You should now be able to explain variables & data types, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Input & Output',
    'rules': [ 'Name and trace the role of each declaration before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the variables & data '
            'types exercise.',
    'extension': 'Add one realistic requirement to the variables & data types exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain variables & data types without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_01'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Variables & Data Types gives you the foundation needed to read, change, and reason about a '
                      'program before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Variables & Data Types** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Variables & Data '
                         'Types**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Variables & Data Types** task: Create a student profile using '
                            'a sensible type for each piece of information and print it clearly. Then create one small '
                            'variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Variables & Data Types** program that exhibits this common mistake: '
                  '**Memorizing declaration syntax without being able to explain what changes in the program.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Variables & Data Types** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what variables & data types means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for variables & data types.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small variables & data types example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Variables & Data Types.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Variables & Data Types without violating the '
                                  'stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Variables & '
                                  'Data Types.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_03',
    'title': 'Input & Output',
    'description': 'Build interactive console programs with cout, cin, getline, stream operators, and predictable '
                   'output formatting.',
    'stage': 'Foundation',
    'difficulty': 'Beginner',
    'introduction': 'In this lesson you will learn **Input & Output**, understand why it is useful, trace a focused '
                    'example, practice it with guidance, then solve an independent variation. You will finish by '
                    'proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what input & output means and why it exists.',
                             'Read and write the core syntax used for input & output.',
                             'Predict the behavior of a small input & output example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['stream', 'insertion operator', 'extraction operator', 'line input'],
    'explanation': 'Build interactive console programs with cout, cin, getline, stream operators, and predictable '
                   'output formatting. C++ syntax is shown with the standard library names used in this lesson. Read '
                   'the declaration from left to right: identify the type or template, the name, the operation, and '
                   'the terminating punctuation.',
    'syntax': 'int age;\n'
              'std::string name;\n'
              'cin >> age;\n'
              'cin.ignore();\n'
              'getline(cin, name);\n'
              'cout << name << " is " << age << " years old\\n";',
    'syntax_breakdown': [ 'Focus on stream: identify what it represents and what role it plays in the statement.',
                          'Next inspect insertion operator: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '#include <iostream>\n'
                '#include <string>\n'
                'using namespace std;\n'
                '\n'
                'int main() {\n'
                '    int age;\n'
                '    string name;\n'
                '    cin >> age;\n'
                '    cin.ignore();\n'
                '    getline(cin, name);\n'
                '    cout << name << " is " << age << " years old\\n";\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'string fullName;\n'
                'cout << "Name: ";\n'
                'getline(cin, fullName);\n'
                'cout << "Welcome, " << fullName << "!\\n";',
    'example2_explanation': 'Change one meaningful input or rule related to input & output, predict the result, and '
                            'only then run the program.',
    'practical_example': 'Imagine a small input & output feature in a student or inventory program. Decide what data '
                         'enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing stream syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make stream behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each stream before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Ask for a name, age, and favorite number, then display a three-line summary.',
    'practice_problem': '**Input & Output independent practice:** Ask for a name, age, and favorite number, then '
                        'display a three-line summary. You must also add one clearly different variation and test it. '
                        "Your work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Input & Output:** Run the program with a normal case, a boundary case, and '
                       'a misuse/invalid case when relevant. For each case, record the actual result and compare it '
                       'with the requirement. A correct submission must preserve the lesson rule and handle the '
                       'defined edge case safely.',
    'mastery_quiz': [ [ 'Input & Output: Which operator extracts input with cin?',
                        ['>>', '<<', '==', '::'],
                        0,
                        'The extraction operator >> reads from an input stream.'],
                      [ 'Which operator inserts output into cout?',
                        ['<<', '>>', '&&', '->'],
                        0,
                        'The insertion operator << sends values to cout.'],
                      [ 'Which function reads a whole line including spaces?',
                        ['getline', 'cinInt', 'readWord', 'lineIn'],
                        0,
                        'getline reads until the line delimiter.'],
                      [ 'What is a common issue after cin >> age before getline?',
                        [ 'A leftover newline may be consumed',
                          'age becomes a string',
                          'cout stops working',
                          'The compiler deletes the input'],
                        0,
                        'Token extraction can leave the newline for the following getline.'],
                      [ 'Why can \\n be preferred to endl for ordinary output?',
                        [ 'It avoids forcing a flush every time',
                          'It reads input',
                          'It creates a vector',
                          'It changes a type'],
                        0,
                        'A newline character does not inherently force a stream flush like endl does.']],
    'summary': 'You should now be able to explain input & output, recognize its syntax, trace the worked example, and '
               'use the concept in a small original program.',
    'next_lesson': 'Operators & Expressions',
    'rules': [ 'Name and trace the role of each stream before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the input & output '
            'exercise.',
    'extension': 'Add one realistic requirement to the input & output exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain input & output without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_02'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Input & Output matters because programs need a reliable way to receive and present data instead '
                      'of relying on hard-coded values.',
    'guided_practice': [ '1. Restate the goal of **Input & Output** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Input & Output**, '
                         'then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Input & Output** task: Ask for a name, age, and favorite '
                            'number, then display a three-line summary. Then create one small variation that changes '
                            'an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Input & Output** program that exhibits this common mistake: '
                  '**Memorizing stream syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Input & Output** to a small real-world feature. Keep the same core rule, but change '
                     'the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what input & output means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for input & output.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small input & output example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Input & Output.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Input & Output without violating the stated '
                                  'rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['input', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_04',
    'title': 'Operators & Expressions',
    'description': 'Use arithmetic, comparison, logical, assignment, increment, decrement, compound assignment, '
                   'ternary expressions, precedence, and associativity to compute results correctly.',
    'stage': 'Foundation',
    'difficulty': 'Beginner',
    'introduction': 'In this lesson you will learn **Operators & Expressions**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what operators & expressions means and why it exists.',
                             'Read and write the core syntax used for operators & expressions.',
                             'Predict the behavior of a small operators & expressions example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['operand', 'operator', 'precedence', 'expression'],
    'explanation': 'Use arithmetic, comparison, logical, assignment, increment, decrement, compound assignment, '
                   'ternary expressions, precedence, and associativity to compute results correctly. C++ syntax is '
                   'shown with the standard library names used in this lesson. Read the declaration from left to '
                   'right: identify the type or template, the name, the operation, and the terminating punctuation.',
    'syntax': 'int a = 17, b = 5;\nint remainder = a % b;\nb += 3;\nbool ready = (a > b) && (a < 30);',
    'syntax_breakdown': [ 'Focus on operand: identify what it represents and what role it plays in the statement.',
                          'Next inspect operator: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '#include <iostream>\n'
                'using namespace std;\n'
                '\n'
                'int main() {\n'
                '    int a = 17, b = 5;\n'
                '    int remainder = a % b;\n'
                '    b += 3;\n'
                '    bool ready = (a > b) && (a < 30);\n'
                '    cout << remainder << " " << b << " " << ready;\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'int a = 8, b = 3;\n'
                'cout << (a / b) << " " << (a % b) << "\\n";\n'
                'cout << ((a > b) ? "larger" : "smaller");',
    'example2_explanation': 'Change one meaningful input or rule related to operators & expressions, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small operators & expressions feature in a student or inventory program. Decide '
                         'what data enters the feature, what rule the feature applies, and what result it should '
                         'produce.',
    'common_mistakes': [ 'Memorizing operand syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make operand behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each operand before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Build a bill calculator that computes subtotal, tax, discount, and final total from numeric inputs.',
    'practice_problem': '**Operators & Expressions independent practice:** Build a bill calculator that computes '
                        'subtotal, tax, discount, and final total from numeric inputs. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Operators & Expressions:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'Operators & Expressions: What does % produce for integer operands?',
                        ['The remainder', 'The quotient only', 'A Boolean', 'A string'],
                        0,
                        'Modulo gives the remainder.'],
                      [ 'Which operator tests equality for primitive values?',
                        ['==', '=', '!=', '=>'],
                        0,
                        '== compares values; = assigns.'],
                      [ 'What does && represent?',
                        ['Logical AND', 'Bitwise NOT', 'Assignment', 'String concatenation only'],
                        0,
                        'Both operands must be true for && to be true.'],
                      [ 'What is the purpose of parentheses in an expression?',
                        [ 'They can make evaluation order explicit',
                          'They create a class',
                          'They allocate memory',
                          'They read input'],
                        0,
                        'Parentheses group operations and make intended precedence clear.'],
                      [ 'What does a += b mean?',
                        ['Add b to a and assign the result to a', 'Compare a and b', 'Create b', 'Divide a by b'],
                        0,
                        'Compound assignment updates the left-hand variable.']],
    'summary': 'You should now be able to explain operators & expressions, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'If / Else Decisions',
    'rules': [ 'Name and trace the role of each operand before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the operators & '
            'expressions exercise.',
    'extension': 'Add one realistic requirement to the operators & expressions exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain operators & expressions without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_03'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Operators & Expressions gives you the foundation needed to read, change, and reason about a '
                      'program before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Operators & Expressions** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Operators & '
                         'Expressions**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Operators & Expressions** task: Build a bill calculator that '
                            'computes subtotal, tax, discount, and final total from numeric inputs. Then create one '
                            'small variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Operators & Expressions** program that exhibits this common mistake: '
                  '**Memorizing operand syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Operators & Expressions** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what operators & expressions means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for operators & expressions.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small operators & expressions example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Operators & Expressions.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Operators & Expressions without violating the '
                                  'stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Operators & '
                                  'Expressions.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_05',
    'title': 'If / Else Decisions',
    'description': 'Translate real rules into if, else if, and else branches, including validation and boundary cases.',
    'stage': 'Foundation',
    'difficulty': 'Beginner',
    'introduction': 'In this lesson you will learn **If / Else Decisions**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what if / else decisions means and why it exists.',
                             'Read and write the core syntax used for if / else decisions.',
                             'Predict the behavior of a small if / else decisions example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['condition', 'branch', 'boundary', 'validation'],
    'explanation': 'Translate real rules into if, else if, and else branches, including validation and boundary cases. '
                   'C++ syntax is shown with the standard library names used in this lesson. Read the declaration from '
                   'left to right: identify the type or template, the name, the operation, and the terminating '
                   'punctuation.',
    'syntax': 'int score;\n'
              'cin >> score;\n'
              'if (score < 0 || score > 100) cout << "INVALID";\n'
              'else if (score >= 75) cout << "PASS";\n'
              'else cout << "FAIL";',
    'syntax_breakdown': [ 'Focus on condition: identify what it represents and what role it plays in the statement.',
                          'Next inspect branch: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '#include <iostream>\n'
                'using namespace std;\n'
                '\n'
                'int main() {\n'
                '    int score;\n'
                '    cin >> score;\n'
                '    if (score < 0 || score > 100) cout << "INVALID";\n'
                '    else if (score >= 75) cout << "PASS";\n'
                '    else cout << "FAIL";\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'int temperature;\n'
                'cin >> temperature;\n'
                'if (temperature >= 30) cout << "hot";\n'
                'else if (temperature >= 20) cout << "warm";\n'
                'else cout << "cool";',
    'example2_explanation': 'Change one meaningful input or rule related to if / else decisions, predict the result, '
                            'and only then run the program.',
    'practical_example': 'Imagine a small if / else decisions feature in a student or inventory program. Decide what '
                         'data enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing condition syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make condition behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each condition before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Read a score and classify it as INVALID, FAIL, PASS, or a higher distinction using clear boundaries.',
    'practice_problem': '**If / Else Decisions independent practice:** Read a score and classify it as INVALID, FAIL, '
                        'PASS, or a higher distinction using clear boundaries. You must also add one clearly different '
                        "variation and test it. Your work should demonstrate the lesson's main rule, not merely "
                        'reproduce Example 1.',
    'expected_output': '**Test contract for If / Else Decisions:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'If / Else Decisions: What does if control?',
                        [ 'Which branch executes when a condition is true',
                          'How memory is allocated',
                          'How files are opened',
                          'How classes are imported'],
                        0,
                        'if selects code based on a Boolean condition.'],
                      [ 'When does else run?',
                        [ 'When the preceding condition is false',
                          'Always',
                          'Only inside a loop',
                          'Only during compilation'],
                        0,
                        'else is the fallback branch.'],
                      [ 'Why test boundary values?',
                        [ 'They verify the branch changes at the intended threshold',
                          'They make code compile faster',
                          'They remove variables',
                          'They replace input'],
                        0,
                        'Boundary tests catch off-by-one and comparison mistakes.'],
                      [ 'Which expression checks a score is in the range 0..100?',
                        ['score >= 0 && score <= 100', 'score = 0 && 100', 'score < 0 || score > 100', 'score == 0'],
                        0,
                        'The first expression accepts every value from 0 through 100 inclusive.'],
                      [ 'What should invalid input usually do?',
                        [ 'Follow an explicit validation path',
                          'Silently corrupt state',
                          'Always crash',
                          'Skip all output'],
                        0,
                        'Validation should be deliberate and visible in the program logic.']],
    'summary': 'You should now be able to explain if / else decisions, recognize its syntax, trace the worked example, '
               'and use the concept in a small original program.',
    'next_lesson': 'Switch Statements',
    'rules': [ 'Name and trace the role of each condition before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the if / else decisions '
            'exercise.',
    'extension': 'Add one realistic requirement to the if / else decisions exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain if / else decisions without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_04'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'If / Else Decisions matters because real programs must choose different actions when data or '
                      'conditions change.',
    'guided_practice': [ '1. Restate the goal of **If / Else Decisions** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **If / Else '
                         'Decisions**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **If / Else Decisions** task: Read a score and classify it as '
                            'INVALID, FAIL, PASS, or a higher distinction using clear boundaries. Then create one '
                            'small variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **If / Else Decisions** program that exhibits this common mistake: '
                  '**Memorizing condition syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **If / Else Decisions** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what if / else decisions means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for if / else decisions.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small if / else decisions example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for If / Else Decisions.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for If / Else Decisions without violating the '
                                  'stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['decision', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_06',
    'title': 'Switch Statements',
    'description': 'Use switch when one expression selects among discrete cases, and understand case labels, break, '
                   'default, and fall-through.',
    'stage': 'Foundation',
    'difficulty': 'Beginner',
    'introduction': 'In this lesson you will learn **Switch Statements**, understand why it is useful, trace a focused '
                    'example, practice it with guidance, then solve an independent variation. You will finish by '
                    'proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what switch statements means and why it exists.',
                             'Read and write the core syntax used for switch statements.',
                             'Predict the behavior of a small switch statements example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['case', 'break', 'default', 'selection'],
    'explanation': 'Use switch when one expression selects among discrete cases, and understand case labels, break, '
                   'default, and fall-through. C++ syntax is shown with the standard library names used in this '
                   'lesson. Read the declaration from left to right: identify the type or template, the name, the '
                   'operation, and the terminating punctuation.',
    'syntax': 'int choice;\n'
              'cin >> choice;\n'
              'switch (choice) {\n'
              '    case 1: cout << "Add"; break;\n'
              '    case 2: cout << "View"; break;\n'
              '    default: cout << "Invalid";\n'
              '}',
    'syntax_breakdown': [ 'Focus on case: identify what it represents and what role it plays in the statement.',
                          'Next inspect break: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '#include <iostream>\n'
                'using namespace std;\n'
                '\n'
                'int main() {\n'
                '    int choice;\n'
                '    cin >> choice;\n'
                '    switch (choice) {\n'
                '        case 1: cout << "Add"; break;\n'
                '        case 2: cout << "View"; break;\n'
                '        default: cout << "Invalid";\n'
                '    }\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'char option;\n'
                'cin >> option;\n'
                'switch (option) {\n'
                '    case \'A\': cout << "Add"; break;\n'
                '    case \'Q\': cout << "Quit"; break;\n'
                '    default: cout << "Unknown";\n'
                '}',
    'example2_explanation': 'Change one meaningful input or rule related to switch statements, predict the result, and '
                            'only then run the program.',
    'practical_example': 'Imagine a small switch statements feature in a student or inventory program. Decide what '
                         'data enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing case syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make case behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each case before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Create a menu for four actions and handle an invalid option safely.',
    'practice_problem': '**Switch Statements independent practice:** Create a menu for four actions and handle an '
                        'invalid option safely. You must also add one clearly different variation and test it. Your '
                        "work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Switch Statements:** Run the program with a normal case, a boundary case, '
                       'and a misuse/invalid case when relevant. For each case, record the actual result and compare '
                       'it with the requirement. A correct submission must preserve the lesson rule and handle the '
                       'defined edge case safely.',
    'mastery_quiz': [ [ 'Switch Statements: What identifies a switch branch?',
                        ['case', 'loop', 'parameter', 'header'],
                        0,
                        'Each case labels a discrete selection.'],
                      [ 'Why is break commonly used in traditional switch statements?',
                        [ 'To stop execution from falling into the next case',
                          'To read input',
                          'To declare a variable',
                          'To allocate memory'],
                        0,
                        'break exits the switch after the selected case.'],
                      [ 'What is default for?',
                        [ 'The fallback when no case matches',
                          'The first case only',
                          'A loop condition',
                          'A return type'],
                        0,
                        'default handles unmatched values.'],
                      [ 'When is switch a good fit?',
                        [ 'A small set of discrete choices',
                          'A complex numeric range with many inequalities',
                          'Every loop',
                          'File buffering'],
                        0,
                        'switch is well suited to discrete options.'],
                      [ 'What is fall-through?',
                        [ 'Execution continuing into a following case',
                          'A compiler crash',
                          'A missing variable',
                          'A file closing'],
                        0,
                        'Without a break in traditional switch syntax, execution can continue into the next case.']],
    'summary': 'You should now be able to explain switch statements, recognize its syntax, trace the worked example, '
               'and use the concept in a small original program.',
    'next_lesson': 'Loops: for, while, do-while',
    'rules': [ 'Name and trace the role of each case before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the switch statements '
            'exercise.',
    'extension': 'Add one realistic requirement to the switch statements exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain switch statements without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_05'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Switch Statements matters because real programs must choose different actions when data or '
                      'conditions change.',
    'guided_practice': [ '1. Restate the goal of **Switch Statements** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Switch '
                         'Statements**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Switch Statements** task: Create a menu for four actions and '
                            'handle an invalid option safely. Then create one small variation that changes an input, '
                            'rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Switch Statements** program that exhibits this common mistake: '
                  '**Memorizing case syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Switch Statements** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what switch statements means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for switch statements.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small switch statements example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Switch Statements.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Switch Statements without violating the stated '
                                  'rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['decision', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_07',
    'title': 'Loops: for, while, do-while',
    'description': 'Control repetition with for, while, and do-while loops; understand initialization, condition, '
                   'update, termination, break, continue, and infinite-loop risks.',
    'stage': 'Foundation',
    'difficulty': 'Beginner',
    'introduction': 'In this lesson you will learn **Loops: for, while, do-while**, understand why it is useful, trace '
                    'a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what loops: for, while, do-while means and why it exists.',
                             'Read and write the core syntax used for loops: for, while, do-while.',
                             'Predict the behavior of a small loops: for, while, do-while example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['iteration', 'condition', 'counter', 'termination'],
    'explanation': 'Control repetition with for, while, and do-while loops; understand initialization, condition, '
                   'update, termination, break, continue, and infinite-loop risks. C++ syntax is shown with the '
                   'standard library names used in this lesson. Read the declaration from left to right: identify the '
                   'type or template, the name, the operation, and the terminating punctuation.',
    'syntax': 'for (int i = 1; i <= 5; ++i) {\n    cout << i << " ";\n}',
    'syntax_breakdown': [ 'Focus on iteration: identify what it represents and what role it plays in the statement.',
                          'Next inspect condition: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '#include <iostream>\n'
                'using namespace std;\n'
                '\n'
                'int main() {\n'
                '    for (int i = 1; i <= 5; ++i) cout << i << " ";\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'int i = 5;\nwhile (i > 0) {\n    cout << i << " ";\n    --i;\n}',
    'example2_explanation': 'Change one meaningful input or rule related to loops: for, while, do-while, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small loops: for, while, do-while feature in a student or inventory program. '
                         'Decide what data enters the feature, what rule the feature applies, and what result it '
                         'should produce.',
    'common_mistakes': [ 'Memorizing iteration syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make iteration behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each iteration before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Read N, print 1 through N, and calculate their sum. Test N=1 and N=0.',
    'practice_problem': '**Loops: for, while, do-while independent practice:** Read N, print 1 through N, and '
                        'calculate their sum. Test N=1 and N=0. You must also add one clearly different variation and '
                        "test it. Your work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Loops: for, while, do-while:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Loops: for, while, do-while: What are the three common parts of a for loop?',
                        [ 'Initialization, condition, update',
                          'Class, object, method',
                          'Input, file, package',
                          'Type, pointer, reference'],
                        0,
                        'A for loop typically contains initialization, continuation condition, and update.'],
                      [ 'What causes an infinite loop?',
                        [ 'The termination condition never becomes false',
                          'Using braces',
                          'Printing output',
                          'Using int'],
                        0,
                        'A loop needs progress toward termination.'],
                      [ 'What does continue do?',
                        [ 'Skip the rest of the current iteration',
                          'End the entire program',
                          'Create a function',
                          'Repeat the declaration'],
                        0,
                        'continue moves to the next iteration.'],
                      [ 'What does break do inside a loop?',
                        [ 'Exit the loop immediately',
                          'Restart the loop from zero',
                          'Declare a variable',
                          'Skip only one statement'],
                        0,
                        'break terminates the nearest loop.'],
                      [ 'Why test a loop with a tiny input first?',
                        [ 'It makes iteration counts easy to verify',
                          'It disables the compiler',
                          'It removes all edge cases',
                          'It guarantees performance'],
                        0,
                        'Small cases make off-by-one mistakes easier to see.']],
    'summary': 'You should now be able to explain loops: for, while, do-while, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Nested Loops & Patterns',
    'rules': [ 'Name and trace the role of each iteration before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the loops: for, while, '
            'do-while exercise.',
    'extension': 'Add one realistic requirement to the loops: for, while, do-while exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain loops: for, while, do-while without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_06'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Loops: for, while, do-while matters because repeated work should be expressed once and '
                      'controlled by clear stopping conditions.',
    'guided_practice': [ '1. Restate the goal of **Loops: for, while, do-while** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Loops: for, while, '
                         'do-while**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Loops: for, while, do-while** task: Read N, print 1 through N, '
                            'and calculate their sum. Test N=1 and N=0. Then create one small variation that changes '
                            'an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Loops: for, while, do-while** program that exhibits this common '
                  'mistake: **Memorizing iteration syntax without being able to explain what changes in the '
                  'program.**. Before changing code, identify the first incorrect value, state, control-flow decision, '
                  'or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Loops: for, while, do-while** to a small real-world feature. Keep the same core rule, '
                     'but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what loops: for, while, do-while means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for loops: for, while, do-while.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small loops: for, while, do-while example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Loops: for, while, do-while.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Loops: for, while, do-while without violating '
                                  'the stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['loop', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_08',
    'title': 'Nested Loops & Patterns',
    'description': 'Use an outer loop to control rows and an inner loop to control repeated work inside each row, '
                   'useful for tables and patterns.',
    'stage': 'Core Problem Solving',
    'difficulty': 'Beginner',
    'introduction': 'In this lesson you will learn **Nested Loops & Patterns**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what nested loops & patterns means and why it exists.',
                             'Read and write the core syntax used for nested loops & patterns.',
                             'Predict the behavior of a small nested loops & patterns example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['outer loop', 'inner loop', 'row', 'column'],
    'explanation': 'Use an outer loop to control rows and an inner loop to control repeated work inside each row, '
                   'useful for tables and patterns. C++ syntax is shown with the standard library names used in this '
                   'lesson. Read the declaration from left to right: identify the type or template, the name, the '
                   'operation, and the terminating punctuation.',
    'syntax': 'for (int row = 1; row <= 3; ++row) {\n'
              '    for (int col = 1; col <= 4; ++col) cout << "* ";\n'
              '    cout << "\\n";\n'
              '}',
    'syntax_breakdown': [ 'Focus on outer loop: identify what it represents and what role it plays in the statement.',
                          'Next inspect inner loop: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '#include <iostream>\n'
                'using namespace std;\n'
                '\n'
                'int main() {\n'
                '    for (int row = 1; row <= 3; ++row) {\n'
                '        for (int col = 1; col <= 4; ++col) cout << "* ";\n'
                '        cout << "\\n";\n'
                '    }\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'for (int r=1; r<=4; ++r) {\n    for (int c=1; c<=r; ++c) cout << "*";\n    cout << "\\n";\n}',
    'example2_explanation': 'Change one meaningful input or rule related to nested loops & patterns, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small nested loops & patterns feature in a student or inventory program. Decide '
                         'what data enters the feature, what rule the feature applies, and what result it should '
                         'produce.',
    'common_mistakes': [ 'Memorizing outer loop syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make outer loop behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each outer loop before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Read N and print an N by N multiplication table.',
    'practice_problem': '**Nested Loops & Patterns independent practice:** Read N and print an N by N multiplication '
                        'table. You must also add one clearly different variation and test it. Your work should '
                        "demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Nested Loops & Patterns:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'Nested Loops & Patterns: In a nested loop, what does the inner loop do?',
                        [ 'It runs as part of each outer-loop iteration',
                          'It runs only once for the whole program',
                          'It replaces the outer loop',
                          'It declares the outer variable'],
                        0,
                        'The inner loop is executed for each relevant outer-loop iteration.'],
                      [ 'For an N by N pattern, what commonly controls rows?',
                        ['The outer loop', 'The input stream only', 'The compiler', 'The return type'],
                        0,
                        'The outer loop commonly controls the rows.'],
                      [ 'What commonly controls columns inside a pattern?',
                        ['The inner loop', 'The class name', 'The file path', 'The exception handler'],
                        0,
                        'The inner loop commonly controls repeated work within one row.'],
                      [ 'Why can nested loops become O(n²)?',
                        [ 'One n-sized loop runs inside another n-sized loop',
                          'Because braces are slow',
                          'Because output is impossible',
                          'Because arrays are fixed'],
                        0,
                        'Two nested n-sized iterations can multiply to roughly n² work.'],
                      [ 'What is a useful pattern test?',
                        [ 'Test N=1, a small N, and a boundary case',
                          'Only test a huge N',
                          'Skip empty/small cases',
                          'Change the loop structure after every run'],
                        0,
                        'Small pattern sizes make row/column mistakes easy to see.']],
    'summary': 'You should now be able to explain nested loops & patterns, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Functions & Return Values',
    'rules': [ 'Name and trace the role of each outer loop before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the nested loops & '
            'patterns exercise.',
    'extension': 'Add one realistic requirement to the nested loops & patterns exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain nested loops & patterns without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_07'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Nested Loops & Patterns matters because repeated work should be expressed once and controlled '
                      'by clear stopping conditions.',
    'guided_practice': [ '1. Restate the goal of **Nested Loops & Patterns** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Nested Loops & '
                         'Patterns**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Nested Loops & Patterns** task: Read N and print an N by N '
                            'multiplication table. Then create one small variation that changes an input, rule, or '
                            'data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Nested Loops & Patterns** program that exhibits this common mistake: '
                  '**Memorizing outer loop syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Nested Loops & Patterns** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what nested loops & patterns means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for nested loops & patterns.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small nested loops & patterns example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Nested Loops & Patterns.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Nested Loops & Patterns without violating the '
                                  'stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['loop', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_09',
    'title': 'Functions & Return Values',
    'description': 'Turn repeated logic into named functions with parameters, return values, declarations, '
                   'definitions, and clear responsibilities.',
    'stage': 'Core Problem Solving',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Functions & Return Values**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what functions & return values means and why it exists.',
                             'Read and write the core syntax used for functions & return values.',
                             'Predict the behavior of a small functions & return values example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['parameter', 'argument', 'return type', 'caller'],
    'explanation': 'Turn repeated logic into named functions with parameters, return values, declarations, '
                   'definitions, and clear responsibilities. C++ syntax is shown with the standard library names used '
                   'in this lesson. Read the declaration from left to right: identify the type or template, the name, '
                   'the operation, and the terminating punctuation.',
    'syntax': 'int square(int n) {\n    return n * n;\n}\n\nint main() {\n    cout << square(6);\n}',
    'syntax_breakdown': [ 'Focus on parameter: identify what it represents and what role it plays in the statement.',
                          'Next inspect argument: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '#include <iostream>\n'
                'using namespace std;\n'
                '\n'
                'int square(int n) {\n'
                '    return n * n;\n'
                '}\n'
                '\n'
                'int main() {\n'
                '    cout << square(6);\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'int add(int a, int b) { return a + b; }\nint main() {\n    cout << add(7, 5);\n}',
    'example2_explanation': 'Change one meaningful input or rule related to functions & return values, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small functions & return values feature in a student or inventory program. Decide '
                         'what data enters the feature, what rule the feature applies, and what result it should '
                         'produce.',
    'common_mistakes': [ 'Memorizing parameter syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make parameter behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each parameter before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Create separate functions for add, subtract, multiply, and safe division.',
    'practice_problem': '**Functions & Return Values independent practice:** Create separate functions for add, '
                        'subtract, multiply, and safe division. You must also add one clearly different variation and '
                        "test it. Your work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Functions & Return Values:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Functions & Return Values: What is a parameter?',
                        [ 'A named input in a function or method declaration',
                          'The returned value only',
                          'A compiler flag',
                          'A file path'],
                        0,
                        'Parameters describe values a caller can supply.'],
                      [ 'What is an argument?',
                        ['The value supplied when calling a function', 'The return type', 'A class name', 'A comment'],
                        0,
                        'Arguments are the actual values passed to parameters.'],
                      [ 'Why use a return value?',
                        [ 'To send a computed result back to the caller',
                          'To create a loop',
                          'To import a library',
                          'To delete a variable'],
                        0,
                        'A return value lets the caller use the result.'],
                      [ 'What does overloading mean?',
                        [ 'Same function/method name with different parameter lists',
                          'Changing only comments',
                          'Changing only the return type',
                          'Creating a new package'],
                        0,
                        'Overloads differ by their parameter lists.'],
                      [ 'What is a good function responsibility?',
                        [ 'One clear job',
                          'Every job in the whole program',
                          'Only printing comments',
                          'Changing unrelated global state'],
                        0,
                        'Focused functions are easier to test and reuse.']],
    'summary': 'You should now be able to explain functions & return values, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Scope, Parameters & References',
    'rules': [ 'Name and trace the role of each parameter before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the functions & return '
            'values exercise.',
    'extension': 'Add one realistic requirement to the functions & return values exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain functions & return values without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_08'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Functions & Return Values matters because focused functions or methods make behavior reusable, '
                      'testable, and easier to debug.',
    'guided_practice': [ '1. Restate the goal of **Functions & Return Values** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Functions & Return '
                         'Values**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Functions & Return Values** task: Create separate functions '
                            'for add, subtract, multiply, and safe division. Then create one small variation that '
                            'changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Functions & Return Values** program that exhibits this common mistake: '
                  '**Memorizing parameter syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Functions & Return Values** to a small real-world feature. Keep the same core rule, '
                     'but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what functions & return values means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for functions & return values.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small functions & return values example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Functions & Return Values.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Functions & Return Values without violating '
                                  'the stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['function', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_10',
    'title': 'Scope, Parameters & References',
    'description': 'Understand local scope, parameter scope, pass-by-value, pass-by-reference, const references, and '
                   'why function interfaces matter.',
    'stage': 'Core Problem Solving',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Scope, Parameters & References**, understand why it is useful, '
                    'trace a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what scope, parameters & references means and why it exists.',
                             'Read and write the core syntax used for scope, parameters & references.',
                             'Predict the behavior of a small scope, parameters & references example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['scope', 'parameter', 'alias', 'lifetime'],
    'explanation': 'Understand local scope, parameter scope, pass-by-value, pass-by-reference, const references, and '
                   'why function interfaces matter. C++ syntax is shown with the standard library names used in this '
                   'lesson. Read the declaration from left to right: identify the type or template, the name, the '
                   'operation, and the terminating punctuation.',
    'syntax': 'void addBonus(int& score) {\n'
              '    score += 5;\n'
              '}\n'
              '\n'
              'int main() {\n'
              '    int score = 70;\n'
              '    addBonus(score);\n'
              '    cout << score;\n'
              '}',
    'syntax_breakdown': [ 'Focus on scope: identify what it represents and what role it plays in the statement.',
                          'Next inspect parameter: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '#include <iostream>\n'
                'using namespace std;\n'
                '\n'
                'void addBonus(int& score) {\n'
                '    score += 5;\n'
                '}\n'
                '\n'
                'int main() {\n'
                '    int score = 70;\n'
                '    addBonus(score);\n'
                '    cout << score;\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'int score = 70;\n{\n    int bonus = 5;\n    score += bonus;\n}\ncout << score;',
    'example2_explanation': 'Change one meaningful input or rule related to scope, parameters & references, predict '
                            'the result, and only then run the program.',
    'practical_example': 'Imagine a small scope, parameters & references feature in a student or inventory program. '
                         'Decide what data enters the feature, what rule the feature applies, and what result it '
                         'should produce.',
    'common_mistakes': [ 'Memorizing scope syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make scope behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each scope before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Write one function that modifies a caller variable by reference and another that reads a large string '
                'through const reference.',
    'practice_problem': '**Scope, Parameters & References independent practice:** Write one function that modifies a '
                        'caller variable by reference and another that reads a large string through const reference. '
                        'You must also add one clearly different variation and test it. Your work should demonstrate '
                        "the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Scope, Parameters & References:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Scope, Parameters & References: What is a C++ reference?',
                        [ 'An alias for an existing object',
                          'A new object by default',
                          'A file handle',
                          'A class definition'],
                        0,
                        'A reference aliases an existing object.'],
                      [ 'Why use const T& for a large read-only object?',
                        [ 'Avoid copying while preventing modification through the reference',
                          'Force a heap allocation',
                          'Delete the object',
                          'Create a thread'],
                        0,
                        'A const reference can avoid a copy while providing read-only access.'],
                      [ 'Can a reference normally be reseated to another object?',
                        ['No', 'Yes with =', 'Only inside loops', 'Only for strings'],
                        0,
                        'A reference remains bound to the object it refers to.'],
                      [ 'What is pass-by-reference useful for?',
                        [ 'Allowing a function to observe or modify caller-owned state',
                          'Always copying values',
                          'Creating files',
                          'Changing the compiler'],
                        0,
                        'Non-const references can modify the caller’s object.'],
                      [ 'What should you prefer when you do not need mutation?',
                        [ 'A const reference where appropriate',
                          'A global pointer',
                          'A raw owning pointer',
                          'An uninitialized reference'],
                        0,
                        'Const references communicate read-only intent.']],
    'summary': 'You should now be able to explain scope, parameters & references, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Arrays',
    'rules': [ 'Name and trace the role of each scope before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the scope, parameters & '
            'references exercise.',
    'extension': 'Add one realistic requirement to the scope, parameters & references exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain scope, parameters & references without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_09'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Scope, Parameters & References matters because C++ programs must reason carefully about '
                      'references, ownership, lifetime, and resource safety.',
    'guided_practice': [ '1. Restate the goal of **Scope, Parameters & References** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Scope, Parameters '
                         '& References**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Scope, Parameters & References** task: Write one function that '
                            'modifies a caller variable by reference and another that reads a large string through '
                            'const reference. Then create one small variation that changes an input, rule, or data '
                            'case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Scope, Parameters & References** program that exhibits this common '
                  'mistake: **Memorizing scope syntax without being able to explain what changes in the program.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Scope, Parameters & References** to a small real-world feature. Keep the same core '
                     'rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what scope, parameters & references means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for scope, parameters & '
                                                 'references.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small scope, parameters & references '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Scope, Parameters & References.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Scope, Parameters & References without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Scope, '
                                  'Parameters & References.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['memory', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_11',
    'title': 'Arrays',
    'description': 'Store a fixed number of same-type values, access them by zero-based index, traverse them, and '
                   'reason about bounds.',
    'stage': 'Core Problem Solving',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Arrays**, understand why it is useful, trace a focused example, '
                    'practice it with guidance, then solve an independent variation. You will finish by proving your '
                    'understanding through concept, syntax, code-reading, debugging, and application checks.',
    'learning_objectives': [ 'Explain what arrays means and why it exists.',
                             'Read and write the core syntax used for arrays.',
                             'Predict the behavior of a small arrays example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['index', 'element', 'length', 'traversal'],
    'explanation': 'Store a fixed number of same-type values, access them by zero-based index, traverse them, and '
                   'reason about bounds. C++ syntax is shown with the standard library names used in this lesson. Read '
                   'the declaration from left to right: identify the type or template, the name, the operation, and '
                   'the terminating punctuation.',
    'syntax': 'int scores[5] = {80, 92, 75, 88, 95};\n'
              'int total = 0;\n'
              'for (int score : scores) total += score;\n'
              'cout << total;',
    'syntax_breakdown': [ 'Focus on index: identify what it represents and what role it plays in the statement.',
                          'Next inspect element: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '#include <iostream>\n'
                'using namespace std;\n'
                '\n'
                'int main() {\n'
                '    int scores[5] = {80, 92, 75, 88, 95};\n'
                '    int total = 0;\n'
                '    for (int score : scores) total += score;\n'
                '    cout << total;\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'int values[] = {4, 8, 15, 16, 23};\nfor (int i = 0; i < 5; ++i) {\n    cout << values[i] << " ";\n}',
    'example2_explanation': 'Change one meaningful input or rule related to arrays, predict the result, and only then '
                            'run the program.',
    'practical_example': 'Imagine a small arrays feature in a student or inventory program. Decide what data enters '
                         'the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing index syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make index behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each index before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Read five scores into an array and report total, average, highest, and lowest.',
    'practice_problem': '**Arrays independent practice:** Read five scores into an array and report total, average, '
                        'highest, and lowest. You must also add one clearly different variation and test it. Your work '
                        "should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Arrays:** Run the program with a normal case, a boundary case, and a '
                       'misuse/invalid case when relevant. For each case, record the actual result and compare it with '
                       'the requirement. A correct submission must preserve the lesson rule and handle the defined '
                       'edge case safely.',
    'mastery_quiz': [ [ 'Arrays: What is the first index of a normal C++ or Java array?',
                        ['0', '1', '-1', 'Depends on the compiler'],
                        0,
                        'Array indexing is zero-based.'],
                      [ 'What should you check before accessing an array index?',
                        [ 'That the index is within valid bounds',
                          'That the index is a string',
                          'That the array is global',
                          'That the loop is infinite'],
                        0,
                        'Out-of-range access is a common bug.'],
                      [ 'What does traversal mean?',
                        [ 'Visiting elements systematically',
                          'Deleting the array',
                          'Compiling twice',
                          'Changing the type'],
                        0,
                        'Traversal processes the elements one by one or by a defined pattern.'],
                      [ 'Why are arrays fixed-size?',
                        [ 'Their length is established as part of the array object',
                          'They cannot store numbers',
                          'They are files',
                          'They are always sorted'],
                        0,
                        'A normal array has a fixed number of elements.'],
                      [ 'What is a 2D array commonly useful for?',
                        ['Rows and columns', 'Only text input', 'Network sockets', 'Exception handling'],
                        0,
                        'Two-dimensional arrays naturally model grids and tables.']],
    'summary': 'You should now be able to explain arrays, recognize its syntax, trace the worked example, and use the '
               'concept in a small original program.',
    'next_lesson': 'Strings & Text Processing',
    'rules': [ 'Name and trace the role of each index before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the arrays exercise.',
    'extension': 'Add one realistic requirement to the arrays exercise while keeping the original behavior correct.',
    'learning_checks': [ 'Can I explain arrays without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_10'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Arrays matters because indexed data appears throughout algorithms and application code.',
    'guided_practice': [ '1. Restate the goal of **Arrays** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Arrays**, then '
                         'change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Arrays** task: Read five scores into an array and report '
                            'total, average, highest, and lowest. Then create one small variation that changes an '
                            'input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Arrays** program that exhibits this common mistake: **Memorizing index '
                  'syntax without being able to explain what changes in the program.**. Before changing code, identify '
                  'the first incorrect value, state, control-flow decision, or ownership assumption; then explain the '
                  'fix in one sentence.',
    'transfer_task': 'Transfer **Arrays** to a small real-world feature. Keep the same core rule, but change the '
                     'context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what arrays means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for arrays.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small arrays example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Arrays.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Arrays without violating the stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['array', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_12',
    'title': 'Strings & Text Processing',
    'description': 'Use std::string for text, compare and concatenate strings, inspect characters, search for '
                   'substrings, and read complete lines.',
    'stage': 'Core Problem Solving',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Strings & Text Processing**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what strings & text processing means and why it exists.',
                             'Read and write the core syntax used for strings & text processing.',
                             'Predict the behavior of a small strings & text processing example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['string', 'character', 'substring', 'search'],
    'explanation': 'Use std::string for text, compare and concatenate strings, inspect characters, search for '
                   'substrings, and read complete lines. C++ syntax is shown with the standard library names used in '
                   'this lesson. Read the declaration from left to right: identify the type or template, the name, the '
                   'operation, and the terminating punctuation.',
    'syntax': 'std::string name = "Ada";\n'
              'string message = "Hello, " + name;\n'
              'cout << message.length() << "\\n";\n'
              'cout << message.find("Ada");',
    'syntax_breakdown': [ 'Focus on string: identify what it represents and what role it plays in the statement.',
                          'Next inspect character: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '#include <iostream>\n'
                '#include <string>\n'
                'using namespace std;\n'
                '\n'
                'int main() {\n'
                '    string name = "Ada";\n'
                '    string message = "Hello, " + name;\n'
                '    cout << message.length() << "\\n";\n'
                '    cout << message.find("Ada");\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'string text = "ClassCode";\nif (text.find("Code") != string::npos) {\n    cout << "found";\n}',
    'example2_explanation': 'Change one meaningful input or rule related to strings & text processing, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small strings & text processing feature in a student or inventory program. Decide '
                         'what data enters the feature, what rule the feature applies, and what result it should '
                         'produce.',
    'common_mistakes': [ 'Memorizing string syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make string behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each string before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Read a full sentence and count its characters and occurrences of a chosen word.',
    'practice_problem': '**Strings & Text Processing independent practice:** Read a full sentence and count its '
                        'characters and occurrences of a chosen word. You must also add one clearly different '
                        "variation and test it. Your work should demonstrate the lesson's main rule, not merely "
                        'reproduce Example 1.',
    'expected_output': '**Test contract for Strings & Text Processing:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Strings & Text Processing: What does string length tell you?',
                        [ 'How many characters/elements are in the text',
                          'How many words must be printed',
                          'The memory address only',
                          'The compiler version'],
                        0,
                        'Length describes the number of characters/elements.'],
                      [ 'Why is whole-line input important?',
                        [ 'It preserves spaces within a line',
                          'It converts all text to integers',
                          'It disables validation',
                          'It creates an array'],
                        0,
                        'Token input stops at whitespace; line input can preserve spaces.'],
                      [ 'What does a search such as find/contains answer?',
                        [ 'Whether or where text occurs',
                          'Whether a loop compiled',
                          'Whether a class is abstract',
                          'Whether a file is executable'],
                        0,
                        'Search operations inspect text for a target.'],
                      [ 'Why should empty strings be tested?',
                        [ 'They expose assumptions about available characters',
                          'They always crash',
                          'They are never valid',
                          'They remove memory'],
                        0,
                        'Empty text is a normal edge case.'],
                      [ 'What is string concatenation?',
                        ['Combining text values', 'Sorting numbers', 'Opening a file', 'Creating a thread'],
                        0,
                        'Concatenation joins strings into a larger text value.']],
    'summary': 'You should now be able to explain strings & text processing, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Vectors',
    'rules': [ 'Name and trace the role of each string before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the strings & text '
            'processing exercise.',
    'extension': 'Add one realistic requirement to the strings & text processing exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain strings & text processing without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_11'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Strings & Text Processing matters because user-facing programs constantly process names, '
                      'messages, commands, and other text.',
    'guided_practice': [ '1. Restate the goal of **Strings & Text Processing** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Strings & Text '
                         'Processing**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Strings & Text Processing** task: Read a full sentence and '
                            'count its characters and occurrences of a chosen word. Then create one small variation '
                            'that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Strings & Text Processing** program that exhibits this common mistake: '
                  '**Memorizing string syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Strings & Text Processing** to a small real-world feature. Keep the same core rule, '
                     'but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what strings & text processing means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for strings & text processing.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small strings & text processing example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Strings & Text Processing.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Strings & Text Processing without violating '
                                  'the stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['string', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_13',
    'title': 'Vectors',
    'description': 'Use std::vector for a resizable sequence, including push_back, size, indexing, iteration, erase, '
                   'and capacity-related thinking.',
    'stage': 'Core Problem Solving',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Vectors**, understand why it is useful, trace a focused example, '
                    'practice it with guidance, then solve an independent variation. You will finish by proving your '
                    'understanding through concept, syntax, code-reading, debugging, and application checks.',
    'learning_objectives': [ 'Explain what vectors means and why it exists.',
                             'Read and write the core syntax used for vectors.',
                             'Predict the behavior of a small vectors example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['vector', 'size', 'capacity', 'iterator'],
    'explanation': 'Use std::vector for a resizable sequence, including push_back, size, indexing, iteration, erase, '
                   'and capacity-related thinking. C++ syntax is shown with the standard library names used in this '
                   'lesson. Read the declaration from left to right: identify the type or template, the name, the '
                   'operation, and the terminating punctuation.',
    'syntax': 'vector<int> scores;\n'
              'scores.push_back(85);\n'
              'scores.push_back(92);\n'
              'for (int x : scores) cout << x << " ";',
    'syntax_breakdown': [ 'Focus on vector: identify what it represents and what role it plays in the statement.',
                          'Next inspect size: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'vector<int> scores;\n'
                'scores.push_back(85);\n'
                'scores.push_back(92);\n'
                'for (int x : scores) cout << x << " ";',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'vector<string> names{"Ren", "Mika"};\n'
                'names.erase(names.begin());\n'
                'for (const auto& name : names) cout << name;',
    'example2_explanation': 'Change one meaningful input or rule related to vectors, predict the result, and only then '
                            'run the program.',
    'practical_example': 'Imagine a small vectors feature in a student or inventory program. Decide what data enters '
                         'the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing vector syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make vector behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each vector before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Build a score list that accepts values until -1, then prints average and removes one selected value.',
    'practice_problem': '**Vectors independent practice:** Build a score list that accepts values until -1, then '
                        'prints average and removes one selected value. You must also add one clearly different '
                        "variation and test it. Your work should demonstrate the lesson's main rule, not merely "
                        'reproduce Example 1.',
    'expected_output': '**Test contract for Vectors:** Run the program with a normal case, a boundary case, and a '
                       'misuse/invalid case when relevant. For each case, record the actual result and compare it with '
                       'the requirement. A correct submission must preserve the lesson rule and handle the defined '
                       'edge case safely.',
    'mastery_quiz': [ [ 'Vectors: Why use a resizable sequence instead of a fixed array?',
                        [ 'The collection can grow and shrink as needed',
                          'It prevents indexing',
                          'It stores only booleans',
                          'It removes all memory use'],
                        0,
                        'Resizable sequences adapt to changing collection size.'],
                      [ 'What operation adds an item?',
                        ['push_back/add', 'compile', 'catch', 'throw'],
                        0,
                        'C++ vector uses push_back; Java ArrayList uses add.'],
                      [ 'What operation reports the number of stored items?',
                        ['size', 'capacity-only', 'length-of-file', 'countLoops'],
                        0,
                        'size reports the current number of elements.'],
                      [ 'Why should removal logic consider indexes?',
                        [ 'Removing an item can shift later elements',
                          'Removal changes the programming language',
                          'Indexes become strings',
                          'Vectors cannot remove'],
                        0,
                        'Sequence removal can change positions.'],
                      [ 'What is a useful empty-collection test?',
                        [ 'Verify the program handles zero elements safely',
                          'Always crash',
                          'Assume index 0 exists',
                          'Skip all validation'],
                        0,
                        'Empty collections are a common boundary case.']],
    'summary': 'You should now be able to explain vectors, recognize its syntax, trace the worked example, and use the '
               'concept in a small original program.',
    'next_lesson': 'Structs & Records',
    'rules': [ 'Name and trace the role of each vector before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the vectors exercise.',
    'extension': 'Add one realistic requirement to the vectors exercise while keeping the original behavior correct.',
    'learning_checks': [ 'Can I explain vectors without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_12'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Vectors matters because programs often need to store, find, update, and process groups of '
                      'related values.',
    'guided_practice': [ '1. Restate the goal of **Vectors** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Vectors**, then '
                         'change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Vectors** task: Build a score list that accepts values until '
                            '-1, then prints average and removes one selected value. Then create one small variation '
                            'that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Vectors** program that exhibits this common mistake: **Memorizing '
                  'vector syntax without being able to explain what changes in the program.**. Before changing code, '
                  'identify the first incorrect value, state, control-flow decision, or ownership assumption; then '
                  'explain the fix in one sentence.',
    'transfer_task': 'Transfer **Vectors** to a small real-world feature. Keep the same core rule, but change the '
                     'context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what vectors means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for vectors.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small vectors example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Vectors.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Vectors without violating the stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['collection', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_14',
    'title': 'Structs & Records',
    'description': 'Group related fields into a named record with struct and use collections of records to model real '
                   'data.',
    'stage': 'Core Problem Solving',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Structs & Records**, understand why it is useful, trace a focused '
                    'example, practice it with guidance, then solve an independent variation. You will finish by '
                    'proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what structs & records means and why it exists.',
                             'Read and write the core syntax used for structs & records.',
                             'Predict the behavior of a small structs & records example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['member', 'record', 'aggregate', 'object'],
    'explanation': 'Group related fields into a named record with struct and use collections of records to model real '
                   'data. C++ syntax is shown with the standard library names used in this lesson. Read the '
                   'declaration from left to right: identify the type or template, the name, the operation, and the '
                   'terminating punctuation.',
    'syntax': 'struct Student {\n'
              '    std::string name;\n'
              '    int age;\n'
              '    double grade;\n'
              '};\n'
              '\n'
              'Student s{"Mika", 18, 91.5};',
    'syntax_breakdown': [ 'Focus on member: identify what it represents and what role it plays in the statement.',
                          'Next inspect record: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'struct Student {\n'
                '    std::string name;\n'
                '    int age;\n'
                '    double grade;\n'
                '};\n'
                '\n'
                'Student s{"Mika", 18, 91.5};',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'struct Product { std::string name; double price; };\n'
                'Product item{"Keyboard", 999.0};\n'
                'cout << item.name << " " << item.price;',
    'example2_explanation': 'Change one meaningful input or rule related to structs & records, predict the result, and '
                            'only then run the program.',
    'practical_example': 'Imagine a small structs & records feature in a student or inventory program. Decide what '
                         'data enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing member syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make member behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each member before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Create a Student record and store several students in a vector, then print the highest grade.',
    'practice_problem': '**Structs & Records independent practice:** Create a Student record and store several '
                        'students in a vector, then print the highest grade. You must also add one clearly different '
                        "variation and test it. Your work should demonstrate the lesson's main rule, not merely "
                        'reproduce Example 1.',
    'expected_output': '**Test contract for Structs & Records:** Run the program with a normal case, a boundary case, '
                       'and a misuse/invalid case when relevant. For each case, record the actual result and compare '
                       'it with the requirement. A correct submission must preserve the lesson rule and handle the '
                       'defined edge case safely.',
    'mastery_quiz': [ [ 'Structs & Records: What is the main design idea in Structs & Records?',
                        [ 'Organizing data and behavior with appropriate object relationships',
                          'Replacing all loops',
                          'Reading files only',
                          'Changing compiler flags'],
                        0,
                        'The lesson focuses on object structure and behavior.'],
                      [ 'What does encapsulation protect?',
                        [ 'Object invariants and implementation details',
                          'The compiler executable',
                          'Only comments',
                          'The network cable'],
                        0,
                        'Encapsulation controls how state is accessed and changed.'],
                      [ 'Why use composition?',
                        [ 'To build a larger object from focused components',
                          'To make every class a subclass',
                          'To avoid all objects',
                          'To disable methods'],
                        0,
                        'Composition models has-a relationships.'],
                      [ 'What does polymorphism allow?',
                        [ 'Common code to work with different concrete implementations',
                          'Every object to have the same state',
                          'Loops to become functions',
                          'Files to become classes'],
                        0,
                        'Polymorphism lets a common interface select behavior appropriate to the object.'],
                      [ 'What makes a constructor important?',
                        [ 'It establishes valid initial object state',
                          'It returns an int',
                          'It creates a package',
                          'It sorts fields'],
                        0,
                        'Constructors establish object state when instances are created.']],
    'summary': 'You should now be able to explain structs & records, recognize its syntax, trace the worked example, '
               'and use the concept in a small original program.',
    'next_lesson': 'References',
    'rules': [ 'Name and trace the role of each member before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the structs & records '
            'exercise.',
    'extension': 'Add one realistic requirement to the structs & records exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain structs & records without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_13'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Structs & Records gives you the foundation needed to read, change, and reason about a program '
                      'before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Structs & Records** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Structs & '
                         'Records**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Structs & Records** task: Create a Student record and store '
                            'several students in a vector, then print the highest grade. Then create one small '
                            'variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Structs & Records** program that exhibits this common mistake: '
                  '**Memorizing member syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Structs & Records** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what structs & records means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for structs & records.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small structs & records example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Structs & Records.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Structs & Records without violating the stated '
                                  'rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Structs & '
                                  'Records.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_15',
    'title': 'References',
    'description': 'Treat a reference as an alias to an existing object and use it to avoid copies or intentionally '
                   'modify caller-owned state.',
    'stage': 'Data & Design',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **References**, understand why it is useful, trace a focused '
                    'example, practice it with guidance, then solve an independent variation. You will finish by '
                    'proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what references means and why it exists.',
                             'Read and write the core syntax used for references.',
                             'Predict the behavior of a small references example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['alias', 'lvalue', 'const reference', 'parameter passing'],
    'explanation': 'Treat a reference as an alias to an existing object and use it to avoid copies or intentionally '
                   'modify caller-owned state. C++ syntax is shown with the standard library names used in this '
                   'lesson. Read the declaration from left to right: identify the type or template, the name, the '
                   'operation, and the terminating punctuation.',
    'syntax': 'int value = 10;\nint& alias = value;\nalias = 25;\ncout << value;',
    'syntax_breakdown': [ 'Focus on alias: identify what it represents and what role it plays in the statement.',
                          'Next inspect lvalue: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'int value = 10;\nint& alias = value;\nalias = 25;\ncout << value;',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'void increase(int& value) { ++value; }\nint score = 10;\nincrease(score);\ncout << score;',
    'example2_explanation': 'Change one meaningful input or rule related to references, predict the result, and only '
                            'then run the program.',
    'practical_example': 'Imagine a small references feature in a student or inventory program. Decide what data '
                         'enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing alias syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make alias behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each alias before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Compare pass-by-value, const reference, and non-const reference using three small functions.',
    'practice_problem': '**References independent practice:** Compare pass-by-value, const reference, and non-const '
                        'reference using three small functions. You must also add one clearly different variation and '
                        "test it. Your work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for References:** Run the program with a normal case, a boundary case, and a '
                       'misuse/invalid case when relevant. For each case, record the actual result and compare it with '
                       'the requirement. A correct submission must preserve the lesson rule and handle the defined '
                       'edge case safely.',
    'mastery_quiz': [ [ 'References: What is a C++ reference?',
                        [ 'An alias for an existing object',
                          'A new object by default',
                          'A file handle',
                          'A class definition'],
                        0,
                        'A reference aliases an existing object.'],
                      [ 'Why use const T& for a large read-only object?',
                        [ 'Avoid copying while preventing modification through the reference',
                          'Force a heap allocation',
                          'Delete the object',
                          'Create a thread'],
                        0,
                        'A const reference can avoid a copy while providing read-only access.'],
                      [ 'Can a reference normally be reseated to another object?',
                        ['No', 'Yes with =', 'Only inside loops', 'Only for strings'],
                        0,
                        'A reference remains bound to the object it refers to.'],
                      [ 'What is pass-by-reference useful for?',
                        [ 'Allowing a function to observe or modify caller-owned state',
                          'Always copying values',
                          'Creating files',
                          'Changing the compiler'],
                        0,
                        'Non-const references can modify the caller’s object.'],
                      [ 'What should you prefer when you do not need mutation?',
                        [ 'A const reference where appropriate',
                          'A global pointer',
                          'A raw owning pointer',
                          'An uninitialized reference'],
                        0,
                        'Const references communicate read-only intent.']],
    'summary': 'You should now be able to explain references, recognize its syntax, trace the worked example, and use '
               'the concept in a small original program.',
    'next_lesson': 'Pointers',
    'rules': [ 'Name and trace the role of each alias before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the references '
            'exercise.',
    'extension': 'Add one realistic requirement to the references exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain references without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_14'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'References matters because C++ programs must reason carefully about references, ownership, '
                      'lifetime, and resource safety.',
    'guided_practice': [ '1. Restate the goal of **References** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **References**, then '
                         'change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **References** task: Compare pass-by-value, const reference, and '
                            'non-const reference using three small functions. Then create one small variation that '
                            'changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **References** program that exhibits this common mistake: **Memorizing '
                  'alias syntax without being able to explain what changes in the program.**. Before changing code, '
                  'identify the first incorrect value, state, control-flow decision, or ownership assumption; then '
                  'explain the fix in one sentence.',
    'transfer_task': 'Transfer **References** to a small real-world feature. Keep the same core rule, but change the '
                     'context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what references means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for references.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small references example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for References.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for References without violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in References.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['memory', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_16',
    'title': 'Pointers',
    'description': 'Understand addresses, pointer variables, dereferencing, nullptr, pointer-to-object relationships, '
                   'and safe pointer checks.',
    'stage': 'Data & Design',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Pointers**, understand why it is useful, trace a focused example, '
                    'practice it with guidance, then solve an independent variation. You will finish by proving your '
                    'understanding through concept, syntax, code-reading, debugging, and application checks.',
    'learning_objectives': [ 'Explain what pointers means and why it exists.',
                             'Read and write the core syntax used for pointers.',
                             'Predict the behavior of a small pointers example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['address', 'dereference', 'nullptr', 'pointer arithmetic'],
    'explanation': 'Understand addresses, pointer variables, dereferencing, nullptr, pointer-to-object relationships, '
                   'and safe pointer checks. C++ syntax is shown with the standard library names used in this lesson. '
                   'Read the declaration from left to right: identify the type or template, the name, the operation, '
                   'and the terminating punctuation.',
    'syntax': 'int value = 42;\nint* ptr = &value;\nif (ptr != nullptr) cout << *ptr;',
    'syntax_breakdown': [ 'Focus on address: identify what it represents and what role it plays in the statement.',
                          'Next inspect dereference: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'int value = 42;\nint* ptr = &value;\nif (ptr != nullptr) cout << *ptr;',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'int value = 7;\nint* p = &value;\n*p = 11;\ncout << value;',
    'example2_explanation': 'Change one meaningful input or rule related to pointers, predict the result, and only '
                            'then run the program.',
    'practical_example': 'Imagine a small pointers feature in a student or inventory program. Decide what data enters '
                         'the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing address syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make address behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each address before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Write a function that receives an int pointer and safely changes the pointed-to value only when the '
                'pointer is valid.',
    'practice_problem': '**Pointers independent practice:** Write a function that receives an int pointer and safely '
                        'changes the pointed-to value only when the pointer is valid. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Pointers:** Run the program with a normal case, a boundary case, and a '
                       'misuse/invalid case when relevant. For each case, record the actual result and compare it with '
                       'the requirement. A correct submission must preserve the lesson rule and handle the defined '
                       'edge case safely.',
    'mastery_quiz': [ [ 'Pointers: What does a pointer store?',
                        ['An address', 'Only an integer value', 'A class blueprint', 'A file name'],
                        0,
                        'Pointers store addresses.'],
                      [ 'What does *ptr do in an expression?',
                        ['Dereference the pointer', 'Create a pointer', 'Compare two strings', 'Delete every object'],
                        0,
                        'Dereferencing accesses the pointed-to object.'],
                      [ 'What does nullptr mean?',
                        [ 'The pointer does not point to an object',
                          'The pointer points to zero bytes of valid data',
                          'The pointer is a reference',
                          'The pointer is automatically owned'],
                        0,
                        'nullptr represents a null pointer value.'],
                      [ 'Why check a pointer before dereferencing it?',
                        [ 'To avoid accessing through a null/invalid pointer',
                          'To make the compiler slower',
                          'To create a vector',
                          'To convert to Java'],
                        0,
                        'Dereferencing an invalid pointer is unsafe.'],
                      [ 'What is pointer arithmetic tied to?',
                        ['The pointed-to element type', 'Only strings', 'The CPU brand', 'The file system'],
                        0,
                        'Pointer increments move by the size of the pointed-to type.']],
    'summary': 'You should now be able to explain pointers, recognize its syntax, trace the worked example, and use '
               'the concept in a small original program.',
    'next_lesson': 'Dynamic Memory & RAII',
    'rules': [ 'Name and trace the role of each address before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the pointers exercise.',
    'extension': 'Add one realistic requirement to the pointers exercise while keeping the original behavior correct.',
    'learning_checks': [ 'Can I explain pointers without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_15'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Pointers matters because C++ programs must reason carefully about references, ownership, '
                      'lifetime, and resource safety.',
    'guided_practice': [ '1. Restate the goal of **Pointers** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Pointers**, then '
                         'change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Pointers** task: Write a function that receives an int pointer '
                            'and safely changes the pointed-to value only when the pointer is valid. Then create one '
                            'small variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Pointers** program that exhibits this common mistake: **Memorizing '
                  'address syntax without being able to explain what changes in the program.**. Before changing code, '
                  'identify the first incorrect value, state, control-flow decision, or ownership assumption; then '
                  'explain the fix in one sentence.',
    'transfer_task': 'Transfer **Pointers** to a small real-world feature. Keep the same core rule, but change the '
                     'context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what pointers means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for pointers.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small pointers example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Pointers.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Pointers without violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Pointers.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['memory', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_17',
    'title': 'Dynamic Memory & RAII',
    'description': 'Understand stack and heap lifetimes, new/delete, dynamic arrays, ownership, leaks, dangling '
                   'pointers, and why modern C++ prefers RAII.',
    'stage': 'Data & Design',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Dynamic Memory & RAII**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what dynamic memory & raii means and why it exists.',
                             'Read and write the core syntax used for dynamic memory & raii.',
                             'Predict the behavior of a small dynamic memory & raii example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['heap', 'ownership', 'leak', 'lifetime'],
    'explanation': 'Understand stack and heap lifetimes, new/delete, dynamic arrays, ownership, leaks, dangling '
                   'pointers, and why modern C++ prefers RAII. C++ syntax is shown with the standard library names '
                   'used in this lesson. Read the declaration from left to right: identify the type or template, the '
                   'name, the operation, and the terminating punctuation.',
    'syntax': 'int* p = new int(42);\ncout << *p;\ndelete p;\np = nullptr;',
    'syntax_breakdown': [ 'Focus on heap: identify what it represents and what role it plays in the statement.',
                          'Next inspect ownership: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'int* p = new int(42);\ncout << *p;\ndelete p;\np = nullptr;',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'int* numbers = new int[3]{2,4,6};\ncout << numbers[1];\ndelete[] numbers;\nnumbers = nullptr;',
    'example2_explanation': 'Change one meaningful input or rule related to dynamic memory & raii, predict the result, '
                            'and only then run the program.',
    'practical_example': 'Imagine a small dynamic memory & raii feature in a student or inventory program. Decide what '
                         'data enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing heap syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make heap behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each heap before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Demonstrate a heap allocation safely, then explain why the same task is better expressed with a '
                'standard container or smart pointer.',
    'practice_problem': '**Dynamic Memory & RAII independent practice:** Demonstrate a heap allocation safely, then '
                        'explain why the same task is better expressed with a standard container or smart pointer. You '
                        'must also add one clearly different variation and test it. Your work should demonstrate the '
                        "lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Dynamic Memory & RAII:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'Dynamic Memory & RAII: What does RAII tie resource management to?',
                        ['Object lifetime', 'Network speed', 'Variable names', 'Compiler warnings'],
                        0,
                        'RAII releases resources when the owning object leaves scope.'],
                      [ 'Why is unique_ptr useful?',
                        [ 'It expresses exclusive ownership',
                          'It creates shared ownership',
                          'It disables destructors',
                          'It removes allocation'],
                        0,
                        'unique_ptr models one owner.'],
                      [ 'What is a memory leak?',
                        [ 'Allocated/resource memory that is no longer reachable for proper release',
                          'A syntax error',
                          'A valid loop',
                          'A type cast'],
                        0,
                        'Leaks consume resources because ownership was not released correctly.'],
                      [ 'What is the Rule of Zero?',
                        [ 'Prefer types that need no custom special member functions for resource management',
                          'Always write five constructors',
                          'Never use classes',
                          'Never use RAII'],
                        0,
                        'The Rule of Zero encourages RAII types so user-defined special members are unnecessary.'],
                      [ 'Why use ownership types explicitly?',
                        [ 'They communicate who is responsible for cleanup',
                          'They prevent all bugs',
                          'They avoid compilation',
                          'They make everything global'],
                        0,
                        'Ownership is part of a robust C++ design.']],
    'summary': 'You should now be able to explain dynamic memory & raii, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Classes & Objects',
    'rules': [ 'Name and trace the role of each heap before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the dynamic memory & '
            'raii exercise.',
    'extension': 'Add one realistic requirement to the dynamic memory & raii exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain dynamic memory & raii without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_16'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Dynamic Memory & RAII matters because C++ programs must reason carefully about references, '
                      'ownership, lifetime, and resource safety.',
    'guided_practice': [ '1. Restate the goal of **Dynamic Memory & RAII** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Dynamic Memory & '
                         'RAII**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Dynamic Memory & RAII** task: Demonstrate a heap allocation '
                            'safely, then explain why the same task is better expressed with a standard container or '
                            'smart pointer. Then create one small variation that changes an input, rule, or data case '
                            'without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Dynamic Memory & RAII** program that exhibits this common mistake: '
                  '**Memorizing heap syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Dynamic Memory & RAII** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what dynamic memory & raii means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for dynamic memory & raii.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small dynamic memory & raii example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Dynamic Memory & RAII.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Dynamic Memory & RAII without violating the '
                                  'stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Dynamic Memory '
                                  '& RAII.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['memory', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_18',
    'title': 'Classes & Objects',
    'description': 'Model data and behavior with classes, objects, fields, methods, and access control.',
    'stage': 'Data & Design',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Classes & Objects**, understand why it is useful, trace a focused '
                    'example, practice it with guidance, then solve an independent variation. You will finish by '
                    'proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what classes & objects means and why it exists.',
                             'Read and write the core syntax used for classes & objects.',
                             'Predict the behavior of a small classes & objects example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['class', 'object', 'field', 'method'],
    'explanation': 'Model data and behavior with classes, objects, fields, methods, and access control. C++ syntax is '
                   'shown with the standard library names used in this lesson. Read the declaration from left to '
                   'right: identify the type or template, the name, the operation, and the terminating punctuation.',
    'syntax': 'class Student {\n'
              'public:\n'
              '    std::string name;\n'
              '    void greet() const { cout << "Hi " << name; }\n'
              '};\n'
              '\n'
              'Student s;\n'
              's.name = "Ren";\n'
              's.greet();',
    'syntax_breakdown': [ 'Focus on class: identify what it represents and what role it plays in the statement.',
                          'Next inspect object: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'class Student {\n'
                'public:\n'
                '    std::string name;\n'
                '    void greet() const { cout << "Hi " << name; }\n'
                '};\n'
                '\n'
                'Student s;\n'
                's.name = "Ren";\n'
                's.greet();',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'class Lamp {\n'
                'public:\n'
                '    bool on = false;\n'
                '    void toggle() { on = !on; }\n'
                '};\n'
                'Lamp lamp; lamp.toggle(); cout << lamp.on;',
    'example2_explanation': 'Change one meaningful input or rule related to classes & objects, predict the result, and '
                            'only then run the program.',
    'practical_example': 'Imagine a small classes & objects feature in a student or inventory program. Decide what '
                         'data enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing class syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make class behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each class before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Create a Book class with title, author, and a method that prints a formatted description.',
    'practice_problem': '**Classes & Objects independent practice:** Create a Book class with title, author, and a '
                        'method that prints a formatted description. You must also add one clearly different variation '
                        "and test it. Your work should demonstrate the lesson's main rule, not merely reproduce "
                        'Example 1.',
    'expected_output': '**Test contract for Classes & Objects:** Run the program with a normal case, a boundary case, '
                       'and a misuse/invalid case when relevant. For each case, record the actual result and compare '
                       'it with the requirement. A correct submission must preserve the lesson rule and handle the '
                       'defined edge case safely.',
    'mastery_quiz': [ [ 'Classes & Objects: What is the main design idea in Classes & Objects?',
                        [ 'Organizing data and behavior with appropriate object relationships',
                          'Replacing all loops',
                          'Reading files only',
                          'Changing compiler flags'],
                        0,
                        'The lesson focuses on object structure and behavior.'],
                      [ 'What does encapsulation protect?',
                        [ 'Object invariants and implementation details',
                          'The compiler executable',
                          'Only comments',
                          'The network cable'],
                        0,
                        'Encapsulation controls how state is accessed and changed.'],
                      [ 'Why use composition?',
                        [ 'To build a larger object from focused components',
                          'To make every class a subclass',
                          'To avoid all objects',
                          'To disable methods'],
                        0,
                        'Composition models has-a relationships.'],
                      [ 'What does polymorphism allow?',
                        [ 'Common code to work with different concrete implementations',
                          'Every object to have the same state',
                          'Loops to become functions',
                          'Files to become classes'],
                        0,
                        'Polymorphism lets a common interface select behavior appropriate to the object.'],
                      [ 'What makes a constructor important?',
                        [ 'It establishes valid initial object state',
                          'It returns an int',
                          'It creates a package',
                          'It sorts fields'],
                        0,
                        'Constructors establish object state when instances are created.']],
    'summary': 'You should now be able to explain classes & objects, recognize its syntax, trace the worked example, '
               'and use the concept in a small original program.',
    'next_lesson': 'Constructors & Object Lifetime',
    'rules': [ 'Name and trace the role of each class before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the classes & objects '
            'exercise.',
    'extension': 'Add one realistic requirement to the classes & objects exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain classes & objects without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_17'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Classes & Objects matters because larger programs need clear ownership of state and behavior '
                      'and predictable relationships between types.',
    'guided_practice': [ '1. Restate the goal of **Classes & Objects** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Classes & '
                         'Objects**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Classes & Objects** task: Create a Book class with title, '
                            'author, and a method that prints a formatted description. Then create one small variation '
                            'that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Classes & Objects** program that exhibits this common mistake: '
                  '**Memorizing class syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Classes & Objects** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what classes & objects means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for classes & objects.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small classes & objects example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Classes & Objects.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Classes & Objects without violating the stated '
                                  'rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Classes & '
                                  'Objects.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['oop', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_19',
    'title': 'Constructors & Object Lifetime',
    'description': 'Use constructors to establish valid initial state, understand destructor timing, initializer '
                   'lists, and scope-based object lifetime.',
    'stage': 'Data & Design',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Constructors & Object Lifetime**, understand why it is useful, '
                    'trace a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what constructors & object lifetime means and why it exists.',
                             'Read and write the core syntax used for constructors & object lifetime.',
                             'Predict the behavior of a small constructors & object lifetime example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['Constructors & Object Lifetime', 'syntax', 'behavior', 'use case'],
    'explanation': 'Use constructors to establish valid initial state, understand destructor timing, initializer '
                   'lists, and scope-based object lifetime. C++ syntax is shown with the standard library names used '
                   'in this lesson. Read the declaration from left to right: identify the type or template, the name, '
                   'the operation, and the terminating punctuation.',
    'syntax': 'class Account {\n    double balance;\npublic:\n    Account(double start) : balance(start) {}\n};',
    'syntax_breakdown': [ 'Focus on Constructors & Object Lifetime: identify what it represents and what role it plays '
                          'in the statement.',
                          'Next inspect syntax: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'class Account {\n    double balance;\npublic:\n    Account(double start) : balance(start) {}\n};',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'struct Product { std::string name; double price; };\n'
                'Product item{"Keyboard", 999.0};\n'
                'cout << item.name << " " << item.price;',
    'example2_explanation': 'Change one meaningful input or rule related to constructors & object lifetime, predict '
                            'the result, and only then run the program.',
    'practical_example': 'Imagine a small constructors & object lifetime feature in a student or inventory program. '
                         'Decide what data enters the feature, what rule the feature applies, and what result it '
                         'should produce.',
    'common_mistakes': [ 'Memorizing Constructors & Object Lifetime syntax without being able to explain what changes '
                         'in the program.',
                         'Ignoring the boundary or lifetime rules that make Constructors & Object Lifetime behave '
                         'correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each Constructors & Object Lifetime before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Create a class whose constructor rejects or normalizes an invalid starting value and explain when its '
                'destructor runs.',
    'practice_problem': '**Constructors & Object Lifetime independent practice:** Create a class whose constructor '
                        'rejects or normalizes an invalid starting value and explain when its destructor runs. You '
                        'must also add one clearly different variation and test it. Your work should demonstrate the '
                        "lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Constructors & Object Lifetime:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Constructors & Object Lifetime: What is the main design idea in Constructors & Object '
                        'Lifetime?',
                        [ 'Organizing data and behavior with appropriate object relationships',
                          'Replacing all loops',
                          'Reading files only',
                          'Changing compiler flags'],
                        0,
                        'The lesson focuses on object structure and behavior.'],
                      [ 'What does encapsulation protect?',
                        [ 'Object invariants and implementation details',
                          'The compiler executable',
                          'Only comments',
                          'The network cable'],
                        0,
                        'Encapsulation controls how state is accessed and changed.'],
                      [ 'Why use composition?',
                        [ 'To build a larger object from focused components',
                          'To make every class a subclass',
                          'To avoid all objects',
                          'To disable methods'],
                        0,
                        'Composition models has-a relationships.'],
                      [ 'What does polymorphism allow?',
                        [ 'Common code to work with different concrete implementations',
                          'Every object to have the same state',
                          'Loops to become functions',
                          'Files to become classes'],
                        0,
                        'Polymorphism lets a common interface select behavior appropriate to the object.'],
                      [ 'What makes a constructor important?',
                        [ 'It establishes valid initial object state',
                          'It returns an int',
                          'It creates a package',
                          'It sorts fields'],
                        0,
                        'Constructors establish object state when instances are created.']],
    'summary': 'You should now be able to explain constructors & object lifetime, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Encapsulation & Access Control',
    'rules': [ 'Name and trace the role of each Constructors & Object Lifetime before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the constructors & '
            'object lifetime exercise.',
    'extension': 'Add one realistic requirement to the constructors & object lifetime exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain constructors & object lifetime without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_18'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Constructors & Object Lifetime matters because larger programs need clear ownership of state '
                      'and behavior and predictable relationships between types.',
    'guided_practice': [ '1. Restate the goal of **Constructors & Object Lifetime** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Constructors & '
                         'Object Lifetime**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Constructors & Object Lifetime** task: Create a class whose '
                            'constructor rejects or normalizes an invalid starting value and explain when its '
                            'destructor runs. Then create one small variation that changes an input, rule, or data '
                            'case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Constructors & Object Lifetime** program that exhibits this common '
                  'mistake: **Memorizing Constructors & Object Lifetime syntax without being able to explain what '
                  'changes in the program.**. Before changing code, identify the first incorrect value, state, '
                  'control-flow decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Constructors & Object Lifetime** to a small real-world feature. Keep the same core '
                     'rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what constructors & object lifetime means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for constructors & object '
                                                 'lifetime.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small constructors & object lifetime '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Constructors & Object Lifetime.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Constructors & Object Lifetime without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Constructors & '
                                  'Object Lifetime.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['oop', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_20',
    'title': 'Encapsulation & Access Control',
    'description': 'Protect class invariants with private state, public methods, validation, getters, setters, and '
                   'carefully chosen protected members.',
    'stage': 'Data & Design',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Encapsulation & Access Control**, understand why it is useful, '
                    'trace a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what encapsulation & access control means and why it exists.',
                             'Read and write the core syntax used for encapsulation & access control.',
                             'Predict the behavior of a small encapsulation & access control example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['private', 'public', 'invariant', 'access'],
    'explanation': 'Protect class invariants with private state, public methods, validation, getters, setters, and '
                   'carefully chosen protected members. C++ syntax is shown with the standard library names used in '
                   'this lesson. Read the declaration from left to right: identify the type or template, the name, the '
                   'operation, and the terminating punctuation.',
    'syntax': 'class BankAccount {\n'
              '    double balance = 0;\n'
              'public:\n'
              '    void deposit(double amount) { if (amount > 0) balance += amount; }\n'
              '    double getBalance() const { return balance; }\n'
              '};',
    'syntax_breakdown': [ 'Focus on private: identify what it represents and what role it plays in the statement.',
                          'Next inspect public: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'class BankAccount {\n'
                '    double balance = 0;\n'
                'public:\n'
                '    void deposit(double amount) { if (amount > 0) balance += amount; }\n'
                '    double getBalance() const { return balance; }\n'
                '};',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'class Score {\n'
                '    int value = 0;\n'
                'public:\n'
                '    void set(int v) { if (v >= 0 && v <= 100) value = v; }\n'
                '    int get() const { return value; }\n'
                '};',
    'example2_explanation': 'Change one meaningful input or rule related to encapsulation & access control, predict '
                            'the result, and only then run the program.',
    'practical_example': 'Imagine a small encapsulation & access control feature in a student or inventory program. '
                         'Decide what data enters the feature, what rule the feature applies, and what result it '
                         'should produce.',
    'common_mistakes': [ 'Memorizing private syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make private behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each private before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Design a Student class whose grade cannot be changed to a value outside 0–100.',
    'practice_problem': '**Encapsulation & Access Control independent practice:** Design a Student class whose grade '
                        'cannot be changed to a value outside 0–100. You must also add one clearly different variation '
                        "and test it. Your work should demonstrate the lesson's main rule, not merely reproduce "
                        'Example 1.',
    'expected_output': '**Test contract for Encapsulation & Access Control:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Encapsulation & Access Control: What is the main design idea in Encapsulation & Access '
                        'Control?',
                        [ 'Organizing data and behavior with appropriate object relationships',
                          'Replacing all loops',
                          'Reading files only',
                          'Changing compiler flags'],
                        0,
                        'The lesson focuses on object structure and behavior.'],
                      [ 'What does encapsulation protect?',
                        [ 'Object invariants and implementation details',
                          'The compiler executable',
                          'Only comments',
                          'The network cable'],
                        0,
                        'Encapsulation controls how state is accessed and changed.'],
                      [ 'Why use composition?',
                        [ 'To build a larger object from focused components',
                          'To make every class a subclass',
                          'To avoid all objects',
                          'To disable methods'],
                        0,
                        'Composition models has-a relationships.'],
                      [ 'What does polymorphism allow?',
                        [ 'Common code to work with different concrete implementations',
                          'Every object to have the same state',
                          'Loops to become functions',
                          'Files to become classes'],
                        0,
                        'Polymorphism lets a common interface select behavior appropriate to the object.'],
                      [ 'What makes a constructor important?',
                        [ 'It establishes valid initial object state',
                          'It returns an int',
                          'It creates a package',
                          'It sorts fields'],
                        0,
                        'Constructors establish object state when instances are created.']],
    'summary': 'You should now be able to explain encapsulation & access control, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Composition',
    'rules': [ 'Name and trace the role of each private before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the encapsulation & '
            'access control exercise.',
    'extension': 'Add one realistic requirement to the encapsulation & access control exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain encapsulation & access control without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_19'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Encapsulation & Access Control matters because larger programs need clear ownership of state '
                      'and behavior and predictable relationships between types.',
    'guided_practice': [ '1. Restate the goal of **Encapsulation & Access Control** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Encapsulation & '
                         'Access Control**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Encapsulation & Access Control** task: Design a Student class '
                            'whose grade cannot be changed to a value outside 0–100. Then create one small variation '
                            'that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Encapsulation & Access Control** program that exhibits this common '
                  'mistake: **Memorizing private syntax without being able to explain what changes in the program.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Encapsulation & Access Control** to a small real-world feature. Keep the same core '
                     'rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what encapsulation & access control means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for encapsulation & access '
                                                 'control.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small encapsulation & access control '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Encapsulation & Access Control.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Encapsulation & Access Control without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Encapsulation '
                                  '& Access Control.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['oop', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_21',
    'title': 'Composition',
    'description': 'Build larger objects from smaller objects, distinguish composition from inheritance, and choose '
                   'ownership relationships deliberately.',
    'stage': 'Data & Design',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Composition**, understand why it is useful, trace a focused '
                    'example, practice it with guidance, then solve an independent variation. You will finish by '
                    'proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what composition means and why it exists.',
                             'Read and write the core syntax used for composition.',
                             'Predict the behavior of a small composition example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['has-a', 'component', 'ownership', 'delegation'],
    'explanation': 'Build larger objects from smaller objects, distinguish composition from inheritance, and choose '
                   'ownership relationships deliberately. C++ syntax is shown with the standard library names used in '
                   'this lesson. Read the declaration from left to right: identify the type or template, the name, the '
                   'operation, and the terminating punctuation.',
    'syntax': 'class Engine { public: void start() { cout << "Engine on"; } };\n'
              'class Car {\n'
              '    Engine engine;\n'
              'public:\n'
              '    void start() { engine.start(); }\n'
              '};',
    'syntax_breakdown': [ 'Focus on has-a: identify what it represents and what role it plays in the statement.',
                          'Next inspect component: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'class Engine { public: void start() { cout << "Engine on"; } };\n'
                'class Car {\n'
                '    Engine engine;\n'
                'public:\n'
                '    void start() { engine.start(); }\n'
                '};',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'class Battery { public: int level = 100; };\n'
                'class Phone {\n'
                '    Battery battery;\n'
                'public:\n'
                '    int batteryLevel() const { return battery.level; }\n'
                '};',
    'example2_explanation': 'Change one meaningful input or rule related to composition, predict the result, and only '
                            'then run the program.',
    'practical_example': 'Imagine a small composition feature in a student or inventory program. Decide what data '
                         'enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing has-a syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make has-a behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each has-a before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Build a Computer that contains CPU and Storage objects, then explain why composition fits the '
                'relationship.',
    'practice_problem': '**Composition independent practice:** Build a Computer that contains CPU and Storage objects, '
                        'then explain why composition fits the relationship. You must also add one clearly different '
                        "variation and test it. Your work should demonstrate the lesson's main rule, not merely "
                        'reproduce Example 1.',
    'expected_output': '**Test contract for Composition:** Run the program with a normal case, a boundary case, and a '
                       'misuse/invalid case when relevant. For each case, record the actual result and compare it with '
                       'the requirement. A correct submission must preserve the lesson rule and handle the defined '
                       'edge case safely.',
    'mastery_quiz': [ [ 'Composition: What is the main design idea in Composition?',
                        [ 'Organizing data and behavior with appropriate object relationships',
                          'Replacing all loops',
                          'Reading files only',
                          'Changing compiler flags'],
                        0,
                        'The lesson focuses on object structure and behavior.'],
                      [ 'What does encapsulation protect?',
                        [ 'Object invariants and implementation details',
                          'The compiler executable',
                          'Only comments',
                          'The network cable'],
                        0,
                        'Encapsulation controls how state is accessed and changed.'],
                      [ 'Why use composition?',
                        [ 'To build a larger object from focused components',
                          'To make every class a subclass',
                          'To avoid all objects',
                          'To disable methods'],
                        0,
                        'Composition models has-a relationships.'],
                      [ 'What does polymorphism allow?',
                        [ 'Common code to work with different concrete implementations',
                          'Every object to have the same state',
                          'Loops to become functions',
                          'Files to become classes'],
                        0,
                        'Polymorphism lets a common interface select behavior appropriate to the object.'],
                      [ 'What makes a constructor important?',
                        [ 'It establishes valid initial object state',
                          'It returns an int',
                          'It creates a package',
                          'It sorts fields'],
                        0,
                        'Constructors establish object state when instances are created.']],
    'summary': 'You should now be able to explain composition, recognize its syntax, trace the worked example, and use '
               'the concept in a small original program.',
    'next_lesson': 'Inheritance',
    'rules': [ 'Name and trace the role of each has-a before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the composition '
            'exercise.',
    'extension': 'Add one realistic requirement to the composition exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain composition without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_20'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Composition matters because larger programs need clear ownership of state and behavior and '
                      'predictable relationships between types.',
    'guided_practice': [ '1. Restate the goal of **Composition** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Composition**, '
                         'then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Composition** task: Build a Computer that contains CPU and '
                            'Storage objects, then explain why composition fits the relationship. Then create one '
                            'small variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Composition** program that exhibits this common mistake: **Memorizing '
                  'has-a syntax without being able to explain what changes in the program.**. Before changing code, '
                  'identify the first incorrect value, state, control-flow decision, or ownership assumption; then '
                  'explain the fix in one sentence.',
    'transfer_task': 'Transfer **Composition** to a small real-world feature. Keep the same core rule, but change the '
                     'context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what composition means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for composition.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small composition example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Composition.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Composition without violating the stated '
                                  'rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Composition.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['oop', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_22',
    'title': 'Inheritance',
    'description': 'Reuse and specialize behavior with base and derived classes, constructor chaining, protected '
                   'access, and careful use of inheritance.',
    'stage': 'Object-Oriented Programming',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Inheritance**, understand why it is useful, trace a focused '
                    'example, practice it with guidance, then solve an independent variation. You will finish by '
                    'proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what inheritance means and why it exists.',
                             'Read and write the core syntax used for inheritance.',
                             'Predict the behavior of a small inheritance example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['base class', 'derived class', 'super', 'reuse'],
    'explanation': 'Reuse and specialize behavior with base and derived classes, constructor chaining, protected '
                   'access, and careful use of inheritance. C++ syntax is shown with the standard library names used '
                   'in this lesson. Read the declaration from left to right: identify the type or template, the name, '
                   'the operation, and the terminating punctuation.',
    'syntax': 'class Animal { public: void eat() { cout << "eat"; } };\n'
              'class Dog : public Animal { public: void bark() { cout << "woof"; } };',
    'syntax_breakdown': [ 'Focus on base class: identify what it represents and what role it plays in the statement.',
                          'Next inspect derived class: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'class Animal { public: void eat() { cout << "eat"; } };\n'
                'class Dog : public Animal { public: void bark() { cout << "woof"; } };',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'class Vehicle { public: void move(){ cout << "move"; } };\n'
                'class Bike : public Vehicle { public: void ring(){ cout << "ring"; } };',
    'example2_explanation': 'Change one meaningful input or rule related to inheritance, predict the result, and only '
                            'then run the program.',
    'practical_example': 'Imagine a small inheritance feature in a student or inventory program. Decide what data '
                         'enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing base class syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make base class behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each base class before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Create a base Vehicle class and two derived types that add specialized behavior.',
    'practice_problem': '**Inheritance independent practice:** Create a base Vehicle class and two derived types that '
                        'add specialized behavior. You must also add one clearly different variation and test it. Your '
                        "work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Inheritance:** Run the program with a normal case, a boundary case, and a '
                       'misuse/invalid case when relevant. For each case, record the actual result and compare it with '
                       'the requirement. A correct submission must preserve the lesson rule and handle the defined '
                       'edge case safely.',
    'mastery_quiz': [ [ 'Inheritance: What is the main design idea in Inheritance?',
                        [ 'Organizing data and behavior with appropriate object relationships',
                          'Replacing all loops',
                          'Reading files only',
                          'Changing compiler flags'],
                        0,
                        'The lesson focuses on object structure and behavior.'],
                      [ 'What does encapsulation protect?',
                        [ 'Object invariants and implementation details',
                          'The compiler executable',
                          'Only comments',
                          'The network cable'],
                        0,
                        'Encapsulation controls how state is accessed and changed.'],
                      [ 'Why use composition?',
                        [ 'To build a larger object from focused components',
                          'To make every class a subclass',
                          'To avoid all objects',
                          'To disable methods'],
                        0,
                        'Composition models has-a relationships.'],
                      [ 'What does polymorphism allow?',
                        [ 'Common code to work with different concrete implementations',
                          'Every object to have the same state',
                          'Loops to become functions',
                          'Files to become classes'],
                        0,
                        'Polymorphism lets a common interface select behavior appropriate to the object.'],
                      [ 'What makes a constructor important?',
                        [ 'It establishes valid initial object state',
                          'It returns an int',
                          'It creates a package',
                          'It sorts fields'],
                        0,
                        'Constructors establish object state when instances are created.']],
    'summary': 'You should now be able to explain inheritance, recognize its syntax, trace the worked example, and use '
               'the concept in a small original program.',
    'next_lesson': 'Polymorphism & Virtual Functions',
    'rules': [ 'Name and trace the role of each base class before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the inheritance '
            'exercise.',
    'extension': 'Add one realistic requirement to the inheritance exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain inheritance without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_21'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Inheritance matters because larger programs need clear ownership of state and behavior and '
                      'predictable relationships between types.',
    'guided_practice': [ '1. Restate the goal of **Inheritance** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Inheritance**, '
                         'then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Inheritance** task: Create a base Vehicle class and two '
                            'derived types that add specialized behavior. Then create one small variation that changes '
                            'an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Inheritance** program that exhibits this common mistake: **Memorizing '
                  'base class syntax without being able to explain what changes in the program.**. Before changing '
                  'code, identify the first incorrect value, state, control-flow decision, or ownership assumption; '
                  'then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Inheritance** to a small real-world feature. Keep the same core rule, but change the '
                     'context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what inheritance means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for inheritance.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small inheritance example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Inheritance.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Inheritance without violating the stated '
                                  'rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Inheritance.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['oop', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_23',
    'title': 'Polymorphism & Virtual Functions',
    'description': 'Use virtual functions and base references/pointers so a common interface can invoke derived '
                   'behavior at runtime.',
    'stage': 'Object-Oriented Programming',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Polymorphism & Virtual Functions**, understand why it is useful, '
                    'trace a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what polymorphism & virtual functions means and why it exists.',
                             'Read and write the core syntax used for polymorphism & virtual functions.',
                             'Predict the behavior of a small polymorphism & virtual functions example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['virtual dispatch', 'override', 'base pointer', 'runtime type'],
    'explanation': 'Use virtual functions and base references/pointers so a common interface can invoke derived '
                   'behavior at runtime. C++ syntax is shown with the standard library names used in this lesson. Read '
                   'the declaration from left to right: identify the type or template, the name, the operation, and '
                   'the terminating punctuation.',
    'syntax': 'class Shape { public: virtual double area() const = 0; virtual ~Shape() = default; };\n'
              'class Square : public Shape { public: double area() const override { return 16; } };',
    'syntax_breakdown': [ 'Focus on virtual dispatch: identify what it represents and what role it plays in the '
                          'statement.',
                          'Next inspect override: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'class Shape { public: virtual double area() const = 0; virtual ~Shape() = default; };\n'
                'class Square : public Shape { public: double area() const override { return 16; } };',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'int add(int a, int b) { return a + b; }\nint main() {\n    cout << add(7, 5);\n}',
    'example2_explanation': 'Change one meaningful input or rule related to polymorphism & virtual functions, predict '
                            'the result, and only then run the program.',
    'practical_example': 'Imagine a small polymorphism & virtual functions feature in a student or inventory program. '
                         'Decide what data enters the feature, what rule the feature applies, and what result it '
                         'should produce.',
    'common_mistakes': [ 'Memorizing virtual dispatch syntax without being able to explain what changes in the '
                         'program.',
                         'Ignoring the boundary or lifetime rules that make virtual dispatch behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each virtual dispatch before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Create Shape subclasses for Circle and Rectangle and process them through a vector of '
                'unique_ptr<Shape>.',
    'practice_problem': '**Polymorphism & Virtual Functions independent practice:** Create Shape subclasses for Circle '
                        'and Rectangle and process them through a vector of unique_ptr<Shape>. You must also add one '
                        "clearly different variation and test it. Your work should demonstrate the lesson's main rule, "
                        'not merely reproduce Example 1.',
    'expected_output': '**Test contract for Polymorphism & Virtual Functions:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Polymorphism & Virtual Functions: What is a parameter?',
                        [ 'A named input in a function or method declaration',
                          'The returned value only',
                          'A compiler flag',
                          'A file path'],
                        0,
                        'Parameters describe values a caller can supply.'],
                      [ 'What is an argument?',
                        ['The value supplied when calling a function', 'The return type', 'A class name', 'A comment'],
                        0,
                        'Arguments are the actual values passed to parameters.'],
                      [ 'Why use a return value?',
                        [ 'To send a computed result back to the caller',
                          'To create a loop',
                          'To import a library',
                          'To delete a variable'],
                        0,
                        'A return value lets the caller use the result.'],
                      [ 'What does overloading mean?',
                        [ 'Same function/method name with different parameter lists',
                          'Changing only comments',
                          'Changing only the return type',
                          'Creating a new package'],
                        0,
                        'Overloads differ by their parameter lists.'],
                      [ 'What is a good function responsibility?',
                        [ 'One clear job',
                          'Every job in the whole program',
                          'Only printing comments',
                          'Changing unrelated global state'],
                        0,
                        'Focused functions are easier to test and reuse.']],
    'summary': 'You should now be able to explain polymorphism & virtual functions, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Abstract Interfaces',
    'rules': [ 'Name and trace the role of each virtual dispatch before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the polymorphism & '
            'virtual functions exercise.',
    'extension': 'Add one realistic requirement to the polymorphism & virtual functions exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain polymorphism & virtual functions without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_22'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Polymorphism & Virtual Functions matters because focused functions or methods make behavior '
                      'reusable, testable, and easier to debug.',
    'guided_practice': [ '1. Restate the goal of **Polymorphism & Virtual Functions** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Polymorphism & '
                         'Virtual Functions**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Polymorphism & Virtual Functions** task: Create Shape '
                            'subclasses for Circle and Rectangle and process them through a vector of '
                            'unique_ptr<Shape>. Then create one small variation that changes an input, rule, or data '
                            'case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Polymorphism & Virtual Functions** program that exhibits this common '
                  'mistake: **Memorizing virtual dispatch syntax without being able to explain what changes in the '
                  'program.**. Before changing code, identify the first incorrect value, state, control-flow decision, '
                  'or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Polymorphism & Virtual Functions** to a small real-world feature. Keep the same core '
                     'rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what polymorphism & virtual functions means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for polymorphism & virtual '
                                                 'functions.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small polymorphism & virtual functions '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Polymorphism & Virtual '
                                  'Functions.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Polymorphism & Virtual Functions without '
                                  'violating the stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['function', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_24',
    'title': 'Abstract Interfaces',
    'description': 'Design contracts with pure virtual functions, abstract classes, virtual destructors, and minimal '
                   'interfaces.',
    'stage': 'Object-Oriented Programming',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Abstract Interfaces**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what abstract interfaces means and why it exists.',
                             'Read and write the core syntax used for abstract interfaces.',
                             'Predict the behavior of a small abstract interfaces example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['abstract class', 'pure virtual', 'interface', 'contract'],
    'explanation': 'Design contracts with pure virtual functions, abstract classes, virtual destructors, and minimal '
                   'interfaces. C++ syntax is shown with the standard library names used in this lesson. Read the '
                   'declaration from left to right: identify the type or template, the name, the operation, and the '
                   'terminating punctuation.',
    'syntax': 'class Payable {\npublic:\n    virtual double pay() const = 0;\n    virtual ~Payable() = default;\n};',
    'syntax_breakdown': [ 'Focus on abstract class: identify what it represents and what role it plays in the '
                          'statement.',
                          'Next inspect pure virtual: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'class Payable {\npublic:\n    virtual double pay() const = 0;\n    virtual ~Payable() = default;\n};',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'struct Animal { virtual string sound() const = 0; virtual ~Animal() = default; };\n'
                'struct Cat : Animal { string sound() const override { return "meow"; } };\n'
                'Animal* a = new Cat; cout << a->sound(); delete a;',
    'example2_explanation': 'Change one meaningful input or rule related to abstract interfaces, predict the result, '
                            'and only then run the program.',
    'practical_example': 'Imagine a small abstract interfaces feature in a student or inventory program. Decide what '
                         'data enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing abstract class syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make abstract class behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each abstract class before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Design an abstract Payment interface with two concrete implementations and call them through the '
                'interface.',
    'practice_problem': '**Abstract Interfaces independent practice:** Design an abstract Payment interface with two '
                        'concrete implementations and call them through the interface. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Abstract Interfaces:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'Abstract Interfaces: What is the main design idea in Abstract Interfaces?',
                        [ 'Organizing data and behavior with appropriate object relationships',
                          'Replacing all loops',
                          'Reading files only',
                          'Changing compiler flags'],
                        0,
                        'The lesson focuses on object structure and behavior.'],
                      [ 'What does encapsulation protect?',
                        [ 'Object invariants and implementation details',
                          'The compiler executable',
                          'Only comments',
                          'The network cable'],
                        0,
                        'Encapsulation controls how state is accessed and changed.'],
                      [ 'Why use composition?',
                        [ 'To build a larger object from focused components',
                          'To make every class a subclass',
                          'To avoid all objects',
                          'To disable methods'],
                        0,
                        'Composition models has-a relationships.'],
                      [ 'What does polymorphism allow?',
                        [ 'Common code to work with different concrete implementations',
                          'Every object to have the same state',
                          'Loops to become functions',
                          'Files to become classes'],
                        0,
                        'Polymorphism lets a common interface select behavior appropriate to the object.'],
                      [ 'What makes a constructor important?',
                        [ 'It establishes valid initial object state',
                          'It returns an int',
                          'It creates a package',
                          'It sorts fields'],
                        0,
                        'Constructors establish object state when instances are created.']],
    'summary': 'You should now be able to explain abstract interfaces, recognize its syntax, trace the worked example, '
               'and use the concept in a small original program.',
    'next_lesson': 'Exception Handling',
    'rules': [ 'Name and trace the role of each abstract class before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the abstract interfaces '
            'exercise.',
    'extension': 'Add one realistic requirement to the abstract interfaces exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain abstract interfaces without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_23'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Abstract Interfaces matters because larger programs need clear ownership of state and behavior '
                      'and predictable relationships between types.',
    'guided_practice': [ '1. Restate the goal of **Abstract Interfaces** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Abstract '
                         'Interfaces**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Abstract Interfaces** task: Design an abstract Payment '
                            'interface with two concrete implementations and call them through the interface. Then '
                            'create one small variation that changes an input, rule, or data case without changing the '
                            'main goal.',
    'debug_task': 'Debug a deliberately small **Abstract Interfaces** program that exhibits this common mistake: '
                  '**Memorizing abstract class syntax without being able to explain what changes in the program.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Abstract Interfaces** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what abstract interfaces means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for abstract interfaces.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small abstract interfaces example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Abstract Interfaces.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Abstract Interfaces without violating the '
                                  'stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Abstract '
                                  'Interfaces.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['oop', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_25',
    'title': 'Exception Handling',
    'description': 'Handle exceptional situations with try, catch, throw, standard exceptions, and custom exception '
                   'types without hiding ordinary logic errors.',
    'stage': 'Object-Oriented Programming',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Exception Handling**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what exception handling means and why it exists.',
                             'Read and write the core syntax used for exception handling.',
                             'Predict the behavior of a small exception handling example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['exception', 'try', 'catch', 'throw'],
    'explanation': 'Handle exceptional situations with try, catch, throw, standard exceptions, and custom exception '
                   'types without hiding ordinary logic errors. C++ syntax is shown with the standard library names '
                   'used in this lesson. Read the declaration from left to right: identify the type or template, the '
                   'name, the operation, and the terminating punctuation.',
    'syntax': 'double divide(double a, double b) {\n'
              '    if (b == 0) throw invalid_argument("division by zero");\n'
              '    return a / b;\n'
              '}',
    'syntax_breakdown': [ 'Focus on exception: identify what it represents and what role it plays in the statement.',
                          'Next inspect try: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'double divide(double a, double b) {\n'
                '    if (b == 0) throw invalid_argument("division by zero");\n'
                '    return a / b;\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'try {\n'
                '    throw invalid_argument("bad score");\n'
                '} catch (const invalid_argument& ex) {\n'
                '    cout << ex.what();\n'
                '}',
    'example2_explanation': 'Change one meaningful input or rule related to exception handling, predict the result, '
                            'and only then run the program.',
    'practical_example': 'Imagine a small exception handling feature in a student or inventory program. Decide what '
                         'data enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing exception syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make exception behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each exception before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Create a safe conversion or validation function that throws a meaningful standard exception for '
                'invalid input.',
    'practice_problem': '**Exception Handling independent practice:** Create a safe conversion or validation function '
                        'that throws a meaningful standard exception for invalid input. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Exception Handling:** Run the program with a normal case, a boundary case, '
                       'and a misuse/invalid case when relevant. For each case, record the actual result and compare '
                       'it with the requirement. A correct submission must preserve the lesson rule and handle the '
                       'defined edge case safely.',
    'mastery_quiz': [ [ 'Exception Handling: Which block contains code that may throw?',
                        ['try', 'catch', 'finally-only', 'throw-only'],
                        0,
                        'try encloses code whose exceptions may be handled.'],
                      [ 'What does catch do?',
                        [ 'Handles a matching exception',
                          'Creates a loop',
                          'Reads a file automatically',
                          'Declares a class'],
                        0,
                        'catch receives an exception of a matching type.'],
                      [ 'What does throw do?',
                        [ 'Signals an exception',
                          'Ends every program successfully',
                          'Sorts a collection',
                          'Allocates memory'],
                        0,
                        'throw raises an exception.'],
                      [ 'Why should exceptions not replace ordinary validation everywhere?',
                        [ 'Expected invalid input is often clearer as normal control flow',
                          'Exceptions cannot contain messages',
                          'Validation is illegal',
                          'Catch cannot run'],
                        0,
                        'Use normal branches for expected conditions and exceptions for exceptional failures.'],
                      [ 'What makes a custom exception useful?',
                        [ 'It can communicate a domain-specific failure',
                          'It automatically fixes bugs',
                          'It removes tests',
                          'It changes a primitive type'],
                        0,
                        'Custom exceptions can express meaningful domain failures.']],
    'summary': 'You should now be able to explain exception handling, recognize its syntax, trace the worked example, '
               'and use the concept in a small original program.',
    'next_lesson': 'File I/O',
    'rules': [ 'Name and trace the role of each exception before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the exception handling '
            'exercise.',
    'extension': 'Add one realistic requirement to the exception handling exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain exception handling without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_24'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Exception Handling matters because useful programs must detect, explain, and recover from '
                      'incorrect states instead of silently failing.',
    'guided_practice': [ '1. Restate the goal of **Exception Handling** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Exception '
                         'Handling**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Exception Handling** task: Create a safe conversion or '
                            'validation function that throws a meaningful standard exception for invalid input. Then '
                            'create one small variation that changes an input, rule, or data case without changing the '
                            'main goal.',
    'debug_task': 'Debug a deliberately small **Exception Handling** program that exhibits this common mistake: '
                  '**Memorizing exception syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Exception Handling** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what exception handling means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for exception handling.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small exception handling example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Exception Handling.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Exception Handling without violating the '
                                  'stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['error', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_26',
    'title': 'File I/O',
    'description': 'Persist simple data using ifstream, ofstream, fstream, append mode, stream state checks, and '
                   'line/token reading.',
    'stage': 'Object-Oriented Programming',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **File I/O**, understand why it is useful, trace a focused example, '
                    'practice it with guidance, then solve an independent variation. You will finish by proving your '
                    'understanding through concept, syntax, code-reading, debugging, and application checks.',
    'learning_objectives': [ 'Explain what file i/o means and why it exists.',
                             'Read and write the core syntax used for file i/o.',
                             'Predict the behavior of a small file i/o example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['Path', 'Files', 'encoding', 'exception'],
    'explanation': 'Persist simple data using ifstream, ofstream, fstream, append mode, stream state checks, and '
                   'line/token reading. C++ syntax is shown with the standard library names used in this lesson. Read '
                   'the declaration from left to right: identify the type or template, the name, the operation, and '
                   'the terminating punctuation.',
    'syntax': 'ofstream out("scores.txt");\nif (!out) return 1;\nout << "Ren 95\\n";\nout.close();',
    'syntax_breakdown': [ 'Focus on Path: identify what it represents and what role it plays in the statement.',
                          'Next inspect Files: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'ofstream out("scores.txt");\nif (!out) return 1;\nout << "Ren 95\\n";\nout.close();',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'ofstream out("notes.txt");\n'
                'out << "ClassCode" << "\\n";\n'
                'out.close();\n'
                'ifstream in("notes.txt");\n'
                'string line; getline(in, line); cout << line;',
    'example2_explanation': 'Change one meaningful input or rule related to file i/o, predict the result, and only '
                            'then run the program.',
    'practical_example': 'Imagine a small file i/o feature in a student or inventory program. Decide what data enters '
                         'the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing Path syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make Path behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each Path before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Write student records to a file and later read them back into memory.',
    'practice_problem': '**File I/O independent practice:** Write student records to a file and later read them back '
                        'into memory. You must also add one clearly different variation and test it. Your work should '
                        "demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for File I/O:** Run the program with a normal case, a boundary case, and a '
                       'misuse/invalid case when relevant. For each case, record the actual result and compare it with '
                       'the requirement. A correct submission must preserve the lesson rule and handle the defined '
                       'edge case safely.',
    'mastery_quiz': [ [ 'File I/O: What should you check before assuming a file operation succeeded?',
                        [ 'The operation result or exception state',
                          'Only the filename length',
                          'The loop counter',
                          'The class name'],
                        0,
                        'I/O can fail and should be handled explicitly.'],
                      [ 'What is append mode for?',
                        [ 'Adding new data without replacing existing contents',
                          'Reading only',
                          'Deleting the file',
                          'Sorting lines'],
                        0,
                        'Append writes after existing content.'],
                      [ 'Why close or scope file resources correctly?',
                        [ 'To release system resources and flush pending work',
                          'To change the file extension',
                          'To speed up every CPU instruction',
                          'To create classes'],
                        0,
                        'Resources should be released predictably.'],
                      [ 'What is a path?',
                        [ 'A representation of a file or directory location',
                          'A loop condition',
                          'A primitive type',
                          'A thread'],
                        0,
                        'A path identifies a filesystem location.'],
                      [ 'Why test missing files?',
                        [ 'They are a normal failure case',
                          'They can never happen',
                          'They change Java into C++',
                          'They remove permissions'],
                        0,
                        'Real applications must handle absent or inaccessible files.']],
    'summary': 'You should now be able to explain file i/o, recognize its syntax, trace the worked example, and use '
               'the concept in a small original program.',
    'next_lesson': 'Iterators & STL Containers',
    'rules': [ 'Name and trace the role of each Path before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the file i/o exercise.',
    'extension': 'Add one realistic requirement to the file i/o exercise while keeping the original behavior correct.',
    'learning_checks': [ 'Can I explain file i/o without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_25'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'File I/O matters because programs often need to preserve, load, or exchange information outside '
                      'a single run.',
    'guided_practice': [ '1. Restate the goal of **File I/O** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **File I/O**, then '
                         'change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **File I/O** task: Write student records to a file and later '
                            'read them back into memory. Then create one small variation that changes an input, rule, '
                            'or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **File I/O** program that exhibits this common mistake: **Memorizing '
                  'Path syntax without being able to explain what changes in the program.**. Before changing code, '
                  'identify the first incorrect value, state, control-flow decision, or ownership assumption; then '
                  'explain the fix in one sentence.',
    'transfer_task': 'Transfer **File I/O** to a small real-world feature. Keep the same core rule, but change the '
                     'context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what file i/o means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for file i/o.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small file i/o example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for File I/O.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for File I/O without violating the stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['io', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_27',
    'title': 'Iterators & STL Containers',
    'description': 'Understand iterator ranges, begin/end, traversal, and how iterator-based algorithms connect '
                   'containers to reusable library operations.',
    'stage': 'Object-Oriented Programming',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Iterators & STL Containers**, understand why it is useful, trace '
                    'a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what iterators & stl containers means and why it exists.',
                             'Read and write the core syntax used for iterators & stl containers.',
                             'Predict the behavior of a small iterators & stl containers example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['iterator', 'begin', 'end', 'range'],
    'explanation': 'Understand iterator ranges, begin/end, traversal, and how iterator-based algorithms connect '
                   'containers to reusable library operations. C++ syntax is shown with the standard library names '
                   'used in this lesson. Read the declaration from left to right: identify the type or template, the '
                   'name, the operation, and the terminating punctuation.',
    'syntax': 'vector<int> values{4, 1, 9};\n'
              'for (auto it = values.begin(); it != values.end(); ++it) {\n'
              '    cout << *it << " ";\n'
              '}',
    'syntax_breakdown': [ 'Focus on iterator: identify what it represents and what role it plays in the statement.',
                          'Next inspect begin: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'vector<int> values{4, 1, 9};\n'
                'for (auto it = values.begin(); it != values.end(); ++it) {\n'
                '    cout << *it << " ";\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'vector<int> v{3,1,2};\nfor (auto it=v.begin(); it!=v.end(); ++it) cout << *it << " ";',
    'example2_explanation': 'Change one meaningful input or rule related to iterators & stl containers, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small iterators & stl containers feature in a student or inventory program. Decide '
                         'what data enters the feature, what rule the feature applies, and what result it should '
                         'produce.',
    'common_mistakes': [ 'Memorizing iterator syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make iterator behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each iterator before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Traverse a vector with iterators, modify one matching value, and explain what end() represents.',
    'practice_problem': '**Iterators & STL Containers independent practice:** Traverse a vector with iterators, modify '
                        'one matching value, and explain what end() represents. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Iterators & STL Containers:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Iterators & STL Containers: What does begin() represent in a C++ container?',
                        ['An iterator to the first element', 'The last element', 'The container size', 'A new object'],
                        0,
                        'begin points to the first element.'],
                      [ 'What does end() represent?',
                        [ 'The position one past the last element',
                          'The last element itself',
                          'The first element',
                          'The capacity'],
                        0,
                        'end marks the end of the iterator range.'],
                      [ 'Why do algorithms use iterator ranges?',
                        [ 'They can work across many container types',
                          'They require global variables',
                          'They avoid all comparisons',
                          'They only work with arrays'],
                        0,
                        'Iterator ranges decouple algorithms from a particular container.'],
                      [ 'What does dereferencing an iterator usually provide?',
                        ['The element at its position', 'The container type', 'The compiler', 'The memory allocator'],
                        0,
                        'Dereferencing accesses the element.'],
                      [ 'What should you avoid?',
                        [ 'Using an invalidated iterator',
                          'Checking begin/end',
                          'Reading an element',
                          'Testing an empty container'],
                        0,
                        'Iterator invalidation can make an iterator unsafe to use.']],
    'summary': 'You should now be able to explain iterators & stl containers, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'STL Algorithms',
    'rules': [ 'Name and trace the role of each iterator before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the iterators & stl '
            'containers exercise.',
    'extension': 'Add one realistic requirement to the iterators & stl containers exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain iterators & stl containers without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_26'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Iterators & STL Containers gives you the foundation needed to read, change, and reason about a '
                      'program before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Iterators & STL Containers** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Iterators & STL '
                         'Containers**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Iterators & STL Containers** task: Traverse a vector with '
                            'iterators, modify one matching value, and explain what end() represents. Then create one '
                            'small variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Iterators & STL Containers** program that exhibits this common '
                  'mistake: **Memorizing iterator syntax without being able to explain what changes in the program.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Iterators & STL Containers** to a small real-world feature. Keep the same core rule, '
                     'but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what iterators & stl containers means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for iterators & stl containers.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small iterators & stl containers example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Iterators & STL Containers.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Iterators & STL Containers without violating '
                                  'the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Iterators & '
                                  'STL Containers.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_28',
    'title': 'STL Algorithms',
    'description': 'Use standard algorithms such as sort, find, count, reverse, binary_search, lower_bound, and '
                   'upper_bound instead of rewriting common loops.',
    'stage': 'Object-Oriented Programming',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **STL Algorithms**, understand why it is useful, trace a focused '
                    'example, practice it with guidance, then solve an independent variation. You will finish by '
                    'proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what stl algorithms means and why it exists.',
                             'Read and write the core syntax used for stl algorithms.',
                             'Predict the behavior of a small stl algorithms example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['algorithm', 'range', 'predicate', 'iterator'],
    'explanation': 'Use standard algorithms such as sort, find, count, reverse, binary_search, lower_bound, and '
                   'upper_bound instead of rewriting common loops. C++ syntax is shown with the standard library names '
                   'used in this lesson. Read the declaration from left to right: identify the type or template, the '
                   'name, the operation, and the terminating punctuation.',
    'syntax': 'vector<int> values{4, 1, 9, 1};\n'
              'sort(values.begin(), values.end());\n'
              'cout << count(values.begin(), values.end(), 1);',
    'syntax_breakdown': [ 'Focus on algorithm: identify what it represents and what role it plays in the statement.',
                          'Next inspect range: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'vector<int> values{4, 1, 9, 1};\n'
                'sort(values.begin(), values.end());\n'
                'cout << count(values.begin(), values.end(), 1);',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'vector<int> v{7,2,5,2};\n'
                'sort(v.begin(), v.end());\n'
                'auto it=find(v.begin(), v.end(), 5);\n'
                'cout << (it != v.end());',
    'example2_explanation': 'Change one meaningful input or rule related to stl algorithms, predict the result, and '
                            'only then run the program.',
    'practical_example': 'Imagine a small stl algorithms feature in a student or inventory program. Decide what data '
                         'enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing algorithm syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make algorithm behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each algorithm before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Sort scores, search for a target, count duplicates, and use lower_bound on the sorted sequence.',
    'practice_problem': '**STL Algorithms independent practice:** Sort scores, search for a target, count duplicates, '
                        'and use lower_bound on the sorted sequence. You must also add one clearly different variation '
                        "and test it. Your work should demonstrate the lesson's main rule, not merely reproduce "
                        'Example 1.',
    'expected_output': '**Test contract for STL Algorithms:** Run the program with a normal case, a boundary case, and '
                       'a misuse/invalid case when relevant. For each case, record the actual result and compare it '
                       'with the requirement. A correct submission must preserve the lesson rule and handle the '
                       'defined edge case safely.',
    'mastery_quiz': [ [ 'STL Algorithms: What does sort do to a range?',
                        [ 'Orders the elements according to a comparison',
                          'Counts files',
                          'Creates a class',
                          'Reads input'],
                        0,
                        'sort rearranges a range into an order.'],
                      [ 'What does binary search require conceptually?',
                        ['An ordered range', 'An empty program', 'A class hierarchy', 'A file stream'],
                        0,
                        'Binary search relies on sorted/ordered data.'],
                      [ 'What does find return in C++?',
                        ['An iterator to the match or end if absent', 'A Boolean only', 'A file', 'A class'],
                        0,
                        'std::find returns an iterator.'],
                      [ 'Why use a comparator?',
                        [ 'To define a custom ordering',
                          'To allocate memory',
                          'To read a database',
                          'To catch exceptions'],
                        0,
                        'Comparators tell sorting algorithms how elements should be ordered.'],
                      [ 'What is a good algorithm test?',
                        [ 'Include duplicates, empty input, and already-ordered data',
                          'Only one random value',
                          'No expected result',
                          'Only compilation'],
                        0,
                        'Different shapes of input reveal different algorithm bugs.']],
    'summary': 'You should now be able to explain stl algorithms, recognize its syntax, trace the worked example, and '
               'use the concept in a small original program.',
    'next_lesson': 'Maps, Sets, Pairs & Tuples',
    'rules': [ 'Name and trace the role of each algorithm before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the stl algorithms '
            'exercise.',
    'extension': 'Add one realistic requirement to the stl algorithms exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain stl algorithms without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_27'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'STL Algorithms matters because solving a problem correctly also requires choosing an approach '
                      'that scales and can be reasoned about.',
    'guided_practice': [ '1. Restate the goal of **STL Algorithms** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **STL Algorithms**, '
                         'then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **STL Algorithms** task: Sort scores, search for a target, count '
                            'duplicates, and use lower_bound on the sorted sequence. Then create one small variation '
                            'that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **STL Algorithms** program that exhibits this common mistake: '
                  '**Memorizing algorithm syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **STL Algorithms** to a small real-world feature. Keep the same core rule, but change '
                     'the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what stl algorithms means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for stl algorithms.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small stl algorithms example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for STL Algorithms.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for STL Algorithms without violating the stated '
                                  'rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['algorithm', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_29',
    'title': 'Maps, Sets, Pairs & Tuples',
    'description': 'Choose associative containers for keys, uniqueness, frequency counting, and multi-value records '
                   'using map, set, unordered_map, pair, and tuple.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Maps, Sets, Pairs & Tuples**, understand why it is useful, trace '
                    'a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what maps, sets, pairs & tuples means and why it exists.',
                             'Read and write the core syntax used for maps, sets, pairs & tuples.',
                             'Predict the behavior of a small maps, sets, pairs & tuples example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['associative container', 'key', 'uniqueness', 'structured value'],
    'explanation': 'Choose associative containers for keys, uniqueness, frequency counting, and multi-value records '
                   'using map, set, unordered_map, pair, and tuple. C++ syntax is shown with the standard library '
                   'names used in this lesson. Read the declaration from left to right: identify the type or template, '
                   'the name, the operation, and the terminating punctuation.',
    'syntax': 'map<string, int> counts;\ncounts["apple"]++;\ncounts["apple"]++;\ncout << counts["apple"];',
    'syntax_breakdown': [ 'Focus on associative container: identify what it represents and what role it plays in the '
                          'statement.',
                          'Next inspect key: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'map<string, int> counts;\ncounts["apple"]++;\ncounts["apple"]++;\ncout << counts["apple"];',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'unordered_map<string,int> scores{{"Ren",95},{"Mika",88}};\n'
                'if (scores.contains("Ren")) cout << scores["Ren"];',
    'example2_explanation': 'Change one meaningful input or rule related to maps, sets, pairs & tuples, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small maps, sets, pairs & tuples feature in a student or inventory program. Decide '
                         'what data enters the feature, what rule the feature applies, and what result it should '
                         'produce.',
    'common_mistakes': [ 'Memorizing associative container syntax without being able to explain what changes in the '
                         'program.',
                         'Ignoring the boundary or lifetime rules that make associative container behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each associative container before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Build a word-frequency counter and compare when map, unordered_map, and set are appropriate.',
    'practice_problem': '**Maps, Sets, Pairs & Tuples independent practice:** Build a word-frequency counter and '
                        'compare when map, unordered_map, and set are appropriate. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Maps, Sets, Pairs & Tuples:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Maps, Sets, Pairs & Tuples: What is a map primarily for?',
                        ['Key-to-value association', 'Only sequential output', 'Only inheritance', 'Compiler settings'],
                        0,
                        'Maps associate keys with values.'],
                      [ 'What is a set primarily for?',
                        ['Unique values', 'Duplicate indexing', 'File bytes only', 'Method return types'],
                        0,
                        'Sets model uniqueness.'],
                      [ 'When is a frequency map useful?',
                        [ 'Counting how often keys occur',
                          'Drawing GUI buttons',
                          'Managing threads only',
                          'Compiling headers'],
                        0,
                        'A map can increment a count for each observed key.'],
                      [ 'Why choose a collection based on access pattern?',
                        [ 'Different structures have different ordering and lookup behavior',
                          'All collections behave identically',
                          'It changes Java into C++',
                          'It prevents testing'],
                        0,
                        'The right structure makes intended operations clearer and often more efficient.'],
                      [ 'What should you test with a map?',
                        ['Missing keys and repeated keys', 'Only one hard-coded key', 'No input', 'Only compilation'],
                        0,
                        'Missing and repeated keys reveal common logic errors.']],
    'summary': 'You should now be able to explain maps, sets, pairs & tuples, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Recursion',
    'rules': [ 'Name and trace the role of each associative container before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the maps, sets, pairs & '
            'tuples exercise.',
    'extension': 'Add one realistic requirement to the maps, sets, pairs & tuples exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain maps, sets, pairs & tuples without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_28'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Maps, Sets, Pairs & Tuples matters because programs often need to store, find, update, and '
                      'process groups of related values.',
    'guided_practice': [ '1. Restate the goal of **Maps, Sets, Pairs & Tuples** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Maps, Sets, Pairs '
                         '& Tuples**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Maps, Sets, Pairs & Tuples** task: Build a word-frequency '
                            'counter and compare when map, unordered_map, and set are appropriate. Then create one '
                            'small variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Maps, Sets, Pairs & Tuples** program that exhibits this common '
                  'mistake: **Memorizing associative container syntax without being able to explain what changes in '
                  'the program.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Maps, Sets, Pairs & Tuples** to a small real-world feature. Keep the same core rule, '
                     'but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what maps, sets, pairs & tuples means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for maps, sets, pairs & tuples.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small maps, sets, pairs & tuples example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Maps, Sets, Pairs & Tuples.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Maps, Sets, Pairs & Tuples without violating '
                                  'the stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['collection', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_30',
    'title': 'Recursion',
    'description': 'Solve a problem by reducing it to smaller instances, with a base case and progress toward '
                   'termination.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Recursion**, understand why it is useful, trace a focused '
                    'example, practice it with guidance, then solve an independent variation. You will finish by '
                    'proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what recursion means and why it exists.',
                             'Read and write the core syntax used for recursion.',
                             'Predict the behavior of a small recursion example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['base case', 'recursive case', 'stack frame', 'termination'],
    'explanation': 'Solve a problem by reducing it to smaller instances, with a base case and progress toward '
                   'termination. C++ syntax is shown with the standard library names used in this lesson. Read the '
                   'declaration from left to right: identify the type or template, the name, the operation, and the '
                   'terminating punctuation.',
    'syntax': 'int factorial(int n) {\n    if (n <= 1) return 1;\n    return n * factorial(n - 1);\n}',
    'syntax_breakdown': [ 'Focus on base case: identify what it represents and what role it plays in the statement.',
                          'Next inspect recursive case: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'int factorial(int n) {\n    if (n <= 1) return 1;\n    return n * factorial(n - 1);\n}',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'int sumTo(int n) {\n    if (n == 0) return 0;\n    return n + sumTo(n-1);\n}',
    'example2_explanation': 'Change one meaningful input or rule related to recursion, predict the result, and only '
                            'then run the program.',
    'practical_example': 'Imagine a small recursion feature in a student or inventory program. Decide what data enters '
                         'the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing base case syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make base case behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each base case before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Implement recursive factorial and recursive sum, then identify the base case and recursive step.',
    'practice_problem': '**Recursion independent practice:** Implement recursive factorial and recursive sum, then '
                        'identify the base case and recursive step. You must also add one clearly different variation '
                        "and test it. Your work should demonstrate the lesson's main rule, not merely reproduce "
                        'Example 1.',
    'expected_output': '**Test contract for Recursion:** Run the program with a normal case, a boundary case, and a '
                       'misuse/invalid case when relevant. For each case, record the actual result and compare it with '
                       'the requirement. A correct submission must preserve the lesson rule and handle the defined '
                       'edge case safely.',
    'mastery_quiz': [ [ 'Recursion: What stops a recursive function?',
                        ['A base case', 'A larger input', 'A global variable', 'A compiler flag'],
                        0,
                        'The base case stops further recursive calls.'],
                      [ 'What should each recursive call do?',
                        [ 'Move toward the base case',
                          'Make the problem larger forever',
                          'Skip all parameters',
                          'Delete the stack'],
                        0,
                        'Progress toward termination is essential.'],
                      [ 'What resource grows with recursive calls?',
                        ['Call stack frames', 'The source file', 'The keyboard buffer', 'The package name'],
                        0,
                        'Each active call has a stack frame.'],
                      [ 'Why test the smallest input?',
                        [ 'It validates the base case',
                          'It guarantees no recursion',
                          'It avoids all logic',
                          'It compiles the code'],
                        0,
                        'The smallest case usually exercises the base case directly.'],
                      [ 'What is a risk of deep recursion?',
                        [ 'Stack exhaustion',
                          'Automatic sorting',
                          'File corruption by default',
                          'Changing the type system'],
                        0,
                        'Very deep recursion can exhaust stack space.']],
    'summary': 'You should now be able to explain recursion, recognize its syntax, trace the worked example, and use '
               'the concept in a small original program.',
    'next_lesson': 'Big-O & Complexity',
    'rules': [ 'Name and trace the role of each base case before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the recursion exercise.',
    'extension': 'Add one realistic requirement to the recursion exercise while keeping the original behavior correct.',
    'learning_checks': [ 'Can I explain recursion without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_29'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Recursion matters because solving a problem correctly also requires choosing an approach that '
                      'scales and can be reasoned about.',
    'guided_practice': [ '1. Restate the goal of **Recursion** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Recursion**, then '
                         'change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Recursion** task: Implement recursive factorial and recursive '
                            'sum, then identify the base case and recursive step. Then create one small variation that '
                            'changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Recursion** program that exhibits this common mistake: **Memorizing '
                  'base case syntax without being able to explain what changes in the program.**. Before changing '
                  'code, identify the first incorrect value, state, control-flow decision, or ownership assumption; '
                  'then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Recursion** to a small real-world feature. Keep the same core rule, but change the '
                     'context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what recursion means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for recursion.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small recursion example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Recursion.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Recursion without violating the stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['algorithm', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_31',
    'title': 'Big-O & Complexity',
    'description': 'Estimate how time and memory grow with input size and use complexity to compare otherwise-correct '
                   'solutions.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Big-O & Complexity**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what big-o & complexity means and why it exists.',
                             'Read and write the core syntax used for big-o & complexity.',
                             'Predict the behavior of a small big-o & complexity example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['input size', 'time complexity', 'space complexity', 'growth'],
    'explanation': 'Estimate how time and memory grow with input size and use complexity to compare otherwise-correct '
                   'solutions. C++ syntax is shown with the standard library names used in this lesson. Read the '
                   'declaration from left to right: identify the type or template, the name, the operation, and the '
                   'terminating punctuation.',
    'syntax': 'for (int i = 0; i < n; ++i) {\n    cout << i;\n}\n// O(n)',
    'syntax_breakdown': [ 'Focus on input size: identify what it represents and what role it plays in the statement.',
                          'Next inspect time complexity: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'for (int i = 0; i < n; ++i) {\n    cout << i;\n}\n// O(n)',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'bool contains(const vector<int>& v, int target) {\n'
                '    for (int x : v) if (x == target) return true;\n'
                '    return false;\n'
                '}\n'
                '// O(n) time, O(1) extra space.',
    'example2_explanation': 'Change one meaningful input or rule related to big-o & complexity, predict the result, '
                            'and only then run the program.',
    'practical_example': 'Imagine a small big-o & complexity feature in a student or inventory program. Decide what '
                         'data enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing input size syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make input size behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each input size before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Compare a linear scan, nested loop, and binary search and explain their growth rates.',
    'practice_problem': '**Big-O & Complexity independent practice:** Compare a linear scan, nested loop, and binary '
                        'search and explain their growth rates. You must also add one clearly different variation and '
                        "test it. Your work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Big-O & Complexity:** Run the program with a normal case, a boundary case, '
                       'and a misuse/invalid case when relevant. For each case, record the actual result and compare '
                       'it with the requirement. A correct submission must preserve the lesson rule and handle the '
                       'defined edge case safely.',
    'mastery_quiz': [ [ 'Big-O & Complexity: What does O(n) describe?',
                        [ 'Linear growth with input size',
                          'Constant growth only',
                          'Always quadratic growth',
                          'A programming language'],
                        0,
                        'O(n) means work grows proportionally with n.'],
                      [ 'What is O(1)?',
                        [ 'Constant-time growth with respect to input size',
                          'One loop exactly',
                          'One variable',
                          'One file'],
                        0,
                        'O(1) does not grow with n in the modeled operation.'],
                      [ 'Why does nested iteration often suggest O(n²)?',
                        [ 'Each of n items may cause another n-sized pass',
                          'Because C++ is slow',
                          'Because Java has objects',
                          'Because loops cannot terminate'],
                        0,
                        'Two independent n-sized loops often multiply to n² work.'],
                      [ 'What does space complexity measure?',
                        [ 'How extra memory grows with input',
                          'Only CPU speed',
                          'Only source-code length',
                          'Network bandwidth'],
                        0,
                        'Space complexity models memory growth.'],
                      [ 'Why analyze complexity after correctness?',
                        [ 'An incorrect fast algorithm is still wrong',
                          'Complexity replaces tests',
                          'Correctness is optional',
                          'Big-O compiles code'],
                        0,
                        'Correctness is required before performance optimization matters.']],
    'summary': 'You should now be able to explain big-o & complexity, recognize its syntax, trace the worked example, '
               'and use the concept in a small original program.',
    'next_lesson': 'Templates & Generic Programming',
    'rules': [ 'Name and trace the role of each input size before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the big-o & complexity '
            'exercise.',
    'extension': 'Add one realistic requirement to the big-o & complexity exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain big-o & complexity without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_30'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Big-O & Complexity matters because solving a problem correctly also requires choosing an '
                      'approach that scales and can be reasoned about.',
    'guided_practice': [ '1. Restate the goal of **Big-O & Complexity** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Big-O & '
                         'Complexity**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Big-O & Complexity** task: Compare a linear scan, nested loop, '
                            'and binary search and explain their growth rates. Then create one small variation that '
                            'changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Big-O & Complexity** program that exhibits this common mistake: '
                  '**Memorizing input size syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Big-O & Complexity** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what big-o & complexity means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for big-o & complexity.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small big-o & complexity example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Big-O & Complexity.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Big-O & Complexity without violating the '
                                  'stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['algorithm', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_32',
    'title': 'Templates & Generic Programming',
    'description': 'Write type-independent algorithms and data structures with function templates, class templates, '
                   'template parameters, and constraints-friendly thinking.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Templates & Generic Programming**, understand why it is useful, '
                    'trace a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what templates & generic programming means and why it exists.',
                             'Read and write the core syntax used for templates & generic programming.',
                             'Predict the behavior of a small templates & generic programming example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['template parameter', 'instantiation', 'generic code', 'constraint'],
    'explanation': 'Write type-independent algorithms and data structures with function templates, class templates, '
                   'template parameters, and constraints-friendly thinking. C++ syntax is shown with the standard '
                   'library names used in this lesson. Read the declaration from left to right: identify the type or '
                   'template, the name, the operation, and the terminating punctuation.',
    'syntax': 'template <typename T>\nT maximum(T a, T b) {\n    return a > b ? a : b;\n}',
    'syntax_breakdown': [ 'Focus on template parameter: identify what it represents and what role it plays in the '
                          'statement.',
                          'Next inspect instantiation: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'template <typename T>\nT maximum(T a, T b) {\n    return a > b ? a : b;\n}',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'template <typename T>\nvoid printTwice(T value) { cout << value << " " << value; }\nprintTwice(4);',
    'example2_explanation': 'Change one meaningful input or rule related to templates & generic programming, predict '
                            'the result, and only then run the program.',
    'practical_example': 'Imagine a small templates & generic programming feature in a student or inventory program. '
                         'Decide what data enters the feature, what rule the feature applies, and what result it '
                         'should produce.',
    'common_mistakes': [ 'Memorizing template parameter syntax without being able to explain what changes in the '
                         'program.',
                         'Ignoring the boundary or lifetime rules that make template parameter behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each template parameter before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Create a generic max function and test it with integers and doubles.',
    'practice_problem': '**Templates & Generic Programming independent practice:** Create a generic max function and '
                        'test it with integers and doubles. You must also add one clearly different variation and test '
                        "it. Your work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Templates & Generic Programming:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Templates & Generic Programming: What does a C++ function template provide?',
                        [ 'A way to generate type-specific versions from generic code',
                          'A runtime database',
                          'A thread',
                          'A file stream'],
                        0,
                        'Templates enable generic programming at compile time.'],
                      [ 'What does a template parameter represent?',
                        ['A type or value supplied to the template', 'Only a variable name', 'A comment', 'A package'],
                        0,
                        'Template parameters are placeholders used when instantiating templates.'],
                      [ 'Why constrain a generic algorithm?',
                        [ 'To state what operations the type must support',
                          'To remove all types',
                          'To disable compilation',
                          'To create a GUI'],
                        0,
                        'Constraints communicate valid template arguments.'],
                      [ 'What is specialization?',
                        [ 'Providing a tailored implementation for a particular template case',
                          'Renaming a variable',
                          'Deleting a type',
                          'Creating a loop'],
                        0,
                        'Specialization customizes template behavior.'],
                      [ 'What is a benefit of generic code?',
                        [ 'Reuse across compatible types',
                          'No need for testing',
                          'No compilation required',
                          'Automatic correctness'],
                        0,
                        'Generic code can reuse algorithms while preserving type checking.']],
    'summary': 'You should now be able to explain templates & generic programming, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Lambda Expressions',
    'rules': [ 'Name and trace the role of each template parameter before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the templates & generic '
            'programming exercise.',
    'extension': 'Add one realistic requirement to the templates & generic programming exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain templates & generic programming without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_31'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Templates & Generic Programming matters because reusable code should avoid unnecessary '
                      'duplication while remaining type-safe.',
    'guided_practice': [ '1. Restate the goal of **Templates & Generic Programming** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Templates & '
                         'Generic Programming**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Templates & Generic Programming** task: Create a generic max '
                            'function and test it with integers and doubles. Then create one small variation that '
                            'changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Templates & Generic Programming** program that exhibits this common '
                  'mistake: **Memorizing template parameter syntax without being able to explain what changes in the '
                  'program.**. Before changing code, identify the first incorrect value, state, control-flow decision, '
                  'or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Templates & Generic Programming** to a small real-world feature. Keep the same core '
                     'rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what templates & generic programming means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for templates & generic '
                                                 'programming.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small templates & generic programming '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Templates & Generic '
                                  'Programming.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Templates & Generic Programming without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Templates & '
                                  'Generic Programming.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['generic', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_33',
    'title': 'Lambda Expressions',
    'description': 'Create short callable objects inline, capture local state, and pass behavior into algorithms.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Lambda Expressions**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what lambda expressions means and why it exists.',
                             'Read and write the core syntax used for lambda expressions.',
                             'Predict the behavior of a small lambda expressions example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['lambda', 'functional interface', 'capture', 'method reference'],
    'explanation': 'Create short callable objects inline, capture local state, and pass behavior into algorithms. C++ '
                   'syntax is shown with the standard library names used in this lesson. Read the declaration from '
                   'left to right: identify the type or template, the name, the operation, and the terminating '
                   'punctuation.',
    'syntax': 'vector<int> v{1,2,3,4};\n'
              'int limit = 2;\n'
              'auto bigger = [limit](int x) { return x > limit; };\n'
              'cout << count_if(v.begin(), v.end(), bigger);',
    'syntax_breakdown': [ 'Focus on lambda: identify what it represents and what role it plays in the statement.',
                          'Next inspect functional interface: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'vector<int> v{1,2,3,4};\n'
                'int limit = 2;\n'
                'auto bigger = [limit](int x) { return x > limit; };\n'
                'cout << count_if(v.begin(), v.end(), bigger);',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'vector<int> v{1,2,3,4,5};\n'
                'int even = count_if(v.begin(), v.end(), [](int x){ return x % 2 == 0; });\n'
                'cout << even;',
    'example2_explanation': 'Change one meaningful input or rule related to lambda expressions, predict the result, '
                            'and only then run the program.',
    'practical_example': 'Imagine a small lambda expressions feature in a student or inventory program. Decide what '
                         'data enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing lambda syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make lambda behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each lambda before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Use a lambda with count_if or sort to express a small rule without creating a separate named '
                'function.',
    'practice_problem': '**Lambda Expressions independent practice:** Use a lambda with count_if or sort to express a '
                        'small rule without creating a separate named function. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Lambda Expressions:** Run the program with a normal case, a boundary case, '
                       'and a misuse/invalid case when relevant. For each case, record the actual result and compare '
                       'it with the requirement. A correct submission must preserve the lesson rule and handle the '
                       'defined edge case safely.',
    'mastery_quiz': [ [ 'Lambda Expressions: What is a lambda?',
                        ['A compact function-like expression', 'A file stream', 'A class file', 'A compiler'],
                        0,
                        'Lambdas represent callable behavior.'],
                      [ 'What is a capture in a C++ lambda?',
                        [ 'How surrounding local variables are made available',
                          'A file handle',
                          'A thread lock',
                          'A return type'],
                        0,
                        'Capture controls access to surrounding variables.'],
                      [ 'Why are lambdas useful with algorithms?',
                        [ 'They can provide short local behavior such as predicates',
                          'They remove containers',
                          'They avoid testing',
                          'They compile without types'],
                        0,
                        'Algorithms often need small pieces of behavior.'],
                      [ 'What is a predicate?',
                        [ 'A callable that returns a Boolean-like decision',
                          'A file path',
                          'A class constructor',
                          'A numeric type'],
                        0,
                        'Predicates answer a yes/no condition.'],
                      [ 'What should a lambda ideally do?',
                        [ 'Express one focused piece of behavior',
                          'Replace the entire application',
                          'Hide all state',
                          'Ignore parameters'],
                        0,
                        'Focused lambdas are easier to read and reuse locally.']],
    'summary': 'You should now be able to explain lambda expressions, recognize its syntax, trace the worked example, '
               'and use the concept in a small original program.',
    'next_lesson': 'Smart Pointers & RAII',
    'rules': [ 'Name and trace the role of each lambda before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the lambda expressions '
            'exercise.',
    'extension': 'Add one realistic requirement to the lambda expressions exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain lambda expressions without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_32'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Lambda Expressions matters because modern code often transforms data and composes behavior in '
                      'compact, reusable ways.',
    'guided_practice': [ '1. Restate the goal of **Lambda Expressions** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Lambda '
                         'Expressions**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Lambda Expressions** task: Use a lambda with count_if or sort '
                            'to express a small rule without creating a separate named function. Then create one small '
                            'variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Lambda Expressions** program that exhibits this common mistake: '
                  '**Memorizing lambda syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Lambda Expressions** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what lambda expressions means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for lambda expressions.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small lambda expressions example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Lambda Expressions.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Lambda Expressions without violating the '
                                  'stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Lambda '
                                  'Expressions.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['functional', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_34',
    'title': 'Smart Pointers & RAII',
    'description': 'Use unique_ptr, shared_ptr, and weak_ptr to express ownership and automatic cleanup, and recognize '
                   'when shared ownership is unnecessary.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Smart Pointers & RAII**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what smart pointers & raii means and why it exists.',
                             'Read and write the core syntax used for smart pointers & raii.',
                             'Predict the behavior of a small smart pointers & raii example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['unique_ptr', 'shared_ptr', 'weak_ptr', 'ownership'],
    'explanation': 'Use unique_ptr, shared_ptr, and weak_ptr to express ownership and automatic cleanup, and recognize '
                   'when shared ownership is unnecessary. C++ syntax is shown with the standard library names used in '
                   'this lesson. Read the declaration from left to right: identify the type or template, the name, the '
                   'operation, and the terminating punctuation.',
    'syntax': 'auto item = make_unique<string>("hello");\ncout << *item;',
    'syntax_breakdown': [ 'Focus on unique_ptr: identify what it represents and what role it plays in the statement.',
                          'Next inspect shared_ptr: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'auto item = make_unique<string>("hello");\ncout << *item;',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'int value = 7;\nint* p = &value;\n*p = 11;\ncout << value;',
    'example2_explanation': 'Change one meaningful input or rule related to smart pointers & raii, predict the result, '
                            'and only then run the program.',
    'practical_example': 'Imagine a small smart pointers & raii feature in a student or inventory program. Decide what '
                         'data enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing unique_ptr syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make unique_ptr behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each unique_ptr before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Rewrite a raw-pointer ownership example using unique_ptr and explain who owns the resource.',
    'practice_problem': '**Smart Pointers & RAII independent practice:** Rewrite a raw-pointer ownership example using '
                        'unique_ptr and explain who owns the resource. You must also add one clearly different '
                        "variation and test it. Your work should demonstrate the lesson's main rule, not merely "
                        'reproduce Example 1.',
    'expected_output': '**Test contract for Smart Pointers & RAII:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'Smart Pointers & RAII: What does a pointer store?',
                        ['An address', 'Only an integer value', 'A class blueprint', 'A file name'],
                        0,
                        'Pointers store addresses.'],
                      [ 'What does *ptr do in an expression?',
                        ['Dereference the pointer', 'Create a pointer', 'Compare two strings', 'Delete every object'],
                        0,
                        'Dereferencing accesses the pointed-to object.'],
                      [ 'What does nullptr mean?',
                        [ 'The pointer does not point to an object',
                          'The pointer points to zero bytes of valid data',
                          'The pointer is a reference',
                          'The pointer is automatically owned'],
                        0,
                        'nullptr represents a null pointer value.'],
                      [ 'Why check a pointer before dereferencing it?',
                        [ 'To avoid accessing through a null/invalid pointer',
                          'To make the compiler slower',
                          'To create a vector',
                          'To convert to Java'],
                        0,
                        'Dereferencing an invalid pointer is unsafe.'],
                      [ 'What is pointer arithmetic tied to?',
                        ['The pointed-to element type', 'Only strings', 'The CPU brand', 'The file system'],
                        0,
                        'Pointer increments move by the size of the pointed-to type.']],
    'summary': 'You should now be able to explain smart pointers & raii, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Move Semantics & Resource Ownership',
    'rules': [ 'Name and trace the role of each unique_ptr before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the smart pointers & '
            'raii exercise.',
    'extension': 'Add one realistic requirement to the smart pointers & raii exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain smart pointers & raii without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_33'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Smart Pointers & RAII matters because C++ programs must reason carefully about references, '
                      'ownership, lifetime, and resource safety.',
    'guided_practice': [ '1. Restate the goal of **Smart Pointers & RAII** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Smart Pointers & '
                         'RAII**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Smart Pointers & RAII** task: Rewrite a raw-pointer ownership '
                            'example using unique_ptr and explain who owns the resource. Then create one small '
                            'variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Smart Pointers & RAII** program that exhibits this common mistake: '
                  '**Memorizing unique_ptr syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Smart Pointers & RAII** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what smart pointers & raii means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for smart pointers & raii.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small smart pointers & raii example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Smart Pointers & RAII.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Smart Pointers & RAII without violating the '
                                  'stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Smart Pointers '
                                  '& RAII.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['memory', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_35',
    'title': 'Move Semantics & Resource Ownership',
    'description': 'Understand lvalues, rvalues, move construction, move assignment, std::move, and why moving can '
                   'transfer resources instead of copying them.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Move Semantics & Resource Ownership**, understand why it is '
                    'useful, trace a focused example, practice it with guidance, then solve an independent variation. '
                    'You will finish by proving your understanding through concept, syntax, code-reading, debugging, '
                    'and application checks.',
    'learning_objectives': [ 'Explain what move semantics & resource ownership means and why it exists.',
                             'Read and write the core syntax used for move semantics & resource ownership.',
                             'Predict the behavior of a small move semantics & resource ownership example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['rvalue', 'move constructor', 'ownership transfer', 'moved-from state'],
    'explanation': 'Understand lvalues, rvalues, move construction, move assignment, std::move, and why moving can '
                   'transfer resources instead of copying them. C++ syntax is shown with the standard library names '
                   'used in this lesson. Read the declaration from left to right: identify the type or template, the '
                   'name, the operation, and the terminating punctuation.',
    'syntax': 'vector<int> source{1,2,3};\nvector<int> target = move(source);\ncout << target.size();',
    'syntax_breakdown': [ 'Focus on rvalue: identify what it represents and what role it plays in the statement.',
                          'Next inspect move constructor: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'vector<int> source{1,2,3};\nvector<int> target = move(source);\ncout << target.size();',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'vector<int> source(1000, 7);\nvector<int> moved = std::move(source);\ncout << moved.size();',
    'example2_explanation': 'Change one meaningful input or rule related to move semantics & resource ownership, '
                            'predict the result, and only then run the program.',
    'practical_example': 'Imagine a small move semantics & resource ownership feature in a student or inventory '
                         'program. Decide what data enters the feature, what rule the feature applies, and what result '
                         'it should produce.',
    'common_mistakes': [ 'Memorizing rvalue syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make rvalue behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each rvalue before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Compare copying and moving a large vector conceptually and explain the state of the moved-from '
                'object.',
    'practice_problem': '**Move Semantics & Resource Ownership independent practice:** Compare copying and moving a '
                        'large vector conceptually and explain the state of the moved-from object. You must also add '
                        "one clearly different variation and test it. Your work should demonstrate the lesson's main "
                        'rule, not merely reproduce Example 1.',
    'expected_output': '**Test contract for Move Semantics & Resource Ownership:** Run the program with a normal case, '
                       'a boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Move Semantics & Resource Ownership: What does std::move primarily do?',
                        [ 'Enables an object to be treated as an rvalue for moving',
                          'Physically moves every byte immediately',
                          'Deletes the object',
                          'Creates a thread'],
                        0,
                        'std::move is a cast that enables move operations when available.'],
                      [ 'Why can moving a vector be cheaper than copying it?',
                        [ 'Ownership of its buffer can be transferred',
                          'Vectors become arrays',
                          'The values disappear',
                          'It skips type checking'],
                        0,
                        'A move can transfer the underlying resources instead of duplicating them.'],
                      [ 'What should you assume about a moved-from object?',
                        [ 'It remains valid but its exact value/state is generally not something to rely on',
                          'It is always destroyed',
                          'It is always unchanged',
                          'It becomes a raw pointer'],
                        0,
                        'Moved-from objects are valid but typically have unspecified value state.'],
                      [ 'What is a move constructor for?',
                        [ 'Constructing an object by taking resources from an rvalue',
                          'Reading a file',
                          'Starting a thread',
                          'Sorting a vector'],
                        0,
                        'Move constructors transfer resources from temporary/rvalue objects.'],
                      [ 'Why is ownership important for move semantics?',
                        [ 'Moving transfers responsibility for resources',
                          'Ownership is unrelated',
                          'It only changes comments',
                          'It disables destructors'],
                        0,
                        'Move semantics are primarily about efficient resource transfer.']],
    'summary': 'You should now be able to explain move semantics & resource ownership, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Linked Lists, Stacks & Queues',
    'rules': [ 'Name and trace the role of each rvalue before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the move semantics & '
            'resource ownership exercise.',
    'extension': 'Add one realistic requirement to the move semantics & resource ownership exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain move semantics & resource ownership without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_34'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Move Semantics & Resource Ownership matters because C++ programs must reason carefully about '
                      'references, ownership, lifetime, and resource safety.',
    'guided_practice': [ '1. Restate the goal of **Move Semantics & Resource Ownership** in one sentence before '
                         'writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Move Semantics & '
                         'Resource Ownership**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Move Semantics & Resource Ownership** task: Compare copying '
                            'and moving a large vector conceptually and explain the state of the moved-from object. '
                            'Then create one small variation that changes an input, rule, or data case without '
                            'changing the main goal.',
    'debug_task': 'Debug a deliberately small **Move Semantics & Resource Ownership** program that exhibits this '
                  'common mistake: **Memorizing rvalue syntax without being able to explain what changes in the '
                  'program.**. Before changing code, identify the first incorrect value, state, control-flow decision, '
                  'or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Move Semantics & Resource Ownership** to a small real-world feature. Keep the same '
                     'core rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what move semantics & resource ownership means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for move semantics & resource '
                                                 'ownership.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small move semantics & resource ownership '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Move Semantics & Resource '
                                  'Ownership.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Move Semantics & Resource Ownership without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Move Semantics '
                                  '& Resource Ownership.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['memory', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_36',
    'title': 'Linked Lists, Stacks & Queues',
    'description': 'Understand node-based structures and FIFO/LIFO behavior, then implement or use the appropriate '
                   'abstraction for the access pattern.',
    'stage': 'Algorithms & Engineering',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Linked Lists, Stacks & Queues**, understand why it is useful, '
                    'trace a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what linked lists, stacks & queues means and why it exists.',
                             'Read and write the core syntax used for linked lists, stacks & queues.',
                             'Predict the behavior of a small linked lists, stacks & queues example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['node', 'LIFO', 'FIFO', 'head'],
    'explanation': 'Understand node-based structures and FIFO/LIFO behavior, then implement or use the appropriate '
                   'abstraction for the access pattern. C++ syntax is shown with the standard library names used in '
                   'this lesson. Read the declaration from left to right: identify the type or template, the name, the '
                   'operation, and the terminating punctuation.',
    'syntax': 'stack<int> history;\nhistory.push(10);\nhistory.push(20);\ncout << history.top();\nhistory.pop();',
    'syntax_breakdown': [ 'Focus on node: identify what it represents and what role it plays in the statement.',
                          'Next inspect LIFO: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'stack<int> history;\nhistory.push(10);\nhistory.push(20);\ncout << history.top();\nhistory.pop();',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'queue<string> line;\nline.push("A"); line.push("B");\ncout << line.front(); line.pop();',
    'example2_explanation': 'Change one meaningful input or rule related to linked lists, stacks & queues, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small linked lists, stacks & queues feature in a student or inventory program. '
                         'Decide what data enters the feature, what rule the feature applies, and what result it '
                         'should produce.',
    'common_mistakes': [ 'Memorizing node syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make node behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each node before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Implement a simple linked-list node chain and separately use stack and queue for undo and '
                'service-order behavior.',
    'practice_problem': '**Linked Lists, Stacks & Queues independent practice:** Implement a simple linked-list node '
                        'chain and separately use stack and queue for undo and service-order behavior. You must also '
                        "add one clearly different variation and test it. Your work should demonstrate the lesson's "
                        'main rule, not merely reproduce Example 1.',
    'expected_output': '**Test contract for Linked Lists, Stacks & Queues:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Linked Lists, Stacks & Queues: Which behavior is central to Linked Lists, Stacks & Queues?',
                        [ 'The data structure or traversal operation shown in the lesson',
                          'Changing compiler flags',
                          'Reading a password',
                          'Formatting a GUI'],
                        0,
                        'The lesson is about the structure and its access/traversal behavior.'],
                      [ 'Why choose a data structure based on access pattern?',
                        [ 'Different structures optimize different operations',
                          'All structures are identical',
                          'It changes the language',
                          'It avoids testing'],
                        0,
                        'Access patterns determine which operations matter most.'],
                      [ 'What should you test first with a new structure?',
                        [ 'Empty, one-item, and several-item cases',
                          'Only a huge random case',
                          'No cases',
                          'Only compilation'],
                        0,
                        'Small boundary cases expose structural mistakes early.'],
                      [ 'What should a traversal track to avoid repeating graph nodes?',
                        ['Visited state', 'File names', 'Compiler flags', 'Class comments'],
                        0,
                        'Visited tracking prevents repeated traversal in graph algorithms.'],
                      [ 'What does a priority queue emphasize?',
                        [ 'Retrieving the highest-priority element efficiently',
                          'Preserving insertion order exactly',
                          'Unique strings only',
                          'File storage'],
                        0,
                        'Priority queues are designed around priority rather than simple FIFO order.']],
    'summary': 'You should now be able to explain linked lists, stacks & queues, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Trees, Heaps & Priority Queues',
    'rules': [ 'Name and trace the role of each node before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the linked lists, '
            'stacks & queues exercise.',
    'extension': 'Add one realistic requirement to the linked lists, stacks & queues exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain linked lists, stacks & queues without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_35'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Linked Lists, Stacks & Queues matters because programs often need to store, find, update, and '
                      'process groups of related values.',
    'guided_practice': [ '1. Restate the goal of **Linked Lists, Stacks & Queues** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Linked Lists, '
                         'Stacks & Queues**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Linked Lists, Stacks & Queues** task: Implement a simple '
                            'linked-list node chain and separately use stack and queue for undo and service-order '
                            'behavior. Then create one small variation that changes an input, rule, or data case '
                            'without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Linked Lists, Stacks & Queues** program that exhibits this common '
                  'mistake: **Memorizing node syntax without being able to explain what changes in the program.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Linked Lists, Stacks & Queues** to a small real-world feature. Keep the same core '
                     'rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what linked lists, stacks & queues means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for linked lists, stacks & '
                                                 'queues.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small linked lists, stacks & queues '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Linked Lists, Stacks & Queues.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Linked Lists, Stacks & Queues without '
                                  'violating the stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['collection', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_37',
    'title': 'Trees, Heaps & Priority Queues',
    'description': 'Represent hierarchical data and priority-based processing with trees, heaps, and priority_queue.',
    'stage': 'Algorithms & Engineering',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Trees, Heaps & Priority Queues**, understand why it is useful, '
                    'trace a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what trees, heaps & priority queues means and why it exists.',
                             'Read and write the core syntax used for trees, heaps & priority queues.',
                             'Predict the behavior of a small trees, heaps & priority queues example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['node', 'heap', 'priority', 'root'],
    'explanation': 'Represent hierarchical data and priority-based processing with trees, heaps, and priority_queue. '
                   'C++ syntax is shown with the standard library names used in this lesson. Read the declaration from '
                   'left to right: identify the type or template, the name, the operation, and the terminating '
                   'punctuation.',
    'syntax': 'priority_queue<int> pq;\npq.push(4); pq.push(9); pq.push(2);\ncout << pq.top();',
    'syntax_breakdown': [ 'Focus on node: identify what it represents and what role it plays in the statement.',
                          'Next inspect heap: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'priority_queue<int> pq;\npq.push(4); pq.push(9); pq.push(2);\ncout << pq.top();',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'queue<string> line;\nline.push("A"); line.push("B");\ncout << line.front(); line.pop();',
    'example2_explanation': 'Change one meaningful input or rule related to trees, heaps & priority queues, predict '
                            'the result, and only then run the program.',
    'practical_example': 'Imagine a small trees, heaps & priority queues feature in a student or inventory program. '
                         'Decide what data enters the feature, what rule the feature applies, and what result it '
                         'should produce.',
    'common_mistakes': [ 'Memorizing node syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make node behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each node before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Process support tickets by priority and explain why a heap is useful for repeatedly retrieving the '
                'highest priority item.',
    'practice_problem': '**Trees, Heaps & Priority Queues independent practice:** Process support tickets by priority '
                        'and explain why a heap is useful for repeatedly retrieving the highest priority item. You '
                        'must also add one clearly different variation and test it. Your work should demonstrate the '
                        "lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Trees, Heaps & Priority Queues:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Trees, Heaps & Priority Queues: Which behavior is central to Trees, Heaps & Priority Queues?',
                        [ 'The data structure or traversal operation shown in the lesson',
                          'Changing compiler flags',
                          'Reading a password',
                          'Formatting a GUI'],
                        0,
                        'The lesson is about the structure and its access/traversal behavior.'],
                      [ 'Why choose a data structure based on access pattern?',
                        [ 'Different structures optimize different operations',
                          'All structures are identical',
                          'It changes the language',
                          'It avoids testing'],
                        0,
                        'Access patterns determine which operations matter most.'],
                      [ 'What should you test first with a new structure?',
                        [ 'Empty, one-item, and several-item cases',
                          'Only a huge random case',
                          'No cases',
                          'Only compilation'],
                        0,
                        'Small boundary cases expose structural mistakes early.'],
                      [ 'What should a traversal track to avoid repeating graph nodes?',
                        ['Visited state', 'File names', 'Compiler flags', 'Class comments'],
                        0,
                        'Visited tracking prevents repeated traversal in graph algorithms.'],
                      [ 'What does a priority queue emphasize?',
                        [ 'Retrieving the highest-priority element efficiently',
                          'Preserving insertion order exactly',
                          'Unique strings only',
                          'File storage'],
                        0,
                        'Priority queues are designed around priority rather than simple FIFO order.']],
    'summary': 'You should now be able to explain trees, heaps & priority queues, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Graphs & Traversal',
    'rules': [ 'Name and trace the role of each node before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the trees, heaps & '
            'priority queues exercise.',
    'extension': 'Add one realistic requirement to the trees, heaps & priority queues exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain trees, heaps & priority queues without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_36'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Trees, Heaps & Priority Queues matters because programs often need to store, find, update, and '
                      'process groups of related values.',
    'guided_practice': [ '1. Restate the goal of **Trees, Heaps & Priority Queues** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Trees, Heaps & '
                         'Priority Queues**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Trees, Heaps & Priority Queues** task: Process support tickets '
                            'by priority and explain why a heap is useful for repeatedly retrieving the highest '
                            'priority item. Then create one small variation that changes an input, rule, or data case '
                            'without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Trees, Heaps & Priority Queues** program that exhibits this common '
                  'mistake: **Memorizing node syntax without being able to explain what changes in the program.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Trees, Heaps & Priority Queues** to a small real-world feature. Keep the same core '
                     'rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what trees, heaps & priority queues means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for trees, heaps & priority '
                                                 'queues.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small trees, heaps & priority queues '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Trees, Heaps & Priority Queues.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Trees, Heaps & Priority Queues without '
                                  'violating the stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['collection', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_38',
    'title': 'Graphs & Traversal',
    'description': 'Represent relationships as graphs and use breadth-first or depth-first traversal to explore '
                   'reachable nodes.',
    'stage': 'Algorithms & Engineering',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Graphs & Traversal**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what graphs & traversal means and why it exists.',
                             'Read and write the core syntax used for graphs & traversal.',
                             'Predict the behavior of a small graphs & traversal example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['vertex', 'edge', 'BFS', 'DFS'],
    'explanation': 'Represent relationships as graphs and use breadth-first or depth-first traversal to explore '
                   'reachable nodes. C++ syntax is shown with the standard library names used in this lesson. Read the '
                   'declaration from left to right: identify the type or template, the name, the operation, and the '
                   'terminating punctuation.',
    'syntax': 'vector<vector<int>> graph{{1,2},{0,3},{0,3},{1,2}};\nqueue<int> q;\nq.push(0);',
    'syntax_breakdown': [ 'Focus on vertex: identify what it represents and what role it plays in the statement.',
                          'Next inspect edge: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'vector<vector<int>> graph{{1,2},{0,3},{0,3},{1,2}};\nqueue<int> q;\nq.push(0);',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'vector<vector<int>> g{{1,2},{0,3},{0,3},{1,2}};\n'
                'queue<int> q; q.push(0);\n'
                'vector<bool> seen(4,false); seen[0]=true;',
    'example2_explanation': 'Change one meaningful input or rule related to graphs & traversal, predict the result, '
                            'and only then run the program.',
    'practical_example': 'Imagine a small graphs & traversal feature in a student or inventory program. Decide what '
                         'data enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing vertex syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make vertex behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each vertex before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Represent a small campus map and describe a BFS from one building and a DFS alternative.',
    'practice_problem': '**Graphs & Traversal independent practice:** Represent a small campus map and describe a BFS '
                        'from one building and a DFS alternative. You must also add one clearly different variation '
                        "and test it. Your work should demonstrate the lesson's main rule, not merely reproduce "
                        'Example 1.',
    'expected_output': '**Test contract for Graphs & Traversal:** Run the program with a normal case, a boundary case, '
                       'and a misuse/invalid case when relevant. For each case, record the actual result and compare '
                       'it with the requirement. A correct submission must preserve the lesson rule and handle the '
                       'defined edge case safely.',
    'mastery_quiz': [ [ 'Graphs & Traversal: Which behavior is central to Graphs & Traversal?',
                        [ 'The data structure or traversal operation shown in the lesson',
                          'Changing compiler flags',
                          'Reading a password',
                          'Formatting a GUI'],
                        0,
                        'The lesson is about the structure and its access/traversal behavior.'],
                      [ 'Why choose a data structure based on access pattern?',
                        [ 'Different structures optimize different operations',
                          'All structures are identical',
                          'It changes the language',
                          'It avoids testing'],
                        0,
                        'Access patterns determine which operations matter most.'],
                      [ 'What should you test first with a new structure?',
                        [ 'Empty, one-item, and several-item cases',
                          'Only a huge random case',
                          'No cases',
                          'Only compilation'],
                        0,
                        'Small boundary cases expose structural mistakes early.'],
                      [ 'What should a traversal track to avoid repeating graph nodes?',
                        ['Visited state', 'File names', 'Compiler flags', 'Class comments'],
                        0,
                        'Visited tracking prevents repeated traversal in graph algorithms.'],
                      [ 'What does a priority queue emphasize?',
                        [ 'Retrieving the highest-priority element efficiently',
                          'Preserving insertion order exactly',
                          'Unique strings only',
                          'File storage'],
                        0,
                        'Priority queues are designed around priority rather than simple FIFO order.']],
    'summary': 'You should now be able to explain graphs & traversal, recognize its syntax, trace the worked example, '
               'and use the concept in a small original program.',
    'next_lesson': 'Testing & Debugging',
    'rules': [ 'Name and trace the role of each vertex before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the graphs & traversal '
            'exercise.',
    'extension': 'Add one realistic requirement to the graphs & traversal exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain graphs & traversal without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_37'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Graphs & Traversal matters because hierarchical and network-shaped data require specialized '
                      'structures and traversal strategies.',
    'guided_practice': [ '1. Restate the goal of **Graphs & Traversal** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Graphs & '
                         'Traversal**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Graphs & Traversal** task: Represent a small campus map and '
                            'describe a BFS from one building and a DFS alternative. Then create one small variation '
                            'that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Graphs & Traversal** program that exhibits this common mistake: '
                  '**Memorizing vertex syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Graphs & Traversal** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what graphs & traversal means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for graphs & traversal.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small graphs & traversal example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Graphs & Traversal.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Graphs & Traversal without violating the '
                                  'stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['tree_graph', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_39',
    'title': 'Testing & Debugging',
    'description': 'Separate compile, runtime, and logic failures; reproduce bugs, read diagnostics, use '
                   'assertions/breakpoints, and test requirements systematically.',
    'stage': 'Algorithms & Engineering',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Testing & Debugging**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what testing & debugging means and why it exists.',
                             'Read and write the core syntax used for testing & debugging.',
                             'Predict the behavior of a small testing & debugging example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['assertion', 'breakpoint', 'reproduction', 'diagnostic'],
    'explanation': 'Separate compile, runtime, and logic failures; reproduce bugs, read diagnostics, use '
                   'assertions/breakpoints, and test requirements systematically. C++ syntax is shown with the '
                   'standard library names used in this lesson. Read the declaration from left to right: identify the '
                   'type or template, the name, the operation, and the terminating punctuation.',
    'syntax': 'assert(age >= 0);\n// Breakpoint: inspect age before this check.',
    'syntax_breakdown': [ 'Focus on assertion: identify what it represents and what role it plays in the statement.',
                          'Next inspect breakpoint: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'assert(age >= 0);\n// Breakpoint: inspect age before this check.',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'int total(int price, int quantity) {\n'
                '    assert(price >= 0);\n'
                '    assert(quantity >= 0);\n'
                '    return price * quantity;\n'
                '}',
    'example2_explanation': 'Change one meaningful input or rule related to testing & debugging, predict the result, '
                            'and only then run the program.',
    'practical_example': 'Imagine a small testing & debugging feature in a student or inventory program. Decide what '
                         'data enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing assertion syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make assertion behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each assertion before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Given a small buggy program, identify the failure type, reproduce it, and write three focused test '
                'cases.',
    'practice_problem': '**Testing & Debugging independent practice:** Given a small buggy program, identify the '
                        'failure type, reproduce it, and write three focused test cases. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Testing & Debugging:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'Testing & Debugging: What should a debugger help you inspect?',
                        [ 'Program state and execution flow',
                          'Only source-code colors',
                          'Only filenames',
                          'Only comments'],
                        0,
                        'Debuggers let you inspect state while stepping through execution.'],
                      [ 'What is a breakpoint?',
                        [ 'A location where execution pauses for inspection',
                          'A compile error',
                          'A file format',
                          'A loop keyword'],
                        0,
                        'Breakpoints pause execution.'],
                      [ 'What is a good first debugging step?',
                        [ 'Reproduce the problem with the smallest useful case',
                          'Rewrite the whole program',
                          'Ignore the error message',
                          'Change five functions'],
                        0,
                        'A reproducible small case narrows the search.'],
                      [ 'What does an assertion check?',
                        [ 'An assumption that should hold during execution',
                          'A user password',
                          'A file extension',
                          'A compiler version'],
                        0,
                        'Assertions verify assumptions.'],
                      [ 'Why write boundary tests?',
                        [ 'They reveal mistakes around limits and transitions',
                          'They make code longer only',
                          'They replace compilation',
                          'They guarantee no bugs'],
                        0,
                        'Boundary tests target common logic failures.']],
    'summary': 'You should now be able to explain testing & debugging, recognize its syntax, trace the worked example, '
               'and use the concept in a small original program.',
    'next_lesson': 'Problem Decomposition & Validation',
    'rules': [ 'Name and trace the role of each assertion before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the testing & debugging '
            'exercise.',
    'extension': 'Add one realistic requirement to the testing & debugging exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain testing & debugging without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_38'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Testing & Debugging matters because useful programs must detect, explain, and recover from '
                      'incorrect states instead of silently failing.',
    'guided_practice': [ '1. Restate the goal of **Testing & Debugging** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Testing & '
                         'Debugging**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Testing & Debugging** task: Given a small buggy program, '
                            'identify the failure type, reproduce it, and write three focused test cases. Then create '
                            'one small variation that changes an input, rule, or data case without changing the main '
                            'goal.',
    'debug_task': 'Debug a deliberately small **Testing & Debugging** program that exhibits this common mistake: '
                  '**Memorizing assertion syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Testing & Debugging** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what testing & debugging means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for testing & debugging.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small testing & debugging example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Testing & Debugging.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Testing & Debugging without violating the '
                                  'stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['error', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_40',
    'title': 'Problem Decomposition & Validation',
    'description': 'Turn a written specification into inputs, rules, state, processing steps, validation, outputs, and '
                   'edge cases before implementation.',
    'stage': 'Algorithms & Engineering',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Problem Decomposition & Validation**, understand why it is '
                    'useful, trace a focused example, practice it with guidance, then solve an independent variation. '
                    'You will finish by proving your understanding through concept, syntax, code-reading, debugging, '
                    'and application checks.',
    'learning_objectives': [ 'Explain what problem decomposition & validation means and why it exists.',
                             'Read and write the core syntax used for problem decomposition & validation.',
                             'Predict the behavior of a small problem decomposition & validation example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['input', 'rule', 'validation', 'edge case'],
    'explanation': 'Turn a written specification into inputs, rules, state, processing steps, validation, outputs, and '
                   'edge cases before implementation. C++ syntax is shown with the standard library names used in this '
                   'lesson. Read the declaration from left to right: identify the type or template, the name, the '
                   'operation, and the terminating punctuation.',
    'syntax': 'struct Requirement { string input; string rule; string output; };',
    'syntax_breakdown': [ 'Focus on input: identify what it represents and what role it plays in the statement.',
                          'Next inspect rule: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'struct Requirement { string input; string rule; string output; };',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'class Battery { public: int level = 100; };\n'
                'class Phone {\n'
                '    Battery battery;\n'
                'public:\n'
                '    int batteryLevel() const { return battery.level; }\n'
                '};',
    'example2_explanation': 'Change one meaningful input or rule related to problem decomposition & validation, '
                            'predict the result, and only then run the program.',
    'practical_example': 'Imagine a small problem decomposition & validation feature in a student or inventory '
                         'program. Decide what data enters the feature, what rule the feature applies, and what result '
                         'it should produce.',
    'common_mistakes': [ 'Memorizing input syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make input behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each input before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Break a parking-system specification into a checklist and identify normal, boundary, invalid, and '
                'conflicting cases.',
    'practice_problem': '**Problem Decomposition & Validation independent practice:** Break a parking-system '
                        'specification into a checklist and identify normal, boundary, invalid, and conflicting cases. '
                        'You must also add one clearly different variation and test it. Your work should demonstrate '
                        "the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Problem Decomposition & Validation:** Run the program with a normal case, '
                       'a boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Problem Decomposition & Validation: Which statement best describes Problem Decomposition & '
                        'Validation?',
                        [ 'It is a core part of Problem Decomposition & Validation',
                          'It is only a compiler warning',
                          'It is unrelated to programming',
                          'It replaces all data types'],
                        0,
                        'This lesson focuses on the role and correct use of Problem Decomposition & Validation.'],
                      [ 'What should a learner be able to do after Problem Decomposition & Validation?',
                        [ 'Use the concept in a small program',
                          'Only memorize its name',
                          'Avoid testing it',
                          'Copy one example unchanged'],
                        0,
                        'Application is the goal, not memorization.'],
                      [ 'Which test is most useful for Problem Decomposition & Validation?',
                        [ 'A normal case plus an important edge case',
                          'No input',
                          'Only a huge random case',
                          'Only comments'],
                        0,
                        'Testing the concept in more than one case reveals misunderstandings.'],
                      [ 'Which mistake should be avoided with Problem Decomposition & Validation?',
                        [ 'Using syntax without understanding its behavior',
                          'Writing a small test',
                          'Reading diagnostics',
                          'Choosing clear names'],
                        0,
                        'Understanding behavior matters more than copying syntax.'],
                      [ 'How should Problem Decomposition & Validation fit into a larger program?',
                        [ 'As one focused tool combined with earlier concepts',
                          'As a replacement for every other feature',
                          'As global state everywhere',
                          'As code that never needs testing'],
                        0,
                        'Programming features are combined according to the problem.']],
    'summary': 'You should now be able to explain problem decomposition & validation, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Data Structures & Algorithms Challenge',
    'rules': [ 'Name and trace the role of each input before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the problem '
            'decomposition & validation exercise.',
    'extension': 'Add one realistic requirement to the problem decomposition & validation exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain problem decomposition & validation without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_39'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Problem Decomposition & Validation matters because larger programs need clear ownership of '
                      'state and behavior and predictable relationships between types.',
    'guided_practice': [ '1. Restate the goal of **Problem Decomposition & Validation** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Problem '
                         'Decomposition & Validation**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Problem Decomposition & Validation** task: Break a '
                            'parking-system specification into a checklist and identify normal, boundary, invalid, and '
                            'conflicting cases. Then create one small variation that changes an input, rule, or data '
                            'case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Problem Decomposition & Validation** program that exhibits this common '
                  'mistake: **Memorizing input syntax without being able to explain what changes in the program.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Problem Decomposition & Validation** to a small real-world feature. Keep the same '
                     'core rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what problem decomposition & validation means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for problem decomposition & '
                                                 'validation.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small problem decomposition & validation '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Problem Decomposition & '
                                  'Validation.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Problem Decomposition & Validation without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Problem '
                                  'Decomposition & Validation.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['oop', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_41',
    'title': 'Data Structures & Algorithms Challenge',
    'description': 'Combine containers, algorithms, functions, validation, and complexity reasoning to solve a '
                   'multi-step problem.',
    'stage': 'Algorithms & Engineering',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Data Structures & Algorithms Challenge**, understand why it is '
                    'useful, trace a focused example, practice it with guidance, then solve an independent variation. '
                    'You will finish by proving your understanding through concept, syntax, code-reading, debugging, '
                    'and application checks.',
    'learning_objectives': [ 'Explain what data structures & algorithms challenge means and why it exists.',
                             'Read and write the core syntax used for data structures & algorithms challenge.',
                             'Predict the behavior of a small data structures & algorithms challenge example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['data structure', 'algorithm', 'invariant', 'complexity'],
    'explanation': 'Combine containers, algorithms, functions, validation, and complexity reasoning to solve a '
                   'multi-step problem. C++ syntax is shown with the standard library names used in this lesson. Read '
                   'the declaration from left to right: identify the type or template, the name, the operation, and '
                   'the terminating punctuation.',
    'syntax': 'sort(values.begin(), values.end());\nauto it = lower_bound(values.begin(), values.end(), target);',
    'syntax_breakdown': [ 'Focus on data structure: identify what it represents and what role it plays in the '
                          'statement.',
                          'Next inspect algorithm: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'sort(values.begin(), values.end());\nauto it = lower_bound(values.begin(), values.end(), target);',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'struct Product { std::string name; double price; };\n'
                'Product item{"Keyboard", 999.0};\n'
                'cout << item.name << " " << item.price;',
    'example2_explanation': 'Change one meaningful input or rule related to data structures & algorithms challenge, '
                            'predict the result, and only then run the program.',
    'practical_example': 'Imagine a small data structures & algorithms challenge feature in a student or inventory '
                         'program. Decide what data enters the feature, what rule the feature applies, and what result '
                         'it should produce.',
    'common_mistakes': [ 'Memorizing data structure syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make data structure behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each data structure before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Solve a problem that combines frequency counting, sorting, searching, and output formatting.',
    'practice_problem': '**Data Structures & Algorithms Challenge independent practice:** Solve a problem that '
                        'combines frequency counting, sorting, searching, and output formatting. You must also add one '
                        "clearly different variation and test it. Your work should demonstrate the lesson's main rule, "
                        'not merely reproduce Example 1.',
    'expected_output': '**Test contract for Data Structures & Algorithms Challenge:** Run the program with a normal '
                       'case, a boundary case, and a misuse/invalid case when relevant. For each case, record the '
                       'actual result and compare it with the requirement. A correct submission must preserve the '
                       'lesson rule and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Data Structures & Algorithms Challenge: What does sort do to a range?',
                        [ 'Orders the elements according to a comparison',
                          'Counts files',
                          'Creates a class',
                          'Reads input'],
                        0,
                        'sort rearranges a range into an order.'],
                      [ 'What does binary search require conceptually?',
                        ['An ordered range', 'An empty program', 'A class hierarchy', 'A file stream'],
                        0,
                        'Binary search relies on sorted/ordered data.'],
                      [ 'What does find return in C++?',
                        ['An iterator to the match or end if absent', 'A Boolean only', 'A file', 'A class'],
                        0,
                        'std::find returns an iterator.'],
                      [ 'Why use a comparator?',
                        [ 'To define a custom ordering',
                          'To allocate memory',
                          'To read a database',
                          'To catch exceptions'],
                        0,
                        'Comparators tell sorting algorithms how elements should be ordered.'],
                      [ 'What is a good algorithm test?',
                        [ 'Include duplicates, empty input, and already-ordered data',
                          'Only one random value',
                          'No expected result',
                          'Only compilation'],
                        0,
                        'Different shapes of input reveal different algorithm bugs.']],
    'summary': 'You should now be able to explain data structures & algorithms challenge, recognize its syntax, trace '
               'the worked example, and use the concept in a small original program.',
    'next_lesson': 'Capstone & Practical Exam Readiness',
    'rules': [ 'Name and trace the role of each data structure before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the data structures & '
            'algorithms challenge exercise.',
    'extension': 'Add one realistic requirement to the data structures & algorithms challenge exercise while keeping '
                 'the original behavior correct.',
    'learning_checks': [ 'Can I explain data structures & algorithms challenge without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_40'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Data Structures & Algorithms Challenge matters because solving a problem correctly also '
                      'requires choosing an approach that scales and can be reasoned about.',
    'guided_practice': [ '1. Restate the goal of **Data Structures & Algorithms Challenge** in one sentence before '
                         'writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Data Structures & '
                         'Algorithms Challenge**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Data Structures & Algorithms Challenge** task: Solve a problem '
                            'that combines frequency counting, sorting, searching, and output formatting. Then create '
                            'one small variation that changes an input, rule, or data case without changing the main '
                            'goal.',
    'debug_task': 'Debug a deliberately small **Data Structures & Algorithms Challenge** program that exhibits this '
                  'common mistake: **Memorizing data structure syntax without being able to explain what changes in '
                  'the program.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Data Structures & Algorithms Challenge** to a small real-world feature. Keep the same '
                     'core rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what data structures & algorithms challenge means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for data structures & algorithms '
                                                 'challenge.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small data structures & algorithms '
                                                 'challenge example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Data Structures & Algorithms '
                                  'Challenge.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Data Structures & Algorithms Challenge without '
                                  'violating the stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['algorithm', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_42',
    'title': 'Capstone & Practical Exam Readiness',
    'description': 'Plan, implement, test, debug, document, and explain a complete C++ console application from a '
                   'detailed specification.',
    'stage': 'Algorithms & Engineering',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Capstone & Practical Exam Readiness**, understand why it is '
                    'useful, trace a focused example, practice it with guidance, then solve an independent variation. '
                    'You will finish by proving your understanding through concept, syntax, code-reading, debugging, '
                    'and application checks.',
    'learning_objectives': [ 'Explain what capstone & practical exam readiness means and why it exists.',
                             'Read and write the core syntax used for capstone & practical exam readiness.',
                             'Predict the behavior of a small capstone & practical exam readiness example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['requirements', 'architecture', 'validation', 'testing'],
    'explanation': 'Plan, implement, test, debug, document, and explain a complete C++ console application from a '
                   'detailed specification. C++ syntax is shown with the standard library names used in this lesson. '
                   'Read the declaration from left to right: identify the type or template, the name, the operation, '
                   'and the terminating punctuation.',
    'syntax': 'int main() {\n    // 1. Parse input\n    // 2. Validate\n    // 3. Process\n    // 4. Report\n}',
    'syntax_breakdown': [ 'Focus on requirements: identify what it represents and what role it plays in the statement.',
                          'Next inspect architecture: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'int main() {\n    // 1. Parse input\n    // 2. Validate\n    // 3. Process\n    // 4. Report\n}',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': '// Focused Capstone & Practical Exam Readiness example\ncout << "Practice the lesson concept";',
    'example2_explanation': 'Change one meaningful input or rule related to capstone & practical exam readiness, '
                            'predict the result, and only then run the program.',
    'practical_example': 'Imagine a small capstone & practical exam readiness feature in a student or inventory '
                         'program. Decide what data enters the feature, what rule the feature applies, and what result '
                         'it should produce.',
    'common_mistakes': [ 'Memorizing requirements syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make requirements behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each requirements before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Build a complete console system from a specification and submit it with validation, tests, and a '
                'short design explanation.',
    'practice_problem': '**Capstone & Practical Exam Readiness independent practice:** Build a complete console system '
                        'from a specification and submit it with validation, tests, and a short design explanation. '
                        'You must also add one clearly different variation and test it. Your work should demonstrate '
                        "the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Capstone & Practical Exam Readiness:** Run the program with a normal case, '
                       'a boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Capstone & Practical Exam Readiness: Which statement best describes Capstone & Practical Exam '
                        'Readiness?',
                        [ 'It is a core part of Capstone & Practical Exam Readiness',
                          'It is only a compiler warning',
                          'It is unrelated to programming',
                          'It replaces all data types'],
                        0,
                        'This lesson focuses on the role and correct use of Capstone & Practical Exam Readiness.'],
                      [ 'What should a learner be able to do after Capstone & Practical Exam Readiness?',
                        [ 'Use the concept in a small program',
                          'Only memorize its name',
                          'Avoid testing it',
                          'Copy one example unchanged'],
                        0,
                        'Application is the goal, not memorization.'],
                      [ 'Which test is most useful for Capstone & Practical Exam Readiness?',
                        [ 'A normal case plus an important edge case',
                          'No input',
                          'Only a huge random case',
                          'Only comments'],
                        0,
                        'Testing the concept in more than one case reveals misunderstandings.'],
                      [ 'Which mistake should be avoided with Capstone & Practical Exam Readiness?',
                        [ 'Using syntax without understanding its behavior',
                          'Writing a small test',
                          'Reading diagnostics',
                          'Choosing clear names'],
                        0,
                        'Understanding behavior matters more than copying syntax.'],
                      [ 'How should Capstone & Practical Exam Readiness fit into a larger program?',
                        [ 'As one focused tool combined with earlier concepts',
                          'As a replacement for every other feature',
                          'As global state everywhere',
                          'As code that never needs testing'],
                        0,
                        'Programming features are combined according to the problem.']],
    'summary': 'You should now be able to explain capstone & practical exam readiness, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Bitwise Operators & Binary Representation',
    'rules': [ 'Name and trace the role of each requirements before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the capstone & '
            'practical exam readiness exercise.',
    'extension': 'Add one realistic requirement to the capstone & practical exam readiness exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain capstone & practical exam readiness without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_41'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Capstone & Practical Exam Readiness matters because real projects require requirements, design '
                      'decisions, testing, maintainability, and trade-off awareness.',
    'guided_practice': [ '1. Restate the goal of **Capstone & Practical Exam Readiness** in one sentence before '
                         'writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Capstone & '
                         'Practical Exam Readiness**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Capstone & Practical Exam Readiness** task: Build a complete '
                            'console system from a specification and submit it with validation, tests, and a short '
                            'design explanation. Then create one small variation that changes an input, rule, or data '
                            'case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Capstone & Practical Exam Readiness** program that exhibits this '
                  'common mistake: **Memorizing requirements syntax without being able to explain what changes in the '
                  'program.**. Before changing code, identify the first incorrect value, state, control-flow decision, '
                  'or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Capstone & Practical Exam Readiness** to a small real-world feature. Keep the same '
                     'core rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what capstone & practical exam readiness means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for capstone & practical exam '
                                                 'readiness.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small capstone & practical exam readiness '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Capstone & Practical Exam '
                                  'Readiness.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Capstone & Practical Exam Readiness without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Capstone & '
                                  'Practical Exam Readiness.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['engineering', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_43',
    'title': 'Bitwise Operators & Binary Representation',
    'description': 'Understand binary representation and use bitwise AND, OR, XOR, NOT, shifts, and masks for compact '
                   'flag and low-level operations.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Bitwise Operators & Binary Representation**, understand why it is '
                    'useful, trace a focused example, practice it with guidance, then solve an independent variation. '
                    'You will finish by proving your understanding through concept, syntax, code-reading, debugging, '
                    'and application checks.',
    'learning_objectives': [ 'Explain what bitwise operators & binary representation means and why it exists.',
                             'Read and write the core syntax used for bitwise operators & binary representation.',
                             'Predict the behavior of a small bitwise operators & binary representation example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['bit', 'mask', 'shift', 'flag'],
    'explanation': 'Understand binary representation and use bitwise AND, OR, XOR, NOT, shifts, and masks for compact '
                   'flag and low-level operations. C++ syntax is shown with the standard library names used in this '
                   'lesson. Read the declaration from left to right: identify the type or template, the name, the '
                   'operation, and the terminating punctuation.',
    'syntax': 'unsigned flags = 0b0101;\nflags |= 0b0010;\nbool enabled = (flags & 0b0010) != 0;',
    'syntax_breakdown': [ 'Focus on bit: identify what it represents and what role it plays in the statement.',
                          'Next inspect mask: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'unsigned flags = 0b0101;\nflags |= 0b0010;\nbool enabled = (flags & 0b0010) != 0;',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'int a = 8, b = 3;\n'
                'cout << (a / b) << " " << (a % b) << "\\n";\n'
                'cout << ((a > b) ? "larger" : "smaller");',
    'example2_explanation': 'Change one meaningful input or rule related to bitwise operators & binary representation, '
                            'predict the result, and only then run the program.',
    'practical_example': 'Imagine a small bitwise operators & binary representation feature in a student or inventory '
                         'program. Decide what data enters the feature, what rule the feature applies, and what result '
                         'it should produce.',
    'common_mistakes': [ 'Memorizing bit syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make bit behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each bit before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Create a permissions flag system where individual bits represent read, write, and admin permissions.',
    'practice_problem': '**Bitwise Operators & Binary Representation independent practice:** Create a permissions flag '
                        'system where individual bits represent read, write, and admin permissions. You must also add '
                        "one clearly different variation and test it. Your work should demonstrate the lesson's main "
                        'rule, not merely reproduce Example 1.',
    'expected_output': '**Test contract for Bitwise Operators & Binary Representation:** Run the program with a normal '
                       'case, a boundary case, and a misuse/invalid case when relevant. For each case, record the '
                       'actual result and compare it with the requirement. A correct submission must preserve the '
                       'lesson rule and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Bitwise Operators & Binary Representation: What does % produce for integer operands?',
                        ['The remainder', 'The quotient only', 'A Boolean', 'A string'],
                        0,
                        'Modulo gives the remainder.'],
                      [ 'Which operator tests equality for primitive values?',
                        ['==', '=', '!=', '=>'],
                        0,
                        '== compares values; = assigns.'],
                      [ 'What does && represent?',
                        ['Logical AND', 'Bitwise NOT', 'Assignment', 'String concatenation only'],
                        0,
                        'Both operands must be true for && to be true.'],
                      [ 'What is the purpose of parentheses in an expression?',
                        [ 'They can make evaluation order explicit',
                          'They create a class',
                          'They allocate memory',
                          'They read input'],
                        0,
                        'Parentheses group operations and make intended precedence clear.'],
                      [ 'What does a += b mean?',
                        ['Add b to a and assign the result to a', 'Compare a and b', 'Create b', 'Divide a by b'],
                        0,
                        'Compound assignment updates the left-hand variable.']],
    'summary': 'You should now be able to explain bitwise operators & binary representation, recognize its syntax, '
               'trace the worked example, and use the concept in a small original program.',
    'next_lesson': 'Type Casting & RTTI',
    'rules': [ 'Name and trace the role of each bit before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the bitwise operators & '
            'binary representation exercise.',
    'extension': 'Add one realistic requirement to the bitwise operators & binary representation exercise while '
                 'keeping the original behavior correct.',
    'learning_checks': [ 'Can I explain bitwise operators & binary representation without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_42'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Bitwise Operators & Binary Representation gives you the foundation needed to read, change, and '
                      'reason about a program before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Bitwise Operators & Binary Representation** in one sentence before '
                         'writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Bitwise Operators '
                         '& Binary Representation**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Bitwise Operators & Binary Representation** task: Create a '
                            'permissions flag system where individual bits represent read, write, and admin '
                            'permissions. Then create one small variation that changes an input, rule, or data case '
                            'without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Bitwise Operators & Binary Representation** program that exhibits this '
                  'common mistake: **Memorizing bit syntax without being able to explain what changes in the '
                  'program.**. Before changing code, identify the first incorrect value, state, control-flow decision, '
                  'or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Bitwise Operators & Binary Representation** to a small real-world feature. Keep the '
                     'same core rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what bitwise operators & binary representation means and why '
                                                 'it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for bitwise operators & binary '
                                                 'representation.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small bitwise operators & binary '
                                                 'representation example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Bitwise Operators & Binary '
                                  'Representation.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Bitwise Operators & Binary Representation '
                                  'without violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Bitwise '
                                  'Operators & Binary Representation.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_44',
    'title': 'Type Casting & RTTI',
    'description': 'Choose explicit conversions deliberately with static_cast and understand when const_cast, '
                   'dynamic_cast, reinterpret_cast, and typeid are appropriate or dangerous.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Type Casting & RTTI**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what type casting & rtti means and why it exists.',
                             'Read and write the core syntax used for type casting & rtti.',
                             'Predict the behavior of a small type casting & rtti example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['conversion', 'static_cast', 'dynamic_cast', 'typeid'],
    'explanation': 'Choose explicit conversions deliberately with static_cast and understand when const_cast, '
                   'dynamic_cast, reinterpret_cast, and typeid are appropriate or dangerous. C++ syntax is shown with '
                   'the standard library names used in this lesson. Read the declaration from left to right: identify '
                   'the type or template, the name, the operation, and the terminating punctuation.',
    'syntax': 'double price = 19.75;\nint whole = static_cast<int>(price);\ncout << whole;',
    'syntax_breakdown': [ 'Focus on conversion: identify what it represents and what role it plays in the statement.',
                          'Next inspect static_cast: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'double price = 19.75;\nint whole = static_cast<int>(price);\ncout << whole;',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'double value = 9.8;\nint whole = static_cast<int>(value);\ncout << whole;',
    'example2_explanation': 'Change one meaningful input or rule related to type casting & rtti, predict the result, '
                            'and only then run the program.',
    'practical_example': 'Imagine a small type casting & rtti feature in a student or inventory program. Decide what '
                         'data enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing conversion syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make conversion behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each conversion before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Convert numeric types safely, then demonstrate a polymorphic dynamic_cast and explain why it needs a '
                'polymorphic base.',
    'practice_problem': '**Type Casting & RTTI independent practice:** Convert numeric types safely, then demonstrate '
                        'a polymorphic dynamic_cast and explain why it needs a polymorphic base. You must also add one '
                        "clearly different variation and test it. Your work should demonstrate the lesson's main rule, "
                        'not merely reproduce Example 1.',
    'expected_output': '**Test contract for Type Casting & RTTI:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'Type Casting & RTTI: What is static_cast used for?',
                        [ 'Explicit compile-time-checked conversions where appropriate',
                          'Unsafe arbitrary memory reinterpretation only',
                          'Thread creation',
                          'File reading'],
                        0,
                        'static_cast expresses many ordinary explicit conversions.'],
                      [ 'What does dynamic_cast need for safe downcasting through a base?',
                        ['A polymorphic base type', 'A vector only', 'A macro', 'A namespace'],
                        0,
                        'Runtime checked casts through a base generally require a polymorphic type.'],
                      [ 'What does typeid provide?',
                        [ 'Runtime type information about an expression/type',
                          'A loop count',
                          'A file path',
                          'A constructor'],
                        0,
                        'typeid is part of C++ RTTI.'],
                      [ 'Why should reinterpret_cast be used sparingly?',
                        [ 'It can express low-level reinterpretations with significant safety risks',
                          'It sorts values',
                          'It validates all types',
                          'It catches exceptions'],
                        0,
                        'Low-level reinterpretation can violate assumptions and safety.'],
                      [ 'Why prefer explicit casts over implicit surprises?',
                        [ 'They make conversion intent visible',
                          'They remove all conversions',
                          'They avoid compilation',
                          'They create memory automatically'],
                        0,
                        'Explicit conversion communicates intent to readers and the compiler.']],
    'summary': 'You should now be able to explain type casting & rtti, recognize its syntax, trace the worked example, '
               'and use the concept in a small original program.',
    'next_lesson': 'Undefined Behavior, Lifetime & const',
    'rules': [ 'Name and trace the role of each conversion before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the type casting & rtti '
            'exercise.',
    'extension': 'Add one realistic requirement to the type casting & rtti exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain type casting & rtti without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_43'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Type Casting & RTTI gives you the foundation needed to read, change, and reason about a program '
                      'before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Type Casting & RTTI** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Type Casting & '
                         'RTTI**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Type Casting & RTTI** task: Convert numeric types safely, then '
                            'demonstrate a polymorphic dynamic_cast and explain why it needs a polymorphic base. Then '
                            'create one small variation that changes an input, rule, or data case without changing the '
                            'main goal.',
    'debug_task': 'Debug a deliberately small **Type Casting & RTTI** program that exhibits this common mistake: '
                  '**Memorizing conversion syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Type Casting & RTTI** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what type casting & rtti means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for type casting & rtti.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small type casting & rtti example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Type Casting & RTTI.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Type Casting & RTTI without violating the '
                                  'stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Type Casting & '
                                  'RTTI.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_45',
    'title': 'Undefined Behavior, Lifetime & const',
    'description': 'Recognize operations whose behavior the C++ standard does not define and reason about object '
                   'lifetime, const-correctness, and safe access.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Undefined Behavior, Lifetime & const**, understand why it is '
                    'useful, trace a focused example, practice it with guidance, then solve an independent variation. '
                    'You will finish by proving your understanding through concept, syntax, code-reading, debugging, '
                    'and application checks.',
    'learning_objectives': [ 'Explain what undefined behavior, lifetime & const means and why it exists.',
                             'Read and write the core syntax used for undefined behavior, lifetime & const.',
                             'Predict the behavior of a small undefined behavior, lifetime & const example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['undefined behavior', 'lifetime', 'const-correctness', 'validity'],
    'explanation': 'Recognize operations whose behavior the C++ standard does not define and reason about object '
                   'lifetime, const-correctness, and safe access. C++ syntax is shown with the standard library names '
                   'used in this lesson. Read the declaration from left to right: identify the type or template, the '
                   'name, the operation, and the terminating punctuation.',
    'syntax': 'const int limit = 100;\nconst int* p = &limit;\ncout << *p;',
    'syntax_breakdown': [ 'Focus on undefined behavior: identify what it represents and what role it plays in the '
                          'statement.',
                          'Next inspect lifetime: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'const int limit = 100;\nconst int* p = &limit;\ncout << *p;',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'const int limit = 100;\nconst int* p = &limit;\ncout << *p;',
    'example2_explanation': 'Change one meaningful input or rule related to undefined behavior, lifetime & const, '
                            'predict the result, and only then run the program.',
    'practical_example': 'Imagine a small undefined behavior, lifetime & const feature in a student or inventory '
                         'program. Decide what data enters the feature, what rule the feature applies, and what result '
                         'it should produce.',
    'common_mistakes': [ 'Memorizing undefined behavior syntax without being able to explain what changes in the '
                         'program.',
                         'Ignoring the boundary or lifetime rules that make undefined behavior behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each undefined behavior before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Review several snippets and label them well-defined, implementation-dependent, or undefined, '
                'explaining the reasoning.',
    'practice_problem': '**Undefined Behavior, Lifetime & const independent practice:** Review several snippets and '
                        'label them well-defined, implementation-dependent, or undefined, explaining the reasoning. '
                        'You must also add one clearly different variation and test it. Your work should demonstrate '
                        "the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Undefined Behavior, Lifetime & const:** Run the program with a normal '
                       'case, a boundary case, and a misuse/invalid case when relevant. For each case, record the '
                       'actual result and compare it with the requirement. A correct submission must preserve the '
                       'lesson rule and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Undefined Behavior, Lifetime & const: What is undefined behavior?',
                        [ 'Behavior for which the C++ standard imposes no requirements',
                          'A normal warning only',
                          'A Java exception',
                          'A valid output format'],
                        0,
                        'Undefined behavior means the standard does not define what must happen.'],
                      [ 'Why does object lifetime matter?',
                        [ 'Using an object outside its lifetime is invalid',
                          'Lifetime only affects comments',
                          'It changes integer size',
                          'It disables functions'],
                        0,
                        'An object is only valid within its lifetime.'],
                      [ 'What does const communicate?',
                        [ 'An object should not be modified through that access path',
                          'The object is always global',
                          'The object is on the heap',
                          'The object is a pointer'],
                        0,
                        'const expresses a non-modification guarantee through that interface.'],
                      [ 'Why are dangling references dangerous?',
                        [ 'They refer to objects whose lifetime has ended',
                          'They always point to zero',
                          'They are automatically repaired',
                          'They are faster'],
                        0,
                        'Access through a dangling reference is invalid.'],
                      [ 'What is a good defensive practice?',
                        [ 'Make ownership and lifetime explicit',
                          'Ignore compiler warnings',
                          'Use uninitialized pointers',
                          'Assume every index is valid'],
                        0,
                        'Clear ownership and validation reduce lifetime bugs.']],
    'summary': 'You should now be able to explain undefined behavior, lifetime & const, recognize its syntax, trace '
               'the worked example, and use the concept in a small original program.',
    'next_lesson': 'Headers, Forward Declarations & Include Guards',
    'rules': [ 'Name and trace the role of each undefined behavior before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the undefined behavior, '
            'lifetime & const exercise.',
    'extension': 'Add one realistic requirement to the undefined behavior, lifetime & const exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain undefined behavior, lifetime & const without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_44'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Undefined Behavior, Lifetime & const gives you the foundation needed to read, change, and '
                      'reason about a program before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Undefined Behavior, Lifetime & const** in one sentence before '
                         'writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Undefined '
                         'Behavior, Lifetime & const**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Undefined Behavior, Lifetime & const** task: Review several '
                            'snippets and label them well-defined, implementation-dependent, or undefined, explaining '
                            'the reasoning. Then create one small variation that changes an input, rule, or data case '
                            'without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Undefined Behavior, Lifetime & const** program that exhibits this '
                  'common mistake: **Memorizing undefined behavior syntax without being able to explain what changes '
                  'in the program.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Undefined Behavior, Lifetime & const** to a small real-world feature. Keep the same '
                     'core rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what undefined behavior, lifetime & const means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for undefined behavior, lifetime '
                                                 '& const.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small undefined behavior, lifetime & const '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Undefined Behavior, Lifetime & '
                                  'const.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Undefined Behavior, Lifetime & const without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Undefined '
                                  'Behavior, Lifetime & const.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_46',
    'title': 'Headers, Forward Declarations & Include Guards',
    'description': 'Split declarations from definitions and understand why headers, forward declarations, include '
                   'guards, and #pragma once matter in multi-file programs.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Headers, Forward Declarations & Include Guards**, understand why '
                    'it is useful, trace a focused example, practice it with guidance, then solve an independent '
                    'variation. You will finish by proving your understanding through concept, syntax, code-reading, '
                    'debugging, and application checks.',
    'learning_objectives': [ 'Explain what headers, forward declarations & include guards means and why it exists.',
                             'Read and write the core syntax used for headers, forward declarations & include guards.',
                             'Predict the behavior of a small headers, forward declarations & include guards example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['declaration', 'definition', 'header', 'translation unit'],
    'explanation': 'Split declarations from definitions and understand why headers, forward declarations, include '
                   'guards, and #pragma once matter in multi-file programs. C++ syntax is shown with the standard '
                   'library names used in this lesson. Read the declaration from left to right: identify the type or '
                   'template, the name, the operation, and the terminating punctuation.',
    'syntax': '// student.h\n#pragma once\nclass Student { public: void print() const; };',
    'syntax_breakdown': [ 'Focus on declaration: identify what it represents and what role it plays in the statement.',
                          'Next inspect definition: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '// student.h\n#pragma once\nclass Student { public: void print() const; };',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': '// math.hpp\n#pragma once\nint add(int, int);\n// math.cpp\nint add(int a,int b){ return a+b; }',
    'example2_explanation': 'Change one meaningful input or rule related to headers, forward declarations & include '
                            'guards, predict the result, and only then run the program.',
    'practical_example': 'Imagine a small headers, forward declarations & include guards feature in a student or '
                         'inventory program. Decide what data enters the feature, what rule the feature applies, and '
                         'what result it should produce.',
    'common_mistakes': [ 'Memorizing declaration syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make declaration behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each declaration before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Split a small class into .hpp and .cpp files and explain which code belongs in each.',
    'practice_problem': '**Headers, Forward Declarations & Include Guards independent practice:** Split a small class '
                        'into .hpp and .cpp files and explain which code belongs in each. You must also add one '
                        "clearly different variation and test it. Your work should demonstrate the lesson's main rule, "
                        'not merely reproduce Example 1.',
    'expected_output': '**Test contract for Headers, Forward Declarations & Include Guards:** Run the program with a '
                       'normal case, a boundary case, and a misuse/invalid case when relevant. For each case, record '
                       'the actual result and compare it with the requirement. A correct submission must preserve the '
                       'lesson rule and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Headers, Forward Declarations & Include Guards: What belongs in a header most commonly?',
                        ['Declarations and interfaces', 'The entire executable', 'Runtime logs only', 'Passwords'],
                        0,
                        'Headers commonly expose declarations and interfaces.'],
                      [ 'What does #pragma once help prevent?',
                        ['Repeated inclusion of the same header', 'Memory leaks', 'Threads', 'Sorting'],
                        0,
                        'It prevents multiple inclusion in common toolchains.'],
                      [ 'What is a forward declaration?',
                        [ 'A declaration that tells the compiler a name/type exists before its full definition',
                          'A runtime object',
                          'A loop',
                          'A file copy'],
                        0,
                        'Forward declarations reduce dependency requirements when a full definition is unnecessary.'],
                      [ 'Why separate declaration and definition?',
                        [ 'It supports multi-file organization and clearer interfaces',
                          'It removes linking',
                          'It prevents classes',
                          'It disables tests'],
                        0,
                        'Separation is a core part of maintainable multi-file C++.'],
                      [ 'What is a translation unit built from?',
                        [ 'A source file after preprocessing',
                          'Only a header filename',
                          'A database row',
                          'A runtime thread'],
                        0,
                        'The preprocessed source forms a translation unit.']],
    'summary': 'You should now be able to explain headers, forward declarations & include guards, recognize its '
               'syntax, trace the worked example, and use the concept in a small original program.',
    'next_lesson': 'Namespaces & Scope',
    'rules': [ 'Name and trace the role of each declaration before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the headers, forward '
            'declarations & include guards exercise.',
    'extension': 'Add one realistic requirement to the headers, forward declarations & include guards exercise while '
                 'keeping the original behavior correct.',
    'learning_checks': [ 'Can I explain headers, forward declarations & include guards without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_45'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Headers, Forward Declarations & Include Guards gives you the foundation needed to read, change, '
                      'and reason about a program before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Headers, Forward Declarations & Include Guards** in one sentence '
                         'before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Headers, Forward '
                         'Declarations & Include Guards**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Headers, Forward Declarations & Include Guards** task: Split a '
                            'small class into .hpp and .cpp files and explain which code belongs in each. Then create '
                            'one small variation that changes an input, rule, or data case without changing the main '
                            'goal.',
    'debug_task': 'Debug a deliberately small **Headers, Forward Declarations & Include Guards** program that exhibits '
                  'this common mistake: **Memorizing declaration syntax without being able to explain what changes in '
                  'the program.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Headers, Forward Declarations & Include Guards** to a small real-world feature. Keep '
                     'the same core rule, but change the context and explain which part of the solution remains '
                     'reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what headers, forward declarations & include guards means '
                                                 'and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for headers, forward '
                                                 'declarations & include guards.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small headers, forward declarations & '
                                                 'include guards example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Headers, Forward Declarations & '
                                  'Include Guards.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Headers, Forward Declarations & Include Guards '
                                  'without violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Headers, '
                                  'Forward Declarations & Include Guards.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_47',
    'title': 'Namespaces & Scope',
    'description': 'Use namespaces to prevent naming collisions, qualify names with std::, and understand nested '
                   'scopes and using declarations.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Namespaces & Scope**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what namespaces & scope means and why it exists.',
                             'Read and write the core syntax used for namespaces & scope.',
                             'Predict the behavior of a small namespaces & scope example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['namespace', 'qualification', 'scope', 'using declaration'],
    'explanation': 'Use namespaces to prevent naming collisions, qualify names with std::, and understand nested '
                   'scopes and using declarations. C++ syntax is shown with the standard library names used in this '
                   'lesson. Read the declaration from left to right: identify the type or template, the name, the '
                   'operation, and the terminating punctuation.',
    'syntax': 'namespace school { int year = 2026; }\ncout << school::year;',
    'syntax_breakdown': [ 'Focus on namespace: identify what it represents and what role it plays in the statement.',
                          'Next inspect qualification: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'namespace school { int year = 2026; }\ncout << school::year;',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'int score = 70;\n{\n    int bonus = 5;\n    score += bonus;\n}\ncout << score;',
    'example2_explanation': 'Change one meaningful input or rule related to namespaces & scope, predict the result, '
                            'and only then run the program.',
    'practical_example': 'Imagine a small namespaces & scope feature in a student or inventory program. Decide what '
                         'data enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing namespace syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make namespace behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each namespace before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Create two namespaces that both define a helper named print and call each one unambiguously.',
    'practice_problem': '**Namespaces & Scope independent practice:** Create two namespaces that both define a helper '
                        'named print and call each one unambiguously. You must also add one clearly different '
                        "variation and test it. Your work should demonstrate the lesson's main rule, not merely "
                        'reproduce Example 1.',
    'expected_output': '**Test contract for Namespaces & Scope:** Run the program with a normal case, a boundary case, '
                       'and a misuse/invalid case when relevant. For each case, record the actual result and compare '
                       'it with the requirement. A correct submission must preserve the lesson rule and handle the '
                       'defined edge case safely.',
    'mastery_quiz': [ [ 'Namespaces & Scope: Why use a namespace?',
                        ['To avoid naming collisions', 'To allocate heap memory', 'To read files', 'To create loops'],
                        0,
                        'Namespaces group names and prevent collisions.'],
                      [ 'What does std::vector mean?',
                        [ 'vector inside the std namespace',
                          'A global vector',
                          'A Java collection',
                          'A compiler command'],
                        0,
                        'std:: qualifies the vector name from the standard namespace.'],
                      [ 'What does a nested scope affect?',
                        [ 'Where a name can be referenced',
                          'The CPU clock',
                          'The file extension',
                          'The language version'],
                        0,
                        'Scope determines name visibility.'],
                      [ 'Why can broad using-directives be risky in large code?',
                        [ 'They can introduce ambiguous names',
                          'They make programs compile faster',
                          'They remove namespaces',
                          'They disable templates'],
                        0,
                        'Large namespaces can contain colliding names.'],
                      [ 'What is a qualified name?',
                        [ 'A name written with its namespace or enclosing scope',
                          'A password',
                          'A compiler flag',
                          'A loop counter'],
                        0,
                        'Qualification identifies exactly which scope owns a name.']],
    'summary': 'You should now be able to explain namespaces & scope, recognize its syntax, trace the worked example, '
               'and use the concept in a small original program.',
    'next_lesson': 'Compiler, Linker & Translation Units',
    'rules': [ 'Name and trace the role of each namespace before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the namespaces & scope '
            'exercise.',
    'extension': 'Add one realistic requirement to the namespaces & scope exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain namespaces & scope without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_46'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Namespaces & Scope gives you the foundation needed to read, change, and reason about a program '
                      'before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Namespaces & Scope** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Namespaces & '
                         'Scope**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Namespaces & Scope** task: Create two namespaces that both '
                            'define a helper named print and call each one unambiguously. Then create one small '
                            'variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Namespaces & Scope** program that exhibits this common mistake: '
                  '**Memorizing namespace syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Namespaces & Scope** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what namespaces & scope means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for namespaces & scope.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small namespaces & scope example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Namespaces & Scope.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Namespaces & Scope without violating the '
                                  'stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Namespaces & '
                                  'Scope.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_48',
    'title': 'Compiler, Linker & Translation Units',
    'description': 'Trace the path from preprocessing through compilation and linking, and diagnose common '
                   'declaration, definition, and linker errors.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Compiler, Linker & Translation Units**, understand why it is '
                    'useful, trace a focused example, practice it with guidance, then solve an independent variation. '
                    'You will finish by proving your understanding through concept, syntax, code-reading, debugging, '
                    'and application checks.',
    'learning_objectives': [ 'Explain what compiler, linker & translation units means and why it exists.',
                             'Read and write the core syntax used for compiler, linker & translation units.',
                             'Predict the behavior of a small compiler, linker & translation units example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['preprocessing', 'translation unit', 'object file', 'linker'],
    'explanation': 'Trace the path from preprocessing through compilation and linking, and diagnose common '
                   'declaration, definition, and linker errors. C++ syntax is shown with the standard library names '
                   'used in this lesson. Read the declaration from left to right: identify the type or template, the '
                   'name, the operation, and the terminating punctuation.',
    'syntax': '// a.cpp\nint add(int a,int b){return a+b;}\n// b.cpp\nint add(int,int);',
    'syntax_breakdown': [ 'Focus on preprocessing: identify what it represents and what role it plays in the '
                          'statement.',
                          'Next inspect translation unit: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '// a.cpp\nint add(int a,int b){return a+b;}\n// b.cpp\nint add(int,int);',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': '// a.cpp\n'
                'int add(int a,int b){return a+b;}\n'
                '// main.cpp\n'
                'int add(int,int);\n'
                'int main(){return add(2,3);} ',
    'example2_explanation': 'Change one meaningful input or rule related to compiler, linker & translation units, '
                            'predict the result, and only then run the program.',
    'practical_example': 'Imagine a small compiler, linker & translation units feature in a student or inventory '
                         'program. Decide what data enters the feature, what rule the feature applies, and what result '
                         'it should produce.',
    'common_mistakes': [ 'Memorizing preprocessing syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make preprocessing behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each preprocessing before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Explain why a program can compile each source file successfully but fail during linking.',
    'practice_problem': '**Compiler, Linker & Translation Units independent practice:** Explain why a program can '
                        'compile each source file successfully but fail during linking. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Compiler, Linker & Translation Units:** Run the program with a normal '
                       'case, a boundary case, and a misuse/invalid case when relevant. For each case, record the '
                       'actual result and compare it with the requirement. A correct submission must preserve the '
                       'lesson rule and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Compiler, Linker & Translation Units: What is a translation unit?',
                        [ 'A source file after preprocessing',
                          'A runtime thread',
                          'A database table',
                          'A debugger window'],
                        0,
                        'A translation unit is the preprocessed source that a compiler compiles.'],
                      [ 'What does the linker do?',
                        [ 'Combines object files and resolves symbols',
                          'Reads user input',
                          'Runs loops',
                          'Formats strings'],
                        0,
                        'The linker connects separately compiled pieces.'],
                      [ 'What kind of problem often produces an undefined reference/linker error?',
                        [ 'A declaration exists but the required definition is missing',
                          'A variable is too descriptive',
                          'A comment is too long',
                          'A loop has braces'],
                        0,
                        'Linkers need definitions for referenced symbols.'],
                      [ 'Why use headers?',
                        [ 'To share declarations and interfaces between translation units',
                          'To execute code twice',
                          'To replace libraries',
                          'To store passwords'],
                        0,
                        'Headers commonly expose declarations needed by other source files.'],
                      [ 'Why does include order matter sometimes?',
                        [ 'Declarations and macro/configuration state can affect what later code sees',
                          'It changes the CPU',
                          'It changes Java bytecode',
                          'It removes all types'],
                        0,
                        'The preprocessor works in source order.']],
    'summary': 'You should now be able to explain compiler, linker & translation units, recognize its syntax, trace '
               'the worked example, and use the concept in a small original program.',
    'next_lesson': 'Build Systems with CMake',
    'rules': [ 'Name and trace the role of each preprocessing before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the compiler, linker & '
            'translation units exercise.',
    'extension': 'Add one realistic requirement to the compiler, linker & translation units exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain compiler, linker & translation units without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_47'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Compiler, Linker & Translation Units gives you the foundation needed to read, change, and '
                      'reason about a program before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Compiler, Linker & Translation Units** in one sentence before '
                         'writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Compiler, Linker & '
                         'Translation Units**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Compiler, Linker & Translation Units** task: Explain why a '
                            'program can compile each source file successfully but fail during linking. Then create '
                            'one small variation that changes an input, rule, or data case without changing the main '
                            'goal.',
    'debug_task': 'Debug a deliberately small **Compiler, Linker & Translation Units** program that exhibits this '
                  'common mistake: **Memorizing preprocessing syntax without being able to explain what changes in the '
                  'program.**. Before changing code, identify the first incorrect value, state, control-flow decision, '
                  'or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Compiler, Linker & Translation Units** to a small real-world feature. Keep the same '
                     'core rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what compiler, linker & translation units means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for compiler, linker & '
                                                 'translation units.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small compiler, linker & translation units '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Compiler, Linker & Translation '
                                  'Units.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Compiler, Linker & Translation Units without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Compiler, '
                                  'Linker & Translation Units.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_49',
    'title': 'Build Systems with CMake',
    'description': 'Understand why larger C++ projects use build systems and learn the purpose of targets, source '
                   'files, include directories, and build configurations.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Build Systems with CMake**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what build systems with cmake means and why it exists.',
                             'Read and write the core syntax used for build systems with cmake.',
                             'Predict the behavior of a small build systems with cmake example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['target', 'configure', 'build', 'CMakeLists.txt'],
    'explanation': 'Understand why larger C++ projects use build systems and learn the purpose of targets, source '
                   'files, include directories, and build configurations. C++ syntax is shown with the standard '
                   'library names used in this lesson. Read the declaration from left to right: identify the type or '
                   'template, the name, the operation, and the terminating punctuation.',
    'syntax': 'cmake_minimum_required(VERSION 3.20)\nproject(ClassCodeDemo)\nadd_executable(app main.cpp math.cpp)',
    'syntax_breakdown': [ 'Focus on target: identify what it represents and what role it plays in the statement.',
                          'Next inspect configure: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'cmake_minimum_required(VERSION 3.20)\nproject(ClassCodeDemo)\nadd_executable(app main.cpp math.cpp)',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'cmake_minimum_required(VERSION 3.20)\nproject(Demo)\nadd_executable(demo main.cpp)',
    'example2_explanation': 'Change one meaningful input or rule related to build systems with cmake, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small build systems with cmake feature in a student or inventory program. Decide '
                         'what data enters the feature, what rule the feature applies, and what result it should '
                         'produce.',
    'common_mistakes': [ 'Memorizing target syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make target behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each target before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Create a minimal two-file CMake project and describe configure, build, and run stages.',
    'practice_problem': '**Build Systems with CMake independent practice:** Create a minimal two-file CMake project '
                        'and describe configure, build, and run stages. You must also add one clearly different '
                        "variation and test it. Your work should demonstrate the lesson's main rule, not merely "
                        'reproduce Example 1.',
    'expected_output': '**Test contract for Build Systems with CMake:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'Build Systems with CMake: What is a CMake target?',
                        [ 'A buildable or linkable unit such as an executable or library',
                          'A runtime variable',
                          'A debugger breakpoint',
                          'A database row'],
                        0,
                        'Targets describe build outputs and their relationships.'],
                      [ 'What does configure mean conceptually?',
                        [ 'Generate build-system files from project configuration',
                          'Run the final program',
                          'Delete source files',
                          'Format C++ code'],
                        0,
                        'CMake configuration prepares a build system.'],
                      [ 'Why use a build system?',
                        [ 'To manage multiple source files, dependencies, and build settings consistently',
                          'To replace the compiler',
                          'To avoid linking',
                          'To remove tests'],
                        0,
                        'Build systems automate project-wide build relationships.'],
                      [ 'Where are CMake project instructions commonly stored?',
                        ['CMakeLists.txt', 'main.cpp only', 'README.exe', 'package.java'],
                        0,
                        'CMake reads CMakeLists.txt files.'],
                      [ 'Why separate build configuration from source logic?',
                        [ 'It keeps toolchain/build concerns manageable',
                          'It makes source code invalid',
                          'It removes executables',
                          'It disables libraries'],
                        0,
                        'Separation keeps project configuration maintainable.']],
    'summary': 'You should now be able to explain build systems with cmake, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Debugging with Breakpoints & Diagnostics',
    'rules': [ 'Name and trace the role of each target before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the build systems with '
            'cmake exercise.',
    'extension': 'Add one realistic requirement to the build systems with cmake exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain build systems with cmake without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_48'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Build Systems with CMake gives you the foundation needed to read, change, and reason about a '
                      'program before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Build Systems with CMake** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Build Systems with '
                         'CMake**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Build Systems with CMake** task: Create a minimal two-file '
                            'CMake project and describe configure, build, and run stages. Then create one small '
                            'variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Build Systems with CMake** program that exhibits this common mistake: '
                  '**Memorizing target syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Build Systems with CMake** to a small real-world feature. Keep the same core rule, '
                     'but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what build systems with cmake means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for build systems with cmake.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small build systems with cmake example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Build Systems with CMake.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Build Systems with CMake without violating the '
                                  'stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Build Systems '
                                  'with CMake.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_50',
    'title': 'Debugging with Breakpoints & Diagnostics',
    'description': 'Use a debugger mindset: set breakpoints, inspect variables, step over/into functions, read call '
                   'stacks, and isolate state changes.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Debugging with Breakpoints & Diagnostics**, understand why it is '
                    'useful, trace a focused example, practice it with guidance, then solve an independent variation. '
                    'You will finish by proving your understanding through concept, syntax, code-reading, debugging, '
                    'and application checks.',
    'learning_objectives': [ 'Explain what debugging with breakpoints & diagnostics means and why it exists.',
                             'Read and write the core syntax used for debugging with breakpoints & diagnostics.',
                             'Predict the behavior of a small debugging with breakpoints & diagnostics example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['breakpoint', 'step over', 'step into', 'call stack'],
    'explanation': 'Use a debugger mindset: set breakpoints, inspect variables, step over/into functions, read call '
                   'stacks, and isolate state changes. C++ syntax is shown with the standard library names used in '
                   'this lesson. Read the declaration from left to right: identify the type or template, the name, the '
                   'operation, and the terminating punctuation.',
    'syntax': 'int total = price * quantity;\n// Set a breakpoint here and inspect price, quantity, total.',
    'syntax_breakdown': [ 'Focus on breakpoint: identify what it represents and what role it plays in the statement.',
                          'Next inspect step over: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'int total = price * quantity;\n// Set a breakpoint here and inspect price, quantity, total.',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'int total(int price, int quantity) {\n'
                '    assert(price >= 0);\n'
                '    assert(quantity >= 0);\n'
                '    return price * quantity;\n'
                '}',
    'example2_explanation': 'Change one meaningful input or rule related to debugging with breakpoints & diagnostics, '
                            'predict the result, and only then run the program.',
    'practical_example': 'Imagine a small debugging with breakpoints & diagnostics feature in a student or inventory '
                         'program. Decide what data enters the feature, what rule the feature applies, and what result '
                         'it should produce.',
    'common_mistakes': [ 'Memorizing breakpoint syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make breakpoint behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each breakpoint before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Given a wrong total, describe exactly which variables you would inspect and which execution steps you '
                'would follow.',
    'practice_problem': '**Debugging with Breakpoints & Diagnostics independent practice:** Given a wrong total, '
                        'describe exactly which variables you would inspect and which execution steps you would '
                        'follow. You must also add one clearly different variation and test it. Your work should '
                        "demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Debugging with Breakpoints & Diagnostics:** Run the program with a normal '
                       'case, a boundary case, and a misuse/invalid case when relevant. For each case, record the '
                       'actual result and compare it with the requirement. A correct submission must preserve the '
                       'lesson rule and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Debugging with Breakpoints & Diagnostics: What should a debugger help you inspect?',
                        [ 'Program state and execution flow',
                          'Only source-code colors',
                          'Only filenames',
                          'Only comments'],
                        0,
                        'Debuggers let you inspect state while stepping through execution.'],
                      [ 'What is a breakpoint?',
                        [ 'A location where execution pauses for inspection',
                          'A compile error',
                          'A file format',
                          'A loop keyword'],
                        0,
                        'Breakpoints pause execution.'],
                      [ 'What is a good first debugging step?',
                        [ 'Reproduce the problem with the smallest useful case',
                          'Rewrite the whole program',
                          'Ignore the error message',
                          'Change five functions'],
                        0,
                        'A reproducible small case narrows the search.'],
                      [ 'What does an assertion check?',
                        [ 'An assumption that should hold during execution',
                          'A user password',
                          'A file extension',
                          'A compiler version'],
                        0,
                        'Assertions verify assumptions.'],
                      [ 'Why write boundary tests?',
                        [ 'They reveal mistakes around limits and transitions',
                          'They make code longer only',
                          'They replace compilation',
                          'They guarantee no bugs'],
                        0,
                        'Boundary tests target common logic failures.']],
    'summary': 'You should now be able to explain debugging with breakpoints & diagnostics, recognize its syntax, '
               'trace the worked example, and use the concept in a small original program.',
    'next_lesson': 'C++ Standards & Feature Selection',
    'rules': [ 'Name and trace the role of each breakpoint before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the debugging with '
            'breakpoints & diagnostics exercise.',
    'extension': 'Add one realistic requirement to the debugging with breakpoints & diagnostics exercise while keeping '
                 'the original behavior correct.',
    'learning_checks': [ 'Can I explain debugging with breakpoints & diagnostics without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_49'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Debugging with Breakpoints & Diagnostics matters because useful programs must detect, explain, '
                      'and recover from incorrect states instead of silently failing.',
    'guided_practice': [ '1. Restate the goal of **Debugging with Breakpoints & Diagnostics** in one sentence before '
                         'writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Debugging with '
                         'Breakpoints & Diagnostics**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Debugging with Breakpoints & Diagnostics** task: Given a wrong '
                            'total, describe exactly which variables you would inspect and which execution steps you '
                            'would follow. Then create one small variation that changes an input, rule, or data case '
                            'without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Debugging with Breakpoints & Diagnostics** program that exhibits this '
                  'common mistake: **Memorizing breakpoint syntax without being able to explain what changes in the '
                  'program.**. Before changing code, identify the first incorrect value, state, control-flow decision, '
                  'or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Debugging with Breakpoints & Diagnostics** to a small real-world feature. Keep the '
                     'same core rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what debugging with breakpoints & diagnostics means and why '
                                                 'it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for debugging with breakpoints & '
                                                 'diagnostics.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small debugging with breakpoints & '
                                                 'diagnostics example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Debugging with Breakpoints & '
                                  'Diagnostics.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Debugging with Breakpoints & Diagnostics '
                                  'without violating the stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['error', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_51',
    'title': 'C++ Standards & Feature Selection',
    'description': 'Recognize major modern C++ eras and choose language features based on the compiler/toolchain and '
                   'project requirements instead of blindly using the newest syntax.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **C++ Standards & Feature Selection**, understand why it is useful, '
                    'trace a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what c++ standards & feature selection means and why it exists.',
                             'Read and write the core syntax used for c++ standards & feature selection.',
                             'Predict the behavior of a small c++ standards & feature selection example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['standard', 'compiler mode', 'feature', 'compatibility'],
    'explanation': 'Recognize major modern C++ eras and choose language features based on the compiler/toolchain and '
                   'project requirements instead of blindly using the newest syntax. C++ syntax is shown with the '
                   'standard library names used in this lesson. Read the declaration from left to right: identify the '
                   'type or template, the name, the operation, and the terminating punctuation.',
    'syntax': 'auto value = 42;              // C++11\nauto [name, score] = student;  // C++17',
    'syntax_breakdown': [ 'Focus on standard: identify what it represents and what role it plays in the statement.',
                          'Next inspect compiler mode: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'auto value = 42;              // C++11\nauto [name, score] = student;  // C++17',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'auto value = 42;\nauto [a,b] = pair{1,2};\n// automatic type deduction plus structured binding',
    'example2_explanation': 'Change one meaningful input or rule related to c++ standards & feature selection, predict '
                            'the result, and only then run the program.',
    'practical_example': 'Imagine a small c++ standards & feature selection feature in a student or inventory program. '
                         'Decide what data enters the feature, what rule the feature applies, and what result it '
                         'should produce.',
    'common_mistakes': [ 'Memorizing standard syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make standard behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each standard before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Take a small program and identify which features require C++11, C++17, or C++20 support.',
    'practice_problem': '**C++ Standards & Feature Selection independent practice:** Take a small program and identify '
                        'which features require C++11, C++17, or C++20 support. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for C++ Standards & Feature Selection:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'C++ Standards & Feature Selection: Why specify a C++ standard in a build?',
                        [ 'To control which language/library features are available',
                          'To rename variables',
                          'To choose a monitor',
                          'To create a database'],
                        0,
                        'The selected standard affects available language and library features.'],
                      [ 'Which feature is associated with C++17?',
                        ['Structured bindings', 'std::jthread', 'Concepts', 'Coroutines'],
                        0,
                        'Structured bindings were introduced in C++17.'],
                      [ 'Which feature is associated with C++20?',
                        ['Concepts', 'Structured bindings', 'nullptr', 'auto'],
                        0,
                        'Concepts are a C++20 feature.'],
                      [ 'Why avoid using a feature unsupported by the project compiler?',
                        [ 'The project may fail to build',
                          'It makes comments longer',
                          'It changes Java',
                          'It removes memory'],
                        0,
                        'Toolchain compatibility is a real project constraint.'],
                      [ 'What is a good modern C++ practice?',
                        [ 'Use the project-supported standard deliberately',
                          'Always use the newest feature regardless of toolchain',
                          'Never update dependencies',
                          'Avoid documentation'],
                        0,
                        'Feature selection should match project constraints.']],
    'summary': 'You should now be able to explain c++ standards & feature selection, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Concepts & Constraints',
    'rules': [ 'Name and trace the role of each standard before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the c++ standards & '
            'feature selection exercise.',
    'extension': 'Add one realistic requirement to the c++ standards & feature selection exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain c++ standards & feature selection without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_50'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'C++ Standards & Feature Selection gives you the foundation needed to read, change, and reason '
                      'about a program before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **C++ Standards & Feature Selection** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **C++ Standards & '
                         'Feature Selection**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **C++ Standards & Feature Selection** task: Take a small program '
                            'and identify which features require C++11, C++17, or C++20 support. Then create one small '
                            'variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **C++ Standards & Feature Selection** program that exhibits this common '
                  'mistake: **Memorizing standard syntax without being able to explain what changes in the program.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **C++ Standards & Feature Selection** to a small real-world feature. Keep the same core '
                     'rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what c++ standards & feature selection means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for c++ standards & feature '
                                                 'selection.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small c++ standards & feature selection '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for C++ Standards & Feature '
                                  'Selection.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for C++ Standards & Feature Selection without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in C++ Standards '
                                  '& Feature Selection.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_52',
    'title': 'Concepts & Constraints',
    'description': 'Use C++20 concepts to express requirements on template parameters and produce clearer diagnostics '
                   'than unconstrained templates.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Concepts & Constraints**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what concepts & constraints means and why it exists.',
                             'Read and write the core syntax used for concepts & constraints.',
                             'Predict the behavior of a small concepts & constraints example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['concept', 'constraint', 'requires', 'diagnostics'],
    'explanation': 'Use C++20 concepts to express requirements on template parameters and produce clearer diagnostics '
                   'than unconstrained templates. C++ syntax is shown with the standard library names used in this '
                   'lesson. Read the declaration from left to right: identify the type or template, the name, the '
                   'operation, and the terminating punctuation.',
    'syntax': 'template <typename T>\n'
              'concept Number = std::is_arithmetic_v<T>;\n'
              '\n'
              'template <Number T> T square(T x) { return x * x; }',
    'syntax_breakdown': [ 'Focus on concept: identify what it represents and what role it plays in the statement.',
                          'Next inspect constraint: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'template <typename T>\n'
                'concept Number = std::is_arithmetic_v<T>;\n'
                '\n'
                'template <Number T> T square(T x) { return x * x; }',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'const int limit = 100;\nconst int* p = &limit;\ncout << *p;',
    'example2_explanation': 'Change one meaningful input or rule related to concepts & constraints, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small concepts & constraints feature in a student or inventory program. Decide '
                         'what data enters the feature, what rule the feature applies, and what result it should '
                         'produce.',
    'common_mistakes': [ 'Memorizing concept syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make concept behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each concept before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Constrain a generic function so it accepts arithmetic types and explain why the constraint improves '
                'the interface.',
    'practice_problem': '**Concepts & Constraints independent practice:** Constrain a generic function so it accepts '
                        'arithmetic types and explain why the constraint improves the interface. You must also add one '
                        "clearly different variation and test it. Your work should demonstrate the lesson's main rule, "
                        'not merely reproduce Example 1.',
    'expected_output': '**Test contract for Concepts & Constraints:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'Concepts & Constraints: What does a concept describe?',
                        [ 'Requirements a template argument must satisfy',
                          'A runtime thread',
                          'A file format',
                          'A database table'],
                        0,
                        'Concepts constrain template arguments.'],
                      [ 'Why use requires/constraints?',
                        [ 'To express valid operations and improve diagnostics',
                          'To remove type checking',
                          'To make every type valid',
                          'To avoid compilation'],
                        0,
                        'Constraints make generic interfaces clearer.'],
                      [ 'When should a generic function reject a type?',
                        [ 'When the type does not satisfy the operations the function needs',
                          'Only at runtime',
                          'Never',
                          'Only for strings'],
                        0,
                        'A constraint should describe the function’s real requirements.'],
                      [ 'What is a benefit over an unconstrained template?',
                        [ 'Errors are expressed closer to the interface requirement',
                          'It disables templates',
                          'It always runs faster',
                          'It removes code reuse'],
                        0,
                        'Constraints can produce clearer compile-time diagnostics.'],
                      [ 'What does a concept not do?',
                        [ 'It does not automatically implement missing operations',
                          'It checks requirements',
                          'It documents intent',
                          'It participates in overload resolution'],
                        0,
                        'A concept constrains types; it does not create missing behavior.']],
    'summary': 'You should now be able to explain concepts & constraints, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Ranges & Views',
    'rules': [ 'Name and trace the role of each concept before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the concepts & '
            'constraints exercise.',
    'extension': 'Add one realistic requirement to the concepts & constraints exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain concepts & constraints without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_51'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Concepts & Constraints gives you the foundation needed to read, change, and reason about a '
                      'program before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Concepts & Constraints** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Concepts & '
                         'Constraints**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Concepts & Constraints** task: Constrain a generic function so '
                            'it accepts arithmetic types and explain why the constraint improves the interface. Then '
                            'create one small variation that changes an input, rule, or data case without changing the '
                            'main goal.',
    'debug_task': 'Debug a deliberately small **Concepts & Constraints** program that exhibits this common mistake: '
                  '**Memorizing concept syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Concepts & Constraints** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what concepts & constraints means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for concepts & constraints.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small concepts & constraints example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Concepts & Constraints.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Concepts & Constraints without violating the '
                                  'stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Concepts & '
                                  'Constraints.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_53',
    'title': 'Ranges & Views',
    'description': 'Use C++20 ranges to compose lazy transformations and filters while keeping data-processing '
                   'pipelines readable.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Ranges & Views**, understand why it is useful, trace a focused '
                    'example, practice it with guidance, then solve an independent variation. You will finish by '
                    'proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what ranges & views means and why it exists.',
                             'Read and write the core syntax used for ranges & views.',
                             'Predict the behavior of a small ranges & views example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['range', 'view', 'pipeline', 'lazy evaluation'],
    'explanation': 'Use C++20 ranges to compose lazy transformations and filters while keeping data-processing '
                   'pipelines readable. C++ syntax is shown with the standard library names used in this lesson. Read '
                   'the declaration from left to right: identify the type or template, the name, the operation, and '
                   'the terminating punctuation.',
    'syntax': 'auto result = values | std::views::filter([](int x){ return x % 2 == 0; });',
    'syntax_breakdown': [ 'Focus on range: identify what it represents and what role it plays in the statement.',
                          'Next inspect view: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'auto result = values | std::views::filter([](int x){ return x % 2 == 0; });',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'auto evens = values | std::views::filter([](int x){return x%2==0;});\nfor(int x: evens) cout << x;',
    'example2_explanation': 'Change one meaningful input or rule related to ranges & views, predict the result, and '
                            'only then run the program.',
    'practical_example': 'Imagine a small ranges & views feature in a student or inventory program. Decide what data '
                         'enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing range syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make range behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each range before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Build a pipeline that filters positive values, transforms them, and explains why a view is lazy.',
    'practice_problem': '**Ranges & Views independent practice:** Build a pipeline that filters positive values, '
                        'transforms them, and explains why a view is lazy. You must also add one clearly different '
                        "variation and test it. Your work should demonstrate the lesson's main rule, not merely "
                        'reproduce Example 1.',
    'expected_output': '**Test contract for Ranges & Views:** Run the program with a normal case, a boundary case, and '
                       'a misuse/invalid case when relevant. For each case, record the actual result and compare it '
                       'with the requirement. A correct submission must preserve the lesson rule and handle the '
                       'defined edge case safely.',
    'mastery_quiz': [ [ 'Ranges & Views: What is a range view?',
                        [ 'A composable, often lazy way to process a sequence',
                          'A database view only',
                          'A thread',
                          'A compiler'],
                        0,
                        'Views describe sequence processing without necessarily materializing a new container.'],
                      [ 'Why are views often lazy?',
                        [ 'Work can be performed as elements are requested',
                          'They always copy data',
                          'They disable iteration',
                          'They require a GUI'],
                        0,
                        'Lazy views defer transformations until iteration.'],
                      [ 'What does filter do?',
                        [ 'Keeps elements satisfying a predicate',
                          'Sorts automatically',
                          'Writes a file',
                          'Changes every type'],
                        0,
                        'filter selects matching elements.'],
                      [ 'Why compose range operations?',
                        [ 'A pipeline can express several transformations clearly',
                          'It removes type checking',
                          'It avoids all tests',
                          'It forces global state'],
                        0,
                        'Pipelines make data-processing steps explicit.'],
                      [ 'What should you consider with a view?',
                        [ 'The lifetime of the underlying range',
                          'Only the variable name',
                          'The monitor size',
                          'The package name'],
                        0,
                        'A view can refer to underlying data, so lifetime matters.']],
    'summary': 'You should now be able to explain ranges & views, recognize its syntax, trace the worked example, and '
               'use the concept in a small original program.',
    'next_lesson': 'Coroutines & Asynchronous Thinking',
    'rules': [ 'Name and trace the role of each range before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the ranges & views '
            'exercise.',
    'extension': 'Add one realistic requirement to the ranges & views exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain ranges & views without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_52'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Ranges & Views gives you the foundation needed to read, change, and reason about a program '
                      'before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Ranges & Views** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Ranges & Views**, '
                         'then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Ranges & Views** task: Build a pipeline that filters positive '
                            'values, transforms them, and explains why a view is lazy. Then create one small variation '
                            'that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Ranges & Views** program that exhibits this common mistake: '
                  '**Memorizing range syntax without being able to explain what changes in the program.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Ranges & Views** to a small real-world feature. Keep the same core rule, but change '
                     'the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what ranges & views means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for ranges & views.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small ranges & views example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Ranges & Views.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Ranges & Views without violating the stated '
                                  'rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Ranges & '
                                  'Views.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_54',
    'title': 'Coroutines & Asynchronous Thinking',
    'description': 'Understand the idea of suspendable functions and coroutine-based control flow without treating '
                   'coroutines as ordinary threads.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Coroutines & Asynchronous Thinking**, understand why it is '
                    'useful, trace a focused example, practice it with guidance, then solve an independent variation. '
                    'You will finish by proving your understanding through concept, syntax, code-reading, debugging, '
                    'and application checks.',
    'learning_objectives': [ 'Explain what coroutines & asynchronous thinking means and why it exists.',
                             'Read and write the core syntax used for coroutines & asynchronous thinking.',
                             'Predict the behavior of a small coroutines & asynchronous thinking example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['coroutine', 'suspend', 'resume', 'co_await'],
    'explanation': 'Understand the idea of suspendable functions and coroutine-based control flow without treating '
                   'coroutines as ordinary threads. C++ syntax is shown with the standard library names used in this '
                   'lesson. Read the declaration from left to right: identify the type or template, the name, the '
                   'operation, and the terminating punctuation.',
    'syntax': '// Conceptual coroutine shape:\nco_await something_async();',
    'syntax_breakdown': [ 'Focus on coroutine: identify what it represents and what role it plays in the statement.',
                          'Next inspect suspend: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '// Conceptual coroutine shape:\nco_await something_async();',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': '// Coroutine idea: suspend at an await point, then resume later.\nco_await fetchData();',
    'example2_explanation': 'Change one meaningful input or rule related to coroutines & asynchronous thinking, '
                            'predict the result, and only then run the program.',
    'practical_example': 'Imagine a small coroutines & asynchronous thinking feature in a student or inventory '
                         'program. Decide what data enters the feature, what rule the feature applies, and what result '
                         'it should produce.',
    'common_mistakes': [ 'Memorizing coroutine syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make coroutine behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each coroutine before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Explain the difference between a coroutine that suspends and a thread that executes concurrently, '
                'using a simple asynchronous example.',
    'practice_problem': '**Coroutines & Asynchronous Thinking independent practice:** Explain the difference between a '
                        'coroutine that suspends and a thread that executes concurrently, using a simple asynchronous '
                        'example. You must also add one clearly different variation and test it. Your work should '
                        "demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Coroutines & Asynchronous Thinking:** Run the program with a normal case, '
                       'a boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Coroutines & Asynchronous Thinking: What is a coroutine?',
                        [ 'A function-like computation that can suspend and resume',
                          'A thread that always runs in parallel',
                          'A file stream',
                          'A class constructor'],
                        0,
                        'Coroutines support suspend/resume control flow.'],
                      [ 'Does a coroutine automatically create a new OS thread?',
                        ['No', 'Yes always', 'Only in loops', 'Only in C++17'],
                        0,
                        'Coroutines and threads are different mechanisms.'],
                      [ 'What does co_await conceptually do?',
                        [ 'Suspend until an awaitable operation can continue',
                          'Delete a task',
                          'Sort a vector',
                          'Compile a header'],
                        0,
                        'co_await expresses suspension around an asynchronous operation.'],
                      [ 'Why learn coroutine concepts carefully?',
                        [ 'Suspension and resumption are different from ordinary sequential calls',
                          'They replace every function',
                          'They remove all state',
                          'They guarantee parallelism'],
                        0,
                        'Coroutines change control flow and require a clear mental model.'],
                      [ 'What is a useful beginner distinction?',
                        [ 'Coroutine = suspend/resume; thread = independent execution path',
                          'They are identical',
                          'Thread = data type',
                          'Coroutine = file'],
                        0,
                        'The mechanisms solve different problems.']],
    'summary': 'You should now be able to explain coroutines & asynchronous thinking, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Package Managers & Third-Party Libraries',
    'rules': [ 'Name and trace the role of each coroutine before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the coroutines & '
            'asynchronous thinking exercise.',
    'extension': 'Add one realistic requirement to the coroutines & asynchronous thinking exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain coroutines & asynchronous thinking without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_53'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Coroutines & Asynchronous Thinking matters because modern code often transforms data and '
                      'composes behavior in compact, reusable ways.',
    'guided_practice': [ '1. Restate the goal of **Coroutines & Asynchronous Thinking** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Coroutines & '
                         'Asynchronous Thinking**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Coroutines & Asynchronous Thinking** task: Explain the '
                            'difference between a coroutine that suspends and a thread that executes concurrently, '
                            'using a simple asynchronous example. Then create one small variation that changes an '
                            'input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Coroutines & Asynchronous Thinking** program that exhibits this common '
                  'mistake: **Memorizing coroutine syntax without being able to explain what changes in the '
                  'program.**. Before changing code, identify the first incorrect value, state, control-flow decision, '
                  'or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Coroutines & Asynchronous Thinking** to a small real-world feature. Keep the same '
                     'core rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what coroutines & asynchronous thinking means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for coroutines & asynchronous '
                                                 'thinking.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small coroutines & asynchronous thinking '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Coroutines & Asynchronous '
                                  'Thinking.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Coroutines & Asynchronous Thinking without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Coroutines & '
                                  'Asynchronous Thinking.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['functional', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_55',
    'title': 'Package Managers & Third-Party Libraries',
    'description': 'Understand dependency management, versioning, include paths, linking, and why projects use tools '
                   'such as vcpkg, Conan, or system packages.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Package Managers & Third-Party Libraries**, understand why it is '
                    'useful, trace a focused example, practice it with guidance, then solve an independent variation. '
                    'You will finish by proving your understanding through concept, syntax, code-reading, debugging, '
                    'and application checks.',
    'learning_objectives': [ 'Explain what package managers & third-party libraries means and why it exists.',
                             'Read and write the core syntax used for package managers & third-party libraries.',
                             'Predict the behavior of a small package managers & third-party libraries example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['dependency', 'version', 'package manager', 'linking'],
    'explanation': 'Understand dependency management, versioning, include paths, linking, and why projects use tools '
                   'such as vcpkg, Conan, or system packages. C++ syntax is shown with the standard library names used '
                   'in this lesson. Read the declaration from left to right: identify the type or template, the name, '
                   'the operation, and the terminating punctuation.',
    'syntax': '#include <fmt/core.h>\nint main(){ fmt::print("Hello\\n"); }',
    'syntax_breakdown': [ 'Focus on dependency: identify what it represents and what role it plays in the statement.',
                          'Next inspect version: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '#include <fmt/core.h>\nint main(){ fmt::print("Hello\\n"); }',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': '#include <fmt/core.h>\nint main(){ fmt::print("Hello from a library\\n"); }',
    'example2_explanation': 'Change one meaningful input or rule related to package managers & third-party libraries, '
                            'predict the result, and only then run the program.',
    'practical_example': 'Imagine a small package managers & third-party libraries feature in a student or inventory '
                         'program. Decide what data enters the feature, what rule the feature applies, and what result '
                         'it should produce.',
    'common_mistakes': [ 'Memorizing dependency syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make dependency behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each dependency before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Describe the steps needed to add one external library to a C++ project without committing the library '
                'source into your repository.',
    'practice_problem': '**Package Managers & Third-Party Libraries independent practice:** Describe the steps needed '
                        'to add one external library to a C++ project without committing the library source into your '
                        'repository. You must also add one clearly different variation and test it. Your work should '
                        "demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Package Managers & Third-Party Libraries:** Run the program with a normal '
                       'case, a boundary case, and a misuse/invalid case when relevant. For each case, record the '
                       'actual result and compare it with the requirement. A correct submission must preserve the '
                       'lesson rule and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Package Managers & Third-Party Libraries: What does a package manager help manage?',
                        ['External dependencies and versions', 'Only loops', 'Only variables', 'Only comments'],
                        0,
                        'Package managers help acquire and integrate dependencies.'],
                      [ 'Why pin or constrain dependency versions?',
                        [ 'To make builds more reproducible',
                          'To avoid compilation',
                          'To remove APIs',
                          'To make code global'],
                        0,
                        'Version constraints reduce unexpected dependency changes.'],
                      [ 'What is linking?',
                        [ 'Connecting compiled code with required libraries',
                          'Reading input',
                          'Sorting a vector',
                          'Running a debugger'],
                        0,
                        'Linking resolves symbols across object files and libraries.'],
                      [ 'Why check a library license?',
                        [ 'Projects have legal obligations when distributing software',
                          'It changes integer sizes',
                          'It prevents exceptions',
                          'It creates namespaces'],
                        0,
                        'Licensing affects how dependencies can be used and distributed.'],
                      [ 'What is a dependency boundary?',
                        [ 'A deliberate interface between your code and an external component',
                          'A loop condition',
                          'A variable scope only',
                          'A compiler error'],
                        0,
                        'Boundaries reduce coupling and clarify integration points.']],
    'summary': 'You should now be able to explain package managers & third-party libraries, recognize its syntax, '
               'trace the worked example, and use the concept in a small original program.',
    'next_lesson': 'C++ Ecosystem & Engineering Practices',
    'rules': [ 'Name and trace the role of each dependency before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the package managers & '
            'third-party libraries exercise.',
    'extension': 'Add one realistic requirement to the package managers & third-party libraries exercise while keeping '
                 'the original behavior correct.',
    'learning_checks': [ 'Can I explain package managers & third-party libraries without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_54'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Package Managers & Third-Party Libraries gives you the foundation needed to read, change, and '
                      'reason about a program before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Package Managers & Third-Party Libraries** in one sentence before '
                         'writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Package Managers & '
                         'Third-Party Libraries**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Package Managers & Third-Party Libraries** task: Describe the '
                            'steps needed to add one external library to a C++ project without committing the library '
                            'source into your repository. Then create one small variation that changes an input, rule, '
                            'or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Package Managers & Third-Party Libraries** program that exhibits this '
                  'common mistake: **Memorizing dependency syntax without being able to explain what changes in the '
                  'program.**. Before changing code, identify the first incorrect value, state, control-flow decision, '
                  'or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Package Managers & Third-Party Libraries** to a small real-world feature. Keep the '
                     'same core rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what package managers & third-party libraries means and why '
                                                 'it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for package managers & '
                                                 'third-party libraries.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small package managers & third-party '
                                                 'libraries example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Package Managers & Third-Party '
                                  'Libraries.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Package Managers & Third-Party Libraries '
                                  'without violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Package '
                                  'Managers & Third-Party Libraries.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_56',
    'title': 'C++ Ecosystem & Engineering Practices',
    'description': 'Connect language knowledge to real development: standard libraries, testing libraries, logging, '
                   'formatting, profiling, documentation, licensing, and maintainable project workflows.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **C++ Ecosystem & Engineering Practices**, understand why it is '
                    'useful, trace a focused example, practice it with guidance, then solve an independent variation. '
                    'You will finish by proving your understanding through concept, syntax, code-reading, debugging, '
                    'and application checks.',
    'learning_objectives': [ 'Explain what c++ ecosystem & engineering practices means and why it exists.',
                             'Read and write the core syntax used for c++ ecosystem & engineering practices.',
                             'Predict the behavior of a small c++ ecosystem & engineering practices example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['logging', 'testing', 'profiling', 'dependency'],
    'explanation': 'Connect language knowledge to real development: standard libraries, testing libraries, logging, '
                   'formatting, profiling, documentation, licensing, and maintainable project workflows. C++ syntax is '
                   'shown with the standard library names used in this lesson. Read the declaration from left to '
                   'right: identify the type or template, the name, the operation, and the terminating punctuation.',
    'syntax': '// A maintainable application separates\n// domain logic, I/O, tests, and configuration.',
    'syntax_breakdown': [ 'Focus on logging: identify what it represents and what role it plays in the statement.',
                          'Next inspect testing: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '// A maintainable application separates\n// domain logic, I/O, tests, and configuration.',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': '// app/\n'
                '//   domain/   services/   io/   tests/\n'
                '// Keep business logic independent from console I/O.',
    'example2_explanation': 'Change one meaningful input or rule related to c++ ecosystem & engineering practices, '
                            'predict the result, and only then run the program.',
    'practical_example': 'Imagine a small c++ ecosystem & engineering practices feature in a student or inventory '
                         'program. Decide what data enters the feature, what rule the feature applies, and what result '
                         'it should produce.',
    'common_mistakes': [ 'Memorizing logging syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make logging behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each logging before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Design a folder structure and engineering checklist for a small production-style C++ application.',
    'practice_problem': '**C++ Ecosystem & Engineering Practices independent practice:** Design a folder structure and '
                        'engineering checklist for a small production-style C++ application. You must also add one '
                        "clearly different variation and test it. Your work should demonstrate the lesson's main rule, "
                        'not merely reproduce Example 1.',
    'expected_output': '**Test contract for C++ Ecosystem & Engineering Practices:** Run the program with a normal '
                       'case, a boundary case, and a misuse/invalid case when relevant. For each case, record the '
                       'actual result and compare it with the requirement. A correct submission must preserve the '
                       'lesson rule and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'C++ Ecosystem & Engineering Practices: Which statement best describes C++ Ecosystem & '
                        'Engineering Practices?',
                        [ 'It is a core part of C++ Ecosystem & Engineering Practices',
                          'It is only a compiler warning',
                          'It is unrelated to programming',
                          'It replaces all data types'],
                        0,
                        'This lesson focuses on the role and correct use of C++ Ecosystem & Engineering Practices.'],
                      [ 'What should a learner be able to do after C++ Ecosystem & Engineering Practices?',
                        [ 'Use the concept in a small program',
                          'Only memorize its name',
                          'Avoid testing it',
                          'Copy one example unchanged'],
                        0,
                        'Application is the goal, not memorization.'],
                      [ 'Which test is most useful for C++ Ecosystem & Engineering Practices?',
                        [ 'A normal case plus an important edge case',
                          'No input',
                          'Only a huge random case',
                          'Only comments'],
                        0,
                        'Testing the concept in more than one case reveals misunderstandings.'],
                      [ 'Which mistake should be avoided with C++ Ecosystem & Engineering Practices?',
                        [ 'Using syntax without understanding its behavior',
                          'Writing a small test',
                          'Reading diagnostics',
                          'Choosing clear names'],
                        0,
                        'Understanding behavior matters more than copying syntax.'],
                      [ 'How should C++ Ecosystem & Engineering Practices fit into a larger program?',
                        [ 'As one focused tool combined with earlier concepts',
                          'As a replacement for every other feature',
                          'As global state everywhere',
                          'As code that never needs testing'],
                        0,
                        'Programming features are combined according to the problem.']],
    'summary': 'You should now be able to explain c++ ecosystem & engineering practices, recognize its syntax, trace '
               'the worked example, and use the concept in a small original program.',
    'next_lesson': 'Operator Overloading',
    'rules': [ 'Name and trace the role of each logging before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the c++ ecosystem & '
            'engineering practices exercise.',
    'extension': 'Add one realistic requirement to the c++ ecosystem & engineering practices exercise while keeping '
                 'the original behavior correct.',
    'learning_checks': [ 'Can I explain c++ ecosystem & engineering practices without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_55'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'C++ Ecosystem & Engineering Practices matters because real projects require requirements, '
                      'design decisions, testing, maintainability, and trade-off awareness.',
    'guided_practice': [ '1. Restate the goal of **C++ Ecosystem & Engineering Practices** in one sentence before '
                         'writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **C++ Ecosystem & '
                         'Engineering Practices**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **C++ Ecosystem & Engineering Practices** task: Design a folder '
                            'structure and engineering checklist for a small production-style C++ application. Then '
                            'create one small variation that changes an input, rule, or data case without changing the '
                            'main goal.',
    'debug_task': 'Debug a deliberately small **C++ Ecosystem & Engineering Practices** program that exhibits this '
                  'common mistake: **Memorizing logging syntax without being able to explain what changes in the '
                  'program.**. Before changing code, identify the first incorrect value, state, control-flow decision, '
                  'or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **C++ Ecosystem & Engineering Practices** to a small real-world feature. Keep the same '
                     'core rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what c++ ecosystem & engineering practices means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for c++ ecosystem & engineering '
                                                 'practices.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small c++ ecosystem & engineering '
                                                 'practices example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for C++ Ecosystem & Engineering '
                                  'Practices.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for C++ Ecosystem & Engineering Practices without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in C++ Ecosystem '
                                  '& Engineering Practices.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['engineering', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_57',
    'title': 'Operator Overloading',
    'description': 'Define natural operator behavior for user-defined types, including unary, binary, comparison, and '
                   'stream operators, while keeping overloads predictable.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Operator Overloading**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what operator overloading means and why it exists.',
                             'Read and write the core syntax used for operator overloading.',
                             'Predict the behavior of a small operator overloading example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['Operator Overloading', 'syntax', 'behavior', 'use case'],
    'explanation': 'Define natural operator behavior for user-defined types, including unary, binary, comparison, and '
                   'stream operators, while keeping overloads predictable. C++ syntax is shown with the standard '
                   'library names used in this lesson. Read the declaration from left to right: identify the type or '
                   'template, the name, the operation, and the terminating punctuation.',
    'syntax': 'struct Point {\n'
              '    int x, y;\n'
              '};\n'
              'Point operator+(const Point& a, const Point& b) { return {a.x+b.x, a.y+b.y}; }',
    'syntax_breakdown': [ 'Focus on Operator Overloading: identify what it represents and what role it plays in the '
                          'statement.',
                          'Next inspect syntax: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'struct Point {\n'
                '    int x, y;\n'
                '};\n'
                'Point operator+(const Point& a, const Point& b) { return {a.x+b.x, a.y+b.y}; }',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': 'int a = 8, b = 3;\n'
                'cout << (a / b) << " " << (a % b) << "\\n";\n'
                'cout << ((a > b) ? "larger" : "smaller");',
    'example2_explanation': 'Change one meaningful input or rule related to operator overloading, predict the result, '
                            'and only then run the program.',
    'practical_example': 'Imagine a small operator overloading feature in a student or inventory program. Decide what '
                         'data enters the feature, what rule the feature applies, and what result it should produce.',
    'common_mistakes': [ 'Memorizing Operator Overloading syntax without being able to explain what changes in the '
                         'program.',
                         'Ignoring the boundary or lifetime rules that make Operator Overloading behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each Operator Overloading before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Create a small Money or Point type with one meaningful binary operator and one comparison operator.',
    'practice_problem': '**Operator Overloading independent practice:** Create a small Money or Point type with one '
                        'meaningful binary operator and one comparison operator. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Operator Overloading:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'Operator Overloading: What does operator overloading allow?',
                        [ 'A type to define meaningful behavior for an operator',
                          'Changing compiler syntax globally',
                          'Creating threads',
                          'Reading files'],
                        0,
                        'Overloaded operators provide type-specific semantics.'],
                      [ 'When is operator overloading appropriate?',
                        [ 'When the operation is natural and unsurprising for the type',
                          'For every method',
                          'To hide unrelated behavior',
                          'To avoid names'],
                        0,
                        'Good overloads match intuitive type semantics.'],
                      [ 'Why overload << for a type?',
                        [ 'To integrate with stream output naturally',
                          'To create a pointer',
                          'To sort automatically',
                          'To allocate memory'],
                        0,
                        'Stream insertion can make output of user types convenient.'],
                      [ 'What is a unary operator?',
                        [ 'An operator that works on one operand',
                          'An operator with two classes',
                          'A file operation',
                          'A loop'],
                        0,
                        'Unary operators take one operand.'],
                      [ 'What should an overloaded operator preserve?',
                        ['Clear, predictable semantics', 'Random side effects', 'Hidden I/O always', 'Global state'],
                        0,
                        'Operator syntax should remain understandable.']],
    'summary': 'You should now be able to explain operator overloading, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Threads & Concurrency Basics',
    'rules': [ 'Name and trace the role of each Operator Overloading before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the operator '
            'overloading exercise.',
    'extension': 'Add one realistic requirement to the operator overloading exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain operator overloading without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_56'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Operator Overloading gives you the foundation needed to read, change, and reason about a '
                      'program before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Operator Overloading** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Operator '
                         'Overloading**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Operator Overloading** task: Create a small Money or Point '
                            'type with one meaningful binary operator and one comparison operator. Then create one '
                            'small variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Operator Overloading** program that exhibits this common mistake: '
                  '**Memorizing Operator Overloading syntax without being able to explain what changes in the '
                  'program.**. Before changing code, identify the first incorrect value, state, control-flow decision, '
                  'or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Operator Overloading** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what operator overloading means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for operator overloading.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small operator overloading example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Operator Overloading.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Operator Overloading without violating the '
                                  'stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Operator '
                                  'Overloading.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'cpp_58',
    'title': 'Threads & Concurrency Basics',
    'description': 'Understand std::thread, joining, mutexes, lock_guard, race conditions, and the difference between '
                   'concurrency and parallelism.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Threads & Concurrency Basics**, understand why it is useful, '
                    'trace a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what threads & concurrency basics means and why it exists.',
                             'Read and write the core syntax used for threads & concurrency basics.',
                             'Predict the behavior of a small threads & concurrency basics example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['thread', 'Runnable', 'shared state', 'race condition'],
    'explanation': 'Understand std::thread, joining, mutexes, lock_guard, race conditions, and the difference between '
                   'concurrency and parallelism. C++ syntax is shown with the standard library names used in this '
                   'lesson. Read the declaration from left to right: identify the type or template, the name, the '
                   'operation, and the terminating punctuation.',
    'syntax': '#include <thread>\n'
              '#include <mutex>\n'
              '\n'
              'std::mutex m;\n'
              'int counter = 0;\n'
              'void work() { std::lock_guard<std::mutex> lock(m); ++counter; }',
    'syntax_breakdown': [ 'Focus on thread: identify what it represents and what role it plays in the statement.',
                          'Next inspect Runnable: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '#include <thread>\n'
                '#include <mutex>\n'
                '\n'
                'std::mutex m;\n'
                'int counter = 0;\n'
                'void work() { std::lock_guard<std::mutex> lock(m); ++counter; }',
    'example1_explanation': 'The example is intentionally small so you can trace state changes before combining it '
                            'with larger programs.',
    'example2': '// Focused Threads & Concurrency Basics example\ncout << "Practice the lesson concept";',
    'example2_explanation': 'Change one meaningful input or rule related to threads & concurrency basics, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small threads & concurrency basics feature in a student or inventory program. '
                         'Decide what data enters the feature, what rule the feature applies, and what result it '
                         'should produce.',
    'common_mistakes': [ 'Memorizing thread syntax without being able to explain what changes in the program.',
                         'Ignoring the boundary or lifetime rules that make thread behave correctly.',
                         'Changing several lines at once when debugging instead of isolating the first incorrect '
                         'state.'],
    'beginner_tips': [ 'Name and trace the role of each thread before adding more code.',
                       'Test the smallest valid case first, then a normal case, then a boundary case.',
                       'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'exercise': 'Create two worker threads that safely update shared state and explain why the mutex is required.',
    'practice_problem': '**Threads & Concurrency Basics independent practice:** Create two worker threads that safely '
                        'update shared state and explain why the mutex is required. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Threads & Concurrency Basics:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Threads & Concurrency Basics: What is a race condition?',
                        [ 'A result that depends on unsafe timing between concurrent operations',
                          'A syntax error',
                          'A file path',
                          'A sorting rule'],
                        0,
                        'Races occur when shared state is accessed without sufficient coordination.'],
                      [ 'Why use a lock or synchronized section?',
                        [ 'To protect critical shared state',
                          'To make all code asynchronous',
                          'To remove objects',
                          'To skip tests'],
                        0,
                        'Synchronization coordinates access to shared mutable state.'],
                      [ 'What does an executor manage?',
                        ['Task execution and worker resources', 'Only strings', 'Only files', 'Only database schemas'],
                        0,
                        'Executor services manage submitted tasks and worker threads.'],
                      [ 'What is an atomic increment?',
                        [ 'An increment operation designed to be indivisible with respect to competing threads',
                          'A loop that runs once',
                          'A compiler flag',
                          'A file append'],
                        0,
                        'Atomic operations provide safe single-step updates to shared variables.'],
                      [ 'Why can a thread-safe individual operation still be insufficient?',
                        [ 'A multi-step sequence may need to be atomic as a whole',
                          'Threads cannot share memory',
                          'Locks never work',
                          'The compiler changes languages'],
                        0,
                        'Correctness can depend on the entire sequence, not just each individual operation.']],
    'summary': 'You should now be able to explain threads & concurrency basics, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Capstone project / practical assessment',
    'rules': [ 'Name and trace the role of each thread before adding more code.',
               'Test the smallest valid case first, then a normal case, then a boundary case.',
               'Prefer the standard-library or language feature that directly expresses the requirement.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the threads & '
            'concurrency basics exercise.',
    'extension': 'Add one realistic requirement to the threads & concurrency basics exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain threads & concurrency basics without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['cpp_57'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Threads & Concurrency Basics matters because concurrent programs must coordinate work without '
                      'corrupting shared state or hiding failures.',
    'guided_practice': [ '1. Restate the goal of **Threads & Concurrency Basics** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Threads & '
                         'Concurrency Basics**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Threads & Concurrency Basics** task: Create two worker threads '
                            'that safely update shared state and explain why the mutex is required. Then create one '
                            'small variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Threads & Concurrency Basics** program that exhibits this common '
                  'mistake: **Memorizing thread syntax without being able to explain what changes in the program.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Threads & Concurrency Basics** to a small real-world feature. Keep the same core '
                     'rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what threads & concurrency basics means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for threads & concurrency '
                                                 'basics.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small threads & concurrency basics '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Threads & Concurrency Basics.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Threads & Concurrency Basics without violating '
                                  'the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Threads & '
                                  'Concurrency Basics.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['concurrency', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'}]

from bot.learning.quality import enrich_curriculum
enrich_curriculum(CPP_CURRICULUM, "cpp")
