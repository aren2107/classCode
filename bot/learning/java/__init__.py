"""Java Curriculum - Loaded from individual lesson files."""
from __future__ import annotations

import importlib
import pkgutil

JAVA_CURRICULUM = []

# Load all lesson modules from this package
for _, module_name, _ in pkgutil.iter_modules(__path__):
    if module_name.startswith("java_"):
        module = importlib.import_module(f".{module_name}", __name__)
        JAVA_CURRICULUM.append(module.LESSON)

# Sort by lesson id to maintain order
JAVA_CURRICULUM.sort(key=lambda x: x["id"])

# Apply enrichment (from original java.py)
from bot.learning.quality import enrich_curriculum
enrich_curriculum(JAVA_CURRICULUM, "java")