# Chapter authoring syntax (content/NN_name.md → LaTeX)

`scripts/md2tex.py` converts a restricted Markdown dialect. Use only what is listed
here; anything else is printed as plain text.

## File

- Name: `content/NN_slug.md`. NN orders the chapters, and only files starting
  with two digits are built (`outline.md` is not).
- First lines:
  ```
  <!-- budget: 13 -->
  # 有機化学 | Q1–Q7 ・ 失分率 63% ・ 弱項
  ```
  The `budget` value is the page target. `build.py` reports actual pages
  against it. Text after `|` in the title is the banner subtitle.

## Blocks

| Markdown | Output |
|---|---|
| `## 1.2 置換・脱離 {S003 S074 T070}` | Section with tiny source tags (`#3 #74 #70H27`); added to the table of contents |
| `### heading {S108}` | Subsection |
| `#### heading` | Run-in bold label |
| paragraph lines | Paragraph (consecutive lines join) |
| `- item` / `1. item` (2-space indent = level 2) | Compact lists |
| pipe table | Full-column `tabularx`. Columns whose cells are all ≤4 chars are narrow and centered. `<!-- cols: X:1.3 c X:0.7 -->` on the line before overrides this (`X:f` = relative width; the f values must sum to the number of X columns). |
| `> [!trap] 標題` + following `>` lines | Red-edged 陷阱 box (body may hold paragraphs, lists, tables) |
| `> [!key] 標題` | Blue 要點 box |
| `> [!memo] 標題` | Grey 一句速記 box |
| `> [!exam] R5-Q3` | 過去問 box |
| ```` ```chem ```` … ```` ``` ```` | Raw chemfig / `\schemestart` code, centered, shrunk to column width |
| ```` ```tikz ```` | Raw TikZ/pgfplots, centered, shrunk to column width |
| ```` ```latex ```` | Raw LaTeX, passed through untouched |
| `---` | Thin separator |
| `<!-- anything -->` | Dropped (except `budget` and `cols`) |

## Inline

| Markdown | Output |
|---|---|
| `**bold**` | Bold |
| `==key==` | Highlight (bold + accent colour; still readable in grayscale) |
| `` `code` `` | Monospace |
| `$...$` | Math, passed raw (may contain `\ce{}`) |
| `\ce{...}` | mhchem, passed raw |
| `◯` / `✗` | Exam marks: `◯` = true statement, `✗` = trap |
| `{{ja:漢字}}` | Force the Japanese font on a kana-free term |
| `₀–₉ ⁰–⁹ ⁺ ⁻` | Converted to sub/superscripts |

## Font switching (automatic)

Body text uses the Traditional Chinese font. Any run that contains kana
(hiragana/katakana), together with the kanji directly attached to it, is set
in the Japanese font, so `カルボン酸誘導体` renders with Japanese glyphs.
Kana-free Japanese terms (e.g. 求核置換) stay in the Chinese font unless
wrapped in `{{ja:…}}`. Each family falls back to the other for glyphs it lacks.

## Conventions (see content-conventions.md)

- Exam-style statements go in tables `| 敘述（題目語氣） | ◯✗ | 理由 |`, with
  the answer column last so it can be folded under.
- Put the item tags of the source entries on every `##`/`###` heading.
