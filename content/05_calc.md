<!-- budget: 4 -->
# 化学工学（化學工程）・物理化学（物理化學）（計算） | 問29〜問35 ・ 過去失分率 32% ・ 得点源

> [!key] 本章用法
> 計算題常不是公式不會，而是**單位、係數銜接、基準點**出錯。答案相差數倍先估量級；差距小則把式連起來，最後再代入，避免中途取整。

## 5.0 計算前の固定動作 {S102 S164}

| 換算 | 倍率 | 罠の例 |
|---|---|---|
| mm → m | ×10⁻³ | 管径 3 mm → 0.003 m（L/D會差1000倍） |
| kPa・kJ → Pa・J | ×10³ | 先令潛熱與質量／莫耳基準一致 |
| ℃ → K | ＋273.15 | 公式T通常取絕對溫度（ΔS ＝ ΔH/T、アレニウス（阿瑞尼斯）） |
| vol% → 小数 | ÷100 | 空気中 O₂ 0.21 → 空氣量以O₂量 **÷0.21** |
| L → m³、g → kg | ×10⁻³ | — |

> [!memo] 固定動作 6 項目（H28・H30 の失点から）
> ①圈出液面／噴嘴、內徑／外徑、液深／槽深、側面／全面並畫圖。②連式後代入、不早取整。③確認求T還是ΔT、比值還是總量。④把空氣比／收率帶到下一步。⑤查數據是否使用，也留意密度、槽尺寸等誘餌。⑥回代檢查反應率0〜1、莫耳分率≤1、含損失流速低於√(2gh)。

| 概数 | 値 | 概数 | 値 |
|---|---|---|---|
| √2 ／ √3 | 1.414 ／ 1.732 | ln 2 ／ ln 10 | 0.693 ／ 2.303 |
| √5 ／ √10 | 2.236 ／ 3.162 | e ／ e⁴ | 2.718 ／ ≈54.6 |
| 1/0.21 | 4.762 | 0.79/0.21 | 3.762 |
| R | 8.314 J/(mol·K) ＝ 0.0821 L·atm ＝ 0.083 L·bar | F | 96 485 C/mol |

立方根以已知值夾估：1.1³＝1.331、1.15³＝1.521、1.2³＝1.728，2^(1/3)≈1.26。平方根可抽出（萃取）完全平方，如√44400＝20√111≈210.7；或用牛頓近似√N≈a−(a²−N)/(2a)。

## 5.1 物理化学（物理化學） {S187 T102 S132 S130 F14 S025 T099 S206 S024 S026 S098 S027 S190 T096 S135 S127 T095 S184}

### 気体 {F14 S025 T099 S206 S024 S127}

- PV＝nRT，先按R選P、V單位。理想氣體vol ppm＝mol ppm；22.4 L/mol限0 ℃、1 atm，其他條件回PV＝nRT（H25-Q28）。
- 等溫連通兩槽：P＝(P₁V₁＋P₂V₂)/(V₁＋V₂)，由總mol守恆、RT約去（R5-Q30）。
- 范德華式對1 mol為(P＋a/V²)(V−b)＝RT；Z＝PV/RT，接近凝結時可小於1。
- 相律F＝C−P＋2，單成分氣液共存F＝1、三相點F＝0。CO₂臨界31 ℃／7.38 MPa，三相點−56.6 ℃／0.518 MPa；氣液差異消失與三相共存不同。
- 氣體黏度與熱導率通常隨溫度**增大**；液體黏度下降。汽化潛熱隨壓力增高而減，臨界點為0。
- ジュール・トムソン効果（焦耳–湯姆孫效應）為等焓節流。筆記常溫比較：H₂／He／Ne可升溫，N₂／空氣／CH₄／CO₂降溫。噴霧罐蒸發冷卻另屬汽化潛熱，不能全稱JT。

### 熱力学（熱力學） {S190 T096 S027 S026 S098 S135}

