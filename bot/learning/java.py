from __future__ import annotations

JAVA_CURRICULUM = [ { 'id': 'java_01',
    'title': 'Programming Fundamentals',
    'description': 'Understand how Java source code is compiled to bytecode and executed by the JVM, and how classes '
                   'and main() form a basic program.',
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
    'explanation': 'Understand how Java source code is compiled to bytecode and executed by the JVM, and how classes '
                   'and main() form a basic program. Java syntax is shown using the standard library or language '
                   'feature for this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'public class Main {\n'
              '    public static void main(String[] args) {\n'
              '        System.out.println("Hello, ClassCode!");\n'
              '    }\n'
              '}',
    'syntax_breakdown': [ 'Focus on source file: identify what it represents and what role it plays in the statement.',
                          'Next inspect compiler: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'public class Main {\n'
                '    public static void main(String[] args) {\n'
                '        System.out.println("Hello, ClassCode!");\n'
                '    }\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'public class Main {\n'
                '    public static void main(String[] args) {\n'
                '        System.out.println("Name: Ren");\n'
                '        System.out.println("Goal: Learn Java");\n'
                '    }\n'
                '}',
    'example2_explanation': 'Change one meaningful input or rule related to programming fundamentals, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small programming fundamentals feature in a student or inventory application. '
                         'Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using source file without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls compiler.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of source file in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Write a program that prints your name, school, and one programming goal on separate lines.',
    'practice_problem': '**Programming Fundamentals independent practice:** Write a program that prints your name, '
                        'school, and one programming goal on separate lines. You must also add one clearly different '
                        "variation and test it. Your work should demonstrate the lesson's main rule, not merely "
                        'reproduce Example 1.',
    'expected_output': '**Test contract for Programming Fundamentals:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'Programming Fundamentals: What is the normal Java entry point?',
                        ['public static void main(String[] args)', 'start()', 'run()', 'begin()'],
                        0,
                        'The JVM uses the main method with this signature as the conventional entry point.'],
                      [ 'What does javac produce from Java source?',
                        ['Bytecode class files', 'A native C++ executable', 'A database table', 'A PDF'],
                        0,
                        'javac compiles source into JVM bytecode.'],
                      [ 'Which statement prints a line in Java?',
                        ['System.out.println()', 'console.write()', 'print.line()', 'System.input()'],
                        0,
                        'println writes text followed by a line terminator.'],
                      [ 'What does a syntax error mean?',
                        [ 'The source violates language grammar',
                          'The output is ugly',
                          'The program is always slow',
                          'The network is offline'],
                        0,
                        'Syntax errors prevent the source from being parsed correctly.'],
                      [ 'Which component executes Java bytecode?',
                        ['The JVM', 'The Scanner', 'ArrayList', 'The compiler only'],
                        0,
                        'The Java Virtual Machine executes bytecode.']],
    'summary': 'You should now be able to explain programming fundamentals, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Variables & Primitive Types',
    'rules': [ 'Explain the job of source file in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
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
                  '**Using source file without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
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
  { 'id': 'java_02',
    'title': 'Variables & Primitive Types',
    'description': "Learn Java's eight primitive types, reference types, declarations, initialization, and the "
                   'difference between storing a value and referring to an object.',
    'stage': 'Foundation',
    'difficulty': 'Beginner',
    'introduction': 'In this lesson you will learn **Variables & Primitive Types**, understand why it is useful, trace '
                    'a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what variables & primitive types means and why it exists.',
                             'Read and write the core syntax used for variables & primitive types.',
                             'Predict the behavior of a small variables & primitive types example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['declaration', 'initialization', 'primitive', 'reference'],
    'explanation': "Learn Java's eight primitive types, reference types, declarations, initialization, and the "
                   'difference between storing a value and referring to an object. Java syntax is shown using the '
                   'standard library or language feature for this lesson. Pay attention to the type, identifier, '
                   'method call, object reference, and punctuation.',
    'syntax': 'int age = 18;\n'
              'double average = 91.5;\n'
              'char grade = (char)65;\n'
              'boolean enrolled = true;\n'
              'String name = "Alex";',
    'syntax_breakdown': [ 'Focus on declaration: identify what it represents and what role it plays in the statement.',
                          'Next inspect initialization: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'public class Main {\n'
                '    public static void main(String[] args) {\n'
                '        int age = 18;\n'
                '        double average = 91.5;\n'
                '        char grade = (char)65;\n'
                '        boolean enrolled = true;\n'
                '        String name = "Alex";\n'
                '        System.out.println(name + " " + age + " " + average + " " + grade + " " + enrolled);\n'
                '    }\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': "byte ageGroup = 18;\nlong population = 8000000L;\nfloat ratio = 0.5f;\nchar grade = 'A';",
    'example2_explanation': 'Change one meaningful input or rule related to variables & primitive types, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small variables & primitive types feature in a student or inventory application. '
                         'Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using declaration without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls initialization.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of declaration in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Create a student profile using an appropriate type for each value and print it.',
    'practice_problem': '**Variables & Primitive Types independent practice:** Create a student profile using an '
                        'appropriate type for each value and print it. You must also add one clearly different '
                        "variation and test it. Your work should demonstrate the lesson's main rule, not merely "
                        'reproduce Example 1.',
    'expected_output': '**Test contract for Variables & Primitive Types:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Variables & Primitive Types: Which is a Java primitive type?',
                        ['int', 'String', 'ArrayList<Integer>', 'Scanner'],
                        0,
                        'int is primitive; String, ArrayList, and Scanner are reference types.'],
                      [ 'What is the usual type for true/false?',
                        ['boolean', 'bool', 'BooleanType', 'bit'],
                        0,
                        'Java uses boolean for true/false values.'],
                      [ 'Which type commonly stores a 64-bit integer?',
                        ['long', 'short', 'byte', 'char'],
                        0,
                        'long is Java’s larger integral primitive among these choices.'],
                      [ 'What does (int) 9.8 do?',
                        [ 'Converts it to an int, yielding 9',
                          'Rounds to 10',
                          'Turns it into a String',
                          'Throws automatically'],
                        0,
                        'Casting to int removes the fractional part.'],
                      [ 'Which is a reference type?',
                        ['String', 'int', 'double', 'boolean'],
                        0,
                        'String is a class/reference type.']],
    'summary': 'You should now be able to explain variables & primitive types, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Scanner Input & Output',
    'rules': [ 'Explain the job of declaration in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the variables & '
            'primitive types exercise.',
    'extension': 'Add one realistic requirement to the variables & primitive types exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain variables & primitive types without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_01'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Variables & Primitive Types gives you the foundation needed to read, change, and reason about a '
                      'program before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Variables & Primitive Types** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Variables & '
                         'Primitive Types**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Variables & Primitive Types** task: Create a student profile '
                            'using an appropriate type for each value and print it. Then create one small variation '
                            'that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Variables & Primitive Types** program that exhibits this common '
                  'mistake: **Using declaration without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Variables & Primitive Types** to a small real-world feature. Keep the same core rule, '
                     'but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what variables & primitive types means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for variables & primitive types.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small variables & primitive types example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Variables & Primitive Types.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Variables & Primitive Types without violating '
                                  'the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Variables & '
                                  'Primitive Types.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_03',
    'title': 'Scanner Input & Output',
    'description': 'Read console input with Scanner and produce clear output with print and println, including the '
                   'common nextInt()/nextLine() transition problem.',
    'stage': 'Foundation',
    'difficulty': 'Beginner',
    'introduction': 'In this lesson you will learn **Scanner Input & Output**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what scanner input & output means and why it exists.',
                             'Read and write the core syntax used for scanner input & output.',
                             'Predict the behavior of a small scanner input & output example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['Scanner', 'token', 'nextLine', 'System.out'],
    'explanation': 'Read console input with Scanner and produce clear output with print and println, including the '
                   'common nextInt()/nextLine() transition problem. Java syntax is shown using the standard library or '
                   'language feature for this lesson. Pay attention to the type, identifier, method call, object '
                   'reference, and punctuation.',
    'syntax': 'Scanner scanner = new Scanner(System.in);\n'
              'int age = scanner.nextInt();\n'
              'scanner.nextLine();\n'
              'String name = scanner.nextLine();\n'
              'System.out.println(name + " is " + age);',
    'syntax_breakdown': [ 'Focus on Scanner: identify what it represents and what role it plays in the statement.',
                          'Next inspect token: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'import java.util.Scanner;\n'
                '\n'
                'public class Main {\n'
                '    public static void main(String[] args) {\n'
                '        Scanner scanner = new Scanner(System.in);\n'
                '        int age = scanner.nextInt();\n'
                '        scanner.nextLine();\n'
                '        String name = scanner.nextLine();\n'
                '        System.out.println(name + " is " + age + " years old");\n'
                '    }\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'Scanner scanner = new Scanner(System.in);\n'
                'System.out.print("Name: ");\n'
                'String name = scanner.nextLine();\n'
                'System.out.println("Welcome, " + name);',
    'example2_explanation': 'Change one meaningful input or rule related to scanner input & output, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small scanner input & output feature in a student or inventory application. '
                         'Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using Scanner without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls token.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of Scanner in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Ask for a name, age, and favorite number, then display a formatted summary.',
    'practice_problem': '**Scanner Input & Output independent practice:** Ask for a name, age, and favorite number, '
                        'then display a formatted summary. You must also add one clearly different variation and test '
                        "it. Your work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Scanner Input & Output:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'Scanner Input & Output: Which Scanner method reads an int?',
                        ['nextInt()', 'nextInteger()', 'readIntLine()', 'getInt()'],
                        0,
                        'Scanner provides nextInt() for integer tokens.'],
                      [ 'Which Scanner method reads a complete line?',
                        ['nextLine()', 'nextText()', 'readLineOnly()', 'line()'],
                        0,
                        'nextLine() consumes the current line.'],
                      [ 'What can happen after nextInt() followed immediately by nextLine()?',
                        [ 'nextLine() can consume the leftover newline',
                          'The int becomes a double',
                          'Scanner changes type',
                          'The JVM stops'],
                        0,
                        'The newline remaining after token input is a classic Scanner issue.'],
                      [ 'Which call prints without automatically moving to a new line?',
                        ['System.out.print()', 'System.out.println()', 'System.in.print()', 'Scanner.print()'],
                        0,
                        'print writes without appending a line terminator.'],
                      [ 'Why should a Scanner be created from System.in?',
                        [ 'System.in is the standard input stream',
                          'It is the JVM heap',
                          'It is the output stream',
                          'It is a package'],
                        0,
                        'System.in represents standard input.']],
    'summary': 'You should now be able to explain scanner input & output, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Operators & Expressions',
    'rules': [ 'Explain the job of Scanner in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the scanner input & '
            'output exercise.',
    'extension': 'Add one realistic requirement to the scanner input & output exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain scanner input & output without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_02'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Scanner Input & Output matters because programs need a reliable way to receive and present data '
                      'instead of relying on hard-coded values.',
    'guided_practice': [ '1. Restate the goal of **Scanner Input & Output** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Scanner Input & '
                         'Output**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Scanner Input & Output** task: Ask for a name, age, and '
                            'favorite number, then display a formatted summary. Then create one small variation that '
                            'changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Scanner Input & Output** program that exhibits this common mistake: '
                  '**Using Scanner without understanding whether it represents data, behavior, or a relationship.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Scanner Input & Output** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what scanner input & output means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for scanner input & output.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small scanner input & output example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Scanner Input & Output.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Scanner Input & Output without violating the '
                                  'stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['input', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_04',
    'title': 'Operators & Expressions',
    'description': 'Use arithmetic, comparison, logical, assignment, increment, decrement, ternary, bitwise, and shift '
                   "operators while respecting Java's precedence rules.",
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
    'explanation': 'Use arithmetic, comparison, logical, assignment, increment, decrement, ternary, bitwise, and shift '
                   "operators while respecting Java's precedence rules. Java syntax is shown using the standard "
                   'library or language feature for this lesson. Pay attention to the type, identifier, method call, '
                   'object reference, and punctuation.',
    'syntax': 'int a = 17, b = 5;\nint remainder = a % b;\nb += 3;\nboolean ready = (a > b) && (a < 30);',
    'syntax_breakdown': [ 'Focus on operand: identify what it represents and what role it plays in the statement.',
                          'Next inspect operator: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'public class Main {\n'
                '    public static void main(String[] args) {\n'
                '        int a = 17, b = 5;\n'
                '        int remainder = a % b;\n'
                '        b += 3;\n'
                '        boolean ready = (a > b) && (a < 30);\n'
                '        System.out.println(remainder + " " + b + " " + ready);\n'
                '    }\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'int a=8,b=3;\nSystem.out.println(a/b + " " + a%b);\nSystem.out.println(a>b ? "larger" : "smaller");',
    'example2_explanation': 'Change one meaningful input or rule related to operators & expressions, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small operators & expressions feature in a student or inventory application. '
                         'Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using operand without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls operator.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of operand in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Build a bill calculator that computes subtotal, tax, discount, and final total.',
    'practice_problem': '**Operators & Expressions independent practice:** Build a bill calculator that computes '
                        'subtotal, tax, discount, and final total. You must also add one clearly different variation '
                        "and test it. Your work should demonstrate the lesson's main rule, not merely reproduce "
                        'Example 1.',
    'expected_output': '**Test contract for Operators & Expressions:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'Operators & Expressions: What does % produce for integer operands?',
                        ['The remainder', 'The quotient only', 'A Boolean', 'A string'],
                        0,
                        'Modulo gives the remainder.'],
                      [ 'Which operator checks equality of primitive values?',
                        ['==', '=', '===', 'equals'],
                        0,
                        'Java uses == for primitive value comparison.'],
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
    'rules': [ 'Explain the job of operand in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the operators & '
            'expressions exercise.',
    'extension': 'Add one realistic requirement to the operators & expressions exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain operators & expressions without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_03'],
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
                            'computes subtotal, tax, discount, and final total. Then create one small variation that '
                            'changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Operators & Expressions** program that exhibits this common mistake: '
                  '**Using operand without understanding whether it represents data, behavior, or a relationship.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
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
  { 'id': 'java_05',
    'title': 'If / Else Decisions',
    'description': 'Translate rules into if, else if, and else branches and test boundaries deliberately.',
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
    'explanation': 'Translate rules into if, else if, and else branches and test boundaries deliberately. Java syntax '
                   'is shown using the standard library or language feature for this lesson. Pay attention to the '
                   'type, identifier, method call, object reference, and punctuation.',
    'syntax': 'int score = 82;\n'
              'if (score < 0 || score > 100) System.out.println("INVALID");\n'
              'else if (score >= 75) System.out.println("PASS");\n'
              'else System.out.println("FAIL");',
    'syntax_breakdown': [ 'Focus on condition: identify what it represents and what role it plays in the statement.',
                          'Next inspect branch: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'public class Main {\n'
                '    public static void main(String[] args) {\n'
                '        int score = 82;\n'
                '        if (score < 0 || score > 100) System.out.println("INVALID");\n'
                '        else if (score >= 75) System.out.println("PASS");\n'
                '        else System.out.println("FAIL");\n'
                '    }\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'int temperature = 27;\n'
                'if (temperature >= 30) System.out.println("hot");\n'
                'else if (temperature >= 20) System.out.println("warm");\n'
                'else System.out.println("cool");',
    'example2_explanation': 'Change one meaningful input or rule related to if / else decisions, predict the result, '
                            'and only then run the program.',
    'practical_example': 'Imagine a small if / else decisions feature in a student or inventory application. Identify '
                         'the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using condition without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls branch.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of condition in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Read a score and classify it as INVALID, FAIL, PASS, or distinction.',
    'practice_problem': '**If / Else Decisions independent practice:** Read a score and classify it as INVALID, FAIL, '
                        'PASS, or distinction. You must also add one clearly different variation and test it. Your '
                        "work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
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
    'rules': [ 'Explain the job of condition in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the if / else decisions '
            'exercise.',
    'extension': 'Add one realistic requirement to the if / else decisions exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain if / else decisions without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_04'],
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
                            'INVALID, FAIL, PASS, or distinction. Then create one small variation that changes an '
                            'input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **If / Else Decisions** program that exhibits this common mistake: '
                  '**Using condition without understanding whether it represents data, behavior, or a relationship.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
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
  { 'id': 'java_06',
    'title': 'Switch Statements',
    'description': 'Use switch for discrete choices and understand case labels, break, default, and modern switch '
                   'expressions at a conceptual level.',
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
    'explanation': 'Use switch for discrete choices and understand case labels, break, default, and modern switch '
                   'expressions at a conceptual level. Java syntax is shown using the standard library or language '
                   'feature for this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'int choice = 2;\n'
              'switch (choice) {\n'
              '    case 1 -> System.out.println("Add");\n'
              '    case 2 -> System.out.println("View");\n'
              '    default -> System.out.println("Invalid");\n'
              '}',
    'syntax_breakdown': [ 'Focus on case: identify what it represents and what role it plays in the statement.',
                          'Next inspect break: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'public class Main {\n'
                '    public static void main(String[] args) {\n'
                '        int choice = 2;\n'
                '        switch (choice) {\n'
                '            case 1 -> System.out.println("Add");\n'
                '            case 2 -> System.out.println("View");\n'
                '            default -> System.out.println("Invalid");\n'
                '        }\n'
                '    }\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': "char option = 'A';\n"
                'switch (option) {\n'
                '    case \'A\' -> System.out.println("Add");\n'
                '    case \'Q\' -> System.out.println("Quit");\n'
                '    default -> System.out.println("Unknown");\n'
                '}',
    'example2_explanation': 'Change one meaningful input or rule related to switch statements, predict the result, and '
                            'only then run the program.',
    'practical_example': 'Imagine a small switch statements feature in a student or inventory application. Identify '
                         'the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using case without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls break.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of case in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Create a four-option menu and handle invalid choices.',
    'practice_problem': '**Switch Statements independent practice:** Create a four-option menu and handle invalid '
                        'choices. You must also add one clearly different variation and test it. Your work should '
                        "demonstrate the lesson's main rule, not merely reproduce Example 1.",
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
    'next_lesson': 'Loops',
    'rules': [ 'Explain the job of case in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the switch statements '
            'exercise.',
    'extension': 'Add one realistic requirement to the switch statements exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain switch statements without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_05'],
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
    'independent_practice': 'Independently solve this **Switch Statements** task: Create a four-option menu and handle '
                            'invalid choices. Then create one small variation that changes an input, rule, or data '
                            'case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Switch Statements** program that exhibits this common mistake: **Using '
                  'case without understanding whether it represents data, behavior, or a relationship.**. Before '
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
  { 'id': 'java_07',
    'title': 'Loops',
    'description': 'Repeat work with for, while, do-while, enhanced for, break, and continue, while checking '
                   'termination conditions.',
    'stage': 'Foundation',
    'difficulty': 'Beginner',
    'introduction': 'In this lesson you will learn **Loops**, understand why it is useful, trace a focused example, '
                    'practice it with guidance, then solve an independent variation. You will finish by proving your '
                    'understanding through concept, syntax, code-reading, debugging, and application checks.',
    'learning_objectives': [ 'Explain what loops means and why it exists.',
                             'Read and write the core syntax used for loops.',
                             'Predict the behavior of a small loops example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['iteration', 'condition', 'counter', 'termination'],
    'explanation': 'Repeat work with for, while, do-while, enhanced for, break, and continue, while checking '
                   'termination conditions. Java syntax is shown using the standard library or language feature for '
                   'this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'for (int i = 1; i <= 5; i++) {\n    System.out.print(i + " ");\n}',
    'syntax_breakdown': [ 'Focus on iteration: identify what it represents and what role it plays in the statement.',
                          'Next inspect condition: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'public class Main {\n'
                '    public static void main(String[] args) {\n'
                '        for (int i = 1; i <= 5; i++) System.out.print(i + " ");\n'
                '    }\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'int i=5;\nwhile(i>0){\n    System.out.print(i + " ");\n    i--;\n}',
    'example2_explanation': 'Change one meaningful input or rule related to loops, predict the result, and only then '
                            'run the program.',
    'practical_example': 'Imagine a small loops feature in a student or inventory application. Identify the '
                         'input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using iteration without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls condition.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of iteration in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Read N, print 1 through N, and calculate the sum.',
    'practice_problem': '**Loops independent practice:** Read N, print 1 through N, and calculate the sum. You must '
                        'also add one clearly different variation and test it. Your work should demonstrate the '
                        "lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Loops:** Run the program with a normal case, a boundary case, and a '
                       'misuse/invalid case when relevant. For each case, record the actual result and compare it with '
                       'the requirement. A correct submission must preserve the lesson rule and handle the defined '
                       'edge case safely.',
    'mastery_quiz': [ [ 'Loops: What are the three common parts of a for loop?',
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
    'summary': 'You should now be able to explain loops, recognize its syntax, trace the worked example, and use the '
               'concept in a small original program.',
    'next_lesson': 'Nested Loops & Patterns',
    'rules': [ 'Explain the job of iteration in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the loops exercise.',
    'extension': 'Add one realistic requirement to the loops exercise while keeping the original behavior correct.',
    'learning_checks': [ 'Can I explain loops without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_06'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Loops matters because repeated work should be expressed once and controlled by clear stopping '
                      'conditions.',
    'guided_practice': [ '1. Restate the goal of **Loops** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Loops**, then '
                         'change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Loops** task: Read N, print 1 through N, and calculate the '
                            'sum. Then create one small variation that changes an input, rule, or data case without '
                            'changing the main goal.',
    'debug_task': 'Debug a deliberately small **Loops** program that exhibits this common mistake: **Using iteration '
                  'without understanding whether it represents data, behavior, or a relationship.**. Before changing '
                  'code, identify the first incorrect value, state, control-flow decision, or ownership assumption; '
                  'then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Loops** to a small real-world feature. Keep the same core rule, but change the '
                     'context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what loops means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for loops.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small loops example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Loops.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Loops without violating the stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['loop', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_08',
    'title': 'Nested Loops & Patterns',
    'description': 'Use nested loops to build tables and patterns by separating row logic from column logic.',
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
    'explanation': 'Use nested loops to build tables and patterns by separating row logic from column logic. Java '
                   'syntax is shown using the standard library or language feature for this lesson. Pay attention to '
                   'the type, identifier, method call, object reference, and punctuation.',
    'syntax': 'for (int row = 1; row <= 3; row++) {\n'
              '    for (int col = 1; col <= 4; col++) System.out.print("* ");\n'
              '    System.out.println();\n'
              '}',
    'syntax_breakdown': [ 'Focus on outer loop: identify what it represents and what role it plays in the statement.',
                          'Next inspect inner loop: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'public class Main {\n'
                '    public static void main(String[] args) {\n'
                '        for (int row = 1; row <= 3; row++) {\n'
                '            for (int col = 1; col <= 4; col++) System.out.print("* ");\n'
                '            System.out.println();\n'
                '        }\n'
                '    }\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'for(int r=1;r<=4;r++){\n'
                '    for(int c=1;c<=r;c++) System.out.print("*");\n'
                '    System.out.println();\n'
                '}',
    'example2_explanation': 'Change one meaningful input or rule related to nested loops & patterns, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small nested loops & patterns feature in a student or inventory application. '
                         'Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using outer loop without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls inner loop.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of outer loop in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
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
    'next_lesson': 'Methods & Return Values',
    'rules': [ 'Explain the job of outer loop in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the nested loops & '
            'patterns exercise.',
    'extension': 'Add one realistic requirement to the nested loops & patterns exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain nested loops & patterns without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_07'],
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
                  '**Using outer loop without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
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
  { 'id': 'java_09',
    'title': 'Methods & Return Values',
    'description': 'Design reusable methods with parameters, return types, overloads, static methods, varargs, and '
                   'recursion.',
    'stage': 'Core Problem Solving',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Methods & Return Values**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what methods & return values means and why it exists.',
                             'Read and write the core syntax used for methods & return values.',
                             'Predict the behavior of a small methods & return values example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['method', 'parameter', 'return type', 'overload'],
    'explanation': 'Design reusable methods with parameters, return types, overloads, static methods, varargs, and '
                   'recursion. Java syntax is shown using the standard library or language feature for this lesson. '
                   'Pay attention to the type, identifier, method call, object reference, and punctuation.',
    'syntax': 'public class Main {\n'
              '    static int square(int n) {\n'
              '        return n * n;\n'
              '    }\n'
              '\n'
              '    public static void main(String[] args) {\n'
              '        System.out.println(square(6));\n'
              '    }\n'
              '}',
    'syntax_breakdown': [ 'Focus on method: identify what it represents and what role it plays in the statement.',
                          'Next inspect parameter: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'public class Main {\n'
                '    static int square(int n) {\n'
                '        return n * n;\n'
                '    }\n'
                '\n'
                '    public static void main(String[] args) {\n'
                '        System.out.println(square(6));\n'
                '    }\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'static int add(int a,int b){ return a+b; }\nSystem.out.println(add(7,5));',
    'example2_explanation': 'Change one meaningful input or rule related to methods & return values, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small methods & return values feature in a student or inventory application. '
                         'Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using method without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls parameter.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of method in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Create methods for add, subtract, multiply, and safe division.',
    'practice_problem': '**Methods & Return Values independent practice:** Create methods for add, subtract, multiply, '
                        'and safe division. You must also add one clearly different variation and test it. Your work '
                        "should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Methods & Return Values:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'Methods & Return Values: What is a parameter?',
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
    'summary': 'You should now be able to explain methods & return values, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Arrays',
    'rules': [ 'Explain the job of method in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the methods & return '
            'values exercise.',
    'extension': 'Add one realistic requirement to the methods & return values exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain methods & return values without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_08'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Methods & Return Values matters because focused functions or methods make behavior reusable, '
                      'testable, and easier to debug.',
    'guided_practice': [ '1. Restate the goal of **Methods & Return Values** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Methods & Return '
                         'Values**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Methods & Return Values** task: Create methods for add, '
                            'subtract, multiply, and safe division. Then create one small variation that changes an '
                            'input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Methods & Return Values** program that exhibits this common mistake: '
                  '**Using method without understanding whether it represents data, behavior, or a relationship.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Methods & Return Values** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what methods & return values means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for methods & return values.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small methods & return values example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Methods & Return Values.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Methods & Return Values without violating the '
                                  'stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['function', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_10',
    'title': 'Arrays',
    'description': 'Store fixed-size collections, use zero-based indexes, traverse arrays, and use java.util.Arrays '
                   'for common operations.',
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
    'explanation': 'Store fixed-size collections, use zero-based indexes, traverse arrays, and use java.util.Arrays '
                   'for common operations. Java syntax is shown using the standard library or language feature for '
                   'this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'int[] scores = {80, 92, 75, 88, 95};\n'
              'int total = 0;\n'
              'for (int score : scores) total += score;\n'
              'System.out.println(total);',
    'syntax_breakdown': [ 'Focus on index: identify what it represents and what role it plays in the statement.',
                          'Next inspect element: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'public class Main {\n'
                '    public static void main(String[] args) {\n'
                '        int[] scores = {80, 92, 75, 88, 95};\n'
                '        int total = 0;\n'
                '        for (int score : scores) total += score;\n'
                '        System.out.println(total);\n'
                '    }\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'int[] values={4,8,15,16,23};\nfor(int i=0;i<values.length;i++) System.out.print(values[i]+" ");',
    'example2_explanation': 'Change one meaningful input or rule related to arrays, predict the result, and only then '
                            'run the program.',
    'practical_example': 'Imagine a small arrays feature in a student or inventory application. Identify the '
                         'input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using index without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls element.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of index in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Read five scores and report total, average, highest, and lowest.',
    'practice_problem': '**Arrays independent practice:** Read five scores and report total, average, highest, and '
                        'lowest. You must also add one clearly different variation and test it. Your work should '
                        "demonstrate the lesson's main rule, not merely reproduce Example 1.",
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
    'next_lesson': 'Strings & StringBuilder',
    'rules': [ 'Explain the job of index in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the arrays exercise.',
    'extension': 'Add one realistic requirement to the arrays exercise while keeping the original behavior correct.',
    'learning_checks': [ 'Can I explain arrays without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_09'],
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
    'independent_practice': 'Independently solve this **Arrays** task: Read five scores and report total, average, '
                            'highest, and lowest. Then create one small variation that changes an input, rule, or data '
                            'case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Arrays** program that exhibits this common mistake: **Using index '
                  'without understanding whether it represents data, behavior, or a relationship.**. Before changing '
                  'code, identify the first incorrect value, state, control-flow decision, or ownership assumption; '
                  'then explain the fix in one sentence.',
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
  { 'id': 'java_11',
    'title': 'Strings & StringBuilder',
    'description': 'Work with immutable String values, comparison via equals, substring/search methods, and mutable '
                   'StringBuilder for repeated text construction.',
    'stage': 'Core Problem Solving',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Strings & StringBuilder**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what strings & stringbuilder means and why it exists.',
                             'Read and write the core syntax used for strings & stringbuilder.',
                             'Predict the behavior of a small strings & stringbuilder example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['String', 'immutability', 'substring', 'StringBuilder'],
    'explanation': 'Work with immutable String values, comparison via equals, substring/search methods, and mutable '
                   'StringBuilder for repeated text construction. Java syntax is shown using the standard library or '
                   'language feature for this lesson. Pay attention to the type, identifier, method call, object '
                   'reference, and punctuation.',
    'syntax': 'String name = "Ada";\n'
              'String message = "Hello, " + name;\n'
              'System.out.println(message.length());\n'
              'System.out.println(message.contains("Ada"));',
    'syntax_breakdown': [ 'Focus on String: identify what it represents and what role it plays in the statement.',
                          'Next inspect immutability: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'public class Main {\n'
                '    public static void main(String[] args) {\n'
                '        String name = "Ada";\n'
                '        String message = "Hello, " + name;\n'
                '        System.out.println(message.length());\n'
                '        System.out.println(message.contains("Ada"));\n'
                '    }\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'String text="ClassCode";\nif(text.contains("Code")) System.out.println("found");',
    'example2_explanation': 'Change one meaningful input or rule related to strings & stringbuilder, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small strings & stringbuilder feature in a student or inventory application. '
                         'Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using String without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls immutability.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of String in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Read a sentence and report its length, first character, and whether it contains a chosen word.',
    'practice_problem': '**Strings & StringBuilder independent practice:** Read a sentence and report its length, '
                        'first character, and whether it contains a chosen word. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Strings & StringBuilder:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'Strings & StringBuilder: What does string length tell you?',
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
    'summary': 'You should now be able to explain strings & stringbuilder, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'ArrayList',
    'rules': [ 'Explain the job of String in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the strings & '
            'stringbuilder exercise.',
    'extension': 'Add one realistic requirement to the strings & stringbuilder exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain strings & stringbuilder without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_10'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Strings & StringBuilder matters because user-facing programs constantly process names, '
                      'messages, commands, and other text.',
    'guided_practice': [ '1. Restate the goal of **Strings & StringBuilder** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Strings & '
                         'StringBuilder**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Strings & StringBuilder** task: Read a sentence and report its '
                            'length, first character, and whether it contains a chosen word. Then create one small '
                            'variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Strings & StringBuilder** program that exhibits this common mistake: '
                  '**Using String without understanding whether it represents data, behavior, or a relationship.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Strings & StringBuilder** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what strings & stringbuilder means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for strings & stringbuilder.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small strings & stringbuilder example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Strings & StringBuilder.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Strings & StringBuilder without violating the '
                                  'stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['string', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_12',
    'title': 'ArrayList',
    'description': 'Use ArrayList for resizable ordered collections and understand add, get, set, remove, size, and '
                   'iteration.',
    'stage': 'Core Problem Solving',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **ArrayList**, understand why it is useful, trace a focused '
                    'example, practice it with guidance, then solve an independent variation. You will finish by '
                    'proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what arraylist means and why it exists.',
                             'Read and write the core syntax used for arraylist.',
                             'Predict the behavior of a small arraylist example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['ArrayList', 'index', 'size', 'generic type'],
    'explanation': 'Use ArrayList for resizable ordered collections and understand add, get, set, remove, size, and '
                   'iteration. Java syntax is shown using the standard library or language feature for this lesson. '
                   'Pay attention to the type, identifier, method call, object reference, and punctuation.',
    'syntax': 'ArrayList<Integer> scores = new ArrayList<>();\n'
              'scores.add(85);\n'
              'scores.add(92);\n'
              'for (int score : scores) System.out.println(score);',
    'syntax_breakdown': [ 'Focus on ArrayList: identify what it represents and what role it plays in the statement.',
                          'Next inspect index: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'import java.util.ArrayList;\n'
                '\n'
                'public class Main {\n'
                '    public static void main(String[] args) {\n'
                '        ArrayList<Integer> scores = new ArrayList<>();\n'
                '        scores.add(85);\n'
                '        scores.add(92);\n'
                '        for (int score : scores) System.out.println(score);\n'
                '    }\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'int[] values={4,8,15,16,23};\nfor(int i=0;i<values.length;i++) System.out.print(values[i]+" ");',
    'example2_explanation': 'Change one meaningful input or rule related to arraylist, predict the result, and only '
                            'then run the program.',
    'practical_example': 'Imagine a small arraylist feature in a student or inventory application. Identify the '
                         'input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using ArrayList without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls index.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of ArrayList in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Accept scores until -1, then calculate the average and remove a selected score.',
    'practice_problem': '**ArrayList independent practice:** Accept scores until -1, then calculate the average and '
                        'remove a selected score. You must also add one clearly different variation and test it. Your '
                        "work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for ArrayList:** Run the program with a normal case, a boundary case, and a '
                       'misuse/invalid case when relevant. For each case, record the actual result and compare it with '
                       'the requirement. A correct submission must preserve the lesson rule and handle the defined '
                       'edge case safely.',
    'mastery_quiz': [ [ 'ArrayList: What is the first index of a normal C++ or Java array?',
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
    'summary': 'You should now be able to explain arraylist, recognize its syntax, trace the worked example, and use '
               'the concept in a small original program.',
    'next_lesson': 'HashMap & HashSet',
    'rules': [ 'Explain the job of ArrayList in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the arraylist exercise.',
    'extension': 'Add one realistic requirement to the arraylist exercise while keeping the original behavior correct.',
    'learning_checks': [ 'Can I explain arraylist without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_11'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'ArrayList matters because programs often need to store, find, update, and process groups of '
                      'related values.',
    'guided_practice': [ '1. Restate the goal of **ArrayList** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **ArrayList**, then '
                         'change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **ArrayList** task: Accept scores until -1, then calculate the '
                            'average and remove a selected score. Then create one small variation that changes an '
                            'input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **ArrayList** program that exhibits this common mistake: **Using '
                  'ArrayList without understanding whether it represents data, behavior, or a relationship.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **ArrayList** to a small real-world feature. Keep the same core rule, but change the '
                     'context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what arraylist means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for arraylist.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small arraylist example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for ArrayList.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for ArrayList without violating the stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['collection', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_13',
    'title': 'HashMap & HashSet',
    'description': 'Use maps for key-value lookup and frequency counting and sets for uniqueness, while understanding '
                   'hashing and the absence of guaranteed sorted order.',
    'stage': 'Core Problem Solving',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **HashMap & HashSet**, understand why it is useful, trace a focused '
                    'example, practice it with guidance, then solve an independent variation. You will finish by '
                    'proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what hashmap & hashset means and why it exists.',
                             'Read and write the core syntax used for hashmap & hashset.',
                             'Predict the behavior of a small hashmap & hashset example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['key', 'value', 'hashing', 'uniqueness'],
    'explanation': 'Use maps for key-value lookup and frequency counting and sets for uniqueness, while understanding '
                   'hashing and the absence of guaranteed sorted order. Java syntax is shown using the standard '
                   'library or language feature for this lesson. Pay attention to the type, identifier, method call, '
                   'object reference, and punctuation.',
    'syntax': 'Map<String,Integer> counts = new HashMap<>();\n'
              'counts.merge("apple", 1, Integer::sum);\n'
              'System.out.println(counts.get("apple"));',
    'syntax_breakdown': [ 'Focus on key: identify what it represents and what role it plays in the statement.',
                          'Next inspect value: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'Map<String,Integer> counts = new HashMap<>();\n'
                'counts.merge("apple", 1, Integer::sum);\n'
                'System.out.println(counts.get("apple"));',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'Map<String,Integer> scores=new HashMap<>();\n'
                'scores.put("Ren",95);\n'
                'System.out.println(scores.getOrDefault("Ren",0));',
    'example2_explanation': 'Change one meaningful input or rule related to hashmap & hashset, predict the result, and '
                            'only then run the program.',
    'practical_example': 'Imagine a small hashmap & hashset feature in a student or inventory application. Identify '
                         'the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using key without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls value.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of key in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Build a word-frequency counter and a set of unique student IDs.',
    'practice_problem': '**HashMap & HashSet independent practice:** Build a word-frequency counter and a set of '
                        'unique student IDs. You must also add one clearly different variation and test it. Your work '
                        "should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for HashMap & HashSet:** Run the program with a normal case, a boundary case, '
                       'and a misuse/invalid case when relevant. For each case, record the actual result and compare '
                       'it with the requirement. A correct submission must preserve the lesson rule and handle the '
                       'defined edge case safely.',
    'mastery_quiz': [ [ 'HashMap & HashSet: What is a map primarily for?',
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
    'summary': 'You should now be able to explain hashmap & hashset, recognize its syntax, trace the worked example, '
               'and use the concept in a small original program.',
    'next_lesson': 'Exception Handling',
    'rules': [ 'Explain the job of key in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the hashmap & hashset '
            'exercise.',
    'extension': 'Add one realistic requirement to the hashmap & hashset exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain hashmap & hashset without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_12'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'HashMap & HashSet matters because programs often need to store, find, update, and process '
                      'groups of related values.',
    'guided_practice': [ '1. Restate the goal of **HashMap & HashSet** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **HashMap & '
                         'HashSet**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **HashMap & HashSet** task: Build a word-frequency counter and a '
                            'set of unique student IDs. Then create one small variation that changes an input, rule, '
                            'or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **HashMap & HashSet** program that exhibits this common mistake: **Using '
                  'key without understanding whether it represents data, behavior, or a relationship.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **HashMap & HashSet** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what hashmap & hashset means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for hashmap & hashset.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small hashmap & hashset example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for HashMap & HashSet.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for HashMap & HashSet without violating the stated '
                                  'rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['collection', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_14',
    'title': 'Exception Handling',
    'description': 'Handle exceptional situations with try, catch, finally, throw, throws, and custom exception '
                   'classes while distinguishing checked and unchecked exceptions.',
    'stage': 'Core Problem Solving',
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
    'explanation': 'Handle exceptional situations with try, catch, finally, throw, throws, and custom exception '
                   'classes while distinguishing checked and unchecked exceptions. Java syntax is shown using the '
                   'standard library or language feature for this lesson. Pay attention to the type, identifier, '
                   'method call, object reference, and punctuation.',
    'syntax': 'try {\n'
              '    int value = Integer.parseInt("42");\n'
              '    System.out.println(value);\n'
              '} catch (NumberFormatException ex) {\n'
              '    System.out.println("Invalid number");\n'
              '}',
    'syntax_breakdown': [ 'Focus on exception: identify what it represents and what role it plays in the statement.',
                          'Next inspect try: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'try {\n'
                '    int value = Integer.parseInt("42");\n'
                '    System.out.println(value);\n'
                '} catch (NumberFormatException ex) {\n'
                '    System.out.println("Invalid number");\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'try {\n'
                '    int value=Integer.parseInt("42");\n'
                '} catch(NumberFormatException ex) {\n'
                '    System.out.println("Invalid");\n'
                '}',
    'example2_explanation': 'Change one meaningful input or rule related to exception handling, predict the result, '
                            'and only then run the program.',
    'practical_example': 'Imagine a small exception handling feature in a student or inventory application. Identify '
                         'the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using exception without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls try.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of exception in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Validate user input and handle a conversion failure without crashing the program.',
    'practice_problem': '**Exception Handling independent practice:** Validate user input and handle a conversion '
                        'failure without crashing the program. You must also add one clearly different variation and '
                        "test it. Your work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
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
    'next_lesson': 'Classes & Objects',
    'rules': [ 'Explain the job of exception in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the exception handling '
            'exercise.',
    'extension': 'Add one realistic requirement to the exception handling exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain exception handling without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_13'],
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
    'independent_practice': 'Independently solve this **Exception Handling** task: Validate user input and handle a '
                            'conversion failure without crashing the program. Then create one small variation that '
                            'changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Exception Handling** program that exhibits this common mistake: '
                  '**Using exception without understanding whether it represents data, behavior, or a relationship.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
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
  { 'id': 'java_15',
    'title': 'Classes & Objects',
    'description': 'Model data and behavior with classes, fields, methods, object creation, access control, and the '
                   'relationship between a class and its instances.',
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
    'explanation': 'Model data and behavior with classes, fields, methods, object creation, access control, and the '
                   'relationship between a class and its instances. Java syntax is shown using the standard library or '
                   'language feature for this lesson. Pay attention to the type, identifier, method call, object '
                   'reference, and punctuation.',
    'syntax': 'class Student {\n'
              '    String name;\n'
              '    void greet() { System.out.println("Hi " + name); }\n'
              '}\n'
              'Student s = new Student();\n'
              's.name = "Ren";\n'
              's.greet();',
    'syntax_breakdown': [ 'Focus on class: identify what it represents and what role it plays in the statement.',
                          'Next inspect object: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'class Student {\n'
                '    String name;\n'
                '    void greet() { System.out.println("Hi " + name); }\n'
                '}\n'
                'Student s = new Student();\n'
                's.name = "Ren";\n'
                's.greet();',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'class Lamp {\n    boolean on;\n    void toggle(){ on=!on; }\n}\nLamp lamp=new Lamp(); lamp.toggle();',
    'example2_explanation': 'Change one meaningful input or rule related to classes & objects, predict the result, and '
                            'only then run the program.',
    'practical_example': 'Imagine a small classes & objects feature in a student or inventory application. Identify '
                         'the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using class without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls object.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of class in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Create a Book class with title, author, and a method that prints its details.',
    'practice_problem': '**Classes & Objects independent practice:** Create a Book class with title, author, and a '
                        'method that prints its details. You must also add one clearly different variation and test '
                        "it. Your work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
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
    'next_lesson': 'Constructors',
    'rules': [ 'Explain the job of class in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the classes & objects '
            'exercise.',
    'extension': 'Add one realistic requirement to the classes & objects exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain classes & objects without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_14'],
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
                            'author, and a method that prints its details. Then create one small variation that '
                            'changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Classes & Objects** program that exhibits this common mistake: **Using '
                  'class without understanding whether it represents data, behavior, or a relationship.**. Before '
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
  { 'id': 'java_16',
    'title': 'Constructors',
    'description': 'Use constructors to establish object state, overload constructors when useful, and understand '
                   'constructor chaining with this().',
    'stage': 'Data & Design',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Constructors**, understand why it is useful, trace a focused '
                    'example, practice it with guidance, then solve an independent variation. You will finish by '
                    'proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what constructors means and why it exists.',
                             'Read and write the core syntax used for constructors.',
                             'Predict the behavior of a small constructors example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['constructor', 'initializer', 'this', 'object state'],
    'explanation': 'Use constructors to establish object state, overload constructors when useful, and understand '
                   'constructor chaining with this(). Java syntax is shown using the standard library or language '
                   'feature for this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'class Account {\n'
              '    private double balance;\n'
              '    Account(double start) { balance = Math.max(0, start); }\n'
              '}',
    'syntax_breakdown': [ 'Focus on constructor: identify what it represents and what role it plays in the statement.',
                          'Next inspect initializer: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'class Account {\n'
                '    private double balance;\n'
                '    Account(double start) { balance = Math.max(0, start); }\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'class Point {\n'
                '    private final int x;\n'
                '    Point(int x){ this.x=x; }\n'
                '    int getX(){ return x; }\n'
                '}',
    'example2_explanation': 'Change one meaningful input or rule related to constructors, predict the result, and only '
                            'then run the program.',
    'practical_example': 'Imagine a small constructors feature in a student or inventory application. Identify the '
                         'input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using constructor without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls initializer.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of constructor in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Create a class with a default constructor and a parameterized constructor that establish valid state.',
    'practice_problem': '**Constructors independent practice:** Create a class with a default constructor and a '
                        'parameterized constructor that establish valid state. You must also add one clearly different '
                        "variation and test it. Your work should demonstrate the lesson's main rule, not merely "
                        'reproduce Example 1.',
    'expected_output': '**Test contract for Constructors:** Run the program with a normal case, a boundary case, and a '
                       'misuse/invalid case when relevant. For each case, record the actual result and compare it with '
                       'the requirement. A correct submission must preserve the lesson rule and handle the defined '
                       'edge case safely.',
    'mastery_quiz': [ [ 'Constructors: What is the main design idea in Constructors?',
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
    'summary': 'You should now be able to explain constructors, recognize its syntax, trace the worked example, and '
               'use the concept in a small original program.',
    'next_lesson': 'Encapsulation & Access Modifiers',
    'rules': [ 'Explain the job of constructor in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the constructors '
            'exercise.',
    'extension': 'Add one realistic requirement to the constructors exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain constructors without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_15'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Constructors matters because larger programs need clear ownership of state and behavior and '
                      'predictable relationships between types.',
    'guided_practice': [ '1. Restate the goal of **Constructors** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Constructors**, '
                         'then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Constructors** task: Create a class with a default constructor '
                            'and a parameterized constructor that establish valid state. Then create one small '
                            'variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Constructors** program that exhibits this common mistake: **Using '
                  'constructor without understanding whether it represents data, behavior, or a relationship.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Constructors** to a small real-world feature. Keep the same core rule, but change the '
                     'context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what constructors means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for constructors.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small constructors example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Constructors.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Constructors without violating the stated '
                                  'rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in '
                                  'Constructors.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['oop', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_17',
    'title': 'Encapsulation & Access Modifiers',
    'description': 'Protect object state with private fields and public methods, and understand public, private, '
                   'protected, and package-private access.',
    'stage': 'Data & Design',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Encapsulation & Access Modifiers**, understand why it is useful, '
                    'trace a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what encapsulation & access modifiers means and why it exists.',
                             'Read and write the core syntax used for encapsulation & access modifiers.',
                             'Predict the behavior of a small encapsulation & access modifiers example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['Encapsulation & Access Modifiers', 'syntax', 'behavior', 'use case'],
    'explanation': 'Protect object state with private fields and public methods, and understand public, private, '
                   'protected, and package-private access. Java syntax is shown using the standard library or language '
                   'feature for this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'class BankAccount {\n'
              '    private double balance;\n'
              '    public void deposit(double amount) { if (amount > 0) balance += amount; }\n'
              '    public double getBalance() { return balance; }\n'
              '}',
    'syntax_breakdown': [ 'Focus on Encapsulation & Access Modifiers: identify what it represents and what role it '
                          'plays in the statement.',
                          'Next inspect syntax: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'class BankAccount {\n'
                '    private double balance;\n'
                '    public void deposit(double amount) { if (amount > 0) balance += amount; }\n'
                '    public double getBalance() { return balance; }\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'class Score {\n'
                '    private int value;\n'
                '    public void set(int v){ if(v>=0&&v<=100) value=v; }\n'
                '    public int get(){ return value; }\n'
                '}',
    'example2_explanation': 'Change one meaningful input or rule related to encapsulation & access modifiers, predict '
                            'the result, and only then run the program.',
    'practical_example': 'Imagine a small encapsulation & access modifiers feature in a student or inventory '
                         'application. Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using Encapsulation & Access Modifiers without understanding whether it represents data, '
                         'behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls syntax.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of Encapsulation & Access Modifiers in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Design a Student class whose grade cannot be set outside 0–100.',
    'practice_problem': '**Encapsulation & Access Modifiers independent practice:** Design a Student class whose grade '
                        'cannot be set outside 0–100. You must also add one clearly different variation and test it. '
                        "Your work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Encapsulation & Access Modifiers:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Encapsulation & Access Modifiers: What is the main design idea in Encapsulation & Access '
                        'Modifiers?',
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
    'summary': 'You should now be able to explain encapsulation & access modifiers, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Composition',
    'rules': [ 'Explain the job of Encapsulation & Access Modifiers in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the encapsulation & '
            'access modifiers exercise.',
    'extension': 'Add one realistic requirement to the encapsulation & access modifiers exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain encapsulation & access modifiers without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_16'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Encapsulation & Access Modifiers matters because larger programs need clear ownership of state '
                      'and behavior and predictable relationships between types.',
    'guided_practice': [ '1. Restate the goal of **Encapsulation & Access Modifiers** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Encapsulation & '
                         'Access Modifiers**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Encapsulation & Access Modifiers** task: Design a Student '
                            'class whose grade cannot be set outside 0–100. Then create one small variation that '
                            'changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Encapsulation & Access Modifiers** program that exhibits this common '
                  'mistake: **Using Encapsulation & Access Modifiers without understanding whether it represents data, '
                  'behavior, or a relationship.**. Before changing code, identify the first incorrect value, state, '
                  'control-flow decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Encapsulation & Access Modifiers** to a small real-world feature. Keep the same core '
                     'rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what encapsulation & access modifiers means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for encapsulation & access '
                                                 'modifiers.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small encapsulation & access modifiers '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Encapsulation & Access '
                                  'Modifiers.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Encapsulation & Access Modifiers without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Encapsulation '
                                  '& Access Modifiers.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['oop', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_18',
    'title': 'Composition',
    'description': 'Build objects from other objects and prefer composition when one object naturally owns or uses '
                   'another object.',
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
    'explanation': 'Build objects from other objects and prefer composition when one object naturally owns or uses '
                   'another object. Java syntax is shown using the standard library or language feature for this '
                   'lesson. Pay attention to the type, identifier, method call, object reference, and punctuation.',
    'syntax': 'class Engine { void start(){ System.out.println("Engine on"); } }\n'
              'class Car {\n'
              '    private final Engine engine = new Engine();\n'
              '    void start(){ engine.start(); }\n'
              '}',
    'syntax_breakdown': [ 'Focus on has-a: identify what it represents and what role it plays in the statement.',
                          'Next inspect component: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'class Engine { void start(){ System.out.println("Engine on"); } }\n'
                'class Car {\n'
                '    private final Engine engine = new Engine();\n'
                '    void start(){ engine.start(); }\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'class Battery { int level=100; }\n'
                'class Phone {\n'
                '    private final Battery battery=new Battery();\n'
                '    int level(){ return battery.level; }\n'
                '}',
    'example2_explanation': 'Change one meaningful input or rule related to composition, predict the result, and only '
                            'then run the program.',
    'practical_example': 'Imagine a small composition feature in a student or inventory application. Identify the '
                         'input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using has-a without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls component.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of has-a in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Create a Computer containing CPU and Storage objects and explain the ownership relationship.',
    'practice_problem': '**Composition independent practice:** Create a Computer containing CPU and Storage objects '
                        'and explain the ownership relationship. You must also add one clearly different variation and '
                        "test it. Your work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
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
    'rules': [ 'Explain the job of has-a in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the composition '
            'exercise.',
    'extension': 'Add one realistic requirement to the composition exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain composition without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_17'],
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
    'independent_practice': 'Independently solve this **Composition** task: Create a Computer containing CPU and '
                            'Storage objects and explain the ownership relationship. Then create one small variation '
                            'that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Composition** program that exhibits this common mistake: **Using has-a '
                  'without understanding whether it represents data, behavior, or a relationship.**. Before changing '
                  'code, identify the first incorrect value, state, control-flow decision, or ownership assumption; '
                  'then explain the fix in one sentence.',
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
  { 'id': 'java_19',
    'title': 'Inheritance',
    'description': 'Reuse and specialize behavior with extends, inherited members, constructor chaining, and the super '
                   'keyword.',
    'stage': 'Data & Design',
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
    'explanation': 'Reuse and specialize behavior with extends, inherited members, constructor chaining, and the super '
                   'keyword. Java syntax is shown using the standard library or language feature for this lesson. Pay '
                   'attention to the type, identifier, method call, object reference, and punctuation.',
    'syntax': 'class Animal { void eat(){ System.out.println("eat"); } }\n'
              'class Dog extends Animal { void bark(){ System.out.println("woof"); } }',
    'syntax_breakdown': [ 'Focus on base class: identify what it represents and what role it plays in the statement.',
                          'Next inspect derived class: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'class Animal { void eat(){ System.out.println("eat"); } }\n'
                'class Dog extends Animal { void bark(){ System.out.println("woof"); } }',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'class Vehicle { void move(){ System.out.println("move"); } }\n'
                'class Bike extends Vehicle { void ring(){ System.out.println("ring"); } }',
    'example2_explanation': 'Change one meaningful input or rule related to inheritance, predict the result, and only '
                            'then run the program.',
    'practical_example': 'Imagine a small inheritance feature in a student or inventory application. Identify the '
                         'input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using base class without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls derived class.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of base class in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Create a base Vehicle class and two subclasses with specialized behavior.',
    'practice_problem': '**Inheritance independent practice:** Create a base Vehicle class and two subclasses with '
                        'specialized behavior. You must also add one clearly different variation and test it. Your '
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
    'next_lesson': 'Polymorphism & Overriding',
    'rules': [ 'Explain the job of base class in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the inheritance '
            'exercise.',
    'extension': 'Add one realistic requirement to the inheritance exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain inheritance without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_18'],
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
                            'subclasses with specialized behavior. Then create one small variation that changes an '
                            'input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Inheritance** program that exhibits this common mistake: **Using base '
                  'class without understanding whether it represents data, behavior, or a relationship.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
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
  { 'id': 'java_20',
    'title': 'Polymorphism & Overriding',
    'description': 'Use parent references to hold child objects and override methods so the actual object type '
                   'determines behavior at runtime.',
    'stage': 'Data & Design',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Polymorphism & Overriding**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what polymorphism & overriding means and why it exists.',
                             'Read and write the core syntax used for polymorphism & overriding.',
                             'Predict the behavior of a small polymorphism & overriding example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['Polymorphism & Overriding', 'syntax', 'behavior', 'use case'],
    'explanation': 'Use parent references to hold child objects and override methods so the actual object type '
                   'determines behavior at runtime. Java syntax is shown using the standard library or language '
                   'feature for this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'class Shape { double area(){ return 0; } }\n'
              'class Square extends Shape { @Override double area(){ return 16; } }\n'
              'Shape s = new Square();\n'
              'System.out.println(s.area());',
    'syntax_breakdown': [ 'Focus on Polymorphism & Overriding: identify what it represents and what role it plays in '
                          'the statement.',
                          'Next inspect syntax: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'class Shape { double area(){ return 0; } }\n'
                'class Square extends Shape { @Override double area(){ return 16; } }\n'
                'Shape s = new Square();\n'
                'System.out.println(s.area());',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'class Shape { double area(){return 0;} }\n'
                'class Square extends Shape { @Override double area(){return 16;} }\n'
                'Shape s=new Square(); System.out.println(s.area());',
    'example2_explanation': 'Change one meaningful input or rule related to polymorphism & overriding, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small polymorphism & overriding feature in a student or inventory application. '
                         'Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using Polymorphism & Overriding without understanding whether it represents data, behavior, '
                         'or a relationship.',
                         'Forgetting the Java-specific rule that controls syntax.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of Polymorphism & Overriding in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Create Circle and Rectangle subclasses and process them through a List<Shape>.',
    'practice_problem': '**Polymorphism & Overriding independent practice:** Create Circle and Rectangle subclasses '
                        'and process them through a List<Shape>. You must also add one clearly different variation and '
                        "test it. Your work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Polymorphism & Overriding:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Polymorphism & Overriding: What is the main design idea in Polymorphism & Overriding?',
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
    'summary': 'You should now be able to explain polymorphism & overriding, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Abstract Classes & Interfaces',
    'rules': [ 'Explain the job of Polymorphism & Overriding in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the polymorphism & '
            'overriding exercise.',
    'extension': 'Add one realistic requirement to the polymorphism & overriding exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain polymorphism & overriding without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_19'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Polymorphism & Overriding matters because larger programs need clear ownership of state and '
                      'behavior and predictable relationships between types.',
    'guided_practice': [ '1. Restate the goal of **Polymorphism & Overriding** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Polymorphism & '
                         'Overriding**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Polymorphism & Overriding** task: Create Circle and Rectangle '
                            'subclasses and process them through a List<Shape>. Then create one small variation that '
                            'changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Polymorphism & Overriding** program that exhibits this common mistake: '
                  '**Using Polymorphism & Overriding without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Polymorphism & Overriding** to a small real-world feature. Keep the same core rule, '
                     'but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what polymorphism & overriding means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for polymorphism & overriding.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small polymorphism & overriding example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Polymorphism & Overriding.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Polymorphism & Overriding without violating '
                                  'the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Polymorphism & '
                                  'Overriding.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['oop', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_21',
    'title': 'Abstract Classes & Interfaces',
    'description': 'Use abstract classes for shared structure and interfaces for contracts that multiple unrelated '
                   'classes can implement.',
    'stage': 'Data & Design',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Abstract Classes & Interfaces**, understand why it is useful, '
                    'trace a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what abstract classes & interfaces means and why it exists.',
                             'Read and write the core syntax used for abstract classes & interfaces.',
                             'Predict the behavior of a small abstract classes & interfaces example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['abstract class', 'interface', 'implements', 'contract'],
    'explanation': 'Use abstract classes for shared structure and interfaces for contracts that multiple unrelated '
                   'classes can implement. Java syntax is shown using the standard library or language feature for '
                   'this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'interface Payable { double pay(); }\n'
              'class Invoice implements Payable {\n'
              '    public double pay(){ return 100; }\n'
              '}',
    'syntax_breakdown': [ 'Focus on abstract class: identify what it represents and what role it plays in the '
                          'statement.',
                          'Next inspect interface: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'interface Payable { double pay(); }\n'
                'class Invoice implements Payable {\n'
                '    public double pay(){ return 100; }\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'interface Payable { double pay(); }\n'
                'class Invoice implements Payable { public double pay(){return 100;} }',
    'example2_explanation': 'Change one meaningful input or rule related to abstract classes & interfaces, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small abstract classes & interfaces feature in a student or inventory application. '
                         'Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using abstract class without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls interface.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of abstract class in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Design a Payable interface with two concrete implementations.',
    'practice_problem': '**Abstract Classes & Interfaces independent practice:** Design a Payable interface with two '
                        'concrete implementations. You must also add one clearly different variation and test it. Your '
                        "work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Abstract Classes & Interfaces:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Abstract Classes & Interfaces: What is the main design idea in Abstract Classes & Interfaces?',
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
    'summary': 'You should now be able to explain abstract classes & interfaces, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Enums & Records',
    'rules': [ 'Explain the job of abstract class in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the abstract classes & '
            'interfaces exercise.',
    'extension': 'Add one realistic requirement to the abstract classes & interfaces exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain abstract classes & interfaces without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_20'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Abstract Classes & Interfaces matters because larger programs need clear ownership of state and '
                      'behavior and predictable relationships between types.',
    'guided_practice': [ '1. Restate the goal of **Abstract Classes & Interfaces** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Abstract Classes & '
                         'Interfaces**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Abstract Classes & Interfaces** task: Design a Payable '
                            'interface with two concrete implementations. Then create one small variation that changes '
                            'an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Abstract Classes & Interfaces** program that exhibits this common '
                  'mistake: **Using abstract class without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Abstract Classes & Interfaces** to a small real-world feature. Keep the same core '
                     'rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what abstract classes & interfaces means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for abstract classes & '
                                                 'interfaces.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small abstract classes & interfaces '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Abstract Classes & Interfaces.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Abstract Classes & Interfaces without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Abstract '
                                  'Classes & Interfaces.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['oop', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_22',
    'title': 'Enums & Records',
    'description': 'Use enums for fixed named states and records for concise immutable data carriers when their '
                   'semantics fit.',
    'stage': 'Object-Oriented Programming',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Enums & Records**, understand why it is useful, trace a focused '
                    'example, practice it with guidance, then solve an independent variation. You will finish by '
                    'proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what enums & records means and why it exists.',
                             'Read and write the core syntax used for enums & records.',
                             'Predict the behavior of a small enums & records example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['Enums & Records', 'syntax', 'behavior', 'use case'],
    'explanation': 'Use enums for fixed named states and records for concise immutable data carriers when their '
                   'semantics fit. Java syntax is shown using the standard library or language feature for this '
                   'lesson. Pay attention to the type, identifier, method call, object reference, and punctuation.',
    'syntax': 'enum Status { NEW, ACTIVE, CLOSED }\nrecord Student(String name, int age) {}',
    'syntax_breakdown': [ 'Focus on Enums & Records: identify what it represents and what role it plays in the '
                          'statement.',
                          'Next inspect syntax: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'enum Status { NEW, ACTIVE, CLOSED }\nrecord Student(String name, int age) {}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'enum Status { NEW, ACTIVE, CLOSED }\n'
                'record User(String name,int age){}\n'
                'System.out.println(Status.ACTIVE);',
    'example2_explanation': 'Change one meaningful input or rule related to enums & records, predict the result, and '
                            'only then run the program.',
    'practical_example': 'Imagine a small enums & records feature in a student or inventory application. Identify the '
                         'input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using Enums & Records without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls syntax.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of Enums & Records in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Model order status with an enum and a small immutable Student record.',
    'practice_problem': '**Enums & Records independent practice:** Model order status with an enum and a small '
                        'immutable Student record. You must also add one clearly different variation and test it. Your '
                        "work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Enums & Records:** Run the program with a normal case, a boundary case, '
                       'and a misuse/invalid case when relevant. For each case, record the actual result and compare '
                       'it with the requirement. A correct submission must preserve the lesson rule and handle the '
                       'defined edge case safely.',
    'mastery_quiz': [ [ 'Enums & Records: What is the main design idea in Enums & Records?',
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
    'summary': 'You should now be able to explain enums & records, recognize its syntax, trace the worked example, and '
               'use the concept in a small original program.',
    'next_lesson': 'Generics',
    'rules': [ 'Explain the job of Enums & Records in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the enums & records '
            'exercise.',
    'extension': 'Add one realistic requirement to the enums & records exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain enums & records without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_21'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Enums & Records gives you the foundation needed to read, change, and reason about a program '
                      'before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Enums & Records** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Enums & Records**, '
                         'then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Enums & Records** task: Model order status with an enum and a '
                            'small immutable Student record. Then create one small variation that changes an input, '
                            'rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Enums & Records** program that exhibits this common mistake: **Using '
                  'Enums & Records without understanding whether it represents data, behavior, or a relationship.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Enums & Records** to a small real-world feature. Keep the same core rule, but change '
                     'the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what enums & records means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for enums & records.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small enums & records example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Enums & Records.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Enums & Records without violating the stated '
                                  'rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Enums & '
                                  'Records.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_23',
    'title': 'Generics',
    'description': 'Write reusable type-safe classes and methods with type parameters, bounds, and wildcards.',
    'stage': 'Object-Oriented Programming',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Generics**, understand why it is useful, trace a focused example, '
                    'practice it with guidance, then solve an independent variation. You will finish by proving your '
                    'understanding through concept, syntax, code-reading, debugging, and application checks.',
    'learning_objectives': [ 'Explain what generics means and why it exists.',
                             'Read and write the core syntax used for generics.',
                             'Predict the behavior of a small generics example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['type parameter', 'generic method', 'wildcard', 'bound'],
    'explanation': 'Write reusable type-safe classes and methods with type parameters, bounds, and wildcards. Java '
                   'syntax is shown using the standard library or language feature for this lesson. Pay attention to '
                   'the type, identifier, method call, object reference, and punctuation.',
    'syntax': 'static <T extends Number> double twice(T value) {\n    return value.doubleValue() * 2;\n}',
    'syntax_breakdown': [ 'Focus on type parameter: identify what it represents and what role it plays in the '
                          'statement.',
                          'Next inspect generic method: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'static <T extends Number> double twice(T value) {\n    return value.doubleValue() * 2;\n}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'static <T extends Number> double twice(T value){return value.doubleValue()*2;}\n'
                'System.out.println(twice(5));',
    'example2_explanation': 'Change one meaningful input or rule related to generics, predict the result, and only '
                            'then run the program.',
    'practical_example': 'Imagine a small generics feature in a student or inventory application. Identify the '
                         'input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using type parameter without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls generic method.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of type parameter in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Create a generic Box<T> and a method that accepts a list of Number values.',
    'practice_problem': '**Generics independent practice:** Create a generic Box<T> and a method that accepts a list '
                        'of Number values. You must also add one clearly different variation and test it. Your work '
                        "should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Generics:** Run the program with a normal case, a boundary case, and a '
                       'misuse/invalid case when relevant. For each case, record the actual result and compare it with '
                       'the requirement. A correct submission must preserve the lesson rule and handle the defined '
                       'edge case safely.',
    'mastery_quiz': [ [ 'Generics: What is a Java generic type parameter?',
                        [ 'A type placeholder such as T',
                          'A runtime thread',
                          'A file extension',
                          'A compiler executable'],
                        0,
                        'T commonly represents a type parameter.'],
                      [ 'Why use generics?',
                        [ 'To preserve type safety while reusing code',
                          'To remove all objects',
                          'To avoid compilation',
                          'To make every value an int'],
                        0,
                        'Generics provide reusable type-safe abstractions.'],
                      [ 'What does a bounded type parameter express?',
                        [ 'A required relationship such as T extends Number',
                          'A loop count',
                          'A file path',
                          'A package name'],
                        0,
                        'Bounds restrict which types are valid arguments.'],
                      [ 'What is a wildcard?',
                        ['A flexible type argument such as ?', 'A thread', 'A primitive', 'A constructor'],
                        0,
                        'Wildcards express flexible generic relationships.'],
                      [ 'Why avoid raw collections?',
                        [ 'They weaken compile-time type safety',
                          'They are always faster',
                          'They cannot store objects',
                          'They prevent loops'],
                        0,
                        'Raw types can defer type errors until runtime.']],
    'summary': 'You should now be able to explain generics, recognize its syntax, trace the worked example, and use '
               'the concept in a small original program.',
    'next_lesson': 'Collections Framework',
    'rules': [ 'Explain the job of type parameter in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the generics exercise.',
    'extension': 'Add one realistic requirement to the generics exercise while keeping the original behavior correct.',
    'learning_checks': [ 'Can I explain generics without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_22'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Generics matters because reusable code should avoid unnecessary duplication while remaining '
                      'type-safe.',
    'guided_practice': [ '1. Restate the goal of **Generics** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Generics**, then '
                         'change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Generics** task: Create a generic Box<T> and a method that '
                            'accepts a list of Number values. Then create one small variation that changes an input, '
                            'rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Generics** program that exhibits this common mistake: **Using type '
                  'parameter without understanding whether it represents data, behavior, or a relationship.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Generics** to a small real-world feature. Keep the same core rule, but change the '
                     'context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what generics means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for generics.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small generics example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Generics.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Generics without violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Generics.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['generic', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_24',
    'title': 'Collections Framework',
    'description': 'Choose List, Set, Map, Queue, Deque, and PriorityQueue based on ordering, uniqueness, lookup, and '
                   'processing requirements.',
    'stage': 'Object-Oriented Programming',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Collections Framework**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what collections framework means and why it exists.',
                             'Read and write the core syntax used for collections framework.',
                             'Predict the behavior of a small collections framework example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['List', 'Set', 'Map', 'Queue'],
    'explanation': 'Choose List, Set, Map, Queue, Deque, and PriorityQueue based on ordering, uniqueness, lookup, and '
                   'processing requirements. Java syntax is shown using the standard library or language feature for '
                   'this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'Deque<String> tasks = new ArrayDeque<>();\n'
              'tasks.addLast("study");\n'
              'tasks.addFirst("urgent");\n'
              'System.out.println(tasks.removeFirst());',
    'syntax_breakdown': [ 'Focus on List: identify what it represents and what role it plays in the statement.',
                          'Next inspect Set: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'Deque<String> tasks = new ArrayDeque<>();\n'
                'tasks.addLast("study");\n'
                'tasks.addFirst("urgent");\n'
                'System.out.println(tasks.removeFirst());',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'Deque<String> tasks=new ArrayDeque<>();\n'
                'tasks.addLast("study"); tasks.addFirst("urgent");\n'
                'System.out.println(tasks.removeFirst());',
    'example2_explanation': 'Change one meaningful input or rule related to collections framework, predict the result, '
                            'and only then run the program.',
    'practical_example': 'Imagine a small collections framework feature in a student or inventory application. '
                         'Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using List without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls Set.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of List in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Choose and justify a collection for history, unique IDs, key-value lookup, and service queues.',
    'practice_problem': '**Collections Framework independent practice:** Choose and justify a collection for history, '
                        'unique IDs, key-value lookup, and service queues. You must also add one clearly different '
                        "variation and test it. Your work should demonstrate the lesson's main rule, not merely "
                        'reproduce Example 1.',
    'expected_output': '**Test contract for Collections Framework:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'Collections Framework: What is a map primarily for?',
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
    'summary': 'You should now be able to explain collections framework, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'File I/O',
    'rules': [ 'Explain the job of List in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the collections '
            'framework exercise.',
    'extension': 'Add one realistic requirement to the collections framework exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain collections framework without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_23'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Collections Framework matters because programs often need to store, find, update, and process '
                      'groups of related values.',
    'guided_practice': [ '1. Restate the goal of **Collections Framework** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Collections '
                         'Framework**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Collections Framework** task: Choose and justify a collection '
                            'for history, unique IDs, key-value lookup, and service queues. Then create one small '
                            'variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Collections Framework** program that exhibits this common mistake: '
                  '**Using List without understanding whether it represents data, behavior, or a relationship.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Collections Framework** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what collections framework means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for collections framework.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small collections framework example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Collections Framework.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Collections Framework without violating the '
                                  'stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['collection', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_25',
    'title': 'File I/O',
    'description': 'Read and write files with modern java.nio.file APIs and understand paths, character encoding, and '
                   'failure handling.',
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
    'explanation': 'Read and write files with modern java.nio.file APIs and understand paths, character encoding, and '
                   'failure handling. Java syntax is shown using the standard library or language feature for this '
                   'lesson. Pay attention to the type, identifier, method call, object reference, and punctuation.',
    'syntax': 'Path path = Path.of("scores.txt");\n'
              'Files.writeString(path, "Ren 95\\n");\n'
              'String text = Files.readString(path);\n'
              'System.out.println(text);',
    'syntax_breakdown': [ 'Focus on Path: identify what it represents and what role it plays in the statement.',
                          'Next inspect Files: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'Path path = Path.of("scores.txt");\n'
                'Files.writeString(path, "Ren 95\\n");\n'
                'String text = Files.readString(path);\n'
                'System.out.println(text);',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'Path path=Path.of("notes.txt");\n'
                'Files.writeString(path,"hello");\n'
                'System.out.println(Files.readString(path));',
    'example2_explanation': 'Change one meaningful input or rule related to file i/o, predict the result, and only '
                            'then run the program.',
    'practical_example': 'Imagine a small file i/o feature in a student or inventory application. Identify the '
                         'input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using Path without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls Files.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of Path in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Write records to a text file and read them back safely.',
    'practice_problem': '**File I/O independent practice:** Write records to a text file and read them back safely. '
                        'You must also add one clearly different variation and test it. Your work should demonstrate '
                        "the lesson's main rule, not merely reproduce Example 1.",
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
    'next_lesson': 'Serialization & Data Formats',
    'rules': [ 'Explain the job of Path in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the file i/o exercise.',
    'extension': 'Add one realistic requirement to the file i/o exercise while keeping the original behavior correct.',
    'learning_checks': [ 'Can I explain file i/o without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_24'],
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
    'independent_practice': 'Independently solve this **File I/O** task: Write records to a text file and read them '
                            'back safely. Then create one small variation that changes an input, rule, or data case '
                            'without changing the main goal.',
    'debug_task': 'Debug a deliberately small **File I/O** program that exhibits this common mistake: **Using Path '
                  'without understanding whether it represents data, behavior, or a relationship.**. Before changing '
                  'code, identify the first incorrect value, state, control-flow decision, or ownership assumption; '
                  'then explain the fix in one sentence.',
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
  { 'id': 'java_26',
    'title': 'Serialization & Data Formats',
    'description': 'Understand object serialization concepts, JSON-like data formats, and why explicit data formats '
                   'are often preferable for long-lived application data.',
    'stage': 'Object-Oriented Programming',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Serialization & Data Formats**, understand why it is useful, '
                    'trace a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what serialization & data formats means and why it exists.',
                             'Read and write the core syntax used for serialization & data formats.',
                             'Predict the behavior of a small serialization & data formats example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['serialization', 'JSON', 'CSV', 'schema'],
    'explanation': 'Understand object serialization concepts, JSON-like data formats, and why explicit data formats '
                   'are often preferable for long-lived application data. Java syntax is shown using the standard '
                   'library or language feature for this lesson. Pay attention to the type, identifier, method call, '
                   'object reference, and punctuation.',
    'syntax': 'record User(String name, int age) {}\n'
              'User user = new User("Ren", 18);\n'
              'String jsonLike = "{"name":"" + user.name() + ""}";',
    'syntax_breakdown': [ 'Focus on serialization: identify what it represents and what role it plays in the '
                          'statement.',
                          'Next inspect JSON: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'record User(String name, int age) {}\n'
                'User user = new User("Ren", 18);\n'
                'String jsonLike = "{"name":"" + user.name() + ""}";',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'record User(String name,int age){}\n'
                'User u=new User("Ren",18);\n'
                'System.out.println("{name:"+u.name()+"}");',
    'example2_explanation': 'Change one meaningful input or rule related to serialization & data formats, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small serialization & data formats feature in a student or inventory application. '
                         'Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using serialization without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls JSON.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of serialization in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Compare plain text, CSV, JSON, and Java object serialization for different persistence needs.',
    'practice_problem': '**Serialization & Data Formats independent practice:** Compare plain text, CSV, JSON, and '
                        'Java object serialization for different persistence needs. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Serialization & Data Formats:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Serialization & Data Formats: Which statement best describes Serialization & Data Formats?',
                        [ 'It is a core part of Serialization & Data Formats',
                          'It is only a compiler warning',
                          'It is unrelated to programming',
                          'It replaces all data types'],
                        0,
                        'This lesson focuses on the role and correct use of Serialization & Data Formats.'],
                      [ 'What should a learner be able to do after Serialization & Data Formats?',
                        [ 'Use the concept in a small program',
                          'Only memorize its name',
                          'Avoid testing it',
                          'Copy one example unchanged'],
                        0,
                        'Application is the goal, not memorization.'],
                      [ 'Which test is most useful for Serialization & Data Formats?',
                        [ 'A normal case plus an important edge case',
                          'No input',
                          'Only a huge random case',
                          'Only comments'],
                        0,
                        'Testing the concept in more than one case reveals misunderstandings.'],
                      [ 'Which mistake should be avoided with Serialization & Data Formats?',
                        [ 'Using syntax without understanding its behavior',
                          'Writing a small test',
                          'Reading diagnostics',
                          'Choosing clear names'],
                        0,
                        'Understanding behavior matters more than copying syntax.'],
                      [ 'How should Serialization & Data Formats fit into a larger program?',
                        [ 'As one focused tool combined with earlier concepts',
                          'As a replacement for every other feature',
                          'As global state everywhere',
                          'As code that never needs testing'],
                        0,
                        'Programming features are combined according to the problem.']],
    'summary': 'You should now be able to explain serialization & data formats, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Lambda Expressions',
    'rules': [ 'Explain the job of serialization in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the serialization & '
            'data formats exercise.',
    'extension': 'Add one realistic requirement to the serialization & data formats exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain serialization & data formats without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_25'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Serialization & Data Formats matters because programs often need to preserve, load, or exchange '
                      'information outside a single run.',
    'guided_practice': [ '1. Restate the goal of **Serialization & Data Formats** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Serialization & '
                         'Data Formats**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Serialization & Data Formats** task: Compare plain text, CSV, '
                            'JSON, and Java object serialization for different persistence needs. Then create one '
                            'small variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Serialization & Data Formats** program that exhibits this common '
                  'mistake: **Using serialization without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Serialization & Data Formats** to a small real-world feature. Keep the same core '
                     'rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what serialization & data formats means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for serialization & data '
                                                 'formats.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small serialization & data formats '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Serialization & Data Formats.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Serialization & Data Formats without violating '
                                  'the stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['io', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_27',
    'title': 'Lambda Expressions',
    'description': 'Write concise functions as values, capture local variables safely, and pass behavior to collection '
                   'APIs.',
    'stage': 'Object-Oriented Programming',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Lambda Expressions**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what lambda expressions means and why it exists.',
                             'Read and write the core syntax used for lambda expressions.',
                             'Predict the behavior of a small lambda expressions example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['lambda', 'functional interface', 'capture', 'method reference'],
    'explanation': 'Write concise functions as values, capture local variables safely, and pass behavior to collection '
                   'APIs. Java syntax is shown using the standard library or language feature for this lesson. Pay '
                   'attention to the type, identifier, method call, object reference, and punctuation.',
    'syntax': 'List<Integer> values = List.of(1,2,3,4);\nvalues.forEach(x -> System.out.println(x * 2));',
    'syntax_breakdown': [ 'Focus on lambda: identify what it represents and what role it plays in the statement.',
                          'Next inspect functional interface: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'List<Integer> values = List.of(1,2,3,4);\nvalues.forEach(x -> System.out.println(x * 2));',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'List<Integer> values=List.of(1,2,3,4);\nvalues.forEach(x -> System.out.println(x*2));',
    'example2_explanation': 'Change one meaningful input or rule related to lambda expressions, predict the result, '
                            'and only then run the program.',
    'practical_example': 'Imagine a small lambda expressions feature in a student or inventory application. Identify '
                         'the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using lambda without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls functional interface.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of lambda in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Use a lambda to filter or sort a collection based on a custom rule.',
    'practice_problem': '**Lambda Expressions independent practice:** Use a lambda to filter or sort a collection '
                        'based on a custom rule. You must also add one clearly different variation and test it. Your '
                        "work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
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
    'next_lesson': 'Streams',
    'rules': [ 'Explain the job of lambda in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the lambda expressions '
            'exercise.',
    'extension': 'Add one realistic requirement to the lambda expressions exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain lambda expressions without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_26'],
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
    'independent_practice': 'Independently solve this **Lambda Expressions** task: Use a lambda to filter or sort a '
                            'collection based on a custom rule. Then create one small variation that changes an input, '
                            'rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Lambda Expressions** program that exhibits this common mistake: '
                  '**Using lambda without understanding whether it represents data, behavior, or a relationship.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
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
  { 'id': 'java_28',
    'title': 'Streams',
    'description': 'Build stream pipelines with filter, map, sorted, reduce, collect, matching, and terminal '
                   'operations while understanding laziness.',
    'stage': 'Object-Oriented Programming',
    'difficulty': 'Intermediate',
    'introduction': 'In this lesson you will learn **Streams**, understand why it is useful, trace a focused example, '
                    'practice it with guidance, then solve an independent variation. You will finish by proving your '
                    'understanding through concept, syntax, code-reading, debugging, and application checks.',
    'learning_objectives': [ 'Explain what streams means and why it exists.',
                             'Read and write the core syntax used for streams.',
                             'Predict the behavior of a small streams example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['pipeline', 'intermediate operation', 'terminal operation', 'collector'],
    'explanation': 'Build stream pipelines with filter, map, sorted, reduce, collect, matching, and terminal '
                   'operations while understanding laziness. Java syntax is shown using the standard library or '
                   'language feature for this lesson. Pay attention to the type, identifier, method call, object '
                   'reference, and punctuation.',
    'syntax': 'List<Integer> values = List.of(1,2,3,4);\n'
              'int total = values.stream()\n'
              '    .filter(x -> x % 2 == 0)\n'
              '    .mapToInt(Integer::intValue)\n'
              '    .sum();',
    'syntax_breakdown': [ 'Focus on pipeline: identify what it represents and what role it plays in the statement.',
                          'Next inspect intermediate operation: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'List<Integer> values = List.of(1,2,3,4);\n'
                'int total = values.stream()\n'
                '    .filter(x -> x % 2 == 0)\n'
                '    .mapToInt(Integer::intValue)\n'
                '    .sum();',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'int total=List.of(1,2,3,4).stream().filter(x->x%2==0).mapToInt(Integer::intValue).sum();\n'
                'System.out.println(total);',
    'example2_explanation': 'Change one meaningful input or rule related to streams, predict the result, and only then '
                            'run the program.',
    'practical_example': 'Imagine a small streams feature in a student or inventory application. Identify the '
                         'input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using pipeline without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls intermediate operation.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of pipeline in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Create a stream pipeline that filters passing grades, maps them to bonus points, and calculates a '
                'total.',
    'practice_problem': '**Streams independent practice:** Create a stream pipeline that filters passing grades, maps '
                        'them to bonus points, and calculates a total. You must also add one clearly different '
                        "variation and test it. Your work should demonstrate the lesson's main rule, not merely "
                        'reproduce Example 1.',
    'expected_output': '**Test contract for Streams:** Run the program with a normal case, a boundary case, and a '
                       'misuse/invalid case when relevant. For each case, record the actual result and compare it with '
                       'the requirement. A correct submission must preserve the lesson rule and handle the defined '
                       'edge case safely.',
    'mastery_quiz': [ [ 'Streams: What does filter do in a stream pipeline?',
                        [ 'Keeps elements matching a predicate',
                          'Changes every element',
                          'Writes a file',
                          'Stops the JVM'],
                        0,
                        'filter selects elements that satisfy a condition.'],
                      [ 'What does map do?',
                        ['Transforms each element', 'Deletes the stream', 'Creates a thread', 'Reads input'],
                        0,
                        'map converts each element to another value.'],
                      [ 'What is reduce for?',
                        [ 'Combining elements into an accumulated result',
                          'Sorting files',
                          'Opening a socket',
                          'Declaring a class'],
                        0,
                        'reduce combines stream elements into one result.'],
                      [ 'Why are intermediate stream operations lazy?',
                        [ 'They can wait until a terminal operation requests results',
                          'They always run twice',
                          'They disable collections',
                          'They avoid types'],
                        0,
                        'Intermediate operations build a pipeline evaluated when needed.'],
                      [ 'Which is a terminal operation?',
                        ['collect', 'filter', 'map', 'sorted'],
                        0,
                        'collect consumes the stream and produces a result.']],
    'summary': 'You should now be able to explain streams, recognize its syntax, trace the worked example, and use the '
               'concept in a small original program.',
    'next_lesson': 'Optional & Null Safety',
    'rules': [ 'Explain the job of pipeline in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the streams exercise.',
    'extension': 'Add one realistic requirement to the streams exercise while keeping the original behavior correct.',
    'learning_checks': [ 'Can I explain streams without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_27'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Streams matters because modern code often transforms data and composes behavior in compact, '
                      'reusable ways.',
    'guided_practice': [ '1. Restate the goal of **Streams** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Streams**, then '
                         'change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Streams** task: Create a stream pipeline that filters passing '
                            'grades, maps them to bonus points, and calculates a total. Then create one small '
                            'variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Streams** program that exhibits this common mistake: **Using pipeline '
                  'without understanding whether it represents data, behavior, or a relationship.**. Before changing '
                  'code, identify the first incorrect value, state, control-flow decision, or ownership assumption; '
                  'then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Streams** to a small real-world feature. Keep the same core rule, but change the '
                     'context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what streams means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for streams.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small streams example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Streams.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Streams without violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Streams.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['functional', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_29',
    'title': 'Optional & Null Safety',
    'description': 'Represent an optional result explicitly with Optional and reduce accidental null handling while '
                   'recognizing when Optional is appropriate.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Optional & Null Safety**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what optional & null safety means and why it exists.',
                             'Read and write the core syntax used for optional & null safety.',
                             'Predict the behavior of a small optional & null safety example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['Optional', 'empty', 'orElse', 'null'],
    'explanation': 'Represent an optional result explicitly with Optional and reduce accidental null handling while '
                   'recognizing when Optional is appropriate. Java syntax is shown using the standard library or '
                   'language feature for this lesson. Pay attention to the type, identifier, method call, object '
                   'reference, and punctuation.',
    'syntax': 'Optional<String> name = Optional.of("Ren");\nString shown = name.orElse("Unknown");',
    'syntax_breakdown': [ 'Focus on Optional: identify what it represents and what role it plays in the statement.',
                          'Next inspect empty: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'Optional<String> name = Optional.of("Ren");\nString shown = name.orElse("Unknown");',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'Optional<String> name=Optional.ofNullable(null);\nSystem.out.println(name.orElse("Unknown"));',
    'example2_explanation': 'Change one meaningful input or rule related to optional & null safety, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small optional & null safety feature in a student or inventory application. '
                         'Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using Optional without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls empty.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of Optional in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Rewrite a lookup that may return null using Optional and explain when returning Optional improves the '
                'API.',
    'practice_problem': '**Optional & Null Safety independent practice:** Rewrite a lookup that may return null using '
                        'Optional and explain when returning Optional improves the API. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Optional & Null Safety:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'Optional & Null Safety: What does Optional represent?',
                        ['A value that may be present or empty', 'A thread', 'A file', 'A primitive keyword'],
                        0,
                        'Optional models a possibly absent result.'],
                      [ 'What does orElse provide?',
                        ['A fallback value when empty', 'A new thread', 'A file path', 'A class'],
                        0,
                        'orElse supplies a fallback.'],
                      [ 'Why can Optional improve a lookup API?',
                        [ 'Absence is represented explicitly',
                          'It prevents all nulls everywhere',
                          'It removes exceptions',
                          'It makes code asynchronous'],
                        0,
                        'Optional can make absence part of the API contract.'],
                      [ 'What should you avoid?',
                        [ 'Using Optional as a replacement for every field and parameter indiscriminately',
                          'Checking presence',
                          'Using map',
                          'Providing a fallback'],
                        0,
                        'Optional is most useful where absence is a meaningful result.'],
                      [ 'What does map on Optional do?',
                        [ 'Transforms the contained value when present',
                          'Deletes the value',
                          'Creates a file',
                          'Starts a thread'],
                        0,
                        'map transforms a present value while preserving emptiness.']],
    'summary': 'You should now be able to explain optional & null safety, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Threads & Concurrency Basics',
    'rules': [ 'Explain the job of Optional in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the optional & null '
            'safety exercise.',
    'extension': 'Add one realistic requirement to the optional & null safety exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain optional & null safety without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_28'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Optional & Null Safety matters because modern code often transforms data and composes behavior '
                      'in compact, reusable ways.',
    'guided_practice': [ '1. Restate the goal of **Optional & Null Safety** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Optional & Null '
                         'Safety**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Optional & Null Safety** task: Rewrite a lookup that may '
                            'return null using Optional and explain when returning Optional improves the API. Then '
                            'create one small variation that changes an input, rule, or data case without changing the '
                            'main goal.',
    'debug_task': 'Debug a deliberately small **Optional & Null Safety** program that exhibits this common mistake: '
                  '**Using Optional without understanding whether it represents data, behavior, or a relationship.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Optional & Null Safety** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what optional & null safety means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for optional & null safety.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small optional & null safety example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Optional & Null Safety.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Optional & Null Safety without violating the '
                                  'stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Optional & '
                                  'Null Safety.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['functional', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_30',
    'title': 'Threads & Concurrency Basics',
    'description': 'Understand threads, Runnable, scheduling, shared state, race conditions, and why concurrency '
                   'introduces correctness concerns.',
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
    'explanation': 'Understand threads, Runnable, scheduling, shared state, race conditions, and why concurrency '
                   'introduces correctness concerns. Java syntax is shown using the standard library or language '
                   'feature for this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'Thread worker = new Thread(() -> System.out.println("Working"));\nworker.start();\nworker.join();',
    'syntax_breakdown': [ 'Focus on thread: identify what it represents and what role it plays in the statement.',
                          'Next inspect Runnable: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'Thread worker = new Thread(() -> System.out.println("Working"));\nworker.start();\nworker.join();',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'Thread worker=new Thread(() -> System.out.println("Working"));\nworker.start();\nworker.join();',
    'example2_explanation': 'Change one meaningful input or rule related to threads & concurrency basics, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small threads & concurrency basics feature in a student or inventory application. '
                         'Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using thread without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls Runnable.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of thread in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Create two workers that perform independent tasks and identify what would become unsafe if they '
                'shared a mutable counter.',
    'practice_problem': '**Threads & Concurrency Basics independent practice:** Create two workers that perform '
                        'independent tasks and identify what would become unsafe if they shared a mutable counter. You '
                        'must also add one clearly different variation and test it. Your work should demonstrate the '
                        "lesson's main rule, not merely reproduce Example 1.",
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
    'next_lesson': 'Executors & Synchronization',
    'rules': [ 'Explain the job of thread in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the threads & '
            'concurrency basics exercise.',
    'extension': 'Add one realistic requirement to the threads & concurrency basics exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain threads & concurrency basics without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_29'],
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
    'independent_practice': 'Independently solve this **Threads & Concurrency Basics** task: Create two workers that '
                            'perform independent tasks and identify what would become unsafe if they shared a mutable '
                            'counter. Then create one small variation that changes an input, rule, or data case '
                            'without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Threads & Concurrency Basics** program that exhibits this common '
                  'mistake: **Using thread without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
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
    'content_version': '3.4.0'},
  { 'id': 'java_31',
    'title': 'Executors & Synchronization',
    'description': 'Use ExecutorService for task management and synchronized/locks for controlled access to shared '
                   'mutable state.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Executors & Synchronization**, understand why it is useful, trace '
                    'a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what executors & synchronization means and why it exists.',
                             'Read and write the core syntax used for executors & synchronization.',
                             'Predict the behavior of a small executors & synchronization example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['executor', 'synchronization', 'lock', 'critical section'],
    'explanation': 'Use ExecutorService for task management and synchronized/locks for controlled access to shared '
                   'mutable state. Java syntax is shown using the standard library or language feature for this '
                   'lesson. Pay attention to the type, identifier, method call, object reference, and punctuation.',
    'syntax': 'ExecutorService pool = Executors.newFixedThreadPool(2);\n'
              'pool.submit(() -> System.out.println("Task"));\n'
              'pool.shutdown();',
    'syntax_breakdown': [ 'Focus on executor: identify what it represents and what role it plays in the statement.',
                          'Next inspect synchronization: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'ExecutorService pool = Executors.newFixedThreadPool(2);\n'
                'pool.submit(() -> System.out.println("Task"));\n'
                'pool.shutdown();',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'ExecutorService pool=Executors.newFixedThreadPool(2);\n'
                'pool.submit(() -> System.out.println("Task"));\n'
                'pool.shutdown();',
    'example2_explanation': 'Change one meaningful input or rule related to executors & synchronization, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small executors & synchronization feature in a student or inventory application. '
                         'Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using executor without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls synchronization.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of executor in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Move from manually created threads to an executor and protect a shared counter.',
    'practice_problem': '**Executors & Synchronization independent practice:** Move from manually created threads to '
                        'an executor and protect a shared counter. You must also add one clearly different variation '
                        "and test it. Your work should demonstrate the lesson's main rule, not merely reproduce "
                        'Example 1.',
    'expected_output': '**Test contract for Executors & Synchronization:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Executors & Synchronization: What does ExecutorService manage?',
                        ['Submitted tasks and worker threads', 'Only files', 'Only strings', 'Only packages'],
                        0,
                        'Executors separate task submission from manual thread creation.'],
                      [ 'Why shut down an ExecutorService?',
                        [ 'To allow its worker resources to terminate',
                          'To sort its queue',
                          'To create more threads',
                          'To clear all Java objects'],
                        0,
                        'shutdown begins orderly termination after submitted work is handled.'],
                      [ 'What is a critical section?',
                        [ 'Code that accesses shared state and needs coordination',
                          'A package declaration',
                          'A file extension',
                          'A compiler stage'],
                        0,
                        'Critical sections require controlled access when shared state can race.'],
                      [ 'What does synchronized provide?',
                        [ 'Mutual exclusion for protected operations',
                          'Automatic database persistence',
                          'A new collection',
                          'A package import'],
                        0,
                        'synchronized coordinates access to a monitor-protected region/method.'],
                      [ 'Why can check-then-act still be unsafe?',
                        [ 'Another thread can change the state between the check and the action',
                          'Checks are illegal',
                          'Threads cannot read fields',
                          'Executors disable locks'],
                        0,
                        'The whole sequence may need to be atomic.']],
    'summary': 'You should now be able to explain executors & synchronization, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Recursion',
    'rules': [ 'Explain the job of executor in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the executors & '
            'synchronization exercise.',
    'extension': 'Add one realistic requirement to the executors & synchronization exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain executors & synchronization without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_30'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Executors & Synchronization matters because concurrent programs must coordinate work without '
                      'corrupting shared state or hiding failures.',
    'guided_practice': [ '1. Restate the goal of **Executors & Synchronization** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Executors & '
                         'Synchronization**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Executors & Synchronization** task: Move from manually created '
                            'threads to an executor and protect a shared counter. Then create one small variation that '
                            'changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Executors & Synchronization** program that exhibits this common '
                  'mistake: **Using executor without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Executors & Synchronization** to a small real-world feature. Keep the same core rule, '
                     'but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what executors & synchronization means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for executors & synchronization.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small executors & synchronization example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Executors & Synchronization.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Executors & Synchronization without violating '
                                  'the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Executors & '
                                  'Synchronization.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['concurrency', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_32',
    'title': 'Recursion',
    'description': 'Solve a problem by reducing it to smaller inputs, using a base case and a recursive step that '
                   'moves toward termination.',
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
    'explanation': 'Solve a problem by reducing it to smaller inputs, using a base case and a recursive step that '
                   'moves toward termination. Java syntax is shown using the standard library or language feature for '
                   'this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'static int factorial(int n) {\n    if (n <= 1) return 1;\n    return n * factorial(n - 1);\n}',
    'syntax_breakdown': [ 'Focus on base case: identify what it represents and what role it plays in the statement.',
                          'Next inspect recursive case: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'static int factorial(int n) {\n    if (n <= 1) return 1;\n    return n * factorial(n - 1);\n}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'static int sumTo(int n){\n    if(n==0)return 0;\n    return n+sumTo(n-1);\n}',
    'example2_explanation': 'Change one meaningful input or rule related to recursion, predict the result, and only '
                            'then run the program.',
    'practical_example': 'Imagine a small recursion feature in a student or inventory application. Identify the '
                         'input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using base case without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls recursive case.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of base case in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Implement recursive factorial and sum, then identify base and recursive cases.',
    'practice_problem': '**Recursion independent practice:** Implement recursive factorial and sum, then identify base '
                        'and recursive cases. You must also add one clearly different variation and test it. Your work '
                        "should demonstrate the lesson's main rule, not merely reproduce Example 1.",
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
    'next_lesson': 'Searching, Sorting & Comparators',
    'rules': [ 'Explain the job of base case in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the recursion exercise.',
    'extension': 'Add one realistic requirement to the recursion exercise while keeping the original behavior correct.',
    'learning_checks': [ 'Can I explain recursion without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_31'],
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
    'independent_practice': 'Independently solve this **Recursion** task: Implement recursive factorial and sum, then '
                            'identify base and recursive cases. Then create one small variation that changes an input, '
                            'rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Recursion** program that exhibits this common mistake: **Using base '
                  'case without understanding whether it represents data, behavior, or a relationship.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
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
  { 'id': 'java_33',
    'title': 'Searching, Sorting & Comparators',
    'description': 'Compare linear and binary search, sort collections, and customize ordering with Comparator.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Searching, Sorting & Comparators**, understand why it is useful, '
                    'trace a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what searching, sorting & comparators means and why it exists.',
                             'Read and write the core syntax used for searching, sorting & comparators.',
                             'Predict the behavior of a small searching, sorting & comparators example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['search', 'sort', 'Comparator', 'ordering'],
    'explanation': 'Compare linear and binary search, sort collections, and customize ordering with Comparator. Java '
                   'syntax is shown using the standard library or language feature for this lesson. Pay attention to '
                   'the type, identifier, method call, object reference, and punctuation.',
    'syntax': 'List<String> names = new ArrayList<>(List.of("Mika","Ren","Aren"));\n'
              'names.sort(Comparator.comparingInt(String::length));',
    'syntax_breakdown': [ 'Focus on search: identify what it represents and what role it plays in the statement.',
                          'Next inspect sort: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'List<String> names = new ArrayList<>(List.of("Mika","Ren","Aren"));\n'
                'names.sort(Comparator.comparingInt(String::length));',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'names.sort(Comparator.comparingInt(String::length));\n'
                'int index=Collections.binarySearch(names,"Ren");\n'
                'System.out.println(index);',
    'example2_explanation': 'Change one meaningful input or rule related to searching, sorting & comparators, predict '
                            'the result, and only then run the program.',
    'practical_example': 'Imagine a small searching, sorting & comparators feature in a student or inventory '
                         'application. Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using search without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls sort.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of search in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Sort students by grade descending and name ascending, then search for a target.',
    'practice_problem': '**Searching, Sorting & Comparators independent practice:** Sort students by grade descending '
                        'and name ascending, then search for a target. You must also add one clearly different '
                        "variation and test it. Your work should demonstrate the lesson's main rule, not merely "
                        'reproduce Example 1.',
    'expected_output': '**Test contract for Searching, Sorting & Comparators:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Searching, Sorting & Comparators: What does sort do to a range?',
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
    'summary': 'You should now be able to explain searching, sorting & comparators, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Big-O & Complexity',
    'rules': [ 'Explain the job of search in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the searching, sorting '
            '& comparators exercise.',
    'extension': 'Add one realistic requirement to the searching, sorting & comparators exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain searching, sorting & comparators without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_32'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Searching, Sorting & Comparators matters because solving a problem correctly also requires '
                      'choosing an approach that scales and can be reasoned about.',
    'guided_practice': [ '1. Restate the goal of **Searching, Sorting & Comparators** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Searching, Sorting '
                         '& Comparators**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Searching, Sorting & Comparators** task: Sort students by '
                            'grade descending and name ascending, then search for a target. Then create one small '
                            'variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Searching, Sorting & Comparators** program that exhibits this common '
                  'mistake: **Using search without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Searching, Sorting & Comparators** to a small real-world feature. Keep the same core '
                     'rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what searching, sorting & comparators means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for searching, sorting & '
                                                 'comparators.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small searching, sorting & comparators '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Searching, Sorting & '
                                  'Comparators.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Searching, Sorting & Comparators without '
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
  { 'id': 'java_34',
    'title': 'Big-O & Complexity',
    'description': 'Estimate time and space growth and use complexity to choose between brute-force, indexed lookup, '
                   'sorting, and logarithmic search strategies.',
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
    'explanation': 'Estimate time and space growth and use complexity to choose between brute-force, indexed lookup, '
                   'sorting, and logarithmic search strategies. Java syntax is shown using the standard library or '
                   'language feature for this lesson. Pay attention to the type, identifier, method call, object '
                   'reference, and punctuation.',
    'syntax': 'for (int i = 0; i < n; i++) { System.out.println(i); }\n// O(n)',
    'syntax_breakdown': [ 'Focus on input size: identify what it represents and what role it plays in the statement.',
                          'Next inspect time complexity: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'for (int i = 0; i < n; i++) { System.out.println(i); }\n// O(n)',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'boolean contains(List<Integer> values,int target){\n'
                '    for(int x:values) if(x==target)return true;\n'
                '    return false;\n'
                '}\n'
                '// O(n) time',
    'example2_explanation': 'Change one meaningful input or rule related to big-o & complexity, predict the result, '
                            'and only then run the program.',
    'practical_example': 'Imagine a small big-o & complexity feature in a student or inventory application. Identify '
                         'the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using input size without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls time complexity.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of input size in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Compare nested loops, HashMap lookup, and binary search in terms of expected growth.',
    'practice_problem': '**Big-O & Complexity independent practice:** Compare nested loops, HashMap lookup, and binary '
                        'search in terms of expected growth. You must also add one clearly different variation and '
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
    'next_lesson': 'Testing with JUnit Concepts',
    'rules': [ 'Explain the job of input size in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the big-o & complexity '
            'exercise.',
    'extension': 'Add one realistic requirement to the big-o & complexity exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain big-o & complexity without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_33'],
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
    'independent_practice': 'Independently solve this **Big-O & Complexity** task: Compare nested loops, HashMap '
                            'lookup, and binary search in terms of expected growth. Then create one small variation '
                            'that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Big-O & Complexity** program that exhibits this common mistake: '
                  '**Using input size without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
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
  { 'id': 'java_35',
    'title': 'Testing with JUnit Concepts',
    'description': 'Understand unit-test structure, assertions, arrange-act-assert thinking, test isolation, edge '
                   'cases, and why tests document expected behavior.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Testing with JUnit Concepts**, understand why it is useful, trace '
                    'a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what testing with junit concepts means and why it exists.',
                             'Read and write the core syntax used for testing with junit concepts.',
                             'Predict the behavior of a small testing with junit concepts example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['test case', 'assertion', 'fixture', 'isolation'],
    'explanation': 'Understand unit-test structure, assertions, arrange-act-assert thinking, test isolation, edge '
                   'cases, and why tests document expected behavior. Java syntax is shown using the standard library '
                   'or language feature for this lesson. Pay attention to the type, identifier, method call, object '
                   'reference, and punctuation.',
    'syntax': '// Conceptual JUnit test\n@Test\nvoid addsNumbers() {\n    assertEquals(5, calculator.add(2,3));\n}',
    'syntax_breakdown': [ 'Focus on test case: identify what it represents and what role it plays in the statement.',
                          'Next inspect assertion: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '// Conceptual JUnit test\n@Test\nvoid addsNumbers() {\n    assertEquals(5, calculator.add(2,3));\n}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': '@Test\nvoid addsNumbers(){\n    assertEquals(5, calculator.add(2,3));\n}',
    'example2_explanation': 'Change one meaningful input or rule related to testing with junit concepts, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small testing with junit concepts feature in a student or inventory application. '
                         'Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using test case without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls assertion.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of test case in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Design unit tests for a grade classifier, including boundary and invalid cases.',
    'practice_problem': '**Testing with JUnit Concepts independent practice:** Design unit tests for a grade '
                        'classifier, including boundary and invalid cases. You must also add one clearly different '
                        "variation and test it. Your work should demonstrate the lesson's main rule, not merely "
                        'reproduce Example 1.',
    'expected_output': '**Test contract for Testing with JUnit Concepts:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Testing with JUnit Concepts: What should a debugger help you inspect?',
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
    'summary': 'You should now be able to explain testing with junit concepts, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Debugging & Error Analysis',
    'rules': [ 'Explain the job of test case in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the testing with junit '
            'concepts exercise.',
    'extension': 'Add one realistic requirement to the testing with junit concepts exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain testing with junit concepts without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_34'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Testing with JUnit Concepts matters because confidence comes from evidence: repeatable tests, '
                      'clear failures, and validation of edge cases.',
    'guided_practice': [ '1. Restate the goal of **Testing with JUnit Concepts** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Testing with JUnit '
                         'Concepts**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Testing with JUnit Concepts** task: Design unit tests for a '
                            'grade classifier, including boundary and invalid cases. Then create one small variation '
                            'that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Testing with JUnit Concepts** program that exhibits this common '
                  'mistake: **Using test case without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Testing with JUnit Concepts** to a small real-world feature. Keep the same core rule, '
                     'but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what testing with junit concepts means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for testing with junit concepts.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small testing with junit concepts example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Testing with JUnit Concepts.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Testing with JUnit Concepts without violating '
                                  'the stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['testing', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_36',
    'title': 'Debugging & Error Analysis',
    'description': 'Classify compile, runtime, and logic failures, read stack traces, inspect state, reproduce bugs, '
                   'and fix root causes.',
    'stage': 'Algorithms & Engineering',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Debugging & Error Analysis**, understand why it is useful, trace '
                    'a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what debugging & error analysis means and why it exists.',
                             'Read and write the core syntax used for debugging & error analysis.',
                             'Predict the behavior of a small debugging & error analysis example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['stack trace', 'breakpoint', 'runtime state', 'root cause'],
    'explanation': 'Classify compile, runtime, and logic failures, read stack traces, inspect state, reproduce bugs, '
                   'and fix root causes. Java syntax is shown using the standard library or language feature for this '
                   'lesson. Pay attention to the type, identifier, method call, object reference, and punctuation.',
    'syntax': 'int total = price * quantity;\n// Set a breakpoint here and inspect price, quantity, total.',
    'syntax_breakdown': [ 'Focus on stack trace: identify what it represents and what role it plays in the statement.',
                          'Next inspect breakpoint: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'int total = price * quantity;\n// Set a breakpoint here and inspect price, quantity, total.',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'int total=price*quantity;\n'
                '// Set a breakpoint here and inspect both operands before the multiplication.',
    'example2_explanation': 'Change one meaningful input or rule related to debugging & error analysis, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small debugging & error analysis feature in a student or inventory application. '
                         'Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using stack trace without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls breakpoint.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of stack trace in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Given a failing method, write a reproduction case and identify the first incorrect state.',
    'practice_problem': '**Debugging & Error Analysis independent practice:** Given a failing method, write a '
                        'reproduction case and identify the first incorrect state. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Debugging & Error Analysis:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Debugging & Error Analysis: What should a debugger help you inspect?',
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
    'summary': 'You should now be able to explain debugging & error analysis, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'JDBC & Database Concepts',
    'rules': [ 'Explain the job of stack trace in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the debugging & error '
            'analysis exercise.',
    'extension': 'Add one realistic requirement to the debugging & error analysis exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain debugging & error analysis without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_35'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Debugging & Error Analysis matters because useful programs must detect, explain, and recover '
                      'from incorrect states instead of silently failing.',
    'guided_practice': [ '1. Restate the goal of **Debugging & Error Analysis** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Debugging & Error '
                         'Analysis**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Debugging & Error Analysis** task: Given a failing method, '
                            'write a reproduction case and identify the first incorrect state. Then create one small '
                            'variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Debugging & Error Analysis** program that exhibits this common '
                  'mistake: **Using stack trace without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Debugging & Error Analysis** to a small real-world feature. Keep the same core rule, '
                     'but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what debugging & error analysis means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for debugging & error analysis.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small debugging & error analysis example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Debugging & Error Analysis.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Debugging & Error Analysis without violating '
                                  'the stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['error', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_37',
    'title': 'JDBC & Database Concepts',
    'description': 'Understand the JDBC flow: connection, prepared statement, parameters, execution, result sets, '
                   'transactions, and resource cleanup.',
    'stage': 'Algorithms & Engineering',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **JDBC & Database Concepts**, understand why it is useful, trace a '
                    'focused example, practice it with guidance, then solve an independent variation. You will finish '
                    'by proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what jdbc & database concepts means and why it exists.',
                             'Read and write the core syntax used for jdbc & database concepts.',
                             'Predict the behavior of a small jdbc & database concepts example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['Connection', 'PreparedStatement', 'ResultSet', 'transaction'],
    'explanation': 'Understand the JDBC flow: connection, prepared statement, parameters, execution, result sets, '
                   'transactions, and resource cleanup. Java syntax is shown using the standard library or language '
                   'feature for this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'String sql = "SELECT name FROM students WHERE id = ?";\n'
              'try (PreparedStatement ps = connection.prepareStatement(sql)) {\n'
              '    ps.setInt(1, id);\n'
              '}',
    'syntax_breakdown': [ 'Focus on Connection: identify what it represents and what role it plays in the statement.',
                          'Next inspect PreparedStatement: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'String sql = "SELECT name FROM students WHERE id = ?";\n'
                'try (PreparedStatement ps = connection.prepareStatement(sql)) {\n'
                '    ps.setInt(1, id);\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'String sql="SELECT name FROM students WHERE id=?";\n'
                'try(PreparedStatement ps=connection.prepareStatement(sql)){\n'
                '    ps.setInt(1,id);\n'
                '}',
    'example2_explanation': 'Change one meaningful input or rule related to jdbc & database concepts, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small jdbc & database concepts feature in a student or inventory application. '
                         'Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using Connection without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls PreparedStatement.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of Connection in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Explain how a parameterized query avoids string concatenation and how try-with-resources manages JDBC '
                'resources.',
    'practice_problem': '**JDBC & Database Concepts independent practice:** Explain how a parameterized query avoids '
                        'string concatenation and how try-with-resources manages JDBC resources. You must also add one '
                        "clearly different variation and test it. Your work should demonstrate the lesson's main rule, "
                        'not merely reproduce Example 1.',
    'expected_output': '**Test contract for JDBC & Database Concepts:** Run the program with a normal case, a boundary '
                       'case, and a misuse/invalid case when relevant. For each case, record the actual result and '
                       'compare it with the requirement. A correct submission must preserve the lesson rule and handle '
                       'the defined edge case safely.',
    'mastery_quiz': [ [ 'JDBC & Database Concepts: What does a concept describe?',
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
    'summary': 'You should now be able to explain jdbc & database concepts, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Data Structures: Stack, Queue & Deque',
    'rules': [ 'Explain the job of Connection in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the jdbc & database '
            'concepts exercise.',
    'extension': 'Add one realistic requirement to the jdbc & database concepts exercise while keeping the original '
                 'behavior correct.',
    'learning_checks': [ 'Can I explain jdbc & database concepts without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_36'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'JDBC & Database Concepts matters because applications need reliable ways to store, query, and '
                      'update persistent data.',
    'guided_practice': [ '1. Restate the goal of **JDBC & Database Concepts** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **JDBC & Database '
                         'Concepts**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **JDBC & Database Concepts** task: Explain how a parameterized '
                            'query avoids string concatenation and how try-with-resources manages JDBC resources. Then '
                            'create one small variation that changes an input, rule, or data case without changing the '
                            'main goal.',
    'debug_task': 'Debug a deliberately small **JDBC & Database Concepts** program that exhibits this common mistake: '
                  '**Using Connection without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **JDBC & Database Concepts** to a small real-world feature. Keep the same core rule, '
                     'but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what jdbc & database concepts means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for jdbc & database concepts.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small jdbc & database concepts example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for JDBC & Database Concepts.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for JDBC & Database Concepts without violating the '
                                  'stated rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['database', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_38',
    'title': 'Data Structures: Stack, Queue & Deque',
    'description': 'Choose LIFO or FIFO structures for undo history, service order, and double-ended processing.',
    'stage': 'Algorithms & Engineering',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Data Structures: Stack, Queue & Deque**, understand why it is '
                    'useful, trace a focused example, practice it with guidance, then solve an independent variation. '
                    'You will finish by proving your understanding through concept, syntax, code-reading, debugging, '
                    'and application checks.',
    'learning_objectives': [ 'Explain what data structures: stack, queue & deque means and why it exists.',
                             'Read and write the core syntax used for data structures: stack, queue & deque.',
                             'Predict the behavior of a small data structures: stack, queue & deque example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['LIFO', 'FIFO', 'deque', 'front'],
    'explanation': 'Choose LIFO or FIFO structures for undo history, service order, and double-ended processing. Java '
                   'syntax is shown using the standard library or language feature for this lesson. Pay attention to '
                   'the type, identifier, method call, object reference, and punctuation.',
    'syntax': 'Deque<Integer> deque = new ArrayDeque<>();\n'
              'deque.addLast(10);\n'
              'deque.addLast(20);\n'
              'System.out.println(deque.removeFirst());',
    'syntax_breakdown': [ 'Focus on LIFO: identify what it represents and what role it plays in the statement.',
                          'Next inspect FIFO: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'Deque<Integer> deque = new ArrayDeque<>();\n'
                'deque.addLast(10);\n'
                'deque.addLast(20);\n'
                'System.out.println(deque.removeFirst());',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'Deque<Integer> deque=new ArrayDeque<>();\n'
                'deque.addLast(10); deque.addLast(20);\n'
                'System.out.println(deque.removeFirst());',
    'example2_explanation': 'Change one meaningful input or rule related to data structures: stack, queue & deque, '
                            'predict the result, and only then run the program.',
    'practical_example': 'Imagine a small data structures: stack, queue & deque feature in a student or inventory '
                         'application. Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using LIFO without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls FIFO.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of LIFO in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Model browser back history with a stack-like deque and a customer queue with FIFO behavior.',
    'practice_problem': '**Data Structures: Stack, Queue & Deque independent practice:** Model browser back history '
                        'with a stack-like deque and a customer queue with FIFO behavior. You must also add one '
                        "clearly different variation and test it. Your work should demonstrate the lesson's main rule, "
                        'not merely reproduce Example 1.',
    'expected_output': '**Test contract for Data Structures: Stack, Queue & Deque:** Run the program with a normal '
                       'case, a boundary case, and a misuse/invalid case when relevant. For each case, record the '
                       'actual result and compare it with the requirement. A correct submission must preserve the '
                       'lesson rule and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Data Structures: Stack, Queue & Deque: Which behavior is central to Data Structures: Stack, '
                        'Queue & Deque?',
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
    'summary': 'You should now be able to explain data structures: stack, queue & deque, recognize its syntax, trace '
               'the worked example, and use the concept in a small original program.',
    'next_lesson': 'Trees, Heaps & Priority Queues',
    'rules': [ 'Explain the job of LIFO in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the data structures: '
            'stack, queue & deque exercise.',
    'extension': 'Add one realistic requirement to the data structures: stack, queue & deque exercise while keeping '
                 'the original behavior correct.',
    'learning_checks': [ 'Can I explain data structures: stack, queue & deque without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_37'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Data Structures: Stack, Queue & Deque matters because programs often need to store, find, '
                      'update, and process groups of related values.',
    'guided_practice': [ '1. Restate the goal of **Data Structures: Stack, Queue & Deque** in one sentence before '
                         'writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Data Structures: '
                         'Stack, Queue & Deque**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Data Structures: Stack, Queue & Deque** task: Model browser '
                            'back history with a stack-like deque and a customer queue with FIFO behavior. Then create '
                            'one small variation that changes an input, rule, or data case without changing the main '
                            'goal.',
    'debug_task': 'Debug a deliberately small **Data Structures: Stack, Queue & Deque** program that exhibits this '
                  'common mistake: **Using LIFO without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Data Structures: Stack, Queue & Deque** to a small real-world feature. Keep the same '
                     'core rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what data structures: stack, queue & deque means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for data structures: stack, '
                                                 'queue & deque.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small data structures: stack, queue & '
                                                 'deque example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Data Structures: Stack, Queue & '
                                  'Deque.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Data Structures: Stack, Queue & Deque without '
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
  { 'id': 'java_39',
    'title': 'Trees, Heaps & Priority Queues',
    'description': 'Understand hierarchical data, binary-tree terminology, heap ordering, and priority queues for '
                   'repeatedly selecting the next most important item.',
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
    'explanation': 'Understand hierarchical data, binary-tree terminology, heap ordering, and priority queues for '
                   'repeatedly selecting the next most important item. Java syntax is shown using the standard library '
                   'or language feature for this lesson. Pay attention to the type, identifier, method call, object '
                   'reference, and punctuation.',
    'syntax': 'PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());\n'
              'pq.add(4); pq.add(9); pq.add(2);\n'
              'System.out.println(pq.poll());',
    'syntax_breakdown': [ 'Focus on node: identify what it represents and what role it plays in the statement.',
                          'Next inspect heap: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());\n'
                'pq.add(4); pq.add(9); pq.add(2);\n'
                'System.out.println(pq.poll());',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'Deque<Integer> deque=new ArrayDeque<>();\n'
                'deque.addLast(10); deque.addLast(20);\n'
                'System.out.println(deque.removeFirst());',
    'example2_explanation': 'Change one meaningful input or rule related to trees, heaps & priority queues, predict '
                            'the result, and only then run the program.',
    'practical_example': 'Imagine a small trees, heaps & priority queues feature in a student or inventory '
                         'application. Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using node without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls heap.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of node in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Process support tickets by priority and explain the heap property behind PriorityQueue.',
    'practice_problem': '**Trees, Heaps & Priority Queues independent practice:** Process support tickets by priority '
                        'and explain the heap property behind PriorityQueue. You must also add one clearly different '
                        "variation and test it. Your work should demonstrate the lesson's main rule, not merely "
                        'reproduce Example 1.',
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
    'rules': [ 'Explain the job of node in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the trees, heaps & '
            'priority queues exercise.',
    'extension': 'Add one realistic requirement to the trees, heaps & priority queues exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain trees, heaps & priority queues without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_38'],
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
                            'by priority and explain the heap property behind PriorityQueue. Then create one small '
                            'variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Trees, Heaps & Priority Queues** program that exhibits this common '
                  'mistake: **Using node without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
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
  { 'id': 'java_40',
    'title': 'Graphs & Traversal',
    'description': 'Represent relationships with adjacency structures and reason about breadth-first and depth-first '
                   'traversal.',
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
    'explanation': 'Represent relationships with adjacency structures and reason about breadth-first and depth-first '
                   'traversal. Java syntax is shown using the standard library or language feature for this lesson. '
                   'Pay attention to the type, identifier, method call, object reference, and punctuation.',
    'syntax': 'Map<Integer,List<Integer>> graph = Map.of(0,List.of(1,2),1,List.of(0,3),2,List.of(0,3),3,List.of(1,2));',
    'syntax_breakdown': [ 'Focus on vertex: identify what it represents and what role it plays in the statement.',
                          'Next inspect edge: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'Map<Integer,List<Integer>> graph = '
                'Map.of(0,List.of(1,2),1,List.of(0,3),2,List.of(0,3),3,List.of(1,2));',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'Map<Integer,List<Integer>> '
                'graph=Map.of(0,List.of(1,2),1,List.of(0,3),2,List.of(0,3),3,List.of(1,2));\n'
                'System.out.println(graph);',
    'example2_explanation': 'Change one meaningful input or rule related to graphs & traversal, predict the result, '
                            'and only then run the program.',
    'practical_example': 'Imagine a small graphs & traversal feature in a student or inventory application. Identify '
                         'the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using vertex without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls edge.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of vertex in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Represent a campus map and describe BFS and DFS from a starting building.',
    'practice_problem': '**Graphs & Traversal independent practice:** Represent a campus map and describe BFS and DFS '
                        'from a starting building. You must also add one clearly different variation and test it. Your '
                        "work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
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
    'next_lesson': 'Problem Decomposition & Validation',
    'rules': [ 'Explain the job of vertex in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the graphs & traversal '
            'exercise.',
    'extension': 'Add one realistic requirement to the graphs & traversal exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain graphs & traversal without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_39'],
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
    'independent_practice': 'Independently solve this **Graphs & Traversal** task: Represent a campus map and describe '
                            'BFS and DFS from a starting building. Then create one small variation that changes an '
                            'input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Graphs & Traversal** program that exhibits this common mistake: '
                  '**Using vertex without understanding whether it represents data, behavior, or a relationship.**. '
                  'Before changing code, identify the first incorrect value, state, control-flow decision, or '
                  'ownership assumption; then explain the fix in one sentence.',
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
  { 'id': 'java_41',
    'title': 'Problem Decomposition & Validation',
    'description': 'Translate a written requirement into inputs, state, rules, validation, processing, outputs, and '
                   'test cases before coding.',
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
    'explanation': 'Translate a written requirement into inputs, state, rules, validation, processing, outputs, and '
                   'test cases before coding. Java syntax is shown using the standard library or language feature for '
                   'this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'record Rule(String input, String condition, String result) {}',
    'syntax_breakdown': [ 'Focus on input: identify what it represents and what role it plays in the statement.',
                          'Next inspect rule: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'record Rule(String input, String condition, String result) {}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'class Battery { int level=100; }\n'
                'class Phone {\n'
                '    private final Battery battery=new Battery();\n'
                '    int level(){ return battery.level; }\n'
                '}',
    'example2_explanation': 'Change one meaningful input or rule related to problem decomposition & validation, '
                            'predict the result, and only then run the program.',
    'practical_example': 'Imagine a small problem decomposition & validation feature in a student or inventory '
                         'application. Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using input without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls rule.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of input in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Break a ticketing or inventory specification into a validation checklist and edge cases.',
    'practice_problem': '**Problem Decomposition & Validation independent practice:** Break a ticketing or inventory '
                        'specification into a validation checklist and edge cases. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
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
    'next_lesson': 'Capstone & Practical Exam Readiness',
    'rules': [ 'Explain the job of input in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the problem '
            'decomposition & validation exercise.',
    'extension': 'Add one realistic requirement to the problem decomposition & validation exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain problem decomposition & validation without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_40'],
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
    'independent_practice': 'Independently solve this **Problem Decomposition & Validation** task: Break a ticketing '
                            'or inventory specification into a validation checklist and edge cases. Then create one '
                            'small variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Problem Decomposition & Validation** program that exhibits this common '
                  'mistake: **Using input without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
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
  { 'id': 'java_42',
    'title': 'Capstone & Practical Exam Readiness',
    'description': 'Plan, implement, test, debug, document, and explain a complete Java console application from a '
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
    'explanation': 'Plan, implement, test, debug, document, and explain a complete Java console application from a '
                   'detailed specification. Java syntax is shown using the standard library or language feature for '
                   'this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'public static void main(String[] args) {\n    // parse -> validate -> process -> report\n}',
    'syntax_breakdown': [ 'Focus on requirements: identify what it represents and what role it plays in the statement.',
                          'Next inspect architecture: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'public static void main(String[] args) {\n    // parse -> validate -> process -> report\n}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': '// Focused Capstone & Practical Exam Readiness example\n'
                'System.out.println("Practice the lesson concept");',
    'example2_explanation': 'Change one meaningful input or rule related to capstone & practical exam readiness, '
                            'predict the result, and only then run the program.',
    'practical_example': 'Imagine a small capstone & practical exam readiness feature in a student or inventory '
                         'application. Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using requirements without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls architecture.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of requirements in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Build a complete console system using OOP, collections, validation, persistence where appropriate, '
                'and tests.',
    'practice_problem': '**Capstone & Practical Exam Readiness independent practice:** Build a complete console system '
                        'using OOP, collections, validation, persistence where appropriate, and tests. You must also '
                        "add one clearly different variation and test it. Your work should demonstrate the lesson's "
                        'main rule, not merely reproduce Example 1.',
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
    'next_lesson': 'Packages & Project Structure',
    'rules': [ 'Explain the job of requirements in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the capstone & '
            'practical exam readiness exercise.',
    'extension': 'Add one realistic requirement to the capstone & practical exam readiness exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain capstone & practical exam readiness without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_41'],
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
                            'console system using OOP, collections, validation, persistence where appropriate, and '
                            'tests. Then create one small variation that changes an input, rule, or data case without '
                            'changing the main goal.',
    'debug_task': 'Debug a deliberately small **Capstone & Practical Exam Readiness** program that exhibits this '
                  'common mistake: **Using requirements without understanding whether it represents data, behavior, or '
                  'a relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
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
  { 'id': 'java_43',
    'title': 'Packages & Project Structure',
    'description': 'Organize Java code into packages, understand imports and access boundaries, and create a '
                   'maintainable source tree.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Packages & Project Structure**, understand why it is useful, '
                    'trace a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what packages & project structure means and why it exists.',
                             'Read and write the core syntax used for packages & project structure.',
                             'Predict the behavior of a small packages & project structure example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['package', 'import', 'visibility', 'source tree'],
    'explanation': 'Organize Java code into packages, understand imports and access boundaries, and create a '
                   'maintainable source tree. Java syntax is shown using the standard library or language feature for '
                   'this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'package school.model;\n\npublic class Student {\n    // model code\n}',
    'syntax_breakdown': [ 'Focus on package: identify what it represents and what role it plays in the statement.',
                          'Next inspect import: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'package school.model;\n\npublic class Student {\n    // model code\n}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'package school.model;\n'
                '\n'
                'public class Student {\n'
                '    private final String name;\n'
                '    public Student(String name){this.name=name;}\n'
                '}',
    'example2_explanation': 'Change one meaningful input or rule related to packages & project structure, predict the '
                            'result, and only then run the program.',
    'practical_example': 'Imagine a small packages & project structure feature in a student or inventory application. '
                         'Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using package without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls import.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of package in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Split a small application into model, service, and app packages and explain their responsibilities.',
    'practice_problem': '**Packages & Project Structure independent practice:** Split a small application into model, '
                        'service, and app packages and explain their responsibilities. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Packages & Project Structure:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Packages & Project Structure: Why use packages?',
                        [ 'To organize types and control naming/access boundaries',
                          'To create loops',
                          'To allocate arrays',
                          'To replace the JVM'],
                        0,
                        'Packages organize related types and namespaces.'],
                      [ 'What does import do?',
                        [ 'Makes another package type available by simple name',
                          'Creates a class',
                          'Starts a thread',
                          'Writes a file'],
                        0,
                        'Imports allow shorter references to types.'],
                      [ 'Why separate model/service/app packages?',
                        [ 'To give different responsibilities clear boundaries',
                          'To make all fields public',
                          'To remove tests',
                          'To avoid compilation'],
                        0,
                        'Package structure can make responsibilities easier to maintain.'],
                      [ 'What is package-private access?',
                        [ 'Accessible within the same package when no public/protected/private modifier is used',
                          'Accessible everywhere',
                          'Accessible only to subclasses',
                          'Accessible only to the JVM'],
                        0,
                        'Default access is package-private.'],
                      [ 'What should a project structure communicate?',
                        ['Responsibilities and dependencies', 'Only file size', 'Only variable names', 'Only comments'],
                        0,
                        'A good structure makes the system easier to navigate.']],
    'summary': 'You should now be able to explain packages & project structure, recognize its syntax, trace the worked '
               'example, and use the concept in a small original program.',
    'next_lesson': 'Nested Classes & Object Lifecycle',
    'rules': [ 'Explain the job of package in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the packages & project '
            'structure exercise.',
    'extension': 'Add one realistic requirement to the packages & project structure exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain packages & project structure without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_42'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Packages & Project Structure matters because real projects require requirements, design '
                      'decisions, testing, maintainability, and trade-off awareness.',
    'guided_practice': [ '1. Restate the goal of **Packages & Project Structure** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Packages & Project '
                         'Structure**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Packages & Project Structure** task: Split a small application '
                            'into model, service, and app packages and explain their responsibilities. Then create one '
                            'small variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Packages & Project Structure** program that exhibits this common '
                  'mistake: **Using package without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Packages & Project Structure** to a small real-world feature. Keep the same core '
                     'rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what packages & project structure means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for packages & project '
                                                 'structure.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small packages & project structure '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Packages & Project Structure.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Packages & Project Structure without violating '
                                  'the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Packages & '
                                  'Project Structure.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['engineering', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_44',
    'title': 'Nested Classes & Object Lifecycle',
    'description': 'Understand static nested classes, inner classes, object creation, initialization order, and the '
                   'lifetime of referenced objects.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Nested Classes & Object Lifecycle**, understand why it is useful, '
                    'trace a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what nested classes & object lifecycle means and why it exists.',
                             'Read and write the core syntax used for nested classes & object lifecycle.',
                             'Predict the behavior of a small nested classes & object lifecycle example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['nested class', 'inner class', 'initialization', 'lifetime'],
    'explanation': 'Understand static nested classes, inner classes, object creation, initialization order, and the '
                   'lifetime of referenced objects. Java syntax is shown using the standard library or language '
                   'feature for this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'class Outer {\n    static class Helper { }\n    class Inner { }\n}',
    'syntax_breakdown': [ 'Focus on nested class: identify what it represents and what role it plays in the statement.',
                          'Next inspect inner class: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'class Outer {\n    static class Helper { }\n    class Inner { }\n}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'class Lamp {\n    boolean on;\n    void toggle(){ on=!on; }\n}\nLamp lamp=new Lamp(); lamp.toggle();',
    'example2_explanation': 'Change one meaningful input or rule related to nested classes & object lifecycle, predict '
                            'the result, and only then run the program.',
    'practical_example': 'Imagine a small nested classes & object lifecycle feature in a student or inventory '
                         'application. Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using nested class without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls inner class.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of nested class in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Create a nested helper that does not need an Outer instance and explain why it can be static.',
    'practice_problem': '**Nested Classes & Object Lifecycle independent practice:** Create a nested helper that does '
                        'not need an Outer instance and explain why it can be static. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Nested Classes & Object Lifecycle:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Nested Classes & Object Lifecycle: What is the main design idea in Nested Classes & Object '
                        'Lifecycle?',
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
    'summary': 'You should now be able to explain nested classes & object lifecycle, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Immutability & Defensive Design',
    'rules': [ 'Explain the job of nested class in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the nested classes & '
            'object lifecycle exercise.',
    'extension': 'Add one realistic requirement to the nested classes & object lifecycle exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain nested classes & object lifecycle without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_43'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Nested Classes & Object Lifecycle matters because larger programs need clear ownership of state '
                      'and behavior and predictable relationships between types.',
    'guided_practice': [ '1. Restate the goal of **Nested Classes & Object Lifecycle** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Nested Classes & '
                         'Object Lifecycle**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Nested Classes & Object Lifecycle** task: Create a nested '
                            'helper that does not need an Outer instance and explain why it can be static. Then create '
                            'one small variation that changes an input, rule, or data case without changing the main '
                            'goal.',
    'debug_task': 'Debug a deliberately small **Nested Classes & Object Lifecycle** program that exhibits this common '
                  'mistake: **Using nested class without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Nested Classes & Object Lifecycle** to a small real-world feature. Keep the same core '
                     'rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what nested classes & object lifecycle means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for nested classes & object '
                                                 'lifecycle.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small nested classes & object lifecycle '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Nested Classes & Object '
                                  'Lifecycle.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Nested Classes & Object Lifecycle without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Nested Classes '
                                  '& Object Lifecycle.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['oop', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_45',
    'title': 'Immutability & Defensive Design',
    'description': 'Design objects whose state cannot be changed after construction, use final fields, defensive '
                   'copies, and distinguish immutable values from mutable references.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Immutability & Defensive Design**, understand why it is useful, '
                    'trace a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what immutability & defensive design means and why it exists.',
                             'Read and write the core syntax used for immutability & defensive design.',
                             'Predict the behavior of a small immutability & defensive design example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['immutable', 'final', 'defensive copy', 'aliasing'],
    'explanation': 'Design objects whose state cannot be changed after construction, use final fields, defensive '
                   'copies, and distinguish immutable values from mutable references. Java syntax is shown using the '
                   'standard library or language feature for this lesson. Pay attention to the type, identifier, '
                   'method call, object reference, and punctuation.',
    'syntax': 'public final class Point {\n'
              '    private final int x;\n'
              '    private final int y;\n'
              '    public Point(int x,int y){ this.x=x; this.y=y; }\n'
              '}',
    'syntax_breakdown': [ 'Focus on immutable: identify what it represents and what role it plays in the statement.',
                          'Next inspect final: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'public final class Point {\n'
                '    private final int x;\n'
                '    private final int y;\n'
                '    public Point(int x,int y){ this.x=x; this.y=y; }\n'
                '}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'public final class Point {\n'
                '    private final int x;\n'
                '    Point(int x){this.x=x;}\n'
                '    int x(){return x;}\n'
                '}',
    'example2_explanation': 'Change one meaningful input or rule related to immutability & defensive design, predict '
                            'the result, and only then run the program.',
    'practical_example': 'Imagine a small immutability & defensive design feature in a student or inventory '
                         'application. Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using immutable without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls final.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of immutable in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Design an immutable StudentProfile and explain what happens when it contains a mutable List.',
    'practice_problem': '**Immutability & Defensive Design independent practice:** Design an immutable StudentProfile '
                        'and explain what happens when it contains a mutable List. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Immutability & Defensive Design:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Immutability & Defensive Design: What is an immutable object?',
                        [ 'Its observable state cannot be changed after construction',
                          'It has no fields',
                          'It cannot be referenced',
                          'It is always a primitive'],
                        0,
                        'Immutable objects do not expose state-changing operations.'],
                      [ 'Why make fields final?',
                        [ 'To prevent reassignment after initialization',
                          'To make them global',
                          'To allocate them on the stack',
                          'To disable constructors'],
                        0,
                        'final fields can be assigned once.'],
                      [ 'What is a defensive copy?',
                        [ 'A separate copy that prevents callers from mutating internal mutable state',
                          'A compiler backup',
                          'A thread clone',
                          'A file copy only'],
                        0,
                        'Defensive copies protect encapsulated mutable data.'],
                      [ 'Why can an immutable object be easier to share?',
                        [ 'Its state cannot unexpectedly change',
                          'It never uses memory',
                          'It cannot be garbage collected',
                          'It has no methods'],
                        0,
                        'Immutable state reduces coordination needs.'],
                      [ 'What is a common immutability trap?',
                        [ 'Returning a mutable internal collection directly',
                          'Using final fields',
                          'Using private fields',
                          'Copying mutable input'],
                        0,
                        'Returning internal mutable state can break immutability.']],
    'summary': 'You should now be able to explain immutability & defensive design, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Date & Time API',
    'rules': [ 'Explain the job of immutable in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the immutability & '
            'defensive design exercise.',
    'extension': 'Add one realistic requirement to the immutability & defensive design exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain immutability & defensive design without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_44'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Immutability & Defensive Design gives you the foundation needed to read, change, and reason '
                      'about a program before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Immutability & Defensive Design** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Immutability & '
                         'Defensive Design**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Immutability & Defensive Design** task: Design an immutable '
                            'StudentProfile and explain what happens when it contains a mutable List. Then create one '
                            'small variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Immutability & Defensive Design** program that exhibits this common '
                  'mistake: **Using immutable without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Immutability & Defensive Design** to a small real-world feature. Keep the same core '
                     'rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what immutability & defensive design means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for immutability & defensive '
                                                 'design.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small immutability & defensive design '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Immutability & Defensive '
                                  'Design.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Immutability & Defensive Design without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Immutability & '
                                  'Defensive Design.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_46',
    'title': 'Date & Time API',
    'description': 'Use java.time types such as LocalDate, LocalTime, LocalDateTime, Duration, Period, formatting, and '
                   'parsing instead of legacy date classes.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Date & Time API**, understand why it is useful, trace a focused '
                    'example, practice it with guidance, then solve an independent variation. You will finish by '
                    'proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what date & time api means and why it exists.',
                             'Read and write the core syntax used for date & time api.',
                             'Predict the behavior of a small date & time api example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['LocalDate', 'LocalDateTime', 'Duration', 'Period'],
    'explanation': 'Use java.time types such as LocalDate, LocalTime, LocalDateTime, Duration, Period, formatting, and '
                   'parsing instead of legacy date classes. Java syntax is shown using the standard library or '
                   'language feature for this lesson. Pay attention to the type, identifier, method call, object '
                   'reference, and punctuation.',
    'syntax': 'LocalDate start = LocalDate.of(2026, 10, 1);\n'
              'LocalDate due = start.plusDays(7);\n'
              'System.out.println(due);',
    'syntax_breakdown': [ 'Focus on LocalDate: identify what it represents and what role it plays in the statement.',
                          'Next inspect LocalDateTime: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'LocalDate start = LocalDate.of(2026, 10, 1);\n'
                'LocalDate due = start.plusDays(7);\n'
                'System.out.println(due);',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'LocalDate start=LocalDate.of(2026,10,1);\nSystem.out.println(start.plusDays(7));',
    'example2_explanation': 'Change one meaningful input or rule related to date & time api, predict the result, and '
                            'only then run the program.',
    'practical_example': 'Imagine a small date & time api feature in a student or inventory application. Identify the '
                         'input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using LocalDate without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls LocalDateTime.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of LocalDate in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Calculate a due date, format it for display, and compute a duration between two times.',
    'practice_problem': '**Date & Time API independent practice:** Calculate a due date, format it for display, and '
                        'compute a duration between two times. You must also add one clearly different variation and '
                        "test it. Your work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Date & Time API:** Run the program with a normal case, a boundary case, '
                       'and a misuse/invalid case when relevant. For each case, record the actual result and compare '
                       'it with the requirement. A correct submission must preserve the lesson rule and handle the '
                       'defined edge case safely.',
    'mastery_quiz': [ [ 'Date & Time API: Which Java type represents a date without a time?',
                        ['LocalDate', 'LocalTime', 'Duration', 'Period'],
                        0,
                        'LocalDate stores a date.'],
                      [ 'Which type represents a time without a date?',
                        ['LocalTime', 'LocalDate', 'Period', 'Path'],
                        0,
                        'LocalTime stores a time of day.'],
                      [ 'What does Period model?',
                        ['Date-based amounts such as days/months/years', 'CPU time only', 'File size', 'A thread'],
                        0,
                        'Period is date-based.'],
                      [ 'What does Duration model?',
                        ['A time-based amount', 'A package', 'A date only', 'A collection'],
                        0,
                        'Duration measures elapsed time-based amounts.'],
                      [ 'Why use java.time instead of legacy Date APIs for new code?',
                        [ 'It provides clearer modern types and APIs',
                          'It removes all exceptions',
                          'It only works on Windows',
                          'It disables formatting'],
                        0,
                        'java.time offers a more coherent modern date/time model.']],
    'summary': 'You should now be able to explain date & time api, recognize its syntax, trace the worked example, and '
               'use the concept in a small original program.',
    'next_lesson': 'NIO Files & Paths',
    'rules': [ 'Explain the job of LocalDate in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the date & time api '
            'exercise.',
    'extension': 'Add one realistic requirement to the date & time api exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain date & time api without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_45'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Date & Time API gives you the foundation needed to read, change, and reason about a program '
                      'before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Date & Time API** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Date & Time API**, '
                         'then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Date & Time API** task: Calculate a due date, format it for '
                            'display, and compute a duration between two times. Then create one small variation that '
                            'changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Date & Time API** program that exhibits this common mistake: **Using '
                  'LocalDate without understanding whether it represents data, behavior, or a relationship.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Date & Time API** to a small real-world feature. Keep the same core rule, but change '
                     'the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what date & time api means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for date & time api.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small date & time api example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Date & Time API.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Date & Time API without violating the stated '
                                  'rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Date & Time '
                                  'API.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_47',
    'title': 'NIO Files & Paths',
    'description': 'Work with Path and Files for directory traversal, copying, moving, reading, writing, and metadata '
                   'while handling I/O exceptions.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **NIO Files & Paths**, understand why it is useful, trace a focused '
                    'example, practice it with guidance, then solve an independent variation. You will finish by '
                    'proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what nio files & paths means and why it exists.',
                             'Read and write the core syntax used for nio files & paths.',
                             'Predict the behavior of a small nio files & paths example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['Path', 'Files', 'directory', 'I/O exception'],
    'explanation': 'Work with Path and Files for directory traversal, copying, moving, reading, writing, and metadata '
                   'while handling I/O exceptions. Java syntax is shown using the standard library or language feature '
                   'for this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'Path folder = Path.of("data");\n'
              'Files.createDirectories(folder);\n'
              'Files.writeString(folder.resolve("notes.txt"), "hello");',
    'syntax_breakdown': [ 'Focus on Path: identify what it represents and what role it plays in the statement.',
                          'Next inspect Files: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'Path folder = Path.of("data");\n'
                'Files.createDirectories(folder);\n'
                'Files.writeString(folder.resolve("notes.txt"), "hello");',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'Path path=Path.of("notes.txt");\n'
                'Files.writeString(path,"hello");\n'
                'System.out.println(Files.readString(path));',
    'example2_explanation': 'Change one meaningful input or rule related to nio files & paths, predict the result, and '
                            'only then run the program.',
    'practical_example': 'Imagine a small nio files & paths feature in a student or inventory application. Identify '
                         'the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using Path without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls Files.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of Path in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Create a data directory, write a file, list its contents, and explain why Path is preferred over raw '
                'string paths.',
    'practice_problem': '**NIO Files & Paths independent practice:** Create a data directory, write a file, list its '
                        'contents, and explain why Path is preferred over raw string paths. You must also add one '
                        "clearly different variation and test it. Your work should demonstrate the lesson's main rule, "
                        'not merely reproduce Example 1.',
    'expected_output': '**Test contract for NIO Files & Paths:** Run the program with a normal case, a boundary case, '
                       'and a misuse/invalid case when relevant. For each case, record the actual result and compare '
                       'it with the requirement. A correct submission must preserve the lesson rule and handle the '
                       'defined edge case safely.',
    'mastery_quiz': [ [ 'NIO Files & Paths: What should you check before assuming a file operation succeeded?',
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
    'summary': 'You should now be able to explain nio files & paths, recognize its syntax, trace the worked example, '
               'and use the concept in a small original program.',
    'next_lesson': 'Annotations & Reflection Basics',
    'rules': [ 'Explain the job of Path in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the nio files & paths '
            'exercise.',
    'extension': 'Add one realistic requirement to the nio files & paths exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain nio files & paths without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_46'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'NIO Files & Paths matters because programs often need to preserve, load, or exchange '
                      'information outside a single run.',
    'guided_practice': [ '1. Restate the goal of **NIO Files & Paths** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **NIO Files & '
                         'Paths**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **NIO Files & Paths** task: Create a data directory, write a '
                            'file, list its contents, and explain why Path is preferred over raw string paths. Then '
                            'create one small variation that changes an input, rule, or data case without changing the '
                            'main goal.',
    'debug_task': 'Debug a deliberately small **NIO Files & Paths** program that exhibits this common mistake: **Using '
                  'Path without understanding whether it represents data, behavior, or a relationship.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **NIO Files & Paths** to a small real-world feature. Keep the same core rule, but '
                     'change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what nio files & paths means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for nio files & paths.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small nio files & paths example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for NIO Files & Paths.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for NIO Files & Paths without violating the stated '
                                  'rule.'},
                    { 'name': 'Invalid or empty case',
                      'input': 'Missing, invalid, duplicate, or otherwise exceptional data where relevant',
                      'expected': 'The program responds safely and predictably instead of silently producing an '
                                  'invalid state.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['io', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_48',
    'title': 'Annotations & Reflection Basics',
    'description': 'Understand annotations as metadata and reflection as runtime inspection, including practical uses '
                   'and the trade-offs of dynamic behavior.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Annotations & Reflection Basics**, understand why it is useful, '
                    'trace a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what annotations & reflection basics means and why it exists.',
                             'Read and write the core syntax used for annotations & reflection basics.',
                             'Predict the behavior of a small annotations & reflection basics example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['annotation', 'metadata', 'reflection', 'Class'],
    'explanation': 'Understand annotations as metadata and reflection as runtime inspection, including practical uses '
                   'and the trade-offs of dynamic behavior. Java syntax is shown using the standard library or '
                   'language feature for this lesson. Pay attention to the type, identifier, method call, object '
                   'reference, and punctuation.',
    'syntax': '@Deprecated\nvoid oldMethod() {}\n\nClass<?> type = String.class;\nSystem.out.println(type.getName());',
    'syntax_breakdown': [ 'Focus on annotation: identify what it represents and what role it plays in the statement.',
                          'Next inspect metadata: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': '@Deprecated\n'
                'void oldMethod() {}\n'
                '\n'
                'Class<?> type = String.class;\n'
                'System.out.println(type.getName());',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': '@Deprecated void oldMethod(){}\nClass<?> type=String.class;\nSystem.out.println(type.getName());',
    'example2_explanation': 'Change one meaningful input or rule related to annotations & reflection basics, predict '
                            'the result, and only then run the program.',
    'practical_example': 'Imagine a small annotations & reflection basics feature in a student or inventory '
                         'application. Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using annotation without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls metadata.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of annotation in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Inspect a class for its methods and explain one legitimate use case and one reason to avoid '
                'reflection when normal code is clearer.',
    'practice_problem': '**Annotations & Reflection Basics independent practice:** Inspect a class for its methods and '
                        'explain one legitimate use case and one reason to avoid reflection when normal code is '
                        'clearer. You must also add one clearly different variation and test it. Your work should '
                        "demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Annotations & Reflection Basics:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Annotations & Reflection Basics: What is an annotation?',
                        ['Metadata attached to program elements', 'A loop', 'A primitive', 'A file stream'],
                        0,
                        'Annotations provide metadata.'],
                      [ 'What does reflection allow?',
                        [ 'Inspecting types and members at runtime',
                          'Compiling C++',
                          'Creating files automatically',
                          'Removing generics'],
                        0,
                        'Reflection can inspect classes, methods, and fields at runtime.'],
                      [ 'Why can reflection be overused?',
                        [ 'It can reduce clarity and move errors to runtime',
                          'It always improves performance',
                          'It removes dependencies',
                          'It guarantees type safety'],
                        0,
                        'Normal language constructs are often clearer and safer.'],
                      [ 'Which is a built-in annotation?',
                        ['@Override', '@Loop', '@ScannerOnly', '@CompileNow'],
                        0,
                        '@Override is a standard Java annotation.'],
                      [ 'What is a reasonable reflection use case?',
                        [ 'Frameworks or tooling that must inspect types dynamically',
                          'Every getter',
                          'Every loop',
                          'All primitive arithmetic'],
                        0,
                        'Framework infrastructure is a common reflection use case.']],
    'summary': 'You should now be able to explain annotations & reflection basics, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'JVM Memory & Garbage Collection',
    'rules': [ 'Explain the job of annotation in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the annotations & '
            'reflection basics exercise.',
    'extension': 'Add one realistic requirement to the annotations & reflection basics exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain annotations & reflection basics without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_47'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Annotations & Reflection Basics gives you the foundation needed to read, change, and reason '
                      'about a program before larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Annotations & Reflection Basics** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Annotations & '
                         'Reflection Basics**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Annotations & Reflection Basics** task: Inspect a class for '
                            'its methods and explain one legitimate use case and one reason to avoid reflection when '
                            'normal code is clearer. Then create one small variation that changes an input, rule, or '
                            'data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Annotations & Reflection Basics** program that exhibits this common '
                  'mistake: **Using annotation without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Annotations & Reflection Basics** to a small real-world feature. Keep the same core '
                     'rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what annotations & reflection basics means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for annotations & reflection '
                                                 'basics.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small annotations & reflection basics '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Annotations & Reflection '
                                  'Basics.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Annotations & Reflection Basics without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Annotations & '
                                  'Reflection Basics.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_49',
    'title': 'JVM Memory & Garbage Collection',
    'description': 'Build a mental model of stack frames, heap objects, references, garbage collection, reachability, '
                   'and memory leaks caused by unwanted references.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **JVM Memory & Garbage Collection**, understand why it is useful, '
                    'trace a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what jvm memory & garbage collection means and why it exists.',
                             'Read and write the core syntax used for jvm memory & garbage collection.',
                             'Predict the behavior of a small jvm memory & garbage collection example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['stack', 'heap', 'reference', 'garbage collection'],
    'explanation': 'Build a mental model of stack frames, heap objects, references, garbage collection, reachability, '
                   'and memory leaks caused by unwanted references. Java syntax is shown using the standard library or '
                   'language feature for this lesson. Pay attention to the type, identifier, method call, object '
                   'reference, and punctuation.',
    'syntax': 'List<String> cache = new ArrayList<>();\n'
              'cache.add("kept");\n'
              '// Objects remain reachable while referenced.',
    'syntax_breakdown': [ 'Focus on stack: identify what it represents and what role it plays in the statement.',
                          'Next inspect heap: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'List<String> cache = new ArrayList<>();\n'
                'cache.add("kept");\n'
                '// Objects remain reachable while referenced.',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'Deque<String> tasks=new ArrayDeque<>();\n'
                'tasks.addLast("study"); tasks.addFirst("urgent");\n'
                'System.out.println(tasks.removeFirst());',
    'example2_explanation': 'Change one meaningful input or rule related to jvm memory & garbage collection, predict '
                            'the result, and only then run the program.',
    'practical_example': 'Imagine a small jvm memory & garbage collection feature in a student or inventory '
                         'application. Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using stack without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls heap.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of stack in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Explain why Java can still suffer memory leaks even though it has garbage collection.',
    'practice_problem': '**JVM Memory & Garbage Collection independent practice:** Explain why Java can still suffer '
                        'memory leaks even though it has garbage collection. You must also add one clearly different '
                        "variation and test it. Your work should demonstrate the lesson's main rule, not merely "
                        'reproduce Example 1.',
    'expected_output': '**Test contract for JVM Memory & Garbage Collection:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'JVM Memory & Garbage Collection: Where are Java objects generally allocated?',
                        ['The heap', 'The source file', 'The CPU register only', 'The package name'],
                        0,
                        'Objects are generally allocated on the heap.'],
                      [ 'What is a stack frame associated with?',
                        ['A method invocation', 'A database table', 'A file path', 'A package'],
                        0,
                        'Each active method invocation has a stack frame.'],
                      [ 'When can an object become eligible for garbage collection?',
                        [ 'When it is no longer reachable',
                          'Immediately after construction',
                          'Whenever a variable is final',
                          'Only after a file closes'],
                        0,
                        'Unreachable objects can become eligible for collection.'],
                      [ 'Can Java still have memory leaks?',
                        [ 'Yes, if unwanted references keep objects reachable',
                          'No, never',
                          'Only in native C++',
                          'Only with arrays'],
                        0,
                        'Garbage collection cannot collect objects that are still reachable.'],
                      [ 'Why is immutability helpful?',
                        [ 'It reduces accidental shared-state changes',
                          'It disables objects',
                          'It prevents garbage collection',
                          'It removes classes'],
                        0,
                        'Immutable objects are easier to reason about across code and threads.']],
    'summary': 'You should now be able to explain jvm memory & garbage collection, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Java Modules',
    'rules': [ 'Explain the job of stack in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the jvm memory & '
            'garbage collection exercise.',
    'extension': 'Add one realistic requirement to the jvm memory & garbage collection exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain jvm memory & garbage collection without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_48'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'JVM Memory & Garbage Collection matters because programs often need to store, find, update, and '
                      'process groups of related values.',
    'guided_practice': [ '1. Restate the goal of **JVM Memory & Garbage Collection** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **JVM Memory & '
                         'Garbage Collection**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **JVM Memory & Garbage Collection** task: Explain why Java can '
                            'still suffer memory leaks even though it has garbage collection. Then create one small '
                            'variation that changes an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **JVM Memory & Garbage Collection** program that exhibits this common '
                  'mistake: **Using stack without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **JVM Memory & Garbage Collection** to a small real-world feature. Keep the same core '
                     'rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what jvm memory & garbage collection means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for jvm memory & garbage '
                                                 'collection.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small jvm memory & garbage collection '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for JVM Memory & Garbage '
                                  'Collection.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for JVM Memory & Garbage Collection without '
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
  { 'id': 'java_50',
    'title': 'Java Modules',
    'description': 'Understand module-info.java, exported packages, required modules, and how modular boundaries can '
                   'make large applications more explicit.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Java Modules**, understand why it is useful, trace a focused '
                    'example, practice it with guidance, then solve an independent variation. You will finish by '
                    'proving your understanding through concept, syntax, code-reading, debugging, and application '
                    'checks.',
    'learning_objectives': [ 'Explain what java modules means and why it exists.',
                             'Read and write the core syntax used for java modules.',
                             'Predict the behavior of a small java modules example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['module', 'requires', 'exports', 'module-info.java'],
    'explanation': 'Understand module-info.java, exported packages, required modules, and how modular boundaries can '
                   'make large applications more explicit. Java syntax is shown using the standard library or language '
                   'feature for this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'module school.app {\n    requires java.sql;\n    exports school.api;\n}',
    'syntax_breakdown': [ 'Focus on module: identify what it represents and what role it plays in the statement.',
                          'Next inspect requires: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'module school.app {\n    requires java.sql;\n    exports school.api;\n}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'module school.app {\n    requires java.sql;\n    exports school.api;\n}',
    'example2_explanation': 'Change one meaningful input or rule related to java modules, predict the result, and only '
                            'then run the program.',
    'practical_example': 'Imagine a small java modules feature in a student or inventory application. Identify the '
                         'input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using module without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls requires.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of module in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Design a tiny two-module application and identify which package should be exported.',
    'practice_problem': '**Java Modules independent practice:** Design a tiny two-module application and identify '
                        'which package should be exported. You must also add one clearly different variation and test '
                        "it. Your work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Java Modules:** Run the program with a normal case, a boundary case, and a '
                       'misuse/invalid case when relevant. For each case, record the actual result and compare it with '
                       'the requirement. A correct submission must preserve the lesson rule and handle the defined '
                       'edge case safely.',
    'mastery_quiz': [ [ 'Java Modules: What file commonly declares a Java module?',
                        ['module-info.java', 'package-info.exe', 'Main.module', 'module.txt'],
                        0,
                        'module-info.java defines module metadata.'],
                      [ 'What does requires mean?',
                        [ 'The module depends on another module',
                          'The module exports a package',
                          'The module creates a class',
                          'The module starts a thread'],
                        0,
                        'requires declares a module dependency.'],
                      [ 'What does exports control?',
                        [ 'Which packages are exposed to other modules',
                          'Which variables are local',
                          'Which loops run',
                          'Which files are binary'],
                        0,
                        'exports controls module API visibility.'],
                      [ 'Why use modules in a large application?',
                        [ 'To make dependencies and boundaries explicit',
                          'To remove packages',
                          'To avoid compilation',
                          'To make all types public'],
                        0,
                        'Modules provide explicit dependency and API boundaries.'],
                      [ 'What is a benefit of strong module boundaries?',
                        [ 'Less accidental access between components',
                          'More global state',
                          'No tests',
                          'No type checking'],
                        0,
                        'Strong boundaries reduce unintended coupling.']],
    'summary': 'You should now be able to explain java modules, recognize its syntax, trace the worked example, and '
               'use the concept in a small original program.',
    'next_lesson': 'Sealed Classes & Pattern Matching',
    'rules': [ 'Explain the job of module in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the java modules '
            'exercise.',
    'extension': 'Add one realistic requirement to the java modules exercise while keeping the original behavior '
                 'correct.',
    'learning_checks': [ 'Can I explain java modules without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_49'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Java Modules gives you the foundation needed to read, change, and reason about a program before '
                      'larger features are introduced.',
    'guided_practice': [ '1. Restate the goal of **Java Modules** in one sentence before writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Java Modules**, '
                         'then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Java Modules** task: Design a tiny two-module application and '
                            'identify which package should be exported. Then create one small variation that changes '
                            'an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Java Modules** program that exhibits this common mistake: **Using '
                  'module without understanding whether it represents data, behavior, or a relationship.**. Before '
                  'changing code, identify the first incorrect value, state, control-flow decision, or ownership '
                  'assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Java Modules** to a small real-world feature. Keep the same core rule, but change the '
                     'context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what java modules means and why it exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for java modules.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small java modules example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Java Modules.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Java Modules without violating the stated '
                                  'rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Java '
                                  'Modules.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['fundamentals', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_51',
    'title': 'Sealed Classes & Pattern Matching',
    'description': 'Use sealed hierarchies to restrict permitted subclasses and modern pattern matching to make '
                   'type-based logic clearer.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Sealed Classes & Pattern Matching**, understand why it is useful, '
                    'trace a focused example, practice it with guidance, then solve an independent variation. You will '
                    'finish by proving your understanding through concept, syntax, code-reading, debugging, and '
                    'application checks.',
    'learning_objectives': [ 'Explain what sealed classes & pattern matching means and why it exists.',
                             'Read and write the core syntax used for sealed classes & pattern matching.',
                             'Predict the behavior of a small sealed classes & pattern matching example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['sealed', 'permits', 'pattern matching', 'exhaustiveness'],
    'explanation': 'Use sealed hierarchies to restrict permitted subclasses and modern pattern matching to make '
                   'type-based logic clearer. Java syntax is shown using the standard library or language feature for '
                   'this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'sealed interface Shape permits Circle, Rectangle {}\n'
              'final class Circle implements Shape {}\n'
              'final class Rectangle implements Shape {}',
    'syntax_breakdown': [ 'Focus on sealed: identify what it represents and what role it plays in the statement.',
                          'Next inspect permits: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'sealed interface Shape permits Circle, Rectangle {}\n'
                'final class Circle implements Shape {}\n'
                'final class Rectangle implements Shape {}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'class Lamp {\n    boolean on;\n    void toggle(){ on=!on; }\n}\nLamp lamp=new Lamp(); lamp.toggle();',
    'example2_explanation': 'Change one meaningful input or rule related to sealed classes & pattern matching, predict '
                            'the result, and only then run the program.',
    'practical_example': 'Imagine a small sealed classes & pattern matching feature in a student or inventory '
                         'application. Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using sealed without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls permits.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of sealed in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Design a sealed Result hierarchy and describe how exhaustive handling improves maintainability.',
    'practice_problem': '**Sealed Classes & Pattern Matching independent practice:** Design a sealed Result hierarchy '
                        'and describe how exhaustive handling improves maintainability. You must also add one clearly '
                        "different variation and test it. Your work should demonstrate the lesson's main rule, not "
                        'merely reproduce Example 1.',
    'expected_output': '**Test contract for Sealed Classes & Pattern Matching:** Run the program with a normal case, a '
                       'boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Sealed Classes & Pattern Matching: What is the main design idea in Sealed Classes & Pattern '
                        'Matching?',
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
    'summary': 'You should now be able to explain sealed classes & pattern matching, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Advanced Collections & Comparators',
    'rules': [ 'Explain the job of sealed in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the sealed classes & '
            'pattern matching exercise.',
    'extension': 'Add one realistic requirement to the sealed classes & pattern matching exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain sealed classes & pattern matching without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_50'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Sealed Classes & Pattern Matching matters because larger programs need clear ownership of state '
                      'and behavior and predictable relationships between types.',
    'guided_practice': [ '1. Restate the goal of **Sealed Classes & Pattern Matching** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Sealed Classes & '
                         'Pattern Matching**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Sealed Classes & Pattern Matching** task: Design a sealed '
                            'Result hierarchy and describe how exhaustive handling improves maintainability. Then '
                            'create one small variation that changes an input, rule, or data case without changing the '
                            'main goal.',
    'debug_task': 'Debug a deliberately small **Sealed Classes & Pattern Matching** program that exhibits this common '
                  'mistake: **Using sealed without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Sealed Classes & Pattern Matching** to a small real-world feature. Keep the same core '
                     'rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what sealed classes & pattern matching means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for sealed classes & pattern '
                                                 'matching.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small sealed classes & pattern matching '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Sealed Classes & Pattern '
                                  'Matching.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Sealed Classes & Pattern Matching without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Sealed Classes '
                                  '& Pattern Matching.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['oop', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_52',
    'title': 'Advanced Collections & Comparators',
    'description': 'Combine maps, sets, queues, immutable collection factories, and multi-key comparators to model '
                   'realistic data-processing tasks.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Advanced Collections & Comparators**, understand why it is '
                    'useful, trace a focused example, practice it with guidance, then solve an independent variation. '
                    'You will finish by proving your understanding through concept, syntax, code-reading, debugging, '
                    'and application checks.',
    'learning_objectives': [ 'Explain what advanced collections & comparators means and why it exists.',
                             'Read and write the core syntax used for advanced collections & comparators.',
                             'Predict the behavior of a small advanced collections & comparators example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['Comparator', 'immutable collection', 'ordering', 'uniqueness'],
    'explanation': 'Combine maps, sets, queues, immutable collection factories, and multi-key comparators to model '
                   'realistic data-processing tasks. Java syntax is shown using the standard library or language '
                   'feature for this lesson. Pay attention to the type, identifier, method call, object reference, and '
                   'punctuation.',
    'syntax': 'students.sort(Comparator.comparingInt(Student::score).reversed()\n    .thenComparing(Student::name));',
    'syntax_breakdown': [ 'Focus on Comparator: identify what it represents and what role it plays in the statement.',
                          'Next inspect immutable collection: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'students.sort(Comparator.comparingInt(Student::score).reversed()\n    .thenComparing(Student::name));',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'Deque<String> tasks=new ArrayDeque<>();\n'
                'tasks.addLast("study"); tasks.addFirst("urgent");\n'
                'System.out.println(tasks.removeFirst());',
    'example2_explanation': 'Change one meaningful input or rule related to advanced collections & comparators, '
                            'predict the result, and only then run the program.',
    'practical_example': 'Imagine a small advanced collections & comparators feature in a student or inventory '
                         'application. Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using Comparator without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls immutable collection.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of Comparator in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Sort a list by score descending, then name ascending, while using a set to prevent duplicate IDs.',
    'practice_problem': '**Advanced Collections & Comparators independent practice:** Sort a list by score descending, '
                        'then name ascending, while using a set to prevent duplicate IDs. You must also add one '
                        "clearly different variation and test it. Your work should demonstrate the lesson's main rule, "
                        'not merely reproduce Example 1.',
    'expected_output': '**Test contract for Advanced Collections & Comparators:** Run the program with a normal case, '
                       'a boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Advanced Collections & Comparators: What is a map primarily for?',
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
    'summary': 'You should now be able to explain advanced collections & comparators, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'CompletableFuture & Async Composition',
    'rules': [ 'Explain the job of Comparator in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the advanced '
            'collections & comparators exercise.',
    'extension': 'Add one realistic requirement to the advanced collections & comparators exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain advanced collections & comparators without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_51'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Advanced Collections & Comparators matters because programs often need to store, find, update, '
                      'and process groups of related values.',
    'guided_practice': [ '1. Restate the goal of **Advanced Collections & Comparators** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Advanced '
                         'Collections & Comparators**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Advanced Collections & Comparators** task: Sort a list by '
                            'score descending, then name ascending, while using a set to prevent duplicate IDs. Then '
                            'create one small variation that changes an input, rule, or data case without changing the '
                            'main goal.',
    'debug_task': 'Debug a deliberately small **Advanced Collections & Comparators** program that exhibits this common '
                  'mistake: **Using Comparator without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Advanced Collections & Comparators** to a small real-world feature. Keep the same '
                     'core rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what advanced collections & comparators means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for advanced collections & '
                                                 'comparators.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small advanced collections & comparators '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Advanced Collections & '
                                  'Comparators.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Advanced Collections & Comparators without '
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
  { 'id': 'java_53',
    'title': 'CompletableFuture & Async Composition',
    'description': 'Understand asynchronous task composition with CompletableFuture, callbacks, combining results, and '
                   'exception handling without confusing async execution with parallelism.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **CompletableFuture & Async Composition**, understand why it is '
                    'useful, trace a focused example, practice it with guidance, then solve an independent variation. '
                    'You will finish by proving your understanding through concept, syntax, code-reading, debugging, '
                    'and application checks.',
    'learning_objectives': [ 'Explain what completablefuture & async composition means and why it exists.',
                             'Read and write the core syntax used for completablefuture & async composition.',
                             'Predict the behavior of a small completablefuture & async composition example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['future', 'stage', 'composition', 'exception handling'],
    'explanation': 'Understand asynchronous task composition with CompletableFuture, callbacks, combining results, and '
                   'exception handling without confusing async execution with parallelism. Java syntax is shown using '
                   'the standard library or language feature for this lesson. Pay attention to the type, identifier, '
                   'method call, object reference, and punctuation.',
    'syntax': 'CompletableFuture<Integer> future = CompletableFuture\n'
              '    .supplyAsync(() -> 42)\n'
              '    .thenApply(x -> x * 2);',
    'syntax_breakdown': [ 'Focus on future: identify what it represents and what role it plays in the statement.',
                          'Next inspect stage: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'CompletableFuture<Integer> future = CompletableFuture\n'
                '    .supplyAsync(() -> 42)\n'
                '    .thenApply(x -> x * 2);',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'class Battery { int level=100; }\n'
                'class Phone {\n'
                '    private final Battery battery=new Battery();\n'
                '    int level(){ return battery.level; }\n'
                '}',
    'example2_explanation': 'Change one meaningful input or rule related to completablefuture & async composition, '
                            'predict the result, and only then run the program.',
    'practical_example': 'Imagine a small completablefuture & async composition feature in a student or inventory '
                         'application. Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using future without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls stage.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of future in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Describe how two asynchronous results could be combined and how an exception can be handled in the '
                'pipeline.',
    'practice_problem': '**CompletableFuture & Async Composition independent practice:** Describe how two asynchronous '
                        'results could be combined and how an exception can be handled in the pipeline. You must also '
                        "add one clearly different variation and test it. Your work should demonstrate the lesson's "
                        'main rule, not merely reproduce Example 1.',
    'expected_output': '**Test contract for CompletableFuture & Async Composition:** Run the program with a normal '
                       'case, a boundary case, and a misuse/invalid case when relevant. For each case, record the '
                       'actual result and compare it with the requirement. A correct submission must preserve the '
                       'lesson rule and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'CompletableFuture & Async Composition: What is a race condition?',
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
    'summary': 'You should now be able to explain completablefuture & async composition, recognize its syntax, trace '
               'the worked example, and use the concept in a small original program.',
    'next_lesson': 'Concurrent Collections & Atomicity',
    'rules': [ 'Explain the job of future in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the completablefuture & '
            'async composition exercise.',
    'extension': 'Add one realistic requirement to the completablefuture & async composition exercise while keeping '
                 'the original behavior correct.',
    'learning_checks': [ 'Can I explain completablefuture & async composition without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_52'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'CompletableFuture & Async Composition matters because larger programs need clear ownership of '
                      'state and behavior and predictable relationships between types.',
    'guided_practice': [ '1. Restate the goal of **CompletableFuture & Async Composition** in one sentence before '
                         'writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **CompletableFuture '
                         '& Async Composition**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **CompletableFuture & Async Composition** task: Describe how two '
                            'asynchronous results could be combined and how an exception can be handled in the '
                            'pipeline. Then create one small variation that changes an input, rule, or data case '
                            'without changing the main goal.',
    'debug_task': 'Debug a deliberately small **CompletableFuture & Async Composition** program that exhibits this '
                  'common mistake: **Using future without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **CompletableFuture & Async Composition** to a small real-world feature. Keep the same '
                     'core rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what completablefuture & async composition means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for completablefuture & async '
                                                 'composition.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small completablefuture & async '
                                                 'composition example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for CompletableFuture & Async '
                                  'Composition.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for CompletableFuture & Async Composition without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in '
                                  'CompletableFuture & Async Composition.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['oop', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'},
  { 'id': 'java_54',
    'title': 'Concurrent Collections & Atomicity',
    'description': 'Choose thread-safe collections and atomic operations for shared state, and understand why '
                   'individual operations may be safe while a larger sequence is not atomic.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Concurrent Collections & Atomicity**, understand why it is '
                    'useful, trace a focused example, practice it with guidance, then solve an independent variation. '
                    'You will finish by proving your understanding through concept, syntax, code-reading, debugging, '
                    'and application checks.',
    'learning_objectives': [ 'Explain what concurrent collections & atomicity means and why it exists.',
                             'Read and write the core syntax used for concurrent collections & atomicity.',
                             'Predict the behavior of a small concurrent collections & atomicity example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['atomic', 'concurrent collection', 'race', 'compound action'],
    'explanation': 'Choose thread-safe collections and atomic operations for shared state, and understand why '
                   'individual operations may be safe while a larger sequence is not atomic. Java syntax is shown '
                   'using the standard library or language feature for this lesson. Pay attention to the type, '
                   'identifier, method call, object reference, and punctuation.',
    'syntax': 'AtomicInteger counter = new AtomicInteger();\n'
              'counter.incrementAndGet();\n'
              'System.out.println(counter.get());',
    'syntax_breakdown': [ 'Focus on atomic: identify what it represents and what role it plays in the statement.',
                          'Next inspect concurrent collection: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'AtomicInteger counter = new AtomicInteger();\n'
                'counter.incrementAndGet();\n'
                'System.out.println(counter.get());',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'Deque<String> tasks=new ArrayDeque<>();\n'
                'tasks.addLast("study"); tasks.addFirst("urgent");\n'
                'System.out.println(tasks.removeFirst());',
    'example2_explanation': 'Change one meaningful input or rule related to concurrent collections & atomicity, '
                            'predict the result, and only then run the program.',
    'practical_example': 'Imagine a small concurrent collections & atomicity feature in a student or inventory '
                         'application. Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using atomic without understanding whether it represents data, behavior, or a relationship.',
                         'Forgetting the Java-specific rule that controls concurrent collection.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of atomic in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Replace a shared integer counter with AtomicInteger and explain the difference between atomic '
                'increment and a multi-step check-then-act operation.',
    'practice_problem': '**Concurrent Collections & Atomicity independent practice:** Replace a shared integer counter '
                        'with AtomicInteger and explain the difference between atomic increment and a multi-step '
                        'check-then-act operation. You must also add one clearly different variation and test it. Your '
                        "work should demonstrate the lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Concurrent Collections & Atomicity:** Run the program with a normal case, '
                       'a boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Concurrent Collections & Atomicity: What is a map primarily for?',
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
    'summary': 'You should now be able to explain concurrent collections & atomicity, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Advanced Java Engineering Practices',
    'rules': [ 'Explain the job of atomic in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the concurrent '
            'collections & atomicity exercise.',
    'extension': 'Add one realistic requirement to the concurrent collections & atomicity exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain concurrent collections & atomicity without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_53'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Concurrent Collections & Atomicity matters because programs often need to store, find, update, '
                      'and process groups of related values.',
    'guided_practice': [ '1. Restate the goal of **Concurrent Collections & Atomicity** in one sentence before writing '
                         'code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Concurrent '
                         'Collections & Atomicity**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Concurrent Collections & Atomicity** task: Replace a shared '
                            'integer counter with AtomicInteger and explain the difference between atomic increment '
                            'and a multi-step check-then-act operation. Then create one small variation that changes '
                            'an input, rule, or data case without changing the main goal.',
    'debug_task': 'Debug a deliberately small **Concurrent Collections & Atomicity** program that exhibits this common '
                  'mistake: **Using atomic without understanding whether it represents data, behavior, or a '
                  'relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Concurrent Collections & Atomicity** to a small real-world feature. Keep the same '
                     'core rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what concurrent collections & atomicity means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for concurrent collections & '
                                                 'atomicity.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small concurrent collections & atomicity '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Concurrent Collections & '
                                  'Atomicity.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Concurrent Collections & Atomicity without '
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
  { 'id': 'java_55',
    'title': 'Advanced Java Engineering Practices',
    'description': 'Connect language skills to maintainable Java systems through API design, immutability, '
                   'composition, SOLID thinking, logging, testing, and dependency boundaries.',
    'stage': 'Advanced Language Skills',
    'difficulty': 'Advanced',
    'introduction': 'In this lesson you will learn **Advanced Java Engineering Practices**, understand why it is '
                    'useful, trace a focused example, practice it with guidance, then solve an independent variation. '
                    'You will finish by proving your understanding through concept, syntax, code-reading, debugging, '
                    'and application checks.',
    'learning_objectives': [ 'Explain what advanced java engineering practices means and why it exists.',
                             'Read and write the core syntax used for advanced java engineering practices.',
                             'Predict the behavior of a small advanced java engineering practices example.',
                             'Apply the concept in a new exercise without copying the worked example.'],
    'terminology': ['API boundary', 'composition', 'SOLID', 'logging'],
    'explanation': 'Connect language skills to maintainable Java systems through API design, immutability, '
                   'composition, SOLID thinking, logging, testing, and dependency boundaries. Java syntax is shown '
                   'using the standard library or language feature for this lesson. Pay attention to the type, '
                   'identifier, method call, object reference, and punctuation.',
    'syntax': 'public interface PaymentService {\n    Receipt pay(Order order);\n}',
    'syntax_breakdown': [ 'Focus on API boundary: identify what it represents and what role it plays in the statement.',
                          'Next inspect composition: explain how it changes the program state or behavior.',
                          'Then identify the boundary syntax such as punctuation, braces, operators, or method calls.',
                          'Finally explain what the whole statement/block accomplishes rather than memorizing '
                          'individual tokens.'],
    'example1': 'public interface PaymentService {\n    Receipt pay(Order order);\n}',
    'example1_explanation': 'The example is intentionally small so you can trace values and object state before '
                            'combining it with larger programs.',
    'example2': 'public interface PaymentService {\n'
                '    Receipt pay(Order order);\n'
                '}\n'
                '// Keep the API small and the implementation replaceable.',
    'example2_explanation': 'Change one meaningful input or rule related to advanced java engineering practices, '
                            'predict the result, and only then run the program.',
    'practical_example': 'Imagine a small advanced java engineering practices feature in a student or inventory '
                         'application. Identify the input/state, the operation, and the expected result before coding.',
    'common_mistakes': [ 'Using API boundary without understanding whether it represents data, behavior, or a '
                         'relationship.',
                         'Forgetting the Java-specific rule that controls composition.',
                         'Fixing the visible error without checking the first incorrect assumption in the program.'],
    'beginner_tips': [ 'Explain the job of API boundary in one sentence before writing it.',
                       'Test a normal case and a boundary or empty case.',
                       'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'exercise': 'Design a small service layer for an inventory application and identify one SOLID principle used by '
                'the design.',
    'practice_problem': '**Advanced Java Engineering Practices independent practice:** Design a small service layer '
                        'for an inventory application and identify one SOLID principle used by the design. You must '
                        'also add one clearly different variation and test it. Your work should demonstrate the '
                        "lesson's main rule, not merely reproduce Example 1.",
    'expected_output': '**Test contract for Advanced Java Engineering Practices:** Run the program with a normal case, '
                       'a boundary case, and a misuse/invalid case when relevant. For each case, record the actual '
                       'result and compare it with the requirement. A correct submission must preserve the lesson rule '
                       'and handle the defined edge case safely.',
    'mastery_quiz': [ [ 'Advanced Java Engineering Practices: Which statement best describes Advanced Java Engineering '
                        'Practices?',
                        [ 'It is a core part of Advanced Java Engineering Practices',
                          'It is only a compiler warning',
                          'It is unrelated to programming',
                          'It replaces all data types'],
                        0,
                        'This lesson focuses on the role and correct use of Advanced Java Engineering Practices.'],
                      [ 'What should a learner be able to do after Advanced Java Engineering Practices?',
                        [ 'Use the concept in a small program',
                          'Only memorize its name',
                          'Avoid testing it',
                          'Copy one example unchanged'],
                        0,
                        'Application is the goal, not memorization.'],
                      [ 'Which test is most useful for Advanced Java Engineering Practices?',
                        [ 'A normal case plus an important edge case',
                          'No input',
                          'Only a huge random case',
                          'Only comments'],
                        0,
                        'Testing the concept in more than one case reveals misunderstandings.'],
                      [ 'Which mistake should be avoided with Advanced Java Engineering Practices?',
                        [ 'Using syntax without understanding its behavior',
                          'Writing a small test',
                          'Reading diagnostics',
                          'Choosing clear names'],
                        0,
                        'Understanding behavior matters more than copying syntax.'],
                      [ 'How should Advanced Java Engineering Practices fit into a larger program?',
                        [ 'As one focused tool combined with earlier concepts',
                          'As a replacement for every other feature',
                          'As global state everywhere',
                          'As code that never needs testing'],
                        0,
                        'Programming features are combined according to the problem.']],
    'summary': 'You should now be able to explain advanced java engineering practices, recognize its syntax, trace the '
               'worked example, and use the concept in a small original program.',
    'next_lesson': 'Capstone project / practical assessment',
    'rules': [ 'Explain the job of API boundary in one sentence before writing it.',
               'Test a normal case and a boundary or empty case.',
               'Prefer clear standard-library APIs and explicit names over clever shortcuts.'],
    'hint': 'Start by writing the input/state, rule, processing steps, and expected output for the advanced java '
            'engineering practices exercise.',
    'extension': 'Add one realistic requirement to the advanced java engineering practices exercise while keeping the '
                 'original behavior correct.',
    'learning_checks': [ 'Can I explain advanced java engineering practices without looking at the example?',
                         'Can I predict the example before running it?',
                         'Can I modify the example to solve a related problem?'],
    'prerequisites': ['java_54'],
    'step_sequence': [ 'Click 📖 Learn',
                       'Click 💻 Example',
                       'Click 🧪 Practice',
                       'Click 🧠 Mastery Check',
                       'After passing, click ➡️ Next Lesson'],
    'mastery_pass_score': 4,
    'mastery_question_count': 5,
    'review_threshold': 3,
    'why_it_matters': 'Advanced Java Engineering Practices matters because real projects require requirements, design '
                      'decisions, testing, maintainability, and trade-off awareness.',
    'guided_practice': [ '1. Restate the goal of **Advanced Java Engineering Practices** in one sentence before '
                         'writing code.',
                         '2. Start from the smallest part of the lesson example that demonstrates **Advanced Java '
                         'Engineering Practices**, then change only what the exercise requires.',
                         '3. Run the exercise against the listed test cases, compare the behavior with your '
                         'prediction, and fix the first mismatch before adding features.'],
    'independent_practice': 'Independently solve this **Advanced Java Engineering Practices** task: Design a small '
                            'service layer for an inventory application and identify one SOLID principle used by the '
                            'design. Then create one small variation that changes an input, rule, or data case without '
                            'changing the main goal.',
    'debug_task': 'Debug a deliberately small **Advanced Java Engineering Practices** program that exhibits this '
                  'common mistake: **Using API boundary without understanding whether it represents data, behavior, or '
                  'a relationship.**. Before changing code, identify the first incorrect value, state, control-flow '
                  'decision, or ownership assumption; then explain the fix in one sentence.',
    'transfer_task': 'Transfer **Advanced Java Engineering Practices** to a small real-world feature. Keep the same '
                     'core rule, but change the context and explain which part of the solution remains reusable.',
    'assessment_contract': { 'mastery_skills': [ 'Core concept',
                                                 'Syntax & usage',
                                                 'Code reading',
                                                 'Debugging',
                                                 'Application'],
                             'demonstration_required': True,
                             'pass_score': 4,
                             'review_if_score_at_or_below': 3},
    'objective_assessment_map': [ { 'objective': 'Explain what advanced java engineering practices means and why it '
                                                 'exists.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Read and write the core syntax used for advanced java engineering '
                                                 'practices.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Predict the behavior of a small advanced java engineering practices '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'},
                                  { 'objective': 'Apply the concept in a new exercise without copying the worked '
                                                 'example.',
                                    'evidence': 'At least one mastery question plus the guided/independent practice '
                                                'task.'}],
    'test_cases': [ { 'name': 'Normal case',
                      'input': 'A valid, ordinary case for the lesson',
                      'expected': 'The program demonstrates the required behavior for Advanced Java Engineering '
                                  'Practices.'},
                    { 'name': 'Boundary case',
                      'input': 'The smallest/largest or transition value relevant to the lesson',
                      'expected': 'The program handles the boundary for Advanced Java Engineering Practices without '
                                  'violating the stated rule.'},
                    { 'name': 'Misuse case',
                      'input': 'A small change that violates one rule taught by the lesson',
                      'expected': 'The student can identify or prevent the specific misuse discussed in Advanced Java '
                                  'Engineering Practices.'}],
    'review_plan': { 'failed_mastery': 'Review the missed skill categories, redo guided practice, then retry mastery.',
                     'passed_4': 'Schedule retrieval review after a short delay and revisit the weak category if any.',
                     'passed_5': 'Schedule a longer retrieval interval and attempt a transfer task later.'},
    'quality_tags': ['engineering', 'topic-specific-practice', 'guided-practice', 'transfer', 'diagnostic-mastery'],
    'content_version': '3.4.0'}]

from bot.learning.quality import enrich_curriculum
enrich_curriculum(JAVA_CURRICULUM, "java")
