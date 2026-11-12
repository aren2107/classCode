"""C++ Curriculum - Loaded from individual lesson files."""
from __future__ import annotations

import importlib
import pkgutil

CPP_CURRICULUM = []

# Load all lesson modules from this package
for _, module_name, _ in pkgutil.iter_modules(__path__):
    if module_name.startswith("cpp_"):
        module = importlib.import_module(f".{module_name}", __name__)
        CPP_CURRICULUM.append(module.LESSON)

# Sort by lesson id to maintain order
CPP_CURRICULUM.sort(key=lambda x: x["id"])

# Apply enrichment (from original cpp.py)
from bot.learning.quality import enrich_curriculum
enrich_curriculum(CPP_CURRICULUM, "cpp")