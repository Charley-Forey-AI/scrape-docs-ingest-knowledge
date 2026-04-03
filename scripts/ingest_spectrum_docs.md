# Spectrum Docs Ingestion Script

Use `scripts/ingest_spectrum_docs.py` to upload all markdown files under `data/spectrum` into the Trimble Ingestion API, with tags derived from folder ancestry.

## What It Does

- Scans only the folder you pass as `--root-dir` (default: `data/spectrum`)
- Finds every `*.md` file in that tree
- Builds tags from all ancestor folders above each file
  - Example: `data/spectrum/hr-and-payroll/payroll/payments/file.md`
  - Tags: `["spectrum", "hr-and-payroll", "payroll", "payments"]`
- Creates an ingestion job (`POST /v1/jobs`)
- Uploads content to returned pre-signed `uploadUrl` (`PUT`)
- Polls the job (`GET /v1/jobs/{jobId}`) until `COMPLETED` or `FAILED`
- Writes resumable state to `scripts/.spectrum_ingest_state.json`
- Uses `chunkerOptions.strategy=text` by default (valid API enum)
- Processes files concurrently with worker threads (`--workers`)

## Required `.env` Values

The script reads values from `.env` (or environment variables):

- `TRIMBLE_ACCESS_TOKEN` (preferred; direct bearer token auth)
- `TRIMBLE_INGEST_URL`
- `TRIMBLE_KNOWLEDGE_LIBRARY_ID`
- `TRIMBLE_TOKEN_URL`
- `TRIMBLE_CLIENT_ID`
- `TRIMBLE_CLIENT_SECRET`
- Optional: `TRIMBLE_REFRESH_TOKEN` (preferred for user-context auth)
- Optional: `TRIMBLE_SCOPE`
- Optional: `TRIMBLE_KB_URL` (preferred if you want to force kbUrl in payload)
- Optional: `TRIMBLE_KNOWLEDGE_URL` (legacy fallback; only used when it already points to `kb.*`)
- Optional: `TRIMBLE_APP_NAME`

## Dry Run First

```powershell
python scripts/ingest_spectrum_docs.py --dry-run --limit 10
```

## Real Run

```powershell
python scripts/ingest_spectrum_docs.py
```

High-throughput submit-only mode (create jobs + upload, no polling):

```powershell
python scripts/ingest_spectrum_docs.py --root-dir "data/spectrum-help/pages" --workers 32 --no-wait-for-completion
```

## Helpful Options

- `--root-dir data/spectrum`
- `--state-file scripts/.spectrum_ingest_state.json`
- `--limit 100`
- `--poll-timeout-s 1800`
- `--poll-interval-s 3`
- `--max-retries 5`
- `--workers 16`
- `--force-reprocess`
- `--no-root-tag`
- `--content-type text/markdown`
- `--chunking-strategy text`
- `--include-file-uri` (off by default)
- `--kb-url https://kb.stage.trimble-ai.com`
- `--no-wait-for-completion` (submit jobs without polling)

## If You See HTTP 422

- The script now prints the API response body for 4xx/5xx errors.
- Common fix already applied: chunking strategy is now valid (`text` instead of invalid `markdown`).
- If error mentions `Failed to call kbUrl`, set `--kb-url https://kb.stage.trimble-ai.com` or `TRIMBLE_KB_URL=https://kb.stage.trimble-ai.com`.

## Authentication Behavior

- If `TRIMBLE_ACCESS_TOKEN` is present, the script uses it directly for `Authorization: Bearer ...`.
- Compatibility fallback: if `TRIMBLE_ACCESS_TOKEN` is missing and `TRIMBLE_AUTHORIZATION_CODE` looks like a JWT, it is used as bearer token.
- If not present, it falls back to OAuth token endpoint flow (`refresh_token` first, then `client_credentials`).

## Resume Behavior

- Completed files are skipped automatically on the next run.
- If the process stops mid-run, re-run the same command and it continues from remaining files.
- Use `--force-reprocess` to process files even if they were already marked completed.

## Throughput Tips for 6000+ Files

- Start with `--workers 16` and increase to `24` or `32` if your network and API rate limits allow.
- Keep `--poll-interval-s` at `2-3` seconds for good responsiveness without over-polling.
- If you hit `429`/`5xx`, reduce workers (for example from `16` to `8`).
- Run continuously; the state file lets you resume safely after interruptions.
- For fastest submission throughput, use `--no-wait-for-completion` so each worker starts the next file immediately after upload.
