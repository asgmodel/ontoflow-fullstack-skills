#!/usr/bin/env python3
"""Create a small, repeatable audit of a web project's UI and integration surface.

The audit is intentionally heuristic. It points an agent to files that need review;
it does not certify a project or replace type checks, builds, API tests, or a browser run.
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path
from typing import Iterable


IGNORED_DIRS = {
    ".git",
    ".next",
    ".nuxt",
    ".svelte-kit",
    "node_modules",
    "dist",
    "build",
    "coverage",
    "bin",
    "obj",
    ".venv",
    "venv",
    "__pycache__",
}
TEXT_EXTENSIONS = {
    ".cs",
    ".cjs",
    ".css",
    ".html",
    ".js",
    ".jsx",
    ".json",
    ".mjs",
    ".py",
    ".scss",
    ".svelte",
    ".ts",
    ".tsx",
    ".vue",
    ".yaml",
    ".yml",
}
UI_EXTENSIONS = {".js", ".jsx", ".svelte", ".ts", ".tsx", ".vue"}
MAX_FILE_BYTES = 1_500_000
MAX_FINDINGS_PER_KIND = 80

ROUTE_PATTERNS = (
    re.compile(r"\bpath\s*[:=]\s*[\"']([^\"']+)[\"']"),
    re.compile(r"\bto\s*=\s*[\"'](/[^\"']*)[\"']"),
    re.compile(r"\[Route\(\s*[\"']([^\"']+)[\"']"),
)
API_PATTERNS = (
    re.compile(r"\bfetch\s*\("),
    re.compile(r"\baxios(?:\.[a-z]+)?\s*\("),
    re.compile(r"\b(?:http|api)Client\b"),
    re.compile(r"\b(?:GET|POST|PUT|PATCH|DELETE)\s+[/\w{}:-]+"),
    re.compile(r"\[\s*Http(?:Get|Post|Put|Patch|Delete)\b", re.I),
)
MOCK_PATTERNS = (
    re.compile(r"\b(?:mock|mocks|fixture|fixtures|dummy|fake|stub|stubs)\b", re.I),
    re.compile(r"\b(?:sampleData|demoData|placeholder|coming\s+soon|lorem\s+ipsum)\b", re.I),
    re.compile(r"\blocalStorage\b"),
)
SECRET_PATTERNS = (
    re.compile(r"\bsk_(?:live|test|sandbox)_[A-Za-z0-9_-]{12,}\b"),
    re.compile(r"\bBearer\s+[A-Za-z0-9._-]{24,}\b"),
    re.compile(
        r"\b(?:api[_-]?key|client[_-]?secret|connection[_-]?string|password|secret)\s*"
        r"[:=]\s*[\"'][^\"']{8,}[\"']",
        re.I,
    ),
)


def iter_files(root: Path) -> Iterable[Path]:
    """Yield readable project text files while skipping generated/vendor trees."""

    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        if any(part in IGNORED_DIRS for part in path.relative_to(root).parts):
            continue
        try:
            if path.stat().st_size > MAX_FILE_BYTES:
                continue
        except OSError:
            continue
        yield path


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def add_limited(target: list[dict[str, object]], item: dict[str, object]) -> None:
    if len(target) < MAX_FINDINGS_PER_KIND:
        target.append(item)


def stack_hints(root: Path, paths: list[Path]) -> list[str]:
    names = {path.name.lower() for path in paths}
    hints: list[str] = []
    if "package.json" in names:
        package_text = read_text(root / "package.json").lower()
        if "react" in package_text:
            hints.append("React")
        if "vite" in package_text:
            hints.append("Vite")
        if "next" in package_text:
            hints.append("Next.js")
        if "remix" in package_text:
            hints.append("Remix")
        if "vue" in package_text:
            hints.append("Vue")
    if any(path.suffix.lower() == ".svelte" for path in paths):
        hints.append("Svelte")
    if any(path.suffix.lower() == ".cs" for path in paths):
        hints.append(".NET/C#")
    if any(path.name.lower() in {"dockerfile", "compose.yml", "docker-compose.yml"} for path in root.rglob("*")):
        hints.append("Docker")
    return sorted(set(hints))


def audit(root: Path) -> dict[str, object]:
    paths = sorted(iter_files(root))
    route_hints: list[dict[str, object]] = []
    api_hints: list[dict[str, object]] = []
    mock_findings: list[dict[str, object]] = []
    secret_findings: list[dict[str, object]] = []
    component_names: collections.defaultdict[str, list[str]] = collections.defaultdict(list)

    for path in paths:
        relative = path.relative_to(root).as_posix()
        text = read_text(path)
        if path.suffix.lower() in UI_EXTENSIONS and "component" in relative.lower():
            component_names[path.stem.lower()].append(relative)

        for line_number, line in enumerate(text.splitlines(), start=1):
            for pattern in ROUTE_PATTERNS:
                match = pattern.search(line)
                if match:
                    add_limited(route_hints, {"file": relative, "line": line_number, "hint": match.group(1)})
                    break
            if any(pattern.search(line) for pattern in API_PATTERNS):
                add_limited(api_hints, {"file": relative, "line": line_number, "hint": line.strip()[:180]})
            if any(pattern.search(line) for pattern in MOCK_PATTERNS):
                add_limited(mock_findings, {"file": relative, "line": line_number, "hint": line.strip()[:180]})
            if any(pattern.search(line) for pattern in SECRET_PATTERNS):
                add_limited(secret_findings, {"file": relative, "line": line_number, "hint": "potential secret-like value"})

    duplicate_components = {
        name: locations for name, locations in sorted(component_names.items()) if len(locations) > 1
    }
    route_dirs = {"routes", "pages", "app"}
    convention_routes = [
        path.relative_to(root).as_posix()
        for path in paths
        if any(part.lower() in route_dirs for part in path.relative_to(root).parts)
        and path.suffix.lower() in UI_EXTENSIONS
    ]

    findings = {
        "potential_mock_or_browser_storage": mock_findings,
        "potential_secrets": secret_findings,
        "duplicate_component_basenames": duplicate_components,
    }
    return {
        "root": str(root),
        "files_scanned": len(paths),
        "stack_hints": stack_hints(root, paths),
        "route_hints": route_hints,
        "convention_route_files": convention_routes[:MAX_FINDINGS_PER_KIND],
        "api_hints": api_hints,
        "findings": findings,
        "limits": {
            "max_file_bytes": MAX_FILE_BYTES,
            "max_findings_per_kind": MAX_FINDINGS_PER_KIND,
            "note": "Heuristic pointers only; run project-specific tests before making claims.",
        },
    }


def print_summary(report: dict[str, object]) -> None:
    findings = report["findings"]
    duplicate_count = len(findings["duplicate_component_basenames"])
    print(f"Scanned {report['files_scanned']} text files under {report['root']}")
    print("Stack hints:", ", ".join(report["stack_hints"]) or "none detected")
    print(f"Route hints: {len(report['route_hints'])} | API hints: {len(report['api_hints'])}")
    print(
        "Potential review items: "
        f"mock/storage={len(findings['potential_mock_or_browser_storage'])}, "
        f"secret-like={len(findings['potential_secrets'])}, "
        f"duplicate component names={duplicate_count}"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Project directory to inspect")
    parser.add_argument("--out", type=Path, help="Write the JSON report to this path")
    parser.add_argument("--strict", action="store_true", help="Exit 1 when secret-like findings exist")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print(f"Audit root is not a directory: {root}", file=sys.stderr)
        return 2
    report = audit(root)
    print_summary(report)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"JSON report: {args.out.resolve()}")
    if args.strict and report["findings"]["potential_secrets"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
