# 技術士（化学部門）一次試験 専門科目 — Study guide outline (v1 revised; awaiting print review)

Target: **at most 56 text pages**, A4, two-column, **11pt**. The user relaxed the original 50-text-page cap to 56 after reviewing the first paired-language draft. Reaction equations, structures, schemes, diagrams and the generated past-question index are outside this limit. Figures never substitute for explanatory depth.

Budget proof: `build.py --text-only` omits fenced `chem`/`tikz` displays, standalone reaction displays and chapter 98, but retains captions, worked examples, all tables and inline formulas/equations. This is a conservative count: inline chemistry is still charged. `artifacts/study_guide_text_budget.pdf` and its `_pages.json` record the result. Run the full build afterward for the print copy. These are two separate pagination systems; the full print PDF can exceed 56 pages.

The 11pt content plan below allocates **52 text pages**, with **4 pages of headroom** under the approved cap. Page targets include chapter-end whitespace. Do not pad to 56 or change font size to force a count. The previous headline allocations summed to 55 despite the printed total of 49; this table replaces that inconsistent arithmetic.

## Basis (from `extracted/` and `artifacts/coverage_report.md`; regenerate with the `gijutsushi-study-guide` skill scripts)

- 504 past questions H23–R7 (15 years), 344 速查 entries (F01–F24 frameworks, S001–S292, legacy T069–T102), 116 miss-log rows.
- The exam has 5 fixed blocks × 7 questions. You answer **25 of 35**, and need **≥50%**.
- Your miss rate per block (questions with a recorded result):

| Block | Questions | Miss rate | Text pages |
|---|---|---|---|
| Title and contents | | | 2 |
| 有機化学 | Q1–7 | 63% | 16 |
| 高分子 | Q15–21 | **70%** | 12 |
| 燃料・エネルギー | Q8–14 | 49% | 4 |
| 無機・セラミックス・電気化学 | Q22–28 | 44% | 6 |
| 化学工学・物理化学（計算） | Q29–35 | 32% | 4 |
| Front: strategy + exam-morning sheet | | | 1 + 3 |
| Reference: glossary and reaction-name navigation | | | 3 |
| Appendix: gap stubs | | | 1 |
| **Allocated text total** | | | **52** |
| **Unallocated headroom** | | | **4** |
| **Approved text cap** | | | **56** |
| Generated question index, equations and figures | | | **outside cap** |

## Treatment levels

- ★ **full**: rule + ◯/✗ trap lines + worked example or scheme. Applies to items that recur across years (≥2 years) or that you missed.
- ● **condensed**: table row or 2–3 bullet lines.
- ・ **one-liner**: a single line in a summary table.
- Merged items are written `A+B`.
- Meta/trend items (S102, S136, S141, S164, S174, S194, S234, T077) are not chapters. Their trap patterns feed Part A.

Explanations and reason cells use Traditional Chinese. Pair Japanese chemical names, terms and reaction names with Chinese at first use in each numbered section, including table cells. Keep the deliberate Japanese statement column intact; put its first-use translation in the adjacent reason cell. The glossary may pair separate columns. Later repetitions need not repeat the gloss. Formula-only symbols and raw figure labels are not prose glossary entries. The right-hand answer/reason cells support fold-to-quiz use.

---

## Front matter (4 text p)

- **0. 使用法與應試策略** (1 p): block map, the 25-of-35 choice, the 50% line, how to read ◯/✗ lines, fixed calculation routine.
- **A. 考前速記 exam-morning sheet** (3 p): written last, drawn from every 一句速記 and 失點紀錄 對策. Covers top traps, numbers to memorise, and confusable 日文 terms (F02, F09).

## 1. 有機化学 Q1–7 (16 text p)

| § | Topic | Items | Pages |
|---|---|---|---|
| 1.1 | 試薬 → 反応 framework・日文試薬名 | F01★ F02★ F06★ S224★ S107★ F05● F09● S038● S167● S261・ | 3.0 |
| 1.2 | 置換・脱離 (SN1/SN2/E1/E2) | S003★+S074 S195★ S237★ F04● S255● S140● T070● S106・ | 2.0 |
| 1.3 | 付加・アルケン/アルキン・syn/anti | F03★ S138★ S240★ S258+T069● S139● S034・ | 2.0 |
| 1.4 | 芳香族 (EAS, 定位, SNAr, ベンザイン, フェノール) | S260★ S281★ S198★ SNAr(R7-Q2)★ S033+S170● S166● S207● T073● S039・ T072・ | 2.5 |
| 1.5 | C–C 結合生成・人名反応・ペリ環状 | S235★ S196★ S168★ S236★ S208● S105● S071● S226・ | 2.5 |
| 1.6 | 立体化学 (R/S, キラリティー, いす形) | S210★ S108★ S238★ S037● S169● S257● S282● S072・ | 1.5 |
| 1.7 | 酸・塩基・電子効果 | S068★ S209+S239★ S225★ T071● S142● S070・ S103・ | 1.0 |
| 1.8 | 構造解析 (NMR/IR/UV/MS) | S035★ S069★ S227★ S171● S197● S004● S256● S259・ S020・ | 1.0 |
| 1.9 | 天然物・物性ほか | S073・ S104・ S001・ S002・ S211・ | 0.5 |

