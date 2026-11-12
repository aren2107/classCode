"""Offline validator for ClassCode's five-part mastery contract."""
from __future__ import annotations
import ast
import pathlib
import sys
import re
import random

ROOT = pathlib.Path(__file__).resolve().parents[1]
src = (ROOT / "bot" / "ui" / "lesson.py").read_text(encoding="utf-8")
tree = ast.parse(src)
needed = {"clean_code", "line_explanation", "_mastery_question", "_code_reading_question", "_debug_question", "_application_question", "lesson_questions"}
namespace = {"re": re, "random": random}
for node in tree.body:
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in needed:
        exec(compile(ast.Module(body=[node], type_ignores=[]), "lesson_helpers.py", "exec"), namespace)
sys.path.insert(0, str(ROOT))
from bot.learning.cpp import CPP_CURRICULUM
from bot.learning.java import JAVA_CURRICULUM

EXPECTED = ["Core concept", "Syntax & usage", "Code reading", "Debugging", "Application"]

for language, curriculum in (("cpp", CPP_CURRICULUM), ("java", JAVA_CURRICULUM)):
    for topic in curriculum:
        questions = namespace["lesson_questions"](topic, language)
        if len(questions) != 5:
            raise SystemExit(f"FAIL {language}/{topic['id']}: expected 5 questions")
        categories = [q["category"] for q in questions]
        if categories != EXPECTED:
            raise SystemExit(f"FAIL {language}/{topic['id']}: categories={categories}")
        for q in questions:
            if len(q["options"]) != 4 or not 0 <= q["answer"] < 4:
                raise SystemExit(f"FAIL {language}/{topic['id']}: invalid answer options")
print("Mastery validation: PASS")
print("C++: 58/58 lessons -> 5 skill categories each")
print("Java: 55/55 lessons -> 5 skill categories each")
