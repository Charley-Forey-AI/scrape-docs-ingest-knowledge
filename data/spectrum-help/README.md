# Spectrum Help One-Time Scrape

This folder stores markdown content scraped from the Spectrum help menu links.

## Inputs

- `input/nav_tree.html` - source nav snippet with `a[href]` entries.

## Script

- `scripts/scrape_spectrum_help.py`

## Run

From repo root:

```powershell
python "scripts/scrape_spectrum_help.py" --dry-run
python "scripts/scrape_spectrum_help.py" --clean-output
```

Optional:

```powershell
python "scripts/scrape_spectrum_help.py" --limit 3
python "scripts/scrape_spectrum_help.py" --delay-s 1.0
python "scripts/scrape_spectrum_help.py" --base-url "https://help.trimble.com"
python "scripts/scrape_spectrum_help.py" --no-discover-nav
python "scripts/scrape_spectrum_help.py" --skip-existing
python "scripts/scrape_spectrum_help.py" --retry-failed-from-manifest "data/spectrum-help/manifest.json"
```

By default, the script discovers deeper pages from each fetched page's vertical nav tree (`id="navTreeScrollView"`), so you get nested submenu pages (not just top-level links).

## Output Layout

- `pages/**.md` - one markdown file per menu URL, path mirrors URL hierarchy.
- `manifest.json` - run metadata and URL-to-file mapping.
- `errors.json` - failures encountered during the run.

## Validation Checklist

- Run `--dry-run` and confirm extracted URL count.
- Run full scrape with resilient network settings:
  - `python "scripts/scrape_spectrum_help.py" --clean-output --request-timeout-s 60 --request-retries 5 --delay-s 0`
- Run full scrape and check terminal summary (`Success`, `Failed`).
- Open 2-3 files in `pages/` and verify:
  - YAML front matter includes `title`, `source_url`, `fetched_at`, `menu_path`.
  - Body content is present and readable markdown.
- Confirm `manifest.json` and `errors.json` were updated.
- Confirm `manifest.json` has:
  - `discovery_warning_count: 0` (or inspect `discovery_warnings` when non-zero)
  - `error_count: 0`
  - `skipped_existing_count` (when using `--skip-existing`)
  - `total_urls` much larger than the 14 seed links when deep discovery succeeds.
