"""Pytest configuration and fixtures for ClassCode tests."""
import pytest
import sys
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch
from datetime import date, datetime, timedelta

# Ensure bot module is importable
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


@pytest.fixture(autouse=True)
def mock_config_database_url():
    """Mock Config.DATABASE_URL for all tests."""
    with patch("bot.config.Config.DATABASE_URL", "postgresql://test:test@localhost:5432/test"):
        with patch("bot.config.Config.GUILD_ID", 123456789):
            with patch("bot.config.Config.DISCORD_TOKEN", "test_token"):
                with patch("bot.config.Config.CODE_RUNNER_URL", "https://test.judge0.com"):
                    yield


@pytest.fixture
def mock_db_connection():
    """Mock psycopg connection for unit tests."""
    conn = MagicMock()
    conn.execute = MagicMock()
    conn.fetchone = MagicMock()
    conn.fetchall = MagicMock()
    conn.__enter__ = MagicMock(return_value=conn)
    conn.__exit__ = MagicMock(return_value=None)
    return conn


@pytest.fixture
def mock_db(mock_db_connection):
    """Mock Database instance with async methods."""
    from bot.database import Database
    db = MagicMock(spec=Database)
    db._get_connection = MagicMock(return_value=mock_db_connection)
    db.execute = AsyncMock()
    db.fetchone = AsyncMock()
    db.fetchall = AsyncMock()
    db.run_transaction = AsyncMock()
    return db


@pytest.fixture
def sample_cpp_lesson():
    """Minimal valid C++ lesson for testing."""
    return {
        "id": "cpp_test_01",
        "title": "Test Lesson",
        "description": "A test lesson",
        "stage": "Foundation",
        "difficulty": "Beginner",
        "introduction": "Test introduction",
        "learning_objectives": ["Objective 1", "Objective 2", "Objective 3"],
        "terminology": ["term1", "term2", "term3"],
        "explanation": "Test explanation",
        "syntax": "int main() { return 0; }",
        "syntax_breakdown": ["breakdown1", "breakdown2", "breakdown3"],
        "example1": "int main() { return 0; }",
        "example1_explanation": "Example explanation",
        "example2": "int main() { return 0; }",
        "example2_explanation": "Example 2 explanation",
        "practical_example": "Practical example",
        "common_mistakes": ["mistake1", "mistake2", "mistake3"],
        "beginner_tips": ["tip1", "tip2", "tip3"],
        "exercise": "Test exercise",
        "practice_problem": "Test practice problem",
        "expected_output": "Test expected output",
        "mastery_quiz": [
            ["Q1", ["A", "B", "C", "D"], 0, "Expl1"],
            ["Q2", ["A", "B", "C", "D"], 1, "Expl2"],
            ["Q3", ["A", "B", "C", "D"], 2, "Expl3"],
            ["Q4", ["A", "B", "C", "D"], 3, "Expl4"],
            ["Q5", ["A", "B", "C", "D"], 0, "Expl5"],
        ],
        "summary": "Test summary",
        "next_lesson": "Next Lesson",
        "prerequisites": [],
        "step_sequence": ["step1", "step2", "step3"],
        "mastery_pass_score": 4,
        "mastery_question_count": 5,
        "review_threshold": 3,
        "why_it_matters": "Why it matters",
        "guided_practice": ["guide1", "guide2", "guide3"],
        "independent_practice": "Independent practice",
        "debug_task": "Debug task",
        "transfer_task": "Transfer task",
        "assessment_contract": {
            "mastery_skills": ["Core concept", "Syntax & usage", "Code reading", "Debugging", "Application"],
            "demonstration_required": True,
            "pass_score": 4,
            "review_if_score_at_or_below": 3,
        },
        "objective_assessment_map": [
            {"objective": "Objective 1", "evidence": "Evidence 1"},
            {"objective": "Objective 2", "evidence": "Evidence 2"},
            {"objective": "Objective 3", "evidence": "Evidence 3"},
        ],
        "test_cases": [
            {"name": "Normal", "input": "input", "expected": "expected"},
            {"name": "Boundary", "input": "input", "expected": "expected"},
            {"name": "Invalid", "input": "input", "expected": "expected"},
        ],
        "review_plan": {
            "failed_mastery": "Review failed",
            "passed_4": "Passed 4",
            "passed_5": "Passed 5",
        },
        "quality_tags": ["tag1", "tag2", "tag3"],
        "content_version": "3.4.0",
        "hint": "Test hint",
        "extension": "Test extension",
        "rules": ["rule1", "rule2", "rule3"],
        "learning_checks": ["check1", "check2", "check3"],
    }


@pytest.fixture
def sample_java_lesson(sample_cpp_lesson):
    """Minimal valid Java lesson for testing."""
    lesson = sample_cpp_lesson.copy()
    lesson["id"] = "java_test_01"
    lesson["syntax"] = "public class Main { public static void main(String[] args) {} }"
    return lesson


@pytest.fixture
def manila_today():
    """Fixed Manila date for testing."""
    return date(2026, 11, 13)


@pytest.fixture
def manila_timestamp():
    """Fixed Manila timestamp for testing."""
    return datetime(2026, 11, 13, 12, 0, 0)


# Configure pytest-asyncio
pytest_plugins = ["pytest_asyncio"]