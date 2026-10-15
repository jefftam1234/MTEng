# Changelog

## 1.1.0 - 2026-10-15

- User approved building the LaTeX template and the 有機化学 sample chapter ("let's do it").
- Added scripts: source_pack.py (per-chapter source pack), md2tex.py (Markdown dialect → LaTeX), build.py (XeLaTeX build, glyph/overfull/page-budget checks, PNG previews). Added assets/latex/main.tex and preamble.tex (A4 two-column 9pt; PMingLiU/JhengHei for 中文, MS Mincho/Yu Gothic for 日本語 with mutual fallback; trap/key/memo/exam boxes; ◯/× marks). Added references/authoring-syntax.md.
- extract.py fix: table rows in extracted items are kept contiguous, and adjacent tables stay separate. Previously every row was separated by a blank line. Regenerated extracted/; index CSVs unchanged.
- Contract impact: compatible additions; the outputs latex/build/, artifacts/study_guide.pdf, artifacts/preview/ and artifacts/packs/ are all generated.
- Validation (executed): build of content/01_organic.md passed: 8 pages, 0 missing glyphs (checked after fixing the log regex; an injected ◯-in-bold case was detected), 0 overfull boxes, chapter 1 = 7 pages against a 13-page budget. Preview pages 2, 4, 5 and 6 were inspected visually. Chemfig structures were checked at 250 dpi: p-toluic acid bromination, benzyne amination and both hydration products are correct after one fix (acid-hydration branches had pointed into the ring). Limitation: content correctness was reviewed by the author only; the user has not yet reviewed it.

## 1.0.0 - 2026-10-15

- Created at the user's request: a repo-specific skill so future agents can use and evolve this repo. Scaffolded with skill-forge (new_skill.py, bootstrap_workspace.py).
- Folded the session's ad-hoc scripts: tools/docx2md.py and tools/extract.py became scripts/docx2md.py and scripts/extract.py (argparse, repo root derived from location or `--repo`, source names as flags). The ad-hoc PowerShell analyses (block miss rates, item ranking, gap keyword scan) became scripts/report.py with assets/gap_keywords.tsv. tools/ was removed.
- Captured knowledge: references/source-format.md (snapshot stacking, T-series, H27-only-in-snapshot-2, header formats, status markers, block structure) and references/content-conventions.md (reader, goal, budget, treatment levels, writing and rendering rules).
- Contract impact: new skill; no existing callers.
- Validation (executed): the folded docx2md.py + extract.py reproduced all 854 files in extracted/ byte-identically to the pre-fold run (hash comparison). report.py output matched the earlier manual analysis (block miss rates; 62% vs 63% for 有機 is a rounding difference on 25/40). check_skill.py with --run-help passed. Limitation: the LaTeX build stage does not exist yet.
