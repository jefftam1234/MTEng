# Changelog

## 1.3.0 - 2026-10-15

- User request: a single skill folder, loaded from AGENTS.md. Removed the `.agents/skills`, `.claude/skills` and `.grok/skills` junctions. They were removed as links only (`cmd /c rmdir`), and the canonical file count stayed at 18 before and after. Git had been tracking four copies of the skill through these junctions.
- Removed the `publish-workspace-skills` skill from this repo, because its only purpose was recreating those links. AGENTS.md now imports this skill with `@.codex/skills/gijutsushi-study-guide/SKILL.md` (CLAUDE.md imports AGENTS.md). `.gitignore` excludes `.agents/`, `.claude/skills/` and `.grok/`.
- AGENTS.md also states the exception that `content/98_qindex.md` is generated and must not be hand-edited.
- Contract impact: loading mechanism changed (import instead of per-agent skill directories). Claude Code no longer lists this skill under its Skill tool; the content loads with the project instructions instead. No script changes.
- Validation: check_skill.py passed; git index verified to contain one copy of the skill.

## 1.2.0 - 2026-10-15

- Completed guide v1 at the user's request ("go with your suggestion, and give me the full doc, then commit and push"): chapters 02–05, strategy (00a), 考前速記 (00b), glossary (06), past-question index (98, generated) and gap appendix (99). The result is 50 pages.
- New script: qindex.py (past-question index from index_questions.csv, chunked to 24 rows per table).
- build.py: content keys like 00a/00b/98; non-numeric keys use a `<!-- label: … -->` banner; vertical-overflow detection fails the build.
- md2tex.py:
  - Banner label override.
  - ASCII subscripts (`V_m`).
  - Proportional automatic column widths.
  - Mismatched `cols` specs are ignored with a warning.
  - `{}` guard so a table cell starting with `[` is not read as a spacing argument.
  - `\item{}` guard so a list item starting with `[` keeps its brackets.
  - Section tags can wrap.
- Template: 11pt; xeCJK `AutoFallBack=true`; ※ routed to CJK fonts; TikZ positioning library; ⊃ ⊂ ∈ ∞ mapped to math.
- Repo: requirements.txt (stdlib only, plus system requirements).
- Contract impact: compatible additions. Content file naming is widened (still numeric-prefixed), and the output now has 50 pages.
- Validation (executed):
  - Full build: 50 pages, 0 errors, 0 missing glyphs, 0 overflow (>3pt), 0 vertical overflow.
  - Two vertical overflows were caught by the new check and fixed: the index table and the glossary table.
  - Previews inspected for pages 1, 3, 4, 9–12, 24, 38, 40.
  - Chemfig structures re-verified at 250 dpi: sulfanilic route, Diels–Alder product (cis esters, C=C between the methyl-bearing carbons), and both hydration products. The p-toluic acid bromination and benzyne schemes are unchanged since 1.1.0.
  - Subscript conversion unit-checked.
- Limitation: chemistry content was checked against the source notes by the author only; the user has not yet reviewed it.

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
