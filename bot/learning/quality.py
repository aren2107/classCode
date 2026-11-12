from __future__ import annotations

"""Instructional-quality metadata for ClassCode 3.4.

The curriculum remains the source of lesson prose. This layer adds an explicit
learning spine, assessment mapping, remediation guidance, and test contracts so
lessons are auditable as educational units rather than just populated records.
"""


def _family(title: str) -> str:
    t = title.lower()
    rules = [
        ("input", ["input", "scanner", "output"]),
        ("decision", ["if / else", "switch", "decision", "condition"]),
        ("loop", ["loop", "iteration", "nested loops"]),
        ("function", ["function", "method"]),
        ("collection", ["vector", "arraylist", "hashmap", "hashset", "collection", "map", "set", "stack", "queue", "deque"]),
        ("array", ["array"]),
        ("string", ["string", "text"]),
        ("oop", ["class", "object", "constructor", "encapsulation", "inheritance", "polymorphism", "interface", "composition"]),
        ("memory", ["pointer", "reference", "memory", "raii", "smart pointer", "move semantics", "resource ownership"]),
        ("error", ["exception", "debug", "error"]),
        ("io", ["file i/o", "file", "serialization", "data format"]),
        ("generic", ["template", "generic"]),
        ("functional", ["lambda", "stream", "optional", "completablefuture", "async"]),
        ("concurrency", ["thread", "concurrency", "executor", "synchron", "atomic"]),
        ("algorithm", ["algorithm", "search", "sort", "sorting", "comparator", "big-o", "complexity", "recursion"]),
        ("tree_graph", ["tree", "heap", "priority", "graph", "traversal"]),
        ("testing", ["testing", "junit", "validation"]),
        ("database", ["jdbc", "database"]),
        ("engineering", ["engineering", "capstone", "project"]),
    ]
    for family, needles in rules:
        if any(n in t for n in needles):
            return family
    return "fundamentals"


def _why(title: str, family: str) -> str:
    reasons = {
        "fundamentals": f"{title} gives you the foundation needed to read, change, and reason about a program before larger features are introduced.",
        "input": f"{title} matters because programs need a reliable way to receive and present data instead of relying on hard-coded values.",
        "decision": f"{title} matters because real programs must choose different actions when data or conditions change.",
        "loop": f"{title} matters because repeated work should be expressed once and controlled by clear stopping conditions.",
        "function": f"{title} matters because focused functions or methods make behavior reusable, testable, and easier to debug.",
        "collection": f"{title} matters because programs often need to store, find, update, and process groups of related values.",
        "array": f"{title} matters because indexed data appears throughout algorithms and application code.",
        "string": f"{title} matters because user-facing programs constantly process names, messages, commands, and other text.",
        "oop": f"{title} matters because larger programs need clear ownership of state and behavior and predictable relationships between types.",
        "memory": f"{title} matters because C++ programs must reason carefully about references, ownership, lifetime, and resource safety.",
        "error": f"{title} matters because useful programs must detect, explain, and recover from incorrect states instead of silently failing.",
        "io": f"{title} matters because programs often need to preserve, load, or exchange information outside a single run.",
        "generic": f"{title} matters because reusable code should avoid unnecessary duplication while remaining type-safe.",
        "functional": f"{title} matters because modern code often transforms data and composes behavior in compact, reusable ways.",
        "concurrency": f"{title} matters because concurrent programs must coordinate work without corrupting shared state or hiding failures.",
        "algorithm": f"{title} matters because solving a problem correctly also requires choosing an approach that scales and can be reasoned about.",
        "tree_graph": f"{title} matters because hierarchical and network-shaped data require specialized structures and traversal strategies.",
        "testing": f"{title} matters because confidence comes from evidence: repeatable tests, clear failures, and validation of edge cases.",
        "database": f"{title} matters because applications need reliable ways to store, query, and update persistent data.",
        "engineering": f"{title} matters because real projects require requirements, design decisions, testing, maintainability, and trade-off awareness.",
    }
    return reasons[family]


def _guided(title: str, exercise: str) -> list[str]:
    return [
        f"1. Restate the goal of **{title}** in one sentence before writing code.",
        f"2. Start from the smallest part of the lesson example that demonstrates **{title}**, then change only what the exercise requires.",
        f"3. Run the exercise against the listed test cases, compare the behavior with your prediction, and fix the first mismatch before adding features.",
    ]


def _debug(title: str, mistakes: list[str]) -> str:
    first = mistakes[0] if mistakes else "a topic-specific misuse"
    return (
        f"Debug a deliberately small **{title}** program that exhibits this common mistake: **{first}**. "
        "Before changing code, identify the first incorrect value, state, control-flow decision, or ownership assumption; "
        "then explain the fix in one sentence."
    )


