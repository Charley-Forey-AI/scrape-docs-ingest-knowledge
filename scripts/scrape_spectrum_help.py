#!/usr/bin/env python3
"""
One-time scraper for Spectrum help docs.

- Reads menu links from data/spectrum-help/input/nav_tree.html
- Fetches each page from help.trimble.com
- Converts HTML content to markdown
- Saves markdown to data/spectrum-help/pages/ mirroring URL path hierarchy
- Writes manifest.json and errors.json
"""

from __future__ import annotations

import argparse
import html
import http.client
import json
import re
import socket
import ssl
import shutil
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse, urlunparse
from urllib.request import Request, urlopen


BASE_URL = "https://help.trimble.com"
DEFAULT_INPUT = Path("data/spectrum-help/input/nav_tree.html")
DEFAULT_OUTPUT_ROOT = Path("data/spectrum-help")
PAGES_DIRNAME = "pages"
MANIFEST_FILENAME = "manifest.json"
ERRORS_FILENAME = "errors.json"
NAV_ROOT_ID = "navTreeScrollView"
DOCS_PATH_PREFIX = "/en/spectrum/spectrum/"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def slugify_filename(value: str) -> str:
    safe = re.sub(r"[^a-zA-Z0-9._-]+", "-", value.strip())
    safe = safe.strip("-._")
    return safe or "index"


def canonicalize_url(raw_href: str, base_url: str) -> tuple[str, str]:
    absolute = urljoin(base_url, raw_href)
    parsed = urlparse(absolute)
    clean = parsed._replace(query="", fragment="")
    normalized_url = urlunparse(clean)
    menu_path = clean.path or "/"
    return normalized_url, menu_path


class NavHrefParser(HTMLParser):
    def __init__(self, scope_element_id: str | None = None) -> None:
        super().__init__()
        self.hrefs: list[str] = []
        self.scope_element_id = scope_element_id
        self._in_scope = scope_element_id is None
        self._scope_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if self.scope_element_id is not None:
            attrs_dict = {k.lower(): v for k, v in attrs}
            if not self._in_scope and attrs_dict.get("id") == self.scope_element_id:
                self._in_scope = True
                self._scope_depth = 1
            elif self._in_scope:
                self._scope_depth += 1

        if not self._in_scope:
            return
        if tag.lower() != "a":
            return
        for key, val in attrs:
            if key.lower() == "href" and val:
                self.hrefs.append(val.strip())
                break

    def handle_endtag(self, tag: str) -> None:
        if self.scope_element_id is None or not self._in_scope:
            return
        self._scope_depth -= 1
        if self._scope_depth <= 0:
            self._in_scope = False
            self._scope_depth = 0


def extract_menu_urls(
    nav_html: str,
    base_url: str,
    scope_element_id: str | None = None,
    docs_path_prefix: str = DOCS_PATH_PREFIX,
) -> list[dict[str, str]]:
    parser = NavHrefParser(scope_element_id=scope_element_id)
    parser.feed(nav_html)

    seen: set[str] = set()
    items: list[dict[str, str]] = []
    for href in parser.hrefs:
        normalized_url, menu_path = canonicalize_url(href, base_url)
        if not menu_path.startswith(docs_path_prefix):
            continue
        if normalized_url in seen:
            continue
        seen.add(normalized_url)
        items.append(
            {
                "href": href,
                "url": normalized_url,
                "menu_path": menu_path,
            }
        )
    return items


def fetch_url(url: str, retries: int = 3, timeout_s: int = 30) -> str:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            req = Request(
                url,
                headers={
                    "User-Agent": (
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/122.0 Safari/537.36"
                    ),
                    # Help avoid partial/chunked transport edge-cases.
                    "Accept-Encoding": "identity",
                    "Connection": "close",
                },
            )
            with urlopen(req, timeout=timeout_s) as resp:
                charset = resp.headers.get_content_charset() or "utf-8"
                return resp.read().decode(charset, errors="replace")
        except (
            HTTPError,
            URLError,
            TimeoutError,
            ValueError,
            socket.timeout,
            ssl.SSLError,
            ConnectionResetError,
            http.client.IncompleteRead,
        ) as exc:
            last_error = exc
            if attempt < retries:
                sleep_s = min(12.0, (2 ** (attempt - 1)) + 0.3 * attempt)
                time.sleep(sleep_s)
                continue
            raise RuntimeError(f"Failed to fetch {url}: {exc}") from exc
    if last_error:
        raise RuntimeError(f"Failed to fetch {url}: {last_error}") from last_error
    raise RuntimeError(f"Failed to fetch {url}: unknown error")


