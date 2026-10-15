#!/usr/bin/env python3
"""Linearize .docx files into Markdown, keeping paragraphs and tables in document order.

Standard library only (no pandoc needed). Paragraph styles other than body text are kept
as an HTML comment prefix (<!--Style--> text); bullet styles become "- "; tables become
Markdown tables (cell line breaks joined with " / ", pipes escaped as ｜); embedded images
are marked [IMAGE]. One <stem>.md per input file is (re)written into the output directory.
"""
from __future__ import annotations

import argparse
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
PLAIN_STYLES = {"", "BodyText", "Compact", "FirstParagraph"}


def run_text(r) -> str:
    out = []
    for c in r:
        if c.tag == W + "t":
            out.append(c.text or "")
        elif c.tag == W + "tab":
            out.append("\t")
        elif c.tag in (W + "br", W + "cr"):
            out.append(" / ")
    return "".join(out)


def para(p) -> tuple[str, str]:
    style = ""
    ppr = p.find(W + "pPr")
    if ppr is not None and (s := ppr.find(W + "pStyle")) is not None:
        style = s.get(W + "val", "")
    parts, has_img = [], False
    for el in p.iter():
        if el.tag == W + "r":
            parts.append(run_text(el))
        elif el.tag == W + "drawing" or el.tag.endswith("}pict"):
            has_img = True
    text = "".join(parts).strip()
    return style, text + (" [IMAGE]" if has_img else "")


def cell_text(tc) -> str:
    return " / ".join(t for _, t in (para(p) for p in tc.iter(W + "p")) if t).replace("|", "｜")


def table(tbl) -> str:
    rows = [[cell_text(tc) for tc in tr.findall(W + "tc")] for tr in tbl.findall(W + "tr")]
    if not rows:
        return ""
    n = max(len(r) for r in rows)
    rows = [r + [""] * (n - len(r)) for r in rows]
    lines = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * n]
    return "\n".join(lines + ["| " + " | ".join(r) + " |" for r in rows[1:]])


def convert(path: Path) -> str:
    with zipfile.ZipFile(path) as z:
        body = ET.fromstring(z.read("word/document.xml")).find(W + "body")
    out = []
    for el in body:
        if el.tag == W + "p":
            style, text = para(el)
            if not text:
                continue
            if style.startswith("ListBullet") or style == "ListParagraph":
                out.append(f"- {text}")
            else:
                out.append(text if style in PLAIN_STYLES else f"<!--{style}--> {text}")
        elif el.tag == W + "tbl":
            out.append(table(el))
    return "\n\n".join(out) + "\n"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("src", type=Path, help="a .docx file or a directory of .docx files")
    p.add_argument("dst", type=Path, help="output directory for .md files")
    a = p.parse_args()
    files = [a.src] if a.src.is_file() else sorted(a.src.glob("*.docx"))
    if not files:
        print(f"error: no .docx found at {a.src}", file=sys.stderr)
        return 1
    a.dst.mkdir(parents=True, exist_ok=True)
    for f in files:
        md = convert(f)
        (a.dst / (f.stem + ".md")).write_text(md, encoding="utf-8")
        print(f"{f.name}: {len(md)} chars")
    return 0


if __name__ == "__main__":
    sys.exit(main())
