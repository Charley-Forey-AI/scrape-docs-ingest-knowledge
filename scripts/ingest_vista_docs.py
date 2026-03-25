#!/usr/bin/env python3
"""
Bulk-ingest Vista markdown files into Trimble Agent Studio Knowledge ingestion service.

Workflow per file:
1) POST /v1/jobs with source metadata, document ID, and tags
2) PUT markdown bytes to the returned pre-signed uploadUrl
3) Poll GET /v1/jobs/{jobId} until COMPLETED or FAILED

Tags are derived from the file's parent folders (all ancestors under root-dir).
Example:
  data/vista/hr-and-payroll/payroll/payments/foo.md
  -> tags: ["vista", "hr-and-payroll", "payroll", "payments"]
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import sys
import threading
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urljoin
from urllib.request import Request, urlopen


DEFAULT_ROOT_DIR = Path("data/vista")
DEFAULT_STATE_FILE = Path("scripts/.vista_ingest_state.json")
DEFAULT_CONTENT_TYPE = "text/markdown"
DEFAULT_CHUNKING_STRATEGY = "text"
DEFAULT_POLL_INTERVAL_S = 3.0
DEFAULT_POLL_TIMEOUT_S = 900.0
DEFAULT_HTTP_TIMEOUT_S = 60
DEFAULT_MAX_RETRIES = 5

TERMINAL_JOB_STATES = {"COMPLETED", "FAILED"}
SUCCESS_JOB_STATE = "COMPLETED"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def to_iso(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()


def parse_env_file(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    values: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            values[key] = value
    return values


def env_or_file(env_file_values: dict[str, str], key: str, default: str | None = None) -> str | None:
    return os.environ.get(key) or env_file_values.get(key) or default


def sanitize_actor_slug(app_name: str) -> str:
    cleaned = []
    for ch in app_name.lower():
        if ch.isalnum():
            cleaned.append(ch)
        elif ch in {"-", "_", " "}:
            cleaned.append("-")
    slug = "".join(cleaned).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "vista-docs-ingest"


def build_document_id(relative_path: Path) -> str:
    digest = hashlib.sha1(relative_path.as_posix().encode("utf-8")).hexdigest()[:24]
    return f"vista-{digest}"


def trim_tag(tag: str, max_len: int = 64) -> str:
    if len(tag) <= max_len:
        return tag
    return tag[:max_len]


def build_tags(relative_path: Path, include_root_tag: bool, root_tag: str) -> list[str]:
    tags: list[str] = []
    seen: set[str] = set()

    if include_root_tag:
        normalized_root_tag = trim_tag(root_tag.strip())
        if normalized_root_tag and normalized_root_tag not in seen:
            tags.append(normalized_root_tag)
            seen.add(normalized_root_tag)

    for part in relative_path.parent.parts:
        normalized = trim_tag(part.strip())
        if normalized and normalized not in seen:
            tags.append(normalized)
            seen.add(normalized)

    # API allows max 50 tags.
    return tags[:50]


@dataclass
class HttpResult:
    status: int
    headers: dict[str, str]
    body_bytes: bytes


class ApiError(RuntimeError):
    def __init__(self, message: str, status: int | None = None, body: str | None = None):
        super().__init__(message)
        self.status = status
        self.body = body


def http_request(
    *,
    method: str,
    url: str,
    headers: dict[str, str] | None = None,
    body_bytes: bytes | None = None,
    timeout_s: int = DEFAULT_HTTP_TIMEOUT_S,
) -> HttpResult:
    req = Request(url=url, data=body_bytes, method=method)
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    try:
        with urlopen(req, timeout=timeout_s) as resp:
            response_body = resp.read()
            response_headers = {k.lower(): v for k, v in resp.headers.items()}
            return HttpResult(status=resp.status, headers=response_headers, body_bytes=response_body)
    except HTTPError as exc:
        err_body = b""
        try:
            err_body = exc.read()
        except Exception:  # noqa: BLE001
            pass
        response_headers = {k.lower(): v for k, v in exc.headers.items()} if exc.headers else {}
        raise ApiError(
            f"HTTP {exc.code} for {method} {url}",
            status=exc.code,
            body=err_body.decode("utf-8", errors="replace"),
        ) from exc
    except URLError as exc:
        raise ApiError(f"Network error for {method} {url}: {exc}") from exc


class TokenManager:
    def __init__(
        self,
        *,
        token_url: str,
        client_id: str,
        client_secret: str,
        scope: str | None,
        refresh_token: str | None,
        static_access_token: str | None,
        timeout_s: int,
    ) -> None:
        self.token_url = token_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope
        self.refresh_token = refresh_token
        self.static_access_token = static_access_token.strip() if static_access_token else None
        self.timeout_s = timeout_s
        self._lock = threading.Lock()

        self._access_token: str | None = None
        self._expires_at_epoch: float = 0.0

    @staticmethod
    def _scope_for_client_credentials(scope: str | None) -> str | None:
        if not scope:
            return None
        parts = [s for s in scope.split() if s]
        # openid/profile-like scopes are typically user-centric and can fail for client_credentials.
        deny = {"openid", "profile", "offline_access"}
        filtered = [s for s in parts if s not in deny]
        return " ".join(filtered) if filtered else None

    def _request_token_with_payload(self, payload: dict[str, str]) -> tuple[str, int]:
        body = urlencode(payload).encode("utf-8")
        result = http_request(
            method="POST",
            url=self.token_url,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            body_bytes=body,
            timeout_s=self.timeout_s,
        )
        if result.status != 200:
            raise ApiError(
                f"Token endpoint returned status {result.status}",
                status=result.status,
                body=result.body_bytes.decode("utf-8", errors="replace"),
            )
        data = json.loads(result.body_bytes.decode("utf-8"))
        access_token = data.get("access_token")
        expires_in = int(data.get("expires_in", 3600))
        if not access_token:
            raise ApiError("Token response does not include access_token")
        new_refresh = data.get("refresh_token")
        if isinstance(new_refresh, str) and new_refresh:
            self.refresh_token = new_refresh
        return access_token, expires_in

    def _request_token(self) -> tuple[str, int]:
        base = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        errors: list[str] = []
        if self.refresh_token:
            payload = dict(base)
            payload.update(
                {
                    "grant_type": "refresh_token",
                    "refresh_token": self.refresh_token,
                }
            )
            try:
                return self._request_token_with_payload(payload)
            except ApiError as exc:
                errors.append(f"refresh_token grant failed: {exc} body={exc.body}")
                print("  Warning: refresh token grant failed; falling back to client_credentials.")
                # Fall through to client_credentials fallback.

        payload = dict(base)
        payload["grant_type"] = "client_credentials"
        scope = self._scope_for_client_credentials(self.scope)
        if scope:
            payload["scope"] = scope
        try:
            return self._request_token_with_payload(payload)
        except ApiError as exc:
            errors.append(f"client_credentials grant failed: {exc} body={exc.body}")
            raise ApiError("Unable to acquire access token. " + " | ".join(errors)) from exc

    def get_access_token(self) -> str:
        if self.static_access_token:
            return self.static_access_token
        with self._lock:
            now = time.time()
            # Refresh token if token is missing or close to expiry (60s leeway).
            if self._access_token and now < (self._expires_at_epoch - 60):
                return self._access_token
            token, expires_in = self._request_token()
            self._access_token = token
            self._expires_at_epoch = time.time() + max(60, expires_in)
            return token


def should_retry_status(status: int | None) -> bool:
    if status is None:
        return True
    return status in {408, 425, 429, 500, 502, 503, 504}


def call_ingest_json(
    *,
    token_manager: TokenManager,
    method: str,
    url: str,
    body_obj: dict[str, Any] | None,
    timeout_s: int,
    max_retries: int,
) -> dict[str, Any]:
    body_bytes = json.dumps(body_obj).encode("utf-8") if body_obj is not None else None
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    attempt = 0
    while True:
        attempt += 1
        try:
            token = token_manager.get_access_token()
            merged_headers = dict(headers)
            merged_headers["Authorization"] = f"Bearer {token}"
            result = http_request(
                method=method,
                url=url,
                headers=merged_headers,
                body_bytes=body_bytes,
                timeout_s=timeout_s,
            )
            if not result.body_bytes:
                return {}
            return json.loads(result.body_bytes.decode("utf-8"))
        except ApiError as exc:
            if attempt >= max_retries or not should_retry_status(exc.status):
                raise
            backoff_s = min(20.0, (2 ** (attempt - 1)) + 0.2 * attempt)
            print(f"  Retry {attempt}/{max_retries} for {method} {url} after error: {exc}")
            time.sleep(backoff_s)


def upload_file_to_presigned_url(
    upload_url: str,
    file_path: Path,
    content_type: str,
    timeout_s: int,
    max_retries: int,
) -> None:
    payload = file_path.read_bytes()
    headers = {"Content-Type": content_type}
    attempt = 0
    while True:
        attempt += 1
        try:
            result = http_request(
                method="PUT",
                url=upload_url,
                headers=headers,
                body_bytes=payload,
                timeout_s=timeout_s,
            )
            if result.status not in {200, 201, 202, 204}:
                raise ApiError(f"Upload failed with status={result.status}", status=result.status)
            return
        except ApiError as exc:
            if attempt >= max_retries or not should_retry_status(exc.status):
                raise
            backoff_s = min(20.0, (2 ** (attempt - 1)) + 0.2 * attempt)
            print(f"  Retry {attempt}/{max_retries} for upload after error: {exc}")
            time.sleep(backoff_s)


def poll_job_until_terminal(
    *,
    ingest_base_url: str,
    job_id: str,
    token_manager: TokenManager,
    interval_s: float,
    timeout_s: float,
    request_timeout_s: int,
    max_retries: int,
    log_prefix: str = "",
    log_fn: Callable[[str], None] | None = None,
) -> dict[str, Any]:
    deadline = time.time() + timeout_s
    endpoint = urljoin(ingest_base_url.rstrip("/") + "/", f"v1/jobs/{job_id}")
    last_status = "UNKNOWN"

    while time.time() < deadline:
        payload = call_ingest_json(
            token_manager=token_manager,
            method="GET",
            url=endpoint,
            body_obj=None,
            timeout_s=request_timeout_s,
            max_retries=max_retries,
        )
        status = str(payload.get("status", "UNKNOWN"))
        if status != last_status:
            msg = f"{log_prefix}job={job_id} status={status}".strip()
            if log_fn:
                log_fn(msg)
            else:
                print(msg)
            last_status = status
        if status in TERMINAL_JOB_STATES:
            return payload
        time.sleep(interval_s)

    raise TimeoutError(f"Timed out waiting for job {job_id}; last status={last_status}")


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"version": 1, "files": {}}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        raise RuntimeError(f"State file is not valid JSON: {path}")
    if not isinstance(data, dict):
        raise RuntimeError(f"State file has invalid format: {path}")
    data.setdefault("version", 1)
    data.setdefault("files", {})
    return data


def save_state(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2), encoding="utf-8")


def list_markdown_files(root_dir: Path) -> list[Path]:
    files = [p for p in root_dir.rglob("*.md") if p.is_file()]
    files.sort(key=lambda p: p.as_posix())
    return files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Bulk ingest markdown files from a folder tree into Trimble Ingestion API.")
    parser.add_argument("--root-dir", type=Path, default=DEFAULT_ROOT_DIR, help="Folder to scan for .md files.")
    parser.add_argument("--env-file", type=Path, default=Path(".env"), help="Path to .env containing Trimble credentials.")
    parser.add_argument("--state-file", type=Path, default=DEFAULT_STATE_FILE, help="JSON state file for resumable processing.")
    parser.add_argument("--limit", type=int, default=None, help="Optional max number of files to process.")
    parser.add_argument("--poll-interval-s", type=float, default=DEFAULT_POLL_INTERVAL_S, help="Job poll interval in seconds.")
    parser.add_argument("--poll-timeout-s", type=float, default=DEFAULT_POLL_TIMEOUT_S, help="Max seconds to wait per job.")
    parser.add_argument("--http-timeout-s", type=int, default=DEFAULT_HTTP_TIMEOUT_S, help="HTTP timeout for each request.")
    parser.add_argument("--max-retries", type=int, default=DEFAULT_MAX_RETRIES, help="Retry attempts for transient API/network errors.")
    parser.add_argument(
        "--workers",
        type=int,
        default=8,
        help="Number of files to ingest concurrently.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Do not call APIs. Show planned file/tag/document mapping only.")
    parser.add_argument("--force-reprocess", action="store_true", help="Reprocess files even if already marked completed in state.")
    parser.add_argument("--no-root-tag", action="store_true", help="Do not include root folder name as a tag.")
    parser.add_argument("--kb-url", default=None, help="Override kbUrl in CreateJob request.")
    parser.add_argument("--content-type", default=DEFAULT_CONTENT_TYPE, help="Source content type for markdown files.")
    parser.add_argument(
        "--chunking-strategy",
        default=DEFAULT_CHUNKING_STRATEGY,
        choices=["text", "code", "json", "openapi", "auto"],
        help="Chunking strategy passed to chunkerOptions.strategy.",
    )
    parser.add_argument(
        "--include-file-uri",
        action="store_true",
        help="Include source.uri as a local file:// URI. Disabled by default.",
    )
    return parser.parse_args()


def required(value: str | None, name: str) -> str:
    if value and value.strip():
        return value.strip()
    raise RuntimeError(f"Missing required configuration: {name}")


def looks_like_jwt(value: str | None) -> bool:
    if not value:
        return False
    parts = value.strip().split(".")
    return len(parts) == 3 and all(parts)


def select_kb_url(env_values: dict[str, str], override: str | None) -> str | None:
    if override:
        return override

    explicit_kb_url = env_or_file(env_values, "TRIMBLE_KB_URL")
    if explicit_kb_url:
        return explicit_kb_url

    # Backward-compatible fallback, but avoid passing clearly invalid/non-KB hosts.
    legacy_knowledge_url = env_or_file(env_values, "TRIMBLE_KNOWLEDGE_URL")
    if legacy_knowledge_url and "://kb." in legacy_knowledge_url:
        return legacy_knowledge_url
    return None


def main() -> int:
    args = parse_args()
    root_dir = args.root_dir.resolve()
    if not root_dir.exists() or not root_dir.is_dir():
        raise RuntimeError(f"Root folder does not exist or is not a directory: {root_dir}")

    env_values = parse_env_file(args.env_file)
    ingest_base_url = required(env_or_file(env_values, "TRIMBLE_INGEST_URL"), "TRIMBLE_INGEST_URL")
    library_id = required(env_or_file(env_values, "TRIMBLE_KNOWLEDGE_LIBRARY_ID"), "TRIMBLE_KNOWLEDGE_LIBRARY_ID")
    token_url = required(env_or_file(env_values, "TRIMBLE_TOKEN_URL"), "TRIMBLE_TOKEN_URL")
    client_id = required(env_or_file(env_values, "TRIMBLE_CLIENT_ID"), "TRIMBLE_CLIENT_ID")
    client_secret = required(env_or_file(env_values, "TRIMBLE_CLIENT_SECRET"), "TRIMBLE_CLIENT_SECRET")
    scope = env_or_file(env_values, "TRIMBLE_SCOPE", "openid kb-ingest profile")
    refresh_token = env_or_file(env_values, "TRIMBLE_REFRESH_TOKEN")
    static_access_token = env_or_file(env_values, "TRIMBLE_ACCESS_TOKEN")
    # Backward compatibility: some local setups store a bearer JWT under this legacy key.
    if not static_access_token:
        legacy_auth_code = env_or_file(env_values, "TRIMBLE_AUTHORIZATION_CODE")
        if looks_like_jwt(legacy_auth_code):
            static_access_token = legacy_auth_code
    app_name = env_or_file(env_values, "TRIMBLE_APP_NAME", "vista-docs-ingest") or "vista-docs-ingest"

    actor_id = f"applications:{sanitize_actor_slug(app_name)}"
    include_root_tag = not args.no_root_tag
    root_tag = root_dir.name
    kb_url = select_kb_url(env_values, args.kb_url)

    files = list_markdown_files(root_dir)
    if args.limit is not None:
        files = files[: args.limit]
    if not files:
        print(f"No markdown files found under: {root_dir}")
        return 0

    state = load_state(args.state_file.resolve())
    state["rootDir"] = str(root_dir)
    state["updatedAt"] = utc_now_iso()
    state_files: dict[str, Any] = state.setdefault("files", {})

    print(f"Root dir: {root_dir}")
    print(f"Files found: {len(files)}")
    print(f"State file: {args.state_file.resolve()}")
    print(f"Dry run: {args.dry_run}")
    print(f"Chunking strategy: {args.chunking_strategy}")
    print(f"Include file URI: {args.include_file_uri}")
    print(f"kbUrl override: {kb_url if kb_url else '(service default)'}")
    print(f"Auth mode: {'static access token' if static_access_token else 'oauth token endpoint'}")
    print(f"Workers: {args.workers}")

    token_manager = TokenManager(
        token_url=token_url,
        client_id=client_id,
        client_secret=client_secret,
        scope=scope,
        refresh_token=refresh_token,
        static_access_token=static_access_token,
        timeout_s=args.http_timeout_s,
    )

    state_path = args.state_file.resolve()
    state_lock = threading.Lock()
    print_lock = threading.Lock()

    completed = 0
    failed = 0
    skipped = 0

    pending: list[tuple[int, Path]] = []
    for idx, file_path in enumerate(files, start=1):
        rel_path = file_path.relative_to(root_dir)
        rel_key = rel_path.as_posix()
        existing = state_files.get(rel_key, {})
        if (not args.force_reprocess) and existing.get("status") == "completed":
            skipped += 1
            print(f"[{idx}/{len(files)}] skip completed: {rel_key}")
            continue
        pending.append((idx, file_path))

    def format_api_error(exc: ApiError) -> str:
        detail = f"{exc}"
        if exc.body:
            body = exc.body.strip()
            if len(body) > 1500:
                body = body[:1500] + "... [truncated]"
            detail = f"{detail} | body={body}"
        return detail

    def process_file(idx: int, file_path: Path) -> bool:
        rel_path = file_path.relative_to(root_dir)
        rel_key = rel_path.as_posix()
        tags = build_tags(rel_path, include_root_tag=include_root_tag, root_tag=root_tag)
        document_id = build_document_id(rel_path)
        stat = file_path.stat()
        created_at = to_iso(stat.st_ctime)
        updated_at = to_iso(stat.st_mtime)

        with print_lock:
            print(f"[{idx}/{len(files)}] ingest: {rel_key} | tags={len(tags)}")

        with state_lock:
            existing = state_files.get(rel_key, {})
            state_record: dict[str, Any] = {
                "status": "processing",
                "documentId": document_id,
                "tags": tags,
                "updatedAt": utc_now_iso(),
                "attempts": int(existing.get("attempts", 0)) + 1,
            }
            state_files[rel_key] = state_record
            save_state(state_path, state)

        if args.dry_run:
            with state_lock:
                state_record["status"] = "dry-run"
                state_record["updatedAt"] = utc_now_iso()
                save_state(state_path, state)
            return True

        try:
            def log_safe(message: str) -> None:
                with print_lock:
                    print(message)

            source_obj: dict[str, Any] = {
                "createdAt": created_at,
                "createdBy": actor_id,
                "updatedAt": updated_at,
                "updatedBy": actor_id,
                "contentType": args.content_type,
                "title": rel_path.name,
                "size": stat.st_size,
            }
            if args.include_file_uri:
                source_obj["uri"] = file_path.resolve().as_uri()

            create_payload: dict[str, Any] = {
                "libraryId": library_id,
                "documentId": document_id,
                "source": source_obj,
                "chunkerOptions": {"strategy": args.chunking_strategy},
                "tags": tags,
            }
            if kb_url:
                create_payload["kbUrl"] = kb_url

            create_url = urljoin(ingest_base_url.rstrip("/") + "/", "v1/jobs")
            create_resp = call_ingest_json(
                token_manager=token_manager,
                method="POST",
                url=create_url,
                body_obj=create_payload,
                timeout_s=args.http_timeout_s,
                max_retries=args.max_retries,
            )
            job_id = str(create_resp.get("id", ""))
            upload_url = create_resp.get("uploadUrl")
            if not job_id:
                raise RuntimeError(f"CreateJob response is missing id for {rel_key}")

            if isinstance(upload_url, str) and upload_url:
                upload_file_to_presigned_url(
                    upload_url=upload_url,
                    file_path=file_path,
                    content_type=args.content_type,
                    timeout_s=args.http_timeout_s,
                    max_retries=args.max_retries,
                )

            final_job = poll_job_until_terminal(
                ingest_base_url=ingest_base_url,
                job_id=job_id,
                token_manager=token_manager,
                interval_s=args.poll_interval_s,
                timeout_s=args.poll_timeout_s,
                request_timeout_s=args.http_timeout_s,
                max_retries=args.max_retries,
                log_prefix=f"[{idx}/{len(files)}] ",
                log_fn=log_safe,
            )
            final_status = str(final_job.get("status", "UNKNOWN"))

            with state_lock:
                state_record = state_files[rel_key]
                state_record["jobId"] = job_id
                state_record["finalStatus"] = final_status
                state_record["completedAt"] = utc_now_iso()
                state_record["updatedAt"] = utc_now_iso()
                if final_status == SUCCESS_JOB_STATE:
                    state_record["status"] = "completed"
                    save_state(state_path, state)
                    return True
                state_record["status"] = "failed"
                state_record["lastError"] = final_job.get("error") or f"Job ended with status={final_status}"
                save_state(state_path, state)
                return False

        except Exception as exc:  # noqa: BLE001 - batch script should continue
            error_message = format_api_error(exc) if isinstance(exc, ApiError) else str(exc)
            with state_lock:
                state_record = state_files[rel_key]
                state_record["status"] = "failed"
                state_record["lastError"] = error_message
                state_record["updatedAt"] = utc_now_iso()
                save_state(state_path, state)
            with print_lock:
                print(f"  ERROR: {rel_key}: {error_message}")
            return False

    if args.workers < 1:
        raise RuntimeError("--workers must be >= 1")

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(process_file, idx, file_path) for idx, file_path in pending]
        for fut in concurrent.futures.as_completed(futures):
            ok = fut.result()
            if ok:
                completed += 1
            else:
                failed += 1

    print("")
    print("Ingestion run finished.")
    print(f"  completed: {completed}")
    print(f"  failed:    {failed}")
    print(f"  skipped:   {skipped}")
    print(f"  state:     {args.state_file.resolve()}")
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user.", file=sys.stderr)
        raise SystemExit(130)