def short_url(url: str, max_len: int = 110) -> str:
    if len(url) <= max_len:
        return url
    return url[: max_len - 3] + "..."


def load_failed_items_from_manifest(manifest_path: Path, base_url: str) -> list[dict[str, str]]:
    if not manifest_path.exists():
        raise RuntimeError(f"Manifest file not found: {manifest_path}")
    try:
        payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Manifest is not valid JSON: {manifest_path}") from exc

    results = payload.get("results")
    if not isinstance(results, list):
        raise RuntimeError(f"Manifest missing 'results' array: {manifest_path}")

    items: list[dict[str, str]] = []
    seen: set[str] = set()
    for row in results:
        if not isinstance(row, dict):
            continue
        if str(row.get("status", "")).lower() != "error":
            continue
        raw_url = row.get("url")
        raw_menu_path = row.get("menu_path")
        if not isinstance(raw_url, str) or not raw_url.strip():
            continue
        normalized_url, fallback_menu_path = canonicalize_url(raw_url, base_url)
        menu_path = raw_menu_path if isinstance(raw_menu_path, str) and raw_menu_path.strip() else fallback_menu_path
        if normalized_url in seen:
            continue
        seen.add(normalized_url)
        items.append(
            {
                "href": normalized_url,
                "url": normalized_url,
                "menu_path": menu_path,
            }
        )
    return items


def _extract_first_block(html_text: str, tag_names: Iterable[str]) -> str | None:
    for tag in tag_names:
        pattern = re.compile(rf"<{tag}\b[^>]*>.*?</{tag}>", re.IGNORECASE | re.DOTALL)
        match = pattern.search(html_text)
        if match:
            return match.group(0)
    return None


def extract_primary_html(html_text: str) -> str:
    # Prioritize semantic containers commonly used in docs pages.
    primary = _extract_first_block(html_text, ("main", "article"))
    if primary:
        return primary

    # Fallback to body content if no explicit article/main blocks.
    body = _extract_first_block(html_text, ("body",))
    return body if body else html_text


def html_title(html_text: str) -> str:
    match = re.search(r"<title[^>]*>(.*?)</title>", html_text, re.IGNORECASE | re.DOTALL)
    if not match:
        return "Untitled"
    title = re.sub(r"\s+", " ", html.unescape(match.group(1))).strip()
    return title or "Untitled"


class HtmlToMarkdownParser(HTMLParser):
    BLOCK_BREAK_TAGS = {
        "div",
        "section",
        "article",
        "main",
        "header",
        "footer",
        "aside",
        "nav",
        "p",
        "ul",
        "ol",
        "li",
        "table",
        "tr",
        "blockquote",
        "pre",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "br",
    }

    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.list_stack: list[str] = []
        self.link_stack: list[str | None] = []
        self.skip_depth = 0

    def _append(self, text: str) -> None:
        if text:
            self.parts.append(text)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "noscript"}:
            self.skip_depth += 1
            return
        if self.skip_depth > 0:
            return

        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            level = int(tag[1])
            self._append("\n" + ("#" * level) + " ")
            return
        if tag in {"strong", "b"}:
            self._append("**")
            return
        if tag in {"em", "i"}:
            self._append("*")
            return
        if tag == "code":
            self._append("`")
            return
        if tag == "pre":
            self._append("\n```\n")
            return
        if tag in {"ul", "ol"}:
            self.list_stack.append(tag)
            self._append("\n")
            return
        if tag == "li":
            marker = "- "
            if self.list_stack and self.list_stack[-1] == "ol":
                marker = "1. "
            self._append("\n" + marker)
            return
        if tag == "a":
            href = None
            for key, val in attrs:
                if key.lower() == "href":
                    href = val
                    break
            self.link_stack.append(href)
            self._append("[")
            return
        if tag == "blockquote":
            self._append("\n> ")
            return
        if tag == "br":
            self._append("\n")
            return
        if tag == "hr":
            self._append("\n---\n")
            return

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "noscript"}:
            if self.skip_depth > 0:
                self.skip_depth -= 1
            return
        if self.skip_depth > 0:
            return

        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self._append("\n\n")
            return
        if tag in {"strong", "b"}:
            self._append("**")
            return
        if tag in {"em", "i"}:
            self._append("*")
            return
        if tag == "code":
            self._append("`")
            return
        if tag == "pre":
            self._append("\n```\n")
            return
        if tag in {"ul", "ol"}:
            if self.list_stack:
                self.list_stack.pop()
            self._append("\n")
            return
        if tag == "a":
            href = self.link_stack.pop() if self.link_stack else None
            if href:
                self._append(f"]({href})")
            else:
                self._append("]")
            return
        if tag in self.BLOCK_BREAK_TAGS:
            self._append("\n")

    def handle_data(self, data: str) -> None:
        if self.skip_depth > 0:
            return
        text = html.unescape(data)
        # Keep paragraph-level readability while avoiding huge whitespace runs.
        text = re.sub(r"[ \t\r\f\v]+", " ", text)
        if text.strip():
            self._append(text)

    def markdown(self) -> str:
        joined = "".join(self.parts)
        # Cleanup spacing and repeated blank lines.
        joined = re.sub(r"\n{3,}", "\n\n", joined)
        joined = re.sub(r" +\n", "\n", joined)
        return joined.strip() + "\n"