Schemes (free): SN2 inversion / SN1 racemisation, E2 anti-periplanar, Markovnikov vs anti-Markovnikov (HBr/peroxide), hydration three ways, EAS σ-complex + directing table, benzyne, SNAr Meisenheimer, Grignard, Wittig, Stork enamine, Diels–Alder (endo), Hofmann/Curtius, acetal protection, LiAlH₄ vs NaBH₄ scope, cumene process, cyclohexane chair ax/eq.

## 2. 高分子 Q15–21 (12 text p)

| § | Topic | Items | Pages |
|---|---|---|---|
| 2.1 | 重合形式の分類 (重縮合/重付加/付加縮合/開環) | F07★ S082★ S271★ S148★ S249★ S204★ S116★ S011● S086● S046● | 2.3 |
| 2.2 | 連鎖重合: ラジカル・イオン・開始剤 | S150★ S230★ S177● S268● T082● | 1.8 |
| 2.3 | 分子量 vs 転化率・逐次重合の定量 | S213+S269★ S117★ S012● T086● | 1.2 |
| 2.4 | 共重合・立体規則性 | S014+S214★ S013● T087● S049● | 1.1 |
| 2.5 | 分子量と測定法 (Mn/Mw, 浸透圧, 光散乱) | S129+T081★ S154★ S270★ S081★ S179+T083● S050● | 1.5 |
| 2.6 | 物性: Tg/Tm・弾性率温度曲線・DSC・粘弾性・ゴム | S084★ T085+F18★ S152★ S083★ S115★ S247★ S045● S118● F10● S096● S151● S203● S178● S015● S176● F11● | 2.5 |
| 2.7 | 材料・用途・高分子反応 | S289★ S267★ S119+S248★ S153★ S205★ S288★ S202★ S149+T084● S051● F19● S215・ S052・ | 1.4 |
| 2.8 | 高分子化学史 | S085+S048● | 0.2 |

Graphs: Mₙ vs conversion (chain / living / step), copolymer composition curves (r₁, r₂), modulus–temperature five regions, DSC trace, stress–strain, stress relaxation vs creep (spring/dashpot).
Structures: nylon-66/6, PET, aramid p/m, phenol/urea/melamine resins, PVA→vinylon, ring-opening monomers.

## 3. 燃料・エネルギー Q8–14 (4 text p)

All energy statistics are flagged **「最新値を確認」** because they change every year.

| § | Topic | Items | Pages |
|---|---|---|---|
| 3.1 | エネルギー統計・政策 | S212★ S199★ S283★ S264● S109● S228● S241● S242● S005+S143● T074・ | 0.7 |
| 3.2 | 石油精製 (FCC, 接触改質, アルキル化, HDS, BTX) | S243★ S111★ S145+T076★ S077● S262● S263● S201● S007・ S042・ | 0.9 |
| 3.3 | 石油製品の規格・物性・発熱量 | S112★ S110+T075★ F08● S076● S043● S144● S078● S284+T078● S146● S008● S200● S172・ S006・ | 0.9 |
| 3.4 | 潤滑油 | S113★ S265★ S287★ S173● S244● S079● T079・ S044・ S009・ | 0.5 |
| 3.5 | 石炭 | S114★ S147★ S080+T080● S010・ S245・ | 0.4 |
| 3.6 | 新燃料・水素・SAF・有機ハイドライド | S229★ S246+S285★ S266+S286● S040● S041● S018・ S075・ | 0.6 |

Diagram: refinery flow (crude → atmospheric/vacuum → FCC/reformer/HDS → products).

## 4. 無機・セラミックス・電気化学 Q22–28 (6 p)

