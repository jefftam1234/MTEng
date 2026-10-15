#!/usr/bin/env python3
"""Split the linearized study notes into per-item / per-question Markdown plus index CSVs.

Inputs : <repo>/extracted/raw/<reagents>.md and <notes>.md (from docx2md.py)
Outputs (all regenerated; never hand-edit):
  extracted/items/{F##,S###,T###}.md      速查 entries (frameworks, numbered, legacy H27-era series)
  extracted/questions/<YEAR>-Q##.md       one per past question (OLD-### when no id)
  extracted/index_items.csv               id, title, chars, n_questions, n_years, years, missed, questions
  extracted/index_questions.csv           qid, year, title, answer, status, refs, dups, copies
  extracted/misses.csv                    rows of the 本批失點紀錄 tables
  artifacts/extraction_report.md
Source quirks handled here are documented in references/source-format.md.
"""
import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RAW = OUT = ART = None
TITLE_MARKER = "技術士（化學部門）一次試驗"

FW = str.maketrans("０１２３４５６７８９", "0123456789")
YEAR = r"(?:H\d{2}|R\d再?|R元再?)"
QID = re.compile(rf"\b({YEAR})-Q(\d{{1,2}})\b")


def last_snapshot(lines, title):
    starts = [i for i, l in enumerate(lines) if l.startswith(title)]
    return lines[starts[-1]:]


def clean(s):
    return s.replace("**", "").strip()


def year_key(y):
    y = y.replace("元", "1")
    era, rest = y[0], y[1:].replace("再", ".5")
    return (0 if era == "H" else 1, float(rest))


# ---------- 速查 ----------
def split_items(lines):
    item_re = re.compile(r"^(\d{1,3})\.\s+(.*)")
    sec_re = re.compile(r"^([０-９]{1,3})　(.*)")
    items, cur = [], None
    for l in lines:
        m, s = item_re.match(l), sec_re.match(l)
        if m and not l.startswith("- "):
            cur = {"id": f"S{int(m.group(1)):03d}", "title": clean(m.group(2)), "body": []}
            items.append(cur)
        elif s and int(s.group(1).translate(FW)) <= 24 and not any(i["id"].startswith("S") for i in items):
            cur = {"id": f"F{int(s.group(1).translate(FW)):02d}", "title": clean(s.group(2)), "body": []}
            items.append(cur)
        elif cur is not None:
            cur["body"].append(l)
    return items


def split_legacy_items(all_lines):
    """Snapshot 2 has a full-width-numbered series ６９–１０２ (H27 era) that snapshot 3 renumbered/dropped."""
    starts = [i for i, l in enumerate(all_lines) if l.startswith(TITLE_MARKER)]
    seg = [l for l in all_lines[starts[1]:starts[2]] if l.strip()]
    sec_re = re.compile(r"^([０-９]{2,3})　(.*)")
    items, cur = [], None
    for l in seg:
        s = sec_re.match(l)
        if s and int(s.group(1).translate(FW)) >= 69:
            cur = {"id": f"T{int(s.group(1).translate(FW)):03d}", "title": clean(s.group(2)), "body": []}
            items.append(cur)
        elif s or re.match(r"^\d{1,3}\.\s", l):
            cur = None
        elif cur is not None:
            cur["body"].append(l)
    return items


# ---------- 解題筆記 ----------
def split_questions(lines):
    old_re = re.compile(r"^問\s*(\d+)\s*　(.*)")
    new_re = re.compile(rf"^({YEAR})-Q(\d{{1,2}})\s*$")
    qs, cur = [], None
    for l in lines:
        mo, mn = old_re.match(l), new_re.match(l)
        if mo:
            emb = QID.search(mo.group(2))
            qid = f"{emb.group(1)}-Q{int(emb.group(2)):02d}" if emb else f"OLD-{int(mo.group(1)):03d}"
            cur = {"qid": qid, "header": clean(mo.group(2)), "body": [], "era": "old"}
            qs.append(cur)
        elif mn:
            cur = {"qid": f"{mn.group(1)}-Q{int(mn.group(2)):02d}", "header": "", "body": [], "era": "new"}
            qs.append(cur)
        elif cur is not None:
            cur["body"].append(l)
    return qs