| データ | 反応熱 ΔH |
|---|---|
| 生成エンタルピー（焓） | ΣΔH_f(生成物) − ΣΔH_f(反応物) |
| 燃焼エンタルピー | ΣΔH_c(==反応物==) − ΣΔH_c(生成物)（方向與生成焓相反） |

- 放熱的ΔH＜0；工程「放熱量」常報正值。估量級：脫水／異構化常＜50，加成／取代約50〜150，燃燒約500〜3000 kJ/mol。
- ヘスの法則（赫斯定律）按路徑相加：C→CO₂為111＋283＝394 kJ/mol；只取CO→CO₂的283會漏一步（H27-Q29）。
- ΔG＝ΔH−TΔS，ΔG°＝−RT lnK＝−nFE°。相變ΔS＝ΔH/T，**用K**：188 J/g÷540 K≈0.35 J/(g·K)，用℃會得錯誤0.70。
- ボルツマン（波茲曼） S＝R lnW。PE鏈熔融ΔS＝R ln(3/1)≈8.31×1.10＝9.14 J/(K·mol)，不能漏R。
- 封閉斷熱剛性容器自由膨脹守ΔU＝0，理想氣體ΔT＝0；節流閥守ΔH＝0。PVᵞ＝常數只用於可逆斷熱，T₂/T₁＝(P₂/P₁)^((γ−1)/γ)；空氣壓比10、298 K約到575 K。題目給γ不代表必須用。

### 溶液と気液平衡 {S187 T102 S132 S130 T095}

| 法則 | 対象 | 式 |
|---|---|---|
| ラウール（拉午耳） | 溶媒（溶劑）（x → 1） | p_A ＝ x_A p_A° |
| ヘンリー（亨利） | 溶質（x → 0、希薄） | p_B ＝ k_H x_B |
| 非理想 | — | pᵢ ＝ ==γᵢ== xᵢ pᵢ° （已給活度係數就要乘入） |

- 正偏差γ＞1連到低沸共沸（乙醇／水）；負偏差γ＜1連到高沸共沸（氯仿／丙酮）。「γ永遠大於1」錯。
- 理想二元泡點：x₁＝(P−p₂°)/(p₁°−p₂°)，y₁＝p₁°x₁/P；α＝p₁°/p₂°，y＝αx/[1＋(α−1)x]。理想混合總壓應介於純成分蒸氣壓。
- 非揮發溶質沸點升高：先算溶劑莫耳分率，以p*＝P/x_溶劑查溫度。NaCl按解離粒子數乘2；15 wt%例約103 ℃，漏解離會落101〜102 ℃。用ΔTb＝Kbmi估量級。
- T102例：甲醇0.10×1.786×236.7＝42.3 kPa；水0.90×1.009×64.24＝58.3；氣相甲醇y＝42.3/100.6≈42%，漏活度係數會得約24%。

```tikz
\begin{tikzpicture}
\begin{axis}[name=txy,width=5.2cm,height=4.6cm,xmin=0,xmax=1,ymin=60,ymax=104,
  xlabel={$x,\ y$（低沸点成分）},ylabel={温度},xtick={0,1},ytick=\empty,
  every axis label/.style={font=\scriptsize},tick label style={font=\tiny},title={\scriptsize T-x-y 図},title style={yshift=-4pt}]
\addplot[thick,blue!70!black,domain=0:1,samples=40] ({x},{100-35*x-12*x*(1-x)});
\addplot[thick,red!70!black,domain=0:1,samples=40] ({3*x/(1+2*x)},{100-35*x-12*x*(1-x)});
\node[font=\tiny,red!70!black] at (axis cs:0.62,96) {露点曲線（気相線）};
\node[font=\tiny,blue!70!black] at (axis cs:0.35,68) {沸点曲線（液相線）};
\end{axis}
\begin{axis}[at={(txy.east)},anchor=west,xshift=8mm,width=5.2cm,height=4.6cm,xmin=0,xmax=1,ymin=0,ymax=1,
  xlabel={$x$},ylabel={$y$},xtick={0,1},ytick={0,1},
  every axis label/.style={font=\scriptsize},tick label style={font=\tiny},title={\scriptsize McCabe-Thiele},title style={yshift=-4pt}]
\addplot[thin,gray,domain=0:1] {x};
\addplot[thick,black,domain=0:1,samples=40] {3*x/(1+2*x)};
\addplot[thick,blue!70!black] coordinates {(0.9,0.9)(0.5,0.6333)};
\addplot[thick,red!70!black] coordinates {(0.5,0.6333)(0.08,0.08)};
\node[font=\tiny,anchor=west] at (axis cs:0.30,0.80) {平衡曲線};
\node[font=\tiny,blue!70!black,anchor=north west] at (axis cs:0.58,0.66) {濃縮部操作線};
\node[font=\tiny,red!70!black,anchor=north west] at (axis cs:0.22,0.24) {回収部};
\end{axis}
\end{tikzpicture}
```

