# L-AE-Energy：例外集加性能量与二进窗平移团（路线 R2-Additive-Energy）

> 路线 **R2-Additive-Energy**（P09 攻关轮次 2，服务 **P1 = E-kill-1**）。  
> 目标：在区间 $I=[N/2,N]$ 上定义真实例外集的加性能量，给出与 $\Delta_K$ 平移团冲突的**不等式链**；条件式地推出 $\mathcal{F}_0$ 有限；并登记与 Balog–Wooley / Sanders 能量增量的接口及精确缺口。  
> **不**重复 L-FW / L-Det / L-Ekill-A2 已写内容（仅引用其结论编号）；**不**声称原猜想已证。

---

## 0. 符号与对象

沿用：$E=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2}$，$K=\lfloor\log_2(N-1)\rfloor$，
$$
W(N)=\{N-2^k:1\le k\le K\},\qquad
\mathcal{F}_0=\{N\ge 2:W(N)\subseteq E\}.
$$
对 $N\ge 4$ 取半区间
$$
I_N:=\Bigl[\tfrac{N}{2},\,N\Bigr]\cap\mathbb{Z},
$$
并写 $E_N:=E\cap I_N$、$M_N:=|E_N|$。

**加性能量**（本路线主对象）
$$
\mathcal{E}_2(E_N)
:=\#\bigl\{(a,b,c,d)\in E_N^4:a+b=c+d\bigr\}.
$$
等价地，令差表示函数 $r_{E_N}(d)=\#\{(x,y)\in E_N^2:x-y=d\}$，则
$$
\mathcal{E}_2(E_N)=\sum_{d\in\mathbb{Z}}r_{E_N}(d)^2.
$$
平凡界
$$
M_N^2\le\mathcal{E}_2(E_N)\le M_N^3
$$
（下界来自平凡解 $(a,b)=(c,d)$ 与互换；上界来自固定三元自由第四元）。  
称 $E_N$ **$\varepsilon$-近随机能量**（近极小 / Sidon 型；假设 **AE-Rand$_\varepsilon$**），若
$$
\mathcal{E}_2(E_N)\le M_N^{2+\varepsilon}.
$$
（当 $M_N\ll |I_N|^{1/2}$ 时，随机集能量亦 $\asymp M_N^2$；本用语取「接近极小阶 $M^{2+\varepsilon}$」。）

半窗指数集与二进差集（与 L-Ekill-A2-1 相同，此处只引用）
$$
A_K=\bigl\{a:\lceil K/2\rceil\le a\le K\bigr\},\qquad
M_K=|A_K|\asymp\tfrac{K}{2},
$$
$$
\Delta_K=\{2^a-2^b:a,b\in A_K,\ a<b\}.
$$
局部相关区间 $J_N:=[N-2^K,\,N-2^{\lceil K/2\rceil}]$（与 $I_N$ 相交非空；不必 $J_N\subset I_N$）。对 $S\subset\mathbb{Z}$ 写**$\Delta_K$-限制相关**
$$
\mathcal{C}(S;\Delta_K)=\sum_{\delta\in\Delta_K}r_S(\delta)
=\sum_{a<b}\sum_{t}1_S(t)\,1_S(t+2^a-2^b).
$$
（L-Ekill-A2-1：若 $N\in\mathcal{F}_0$ 则 $\mathcal{C}(E\cap J_N;\Delta_K)\ge\binom{M_K}{2}$。）

**$\Delta_K$-限制能量**
$$
\mathcal{E}_2(S;\Delta_K):=\sum_{\delta\in\Delta_K}r_S(\delta)^2.
$$
恒有 $\mathcal{E}_2(S;\Delta_K)\le\mathcal{E}_2(S)$。

---

## L-AE-1（已证：整窗 $\Rightarrow$ 半窗点落入 $E_N$ 并形成 $\Delta_K$-团）

设 $N\in\mathcal{F}_0$、$K=\lfloor\log_2(N-1)\rfloor\ge 2$，且 $2^K<N\le 2^{K+1}$。令
$$
S_N:=\{N-2^a:a\in A_K\},\qquad
S_N^\circ:=S_N\cap I_N.
$$
则：

