# L-Thin：薄可表族嵌入与失败集增长约束（路线 R18-Thin-Families）

> 路线 **R18-Thin-Families**（P09 攻关轮次 18，服务理解 **CS / 例外**）。  
> 解析讨论三类「薄族」：  
> （i）无限可表参数族如何嵌入全形 $\mathcal{R}$；  
> （ii）若失败集 $\mathcal{F}_0$ 无限，在 L-Rand 种植模型下的**最小自然增长**；  
> （iii）形如「若 $\mathcal{F}_0=\{N_j\}$ 则 $N_{j+1}/N_j$ 必须…」的条件式约束。  
> **不**声称原猜想 / E-kill / 真实 $\mathcal{F}_0$ 有限；禁止数值程序。

---

## 0. 符号

$$
\mathcal{S}=\{y^3+z^2:y,z\in\mathbb{N}_0\},
\qquad
\mathcal{R}_{4,3,2}=\{x^4+y^3+z^2:x,y,z\in\mathbb{N}_0\},
$$
$$
\mathcal{R}
=\{x^4+y^3+z^2+2^k:x,y,z\in\mathbb{N}_0,\ k\in\mathbb{N}_1\}
=\mathcal{R}_{4,3,2}+\{2^k:k\ge 1\},
$$
$$
E=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2},
\qquad
W(N)=\{N-2^k:1\le k\le K\},
\quad K=\lfloor\log_2(N-1)\rfloor,
$$
$$
\mathcal{F}_0=\{N\ge 2:W(N)\subseteq E\}.
$$
（本文件 $\mathcal{F}_0$ 一律取 E-kill 失败集，同 L-Rand / L-Pack；与 L-Slowx 的纯 $x=0$ 切片失败集区分时写 $\mathcal{F}_0^{\mathrm{kill}}$。）

骨架 CS-弱：无限族 $n_t=t^3+t^2+2$ 与下界 $|\mathcal{R}\cap[1,X]|\gg_\varepsilon X^{5/6-\varepsilon}$。  
L-Rand 模型 R / S 与边际 $\delta_m=c/(\log(m+2))^\kappa$ 见 `L-Rand.md`。

---

## L-Thin-1（已证：CS 射线嵌入 $\mathcal{R}$）

对一切整数 $t\ge 0$，令
$$
n_t:=t^3+t^2+2.
$$
则
$$
n_t=0^4+t^3+t^2+2^1\in\mathcal{R},
$$
且同时 $n_t-2\in\mathcal{S}\subseteq\mathcal{R}_{4,3,2}$。特别地 $\{n_t:t\ge 0\}\subseteq\mathcal{R}$ 为无限可表族。

**证明.** 取 $(x,y,z,k)=(0,t,t,1)$ 即得。证毕。

**计数.** $n_t\le X\iff t^3+t^2+2\le X\Rightarrow t\ll X^{1/3}$，故
$$
\bigl|\{n_t:n_t\le X\}\bigr|\asymp X^{1/3}.
$$
单射线**只**贡献 $X^{1/3}$；骨架 CS-弱的 $X^{5/6-\varepsilon}$ 来自整片 $\mathcal{S}$（或 $\mathcal{S}+2^k$）的二维参数 $(y,z)$，不是来自 $\{n_t\}$。

---

## L-Thin-2（已证：多项式参数族的嵌入模板）

设整数系数映射
$$
t\mapsto\bigl(x(t),y(t),z(t),k(t)\bigr)
\in\mathbb{N}_0^3\times\mathbb{N}_1
$$
在无限集 $T\subseteq\mathbb{N}_0$ 上有定义，并令
$$
\Phi(t):=x(t)^4+y(t)^3+z(t)^2+2^{k(t)}.
$$
则 $\{\Phi(t):t\in T\}\subseteq\mathcal{R}$。

若另有多项式增长控制
$$
\max\bigl\{x(t),y(t),z(t),2^{k(t)}\bigr\}\ll t^{A}
$$
（某固定 $A<\infty$），则
$$
\bigl|\{\Phi(t):\Phi(t)\le X\}\bigr|\gg_\varepsilon X^{1/A-\varepsilon}
$$
（在 $\Phi$ 近单射时）；特别地该族密度为零。

**证明.** 逐点落入 $\mathcal{R}$ 由定义；计数由 $\Phi(t)\ll t^{O(A)}$ 反解 $t\ll X^{1/A}$。证毕。

