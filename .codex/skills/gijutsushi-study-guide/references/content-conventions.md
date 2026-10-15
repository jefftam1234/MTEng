# Content conventions for the study guide

## Reader and goal

The reader is a Hong Kong chemistry graduate, about 15 years out of university,
who studied in Traditional Chinese and now takes the exam in Japanese. The goal
is **passing the exam (cramming)**, not complete teaching. 有機 and 高分子 are
self-taught weak areas, with miss rates of about 63% and 70%, so they get the
most pages. The guide is printed and read on paper.

## Size and structure (agreed 2026-10-15)

- The original aim was at most 50 text pages, excluding reaction equations, structures and diagrams. After the expanded bilingual draft measured 56, the user explicitly relaxed the cap to **56 text pages**. Keep A4, two columns, **11pt**. The full physical print count is longer because figures and the generated question index are outside the cap.
- The recalibrated plan allocates 52 text pages with four pages of headroom; organic chemistry has 16 and polymers 12. The three-page quick sheet replaces the older two-page description. Do not pad to the cap.
- Count using `build.py --text-only`; it removes fenced chem/tikz figures, standalone reaction displays and chapter 98. Captions, tables, worked reasoning and inline equations remain charged. The result is conservative, reproducible pagination, not an estimate obtained by subtracting guessed figure areas.
- The live plan is `content/outline.md`: chapters by exam block, per-section
  page budgets, and item ids with treatment levels. Update it when priorities
  change.
- Front matter has a strategy page and a 3-page 考前速記 sheet (written last,
  from all 一句速記 lines and 失點紀錄 對策). Back matter has a 中/日/英
  glossary and the gap appendix (headings and stub outlines only, no
  invented content).

## Treatment levels

- ★ full: rule, ◯/✗ trap lines, and an example or scheme. Used when an item
  appears in two or more years, or was ever missed.
- ● condensed: a table row or 2–3 bullets.
- ・ one-liner.
- Merges are written `A+B`.
- Meta/trend items (S102 S136 S141 S164 S174 S194 S234 T077) only feed the
  考前速記 sheet.

## Writing rules

- Explanations and reason cells use Traditional Chinese. Japanese chemical names, terms and reaction names receive a Chinese gloss at first use in each numbered section, including tables. Japanese exam-statement cells stay Japanese; their first-use gloss goes in the adjacent reason cell. Separate glossary columns also count as pairing. Do not repeat glosses on every later occurrence. Raw figure labels and formula-only symbols are outside this prose convention.
- Write facts as ◯ (true) / ✗ (trap) statements in the exam's 誤っているもの
  style. Distinguish exact source wording from practice statements reconstructed from source notes; never claim a summary is a verbatim exam quotation.
- Trap tables put the answer in the right-hand column (fold-to-quiz).
- Graphs only where a question asks about the shape of a curve. Planned graphs
  are listed per chapter in the outline.
- Energy statistics and policy numbers are tagged 「最新値を確認」.
- Every chapter section cites its item ids in heading tags so it can be traced
  back to `extracted/items/`.

## Rendering

XeLaTeX + xeCJK with two CJK font families. Traditional Chinese uses Microsoft
JhengHei / PMingLiU; Japanese uses Yu Gothic / MS Mincho, switched explicitly
so kanji keep Japanese glyph shapes. mhchem handles equations, chemfig handles
structures, and TikZ/pgfplots handles graphs. These fonts ship with Windows;
other machines need a substitute such as Noto Sans/Serif TC and JP.
