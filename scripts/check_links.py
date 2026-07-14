#!/usr/bin/env python3
"""Check repository, pinned source, and install-entry links in the catalog."""

from __future__ import annotations

import argparse
import random
import ssl
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "skills.yaml"
USER_AGENT = "awesome-academic-skills-link-check/0.1 (+https://github.com/)"


@dataclass(frozen=True)
class Result:
    url: str
    ok: bool
    status: int | None
    detail: str


def request(url: str, method: str, timeout: float) -> tuple[int, str]:
    headers = {"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"}
    if method == "GET":
        headers["Range"] = "bytes=0-2047"
    req = Request(url, method=method, headers=headers)
    with urlopen(req, timeout=timeout, context=ssl.create_default_context()) as response:
        status = response.getcode()
        return status, response.geturl()


def check(url: str, timeout: float) -> Result:
    try:
        status, final_url = request(url, "HEAD", timeout)
        return Result(url, 200 <= status < 400, status, final_url)
    except HTTPError as exc:
        if exc.code not in {403, 405}:
            return Result(url, False, exc.code, str(exc.reason))
    except (URLError, TimeoutError, ssl.SSLError) as exc:
        return Result(url, False, None, str(exc))

    try:
        status, final_url = request(url, "GET", timeout)
        return Result(url, 200 <= status < 400, status, final_url)
    except HTTPError as exc:
        return Result(url, False, exc.code, str(exc.reason))
    except (URLError, TimeoutError, ssl.SSLError) as exc:
        return Result(url, False, None, str(exc))


def collect_urls(scope: str) -> list[str]:
    data = yaml.safe_load(DATA_PATH.read_text(encoding="utf-8"))
    fields = {
        "repository": ("repository_url",),
        "source": ("source_url",),
        "install": ("install_url",),
        "all": ("repository_url", "source_url", "install_url"),
    }[scope]
    urls = {
        str(item[field])
        for item in data["skills"]
        for field in fields
        if item.get(field)
    }
    return sorted(urls)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--scope",
        choices=("repository", "source", "install", "all"),
        default="all",
        help="which catalog links to check",
    )
    parser.add_argument("--timeout", type=float, default=15.0, help="per-request timeout")
    parser.add_argument("--workers", type=int, default=8, help="parallel request count")
    parser.add_argument("--sample", type=int, default=0, help="deterministic sample size; 0 checks all")
    parser.add_argument("--seed", type=int, default=0, help="sampling seed")
    args = parser.parse_args()

    urls = collect_urls(args.scope)
    if args.sample:
        if args.sample < 1:
            parser.error("--sample must be positive")
        rng = random.Random(args.seed)
        urls = sorted(rng.sample(urls, min(args.sample, len(urls))))
    if not urls:
        print("No links selected.", file=sys.stderr)
        return 1

    results: list[Result] = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {pool.submit(check, url, args.timeout): url for url in urls}
        for future in as_completed(futures):
            results.append(future.result())

    failures = 0
    for result in sorted(results, key=lambda item: item.url):
        label = "OK" if result.ok else "FAIL"
        status = str(result.status) if result.status is not None else "network"
        print(f"[{label}] {status} {result.url}")
        if not result.ok:
            failures += 1
            print(f"       {result.detail}")

    print(f"Checked {len(results)} unique link(s): {len(results) - failures} OK, {failures} failed.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
