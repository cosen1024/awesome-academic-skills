#!/usr/bin/env python3
"""Validate the structure and curation invariants of data/skills.yaml."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "data" / "skills.yaml"
REQUIRED_CATEGORIES = {
    "ideas",
    "literature-search",
    "reading-knowledge",
    "research-design",
    "experiment-code",
    "data-analysis",
    "paper-writing",
    "polishing-translation",
    "citation-latex",
    "scientific-plotting",
    "pre-submission",
    "peer-review-response",
    "end-to-end",
}
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def iso_date(value: object) -> str | None:
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, str):
        try:
            return date.fromisoformat(value).isoformat()
        except ValueError:
            return None
    return None


def is_https_github(url: object) -> bool:
    if not isinstance(url, str):
        return False
    parsed = urlparse(url)
    return parsed.scheme == "https" and parsed.netloc.lower() == "github.com"


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        return [f"cannot load {path}: {exc}"]

    if not isinstance(data, dict):
        return ["catalog root must be a mapping"]
    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    catalog_date = iso_date(data.get("last_verified"))
    if not catalog_date:
        errors.append("last_verified must be an ISO date")

    categories = data.get("categories")
    if not isinstance(categories, list):
        return errors + ["categories must be a list"]
    category_ids = [item.get("id") for item in categories if isinstance(item, dict)]
    if len(category_ids) != len(set(category_ids)):
        errors.append("category ids must be unique")
    if set(category_ids) != REQUIRED_CATEGORIES:
        missing = sorted(REQUIRED_CATEGORIES - set(category_ids))
        extra = sorted(set(category_ids) - REQUIRED_CATEGORIES)
        errors.append(f"category set mismatch; missing={missing}, extra={extra}")
    for index, item in enumerate(categories):
        if not isinstance(item, dict):
            errors.append(f"categories[{index}] must be a mapping")
            continue
        for field in ("id", "name_zh", "name_en"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"categories[{index}].{field} must be non-empty")

    skills = data.get("skills")
    if not isinstance(skills, list):
        return errors + ["skills must be a list"]
    if len(skills) < 20:
        errors.append(f"catalog must contain at least 20 skills, got {len(skills)}")

    seen_ids: set[str] = set()
    seen_sources: set[tuple[str, str]] = set()
    category_counts: Counter[str] = Counter()

    required_strings = (
        "id",
        "category",
        "entry_type",
        "repository",
        "repository_url",
        "license",
        "source_ref",
        "skill",
        "skill_path",
        "source_url",
        "purpose_zh",
        "purpose_en",
        "install_method",
        "install_url",
        "verification_status",
        "notes_zh",
        "notes_en",
    )

    for index, item in enumerate(skills):
        prefix = f"skills[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be a mapping")
            continue
        for field in required_strings:
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"{prefix}.{field} must be a non-empty string")

        skill_id = item.get("id")
        if isinstance(skill_id, str):
            if not ID_RE.fullmatch(skill_id):
                errors.append(f"{prefix}.id must use lowercase kebab-case")
            if skill_id in seen_ids:
                errors.append(f"duplicate skill id: {skill_id}")
            seen_ids.add(skill_id)

        category = item.get("category")
        if category not in REQUIRED_CATEGORIES:
            errors.append(f"{prefix}.category is unknown: {category!r}")
        elif isinstance(category, str):
            category_counts[category] += 1

        if item.get("entry_type") not in {"skill", "skill-suite", "plugin"}:
            errors.append(f"{prefix}.entry_type must be skill, skill-suite, or plugin")
        if not is_https_github(item.get("repository_url")):
            errors.append(f"{prefix}.repository_url must be an https://github.com URL")
        if not is_https_github(item.get("source_url")):
            errors.append(f"{prefix}.source_url must be an https://github.com URL")
        if not is_https_github(item.get("install_url")):
            errors.append(f"{prefix}.install_url must be an https://github.com URL")

        source_ref = item.get("source_ref")
        if not isinstance(source_ref, str) or not SHA_RE.fullmatch(source_ref):
            errors.append(f"{prefix}.source_ref must be a full 40-character commit SHA")
        else:
            if source_ref not in str(item.get("source_url", "")):
                errors.append(f"{prefix}.source_url must be pinned to source_ref")
            if source_ref not in str(item.get("install_url", "")):
                errors.append(f"{prefix}.install_url must be pinned to source_ref")

        skill_path = item.get("skill_path")
        if isinstance(skill_path, str):
            if not skill_path.endswith("SKILL.md"):
                errors.append(f"{prefix}.skill_path must point to SKILL.md")
            if skill_path not in unquote(str(item.get("source_url", ""))):
                errors.append(f"{prefix}.source_url must contain skill_path")

        platforms = item.get("platforms")
        if not isinstance(platforms, list) or not platforms or not all(
            isinstance(value, str) and value.strip() for value in platforms
        ):
            errors.append(f"{prefix}.platforms must be a non-empty string list")

        if not item.get("install_command") and not item.get("install_url"):
            errors.append(f"{prefix} needs an install command or entry URL")
        if item.get("verification_status") != "verified":
            errors.append(f"{prefix}.verification_status must be verified in the main catalog")
        verified_at = iso_date(item.get("verified_at"))
        if not verified_at:
            errors.append(f"{prefix}.verified_at must be an ISO date")
        elif catalog_date and verified_at != catalog_date:
            errors.append(f"{prefix}.verified_at must match catalog last_verified")

        source_key = (str(item.get("repository")), str(item.get("skill")))
        if source_key in seen_sources:
            errors.append(f"duplicate repository/skill pair: {source_key}")
        seen_sources.add(source_key)

    uncovered = sorted(REQUIRED_CATEGORIES - set(category_counts))
    if uncovered:
        errors.append(f"categories without entries: {uncovered}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=DEFAULT_DATA)
    args = parser.parse_args()
    errors = validate(args.path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    data = yaml.safe_load(args.path.read_text(encoding="utf-8"))
    print(
        f"OK: {len(data['skills'])} entries across "
        f"{len(data['categories'])} categories ({data['last_verified']})."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