| § | Topic | Items | Pages |
|---|---|---|---|
| 4.1 | 元素・化合物 (酸化物の酸塩基, ハロゲン, 炭素同素体) | S180+S054★ S090+S017★ F13● T092● S123● S055・ S053・ S022・ T088・ | 1.0 |
| 4.2 | 無機工業・金属精錬 | S231★ S125★ S092★ S182● T094● S056・ | 0.8 |
| 4.3 | 結晶構造・欠陥・XRD | S158★ S253★ S186+T090★ S159+S272★ S185★ S251★ S124● S252● | 1.2 |
| 4.4 | セラミックス製造・熱伝導 | S218★ S156★ S216+S274★ S157★ S277● S276● S278・ | 1.2 |
| 4.5 | 機能材料・ガラス・半導体・レーザー | S155★ S250★ S273★ S019★ S093+S232★ S126★ S091+S121+S275★ S021● S122● S183● S217● T089● S057・ S059・ | 1.0 |
| 4.6 | 電気化学 (電解, ファラデー, 電池, ネルンスト, コロイド) | F12★ S087★ S120★ S088★ S089★ S016● T093● F21● S058・ | 0.8 |

## 5. 化学工学・物理化学（計算）Q29–35 (4 text p)

The 公式集 is folded in here. Each formula gets a 検算 line (dimension/magnitude check).

| § | Topic | Items | Pages |
|---|---|---|---|
| 5.0 | 計算前の固定動作・単位換算 | 公式集§0 S102● S164● | 0.3 |
| 5.1 | 物理化学 (気体, 相律, 熱化学, エントロピー, 気液平衡) | S187+T102★ S132★ S130★ F14● S025● T099● S206● S024● S026+S098● S027● S190+T096● S135● S127● T095● S184● | 1.0 |
| 5.2 | 反応速度・反応器 | S254★ S292★ T101★ S131★ S220+S023★ S066・ | 0.7 |
| 5.3 | 流体 | S101+S062★ S095● S030● S291● S222● S031+S097+T100● S028・ | 0.7 |
| 5.4 | 伝熱 | S193+S223+S063★ S133+T097★ S094● S099● S032● S064● S065● | 0.6 |
| 5.5 | 分離・物質収支 (蒸留, 抽出, 吸収, 吸着, 膜, 湿度, 燃焼, 晶析) | T098★(repeat miss) S189+S128+S061★ S221+S290★ S029● S100● S161● F22● S067+S134+S192+S219● S233● S160+S060● S162● S163+S191● | 0.7 |

Graphs: Levenspiel (CSTR/PFR), T-x-y diagram, McCabe–Thiele, triangular diagram + lever rule, absorption operating line, CO₂ phase diagram, Arrhenius plot, Michaelis–Menten.

## 6. Reference (3 p)

中／日／英 glossary (consolidated from all items), カタカナ構詞 (F05), 人名反応 index pointing to sections.

## Appendix: gaps (1 p, headings + stub outline only)

Topics that are thin or absent in your material, kept as headings to fill later. The source is the gap scan in `artifacts/coverage_report.md` (≤5 hits = gap; "thin" = 6–10 hits):

- 分析化学: 滴定 (0), 吸光光度法 Lambert–Beer (4); thin: クロマトグラフィー, 原子吸光/ICP
- 化学平衡: thin: 平衡定数・ルシャトリエ, ΔG°＝−RT ln K
- 電気化学: 腐食・防食 (2), めっき・電解精錬 (0)
- 錯体化学 (thin)
- 生体分子: 核酸 (0); thin: 糖, 酵素
- 界面化学: 界面活性剤 (4)
- 単位操作: 粉体・粉砕 (4); thin: 晶析
- 安全: 爆発限界・燃焼範囲 (0)
- グリーンケミストリー・原子効率 (0)

## Build notes

- Hand-edited master sources are `content/*.md`, except generated `98_qindex.md`, and `latex/` templates/figures. Compiled chapter fragments live in generated `latex/build/`. Keep A4 two columns at **11pt** for both builds. Schemes/graphs use TikZ/chemfig, including fenced blocks in the chapter sources.
- Engine: XeLaTeX + xeCJK. 中文 uses Microsoft JhengHei/PMingLiU; 日文 uses Yu Gothic/MS Mincho as a separate font family, so kanji keep Japanese glyph shapes.

## Revision evidence

Organic and polymer depth now includes source-pack question summaries and R-era miss-log fixes, additional Japanese ◯/✗ rows with Chinese reasons, and worked reasoning for the starred frameworks. New facts cite item tags; the added practice boxes are **note summaries, not verbatim full exam questions**. Existing source limitations still require user review; source notes are not independently certified chemistry references. The 56-page relaxation authorizes space, not general-knowledge gap filling.