- T-x-y上露點氣相線、下泡點液相線；以低沸成分為基準，氣相較富該成分，x-y曲線在對角線上。P-x圖的上下不能照搬（H24-Q26）。
- 槓桿定則：**靠近哪個端點，該相就較多**；兩相量比取對側線段。包晶型分解熔融生成另一固相＋液相，不能當成只在固態分解，也不宜用單純熔體法長晶。

## 5.2 反応速度・反応器（反應器） {S131 T101 S254 S292 S220 S023 S066}

| | 0 次 | 1 次 | 2 次 |
|---|---|---|---|
| 積分形 | C₀ − C ＝ kt | ln(C₀/C) ＝ kt | 1/C − 1/C₀ ＝ kt |
| 転化率（轉化率）表示 | x ＝ kt/C₀ | −ln(1−x) ＝ kt | x/(1−x) ＝ kC₀t |
| 直線化 | C vs t | ln C vs t | 1/C vs t |
| 半減期 | C₀/2k（逐步縮短） | ln2/k（一定） | 1/kC₀（伸びる） |
| k の単位 | mol/(m³·s) | s⁻¹ | m³/(mol·s) |

同一系統若1小時達50%，從起點達75%的時間：零級1.5 h、一級2 h、二級3 h。放射（輻射）衰變一級：t＝t½×log(N₀/N)/log2。

- **アレニウス（阿瑞尼斯）**：k＝A exp(−Ea/RT)；ln(k₂/k₁)＝(Ea/R)(1/T₁−1/T₂)。Ea80.1 kJ/mol、50→100 ℃，指數約4，倍率e⁴≈55。別以「每10 ℃兩倍」代替；K與kJ→J兩項都換。
- 速率級數不能直接抄總反應係數。中間體以d[I]/dt≈0處理；R7-Q35慢步A＋B→C′、快步2B＋C′→2C，得d[C]/dt＝2k₂[A][B]，對B是一級。
- **ミカエリス・メンテン（米氏方程）** r＝VmC/(Km＋C)。C≪Km近一級，C≫Km酵素飽和近零級，C＝Km時r＝Vm/2；Km較小表示較高親和性。