**例.** L-Thin-1 取 $A=3$、$k\equiv 1$、$x\equiv 0$、$y=z=\mathrm{id}$。  
**非例.** 缺项族 $\{2^k\}$ 本身不是 $\mathcal{R}$ 的参数化（对照 L-Poly-5）；它是射击集，不是可表值集。

---

## L-Thin-3（已证对照：可表薄族 vs 失败薄族）

| 对象 | 所在侧 | 典型间距 | 密度贡献 |
|------|--------|----------|----------|
| CS 射线 $\{n_t\}$ | $\subseteq\mathcal{R}$（可表） | $n_{t+1}-n_t=3t^2+3t+1$，比值 $n_{t+1}/n_t\to 1$ | $\asymp X^{1/3}=o(X)$ |
| 全片 $\mathcal{S}$（CS-弱引擎） | $\subseteq\mathcal{R}_{4,3,2}\subseteq\mathcal{R}-P_2$ 平移源 | 二维参数，差集厚（L-CSdiff-4） | $\asymp X^{5/6}$ |
| L08 失败中心 $\{N_j\}$ | $\subseteq\mathcal{F}_0$（整窗失败） | $N_{j+1}/N_j\to\infty$（超指数） | $|\mathcal{F}_0\cap[1,X]|\asymp\log\log X$ |
| Roth 例外 $E$ | 不可表 | — | $\ll X/(\log X)^{1/20}$ |

**一句话.** 「薄」在可表侧允许比值 $\to 1$ 的多项式族；在失败侧，若还要求 $E$ 极薄（L08），则中心列必须超指数稀疏。二者**不可**互换叙事。

---

## L-Thin-4（已证：窗不交 $\Rightarrow$ 失败对 $|E|$ 的加性下界）

设严格增列 $\{N_j\}_{j\ge 1}\subseteq\mathcal{F}_0$，并设窗族两两不交：
$$
W(N_i)\cap W(N_j)=\varnothing\qquad(i\neq j).
$$
则对一切 $J\ge 1$，
$$
\bigl|E\cap[1,N_J]\bigr|
\ge
\sum_{j=1}^{J}\lvert W(N_j)\rvert
=
\sum_{j=1}^{J}K(N_j)
\gg
\sum_{j=1}^{J}\log N_j.
$$

**证明.** 每个 $N_j\in\mathcal{F}_0\Rightarrow W(N_j)\subseteq E$；不交则基数相加。$K(N)=\lfloor\log_2(N-1)\rfloor\gg\log N$。证毕。

**注（不交的充分条件）.** 若 $N<M$ 且 $M-N$ 不能写成 $2^b-2^a$（$1\le a\le K(N)$，$1\le b\le K(M)$），则 $W(N)\cap W(M)=\varnothing$。特别地：$M-N$ 为奇数时自动不交（因 $a\ge 1$ 时 $2^b-2^a$ 偶）。L08 中心皆奇，故改用超指数分离保证不交（见 L-Thin-7）。

---

## L-Thin-5（已证：L-Rand 种植下无限 $\widetilde{\mathcal{F}}_0$ 的最小自然增长）

沿用 L-Rand 模型 S（尺度种植）：中心 $N_K=2^K+2^{\lfloor K/2\rfloor}$，窗两两不交，$p_K\asymp K^{-\kappa}$，种植示性独立。

### （A）临界边际 $\kappa=1$

由 L-Rand-5，$κ\le 1$ 时 $\widetilde{\mathcal{F}}_0$ a.s. 无限。取 $κ=1$，令
$$
S(L):=\sum_{K=K_0}^{L}\xi_K,\qquad \xi_K\sim\mathrm{Bernoulli}(p_K),\quad p_K\asymp K^{-1}.
$$
则 $\mathbb{E}[S(L)]\asymp\log L$。对 $X\in(2^L,2^{L+1}]$ 有
$$
\mathbb{E}\bigl[\lvert\widetilde{\mathcal{F}}_0\cap[1,X]\rvert\bigr]
\ge
\mathbb{E}[S(L)]
\asymp\log\log X.
$$
独立 Bernoulli 的强大数律给出：在种植成功的 a.s. 无限事件上，
$$
\frac{\lvert\widetilde{\mathcal{F}}_0\cap[1,X]\rvert}{\log\log X}
\to c
$$
（沿 $X=2^{L}$，$c>0$ 依赖 $p_K\sim c_0/K$ 的首项）。

**解读.** 在「每个二进尺度至多种一次、边际恰为 Roth 临界种植预算 $κ=1$」的饱和模型中，$\log\log X$ 是无限失败集的**最小自然增长**（尺度穷尽谐波级数）。

