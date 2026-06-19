"""Shared helpers for analysis scripts."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
INTERNAL_ROOT = SCRIPT_DIR.parent
if str(INTERNAL_ROOT) not in sys.path:
    sys.path.insert(0, str(INTERNAL_ROOT))

from pipeline_paths import STRUCTURED_YAML_DIR, iter_files


def load_structured_jobs() -> list[dict]:
    """Load all structured jobs across dated subdirectories."""
    jobs = []
    for file in iter_files(STRUCTURED_YAML_DIR, "*.yaml"):
        try:
            with file.open("r", encoding="utf-8") as handle:
                jobs.append(yaml.safe_load(handle))
        except Exception as exc:
            print(f"Error loading {file}: {exc}")
    return jobs