def html_to_markdown(html_fragment: str) -> str:
    parser = HtmlToMarkdownParser()
    parser.feed(html_fragment)
    return parser.markdown()


def menu_path_to_markdown_path(output_root: Path, menu_path: str) -> Path:
    pages_root = output_root / PAGES_DIRNAME
    parsed = urlparse(menu_path)
    clean_path = parsed.path if parsed.path else menu_path
    clean_path = clean_path.strip("/")
    if not clean_path:
        return pages_root / "index.md"
    path_obj = Path(clean_path)
    if path_obj.suffix:
        stem = slugify_filename(path_obj.stem)
        parent = path_obj.parent
        return pages_root / parent / f"{stem}.md"
    return pages_root / clean_path / "index.md" if clean_path.endswith("/") else pages_root / f"{clean_path}.md"


def front_matter(title: str, source_url: str, fetched_at: str, menu_path: str) -> str:
    return (
        "---\n"
        f"title: {json.dumps(title)}\n"
        f"source_url: {json.dumps(source_url)}\n"
        f"fetched_at: {json.dumps(fetched_at)}\n"
        f"menu_path: {json.dumps(menu_path)}\n"
        "---\n\n"
    )


@dataclass
class CrawlResult:
    href: str
    url: str
    menu_path: str
    output_file: str | None
    status: str
    title: str | None = None
    error: str | None = None
    discovered_from_url: str | None = None


