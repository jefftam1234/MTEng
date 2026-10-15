# 技術士（化学部門）一次試験 study guide

A printable cram guide for the **専門科目** of Japan's 技術士 first-stage exam
(chemistry), written for a reader who studied chemistry in Traditional Chinese
and now sits the exam in Japanese.

## What this produces

- An A4 two-column PDF of about 49 pages of text, plus reaction schemes,
  structures and a few graphs (these don't count toward the page budget).
- Every term is paired 日本語 ↔ 中文 (with English where useful). Facts are
  written as ◯/✗ statements in the exam's 「誤っているもの」 style.
- 有機化学 and 高分子 get the most space because they are the weak areas
  (past miss rates about 63% and 70%).
- The guide ends with an appendix of headings for topics the notes don't yet
  cover.

## How it is built

1. The original notes (three Word files in `source/`) are split into one small
   Markdown file per topic and per past question (`extracted/`).
2. A report ranks topics by how often they appeared in past exams (H23–R7)
   and how often they were answered wrongly (`artifacts/coverage_report.md`).
3. The chapter plan with page budgets is in `content/outline.md`. The
   chapters are written as Markdown in `content/`.
4. The chapters are typeset with LaTeX (`latex/`) into a PDF in `artifacts/`.

## Layout

| Folder | Contents | Edit by hand? |
|---|---|---|
| `source/` | Original Word notes | No (read-only) |
| `extracted/` | Topics and questions split out of the notes, index CSVs | No (regenerated) |
| `artifacts/` | Reports and the built PDF | No (regenerated) |
| `content/` | Outline and chapter Markdown: the master copy | **Yes** |
| `latex/` | Print template, figures, chapter `.tex` | Yes (templates/figures) |
| `.codex/skills/` | Scripts and instructions for AI agents working here | Via agents |

## Rebuilding

From the repository root, with Python 3:

```
python -X utf8 .codex/skills/gijutsushi-study-guide/scripts/docx2md.py source extracted/raw
python -X utf8 .codex/skills/gijutsushi-study-guide/scripts/extract.py
python -X utf8 .codex/skills/gijutsushi-study-guide/scripts/report.py
python -X utf8 .codex/skills/gijutsushi-study-guide/scripts/build.py
```

The last command produces `artifacts/study_guide.pdf` (it needs XeLaTeX and
the Windows CJK fonts). Add `--png all` to also get page images in
`artifacts/preview/`.

## Status

Chapter 1 (有機化学) is written and typeset as the layout sample. The other
four exam blocks, the exam-morning sheet, the glossary and the gap appendix
are still to come.