```tikz
\begin{tikzpicture}
\begin{axis}[name=lev,width=5.2cm,height=4.6cm,xmin=0,xmax=1,ymin=0,ymax=6,
  xlabel={転化率 $X$},ylabel={$1/(-r_A)$},xtick={0,0.8},ytick=\empty,
  every axis label/.style={font=\scriptsize},tick label style={font=\tiny},title={\scriptsize Levenspiel プロット},title style={yshift=-4pt}]
\addplot[fill=blue!15,draw=none,domain=0:0.8,samples=40] {1/(1-x)} \closedcycle;
\addplot[thick,black,domain=0:0.83,samples=40] {1/(1-x)};
\draw[thick,dashed,red!70!black] (axis cs:0,0) rectangle (axis cs:0.8,5);
\node[font=\tiny,blue!70!black] at (axis cs:0.40,0.7) {PFR ＝ 曲線下面積};
\node[font=\tiny,red!70!black] at (axis cs:0.40,4.5) {CSTR ＝ 長方形};
\end{axis}
\begin{axis}[at={(lev.east)},anchor=west,xshift=8mm,width=5.2cm,height=4.6cm,xmin=0,xmax=10,ymin=0,ymax=1.15,
  xlabel={基質濃度 $C_S$},ylabel={$r$},xtick={1},xticklabels={$K_m$},ytick={0.5,1},yticklabels={$V_m/2$,$V_m$},
  every axis label/.style={font=\scriptsize},tick label style={font=\tiny},title={\scriptsize ミカエリス・メンテン},title style={yshift=-4pt}]
\addplot[thick,black,domain=0:10,samples=60] {x/(1+x)};
\addplot[thin,dashed,gray,domain=0:10] {1};
\draw[thin,dotted] (axis cs:1,0)--(axis cs:1,0.5)--(axis cs:0,0.5);
\node[font=\tiny,anchor=west] at (axis cs:3.5,0.62) {0 次（飽和）};
\node[font=\tiny,anchor=west] at (axis cs:0.15,0.20) {1 次};
\end{axis}
\end{tikzpicture}
```

### 反応器の選択 {S220 S023}

| 反応器 | 設計式 | 性格 |
|---|---|---|
| 回分（批次） | t ＝ C_A0∫dX/(−r_A) | — |
| 管型（管式） PFR | V ＝ F_A0∫dX/(−r_A) | 沿程有濃度梯度，入口放熱集中、較難除熱 |
| 槽型（槽式） CSTR | V ＝ F_A0 X/(−r_A)_出口 | 全槽等於出口濃度，易控溫 |

- 正級數反應通常V_PFR＜V_CSTR；CSTR全槽按較慢出口濃度運作。一級、X＝0.9：kτ為2.30對9.0，體積比約3.9。多槽串聯可逼近PFR。
- Levenspiel圖1/(−r)上升選PFR，下降選CSTR；自催化U形可先CSTR至最低點，再接PFR，按面積比較。

## 5.3 流体 {S095 S101 S062 S030 S291 S222 S097 T100 S031 S028}

| 式 | 内容 | 注意 |
|---|---|---|
| Re ＝ ρuD/μ | 層流 ＜ 2100〜2300、乱流（紊流） ＞ 4000 | 特徵長度取管徑 |
| ΔP ＝ 4f(L/D)(ρu²/2) | ファニング（范寧）（層流 f ＝ 16/Re） | ダルシー（達西） λ ＝ 4f ＝ 64/Re；先確認摩擦因子定義 |
| ΔP ＝ 32μLu/D² | ハーゲン・ポアズイユ（哈根–泊肅葉）（僅圓管層流） | 范寧式的層流特例；ΔP ∝ u¹（乱流は ∝ u²） |
| ρ₁u₁A₁ ＝ ρ₂u₂A₂ | 連續方程、質量守恆 | Q ＝ u·πD²/4（直径！） |
| P ＋ ρu²/2 ＋ ρgz ＝ 一定 | ベルヌーイ（伯努利）（能量守恆） | τ＝μdu/dy為牛頓黏性定律，不是伯努利式 |
| u ＝ √(2gH) | トリチェリ（托里拆利） | 含損失時更慢，可作上限驗算 |
| u_t ＝ (ρ_p − ρ)g d_p²/18μ | ストークス（斯托克斯）（Re_p ＜ 1） | 粒徑平方、密度取差；遠心では g → rω² |

> [!trap] トリチェリの基準点（H26-Q30 ＝ H28-Q35、同じ罠で二回出題）
> H從**液面量至噴嘴**。噴嘴離底0.1 m，液深＝H＋0.1。依Q＝V/t、A＝πd²/4、u＝Q/A、H＝u²/2g，最後修基準。別把直徑當半徑；槽尺寸與密度在此可能不需用。