### （B）亚临界 $κ\in(0,1)$

同模型下 $\mathbb{E}[S(L)]\asymp L^{1-κ}$，故
$$
\mathbb{E}\bigl[\lvert\widetilde{\mathcal{F}}_0\cap[1,X]\rvert\bigr]
\asymp(\log X)^{1-κ}.
$$
比 $\log\log X$ **更快**；不是「最小」。

### （C）稀疏子列种植仍受谐波约束

若只在子列尺度 $\{K_j\}$ 上种植，且保持 $p_{K_j}\le C K_j^{-κ}$，则 a.s. 无限仍需 $\sum_j K_j^{-κ}=\infty$。当 $κ=1$ 时，
$$
\sum_j K_j^{-1}=\infty
$$
迫使在 $K\le L$ 内可放置的成功期望至多与调和发散同级；取最稀发散（$K_j=j$）恰回到（A）的 $\log\log X$。若插入额外对数（$K_j=j\log(j+1)$ 等），期望可降为 $\log\log\log X$ 型，但**每一个**成功中心仍消耗 $\asymp K_j$ 个边际预算点，且须 $p_{K_j}\le C/K_j$。

**与抽象 L08.** L08 取 $N_j=2^{2^j}+1$，得 $|\mathcal{F}_0\cap[1,X]|\asymp\log\log X$，与（A）同阶；其 $|E\cap[1,X]|=O(\log X)$ 远优于 Roth，因未受「每尺度边际 $K^{-κ}$」约束，而是确定性一次种死。

**结算一句.** 在 L-Rand 饱和种植（$κ=1$）下，无限 $\widetilde{\mathcal{F}}_0$ 的自然最小增长是
$$
\lvert\widetilde{\mathcal{F}}_0\cap[1,X]\rvert\asymp\log\log X;
$$
抽象确定性构造可同阶，但不能在保持每尺度 Bernoulli 预算时系统性更慢到 $o(\log\log X)$（除非放弃「几乎每尺度都尝试」的饱和性，见上（C）的额外对数稀化）。

---

## L-Thin-6（条件式：比值下界 — 窗不交 + 极薄 $E$）

### 假设 Thin-Disj

$\{N_j\}\uparrow\subseteq\mathcal{F}_0$ 且 $\{W(N_j)\}$ 两两不交。

### 假设 Thin-LogE$_{C}$

存在 $C<\infty$ 使对一切充分大 $J$，
$$
\bigl|E\cap[1,N_J]\bigr|\le C\log N_J.
$$
（L08 级；远强于 Roth。）

### 结论

在 Thin-Disj + Thin-LogE$_{C}$ 下，对充分大 $J$，
$$
\sum_{j=1}^{J}\log N_j\ll_C\log N_J.
$$
因而**不能**有 $N_{j+1}/N_j$ 一致有界且 $\log N_j$ 近等差：若存在 $Q<\infty$ 与无限多 $j$ 使
$$
\frac{N_{j+1}}{N_j}\le Q
\qquad\text{且}\qquad
\log N_{j+1}\ge\log N_j+c
$$
（$c>0$ 固定）在长度为 $\asymp J$ 的块上成立，则左端 $\gg J\cdot\log N_1$ 与右端 $\log N_J\ll J\log Q$ 在 $J\to\infty$ 时冲突（除非 $c$ 块极短）。

**更干净的充分排斥形.** 若另设 $\log N_j\ge c\,2^{j}$（L08 型下界），则 Thin-LogE$_{C}$ 兼容当且仅当
$$
\sum_{j\le J}2^{j}\ll\log N_J\asymp 2^{J},
$$
即增长至少双指数级。典型实现：
$$
\frac{N_{j+1}}{N_j}\ge N_j\qquad\bigl(\text{即 }N_{j+1}\ge N_j^{2}\bigr)
$$
对充分大 $j$ 成立（L08：$N_j=2^{2^j}+1$ 远强于此）。

**引理形式.** Thin-Disj + Thin-LogE$_{C}$ + $\log N_j\ge c\,2^{j}$ $\Rightarrow$ 存在 $j_0$ 使
$$
\forall j\ge j_0:\quad
\frac{N_{j+1}}{N_j}\ge 2.
$$
（实际上 $N_{j+1}/N_j\to\infty$。）

