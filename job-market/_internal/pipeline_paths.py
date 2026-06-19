"""Shared path helpers for the job-market pipeline."""
from __future__ import annotations

import csv
import re
from functools import lru_cache
from pathlib import Path

INTERNAL_ROOT = Path(__file__).resolve().parent
JOB_MARKET_ROOT = INTERNAL_ROOT.parent

PIPELINE_DATA_DIR = INTERNAL_ROOT / "data"
SCRAPES_DIR = PIPELINE_DATA_DIR / "scrapes"
GLOBAL_DEDUP_CSV = PIPELINE_DATA_DIR / "all_jobs_dedup.csv"

BUILTIN_JSON_DIR = INTERNAL_ROOT / "jobs" / "builtin"
RAW_HTML_DIR = INTERNAL_ROOT / "jobs" / "raw"
RAW_YAML_DIR = JOB_MARKET_ROOT / "data_raw"
STRUCTURED_YAML_DIR = JOB_MARKET_ROOT / "data_structured"

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DATE_STAMP_RE = re.compile(r"^\d{8}$")
COMBINED_CSV_RE = re.compile(r"^all_jobs_(\d{8})\.csv$")
DEDUP_CSV_RE = re.compile(r"^all_jobs_(\d{8})_dedup\.csv$")


def ensure_base_dirs() -> None:
    """Create the directories used by the pipeline if they do not exist."""
    for path in (
        PIPELINE_DATA_DIR,
        SCRAPES_DIR,
        BUILTIN_JSON_DIR,
        RAW_HTML_DIR,
        RAW_YAML_DIR,
        STRUCTURED_YAML_DIR,
    ):
        path.mkdir(parents=True, exist_ok=True)


def is_scraped_date(value: str) -> bool:
    return bool(DATE_RE.fullmatch(value))


def date_to_stamp(scraped_date: str) -> str:
    """Convert YYYY-MM-DD to YYYYMMDD."""
    if not is_scraped_date(scraped_date):
        raise ValueError(f"Invalid scraped_date: {scraped_date}")
    return scraped_date.replace("-", "")


def stamp_to_date(date_stamp: str) -> str:
    """Convert YYYYMMDD to YYYY-MM-DD."""
    if not DATE_STAMP_RE.fullmatch(date_stamp):
        raise ValueError(f"Invalid date stamp: {date_stamp}")
    return f"{date_stamp[:4]}-{date_stamp[4:6]}-{date_stamp[6:8]}"


def scrape_dir(scraped_date: str) -> Path:
    """Return the per-scrape directory for CSV outputs."""
    path = SCRAPES_DIR / scraped_date
    path.mkdir(parents=True, exist_ok=True)
    return path


def combined_csv_path(scraped_date: str) -> Path:
    return scrape_dir(scraped_date) / "all_jobs.csv"


def dedup_csv_path(scraped_date: str) -> Path:
    return scrape_dir(scraped_date) / "all_jobs_dedup.csv"


def dated_dir(base_dir: Path, scraped_date: str) -> Path:
    """Return a YYYY-MM-DD subdirectory under base_dir."""
    path = base_dir / scraped_date
    path.mkdir(parents=True, exist_ok=True)
    return path


def dated_output_path(base_dir: Path, scraped_date: str, filename: str) -> Path:
    """Return a dated output path and ensure its parent directory exists."""
    return dated_dir(base_dir, scraped_date) / filename


def infer_scraped_date_from_path(path: Path) -> str | None:
    """Infer scraped_date from a YYYY-MM-DD parent directory."""
    parent_name = path.parent.name
    return parent_name if is_scraped_date(parent_name) else None


def infer_scraped_date_from_csv_path(csv_path: Path) -> str | None:
    """Infer scraped_date from a CSV path or legacy CSV filename."""
    scraped_date = infer_scraped_date_from_path(csv_path)
    if scraped_date:
        return scraped_date

    match = COMBINED_CSV_RE.match(csv_path.name) or DEDUP_CSV_RE.match(csv_path.name)
    if match:
        return stamp_to_date(match.group(1))

    return None


def infer_job_id_from_filename(path: Path) -> str:
    """Extract the Built In job ID from an HTML or YAML filename."""
    stem = path.stem
    if path.suffix.lower() == ".html":
        return stem.rsplit("_", 1)[-1]
    return stem.split("_", 1)[0]