- 橫流沉澱池ハーゼン（哈曾）框架：E＝ut/(Q/A)，由表面負荷率控制，**不按深度**（R3-Q34）。
- 攪拌P＝Npρn³d⁵，同裝置P∝n³。泵相似律Q∝n、H∝n²、P∝n³。放大n∝dᵃ：Re固定a=−2、尖端速固定−1、P/V固定**−2/3**、Fr固定−1/2、轉數固定0；記得d⁵/d³=d²。
- 填充床柯澤尼–卡曼：ΔP∝μLu(1−ε)²/(dp²ε³)，空隙率稍降即大增壓損。Ergun另加高流速慣性項。
- 液中稱量分兩步：先補空氣浮力求真質量，再用浸液減重除體積求液密度，不把兩個修正混成一項。

## 5.4 伝熱（傳熱） {S094 S193 S223 S063 S133 T097 S099 S032 S064 S065}

| 形式 | 法則 | 温度依存 |
|---|---|---|
| 伝導（傳導） | フーリエ（傅立葉） q ＝ −λ dT/dx | ΔT の 1 乗 |
| 対流（對流） | ニュートン（牛頓）の冷却則 q ＝ h(T − T_s) | ΔT の 1 乗 |
| 放射（輻射） | Q ＝ εFAσ(T₁⁴ − T₂⁴) | ==T の 4 乗==；真空仍可傳熱 |

輻射另取決於放射率ε、面積、形態因子F；ε等於吸收率（克希荷夫），黑體1、拋光金屬較低。

### 熱抵抗（熱阻）の直列（R3-Q35・R7-Q34 失分） {S193 S223 S063}

1/U＝1/h₁＋L/λ＋1/h₂，為每單位面積的熱阻和；q＝ΔT/ΣR，各層降溫與該層熱阻成比例。

- **最大熱阻承擔最大溫降**，常是氣膜。皮膚例R皮=0.004/0.21≈0.019、R氣=1/8.8≈0.114，約1:6；7.5 K中皮膚約1.07 K，T₁≈35.4 ℃。
- 上限檢查：只留最大熱阻所得熱流，比全熱阻答案大。
- 求溫差時小項可能重要，不早捨去；中間溫度由已知端沿各層熱阻計回。
- h量級W/(m²K)：氣體自然對流5〜25，液體強制500〜10⁴，沸騰／凝結10³〜10⁵。膜厚δ變薄使h≈λ/δ提高。

### 熱交換器（H27-Q30・H29-Q33） {S133 T097 S032 S099 S064 S065}

熱交換器順序：①以資料齊的一側Q＝ṁcpΔT；凝結蒸氣改用ṁ×潛熱。②熱收支求另一出口。③畫逆流／並流查兩端ΔT。④A＝Q/(UΔTlm)，L＝A/(πd)。

ΔTlm＝(ΔT₁−ΔT₂)/ln(ΔT₁/ΔT₂)。水2.8 kg/s、30→80 ℃、蒸氣130 ℃：Q≈5.85×10⁵ W，ΔTlm＝50/ln2≈72.5 K，U≈810 W/(m²K)。對數平均不超算術平均；兩端比＜2時算術近似誤差小於約4%。

- 逆流是高溫入口對低溫**出口**，通常平均推動力大、面積小；冷流出口可超過熱流出口溫度。
- 傳熱側面積πdL，流速才用截面πd²/4。查內／外徑基準，Uodo＝Uidi。夾套取**液深與側面**，不是總槽深。
- 最小冷卻水量按夾點極限：水出口逼近熱流**入口**溫度（H25-Q35）。
- 理想多效蒸發按各效熱負荷近等、UA相同則ΔT近等處理；溶液沸點＝加熱蒸氣對應基準加沸點升高修正，先查題目的壓力與溫差定義。
- 房間穩態熱收支：通風引熱ṁcp(T外−T室)＝冷房能力；室內循環風量不等於新風量。