def q_meta(q):
    text = "\n".join(q["body"])
    topic = q["header"]
    m = re.search(r"^主題：(.*)$", text, re.M)
    status_src = topic
    if m:
        topic = clean(m.group(1))
        status_src = topic
    ans = re.search(r"正解[：:]\s*([^\s　]+)", status_src) or re.search(r"（答：(.*?)）\s*$", q["header"])
    if "用戶答錯" in status_src or "猜" in status_src:
        status = "wrong" if "用戶答錯" in status_src else "guessed"
    elif "用戶答對" in status_src:
        status = "right_partial" if re.search(r"理由錯|說法需修正|不確定", status_src) else "right"
    else:
        status = "unknown"
    refs = sorted({int(x) for x in re.findall(r"速查第(\d+)項", text + q["header"])})
    dup = sorted({f"{a}-Q{int(b):02d}" for a, b in re.findall(rf"(?:重複|同)\s*({YEAR})-Q(\d+)", text)})
    title = re.split(r"\s{2,}|　正解", topic)[0]
    return {"title": title, "answer": ans.group(1) if ans else "", "status": status, "refs": refs, "dups": dup}


def parse_misses(lines):
    rows, batch = [], None
    hdr = re.compile(rf"^({YEAR})（問(\d+)〜問(\d+)）\s*本批失點紀錄")
    for l in lines:
        h = hdr.match(l)
        if h:
            batch = h.group(1)
            continue
        if batch and l.startswith("| Q"):
            cells = [c.strip() for c in l.strip("|").split("|")]
            qn = re.match(r"Q(\d+)", cells[0])
            if qn:
                rows.append({"qid": f"{batch}-Q{int(qn.group(1)):02d}", "type": cells[1] if len(cells) > 1 else "",
                             "fix": cells[2] if len(cells) > 2 else ""})
        elif batch and l and not l.startswith("|"):
            batch = None if not l.startswith("出處") else batch
    uniq = {(r["qid"], r["type"]): r for r in rows}
    return list(uniq.values())


def write_md(path, header, body):
    blocks = []
    sep = re.compile(r"^\|[\s:|-]+\|$")
    for k, line in enumerate(body):
        new_table = k + 1 < len(body) and sep.match(body[k + 1]) and not sep.match(line)
        if line.startswith("|") and blocks and blocks[-1].startswith("|") and not new_table:
            blocks[-1] += "\n" + line
        else:
            blocks.append(line)
    path.write_text(header + "\n\n" + "\n\n".join(blocks).strip() + "\n", encoding="utf-8")


