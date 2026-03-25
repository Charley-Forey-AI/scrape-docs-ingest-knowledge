# Vista Help One-Time Scrape

This folder stores markdown content scraped from the Vista help menu links.

## Inputs

- `input/nav_tree.html` - source nav snippet with `a[href]` entries.

## Script

- `scripts/scrape_vista_help.py`

## Run

From repo root:

```powershell
python "scripts/scrape_vista_help.py" --dry-run
python "scripts/scrape_vista_help.py" --clean-output
```

Optional:

```powershell
python "scripts/scrape_vista_help.py" --limit 3
python "scripts/scrape_vista_help.py" --delay-s 1.0
python "scripts/scrape_vista_help.py" --base-url "https://help.trimble.com"
python "scripts/scrape_vista_help.py" --no-discover-nav
```

By default, the script discovers deeper pages from each fetched page's vertical nav tree (`id="navTreeScrollView"`), so you get nested submenu pages (not just top-level links).

## Output Layout

- `pages/**.md` - one markdown file per menu URL, path mirrors URL hierarchy.
- `manifest.json` - run metadata and URL-to-file mapping.
- `errors.json` - failures encountered during the run.

## Validation Checklist

- Run `--dry-run` and confirm extracted URL count.
- Run full scrape and check terminal summary (`Success`, `Failed`).
- Open 2-3 files in `pages/` and verify:
  - YAML front matter includes `title`, `source_url`, `fetched_at`, `menu_path`.
  - Body content is present and readable markdown.
- Confirm `manifest.json` and `errors.json` were updated.
