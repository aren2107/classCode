"""Offline curriculum quality audit for ClassCode.

Run from the project root:
    python tools/validate_curriculum.py
"""
from __future__ import annotations
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from bot.learning.cpp import CPP_CURRICULUM
from bot.learning.java import JAVA_CURRICULUM
from bot.learning.schema import validate_curriculum


def report(name, curriculum):
    validate_curriculum(curriculum, name)
    print(f"{name.upper()}: PASS")
    print(f"  Lessons: {len(curriculum)}")
    print(f"  Unique IDs: {len({x['id'] for x in curriculum})}")
    print(f"  Unique practice contracts: {len({x['practice_problem'] for x in curriculum})}")
    print(f"  Unique expected-output contracts: {len({x['expected_output'] for x in curriculum})}")
    print("  Prerequisite chain: valid")
    print("  Mastery bank: 5 questions per lesson; pass = 4/5")


if __name__ == "__main__":
    report("cpp", CPP_CURRICULUM)
    report("java", JAVA_CURRICULUM)