1. $S_N\subset E$，且 $|S_N^\circ|\ge M_K-1$。  
   （因 $a\le K\Rightarrow N-2^a\ge N-2^K\ge 1$；又 $a\le K-1\Rightarrow 2^a\le 2^{K-1}<N/2$（用 $N>2^K$），故 $N-2^a>N/2$。仅可能 $a=K$ 使 $N-2^K\le 2^K$ 落在 $I_N$ 外。）

2. 对 $a,b\in A_K$、$a<b$，无序对 $\{N-2^a,N-2^b\}$ 在 Cayley 图 $\mathrm{Cay}(\mathbb{Z},\Delta_K\cup(-\Delta_K))$ 中相邻（差的绝对值为 $|2^a-2^b|\in\Delta_K$）。故 $S_N^\circ$ 是大小 $\ge M_K-1$ 的 $\Delta_K$-平移团。

3. 引用 L-Ekill-A2-1：
   $$
   \mathcal{C}(E_N;\Delta_K)\ge\mathcal{C}(E\cap J_N;\Delta_K)\ge\binom{M_K}{2}.
   $$
   （$J_N\subset I_N$：由 $N>2^K$ 得 $N-2^K>0$，且 $N-2^{\lceil K/2\rceil}\le N-2^{K/2}<N$，而 $N-2^K>N/2$ 不必；相关求和的支撑点 $t=N-2^b$（$b\in A_K$）满足 $t\ge N-2^K$。若 $N-2^K<N/2$，则把 $\mathcal{C}$ 改在 $E\cap(J_N\cup I_N)$ 上计数；因团点几乎全在 $I_N$，至多损失 $O(K)$ 量级已含于 $\binom{M_K}{2}$ 的主项。严格写法：对 $b\le K-1$ 的对已全部落入 $E_N$，给出
   $$
   \mathcal{C}(E_N;\Delta_K)\ge\binom{M_K-1}{2}.
   $$
   下文一律用 $\gg K^2$ 下界。）

**证明.** (1)(2) 由 $N\in\mathcal{F}_0$ 与二进单调性直接验证。(3) 对每对 $\lceil K/2\rceil\le a<b\le K-1$ 取 $t=N-2^b\in I_N\cap E$，则 $t+(2^b-2^a)$ 调整序后与 $N-2^a\in E$ 配对，贡献 $1$；对数目 $\binom{M_K-1}{2}$。证毕。

**注.** $S_N$ 本身近 Sidon：二进唯一表示给出
$$
(N-2^{a})+(N-2^{b})=(N-2^{c})+(N-2^{d})\iff\{a,b\}=\{c,d\},
$$
故 $\mathcal{E}_2(S_N)\asymp M_K^2$。平移团**不**自动抬升 $S_N$ 的加性能量至 $M_K^{2+\delta}$。

---

## L-AE-2（已证：相关 $\to$ 限制能量的 Cauchy–Schwarz 链）

对任意有限 $S\subset\mathbb{Z}$ 与任意有限对称差集候选 $\Delta$，
$$
\mathcal{C}(S;\Delta)^2
=\Bigl(\sum_{\delta\in\Delta}r_S(\delta)\Bigr)^2
\le|\Delta|\sum_{\delta\in\Delta}r_S(\delta)^2
=|\Delta|\,\mathcal{E}_2(S;\Delta)
\le|\Delta|\,\mathcal{E}_2(S).
$$
特别地，取 $S=E_N$、$\Delta=\Delta_K$，并结合 L-AE-1：若 $N\in\mathcal{F}_0$，令 $\mathcal{C}_N:=\mathcal{C}(E_N;\Delta_K)\ge\binom{M_K-1}{2}$，则
\begin{align*}
\mathcal{C}_N^2
&\le|\Delta_K|\,\mathcal{E}_2(E_N;\Delta_K)
\le|\Delta_K|\,\mathcal{E}_2(E_N)
\le\binom{M_K}{2}\,\mathcal{E}_2(E_N).
\end{align*}
整理得**整窗能量下界**
$$
\mathcal{E}_2(E_N)\;\ge\;\mathcal{E}_2(E_N;\Delta_K)\;\ge\;\frac{\mathcal{C}_N^2}{|\Delta_K|}\;\ge\;\frac{\binom{M_K-1}{2}^2}{\binom{M_K}{2}}\;\gg\;K^2.
$$
（大 $K$ 时右端 $\ge(1-o(1))\mathcal{C}_N$。）若再设表示函数在 $\Delta_K$ 上「不均匀」——即存在 $\theta\in(0,1]$ 使
$$
\#\bigl\{\delta\in\Delta_K:r_{E_N}(\delta)\ge 1\bigr\}\le|\Delta_K|^{1-\theta},
$$
则同一链条加强为
$$
\mathcal{E}_2(E_N;\Delta_K)
\ge\frac{\mathcal{C}_N^2}{|\Delta_K|^{1-\theta}}
\gg K^{2+2\theta}.
$$