def run(
    input_file: Path,
    output_root: Path,
    base_url: str,
    delay_s: float,
    dry_run: bool,
    limit: int | None,
    discover_nav: bool,
    clean_output: bool,
    max_urls: int,
    request_timeout_s: int,
    request_retries: int,
    discovery_log_every: int,
    retry_failed_from_manifest: Path | None,
    skip_existing: bool,
) -> int:
    if retry_failed_from_manifest is not None:
        seed_menu_items = load_failed_items_from_manifest(
            retry_failed_from_manifest.resolve(),
            base_url=base_url,
        )
        print(f"Loaded failed URLs from manifest: {retry_failed_from_manifest.as_posix()}")
    else:
        nav_html = input_file.read_text(encoding="utf-8")
        seed_menu_items = extract_menu_urls(nav_html, base_url=base_url)

    if limit is not None:
        seed_menu_items = seed_menu_items[:limit]

    print(f"Extracted seed menu URLs: {len(seed_menu_items)}")
    if not seed_menu_items:
        if retry_failed_from_manifest is not None:
            print("No failed URLs found in manifest; nothing to retry.")
            return 0
        print("No URLs found. Check nav_tree.html content.")
        return 1

    for item in seed_menu_items[:5]:
        print(f"- {item['url']} -> {item['menu_path']}")

    if dry_run:
        print("\nDry run complete; no pages fetched.")
        return 0

    pages_root = output_root / PAGES_DIRNAME
    if clean_output and output_root.exists():
        if pages_root.exists():
            shutil.rmtree(pages_root, ignore_errors=True)
        manifest_path = output_root / MANIFEST_FILENAME
        if manifest_path.exists():
            manifest_path.unlink()
        errors_path = output_root / ERRORS_FILENAME
        if errors_path.exists():
            errors_path.unlink()

    output_root.mkdir(parents=True, exist_ok=True)
    pages_root.mkdir(parents=True, exist_ok=True)

    ordered_items: dict[str, dict[str, str | None]] = {
        item["url"]: {
            "href": item["href"],
            "url": item["url"],
            "menu_path": item["menu_path"],
            "discovered_from_url": None,
        }
        for item in seed_menu_items
    }
    html_cache: dict[str, str] = {}
    discovery_warnings: list[dict[str, str]] = []

    if discover_nav:
        if retry_failed_from_manifest is not None:
            print("\nSkipping nav discovery because --retry-failed-from-manifest was provided.")
        else:
            print("\nDiscovering deeper menu links from page nav trees...")
    if discover_nav and retry_failed_from_manifest is None:
        queue: list[str] = list(ordered_items.keys())
        scanned: set[str] = set()
        discovered_from_nav_count = 0

        while queue:
            page_url = queue.pop(0)
            if page_url in scanned:
                continue
            scanned.add(page_url)
            discover_idx = len(scanned)
            queue_remaining_before = len(queue)
            print(
                f"[discover {discover_idx}] fetching {short_url(page_url)} "
                f"(queue_remaining={queue_remaining_before}, total_known={len(ordered_items)})"
            )
            started_at = time.time()
            try:
                page_html = fetch_url(
                    page_url,
                    retries=request_retries,
                    timeout_s=request_timeout_s,
                )
                html_cache[page_url] = page_html
                added_this_page = 0
                discovered = extract_menu_urls(
                    page_html,
                    base_url=base_url,
                    scope_element_id=NAV_ROOT_ID,
                )
                discovered_fallback = extract_menu_urls(
                    page_html,
                    base_url=base_url,
                    scope_element_id=None,
                )
                for item in [*discovered, *discovered_fallback]:
                    if len(ordered_items) >= max_urls:
                        break
                    url = item["url"]
                    if url in ordered_items:
                        continue
                    ordered_items[url] = {
                        "href": item["href"],
                        "url": item["url"],
                        "menu_path": item["menu_path"],
                        "discovered_from_url": page_url,
                    }
                    queue.append(url)
                    added_this_page += 1
                    discovered_from_nav_count += 1

                elapsed_s = time.time() - started_at
                print(
                    f"  -> ok in {elapsed_s:.1f}s, added_this_page={added_this_page}, "
                    f"added_total={discovered_from_nav_count}, queue_now={len(queue)}, total_known={len(ordered_items)}"
                )
                if discovery_log_every > 0 and discover_idx % discovery_log_every == 0:
                    print(
                        f"  discovery progress: scanned={discover_idx}, "
                        f"known_urls={len(ordered_items)}, queue={len(queue)}"
                    )
                if len(ordered_items) >= max_urls:
                    print(f"Reached max URL cap ({max_urls}); stopping discovery.")
                    break
                time.sleep(delay_s)
            except Exception as exc:  # noqa: BLE001 - one-time batch script
                discovery_warnings.append({"url": page_url, "error": str(exc)})
                elapsed_s = time.time() - started_at
                print(f"  Discovery warning ({elapsed_s:.1f}s) for {page_url}: {exc}")

        print(f"Discovered total menu URLs: {len(ordered_items)}")
        if discovery_warnings:
            print(f"Discovery warnings: {len(discovery_warnings)}")

    menu_items: list[dict[str, str | None]] = list(ordered_items.values())

    fetched_at = utc_now_iso()
    results: list[CrawlResult] = []
    errors: list[dict[str, str]] = []
    skipped_existing_count = 0

    for idx, item in enumerate(menu_items, start=1):
        href = item["href"]
        url = item["url"]
        menu_path = item["menu_path"]
        discovered_from_url = item.get("discovered_from_url")
        md_path = menu_path_to_markdown_path(output_root, str(menu_path))
        if skip_existing and md_path.exists():
            skipped_existing_count += 1
            print(f"[{idx}/{len(menu_items)}] Skipping existing {url}")
            results.append(
                CrawlResult(
                    href=str(href),
                    url=str(url),
                    menu_path=str(menu_path),
                    output_file=str(md_path.as_posix()),
                    status="skipped-existing",
                    discovered_from_url=str(discovered_from_url) if discovered_from_url else None,
                )
            )
            continue

        print(f"[{idx}/{len(menu_items)}] Fetching {url}")

        try:
            raw_html = html_cache.get(url) or fetch_url(
                url,
                retries=request_retries,
                timeout_s=request_timeout_s,
            )
            title = html_title(raw_html)
            primary_html = extract_primary_html(raw_html)
            markdown_body = html_to_markdown(primary_html)
            md_path.parent.mkdir(parents=True, exist_ok=True)
            md_text = front_matter(
                title=title,
                source_url=url,
                fetched_at=fetched_at,
                menu_path=menu_path,
            ) + markdown_body
            md_path.write_text(md_text, encoding="utf-8")

            results.append(
                CrawlResult(
                    href=href,
                    url=url,
                    menu_path=menu_path,
                    output_file=str(md_path.as_posix()),
                    status="ok",
                    title=title,
                    discovered_from_url=discovered_from_url,
                )
            )
            time.sleep(delay_s)
        except Exception as exc:  # noqa: BLE001 - one-time batch script
            err = str(exc)
            results.append(
                CrawlResult(
                    href=href,
                    url=url,
                    menu_path=menu_path,
                    output_file=None,
                    status="error",
                    error=err,
                    discovered_from_url=discovered_from_url,
                )
            )
            errors.append({"url": url, "menu_path": menu_path, "error": err})
            print(f"  ERROR: {err}")

    manifest = {
        "generated_at": utc_now_iso(),
        "base_url": base_url,
        "input_file": str(input_file.as_posix()),
        "discover_nav": discover_nav,
        "nav_scope_element_id": NAV_ROOT_ID if discover_nav else None,
        "total_urls": len(menu_items),
        "ok_count": sum(1 for r in results if r.status == "ok"),
        "error_count": sum(1 for r in results if r.status == "error"),
        "skipped_existing_count": skipped_existing_count,
        "discovery_warning_count": len(discovery_warnings),
        "discovery_warnings": discovery_warnings,
        "results": [r.__dict__ for r in results],
    }

    (output_root / MANIFEST_FILENAME).write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (output_root / ERRORS_FILENAME).write_text(
        json.dumps(
            {
                "generated_at": utc_now_iso(),
                "errors": errors,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    print("\nDone.")
    print(f"  Success: {manifest['ok_count']}")
    print(f"  Failed:  {manifest['error_count']}")
    print(f"  Skipped existing: {manifest['skipped_existing_count']}")
    print(f"  Manifest: {(output_root / MANIFEST_FILENAME).as_posix()}")
    print(f"  Errors:   {(output_root / ERRORS_FILENAME).as_posix()}")
    return 0 if manifest["error_count"] == 0 else 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="One-time scraper for Spectrum help menu URLs into markdown."
    )
    parser.add_argument(
        "--input-file",
        type=Path,
        default=DEFAULT_INPUT,
        help="Path to nav HTML snippet containing menu links.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help="Root output directory for markdown pages and manifests.",
    )
    parser.add_argument(
        "--base-url",
        default=BASE_URL,
        help="Base URL prepended to relative href values.",
    )
    parser.add_argument(
        "--delay-s",
        type=float,
        default=0.5,
        help="Polite delay between successful requests.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only parse and print extracted URLs (no fetch/write).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional limit on number of menu URLs to process.",
    )
    parser.add_argument(
        "--discover-nav",
        dest="discover_nav",
        action="store_true",
        help="Discover deeper links from each page's vertical nav tree.",
    )
    parser.add_argument(
        "--no-discover-nav",
        dest="discover_nav",
        action="store_false",
        help="Disable nav-tree discovery and only scrape input-file links.",
    )
    parser.set_defaults(discover_nav=True)
    parser.add_argument(
        "--clean-output",
        action="store_true",
        help="Delete prior pages/manifest/errors under output-root before scraping.",
    )
    parser.add_argument(
        "--max-urls",
        type=int,
        default=20000,
        help="Maximum number of discovered docs URLs to process.",
    )
    parser.add_argument(
        "--request-timeout-s",
        type=int,
        default=12,
        help="HTTP request timeout in seconds.",
    )
    parser.add_argument(
        "--request-retries",
        type=int,
        default=2,
        help="Retry count per URL request.",
    )
    parser.add_argument(
        "--discovery-log-every",
        type=int,
        default=1,
        help="Print discovery progress summary every N scanned URLs (0 disables).",
    )
    parser.add_argument(
        "--retry-failed-from-manifest",
        type=Path,
        default=None,
        help="Retry only URLs that failed in a prior manifest.json file.",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip fetching pages that already exist on disk under output-root/pages.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return run(
        input_file=args.input_file,
        output_root=args.output_root,
        base_url=args.base_url,
        delay_s=args.delay_s,
        dry_run=args.dry_run,
        limit=args.limit,
        discover_nav=args.discover_nav,
        clean_output=args.clean_output,
        max_urls=args.max_urls,
        request_timeout_s=args.request_timeout_s,
        request_retries=args.request_retries,
        discovery_log_every=args.discovery_log_every,
        retry_failed_from_manifest=args.retry_failed_from_manifest,
        skip_existing=args.skip_existing,
    )


if __name__ == "__main__":
    raise SystemExit(main())