def main():
    global RAW, OUT, ART
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--repo", type=Path, default=ROOT, help="repository root (default: derived from script location)")
    p.add_argument("--reagents", default="技術士_有機_試劑速查.md", help="linearized 試劑速查 file in extracted/raw")
    p.add_argument("--notes", default="技術士_有機_解題筆記.md", help="linearized 解題筆記 file in extracted/raw")
    a = p.parse_args()
    RAW, OUT, ART = a.repo / "extracted" / "raw", a.repo / "extracted", a.repo / "artifacts"
    for f in (a.reagents, a.notes):
        if not (RAW / f).is_file():
            sys.exit(f"error: missing {RAW / f}; run docx2md.py first")
    for d in ("items", "questions"):
        (OUT / d).mkdir(parents=True, exist_ok=True)
        for f in (OUT / d).glob("*.md"):
            f.unlink()

    sq_all = (RAW / a.reagents).read_text(encoding="utf-8").splitlines()
    sq = [l for l in last_snapshot(sq_all, TITLE_MARKER) if l.strip()]
    items = split_items(sq)
    items += split_legacy_items(sq_all)

    kj = (RAW / a.notes).read_text(encoding="utf-8").splitlines()
    kj = [l for l in kj if l.strip()]
    qs = split_questions(kj)
    misses = parse_misses(kj)
    miss_ids = {m["qid"] for m in misses}

    # questions: merge duplicates of the same qid (old + new era) into one record
    by_q = defaultdict(list)
    for q in qs:
        by_q[q["qid"]].append(q)
    qrows = []
    item_cited_by = defaultdict(set)
    for qid, group in by_q.items():
        metas = [q_meta(q) for q in group]
        meta = next((m for m in reversed(metas) if m["status"] != "unknown"), metas[-1])
        refs = sorted({r for m in metas for r in m["refs"]})
        status = meta["status"]
        if qid in miss_ids and status in ("unknown", "right"):
            status = "missed_log" if status == "unknown" else "right_partial"
        for r in refs:
            legacy = qid.startswith("H27-") and 69 <= r <= 102
            item_cited_by[f"{'T' if legacy else 'S'}{r:03d}"].add(qid)
        q = group[-1]
        body = [f"<!-- era: {q['era']}; copies in source: {len(group)} -->"] + ([q["header"]] if q["header"] else []) + q["body"]
        write_md(OUT / "questions" / f"{qid}.md", f"# {qid}　{meta['title']}", body)
        y = re.match(YEAR, qid)
        qrows.append({"qid": qid, "year": y.group(0) if y else "", "title": meta["title"], "answer": meta["answer"],
                      "status": status,
                      "refs": " ".join(f"{'T' if qid.startswith('H27-') and 69 <= r <= 102 else 'S'}{r:03d}" for r in refs),
                      "dups": " ".join(sorted({d for m in metas for d in m["dups"]})), "copies": len(group)})

    # items: source questions cited inside the item (出處 / 例（R7-Q35）)
    irows = []
    seen = defaultdict(int)
    for it in items:
        seen[it["id"]] += 1
        iid = it["id"] if seen[it["id"]] == 1 else f"{it['id']}_{seen[it['id']]}"
        text = "\n".join(it["body"])
        src = {f"{a}-Q{int(b):02d}" for a, b in QID.findall(text + it["title"])}
        cited = item_cited_by.get(it["id"], set())
        allq = src | cited
        years = sorted({re.match(YEAR, q).group(0) for q in allq}, key=year_key)
        missed = sorted(q for q in allq if q in miss_ids or any(r["qid"] == q and r["status"] in ("wrong", "guessed", "missed_log") for r in qrows))
        write_md(OUT / "items" / f"{iid}.md", f"# {iid}　{it['title']}", it["body"])
        irows.append({"id": iid, "title": it["title"], "chars": len(text), "n_questions": len(allq),
                      "n_years": len(years), "years": " ".join(years), "missed": " ".join(missed),
                      "questions": " ".join(sorted(allq))})

    def dump(name, rows):
        with open(OUT / name, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)

    dump("index_items.csv", irows)
    dump("index_questions.csv", sorted(qrows, key=lambda r: (year_key(r["year"]) if r["year"] else (9, 0), r["qid"])))
    dump("misses.csv", misses)

    # report
    ids = [int(r["id"][1:4]) for r in irows if r["id"].startswith("S") and "_" not in r["id"]]
    missing = sorted(set(range(1, max(ids) + 1)) - set(ids))
    dupes = [r["id"] for r in irows if "_" in r["id"]]
    st = defaultdict(int)
    for r in qrows:
        st[r["status"]] += 1
    yrs = defaultdict(int)
    for r in qrows:
        yrs[r["year"] or "?"] += 1
    ART.mkdir(exist_ok=True)
    rep = [
        "# Extraction report", "",
        f"- 速查 items: {len(irows)} ({sum(1 for r in irows if r['id'].startswith('F'))} framework sections, "
        f"{len(ids)} numbered; max #{max(ids)})",
        f"- Numbered ids missing: {missing or 'none'}",
        f"- Duplicate item ids: {dupes or 'none'}",
        f"- Question records: {len(qrows)} (from {len(qs)} raw entries)",
        f"- Status: " + ", ".join(f"{k}={v}" for k, v in sorted(st.items())),
        f"- Miss-log rows: {len(misses)}",
        f"- Questions per exam year: " + ", ".join(f"{k}={v}" for k, v in sorted(yrs.items(), key=lambda kv: year_key(kv[0]) if kv[0] != '?' else (9, 0))),
        f"- Items cited by ≥1 question: {sum(1 for r in irows if r['n_questions'])}; by ≥2 years: {sum(1 for r in irows if r['n_years'] >= 2)}",
        f"- Total item text chars: {sum(r['chars'] for r in irows)}",
    ]
    (ART / "extraction_report.md").write_text("\n".join(rep) + "\n", encoding="utf-8")
    print("\n".join(rep))


if __name__ == "__main__":
    main()
