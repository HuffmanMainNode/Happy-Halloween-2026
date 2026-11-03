#!/usr/bin/env python3
"""Validate the Halloween collection manifest without network access."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def repository_parts(value: str):
    parsed = urlsplit(value)
    try:
        port_ok = parsed.port in (None, 443)
    except ValueError:
        return None
    if (
        parsed.scheme != "https"
        or parsed.hostname != "github.com"
        or parsed.username is not None
        or parsed.password is not None
        or not port_ok
        or parsed.query
        or parsed.fragment
    ):
        return None
    parts = [part for part in parsed.path.strip("/").split("/") if part]
    if len(parts) != 2 or not all(parts):
        return None
    return parts[0], parts[1].removesuffix(".git")


def validate_manifest(data: object) -> list[str]:
    errors = []
    if not isinstance(data, dict):
        return ["manifest must be a JSON object"]
    if data.get("schema_version") != "1.0.0":
        errors.append("schema_version must be 1.0.0")
    for field in ("collection", "maintainer", "tagline"):
        value = data.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{field} must be a non-empty string")
    if not isinstance(data.get("projects"), list) or not data["projects"]:
        return errors + ["projects must be a non-empty array"]

    seen_ids = set()
    for index, project in enumerate(data["projects"]):
        prefix = f"projects[{index}]"
        if not isinstance(project, dict):
            errors.append(f"{prefix} must be an object")
            continue
        project_id = project.get("id")
        if not isinstance(project_id, str) or not SLUG.fullmatch(project_id):
            errors.append(f"{prefix}.id must be a lowercase slug")
        elif project_id in seen_ids:
            errors.append(f"{prefix}.id is duplicated: {project_id}")
        else:
            seen_ids.add(project_id)

        for field in ("name", "purpose"):
            value = project.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{prefix}.{field} must be a non-empty string")

        repo_url = project.get("repository")
        repo_parts = repository_parts(repo_url) if isinstance(repo_url, str) else None
        if repo_parts is None:
            errors.append(f"{prefix}.repository must be an HTTPS GitHub owner/repository URL")
            continue

        for field in ("human_guide", "agent_guide"):
            guide = project.get(field)
            guide_parts = repository_parts(guide) if isinstance(guide, str) else None
            if guide_parts != repo_parts or not isinstance(guide, str) or "/blob/main/" not in guide:
                errors.append(f"{prefix}.{field} must point to a Markdown guide in the same repository")
            elif not guide.lower().endswith(".md"):
                errors.append(f"{prefix}.{field} must point to a Markdown file")

    limitations = data.get("limitations")
    if not isinstance(limitations, list) or not all(
        isinstance(item, str) and item.strip() for item in limitations
    ):
        errors.append("limitations must be an array of non-empty strings")
    return errors


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", default="collection.json")
    args = parser.parse_args(argv)
    try:
        data = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"Manifest read failed: {type(error).__name__}", file=sys.stderr)
        return 2
    errors = validate_manifest(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Valid collection manifest: {len(data['projects'])} projects")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
