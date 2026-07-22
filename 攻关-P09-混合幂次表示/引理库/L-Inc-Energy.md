# L-Inc-Energy：能量增量 → AP / 多项式构型 → 与 Roth 例外冲突（路线 R12-Energy-Increment）

> 路线 **R12-Energy-Increment**（P09 攻关轮次 12，服务 **P1 = E-kill-1**）。  
> **定位**：超越 L-AE 的「近随机能量讨论」。L-AE 已证整窗 $\Rightarrow\mathcal{E}_2\gg K^2$，并指出平坦饱和 **AE-G1** 使「仅近随机 $\not\Rightarrow\mathcal{F}_0$ 有限」。本路线把主轴改为：  
> $$
> N\in\mathcal{F}_0
> \;\Longrightarrow\;
> E\text{ 含完整 }\Delta_K\text{-平移团}
> \;\Longrightarrow\;
> \text{对 }E\cap[N/2,N]\text{ 做能量增量}
> \;\Longrightarrow\;
> \text{高能量}\Rightarrow\text{长 AP / 多项式构型}
> \;\overset{?}{\Longrightarrow}\;
> \text{与混合幂差集或「Roth 例外不应含长 AP」冲突}.
> $$
> **信念登记（非定理）.** 真实 $E$ 作为圆法例外集，文献上**通常被认为**伪随机（差表示均匀、无长 AP、无厚 Bohr 片），但**无证明**；本文件条件式恰把该信念写成可检验输入 Inc-NoAP / Inc-Pseudo。  
> **不**重复证明 L-AE-1…3（仅引用）；**不**声称原猜想已证。

---

## 0. 符号与对象

沿用 L-AE / L-Ekill-A2：
$$
E=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2},\qquad
K=\lfloor\log_2(N-1)\rfloor,\qquad
W(N)=\{N-2^k:1\le k\le K\},
$$
$$
\mathcal{F}_0=\{N\ge 2:W(N)\subseteq E\},\qquad
I_N=\bigl[\tfrac{N}{2},N\bigr]\cap\mathbb{Z},\qquad
E_N=E\cap I_N,\qquad M_N=|E_N|.
$$
半窗指数集 $A_K=\{\lceil K/2\rceil,\ldots,K\}$，$M_K=|A_K|\asymp K/2$，
$$
\Delta_K=\{2^a-2^b:a,b\in A_K,\,a<b\},
\qquad
S_N=\{N-2^a:a\in A_K\}.
$$
加性能量与 $\Delta_K$-限制相关 / 能量同 L-AE：
$$
\mathcal{E}_2(E_N)=\sum_d r_{E_N}(d)^2,\qquad
\mathcal{C}(E_N;\Delta_K)=\sum_{\delta\in\Delta_K}r_{E_N}(\delta),\qquad
\mathcal{E}_2(E_N;\Delta_K)=\sum_{\delta\in\Delta_K}r_{E_N}(\delta)^2.
$$

**构型计数（本路线新增主对象）.** 对有限 $A\subset\mathbb{Z}$、长度 $\ell\ge 3$，写
$$
\Lambda_\ell(A)
:=\#\bigl\{(x,d)\in\mathbb{Z}\times\mathbb{N}:d\ge 1,\;
\{x,x+d,\ldots,x+(\ell-1)d\}\subset A\bigr\}
$$
（含平凡与非平凡；下文「长 AP」指 $\ell\ge\omega(K)$ 且公差 $d\ge 1$ 的非退化构型）。  
多项式构型计数（示意；$P\in\mathbb{Z}[t]$ 固定、$\deg P\ge 2$）
$$
\Lambda_P(A):=\#\bigl\{(x,d):d\ge 1,\;\{x,\,x+P(d)\}\subset A\bigr\}
$$
（可扩至多点 $\{x,x+P_1(d),\ldots\}$；本文件以 AP 为主、多项式为旁注）。

**能量增量阈值（抽象组合，引用模板）.** 称集合 $A$ **$c$-能量富**（Inc-High$_c$），若
$$
\mathcal{E}_2(A)\ge|A|^{2+c}.
$$
称 $A$ **$\varepsilon$-能量贫**（Inc-Poor$_\varepsilon$），若 $\mathcal{E}_2(A)\le|A|^{2+\varepsilon}$。

---