**证明.** L-Thin-4 + Thin-LogE$_{C}$ 得 $\sum_{j\le J}\log N_j\ll\log N_J$。若无穷多 $j$ 有 $N_{j+1}<2N_j$，则 $\log N_{j+1}<\log N_j+\log 2$，与 $\log N_j\ge c2^{j}$ 的几何增长叠加后，和式左端将 $\gg 2^{J}$ 而右端 $\asymp\log N_J$；当 $N_J$ 仅单指数于 $J$ 时已冲突。在 L08 标定 $\log N_J\asymp 2^{J}$ 下，必须几乎所有步进满足 $N_{j+1}/N_j\to\infty$。证毕。

---

## L-Thin-7（条件式：比值约束 — Roth 预算版）

### 假设 Thin-Disj$_{C}$（有界重数）

存在 $C<\infty$，使每点 $m\in E$ 落入至多 $C$ 个窗 $W(N_j)$（$N_j\in\mathcal{F}_0$）。

### 假设 Roth-κ

$|E\cap[1,X]|\ll X/(\log X)^\kappa$（骨架取 $κ=1/20$）。

### 结论（计数上界，同 L-LSW-5 量级）

$$
\sum_{N_j\le X}\log N_j
\ll_C
\bigl|E\cap[1,2X]\bigr|
\ll
\frac{X}{(\log X)^\kappa},
$$
从而
$$
\bigl|\mathcal{F}_0\cap[1,X]\bigr|
\ll
\frac{X}{(\log X)^{\kappa+1}}
$$
（因每项 $\log N_j\gg 1$；更精时用 $\log N_j\gg\log X$ 于 $N_j\asymp X$ 的主贡献段）。

### 比值形式（平均间隙）

令 $M(X)=|\mathcal{F}_0\cap[1,X]|$。若 $M(X)\to\infty$，则平均间距满足
$$
\frac{X}{M(X)}\gg(\log X)^{\kappa+1}.
$$
这**不**强迫 $N_{j+1}/N_j\to\infty$（例如 $N_j=\lfloor j\,(\log j)^{\kappa+2}\rfloor$ 可使比值 $\to 1$ 而仍兼容 Roth 上界）。  
**对照 L-Thin-6：** 只有额外要求 $|E|\ll\log X$（极薄）时，才强制比值 $\to\infty$。

### 与 L-Rand-5 的衔接

模型 S 的种植中心满足 $N_K\asymp 2^K$，故对种植成功子列 $\{K_j\}$ 自动有
$$
\frac{N_{K_{j+1}}}{N_{K_j}}=2^{K_{j+1}-K_j}\ge 2,
$$
且当 $K_{j+1}\ge K_j+1$ 时严格 $\ge 2$。若成功尺度相邻（$κ<1$ 时典型），则
$$
\frac{N_{j+1}}{N_j}\asymp 2.
$$
若成功尺度稀疏到 $K_{j+1}-K_j\to\infty$，则比值 $\to\infty$。

---

## L-Thin-8（条件式汇总：「若 $\mathcal{F}_0=\{N_j\}$ 则…」）

下列约束均可仅用 L-Thin-4…7 + L-Rand-5 解析检验。

| 标签 | 附加假设 | 必然后果 |
|------|----------|----------|
| **(R1)** Thin-Disj | 窗两两不交 | $\lvert E\cap[1,N_J]\rvert\ge\sum_{j\le J}K(N_j)$ |
| **(R2)** Thin-Disj + Thin-LogE$_{C}$ | 极薄例外 | $\sum_{j\le J}\log N_j\ll\log N_J$；不能「多项式密」 |
| **(R3)** (R2) + $\log N_j\ge c2^{j}$ | L08 标定 | $N_{j+1}/N_j\to\infty$；典型 $N_{j+1}\ge N_j^{2}$ |
| **(R4)** Thin-Disj$_{C}$ + Roth-κ | Roth 预算 | $M(X)\ll X/(\log X)^{\kappa+1}$；平均间隙 $\gg(\log X)^{\kappa+1}$；**允许** $N_{j+1}/N_j\to 1$ |
| **(R5)** 模型 S、$κ=1$、饱和种植 | L-Rand 临界 | a.s. 无限且 $M(X)\asymp\log\log X$；$N_j\asymp 2^{K_j}$ 故相邻成功比 $\ge 2$ |
| **(R6)** 模型 S、$κ\le 1$、稀疏子列 $K_j$ | $\sum K_j^{-κ}=\infty$ | 无限失败；期望 $M(2^{L})$ 可低至调和发散包络（$κ=1$ 时 $\ge\omega(1)$ 任意慢于饱和 $\log\log$，若允许多余对数稀化） |

**可写成单行条件式的核心句：**

