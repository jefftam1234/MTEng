---
name: gijutsushi-study-guide
description: Build and grow the 技術士（化学部門）一次試験 専門科目 study guide in this repo - extract the docx study notes into per-item and per-question Markdown, rank topics by past-exam frequency and the candidate's misses, curate bilingual 中文/日本語 Markdown chapters, and compile the A4 LaTeX printout. Use for any work in this repository, including adding new exam years or notes, re-ranking, writing chapters or rebuilding the PDF.
metadata:
  version: "1.1.0"
---

# Gijutsushi study guide

This repo turns one candidate's study notes into a printed cram guide of about
49 A4 pages for the 技術士 化学部門 一次試験 専門科目. The aim is passing the
exam, not complete teaching. Read
[content-conventions.md](references/content-conventions.md) and
[authoring-syntax.md](references/authoring-syntax.md) before writing content,
and [source-format.md](references/source-format.md) before touching
extraction.

## Contract

- Inputs: docx notes in `source/` (read-only). Hand-edited sources of truth
  are `content/*.md` and `latex/` templates/figures.
- Outputs: `extracted/` and `artifacts/` (both generated, never hand-edit),
  plus the compiled PDF in `artifacts/`.
- Side effects: scripts rewrite only their own generated outputs.
- Prerequisites: Python 3.9+ standard library; XeLaTeX (MiKTeX here) with
  xeCJK, mhchem, chemfig, pgfplots; CJK fonts as described in
  content-conventions.md. On Windows, run Python with `-X utf8`.
- State: none hidden. Decisions live in `content/outline.md`, the references
  and the CHANGELOG.
- Failure: scripts exit nonzero and name the missing input. Do not
  hand-patch generated files to work around a failure.

## State of the repo (update when it changes)

| Stage | Status |
|---|---|
| Extraction (504 questions H23–R7, 344 items, 116 miss rows) | done |
| Coverage/priority report | done |
| Outline with page budget (`content/outline.md`) | v1 approved in principle; 49 p |
| LaTeX template + build (`latex/`, `build.py`) | done; A4 two-column 9pt, XeLaTeX |
| `01_organic.md` 有機化学 | v1 written (all 74 outline items): 7 p against a 13 p budget; awaiting user review of layout and density |
| Chapters 02–05, 考前速記, strategy, glossary, gap appendix | pending (考前速記 is written last) |

## Pipeline

Run from the repository root (`S` = `.codex/skills/gijutsushi-study-guide/scripts`):

1. `python -X utf8 S/docx2md.py source extracted/raw`: docx to ordered Markdown.
2. `python -X utf8 S/extract.py`: items, questions, index CSVs and
   `artifacts/extraction_report.md`.
3. `python -X utf8 S/report.py`: `artifacts/coverage_report.md` (block miss
   rates, item ranking, gap scan from `assets/gap_keywords.tsv`).
4. `python -X utf8 S/source_pack.py <N>`: `artifacts/packs/chapter<N>.md`,
   which holds every outline item of chapter N in full plus the block's
   per-question key lines and 失點紀錄 rows. Read the whole pack, then
   write `content/0N_<slug>.md` in the dialect of authoring-syntax.md.
5. `python -X utf8 S/build.py --png all`: md2tex → `latex/build/`, two
   XeLaTeX passes, `artifacts/study_guide.pdf` and page previews in
   `artifacts/preview/`. It reports pages per chapter against budget, missing
   glyphs and overfull boxes, and exits 1 on errors or missing glyphs.
   `--chapters 01` builds a subset.
6. **Look at the previews.** For every chemfig structure, render a crop at
   250 dpi (`pdftoppm -r 250 -x -y -W -H`) and check substituent positions
   and stereo. A wrong structure teaches a wrong answer.

## Data contracts

- Item ids: `F01`–`F24` are frameworks, `S001`–`S292` are numbered 速查
  entries, `T069`–`T102` are the legacy H27-era series.
- Question ids: `H23-Q01` … `R7-Q35`, plus `R1再-Q..` for the re-exam and
  `OLD-NNN` when no id is known.
- `status` is one of `right`, `right_partial`, `wrong`, `guessed`,
  `missed_log` or `unknown` (see source-format.md).
- Exam blocks: Q1–7 有機, Q8–14 燃料, Q15–21 高分子, Q22–28 無機, Q29–35 計算.

## Growing this repo

- **New notes or a new exam year:** replace or add the docx in `source/`, run
  steps 1–3, and diff `artifacts/coverage_report.md` against the last run. If
  the docx has a new header format or snapshot pattern, update `extract.py`
  and source-format.md together.
- **New gap topics:** add a `label<TAB>regex` line to `assets/gap_keywords.tsv`.
- **Priority or budget changes:** edit `content/outline.md`. Record lasting
  decisions in content-conventions.md.
- **New repeatable step** (for example the LaTeX build): put it in `scripts/`
  with argparse, re-runnable output and UTF-8 I/O, and document it here. Then
  bump `metadata.version` and add a CHANGELOG entry (global skills
  skill-forge and skill-maintenance).
- After adding a skill under `.codex/skills`, run
  `python .codex/skills/publish-workspace-skills/scripts/publish_skill_links.py --fix`.

## Scripts

| Script | Purpose |
|---|---|
| `scripts/docx2md.py` | Linearize .docx (paragraphs, tables, bullets) to Markdown; stdlib only |
| `scripts/extract.py` | Split notes into items/questions, handle snapshots, write index CSVs and extraction report |
| `scripts/report.py` | Block miss rates, item priority ranking, gap scan |
| `scripts/source_pack.py` | Gather one chapter's items and past-question key lines into a single pack |
| `scripts/md2tex.py` | Chapter Markdown dialect → LaTeX fragment (also used by build.py) |
| `scripts/build.py` | Full PDF build, checks, page budget report, PNG previews |

Templates: `assets/latex/main.tex` and `assets/latex/preamble.tex` are copied
to `latex/` only when missing. After changing the asset, copy it over the repo
copy deliberately; check first that the copy holds no hand edits.

## Gotchas

- Write files with Python or editor tools, not Windows PowerShell 5.1
  `Set-Content`, which adds a BOM.
- The Windows console is cp1252, so `print` of CJK text fails without `-X utf8`.
- pandoc is not installed here; `docx2md.py` replaces it.
- Fonts: bold Microsoft JhengHei lacks ◯, so `\maru` uses MS Mincho. Symbol
  ranges (①, ★, ■) are routed to the CJK fonts by `\xeCJKDeclareCharClass`.
  `\tracinglostchars=2` makes missing glyphs show in the log, which build.py
  then fails on.
- mhchem: no primes (`R'2` errors), so use `R^1R^2`. Put Japanese arrow
  labels in `->[{\text{…}}]`. Wrap `\underset` in `$…$` outside `\ce`.
- chemfig: branch angles on ring atoms are absolute (`-[:170]`); relative
  `[::x]` points into the ring. For a left-hand group like `MeO_2C`, attach
  to the C with `-[:150,,,3]`. Lengthen arrows with `\arrow{…}[,1.4]`.
