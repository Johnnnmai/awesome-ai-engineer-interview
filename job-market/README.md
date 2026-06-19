# Job Market Data

2,445 AI Engineer job descriptions from builtin.com (January - March 2026) covering LA (Global), New York, London, Amsterdam, Berlin, and India.

For analysis and insights based on this data, see [role/](../role/).

## Contents

- [data_structured/](data_structured/) - structured YAML files grouped into `YYYY-MM-DD/` scrape-date folders
- [data_raw/](data_raw/) - raw extracted YAML files grouped into `YYYY-MM-DD/` scrape-date folders
- [analysis.ipynb](analysis.ipynb) - Jupyter notebook with data analysis
- [_internal/](_internal/) - scraping scripts, processing scripts, and `_internal/data/` for pipeline CSVs

## Highlights

- 1,683 jobs (72.0%) are AI-First (RAG, agents, LLMs)
- 593 jobs (25.4%) are AI-Support (platforms, infrastructure, tooling)
- 48 jobs (2.1%) are traditional ML rebranded as "AI Engineer"
- 1,172 unique companies, led by Capital One (47), Jack & Jill AI (27), Optum (26)

Top skills:

- Python (82.7%), TypeScript (20.8%), Java (18.3%)
- RAG (34.5%), LLMs (21.2%), prompt engineering (18.0%)
- AWS (41.3%), Docker (32.6%), Kubernetes (28.3%)
- LangChain (23.1%), PyTorch (22.5%), SQL (21.0%)

## Data Format

Each YAML file in `data_structured/YYYY-MM-DD/` contains:

```yaml
title: Senior AI/Data Engineer
company: WorkWave
location: USA
work_type: FULL_TIME
level: Expert/Leader
skills: [Python, AWS, Airflow, dbt]
company_size: 1,000 Employees
compensation: $160,000 - $180,000/year
description: |
  Full job description...
posted_date: 2026-01-18
url: https://builtin.com/job/...
source: Built In
```