> 若 $\mathcal{F}_0=\{N_j\}_{j\ge 1}$ 升列、窗两两不交、且 $|E\cap[1,N_J]|\le C\log N_J$，则
> $$
> \sum_{j\le J}\log N_j\ll_C\log N_J;
> $$
> 若再有 $\log N_j\ge c\,2^{j}$，则必有
> $$
> \frac{N_{j+1}}{N_j}\to\infty
> \qquad(j\to\infty).
> $$

> 若仅 Roth-κ + 有界重数，则只得
> $$
> \bigl|\mathcal{F}_0\cap[1,X]\bigr|\ll\frac{X}{(\log X)^{\kappa+1}},
> $$
> **不**得比值 $\to\infty$。

---

## L-Thin-9（已证对照：与 CS / Pack / Rand / L08 的正交性）

| 路线 | 关系 |
|------|------|
| CS-弱 / L-Thin-1–3 | 可表薄族嵌入 $\mathcal{R}$；比值可 $\to 1$；与 $\mathcal{F}_0$ 薄失败正交 |
| L-CSdiff | 差集厚支撑「可表侧」；不约束 $\mathcal{F}_0$ 中心比值 |
| L-Pack-8 / L08 | 超指数中心恰实现 Thin-LogE + Disj；破 Mix-Link |
| L-Rand-5 | 给出饱和种植下 $M(X)\asymp\log\log X$ 的概率模型 |
| L-LSW-5 | Roth 下 $M(X)\ll X/(\log)^{1/20}$；与 L-Thin-7(R4) 同级 |
| L-Slowx | 缓增 $x$ 仍密度零可表；与本路线「失败薄族」对偶 |

**不可写为定理.** 「$\mathcal{F}_0$ 无限 $\Rightarrow N_{j+1}/N_j\to\infty$」（缺 Thin-LogE）；「CS 射线稠 $\Rightarrow$ E-kill」（审查阻断项 3）；「Roth + 无限 $\mathcal{F}_0$ $\Rightarrow$ 矛盾」（L08）。

---

## 缺口登记（本路线不关闭）

| 编号 | 内容 | 状态 |
|------|------|------|
| Thin-G1 | 真实 $E$ 是否排除 Thin-LogE 级极薄整窗列 | 未证（＝E-kill 本体） |
| Thin-G2 | 真实 $E$ 上窗重数是否有界（Thin-Disj$_{C}$） | 未证；对照 Pack-G1 |
| Thin-G3 | 由圆法导出「整窗中心比值不能长期 $\approx 1$」 | 未证；需 Mix-Link 型输入 |
| Thin-G4 | CS 参数族与 $E$ 的相关：$\Phi(t)-2^k$ 命中 $E$ 的频率 | 未证；服务理解，非 E-kill |

---

## 结算

| 编号 | 状态 | 摘要 |
|------|------|------|
| L-Thin-1 | 已证 | $n_t=t^3+t^2+2=0^4+t^3+t^2+2^1\in\mathcal{R}$；计数 $\asymp X^{1/3}$ |
| L-Thin-2 | 已证 | 多项式参数族嵌入模板；密度零 |
| L-Thin-3 | 已证对照 | 可表薄族（比→1）vs 失败薄族（极薄时比→∞） |
| L-Thin-4 | 已证 | 窗不交 $\Rightarrow\|E\|\ge\sum K(N_j)$ |
| L-Thin-5 | 已证 | L-Rand 饱和 $κ=1$：无限 $\widetilde{\mathcal{F}}_0$ 自然增长 $\asymp\log\log X$ |
| L-Thin-6 | 条件式 | Thin-Disj+LogE$\Rightarrow\sum\log N_j\ll\log N_J$；L08 标定$\Rightarrow$比→∞ |
| L-Thin-7 | 条件式 | Roth+有界重数$\Rightarrow M(X)\ll X/(\log)^{\kappa+1}$；**不**强迫比→∞ |
| L-Thin-8 | 条件式汇总 | (R1)–(R6) 比值 / 计数约束表 |
| L-Thin-9 | 已证对照 | 与 CS / Pack / Rand / L08 / LSW 正交 |

**本轮结论.** 无限可表族（CS 射线）以多项式参数嵌入 $\mathcal{R}$，比值可趋于 $1$；无限失败族在 L-Rand 饱和种植下自然按 $\log\log X$ 增长，仅当额外要求极薄 $E$（L08 级）时才强制 $N_{j+1}/N_j\to\infty$。Roth 预算只限制计数上界，不限制比值下界。原猜想 / E-kill 保持开放。