**证明.** Cauchy–Schwarz 即第一式；L-AE-1 给 $\mathcal{C}$ 下界；加强形把 $|\Delta|$ 换成有效支撑大小。证毕。

**锐性.** 当 $r_{E_N}\equiv 1$ 于 $\Delta_K$ 的全部元素上（恰由单一平移团实现）时，$|\mathrm{supp}\,r\cap\Delta_K|=|\Delta_K|$ 且 $\mathcal{E}_2(E_N;\Delta_K)=\binom{M_K}{2}\asymp K^2$，与 $\mathcal{E}_2\le M_N^{2+\varepsilon}$ 在 $M_N\ge K$ 时**相容**。故「仅 $\varepsilon$-近随机能量」不足以与整窗冲突——见缺口 AE-G1。

---

## L-AE-3（已证：近随机能量 $\Rightarrow$ 差表示的 $\ell^{2}$ 控制）

设 $\mathcal{E}_2(E_N)\le M_N^{2+\varepsilon}$。则：

1. $\displaystyle\sum_{d}r_{E_N}(d)^2\le M_N^{2+\varepsilon}$；
2. 对任意 $\Delta$，有 $\mathcal{E}_2(E_N;\Delta)\le M_N^{2+\varepsilon}$；
3. （流行差粗界）$\displaystyle\max_{d\neq 0}r_{E_N}(d)\le M_N^{1+\varepsilon/2}$（因 $r(d)^2\le\mathcal{E}_2$）；
4. （Hölder 相关上界）对任意 $\Delta$，
   $$
   \mathcal{C}(E_N;\Delta)
   \le|\Delta|^{1/2}\,M_N^{1+\varepsilon/2}.
   $$

**证明.** (1)(2) 定义；(3) 取单项；(4) 由 L-AE-2 的 CS 与 (2)。证毕。

**与整窗比较.** 整窗要求 $\mathcal{C}(E_N;\Delta_K)\ge\binom{M_K-1}{2}\asymp K^2$。L-AE-3(4) 给出
$$
K^2\ll\mathcal{C}\le|\Delta_K|^{1/2}M_N^{1+\varepsilon/2}\ll K\,M_N^{1+\varepsilon/2},
$$
即必要条件
$$
M_N\;\gg\;K^{1/(1+\varepsilon/2)}.
$$
此仅排除「半区间内例外极少」的情形；在 Roth 尺度 $M_N\ll N/(\log N)^{c}$ 下自动满足，**无**新的 E-kill。要得到与 $\binom{M_K}{2}$ 的真冲突，需比 CS 更强的输入（AE-G1 / AE-Corr / AE-Jump）。

---

## L-AE-4（条件式：近随机 + 相关亏缺 / 团–能量跃迁 $\Rightarrow\mathcal{F}_0$ 有限）

对 $0$-$1$ 值的 $r$（每个差至多一对），恒有 $\mathcal{E}_2(S;\Delta)=\mathcal{C}(S;\Delta)$。单一 $\Delta_K$-团恰实现该饱和，故「限制能量小于相关」对团嵌入**永假**。正确的条件式输入是下列二者之一。

### 4.1 假设 AE-Corr$_\eta$（近随机 $\Rightarrow$ 相关亏缺）

