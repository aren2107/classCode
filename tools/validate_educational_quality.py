"""Offline educational quality validator for ClassCode 3.4.0."""
from __future__ import annotations
import pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from bot.learning.cpp import CPP_CURRICULUM
from bot.learning.java import JAVA_CURRICULUM

REQUIRED=("why_it_matters","guided_practice","independent_practice","debug_task","transfer_task","assessment_contract","objective_assessment_map","test_cases","review_plan","quality_tags","content_version")
for language,curriculum in (("cpp",CPP_CURRICULUM),("java",JAVA_CURRICULUM)):
    assert all(l.get("content_version")=="3.4.0" for l in curriculum)
    assert all(all(k in l for k in REQUIRED) for l in curriculum)
    assert len({l["practice_problem"] for l in curriculum})==len(curriculum)
    assert len({l["expected_output"] for l in curriculum})==len(curriculum)
    assert all(len(l["test_cases"])>=3 for l in curriculum)
    assert all(l["assessment_contract"]["demonstration_required"] for l in curriculum)
    assert all(len(l["objective_assessment_map"])==len(l["learning_objectives"]) for l in curriculum)
    print(f"{language.upper()}: EDUCATIONAL QUALITY PASS ({len(curriculum)} lessons)")
print("Educational quality validation: PASS")