def iter_files(base_dir: Path, pattern: str) -> list[Path]:
    """Return files under base_dir, including dated subdirectories."""
    return sorted(path for path in base_dir.rglob(pattern) if path.is_file())


def resolve_csv_path(csv_arg: str | Path, *, relative_to: Path | None = None) -> Path:
    """Resolve legacy and current CSV paths."""
    csv_path = Path(csv_arg)
    if csv_path.is_absolute() and csv_path.exists():
        return csv_path

    basename = csv_path.name
    candidates: list[Path] = []

    if not csv_path.is_absolute():
        candidates.append(Path.cwd() / csv_path)
        if relative_to is not None:
            candidates.append(relative_to / csv_path)
        candidates.extend(
            [
                INTERNAL_ROOT / csv_path,
                JOB_MARKET_ROOT / csv_path,
                PIPELINE_DATA_DIR / csv_path,
                SCRAPES_DIR / csv_path,
            ]
        )

    if basename == "all_jobs_dedup.csv":
        candidates.append(GLOBAL_DEDUP_CSV)

    combined_match = COMBINED_CSV_RE.match(basename)
    if combined_match:
        candidates.append(combined_csv_path(stamp_to_date(combined_match.group(1))))

    dedup_match = DEDUP_CSV_RE.match(basename)
    if dedup_match:
        candidates.append(dedup_csv_path(stamp_to_date(dedup_match.group(1))))

    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()

    if basename == "all_jobs_dedup.csv":
        return GLOBAL_DEDUP_CSV
    if combined_match:
        return combined_csv_path(stamp_to_date(combined_match.group(1)))
    if dedup_match:
        return dedup_csv_path(stamp_to_date(dedup_match.group(1)))

    if csv_path.is_absolute():
        return csv_path
    if relative_to is not None:
        return (relative_to / csv_path).resolve()
    return csv_path.resolve()


def resolve_nested_file(base_dir: Path, file_arg: str | Path) -> Path:
    """Resolve a file under base_dir, including dated subdirectories."""
    file_path = Path(file_arg)

    candidates: list[Path] = []
    if file_path.is_absolute():
        candidates.append(file_path)
    else:
        candidates.extend([Path.cwd() / file_path, base_dir / file_path])

    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()

    if len(file_path.parts) == 1:
        matches = sorted(path for path in base_dir.rglob(file_path.name) if path.is_file())
        if len(matches) == 1:
            return matches[0]

    return candidates[-1] if candidates else file_path


def load_csv_rows(csv_path: Path) -> list[dict[str, str]]:
    """Load rows from a pipeline CSV and backfill scraped_date when needed."""
    inferred_scraped_date = infer_scraped_date_from_csv_path(csv_path)
    rows: list[dict[str, str]] = []

    with csv_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            job_id = str(row.get("id", "") or row.get("job_id", "")).strip()
            if job_id:
                row["id"] = job_id

            scraped_date = (row.get("scraped_date") or "").strip()
            if not scraped_date and inferred_scraped_date:
                row["scraped_date"] = inferred_scraped_date

            rows.append(row)

    return rows


def load_csv_rows_by_job_id(csv_path: Path) -> dict[str, dict[str, str]]:
    """Load rows keyed by job ID."""
    return {row["id"]: row for row in load_csv_rows(csv_path) if row.get("id")}


def job_date_lookup(rows: list[dict[str, str]]) -> dict[str, str]:
    """Build a job_id -> scraped_date lookup from CSV rows."""
    return {
        row["id"]: row["scraped_date"]
        for row in rows
        if row.get("id") and row.get("scraped_date")
    }


@lru_cache(maxsize=1)
def load_global_job_dates() -> dict[str, str]:
    """Load the global job_id -> scraped_date mapping."""
    if not GLOBAL_DEDUP_CSV.exists():
        return {}
    return job_date_lookup(load_csv_rows(GLOBAL_DEDUP_CSV))


def find_scraped_date(
    job_id: str,
    *,
    path: Path | None = None,
    date_lookup: dict[str, str] | None = None,
) -> str | None:
    """Resolve scraped_date from the file path, a supplied lookup, or the global CSV."""
    if path is not None:
        scraped_date = infer_scraped_date_from_path(path)
        if scraped_date:
            return scraped_date

    if date_lookup is not None and job_id in date_lookup:
        return date_lookup[job_id]

    return load_global_job_dates().get(job_id)


ensure_base_dirs()