def _tests(title: str, family: str) -> list[dict]:
    base = [
        {"name": "Normal case", "input": "A valid, ordinary case for the lesson", "expected": f"The program demonstrates the required behavior for {title}."},
        {"name": "Boundary case", "input": "The smallest/largest or transition value relevant to the lesson", "expected": f"The program handles the boundary for {title} without violating the stated rule."},
        {"name": "Invalid or empty case", "input": "Missing, invalid, duplicate, or otherwise exceptional data where relevant", "expected": f"The program responds safely and predictably instead of silently producing an invalid state."},
    ]
    if family in {"fundamentals", "oop", "memory", "generic", "functional", "concurrency", "engineering"}:
        base[2] = {"name": "Misuse case", "input": "A small change that violates one rule taught by the lesson", "expected": f"The student can identify or prevent the specific misuse discussed in {title}."}
    return base


def enrich_lesson(lesson: dict, language: str, index: int) -> None:
    title = lesson["title"]
    family = _family(title)
    exercise = lesson.get("exercise", "Complete the lesson exercise.")
    lesson["prerequisites"] = [] if index == 0 else ["__PREVIOUS_LESSON__"]
    lesson["step_sequence"] = [
        "Click 📖 Learn",
        "Click 💻 Example",
        "Click 🧪 Practice",
        "Click 🧠 Mastery Check",
        "After passing, click ➡️ Next Lesson",
    ]
    lesson["mastery_pass_score"] = 4
    lesson["mastery_question_count"] = 5
    lesson["review_threshold"] = 3
    lesson["why_it_matters"] = _why(title, family)
    lesson["guided_practice"] = _guided(title, exercise)
    lesson["independent_practice"] = (
        f"Independently solve this **{title}** task: {exercise} Then create one small variation that changes an input, rule, or data case without changing the main goal."
    )
    lesson["debug_task"] = _debug(title, lesson.get("common_mistakes", []))
    lesson["transfer_task"] = (
        f"Transfer **{title}** to a small real-world feature. Keep the same core rule, but change the context and explain which part of the solution remains reusable."
    )
    lesson["assessment_contract"] = {
        "mastery_skills": ["Core concept", "Syntax & usage", "Code reading", "Debugging", "Application"],
        "demonstration_required": True,
        "pass_score": 4,
        "review_if_score_at_or_below": 3,
    }
    lesson["objective_assessment_map"] = [
        {"objective": objective, "evidence": "At least one mastery question plus the guided/independent practice task."}
        for objective in lesson.get("learning_objectives", [])
    ]
    lesson["test_cases"] = _tests(title, family)
    lesson["review_plan"] = {
        "failed_mastery": "Review the missed skill categories, redo guided practice, then retry mastery.",
        "passed_4": "Schedule retrieval review after a short delay and revisit the weak category if any.",
        "passed_5": "Schedule a longer retrieval interval and attempt a transfer task later.",
    }
    lesson["quality_tags"] = [family, "topic-specific-practice", "guided-practice", "transfer", "diagnostic-mastery"]
    lesson["content_version"] = "3.4.0"

    # Replace the old generic assessment wording with a concrete, auditable contract.
    lesson["practice_problem"] = (
        f"**{title} independent practice:** {exercise} "
        f"You must also add one clearly different variation and test it. Your work should demonstrate the lesson's main rule, not merely reproduce Example 1."
    )
    lesson["expected_output"] = (
        f"**Test contract for {title}:** Run the program with a normal case, a boundary case, and a misuse/invalid case when relevant. "
        f"For each case, record the actual result and compare it with the requirement. A correct submission must preserve the lesson rule and handle the defined edge case safely."
    )

    # Make the introduction explain purpose, not merely repeat the lesson title.
    lesson["introduction"] = (
        f"In this lesson you will learn **{title}**, understand why it is useful, trace a focused example, practice it with guidance, "
        "then solve an independent variation. You will finish by proving your understanding through concept, syntax, code-reading, debugging, and application checks."
    )


def enrich_curriculum(curriculum: list[dict], language: str) -> None:
    for index, lesson in enumerate(curriculum):
        enrich_lesson(lesson, language, index)
    for index, lesson in enumerate(curriculum):
        lesson["prerequisites"] = [] if index == 0 else [curriculum[index - 1]["id"]]


def enrich_all(cpp: list[dict], java: list[dict]) -> None:
    enrich_curriculum(cpp, "cpp")
    enrich_curriculum(java, "java")
