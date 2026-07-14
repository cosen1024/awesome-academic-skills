#!/usr/bin/env python3
"""Render the catalog tables in README.md and README_EN.md from YAML."""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "skills.yaml"
START = "<!-- CATALOG:START -->"
END = "<!-- CATALOG:END -->"
BLOCK_RE = re.compile(rf"{re.escape(START)}.*?{re.escape(END)}", re.DOTALL)


def cell(value: object) -> str:
    return html.escape(str(value), quote=False).replace("|", "&#124;").replace("\n", " ")


def render_catalog(data: dict[str, object], language: str) -> str:
    skills = data["skills"]
    assert isinstance(skills, list)
    lines = [START]
    for category in data["categories"]:
        assert isinstance(category, dict)
        category_id = category["id"]
        title = category["name_zh" if language == "zh" else "name_en"]
        table_header = (
            "| 仓库 / Skill | 用途 |"
            if language == "zh"
            else "| Repository / Skill | Purpose |"
        )
        lines.extend(
            [
                "",
                f"### {title}",
                "",
                table_header,
                "|---|---|",
            ]
        )
        for item in skills:
            assert isinstance(item, dict)
            if item["category"] != category_id:
                continue
            repository = cell(item["repository"])
            skill = cell(item["skill"])
            source_url = item["source_url"]
            repository_url = item["repository_url"]
            purpose = item["purpose_zh" if language == "zh" else "purpose_en"]
            row = (
                f"| [{repository}]({repository_url})<br>[{skill}]({source_url}) "
                f"| {cell(purpose)} |"
            )
            lines.append(row)
    lines.extend(["", END])
    return "\n".join(lines)


def update_readme(path: Path, catalog: str, write: bool) -> bool:
    content = path.read_text(encoding="utf-8")
    if not BLOCK_RE.search(content):
        raise ValueError(f"catalog markers not found in {path}")
    rendered = BLOCK_RE.sub(catalog, content)
    if rendered == content:
        print(f"OK: {path.name} is up to date")
        return True
    if write:
        path.write_text(rendered, encoding="utf-8")
        print(f"UPDATED: {path.name}")
        return True
    print(f"STALE: {path.name}; run scripts/render_readmes.py --write", file=sys.stderr)
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="fail if generated blocks are stale")
    mode.add_argument("--write", action="store_true", help="rewrite generated blocks")
    args = parser.parse_args()

    data = yaml.safe_load(DATA_PATH.read_text(encoding="utf-8"))
    targets = ((ROOT / "README.md", "zh"), (ROOT / "README_EN.md", "en"))
    results = [
        update_readme(path, render_catalog(data, language), args.write)
        for path, language in targets
    ]
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
