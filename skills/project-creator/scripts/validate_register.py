#!/usr/bin/env python3
"""Check register structure and task dependencies; never certify remote state."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlsplit

RESOURCE_STATES = {"planned", "attempting", "uncertain", "verified", "failed", "blocked"}
TASK_STATES = {"pending", "ready", "dispatched", "running", "blocked", "review", "verified"}
TRANSPORT_STATES = {"draft", "send_uncertain", "accepted", "generating", "settled", "failed"}


def validate(data):
    errors = []
    if not isinstance(data, dict):
        return ["register must be an object"]
    if data.get("schema_version") != 1:
        errors.append("schema_version must equal 1")
    for key, host, required in (
        ("chatgpt_project", "chatgpt.com", ("name", "observed_id", "observed_url", "evidence")),
        ("github_repository", "github.com", ("owner", "name", "observed_url", "visibility", "evidence")),
        ("repository_initialization", None, ("observed_commit", "evidence")),
    ):
        item = data.get(key)
        if not isinstance(item, dict):
            errors.append(f"{key} must be an object")
            continue
        if item.get("status") not in RESOURCE_STATES:
            errors.append(f"{key}.status is invalid")
        if item.get("status") == "verified":
            for field in required:
                if not item.get(field):
                    errors.append(f"{key}.{field} is required when verified")
        url = item.get("observed_url")
        if host and url:
            try:
                parts = urlsplit(url)
                valid = parts.scheme == "https" and parts.hostname == host and not parts.username and not parts.password
            except (TypeError, ValueError):
                valid = False
            if not valid:
                errors.append(f"{key}.observed_url must be a safe HTTPS {host} URL")
    repo = data.get("github_repository", {})
    if isinstance(repo, dict) and repo.get("visibility") not in {"private", "public", "internal"}:
        errors.append("github_repository.visibility is invalid")
    init = data.get("repository_initialization", {})
    if isinstance(init, dict) and init.get("status") == "verified" and (not isinstance(repo, dict) or repo.get("status") != "verified"):
        errors.append("verified initialization requires verified repository identity")
    tasks = data.get("tasks")
    if not isinstance(tasks, list):
        errors.append("tasks must be an array")
        tasks = []
    by_id = {}
    for i, task in enumerate(tasks):
        if not isinstance(task, dict):
            errors.append(f"tasks[{i}] must be an object")
            continue
        task_id = task.get("id")
        if not isinstance(task_id, str) or not task_id.strip():
            errors.append(f"tasks[{i}].id must be nonempty")
            continue
        if task_id in by_id:
            errors.append(f"duplicate task ID: {task_id}")
        by_id[task_id] = task
        if task.get("status") not in TASK_STATES:
            errors.append(f"{task_id}.status is invalid")
        if task.get("transport_status") is not None and task.get("transport_status") not in TRANSPORT_STATES:
            errors.append(f"{task_id}.transport_status is invalid")
        deps = task.get("dependencies", [])
        if not isinstance(deps, list) or any(not isinstance(d, str) for d in deps):
            errors.append(f"{task_id}.dependencies must be string IDs")
        if task.get("status") == "verified" and not task.get("evidence"):
            errors.append(f"{task_id}.evidence is required when verified")
        if task.get("conversation_verified") and not (task.get("observed_conversation_url") and task.get("membership_evidence")):
            errors.append(f"{task_id} requires conversation URL and membership evidence")
    graph = {}
    for task_id, task in by_id.items():
        deps = task.get("dependencies", [])
        graph[task_id] = deps if isinstance(deps, list) and all(isinstance(d, str) for d in deps) else []
        for dep in graph[task_id]:
            if dep not in by_id:
                errors.append(f"{task_id} depends on unknown task: {dep}")
    visited, active = set(), set()
    def visit(task_id):
        if task_id in active:
            errors.append(f"dependency cycle at {task_id}")
            return
        if task_id in visited:
            return
        active.add(task_id)
        for dep in graph[task_id]:
            if dep in graph:
                visit(dep)
        active.remove(task_id)
        visited.add(task_id)
    for task_id in graph:
        visit(task_id)
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("register", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.register.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    errors = validate(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print("Register structure valid; external outcomes still require live verification.")


if __name__ == "__main__":
    main()
