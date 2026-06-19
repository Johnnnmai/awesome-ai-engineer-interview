# Job Scraping Pipeline

## Overview

```
Built In listing pages
  │
  ├─ scrape_builtin_requests.py  (requests + Oxylabs proxy)
  │   └─ jobs/builtin/{site}_{YYYYMMDD}.json    (per-location)
  │   └─ data/scrapes/{YYYY-MM-DD}/all_jobs.csv
  │
  ├─ clean_dedup.py
  │   └─ data/scrapes/{YYYY-MM-DD}/all_jobs_dedup.csv
  │   └─ data/all_jobs_dedup.csv                (global, all months, with scraped_date)
  │
  ├─ download_all_html.py  (requests + Oxylabs, 8 threads)
  │   └─ jobs/raw/{YYYY-MM-DD}/{title}_{job_id}.html
  │
  ├─ extract_from_html.py
  │   └─ data_raw/{YYYY-MM-DD}/{job_id}_{company}_{title}.yaml
  │
  └─ extract_llm.py  (Z.ai / GLM-4.7)
      └─ data_structured/{YYYY-MM-DD}/{job_id}_{company}_{title}.yaml
```

## Environment Variables

Set in `.env` file (in project root):

| Variable | Description |
|----------|-------------|
| `OXYLABS_ENDPOINT` | Proxy endpoint (default: `pr.oxylabs.io:7777`) |
| `OXYLABS_USER` | Oxylabs username |
| `OXYLABS_PASSWORD` | Oxylabs password |
| `ZAI_API_KEY` | Z.ai API key (Anthropic-compatible) |

## Directory Structure

```
job-market/
├── _internal/                    # Pipeline scripts and intermediate data
│   ├── scrapers/
│   │   ├── scrape_builtin_requests.py   # Step 1: Scrape listings
│   │   ├── download_all_html.py         # Step 3: Download job pages
│   │   ├── extract_from_html.py         # Step 4: HTML → YAML
│   │   └── pagination/                  # Legacy Playwright scraper
│   │   ├── clean_dedup.py               # Step 2: Deduplication
│   ├── data/
│   │   ├── all_jobs_dedup.csv           # Global dedup CSV (all months, with scraped_date)
│   │   └── scrapes/{YYYY-MM-DD}/
│   │       ├── all_jobs.csv             # Raw combined listings for one scrape
│   │       └── all_jobs_dedup.csv       # Deduplicated new jobs for one scrape
│   ├── extract_llm.py                   # Step 5: LLM enrichment
│   └── jobs/
│       ├── builtin/                     # Per-site JSON files
│       └── raw/{YYYY-MM-DD}/            # Downloaded HTML pages grouped by scrape date
├── data_raw/{YYYY-MM-DD}/        # Extracted YAML grouped by scrape date
├── data_structured/{YYYY-MM-DD}/ # LLM-enriched YAML grouped by scrape date
└── analysis.ipynb                # Analysis notebook
```

## Steps

### Step 1: Scrape Listings

```bash
cd job-market/_internal
python scrapers/scrape_builtin_requests.py
```

- Scrapes all 5 Built In locations (LA, Berlin, London, Amsterdam, New York)
- Saves per-location JSONs: `jobs/builtin/{site}_{YYYYMMDD}.json`
- Combines into: `data/scrapes/{YYYY-MM-DD}/all_jobs.csv`
- Pass site names to scrape specific locations: `python scrapers/scrape_builtin_requests.py la berlin`
- Pass `--date 2026-03-15` to override date stamp

If requests fails (Built In requires JS rendering), fall back to the Playwright scraper in `scrapers/pagination/scrape_builtin_cards.py`.

### Step 2: Deduplicate

```bash
python scrapers/clean_dedup.py data/scrapes/{YYYY-MM-DD}/all_jobs.csv
```

- Removes spam companies (Alignerr)
- Deduplicates within the scrape by (title, company)
- Removes IDs already in global `data/all_jobs_dedup.csv`
- Saves date-specific: `data/scrapes/{YYYY-MM-DD}/all_jobs_dedup.csv`
- Appends new jobs to global: `data/all_jobs_dedup.csv` (with `scraped_date` column)

### Step 3: Download HTML

```bash
python scrapers/download_all_html.py --csv data/scrapes/{YYYY-MM-DD}/all_jobs_dedup.csv
```

- Downloads full job pages for each URL in the CSV
- 8 concurrent threads, 3 retries per URL
- Skips already-downloaded files across `jobs/raw/`
- Failed URLs saved to `jobs/queue/failed_urls.txt`

### Step 4: Extract to YAML

```bash
python scrapers/extract_from_html.py --all --csv data/scrapes/{YYYY-MM-DD}/all_jobs_dedup.csv
```

- Parses HTML files and extracts structured job data
- Primary source: JSON-LD structured data
- Fallback: HTML parsing (title, skills, company size)
- Output: `data_raw/{YYYY-MM-DD}/{job_id}_{company}_{title}.yaml`

### Step 5: LLM Enrichment

```bash
python extract_llm.py --all --csv data/scrapes/{YYYY-MM-DD}/all_jobs_dedup.csv
```

- Sends each job description to Z.ai (GLM-4.7)
- Classifies AI type (ai-first, ml-first, ai-support)
- Extracts skills by category, responsibilities, use cases
- Skips already-processed files
- Output: `data_structured/{YYYY-MM-DD}/{job_id}_{company}_{title}.yaml`

## Deduplication Strategy

1. **Spam removal**: Filter out known spam companies (e.g., Alignerr)
2. **Within-scrape dedup**: `drop_duplicates(subset=['title', 'company'])`
3. **Cross-month dedup**: Remove IDs already in global `data/all_jobs_dedup.csv`

Job IDs are extracted from Built In URLs (last path segment) and are stable across scrapes. The global `data/all_jobs_dedup.csv` is the single source of truth for which jobs have been processed and which dated folder a job belongs to.

## Running for a New Month

```bash
cd job-market/_internal

# 1. Scrape
python scrapers/scrape_builtin_requests.py

# 2. Dedup
python scrapers/clean_dedup.py data/scrapes/{YYYY-MM-DD}/all_jobs.csv

# 3. Download HTML
python scrapers/download_all_html.py --csv data/scrapes/{YYYY-MM-DD}/all_jobs_dedup.csv

# 4. Extract YAML
python scrapers/extract_from_html.py --all --csv data/scrapes/{YYYY-MM-DD}/all_jobs_dedup.csv

# 5. LLM enrichment
python extract_llm.py --all --csv data/scrapes/{YYYY-MM-DD}/all_jobs_dedup.csv

# 6. Re-run analysis.ipynb on combined dataset
```

All months' data accumulates under dated folders in `data_raw/` and `data_structured/` — the analysis notebook and helper scripts read those directories recursively.