## 5.5 分離・物質収支・燃焼 {S029 S100 S161 F22 S192 S134 S067 S219 S233 S221 S290 S160 S060 S162 S163 S191 S189 S128 S061 T098}

### 蒸留（蒸餾） {S029 S100 S161 F22}

- 聯立總量F＝D＋W與成分Fz＝DxD＋WxW，不能直接把分率相乘（H25-Q32）。
- 還流比（回流比）**R＝L/D**，分母是餾出量。濃縮段L＝RD、V＝(R＋1)D；回收段L′＝RD＋qF、V′＝V−(1−q)F。
- q：過冷液＞1、飽和液1、氣液混合0〜1、飽和蒸氣0、過熱蒸氣＜0。q要**乘F**。R無因次，不能直接與流量相加；q=1應回V′=V。
- 全回流R→∞給最少理論板；最小回流Rmin需無限板。筆記實務估R≈1.2〜1.5Rmin。濃縮操作線y＝R/(R＋1)x＋xD/(R＋1)。

### 抽出（萃取）・吸収（吸收）・吸着（吸附） {S192 S134 S067 S219 S233 S221 S290}

```tikz
\begin{tikzpicture}
\begin{axis}[name=tri,width=5.2cm,height=4.8cm,xmin=0,xmax=1,ymin=0,ymax=1,axis lines=left,
  xlabel={C（抽剤）分率},ylabel={A 分率},xtick={0,1},ytick={0,1},
  every axis label/.style={font=\scriptsize},tick label style={font=\tiny},title={\scriptsize 三角線図とてこの原理},title style={yshift=-4pt}]
\addplot[thin,black] coordinates {(0,1)(1,0)};
\addplot[thick,gray,smooth] coordinates {(0.04,0.0)(0.05,0.30)(0.1,0.55)(0.25,0.55)(0.4,0.15)(0.45,0.0)};
\addplot[thick,blue!70!black,mark=*,mark size=1.2pt] coordinates {(0.1,0.55)(0.3,0.2833)(0.4,0.15)};
\node[font=\tiny,anchor=south east] at (axis cs:0.1,0.55) {R（抽残相）};
\node[font=\tiny,anchor=south west] at (axis cs:0.3,0.29) {M};
\node[font=\tiny,anchor=north west] at (axis cs:0.4,0.15) {E（抽出相）};
\node[font=\tiny,align=left,anchor=west] at (axis cs:0.5,0.75) {E : R ＝ $\overline{\mathrm{MR}}$ : $\overline{\mathrm{ME}}$\\＝ 2 : 1};
\end{axis}
\begin{axis}[at={(tri.east)},anchor=west,xshift=8mm,width=5.2cm,height=4.8cm,xmin=2.6,xmax=3.6,ymin=-6,ymax=0,axis lines=left,
  xlabel={$1/T$（$10^{-3}$ K$^{-1}$）},ylabel={$\ln k$},xtick=\empty,ytick=\empty,
  every axis label/.style={font=\scriptsize},tick label style={font=\tiny},title={\scriptsize アレニウスプロット},title style={yshift=-4pt}]
\addplot[thick,black,domain=2.7:3.5] {-5*(x-2.7)-0.5};
\node[font=\tiny,anchor=west] at (axis cs:3.0,-1.2) {傾き ＝ $-E_a/R$};
\end{axis}
\end{tikzpicture}
```

- 三角圖頂點純物、邊為二元；加C沿F–C直線移動，A:B不變。槓桿mE/mR＝MR/ME，接近M的一相較多（R3-Q29應2:1，非1:2）。
- 液液平衡先查各繫線分配係數是否可視常數。相總量含溶劑與溶質，如水相莫耳分率(20−x)/(120−x)。二次式可代選項驗。甲苯／苯／己烷／醚常在上層；CH₂Cl₂／CHCl₃／CCl₄在下層。
- 吸收塔L(xB−xT)＝G(yB−yT)；Lmin時塔底液與入口氣平衡，xB*=yB/m。L=αLmin則xB=xB*/α，不能超平衡上限。
- 批次吸附V(C₀−C)＝Wq*，Freundlich q=kC^(1/n)。n=2可令y=√C解正根，再平方得C；R7-Q31為0.0084。檢查0<C<C₀及平方引入的偽根。
- CO₂化學吸收用MEA／熱碳酸鉀，加熱再生；物理吸收用甲醇／PEG，高壓吸收、減壓再生。

