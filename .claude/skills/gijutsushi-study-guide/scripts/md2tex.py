#!/usr/bin/env python3
"""Convert one chapter Markdown file (restricted dialect) into a LaTeX fragment.

The dialect is specified in references/authoring-syntax.md. Output macros
(\\chapterbanner, \\secthead, \\ja, boxes, ...) are defined in assets/latex/preamble.tex.
Usable stand-alone (`md2tex.py in.md out.tex`) or imported by build.py.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

KANA = "\u3040-\u309f\u30a0-\u30ff\u31f0-\u31ff\uff66-\uff9f"
HAN = "\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\u3005\u30fc\u30fb"
JA_RUN = re.compile(rf"[{HAN}{KANA}]*[{KANA}][{HAN}{KANA}]*")
SUPMAP = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9",
          "⁺": "+", "⁻": "-", "ⁿ": "n"}
SUBMAP = {"ₙ": "n", "ₘ": "m", "ₓ": "x"}
ESC = {"\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "$": r"\$", "&": r"\&", "#": r"\#",
       "%": r"\%", "_": r"\_", "^": r"\textasciicircum{}", "~": r"\textasciitilde{}"}
BOXES = {"trap": "trapbox", "key": "keybox", "memo": "memobox", "exam": "exambox"}
INLINE = re.compile(r"(\$[^$\n]+\$)|(\\ce\{)|(`[^`\n]+`)|(\*\*.+?\*\*)|(==.+?==)|(\{\{ja:.+?\}\})")


def tag_label(tag: str) -> str:
    m = re.fullmatch(r"([FST])(\d+)", tag)
    if not m:
        return tag
    kind, n = m.group(1), int(m.group(2))
    return {"S": f"\\#{n}", "T": f"\\#{n}H27", "F": f"框{n}"}[kind]


def scripts(text: str) -> str:
    """Map Unicode sub/superscript runs to LaTeX (applied to already-escaped text)."""
    def sup(m):
        return r"\textsuperscript{" + "".join(SUPMAP[c] for c in m.group(0)) + "}"

    def sub(m):
        return r"\textsubscript{" + "".join(str("₀₁₂₃₄₅₆₇₈₉".index(c)) if c in "₀₁₂₃₄₅₆₇₈₉" else SUBMAP[c]
                                             for c in m.group(0)) + "}"
    text = re.sub("[" + "".join(SUPMAP) + "]+", sup, text)
    return re.sub("[₀₁₂₃₄₅₆₇₈₉" + "".join(SUBMAP) + "]+", sub, text)


def plain(text: str, ja: str) -> str:
    out, pos = [], 0
    for m in JA_RUN.finditer(text):
        out.append(escape(text[pos:m.start()]))
        out.append(f"\\{ja}{{{escape(m.group(0))}}}")
        pos = m.end()
    out.append(escape(text[pos:]))
    return "".join(out)


def escape(s: str) -> str:
    s = "".join(ESC.get(c, c) for c in s)
    s = s.replace("◯", r"\maru{}").replace("✗", r"\batsu{}").replace("✕", r"\batsu{}")
    s = s.replace("✓", r"\ensuremath{\checkmark}").replace("✔", r"\ensuremath{\checkmark}")
    return scripts(s)


def balanced(text: str, start: int) -> int:
    """Index just after the brace group opening at text[start] == '{'."""
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return i + 1
    raise ValueError(f"unbalanced braces: {text[start:start + 40]!r}")


def inline(text: str, ja: str = "ja") -> str:
    out, pos = [], 0
    while (m := INLINE.search(text, pos)):
        out.append(plain(text[pos:m.start()], ja))
        tok = m.group(0)
        if m.group(1):
            out.append(tok)
            pos = m.end()
        elif m.group(2):
            end = balanced(text, m.end() - 1)
            out.append(text[m.start():end])
            pos = end
        elif m.group(3):
            out.append(r"\texttt{" + escape(tok[1:-1]) + "}")
            pos = m.end()
        elif m.group(4):
            out.append(r"\textbf{" + inline(tok[2:-2], ja) + "}")
            pos = m.end()
        elif m.group(5):
            out.append(r"\hl{" + inline(tok[2:-2], ja) + "}")
            pos = m.end()
        else:
            out.append(f"\\{ja}{{" + escape(tok[5:-2]) + "}")
            pos = m.end()
    out.append(plain(text[pos:], ja))
    return "".join(out)


def split_heading(text: str) -> tuple[str, str]:
    m = re.match(r"^(.*?)\s*\{([FST]\d+(?:\s+[FST]\d+)*)\}\s*$", text)
    if not m:
        return text, ""
    return m.group(1), r"\,".join(tag_label(t) for t in m.group(2).split())


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def table(rows: list[str], spec: str | None) -> str:
    head = cells(rows[0])
    body = [cells(r) for r in rows[1:] if not re.fullmatch(r"\|?[\s:\-|]+\|?", r.strip())]
    n = len(head)
    body = [(r + [""] * n)[:n] for r in body]
    if spec and len(spec.split()) != n:
        print(f"warning: cols spec {spec!r} has {len(spec.split())} columns, table has {n}; ignored", file=sys.stderr)
        spec = None
    if spec:
        cols = spec.split()
    else:
        cols = []
        for j in range(n):
            longest = max(len(r[j]) for r in [head] + body)
            cols.append("c" if longest <= 4 else ("l" if longest <= 8 else "X"))
        if "X" not in cols:
            cols[max(range(n), key=lambda j: max(len(r[j]) for r in [head] + body))] = "X"
    def col(c: str) -> str:
        if c.startswith("X:"):
            return f">{{\\hsize={c[2:]}\\hsize}}Y"
        return {"X": "Y", "l": "l", "c": "c", "r": "r"}.get(c, "Y")
    colspec = "".join(col(c) for c in cols)
    lines = [r"\begin{gtable}{" + colspec + "}",
             r"\rowcolor{thead}" + " & ".join(r"\textbf{" + inline(h, "jas") + "}" for h in head) + r" \\"]
    lines += ["{}" + " & ".join(inline(c) for c in r) + r" \\" for r in body]
    lines.append(r"\end{gtable}")
    return "\n".join(lines)


def convert(md: str, chapter: str) -> tuple[str, dict]:
    meta: dict = {}
    out: list[str] = []
    lines = md.splitlines()
    i, para, lst, spec = 0, [], [], None

    def flush_para():
        if para:
            out.append(inline(" ".join(para)) + "\n")
            para.clear()

    def flush_list():
        if not lst:
            return
        depth0 = None
        stack = []
        for indent, kind, text in lst:
            lvl = 1 if indent >= 2 else 0
            if depth0 is None:
                depth0 = 0
            while len(stack) > lvl + 1:
                out.append(r"\end{" + stack.pop() + "}")
            if len(stack) < lvl + 1:
                env = "enumerate" if kind == "num" else "itemize"
                out.append(r"\begin{" + env + "}")
                stack.append(env)
            out.append(r"\item{} " + inline(text))
        while stack:
            out.append(r"\end{" + stack.pop() + "}")
        lst.clear()

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if s.startswith("<!--"):
            body = s[4:-3].strip() if s.endswith("-->") else s[4:].strip()
            if m := re.match(r"budget:\s*([\d.]+)", body):
                meta["budget"] = float(m.group(1))
            elif m := re.match(r"label:\s*(.+)", body):
                chapter = m.group(1).strip()
            elif m := re.match(r"cols:\s*(.+)", body):
                spec = m.group(1)
            while not lines[i].rstrip().endswith("-->"):
                i += 1
            i += 1
            continue
        if s.startswith("```"):
            flush_para(); flush_list()
            lang = s[3:].strip()
            j = i + 1
            while j < len(lines) and not lines[j].strip().startswith("```"):
                j += 1
            code = "\n".join(lines[i + 1:j])
            if lang in ("chem", "tikz"):
                out.append(r"\begin{figblock}" + "\n" + code + "\n" + r"\end{figblock}")
            else:
                out.append(code)
            i = j + 1
            continue
        if not s:
            flush_para(); flush_list()
            i += 1
            continue
        if m := re.match(r"^(#{1,4})\s+(.*)$", s):
            flush_para(); flush_list()
            level, text = len(m.group(1)), m.group(2)
            if level == 1:
                title, _, sub = text.partition("|")
                meta["title"] = title.strip()
                out.append(f"\\chapterbanner{{{chapter}}}{{{inline(title.strip(), 'jas')}}}{{{inline(sub.strip(), 'jas')}}}")
            else:
                head, tags = split_heading(text)
                macro = {2: "secthead", 3: "subsecthead", 4: "minihead"}[level]
                out.append(f"\\{macro}{{{inline(head, 'jas')}}}{{{tags}}}")
            i += 1
            continue
        if s.startswith(">"):
            flush_para(); flush_list()
            block = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                block.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            first = block[0].strip()
            kind, title = "key", ""
            if m := re.match(r"\[!(\w+)\]\s*(.*)", first):
                kind, title, block = m.group(1), m.group(2), block[1:]
            env = BOXES.get(kind, "keybox")
            inner, _ = convert("\n".join(block), chapter)
            out.append(f"\\begin{{{env}}}{{{inline(title, 'jas')}}}\n{inner}\\end{{{env}}}")
            continue
        if s.startswith("|"):
            flush_para(); flush_list()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i])
                i += 1
            out.append(table(rows, spec))
            spec = None
            continue
        if m := re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", line):
            flush_para()
            lst.append((len(m.group(1)), "num" if m.group(2)[0].isdigit() else "bullet", m.group(3)))
            i += 1
            continue
        if s == "---":
            flush_para(); flush_list()
            out.append(r"\sepline")
            i += 1
            continue
        if lst and line.startswith("  "):
            indent, kind, text = lst[-1]
            lst[-1] = (indent, kind, text + " " + s)
            i += 1
            continue
        flush_list()
        para.append(s)
        i += 1
    flush_para(); flush_list()
    return "\n".join(out) + "\n", meta


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("src", type=Path, help="chapter Markdown file")
    p.add_argument("dst", type=Path, help="output .tex fragment")
    p.add_argument("--chapter", help="chapter number shown in the banner (default: filename prefix)")
    a = p.parse_args()
    key = a.src.name.split("_")[0]
    chap = a.chapter or (f"第{int(key)}章" if key.isdigit() else key)
    tex, meta = convert(a.src.read_text(encoding="utf-8"), chap)
    a.dst.parent.mkdir(parents=True, exist_ok=True)
    a.dst.write_text(tex, encoding="utf-8")
    print(f"{a.src.name} -> {a.dst} {meta}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
