#!/usr/bin/env python3
"""Build the study-guide PDF: content/NN_*.md -> latex/build/*.tex -> XeLaTeX -> artifacts/study_guide.pdf.

Steps:
  1. If latex/main.tex or latex/preamble.tex is missing, copy it from the skill's assets/latex/
     (existing files are never overwritten; they are hand-edited).
  2. Convert every content/[0-9][0-9]_*.md (or those matching --chapters) with md2tex.py into
     latex/build/chNN.tex and write latex/build/chapters.tex.
  3. Run xelatex twice (table of contents) with output in latex/build/.
  4. Check the log: errors, missing glyphs ("Missing character"), overfull boxes; report pages per
     chapter against each file's <!-- budget: N --> comment.
  5. Copy the PDF to artifacts/study_guide.pdf; with --png, render pages to artifacts/preview/.
Exit code 1 on LaTeX errors or missing glyphs.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import md2tex  # noqa: E402

SKILL = Path(__file__).resolve().parent.parent
ROOT = Path(__file__).resolve().parents[4]


def run_xelatex(latex: Path) -> subprocess.CompletedProcess:
    return subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", "-output-directory=build",
                           "main.tex"], cwd=latex, capture_output=True, text=True, encoding="utf-8", errors="replace")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--repo", type=Path, default=ROOT, help="repository root (default: derived from script location)")
    p.add_argument("--chapters", default="", help="comma list of chapter prefixes to include, e.g. 01,02 (default all)")
    p.add_argument("--png", default="", help="page range to render as PNG previews, e.g. 1-6 or 'all'")
    p.add_argument("--dpi", type=int, default=110, help="preview resolution")
    a = p.parse_args()

    latex, content = a.repo / "latex", a.repo / "content"
    build = latex / "build"
    build.mkdir(parents=True, exist_ok=True)
    for name in ("main.tex", "preamble.tex"):
        if not (latex / name).exists():
            shutil.copyfile(SKILL / "assets" / "latex" / name, latex / name)
            print(f"template: copied {name}")

    wanted = [c.strip() for c in a.chapters.split(",") if c.strip()]
    sources = sorted(f for f in content.glob("[0-9][0-9]*_*.md")
                     if not wanted or f.name.split("_")[0] in wanted)
    if not sources:
        print("error: no content/NN_*.md chapters found", file=sys.stderr)
        return 1
    for old in build.glob("ch*.tex"):
        old.unlink()
    budgets, includes = {}, []
    for src in sources:
        nn = src.name.split("_")[0]
        label = f"第{int(nn)}章" if nn.isdigit() else nn
        tex, meta = md2tex.convert(src.read_text(encoding="utf-8"), label)
        first, _, rest = tex.partition("\n")
        if first.startswith("\\chapterbanner"):
            tex = f"{first}\n\\label{{ch{nn}-start}}\n{rest}\\label{{ch{nn}-end}}\n"
        else:
            tex = f"\\clearpage\\label{{ch{nn}-start}}\n{tex}\\label{{ch{nn}-end}}\n"
        (build / f"ch{nn}.tex").write_text(tex, encoding="utf-8")
        includes.append(f"\\input{{build/ch{nn}.tex}}")
        budgets[nn] = (meta.get("title", src.stem), meta.get("budget"))
    (build / "chapters.tex").write_text("\n".join(includes) + "\n", encoding="utf-8")

    for _ in range(2):
        r = run_xelatex(latex)
        if r.returncode != 0:
            break
    log = (build / "main.log").read_text(encoding="utf-8", errors="replace") if (build / "main.log").exists() else ""
    errors = re.findall(r"^! .*(?:\n.*){0,3}", log, re.M)
    missing = sorted(set(re.findall(r"Missing character: There is no (\S+) in font ([^/\n]+)", log)))
    overfull = re.findall(r"Overfull \\hbox \((\d+\.?\d*)pt too wide\)", log)
    big_over = [float(x) for x in overfull if float(x) > 3]
    pages = re.search(r"Output written on .*?\((\d+)\s+pag", log, re.S)

    print(f"xelatex: {'OK' if r.returncode == 0 else 'FAILED'}; pages: {pages.group(1) if pages else '?'}")
    for e in errors[:5]:
        print("ERROR", e.strip().replace("\n", " | ")[:300])
    for ch, font in missing[:40]:
        print(f"MISSING glyph {ch!r} ({hex(ord(ch[0])) if ch else ''}) in {font}")
    print(f"overfull boxes: {len(overfull)} (>3pt: {len(big_over)}, max {max(big_over, default=0):.1f}pt)")

    aux = (build / "main.aux").read_text(encoding="utf-8", errors="replace") if (build / "main.aux").exists() else ""
    labels = {m.group(1): int(m.group(2)) for m in re.finditer(r"\\newlabel\{(ch\w+-(?:start|end))\}\{\{[^}]*\}\{(\d+)\}", aux)}
    for nn, (title, budget) in budgets.items():
        s, e = labels.get(f"ch{nn}-start"), labels.get(f"ch{nn}-end")
        if s and e:
            used = e - s + 1
            flag = "" if budget is None else (" OVER" if used > budget + 0.5 else "")
            print(f"chapter {nn} {title}: pages {s}-{e} = {used}" + (f" (budget {budget:g}){flag}" if budget else ""))

    pdf = build / "main.pdf"
    if r.returncode == 0 and pdf.exists():
        dst = a.repo / "artifacts" / "study_guide.pdf"
        dst.parent.mkdir(exist_ok=True)
        try:
            shutil.copyfile(pdf, dst)
            print(f"pdf: {dst}")
        except PermissionError:
            print(f"pdf: {pdf} (artifacts copy locked by a viewer)")
        if a.png:
            prev = a.repo / "artifacts" / "preview"
            prev.mkdir(exist_ok=True)
            for old in prev.glob("*.png"):
                old.unlink()
            rng = [] if a.png == "all" else ["-f", a.png.split("-")[0], "-l", a.png.split("-")[-1]]
            subprocess.run(["pdftoppm", "-png", "-r", str(a.dpi), *rng, str(pdf), str(prev / "p")], check=False)
            print(f"previews: {prev}")
    return 0 if r.returncode == 0 and not missing else 1


if __name__ == "__main__":
    sys.exit(main())