## L-Inc-1（已证：整窗 $\Rightarrow$ 完整 $\Delta_K$-平移团）

设 $N\in\mathcal{F}_0$ 且 $2^K<N\le 2^{K+1}$。则：

1. $S_N\subset E$，且 $S_N^\circ:=S_N\cap I_N$ 满足 $|S_N^\circ|\ge M_K-1$；  
2. $S_N^\circ$ 是 $\mathrm{Cay}(\mathbb{Z},\Delta_K\cup(-\Delta_K))$ 中大小 $\ge M_K-1$ 的团；  
3. $\mathcal{C}(E_N;\Delta_K)\ge\binom{M_K-1}{2}\gg K^2$。

**证明.** 即 L-AE-1；此处不重写。证毕。

**注（团本身无长 AP）.** 纯二进点集 $S_N$ 上，方程
$$
2(N-2^b)=(N-2^a)+(N-2^c)
\iff 2^{b+1}=2^a+2^c
$$
在 $a,b,c\in A_K$ 上仅有平凡解（两侧 $2$-进赋值冲突）。故**不能**从团点直接读出长 AP；能量增量必须作用于整片 $E_N$，而非仅 $S_N$。

---

## L-Inc-2（已证：整窗 $\Rightarrow$ 限制构型密度下界）

沿用 L-AE-2 的 Cauchy–Schwarz 链。若 $N\in\mathcal{F}_0$，则
$$
\mathcal{E}_2(E_N;\Delta_K)
\ge\frac{\mathcal{C}(E_N;\Delta_K)^2}{|\Delta_K|}
\ge\frac{\binom{M_K-1}{2}^2}{\binom{M_K}{2}}
\gg K^2,
$$
且 $\mathcal{E}_2(E_N)\ge\mathcal{E}_2(E_N;\Delta_K)\gg K^2$。

进一步定义**团–差构型密度**
$$
\kappa_\Delta(E_N;K)
:=\frac{\mathcal{C}(E_N;\Delta_K)}{\binom{M_K}{2}}.
$$
则整窗给出
$$
\kappa_\Delta(E_N;K)\ge\frac{\binom{M_K-1}{2}}{\binom{M_K}{2}}=1-O\Bigl(\tfrac{1}{K}\Bigr).
$$
即：整窗 $\Rightarrow$ $\Delta_K$-相关构型以相对密度 $1-o(1)$ 饱和。

**证明.** L-AE-1 + L-AE-2。证毕。

**解读.** 这是本路线的**已证构型下界**：不是「$E_N$ 含长 AP」，而是「$E_N$ 几乎装下全部 $\Delta_K$-差对」。后续能量增量把该饱和升级为加性结构（AP / Bohr / GAP），再与例外集假说冲突。

---

## L-Inc-3（已证：能量二分——贫 / 富）

对任意有限 $A\subset\mathbb{Z}$ 与任意 $c>\varepsilon>0$，下列恰一成立（可并存时优先富）：

- **(Poor)** $\mathcal{E}_2(A)\le|A|^{2+\varepsilon}$（能量贫）；  
- **(Rich)** $\mathcal{E}_2(A)\ge|A|^{2+c}$（能量富）。

特别地取 $A=E_N$。若 $N\in\mathcal{F}_0$，则由 L-Inc-2 知 $\mathcal{E}_2(E_N)\gg K^2$。于是：

1. 若同时 $M_N\le K^{1/(1+\varepsilon/2)-\eta}$（$\eta>0$ 固定），则与 L-AE-3(4) 的相关上界冲突（半区间例外过稀不能撑 $\mathcal{C}\asymp K^2$）——但 Roth 尺度下 $M_N$ 远大于此，**无新杀伤**；  
2. 在 Roth 尺度 $M_N\ll N/(\log N)^{1/20}$ 下，弱下界 $\mathcal{E}_2\gg K^2$ **两者皆容**：贫枝需 $M_N^{2+\varepsilon}\gg K^2$，富枝当然更大。故整窗不强制富能量——这正是 AE-G1 / 平坦饱和的再现。

**证明.** 二分是定义；比较句引用 L-AE-3 与 AE-G1。证毕。

**本路线相对 L-AE 的转向.** 不再把「证明 AE-Rand」当作主目标；改为：  
- **贫枝**：用「近完整 $\Delta_K$-团 + 能量贫」与混合幂差集多解 / 相关亏缺冲突（Inc-Flat-Clash）；  
- **富枝**：用能量增量产出长 AP，再与 Inc-NoAP 冲突。

