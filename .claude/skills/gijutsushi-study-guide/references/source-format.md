# Source format: the study-note docx files

Findings from the first extraction (2026-10-15). `extract.py` implements every
rule below. Re-check them when new source files arrive.

## Files in `source/`

| File | Content | Size (text) |
|---|---|---|
| 技術士_専門_公式集.docx | Formulas for calculation questions, each with 出處 (e.g. R5-Q29) | ~7K chars |
| 技術士_有機_解題筆記.docx | Question-by-question write-ups (考點, 陷阱, 一句速記) plus per-batch 失點紀錄 tables | ~515K chars |
| 技術士_有機_試劑速查.docx | Topic reference: frameworks １–２４, numbered items 1–292 | ~300K chars |

Despite the 有機 in the names, both large files cover all five exam blocks.
No source contains images, so every structure, scheme and graph has to be drawn.

## Snapshot stacking (the main trap)

Each large docx is **three snapshots pasted one after another**. Each snapshot
starts with the line `技術士（化學部門）一次試驗`.

- 速查: snapshots 1 and 2 stop at item 67. Snapshot 3 (the last) holds 1–292
  and is the one extracted.
- **Snapshot 2 has a separate full-width series ６９–１０２** written during
  the H27 pass. Snapshot 3 reused numbers 68+ for different H28+ topics, so
  about 22 of the old entries survive only in snapshot 2. They are extracted as
  `T069`–`T102`. Questions from H27 that cite 速查第69–102項 point to the T
  series; all other citations point to S.
- 解題筆記: snapshots are **not cumulative**. The H27 write-ups (34 questions)
  exist only in snapshot 2. Questions are therefore taken from all snapshots,
  keeping the last copy per question id.
- Numbering gaps in 速查 (47, 137, 165, 175, 181, 188) are genuinely absent
  from the source.

Raw files are 2–4× larger than their real text when parsed with a naive regex
over `document.xml`. Use the XML parser in `docx2md.py`.

## Question headers

- Older era: `問 N　<title>（答：…）`. These sometimes embed an id
  (`問 61　H24-Q28 …`). Without an id the question becomes `OLD-NNN`.
- Newer era: a line containing only `H25-Q5` / `R1再-Q7` / `R7-Q35`, followed by
  `主題：<topic>　正解：<answer>　用戶答對|用戶答錯（選 ③）…`.
- Year tokens: `H23`–`H30`, `R1再` (re-exam; there is no plain R1), `R2`–`R7`.

## Result markers → `status`

| Marker in 主題 line | status |
|---|---|
| 用戶答錯 | wrong |
| 猜 (guess) | guessed |
| 用戶答對 with 理由錯 / 說法需修正 / 不確定 | right_partial |
| 用戶答對 | right |
| none, but listed in a 失點紀錄 table | missed_log |
| none | unknown (most of H23–H30) |

`失點紀錄` tables follow a line `R5（問1〜問7）　本批失點紀錄` and have the
columns `題 | 類型 | 對策`.

## Exam structure inferred from the questions

There are 35 questions in five fixed blocks: Q1–7 有機, Q8–14 燃料・エネルギー,
Q15–21 高分子, Q22–28 無機・セラミックス (with electrochemistry), and
Q29–35 化学工学・物理化学 calculations. Older years (H26) are shifted by
about one question. The candidate answers 25 of the 35 and needs 50%.
Confirm this against the current 受験案内.
