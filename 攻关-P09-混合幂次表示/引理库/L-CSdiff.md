# L-CSdiff：立方–平方差集结构与 $\Delta_K$ 吞噬接口

> 路线 **R15-CS-Difference-Structure**（P09 攻关轮次 15，服务 **P1 = E-kill-1**）。  
> 研究对象是立方–平方切片差集
> $$
> \mathcal{S}-\mathcal{S}
> =\bigl\{(y^3+z^2)-(y'^3+z'^2):y,z,y',z'\in\mathbb{N}_0\bigr\},
> $$
> 以及它与全形差集 $\mathcal{R}-\mathcal{R}$、例外差集 $E-E$、半窗二进差族 $\Delta_K$ 的包含 / 密度关系。  
> 动机：整窗迫使许多 $2^a-2^b$ 落入 $E-E$（L-Diff-3）；而 $E$ 的补是
> $$
> \mathcal{R}_{4,3,2}=\bigcup_{x\ge 0}\bigl(x^4+\mathcal{S}\bigr).
> $$
> 若「大多数」$\Delta_K$ 差分已属于 $\mathcal{S}-\mathcal{S}$（乃至 $\mathcal{R}-\mathcal{R}$），则真实 $E$ 要整窗吞噬 $\Delta_K$ 必须同时承载厚的立方–平方差结构——这给出条件式 E-kill 接口。  
> **不**声称原猜想 / $\mathcal{F}_0$ 有限已证。禁止数值程序。

---

## 0. 符号

沿用
$$
\mathcal{S}=\{y^3+z^2:y,z\in\mathbb{N}_0\},
\qquad
\mathcal{R}_{4,3,2}=\{x^4+y^3+z^2:x,y,z\in\mathbb{N}_0\}
=\bigcup_{x\ge 0}(x^4+\mathcal{S}),
$$
$$
E=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2},
\qquad
W(N)=\{N-2^k:1\le k\le K\},\quad K=\lfloor\log_2(N-1)\rfloor,
\qquad
\mathcal{F}_0=\{N\ge 2:W(N)\subseteq E\}.
$$
差集
$$
\mathcal{S}-\mathcal{S}
=\{s-s':s,s'\in\mathcal{S}\},
\qquad
\mathcal{R}-\mathcal{R}
=\{r-r':r,r'\in\mathcal{R}_{4,3,2}\},
\qquad
E-E=\{e-e':e,e'\in E\}.
$$
平方差切片（取 $y=y'=0$）
$$
\square-\square=\{z^2-z'^2:z,z'\in\mathbb{N}_0\}.
$$
半窗指数集与二进差族（同 L-AE / L-Diff）
$$
A_K=\bigl\{a:\lceil K/2\rceil\le a\le K\bigr\},\qquad
M_K=|A_K|,
$$
$$
\Delta_K=\{2^b-2^a:a,b\in A_K,\ a<b\}
=\{D(a,b-a):a,b\in A_K,\ a<b\},
$$
其中 $D(\alpha,\beta)=2^\alpha(2^\beta-1)$。表示函数
$$
r_{\mathcal{S}}(\delta)=\#\{(s,s')\in\mathcal{S}^2:s-s'=\delta\},
\qquad
r_{\square}(\delta)=\#\{(z,z')\in\mathbb{N}_0^2:z^2-z'^2=\delta\}.
$$
（下文「落入」按集合计；$|\Delta_K|=\binom{M_K}{2}$ 与有序对一一对应。）

---

## L-CSdiff-1（已证：分解与包含）

