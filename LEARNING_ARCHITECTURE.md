# ClassCode Learning Architecture — 3.3.0

## Root cause found
The old learning system stored only a small set of fields per lesson and generated most visible teaching material from the lesson title using generic helpers. Mastery questions lived separately in `bot/ui/lesson.py` and fell back to generic title-based questions. This allowed the UI to display a new title while still presenting nearly identical educational material.

There was no separate web frontend or HTTP lesson API in this project. The Discord UI directly selects a curriculum record by `language + topic_id` and renders it.

## New lesson contract
Every lesson record owns:
- stable lesson ID
- title
- description/introduction
- stage/difficulty
- learning objectives
- terminology
- explanation
- syntax
- syntax breakdown
- worked example
- second example
- practical example
- common mistakes
- beginner tips
- mini exercise
- practice problem
- expected-output guidance
- five-question mastery bank
- summary
- next-lesson mapping

The UI renders these fields directly. It no longer invents the core lesson content from the title.

## Curriculum validation
`bot/learning/schema.py` validates both tracks at import/startup. It rejects:
- duplicate IDs
- duplicate titles
- missing required lesson fields
- insufficient objectives/terminology/mistakes/tips
- missing or malformed mastery questions
- broken next-lesson mappings
- wrong language prefixes

`tests/test_curriculum.py` additionally verifies adjacent lessons have different descriptions, syntax, exercises, and mastery questions, and that every quiz is tied to its exact lesson title.

## Progress service
Progress selection was moved into `bot/learning/progress.py` so it is independent of Discord UI rendering and can be tested directly.

Progress is stored in Supabase PostgreSQL using `user_progress(user_id, language, topic_id, status, completed_at)`. PostgreSQL is the only supported database technology. Existing lesson IDs were preserved for the original lessons; new lessons are appended with new stable IDs.

Navigation always resolves the target lesson from the selected language curriculum by its exact ID.

## Mastery
Mastery questions now come from `topic["mastery_quiz"]`. There is no shared fallback quiz for curriculum lessons.

The Discord mastery UI uses a mobile-friendly select menu and requires at least 4/5 correct answers to pass.

## Curriculum breadth
- C++: 58 lessons, from fundamentals through data structures, modern C++, templates, concepts, ranges, coroutines, build systems, dependencies, operator overloading, and concurrency.
- Java: 55 lessons, from fundamentals through OOP, collections, generics, functional programming, streams, NIO, date/time, JDBC, JVM memory, modules, sealed classes, concurrency, async composition, and engineering practices.

The roadmap breadth was used as a reference only; lesson wording and teaching material are original.
