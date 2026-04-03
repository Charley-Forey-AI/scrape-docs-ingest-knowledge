# scrape-docs-ingest-knowledge

Reusable scripts to scrape help documentation sites and ingest the generated markdown into Trimble Knowledge.

This repo is set up with Spectrum examples, but the workflow is generic:

1. Export nav links from a help site.
2. Scrape pages and convert to markdown.
3. Bulk ingest markdown into a Knowledge library.

## Repo Layout

- `scripts/scrape_spectrum_help.py` - Scrapes help pages to markdown files.
- `scripts/ingest_spectrum_docs.py` - Ingests markdown files into Trimble Ingestion API.
- `scripts/ingest_spectrum_docs.md` - Detailed ingest script usage.
- `data/spectrum-help/` - Input nav, generated pages, manifest, and errors.
- `.env.example` - Required environment variable template.

## Prerequisites

- Python 3.11+ (3.12+ recommended)
- Access to Trimble Knowledge/Ingress endpoints
- API credentials or bearer token

## Quick Start

### 1) Create and activate a virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2) Configure environment variables

Copy `.env.example` to `.env` and fill values:

```powershell
Copy-Item .env.example .env
```

Required values for ingestion are typically:

- `TRIMBLE_INGEST_URL`
- `TRIMBLE_KNOWLEDGE_LIBRARY_ID`
- `TRIMBLE_ACCESS_TOKEN` (preferred), or OAuth client values

## Scrape Help Docs

Use a nav tree HTML file as input and write pages under `data/spectrum-help/pages`.

```powershell
python scripts/scrape_spectrum_help.py
```

Common outputs:

- `data/spectrum-help/pages/...` markdown files
- `data/spectrum-help/manifest.json`
- `data/spectrum-help/errors.json`

## Ingest Markdown

Dry run first:

```powershell
python scripts/ingest_spectrum_docs.py --root-dir "data/spectrum-help/pages" --dry-run --limit 10
```

Full run:

```powershell
python scripts/ingest_spectrum_docs.py --root-dir "data/spectrum-help/pages"
```

High-throughput submit mode (no polling):

```powershell
python scripts/ingest_spectrum_docs.py --root-dir "data/spectrum-help/pages" --workers 32 --no-wait-for-completion
```

## Notes

- The ingest script supports resumable state via `scripts/.spectrum_ingest_state.json`.
- Tags are derived from folder ancestry under `--root-dir`.
- If you hit long-path issues on Windows, run Git commands with long path support enabled.

## Example Source

Spectrum documentation source used by this repo:

- https://help.trimble.com/en