### 膜分離（H30-Q29） {S160 S060}

孔徑MF微濾＞UF超濾＞NF奈米濾；RO逆滲透按緻密膜溶解擴散。MF截細菌，UF蛋白／病毒，NF多價離子，RO可脫單價鹽。海水操作5〜8 MPa，π約2.5〜3 MPa；π=icRT，NaCl取i≈2。氣體多孔膜克努森擴散∝1/√M；緻密膜看溶解擴散，CO₂常快於N₂。電透析靠電位差，透析靠濃度差。

### 湿度（H30-Q34・R1再-Q32） {S163 S191}

- 相對濕度φ=pw/ps(T)，分母取氣溫的飽和壓；絕對濕度H=(18/29)pw/(P−pw)，單位kg水/kg乾空氣。未凝結前加冷熱H不變；φ到100%為露點。25 ℃、70%、ps=3.21 kPa例H≈0.0143，別漏70%。
- 濕球平衡h(T−Ts)=ΔvH·k(ps−p)；ps取濕球溫度，p為空氣水分壓；求φ時回p/p*(氣溫)。

### 燃焼計算（H29-Q28・R3-Q31/32・R7-Q30） {S189 S128 S061}

| 量 | 式 |
|---|---|
| 理論酸素（氧）量 O₀ | 燃燒式O₂係數 |
| 理論空気量 A₀ | O₀ **÷ 0.21** |
| 実際空気量 | A₀ × 空気比 m |
| 過剰 O₂ | (m − 1) × O₀ ← 容易遺漏的項 |
| N₂ | m × O₀ × 79/21 |
| 乾き燃焼ガス | CO₂ ＋ N₂ ＋ 過剰 O₂（不含H₂O） |

- 係數逐段保留：丙烷、空氣比1.2、一次空氣70%，(5/0.21)×1.2×0.70≈20.0 m³N/m³N，不能漏1.2。
- 完全燃燒指燃料燒盡，不表示氧全消耗。筆記乾煙氣近似檢查m≈21/(21−O₂%_dry)，須符合題目的燃料與近似條件。
- 甲醇理論空氣量：(1.5/0.21)×22.4/32≈5.0 m³/kg；7.14只是mol比，中途不能停。
- 斷熱火焰先按生成氣熱容量求ΔT，H₂O按蒸氣計，最後**加入口25 ℃**；用低位熱值。1666＋25約1700 ℃。
- 定容燃燒P₂=P₁(n₂/n₁)(T₂/T₁)；用100 mol基準數Δn，R與V約去。

### 晶析（結晶操作）・リサイクル（回收） {T098 S162}

> [!trap] 水和（水合）物の析出（H27-Q31 → R5-Q31 で再失分）
> CuSO₄·5H₂O析出同時帶走**無水鹽與結晶水**。設析量W，以(無水鹽−0.64W)/(水−0.36W)=S低溫/100；比例160/250與90/250。60 ℃飽和100 g、S由30降20，W約14 g。只扣鹽不扣水即失分（H27-Q31／R5-Q31）。

- 循環排放：惰性物只能由purge離開，穩態入量=排量；分流各成分同R:P比。分離器未反應量=(新料＋循環未反應量)(1−反應率)，H30-Q33例x₁≈215.4、R≈260。
- 冷凝後氣體仍含飽和水蒸氣：yw=ps/P；濕氣總量=乾氣/(1−yw)，不能視為水全除去。