存在 $\varepsilon,\eta>0$、$N_0$，使对一切 $N\ge N_0$，只要 $\mathcal{E}_2(E_N)\le M_N^{2+\varepsilon}$，就有
$$
\mathcal{C}(E_N;\Delta_K)\le(1-\eta)\binom{M_K}{2}.
$$
（意图：近 Sidon 型例外集不能「几乎装下」整窗所需的 $\Delta_K$-对；对真实 $E$ 未证，且抽象上被 AE-G1 / L08 阻挡——故必须用 $\mathcal{R}_{4,3,2}$ 的补集结构。）

**结论.** AE-Corr$_\eta$ $\Rightarrow\mathcal{F}_0$ 有限。

**证明.** 若 $N\in\mathcal{F}_0$ 大，则 L-AE-1 给 $\mathcal{C}\ge\binom{M_K-1}{2}$，与 AE-Corr 在 $\eta$ 固定、$K$ 大时冲突。证毕。

### 4.2 假设 AE-Jump$_{\delta}$（团 $\Rightarrow$ 能量跃迁）

存在 $\delta>0$、$K_0$，使对一切 $K\ge K_0$ 与 $2^K<N\le 2^{K+1}$，只要 $|S_N^\circ|\ge(1-\tfrac12)M_K$（半窗团几乎完整），就有
$$
\mathcal{E}_2(E_N)\ge M_N^{2+\delta}.
$$
（意图：真实 $E$ 一旦含大 $\Delta_K$-团，则差表示在 $\Delta_K$ 外或团邻域内被迫成簇，把总能量从 Sidon 阶抬到 $M^{2+\delta}$。）

**结论.** AE-Jump$_{\delta}$ + AE-Rand$_\varepsilon$（$\varepsilon<\delta$）$\Rightarrow\mathcal{F}_0$ 有限。

**证明.** $N\in\mathcal{F}_0$ 大 $\Rightarrow$ 团假设成立 $\Rightarrow\mathcal{E}_2(E_N)\ge M_N^{2+\delta}$，与 AE-Rand$_\varepsilon$ 的 $\le M_N^{2+\varepsilon}$ 矛盾。证毕。

### 4.3 假设 AE-Super$_\eta$（相关大 $\Rightarrow$ 限制能量超饱和）

