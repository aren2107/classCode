"""Tests for curriculum refactoring (Task 3)."""
import pytest


def test_cpp_curriculum_loads_identical_to_original():
    """CPP_CURRICULUM should load identically after refactoring."""
    from bot.learning.cpp import CPP_CURRICULUM as new_cpp
    assert len(new_cpp) == 58
    assert all("id" in lesson for lesson in new_cpp)
    assert all(lesson["id"].startswith("cpp_") for lesson in new_cpp)
    # Verify first lesson unchanged
    first = new_cpp[0]
    assert first["id"] == "cpp_01"
    assert first["title"] == "Programming Fundamentals"
    assert len(first["mastery_quiz"]) == 5


def test_java_curriculum_loads_identical_to_original():
    """JAVA_CURRICULUM should load identically after refactoring."""
    from bot.learning.java import JAVA_CURRICULUM as new_java
    assert len(new_java) == 55
    assert all(lesson["id"].startswith("java_") for lesson in new_java)
    first = new_java[0]
    assert first["id"] == "java_01"
    assert first["title"] == "Programming Fundamentals"


def test_cpp_curriculum_validates():
    """CPP_CURRICULUM should pass schema validation."""
    from bot.learning.schema import validate_curriculum
    from bot.learning.cpp import CPP_CURRICULUM
    validate_curriculum(CPP_CURRICULUM, "cpp")


def test_java_curriculum_validates():
    """JAVA_CURRICULUM should pass schema validation."""
    from bot.learning.schema import validate_curriculum
    from bot.learning.java import JAVA_CURRICULUM
    validate_curriculum(JAVA_CURRICULUM, "java")