---

## L-Inc-4（已证：能量增量模板 $\Rightarrow$ 构型密度下界——组合黑箱）

**引用模板（Bloom–Sisask / Sanders / Balog–Szemerédi–Gowers 型；非本仓库新证）.**  
存在绝对函数 $\omega_\ast:(0,1]\to[3,\infty)$ 与 $\gamma:(0,1]\to(0,1]$，使对一切有限 $A\subset\mathbb{Z}$：若 $\mathcal{E}_2(A)\ge|A|^{2+c}$，则存在 $A'\subset A$、$|A'|\ge|A|^{\gamma(c)}$，满足
$$
\Lambda_{\ell}(A')\ge |A'|^{\,2-\eta}\qquad\text{对某个 }\ell=\ell(c)\ge\omega_\ast(c),\ \eta=\eta(c)>0,
$$
或更弱地：$A'$ 含相对稠密的 Bohr / GAP 片 $P$，且
$$
|P\cap A'|\ge|A'|^{\gamma(c)}.
$$
（具体常数随文献版本变化；本文件只依赖「富能量 $\Rightarrow$ 可检出长度 $\ge\omega(c)$ 的加性构型」这一形状。）

**本路线推论（已证蕴含，给定模板）.**  
若 $E_N$ 满足 Inc-High$_c$，则
$$
\Lambda_{\ell}(E_N)\ge 1\qquad\text{对某个 }\ell\ge\omega_\ast(c),
$$
且事实上有多项式级下界（依所选模板）。写
$$
\omega(K):=\omega_\ast(c_0)
$$
（固定小 $c_0>0$ 时为绝对常数；若允许 $c=c(K)\to 0$ 则 $\omega(K)\to\infty$ 缓慢——见缺口 Inc-G3）。

**证明.** 直接套用模板于 $A=E_N$。证毕。

**注.** 本条**不**断言真实 $E_N$ 能量富；只断言「一旦富，则构型密度下界成立」。与 L-Inc-2 的「整窗 $\Rightarrow\Delta_K$-饱和」并列，构成已证层的两端。

---

## L-Inc-5（已证：二进团与 3-AP 的正交——排除「团即 AP」误读）

设 $a,b,c\in A_K$。则 $\{N-2^a,N-2^b,N-2^c\}$ 成 3-AP 当且仅当 $\{a,b,c\}$ 平凡（至多两点重合的退化）。  
因而 L-Inc-1 的平移团**不是**长度 $\ge 3$ 的 AP 源；任何「整窗 $\Rightarrow$ 长 AP」断言必须经过 $E_N\setminus S_N$ 的额外结构或能量富枝。

**证明.** 见 L-Inc-1 注中的 $2$-进赋值。证毕。

---

## L-Inc-6（条件式：Inc-NoAP$_\omega$ $\Rightarrow$ 整窗不能走富枝）

**假设 Inc-NoAP$_\omega$.**  
存在函数 $\omega:\mathbb{N}\to[3,\infty)$ 与 $N_0$，使对一切 $N\ge N_0$，
$$
\Lambda_\ell(E_N)=0\qquad\text{对一切 }\ell\ge\omega(K)
$$
（即半窗例外集不含长度 $\ge\omega(K)$ 的 AP）。  
更强形 **Inc-NoAP$^\sharp$**：对一切区间 $I\subset[1,X]$，$|I|\asymp X$，有 $\Lambda_\ell(E\cap I)=0$（$\ell\ge\omega(\log X)$）。

**意图.** 圆法例外集的「伪随机信念」常蕴含：例外点不应沿长等差数列堆积（否则主弧/奇异级数或局部密度会强制其中多数可表）。对真实 $E$ **未证**。

**引理.** Inc-NoAP$_\omega$ + L-Inc-4 模板（取 $\omega_\ast(c)\ge\omega(K)$ 对大 $K$）$\Rightarrow$ 对大 $N\in\mathcal{F}_0$，集合 $E_N$ **不能**满足 Inc-High$_c$。  
即：整窗若存在，则必须落在能量贫枝。

**证明.** 若 Inc-High$_c$，L-Inc-4 给 $\Lambda_\ell(E_N)\ge 1$（$\ell\ge\omega_\ast(c)$），与 Inc-NoAP 矛盾。证毕。

---

## L-Inc-7（条件式：贫枝 + 平坦团冲突 Inc-Flat-Clash）

由 L-Inc-6，在 Inc-NoAP 下整窗被迫能量贫：$\mathcal{E}_2(E_N)\le M_N^{2+\varepsilon}$。此时 L-AE 锐性（AE-G1）指出：单一 $\Delta_K$-团的平坦嵌入恰与贫能量相容。要得矛盾需额外输入。

**假设 Inc-Flat-Clash$_\eta$（贫能量不能近饱和 $\Delta_K$-相关）.**  
存在 $\varepsilon,\eta>0$、$N_0$，使只要 $\mathcal{E}_2(E_N)\le M_N^{2+\varepsilon}$，就有
$$
\kappa_\Delta(E_N;K)\le 1-\eta.
$$
（等价于 L-AE 的 AE-Corr$_\eta$，此处改名以强调「增量后残差贫枝」语境。）

**引理.** Inc-NoAP$_\omega$ + Inc-Flat-Clash$_\eta$ $\Rightarrow\mathcal{F}_0$ 有限。

**证明.** 大 $N\in\mathcal{F}_0$ $\Rightarrow$ L-Inc-2 给 $\kappa_\Delta\ge 1-O(1/K)$；又由 L-Inc-6 必能量贫 $\Rightarrow$ Inc-Flat-Clash 给 $\kappa_\Delta\le 1-\eta$，矛盾。证毕。

**假设 Inc-MixDiff$_\theta$（混合幂差集强迫流行差）.**  
若 $\kappa_\Delta(E_N;K)\ge 1-\eta'$，则存在 $\gg K^{2\theta}$ 个 $\delta\in\Delta_K$ 使 $r_{E_N}(\delta)\ge 2$（来自方程 $f(\mathbf{u})-f(\mathbf{v})=\delta$、$f=x^4+y^3+z^2$ 的多解，对照 L-Diff）。  
则限制能量超饱和 $\mathcal{E}_2(E_N;\Delta_K)\ge(1+\eta)\mathcal{C}$，与纯 $0$-$1$ 团实现冲突（同 AE-Super）。

**引理.** Inc-MixDiff$_\theta$ $\Rightarrow\mathcal{F}_0$ 有限（无需 NoAP）。

**证明.** 整窗 $\Rightarrow$ 近饱和相关 + 团的 $0$-$1$ 实现；Inc-MixDiff 强迫 $r\ge 2$ 成簇，矛盾。证毕。

---

## L-Inc-8（条件式：富枝 + 结构片不撑窗 Inc-Struct）

若不假设 Inc-NoAP，允许富枝。此时 L-Inc-4 产出 Bohr/GAP 片 $P\subset I_N$。

**假设 Inc-Struct$_\theta$.**  
对能量增量产出的结构片 $P$，
$$
\#\{1\le k\le K:N-2^k\in P\cap E\}\le C K^{\theta},\qquad\theta<1.
$$
（同 AE-Struct；真实 $E$ 上未证，且抽象上被 L08 阻挡。）

**引理.** Inc-High 强制发生（例如由 Inc-Jump：大团 $\Rightarrow$ 能量跃迁）+ L-Inc-4 + Inc-Struct$_\theta$ + 残差上的 Inc-Flat-Clash $\Rightarrow\mathcal{F}_0$ 有限。

**证明梗概.** 与 L-AE-6 同构：增量迭代剥离结构片；Inc-Struct 限制窗点落入结构例外的数量；残差贫且不能装 $\Delta_K$-整团。证毕。

---

## L-Inc-9（条件式总述：能量增量 E-kill 图式）

**目标图式（条件式；原猜想开放）**
$$
\begin{align*}
N\in\mathcal{F}_0
&\ \stackrel{\mathrm{L\text{-}Inc\text{-}1/2}}{\Longrightarrow}\
\text{完整 }\Delta_K\text{-团},\ \kappa_\Delta=1-o(1)\\
&\ \Longrightarrow\
\begin{cases}
\mathrm{Rich}:\ \mathcal{E}_2\ge M^{2+c}
\ \stackrel{\mathrm{L\text{-}Inc\text{-}4}}{\Longrightarrow}\
\text{长 AP / Bohr}
\ \stackrel{\mathrm{Inc\text{-}NoAP\ 或\ Struct}}{\Longrightarrow}\ \bot\\[4pt]
\mathrm{Poor}:\ \mathcal{E}_2\le M^{2+\varepsilon}
\ \stackrel{\mathrm{Inc\text{-}Flat\text{-}Clash\ 或\ MixDiff}}{\Longrightarrow}\ \bot
\end{cases}\\
&\ \Longrightarrow\ \mathcal{F}_0\text{ 有限}
\ \stackrel{\mathrm{L07}}{\Longrightarrow}\
\text{$x=0$ 型充分大全体可表}.
\end{align*}
$$

**压缩形（用户目标句）.**  
若真实 $E$ 满足「无长度 $\ge\omega(K)$ 的 AP」（Inc-NoAP$_\omega$），则与「整窗 $\Rightarrow$ 团 $\Rightarrow$（在 Jump 或贫枝 Clash 下）必出长 AP 或相关饱和」联立得矛盾，故 $\mathcal{F}_0$ 有限。

**信念 vs 定理.**  
「真实 $E$ 伪随机 / 无长 AP」是圆法例外集的**常见信念**，不是本仓库定理；写成 Inc-NoAP / Inc-Pseudo 后方可进入条件式链。L08 表明抽象密度零集可无限整窗且可人为 AP-free（把窗种种成 Sidon 型），故 Inc-NoAP 必须吃进 $\mathcal{R}_{4,3,2}$ 的算术（不能只靠密度）。

---

## L-Inc-10（已证对照：与 L-AE / L-Diff / L-FW / Pack 的关系）

| 路线 | 检测物 | 本路线增量 |
|------|--------|------------|
| L-AE | $\mathcal{E}_2$；近随机 / Corr / Jump | **超越**近随机主讨论；主轴改为增量 $\to$ AP 构型；贫枝 Clash $\equiv$ AE-Corr |
| L-AE-6 | Sanders + AE-Struct | 富枝接口同构；本文件用 Inc-NoAP 提供**另一杀伤**（直接禁长 AP） |
| L-Diff | $f(\mathbf{u})-f(\mathbf{v})=2^a(2^b-1)$ | Inc-MixDiff 的候选算术来源 |
| L-FW | $|\Phi_N|$ 低频指纹 | 不使用 $k$-谱；构型在物理空间 |
| L-Pack | 邻/倍窗装填 | 不使用多窗；单窗能量增量 |
| L08 | 抽象密度零可无限 $\mathcal{F}_0$ | Inc-NoAP / Flat-Clash / MixDiff 均需真实混合幂输入 |

---

## 精确缺口登记

| 代号 | 内容 | 堵住则得 |
|------|------|----------|
| **Inc-G1** | **Inc-NoAP$_\omega$ 对真实 $E$.** 需证：$E\cap[N/2,N]$（或全局 $E$）不含长度 $\ge\omega(K)$ 的 AP。信念强于 Roth 密度；抽象上非真（L08 可造 AP-free 整窗族）。必须用 $\mathcal{R}_{4,3,2}$ 在长 AP 上的正密度 / 圆法。 | 与富枝模板联立杀富窗；再加 Flat-Clash 杀贫窗 |
| **Inc-G2** | **Inc-Flat-Clash / Inc-MixDiff.** 贫能量下不能近饱和 $\Delta_K$-团；或混合幂差集强迫 $r\ge 2$。同 AE-G2 / Diff-Out。 | 贫枝闭合 |
| **Inc-G3** | **增量长度 $\omega(K)$. ** 模板给出的 AP 长度常为绝对常数或 $(\log)^{O(1)}$；需 $\omega(K)\to\infty$ 或与窗尺度 $K$ 对齐的均匀版本，才能叫「长」。 | NoAP 假设与模板对接 |
| **Inc-G4** | **Inc-Jump.** 大 $\Delta_K$-团是否迫使 $\mathcal{E}_2\ge M^{2+\delta}$（真实 $E$）。若成立，则整窗直接进富枝，可绕过「贫枝相容」的 AE-G1。 | 单枝富能量路径 |
| **Inc-G5** | **Inc-Struct$_\theta$.** 结构片与二进窗交 $<K^{1-\delta}$（同 AE-G4）。 | 无 NoAP 时的富枝闭合 |
| **Inc-G6** | **伪随机信念的定量式 Inc-Pseudo.** 例如 Gowers $U^{s}$ 范数 $\|1_E-\delta_E\|_{U^{s}}=o(1)$；蕴含 NoAP 与 Flat-Clash，但是否对圆法例外集成立完全开放。 | 统一条件式输入 |

---

## 不等式 / 逻辑链速查

**链 A（已证：整窗 $\to$ 构型饱和）**
$$
N\in\mathcal{F}_0
\ \Longrightarrow\
\kappa_\Delta(E_N;K)=1-o(1)
\ \Longrightarrow\
\mathcal{E}_2(E_N;\Delta_K)\gg K^2.
$$

**链 B（已证：富能量 $\to$ AP 下界，给定模板）**
$$
\mathcal{E}_2(E_N)\ge M_N^{2+c}
\ \Longrightarrow\
\Lambda_\ell(E_N)\gg_\ell 1
\quad(\ell\ge\omega_\ast(c)).
$$

**链 C（条件式：无长 AP $\Rightarrow$ 整窗矛盾）**
$$
\mathrm{Inc\text{-}NoAP}_\omega
+\mathrm{Inc\text{-}Flat\text{-}Clash}_\eta
+\bigl(N\in\mathcal{F}_0\bigr)
\ \Longrightarrow\
\bigl(\kappa_\Delta=1-o(1)\bigr)
\wedge
\bigl(\kappa_\Delta\le 1-\eta\bigr)
\ \Longrightarrow\ \bot
\ \Longrightarrow\ \mathcal{F}_0\text{ 有限}.
$$

**链 C′（条件式：无长 AP + Jump）**
$$
\mathrm{Inc\text{-}NoAP}_\omega
+\mathrm{Inc\text{-}Jump}_\delta
+\bigl(N\in\mathcal{F}_0\bigr)
\ \Longrightarrow\
\text{富能量}\Rightarrow\text{长 AP}\Rightarrow\bot.
$$

**链 D（条件式：MixDiff 单刀）**
$$
\mathrm{Inc\text{-}MixDiff}_\theta
+\bigl(N\in\mathcal{F}_0\bigr)
\ \Longrightarrow\
\text{相关近饱和}+\text{流行差 }r\ge 2
\ \Longrightarrow\ \bot.
$$

---

## 状态表

| 编号 | 状态 | 摘要 |
|------|------|------|
| L-Inc-1 | 已证（引 L-AE-1） | 整窗 $\Rightarrow$ 完整 $\Delta_K$-团 |
| L-Inc-2 | 已证 | 整窗 $\Rightarrow$ $\kappa_\Delta=1-o(1)$，$\mathcal{E}_2(\Delta_K)\gg K^2$ |
| L-Inc-3 | 已证 | 贫/富能量二分；整窗不强制富（AE-G1 再现） |
| L-Inc-4 | 已证（模板蕴含） | 富能量 $\Rightarrow$ 长 AP / Bohr 构型密度下界 |
| L-Inc-5 | 已证 | 二进团本身无 3-AP（排除误读） |
| L-Inc-6 | 条件式 | Inc-NoAP $\Rightarrow$ 整窗不能走富枝 |
| L-Inc-7 | 条件式 | NoAP + Flat-Clash（或 MixDiff）$\Rightarrow\mathcal{F}_0$ 有限 |
| L-Inc-8 | 条件式 | 富枝 + Struct 增量迭代杀窗 |
| L-Inc-9 | 条件式总述 | 全图式；信念 ≠ 定理 |
| L-Inc-10 | 已证（对照） | 与 AE/Diff/FW/Pack/L08 关系 |

**本轮结论.** 已把 E-kill 主轴从「近随机能量」转为「能量增量 $\to$ 构型 $\to$ 与 NoAP / 混合幂差集冲突」。**已证**：整窗给出 $\Delta_K$-构型饱和（L-Inc-1/2）及富能量下的 AP 下界模板（L-Inc-4）。**条件式**：若 $E$ 无长度 $\ge\omega(K)$ 的 AP，则与 Flat-Clash（或 Jump）联立得 $\mathcal{F}_0$ 有限（L-Inc-6/7）。真实 $E$ 的伪随机 / 无长 AP **未证**（Inc-G1）。原猜想保持开放。
