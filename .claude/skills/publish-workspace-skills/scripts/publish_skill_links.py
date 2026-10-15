#!/usr/bin/env python3
"""Check or publish workspace skills for every supported local agent.

The canonical source is <workspace>/.codex/skills.  Local agent paths are not
tracked as links because Git can materialize symlinks as text files on Windows.
Run with --fix after cloning to create Windows directory junctions (or POSIX
directory symlinks).  A normal run is diagnostic only.
"""

from __future__ import annotations

import argparse
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path


AGENT_LINKS = (Path(".agents/skills"), Path(".claude/skills"), Path(".grok/skills"))


class Report:
    def __init__(self) -> None:
        self.failed = False

    def line(self, status: str, label: str, detail: str = "") -> None:
        if status == "FAIL":
            self.failed = True
        print(f"{status:<4}  {label}" + (f"  {detail}" if detail else ""))


def repository_root() -> Path:
    # <repo>/.codex/skills/publish-workspace-skills/scripts/<this file>
    return Path(__file__).resolve().parents[4]


def file_identity(path: Path) -> tuple[int, int] | None:
    try:
        stat = os.stat(path)
    except OSError:
        return None
    return stat.st_dev, stat.st_ino


def same_directory(left: Path, right: Path) -> bool:
    left_id, right_id = file_identity(left), file_identity(right)
    return left_id is not None and left_id == right_id


def content_drift(link: Path, target: Path) -> list[str]:
    expected = sorted(target.glob("*/SKILL.md"))
    found = sorted(link.glob("*/SKILL.md"))
    if len(found) != len(expected):
        return [f"skill count is {len(found)}, expected {len(expected)}"]
    return [
        path.relative_to(target).as_posix()
        for path in expected
        if not (link / path.relative_to(target)).is_file()
        or (link / path.relative_to(target)).read_bytes() != path.read_bytes()
    ]


def check(report: Report, workspace: Path) -> None:
    target = workspace / ".codex" / "skills"
    if not target.is_dir():
        report.line("FAIL", "canonical skills", f"missing: {target}")
        return

    for relative in AGENT_LINKS:
        link = workspace / relative
        name = relative.as_posix()
        if not (link.exists() or link.is_symlink()):
            report.line("WARN", name, "absent; run with --fix")
            continue
        if link.is_file():
            report.line("FAIL", name, "is a file, not a skills-directory link")
            continue
        if not same_directory(link, target):
            drift = content_drift(link, target)
            detail = "separate directory" + (f"; drift: {', '.join(drift)}" if drift else "")
            report.line("FAIL", name, detail)
            continue
        report.line("OK", name, f"junction/symlink to {target}")


def publish(report: Report, workspace: Path, replace: bool) -> None:
    target = workspace / ".codex" / "skills"
    if not target.is_dir():
        report.line("FAIL", "canonical skills", f"missing: {target}")
        return

    for relative in AGENT_LINKS:
        link = workspace / relative
        name = relative.as_posix()
        if link.exists() or link.is_symlink():
            if same_directory(link, target):
                report.line("OK", name, "already correct")
                continue
            if not replace:
                report.line("FAIL", name, "exists but is not the canonical skills directory; use --replace after review")
                continue
            if link.is_file() or link.is_symlink():
                link.unlink()
            else:
                shutil.rmtree(link)
        link.parent.mkdir(parents=True, exist_ok=True)
        if platform.system() == "Windows":
            subprocess.run(["cmd", "/c", "mklink", "/J", str(link), str(target)], check=True, text=True, capture_output=True)
        else:
            os.symlink(target, link, target_is_directory=True)
        report.line("OK", name, f"created -> {target}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fix", action="store_true", help="create missing local skill-directory links")
    parser.add_argument("--replace", action="store_true", help="with --fix, replace a noncanonical existing path")
    args = parser.parse_args()
    if args.replace and not args.fix:
        parser.error("--replace requires --fix")

    report = Report()
    workspace = repository_root()
    if args.fix:
        publish(report, workspace, args.replace)
    else:
        check(report, workspace)
    return 1 if report.failed else 0


if __name__ == "__main__":
    sys.exit(main())