若 $\mathcal{C}(E_N;\Delta_K)\ge(1-\eta')\binom{M_K}{2}$，则
$$
\mathcal{E}_2(E_N;\Delta_K)\ge(1+\eta)\mathcal{C}(E_N;\Delta_K).
$$
（即不能以纯 $0$-$1$ 平坦实现近最大相关，必须出现 $r(\delta)\ge 2$ 的流行差。对含孤立团的集合为假；对真实 $E$ 若差分来自 $f(\mathbf{u})-f(\mathbf{v})$ 的多解则可期。）

与 L-AE-2 的 CS 下界 $\mathcal{E}_2\ge\mathcal{C}^2/|\Delta|$ 比较：整窗平坦时两者同阶 $\asymp\mathcal{C}$；超饱和要求严格大于平坦基线。

**结论.** AE-Super$_\eta$ $\Rightarrow$ 整窗不可能（与「整窗 $\Rightarrow$ 存在 $0$-$1$ 实现的团嵌入」冲突）$\Rightarrow\mathcal{F}_0$ 有限。

**注.** 4.1–4.3 均为 L-Ekill-A2-2 反相关准则的能量语言变体；对真实 $E$ 均未证。用户目标句「近随机 $\Rightarrow$ 不能撑整窗」的精确条件式落点是 **AE-Corr** 或 **AE-Jump + AE-Rand**。

---

## L-AE-5（条件式：Balog–Wooley 型二分接口）

**背景接口（引用，非本仓库新证）.** Balog–Wooley 型定理断言：对有限 $A\subset\mathbb{Z}$，存在绝对 $c>0$ 与大子集 $A'\subset A$，使得下列二者之一成立：

- **(Add)** 加性能量增益：$\mathcal{E}_2(A')\ge|A'|^{2+c}$；
- **(Mul)** 乘性能量增益：$\mathcal{E}_\times(A')\ge|A'|^{2+c}$（$\mathcal{E}_\times$ 为 $\#\{(a,b,c,d):ab=cd\}$）。

**本路线用法（条件式模板 AE-BW）.**

对 $A=E_N$ 施分：

| 枝 | 输出 | 接杀机制 |
|----|------|----------|
| Add 增益 | $\exists E'\subset E_N$，$\mathcal{E}_2(E')\ge|E'|^{2+c}$ | 交 L-AE-6（Sanders / BSG）得加性结构，再喂「结构片不撑整窗」假设 AE-Struct |
| Mul 增益 | $\exists E'\subset E_N$ 具乘性结构 | 乘性结构片与 $\mathcal{R}_{4,3,2}$ 的局部/模分布冲突（需另设 AE-Mul；本路线不展开） |
| 两枝皆弱 | 即全局近 $\varepsilon$-随机且近乘性随机 | 回到 L-AE-3/4：用 AE-Corr 或 AE-Jump+Rand 杀平移团 |

**条件结论.** AE-BW 二分可运行 + AE-Corr / AE-Jump（低能量枝）+ AE-Struct（高能量枝）$\Rightarrow\mathcal{F}_0$ 有限。

**缺口.** 真实 $E_N$ 上 BW 常数与「结构片 $\subset E$」的可表性均未验证；Mul 枝完全开放。

---

## L-AE-6（条件式：Sanders / 能量增量 $\Rightarrow$ 结构 $\Rightarrow$ 窗薄）

**假设 AE-High$_c$.** $\mathcal{E}_2(E_N)\ge M_N^{2+c}$。

**接口（Sanders / Bogolyubov–Ruzsa 型，引用模板）.**  
存在依赖 $c$ 的 $\kappa>0$，使 $E_N$ 含一个相对稠密的广义算术结构片 $P$（Bohr 集或秩 $\ll_c 1$ 的 GAP），满足
$$
|P\cap E_N|\ge M_N^{\kappa}.
$$

**假设 AE-Struct$_\theta$.**  
对一切充分大 $N$ 与一切由 AE-High 产出的结构片 $P\subset I_N$，
$$
\#\{1\le k\le K:N-2^k\in P\cap E\}\le C K^{\theta},\qquad\theta<1.
$$
（结构片不能提供完整二进窗；允许 $o(K)$ 个窗点落入结构例外。）

**引理.** AE-High$_c$ + Sanders 模板 + AE-Struct$_\theta$ $\Rightarrow$ 该 $N$ 不能满足 $\rho_E(N;K)=K$。对所有大 $N$ 若还并入低能量枝的 L-AE-4，则 $\mathcal{F}_0$ 有限。

**证明梗概.** 高能量 $\Rightarrow$ 结构片 $P$；AE-Struct 限制窗点落入 $P\cap E$ 的数量；完整窗要求 $K$ 个点全在 $E$，若能证明「窗点若在 $E$ 则倾向落入高能量结构片」（能量增量迭代把 $E_N$ 分解为结构片+低能量残差）并控制残差上的 $\Delta_K$-团（L-AE-4），则整窗不可能。证毕（条件式）。

**能量增量迭代图式**
$$
\begin{CD}
E_N @>{\mathcal{E}_2\ge M^{2+c}}>> P_1\subset E_N\text{（结构）}\\
@VV{\text{残差 }E^{(1)}=E_N\setminus P_1}V @VV{\text{AE-Struct}}V\\
E^{(1)} @>{\text{低能量或再增量}}>> \cdots @>>> \text{残差满足 AE-Rand}
 @>{\text{AE-Corr / Jump}}>> \text{无 }\Delta_K\text{-整团}.
\end{CD}
$$

---

## L-AE-7（已证：与 A2 / FW / Det 的正交关系——只登记不重复）

| 路线 | 整窗检测物 | 本路线是否复用证明 |
|------|------------|-------------------|
| A2 | $\mathcal{C}_E(J_N,K)\ge\binom{M_K}{2}$ | **引用** L-Ekill-A2-1 为 L-AE-1(3)；不重写证明 |
| FW | $|\Phi_N(\alpha)|$ 低频指纹 | **不**使用 $\Phi_N$；能量在物理空间 $I_N$ |
| Det | $\rho_E\le C K^{\theta}$ / 曲面空虚 | **不**使用行列式；仅在总图上与 L-Det-1 并列指向 L07 |

本路线新增量：把 A2 相关改写成 $\mathcal{E}_2(\,\cdot\,;\Delta_K)$ 链条，并接入 BW/Sanders 二分。

---

## L-AE-8（条件式总述：近随机能量路线的 E-kill 图式）

**目标图式（条件式；原猜想仍开放）**
$$
\begin{align*}
&\underbrace{\mathrm{AE\text{-}Rand}_\varepsilon}_{\mathcal{E}_2(E_N)\le M_N^{2+\varepsilon}}
+\underbrace{\mathrm{AE\text{-}Corr}_\eta\text{ 或 }\mathrm{AE\text{-}Jump}_\delta}_{\text{近随机$\Rightarrow$相关亏缺 / 团$\Rightarrow$能量跃迁}}\\
&\qquad\text{或}\qquad
\underbrace{\mathrm{AE\text{-}High}+\mathrm{Sanders}+\mathrm{AE\text{-}Struct}}_{\text{高能量结构枝}}\\
&\qquad\text{或}\qquad
\underbrace{\mathrm{AE\text{-}Super}_\eta}_{\text{大相关$\Rightarrow$限制能量超饱和}}\\
&\Longrightarrow\ \mathcal{F}_0\text{ 有限}
\ \stackrel{\mathrm{L07}}{\Longrightarrow}\
\text{$x=0$ 型充分大全体可表}.
\end{align*}
$$

**不可写为定理的部分.** AE-Corr、AE-Jump、AE-Super、AE-Struct、AE-Mul、真实 $E$ 上的 Sanders 常数；以及「AE-Rand 单独成立」——见 AE-G1 与 L08。

---

## 精确缺口登记

| 代号 | 内容 | 堵住则得 |
|------|------|----------|
| **AE-G1** | **平坦饱和.** $r\equiv 1$ 于 $\Delta_K$ 上使 $\mathcal{E}_2(\,\cdot\,;\Delta_K)=\mathcal{C}\asymp K^2$，与 $\mathcal{E}_2\le M^{2+\varepsilon}$（$M\ge K$）相容；单一 $\Delta_K$-团（二进近 Sidon）**不**抬升总能量。故「仅近随机能量 $\not\Rightarrow\mathcal{F}_0$ 有限」。抽象上与 L08 一致：可植入稀疏整窗族保持能量近极小。 | 必须 AE-Corr / AE-Jump 或更高阶 Gowers |
| **AE-G2** | **AE-Corr / AE-Jump / AE-Super 对真实 $E$.** 需证：近 Sidon 型真实例外集不能装下近完整 $\Delta_K$-团；或团迫使能量跃迁至 $M^{2+\delta}$；或大相关迫使 $r\ge 2$ 成簇。可能来源：$\mathcal{R}_{4,3,2}$ 的差分多解。 | L-AE-4 $\Rightarrow\mathcal{F}_0$ 有限 |
| **AE-G3** | **Sanders 模板均匀性.** 对 $E_N=E\cap[N/2,N]$，能量增量产出的 Bohr/GAP 参数需对 $N$ 均匀，且结构片落在 $I_N$ 内。 | 高能量枝可运行 |
| **AE-G4** | **AE-Struct$_\theta$.** 结构片与二进窗 $\{N-2^k\}$ 的交 $<K^{1-\delta}$；不能从抽象 Bohr 集形式推出（L08 可把窗种种入结构集）。必须用 $\mathcal{R}_{4,3,2}$ 在 AP/Bohr 上的正密度或圆法。 | 高能量枝闭合 |
| **AE-G5** | **BW 乘性枝 AE-Mul.** $E$ 的乘性结构与混合幂补集的相容性未建。 | 二分无漏枝 |
| **AE-G6** | **高阶模式.** 整窗是 $|A_K|$-齐性 $\Delta_K$-团，真检测物是高线性形 / Gowers $U^{s}$ 而非仅 $\mathcal{E}_2$；$\mathcal{E}_2$ 只控制 $2$-相关。 | 绕过 AE-G1 的替代路线 |

---

## 不等式链速查（可引用）

**链 A（已证，整窗 $\to$ 弱能量下界）**
$$
N\in\mathcal{F}_0
\ \Longrightarrow\
\mathcal{C}(E_N;\Delta_K)\ge\binom{M_K-1}{2}
\ \Longrightarrow\
\mathcal{E}_2(E_N;\Delta_K)\ge\frac{\mathcal{C}^2}{|\Delta_K|}\gg K^2
\ \Longrightarrow\
\mathcal{E}_2(E_N)\gg K^2.
$$

**链 B（已证，近随机 $\to$ 相关上界）**
$$
\mathcal{E}_2(E_N)\le M_N^{2+\varepsilon}
\ \Longrightarrow\
\mathcal{C}(E_N;\Delta_K)\le|\Delta_K|^{1/2}M_N^{1+\varepsilon/2}.
$$
（对整窗所需的 $\mathcal{C}\asymp K^2$ 仅强制 $M_N\gg K^{1/(1+\varepsilon/2)}$，在 Roth 尺度下无新信息。）

**链 C（条件式，Jump + Rand 杀窗）**
$$
\mathrm{AE\text{-}Jump}_\delta
+\mathrm{AE\text{-}Rand}_\varepsilon\ (\varepsilon<\delta)
+\bigl(N\in\mathcal{F}_0\bigr)
\ \Longrightarrow\
M_N^{2+\delta}\le\mathcal{E}_2(E_N)\le M_N^{2+\varepsilon}
\ \Longrightarrow\ \text{矛盾}
\ \Longrightarrow\ \mathcal{F}_0\text{ 有限}.
$$

**链 C′（条件式，Corr 杀窗）**
$$
\mathrm{AE\text{-}Corr}_\eta
+\bigl(N\in\mathcal{F}_0\bigr)
\ \Longrightarrow\
\binom{M_K-1}{2}\le\mathcal{C}\le(1-\eta)\binom{M_K}{2}
\ \Longrightarrow\ \text{矛盾（$K$ 大）}.
$$

**链 D（条件式，BW/Sanders 二分）**
$$
E_N
\ \xrightarrow{\mathrm{BW}}
\mathrm{Add}/\mathrm{Mul}
\ \xrightarrow{\mathrm{Sanders\ or\ AE\text{-}Mul}}
\mathrm{Struct}
\ \xrightarrow{\mathrm{AE\text{-}Struct}}
\rho_E<K
\ \xrightarrow{\mathrm{残差+Corr/Jump}}
\mathcal{F}_0\text{ 有限}.
$$

---

## 状态表

| 编号 | 状态 | 摘要 |
|------|------|------|
| L-AE-1 | 已证 | 整窗 $\Rightarrow$ $E_N$ 内 $\Delta_K$-团 + $\mathcal{C}\gg K^2$ |
| L-AE-2 | 已证 | $\mathcal{C}^2\le|\Delta|\,\mathcal{E}_2(\Delta)\le|\Delta|\,\mathcal{E}_2$；整窗 $\Rightarrow\mathcal{E}_2\gg K^2$ |
| L-AE-3 | 已证 | 近随机 $\Rightarrow$ $r$ 的 $\ell^2$/相关上界 |
| L-AE-4 | 条件式 | AE-Corr / AE-Jump+Rand / AE-Super $\Rightarrow\mathcal{F}_0$ 有限 |
| L-AE-5 | 条件式 | Balog–Wooley 二分接口 |
| L-AE-6 | 条件式 | Sanders 增量 + AE-Struct $\Rightarrow$ 高能量枝杀窗 |
| L-AE-7 | 已证（对照） | 与 A2/FW/Det 正交关系 |
| L-AE-8 | 条件式总述 | 全图式；原猜想开放 |

**本轮结论.** 已建立加性能量语言下的不等式链与 BW/Sanders 接口；**不能**由「$\mathcal{E}_2(E\cap I)\le|E\cap I|^{2+\varepsilon}$」单独推出 $\mathcal{F}_0$ 有限（AE-G1）。条件式闭合依赖 AE-Corr / AE-Jump / AE-Struct 等真实 $E$ 输入。原猜想保持开放。