**定理.**
$$
\mathcal{S}-\mathcal{S}\subseteq\mathcal{R}-\mathcal{R},
$$
且
$$
\mathcal{R}-\mathcal{R}
=\bigl\{x^4-{x'}^4:x,x'\in\mathbb{N}_0\bigr\}+(\mathcal{S}-\mathcal{S}).
$$
更细地：每个 $d\in\mathcal{R}-\mathcal{R}$ 可写成
$$
d=(x^4-{x'}^4)+(s-s'),
\qquad s,s'\in\mathcal{S}.
$$

**证明.** 取 $x=x'=0$ 得 $\mathcal{S}\subseteq\mathcal{R}_{4,3,2}$，故 $\mathcal{S}-\mathcal{S}\subseteq\mathcal{R}-\mathcal{R}$。  
反之，任意 $r=x^4+s$、$r'={x'}^4+s'$（$s,s'\in\mathcal{S}$）给出
$$
r-r'=(x^4-{x'}^4)+(s-s').
$$
证毕。

**解读.** 全形差集是「四次平移」与立方–平方差的 Minkowski 和；研究 $\mathcal{S}-\mathcal{S}$ 是 $\mathcal{R}-\mathcal{R}$ 的**核心纤维**。

---

## L-CSdiff-2（已证：平方切片刻画）

**定理.**
$$
\square-\square\subseteq\mathcal{S}-\mathcal{S},
$$
且对一切整数 $n$，
$$
n\in\square-\square
\iff
n\not\equiv 2\pmod{4}.
$$
特别地，当 $n\equiv 0\pmod{4}$ 时有显式表示
$$
n=\Bigl(\tfrac{n}{4}+1\Bigr)^2-\Bigl(\tfrac{n}{4}-1\Bigr)^2
$$
（右端两平方非负当且仅当 $|n|\ge 4$ 或 $n=0$；对 $n=\pm 4$ 取 $(2,0)$ 等）。

**证明.** 取 $y=y'=0$ 得 $\square-\square\subseteq\mathcal{S}-\mathcal{S}$。  
若 $n=z^2-z'^2=(z-z')(z+z')$，则 $z,z'$ 同奇偶（否则 $n$ 奇且因子一奇一偶，矛盾于同奇偶乘积），故 $z-z'$ 与 $z+z'$ 同为偶数或同为奇数；若同奇则 $n$ 奇；若同偶则 $n\equiv 0\pmod{4}$。故 $n\not\equiv 2\pmod{4}$。  

反之：若 $n$ 奇，取 $z-z'=1$、$z+z'=n$，得 $z=(n+1)/2$、$z'=(n-1)/2$（非负当 $n\ge 1$；负 $n$ 互换）。若 $n\equiv 0\pmod{4}$，$n\neq 0$，取
$$
z-z'=2,\qquad z+z'=n/2
$$
（二者同偶），得 $z=n/4+1$、$z'=n/4-1$（$|n|\ge 4$ 时非负）。$n=0$ 取 $z=z'$。证毕。

---

## L-CSdiff-3（已证：半窗 $\Delta_K$ 整落入 $\mathcal{S}-\mathcal{S}$）

**定理.** 设 $K\ge 4$。则
$$
\Delta_K\subseteq\square-\square\subseteq\mathcal{S}-\mathcal{S}\subseteq\mathcal{R}-\mathcal{R}.
$$
即：半窗内**每一个**二进差分 $2^b-2^a$（$a,b\in A_K$，$a<b$）都是立方–平方差，且已是平方差。

**证明.** 对 $a,b\in A_K$、$a<b$，
$$
\delta=2^b-2^a=2^a(2^{b-a}-1).
$$
因 $a\ge\lceil K/2\rceil\ge 2$（$K\ge 4$），有 $\delta\equiv 0\pmod{4}$。由 L-CSdiff-2，$\delta\in\square-\square$。再套 L-CSdiff-1 即得链。证毕。

**显式平方表示.** $\delta/4=2^{a-2}(2^{b-a}-1)$，故
$$
\delta=\bigl(2^{a-2}(2^{b-a}-1)+1\bigr)^2-\bigl(2^{a-2}(2^{b-a}-1)-1\bigr)^2.
$$

**计数形.** $|\Delta_K\cap(\mathcal{S}-\mathcal{S})|=|\Delta_K|=\binom{M_K}{2}$，相对密度
$$
\frac{|\Delta_K\cap(\mathcal{S}-\mathcal{S})|}{|\Delta_K|}=1.
$$
此即题述「$\Delta_K$ 中大多数差分属于 $\mathcal{S}-\mathcal{S}$」的**已证最强形**（全体，非仅正比例）。

**注（$a=1$ 边界）.** 全窗差 $2^\ell-2^1=2(2^{\ell-1}-1)\equiv 2\pmod{4}$ **不**在 $\square-\square$ 中，但仍可能在 $\mathcal{S}-\mathcal{S}$ 中（需立方项）。半窗避开此边界；本路线以 $A_K$ 为默认检测族（与 L-AE / L-Diff 一致）。

---

## L-CSdiff-4（已证：薄集厚差 — 密度对照）

**定理.**
1. （薄）$\#(\mathcal{S}\cap[1,X])\ll X^{5/6}$（引 L-CRB-2 箱计数）。  
2. （厚）对一切 $X\ge 1$，
   $$
   \#\bigl((\mathcal{S}-\mathcal{S})\cap[-X,X]\bigr)
   \ge
   \#\bigl\{n\in[-X,X]:n\not\equiv 2\pmod{4}\bigr\}
   \ge\tfrac{3}{2}X-O(1).
   $$
   故 $\mathcal{S}-\mathcal{S}$ 在 $\mathbb{Z}$ 上具有**正下密度** $\ge 3/4$。  
3. （能量 CS）令 $S_X=\mathcal{S}\cap[0,X]$，$M=|S_X|$。则
   $$
   \sum_{\delta}r_{S_X}(\delta)^2=\mathcal{E}_2(S_X),\qquad
   \sum_{\delta}r_{S_X}(\delta)=M^2,
   $$
   且由 Cauchy–Schwarz
   $$
   M^4
   =\Bigl(\sum_{\delta}r_{S_X}(\delta)\Bigr)^2
   \le
   \#\{\delta:r_{S_X}(\delta)>0\}\cdot\mathcal{E}_2(S_X).
   $$
   特别地，支撑大小
   $$
   \#\bigl((S_X-S_X)\bigr)
   \ge
   \frac{M^4}{\mathcal{E}_2(S_X)}
   \ge
   \frac{M^2}{\max(1,M)}
   =M
   $$
   （用平凡 $\mathcal{E}_2\le M^3$）；若 $S_X$ 近随机能量 $\mathcal{E}_2\ll M^{2+\varepsilon}$，则差支撑 $\gg M^{2-\varepsilon}$。

**证明.** (1) 已知。(2) 由 L-CSdiff-2 的包含与模 4 计数。(3) 标准加性能量恒等式与 CS。证毕。

**解读.** $\mathcal{S}$ 密度零，但 $\mathcal{S}-\mathcal{S}$ **不**稀——平方切片 alone 已给出密度 $3/4$。这解释为何「整窗要吞 $\Delta_K$」与「$\Delta_K\subset\mathcal{S}-\mathcal{S}$」可以同时成立集合论上，却在**表示多重性 / 纤维结构**上对真实 $E$ 施压（见条件式节）。

---

## L-CSdiff-5（已证：二进差分的平方表示下界）

**定理.** 设 $a\ge 2$、$b\ge 1$，令 $\delta=D(a,b)=2^a(2^b-1)$。则
$$
r_{\square}(\delta)\ge 1,
$$
从而 $r_{\mathcal{S}}(\delta)\ge 1$。更精细地：每个因子分解
$$
\delta=uv,\qquad u\equiv v\pmod{2},\quad u,v>0,\quad v>u,\quad uv=\delta
$$
对应至多一组
$$
z=\tfrac{u+v}{2},\qquad z'=\tfrac{v-u}{2}
$$
使 $z^2-{z'}^2=\delta$。因 $\delta\equiv 0\pmod{4}$，至少存在一对偶因子（例如 $u=2$、$v=\delta/2$），故
$$
r_{\square}(\delta)
=\#\{(u,v):uv=\delta,\ u\equiv v\pmod 2,\ v>u>0\}
\asymp
\tau_{\mathrm{even}}(\delta),
$$
其中 $\tau_{\mathrm{even}}$ 计同偶正因子对数。特别地，当 $2^b-1$ 有 $\gg (\log b)^{c}$ 个奇因子时，$r_{\square}(\delta)$ 可超过 $1$。

**证明.** 存在性见 L-CSdiff-2/3。因子对应是 $z^2-{z'}^2=(z-z')(z+z')$ 的标准双射（同奇偶条件保证 $z,z'\in\mathbb{Z}$）。证毕。

**与 L-Diff-1 对照.** L-Diff 上界控制的是全形方程 $f(\mathbf{u})-f(\mathbf{v})=\delta$ 的箱内解数；本条给的是**平方切片**的表示下界。二者不矛盾：下界可小（$\ge 1$），上界 $X^{7/6+\varepsilon}$ 针对全箱。

---

## L-CSdiff-6（已证：整窗 $\Rightarrow$ 双落入 $(E-E)\cap(\mathcal{S}-\mathcal{S})$）

**定理.** 若 $N\in\mathcal{F}_0$ 且 $K=\lfloor\log_2(N-1)\rfloor\ge 4$，则对一切 $a,b\in A_K$、$a<b$，
$$
2^b-2^a\in(E-E)\cap(\mathcal{S}-\mathcal{S})\cap(\mathcal{R}-\mathcal{R}).
$$
按有序对计：
$$
\#\bigl\{(a,b)\in A_K^2:a<b,\ 2^b-2^a\in(E-E)\cap(\mathcal{S}-\mathcal{S})\bigr\}
=\binom{M_K}{2}.
$$

**证明.** L-Diff-3（或 L-Ekill-A2-1）给出 $2^b-2^a\in E-E$；L-CSdiff-3 给出同元属于 $\mathcal{S}-\mathcal{S}\subseteq\mathcal{R}-\mathcal{R}$。证毕。

**定位.** 这是本路线的**已证构型恒等式**：整窗不是在「稀差集」上饱和，而是在**已经属于立方–平方差（乃至平方差）**的差族上饱和。E-kill 的增量在于：真实 $E$ 能否把整份 $\Delta_K$ 同时嵌进 $E-E$。

---

## L-CSdiff-7（条件式：结构反吞噬 $\Rightarrow\mathcal{F}_0$ 有限）

### 7.1 假设 CSdiff-Out$_\eta$

存在 $\eta\in(0,1]$、$K_0$，使对一切 $K\ge K_0$ 与一切 $2^K<N\le 2^{K+1}$，
$$
\#\bigl\{(a,b)\in A_K^2:a<b,\ 2^b-2^a\in E-E\bigr\}
\le(1-\eta)\binom{M_K}{2}.
$$
（与 Diff-Out$_\eta$ 同文；此处强调检测族已由 L-CSdiff-3 钉在 $\mathcal{S}-\mathcal{S}$ 内。）

**引理.** CSdiff-Out$_\eta\Rightarrow\mathcal{F}_0$ 有限 $\stackrel{\mathrm{L07}}{\Rightarrow}$ $x=0$ 型充分大全体可表。

**证明.** 同 L-Diff-4：大 $N\in\mathcal{F}_0$ 时 L-CSdiff-6 迫使左端 $=\binom{M_K}{2}$，矛盾。证毕。

### 7.2 假设 CSdiff-Fiber$_\theta$（平方纤维过厚 $\Rightarrow$ 例外相关亏缺）

存在 $\theta>0$、$c>0$、$K_0$，使只要 $\delta=2^b-2^a\in\Delta_K$ 满足 $r_{\square}(\delta)\ge 2^{\theta a}$（或 $\tau(2^b-1)\ge 2^{\theta a}$），则对一切大 $N$，
$$
r_{E\cap[N/2,N]}(\delta)
\le
(1-c)\,r_{\mathbb{Z}\cap[N/2,N]}(\delta)
=
(1-c)\bigl(\tfrac{N}{2}-O(\delta)\bigr)_+.
$$
直观：平方差纤维过厚时，真实例外集不能在差 $\delta$ 上近饱和。

**引理.** 若存在 $\eta>0$ 使「$r_{\square}(\delta)\ge 2^{\theta a}$ 的 $\delta\in\Delta_K$」至少占 $\eta$ 比例，且 CSdiff-Fiber$_\theta$ 成立，则对这些差 CSdiff-Out 的局部版成立；若再与「其余差上的 Diff-Link / AE-Corr」拼合，可推 $\mathcal{F}_0$ 有限。

### 7.3 假设 CSdiff-Clash$_\eta$（$(E-E)\cap(\mathcal{S}-\mathcal{S})$ 不能近满 $\Delta_K$）

存在 $\eta>0$、$K_0$，使对大 $K$ 与 $2^K<N\le 2^{K+1}$，
$$
\#\bigl\{(a,b):a<b,\ 2^b-2^a\in(E-E)\cap(\mathcal{S}-\mathcal{S})\bigr\}
\le(1-\eta)\binom{M_K}{2}.
$$
因 L-CSdiff-3 已证 $\Delta_K\subseteq\mathcal{S}-\mathcal{S}$，本假设 $\Leftrightarrow$ CSdiff-Out$_\eta$。

**引理.** CSdiff-Clash$_\eta\Rightarrow\mathcal{F}_0$ 有限（由 L-CSdiff-6）。

### 7.4 假设 CSdiff-Mix$_\theta$（与 Inc-MixDiff 对齐）

若 $\kappa_\Delta(E_N;K)\ge 1-\eta'$，则 $\gg K^{2\theta}$ 个 $\delta\in\Delta_K$ 满足 $r_{E_N}(\delta)\ge 2$，且这些 $\delta$ 的超额表示来自 $\mathcal{S}-\mathcal{S}$ 或 $\mathcal{R}-\mathcal{R}$ 的多解（对照 L-Diff-1 纤维与 L-CSdiff-5 的 $\tau_{\mathrm{even}}$）。

**引理.** CSdiff-Mix$_\theta\Rightarrow\mathcal{F}_0$ 有限（同 L-Inc-7 的 MixDiff 枝）。

**总图式（条件式）**
$$
\begin{align*}
N\in\mathcal{F}_0
&\ \stackrel{\mathrm{L\text{-}CSdiff\text{-}6}}{\Longrightarrow}\
\Delta_K\subseteq(E-E)\cap(\mathcal{S}-\mathcal{S})\\
&\ \stackrel{\mathrm{CSdiff\text{-}Out/Clash/Fiber/Mix}}{\Longrightarrow}\
\bot\\
&\ \Longrightarrow\ \mathcal{F}_0\text{ 有限}
\ \stackrel{\mathrm{L07}}{\Longrightarrow}\
\text{$x=0$ 型充分大全体可表}.
\end{align*}
$$

---

## L-CSdiff-8（已证对照：与 Diff / AE / Inc / Slowx 的关系）

| 路线 | 检测物 | 本路线增量 |
|------|--------|------------|
| L-Diff | $f(\mathbf{u})-f(\mathbf{v})=D$；$\kappa_E$；Diff-Out | 把「可能 $\in\mathcal{R}-\mathcal{R}$」升级为**已证** $\Delta_K\subseteq\mathcal{S}-\mathcal{S}\subseteq\mathcal{R}-\mathcal{R}$；Diff-Out 的检测族获得立方–平方结构标签 |
| L-AE / L-Inc | $\mathcal{E}_2$；$\Delta_K$-团；MixDiff | L-CSdiff-3/6 是 MixDiff / Flat-Clash 的**算术前置**：团差全部是平方差 |
| L-Slowx | $\mathcal{S}$ 薄；$x^4+\mathcal{S}$ | 本路线用同一 $\mathcal{S}$，但转向**差集厚**（L-CSdiff-4），而非缓增切片覆盖 |
| L08 | 抽象密度零可无限 $\mathcal{F}_0$ | CSdiff-Out/Clash 必须吃进 $\mathcal{S}$ 的算术（平方差纤维），不能只靠密度 |

**与「大多数」一语的结算.**  
- **集合论层（已证）**：$\Delta_K$ 的 $100\%$ 属于 $\mathcal{S}-\mathcal{S}$ 与 $\mathcal{R}-\mathcal{R}$（L-CSdiff-3）。  
- **例外吞噬层（条件式）**：真实 $E$ 不能让这 $100\%$ 同时落入 $E-E$（CSdiff-Out / Clash）。  
二者合起来精确化用户目标句：「大多数差分属于 $\mathcal{S}-\mathcal{S}$ 或 $\mathcal{R}-\mathcal{R}$，从而真实 $E$ 很难吞下整窗」。

---

## 精确缺口登记

| 代号 | 内容 | 堵住则得 |
|------|------|----------|
| **CSdiff-G1** | **CSdiff-Out$_\eta$ / Clash$_\eta$ 对真实 $E$.** 需用 $\mathcal{R}_{4,3,2}=\bigcup(x^4+\mathcal{S})$ 证明半窗差不能被 $E-E$ 饱和。同 Diff-G1；抽象上被 L08 阻挡。 | $\mathcal{F}_0$ 有限 |
| **CSdiff-G2** | **CSdiff-Fiber$_\theta$.** 定量：$\tau_{\mathrm{even}}(\delta)$ 大 $\Rightarrow$ $r_E(\delta)$ 亏缺。需平方差平移与可表集的相关估计。 | 对高纤维差局部 Out |
| **CSdiff-G3** | **CSdiff-Mix$_\theta$.** 整窗饱和 $\Rightarrow$ 多解超额 $r_E\ge 2$（来自 $\mathcal{S}-\mathcal{S}$ 多解）。同 Inc-G2 / Diff-G2。 | 无 Out 时的超饱和杀窗 |
| **CSdiff-G4** | **全窗 $a=1$ 边.** $2^\ell-2\notin\square-\square$；是否仍 $\in\mathcal{S}-\mathcal{S}$（立方贡献）？若否，全窗版需单独处理。半窗路线不受影响。 | 全窗强化 |
| **CSdiff-G5** | **四次平移层.** 利用 $\mathcal{R}-\mathcal{R}=\{x^4-{x'}^4\}+(\mathcal{S}-\mathcal{S})$ 把「同 $x$ 纤维」与「跨 $x$ 纤维」分开估，期望更强的 Clash。 | 细纤维 E-kill |

---

## 状态一览

| 编号 | 状态 | 备注 |
|------|------|------|
| L-CSdiff-1 | 已证 | $\mathcal{R}-\mathcal{R}=\{x^4-{x'}^4\}+(\mathcal{S}-\mathcal{S})$；$\mathcal{S}-\mathcal{S}\subseteq\mathcal{R}-\mathcal{R}$ |
| L-CSdiff-2 | 已证 | $\square-\square\subseteq\mathcal{S}-\mathcal{S}$；$n\in\square-\square\Leftrightarrow n\not\equiv 2\pmod 4$ |
| L-CSdiff-3 | 已证 | $K\ge 4\Rightarrow\Delta_K\subseteq\square-\square\subseteq\mathcal{S}-\mathcal{S}$（全体） |
| L-CSdiff-4 | 已证 | $\mathcal{S}$ 薄 / $\mathcal{S}-\mathcal{S}$ 厚（密度 $\ge 3/4$）；CS 能量支撑 |
| L-CSdiff-5 | 已证 | $a\ge 2\Rightarrow r_{\square}(D(a,b))\ge 1$；$\asymp\tau_{\mathrm{even}}$ |
| L-CSdiff-6 | 已证 | 整窗 $\Rightarrow\Delta_K\subseteq(E-E)\cap(\mathcal{S}-\mathcal{S})$ |
| L-CSdiff-7 | 条件式 | Out / Fiber / Clash / Mix $\Rightarrow\mathcal{F}_0$ 有限 |
| L-CSdiff-8 | 已证（对照） | 与 Diff/AE/Inc/Slowx/L08 |

**原猜想（含 $x>0$）仍开放。**
