# L-Diff-Eq：混合幂差分方程与 $E-E$ 约束累积

> 路线 **R3-Diff-Eq-Diophantine**（轮次 3，服务 P1）。角度：若 $N\in\mathcal{F}_0$，则窗点 $N-2^k$ 整窗落入 $E$，从而对许多 $k<\ell$ 有
> $$
> N-2^k\notin\mathcal{R}_{4,3,2},\qquad N-2^\ell\notin\mathcal{R}_{4,3,2},
> $$
> 且差分 $2^\ell-2^k=2^k(2^{\ell-k}-1)$ 落在差集 $E-E$ 中。对偶地，同一差分若落入 $\mathcal{R}-\mathcal{R}$，则对应丢番图方程
> $$
> \bigl(x_1^4+y_1^3+z_1^2\bigr)-\bigl(x_2^4+y_2^3+z_2^2\bigr)=2^a(2^b-1)
> $$
> 有非负整点。本文件登记：**固定 $a,b$ 时解数的已证上界**，以及 **「$\Delta_K$ 几乎全落在 $E-E$ 外 $\Rightarrow$ 与整窗矛盾」** 的条件式累积。
>
> **不**声称原猜想已证；含「假设 Diff-†」的条目为条件式。禁止数值程序。

## 符号

沿用
$$
\mathcal{R}_{4,3,2}=\{x^4+y^3+z^2:x,y,z\in\mathbb{N}_0\},
\qquad
E=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2},
$$
$$
W(N)=\{N-2^k:1\le k\le K\},\quad K=\lfloor\log_2(N-1)\rfloor,
\qquad
\mathcal{F}_0=\{N\ge 2:W(N)\subseteq E\}.
$$
写 $f(x,y,z)=x^4+y^3+z^2$。混合幂差集与例外差集
$$
\mathcal{R}-\mathcal{R}=\{f(\mathbf{u})-f(\mathbf{v}):\mathbf{u},\mathbf{v}\in\mathbb{N}_0^3\},
\qquad
E-E=\{e_1-e_2:e_1,e_2\in E\}.
$$
对 $a\ge 0$、$b\ge 1$ 记二进差分
$$
D(a,b)=2^a(2^b-1).
$$
（故 $k<\ell$ 时 $2^\ell-2^k=D(k,\ell-k)$。）箱
$$
B(X)=\bigl\{(x,y,z)\in\mathbb{N}_0^3:
x\le X^{1/4},\ y\le X^{1/3},\ z\le X^{1/2}\bigr\}.
$$
解数
$$
\mathcal{N}_D(X)=\#\bigl\{(\mathbf{u},\mathbf{v})\in B(X)^2:f(\mathbf{u})-f(\mathbf{v})=D\bigr\}.
$$
半窗指数集（与 L-Ekill-A2 一致）
$$
A_K=\bigl\{a:\lceil K/2\rceil\le a\le K\bigr\},\quad M_K=|A_K|,
$$
$$
\Delta_K=\bigl\{D(\alpha,\beta-\alpha):\alpha,\beta\in A_K,\ \alpha<\beta\bigr\}.
$$
对 $N$ 定义 $E-E$ 命中计数
$$
\kappa_E(N;K)=\#\bigl\{(\alpha,\beta)\in A_K\times A_K:\alpha<\beta,\ D(\alpha,\beta-\alpha)\in E-E\bigr\}.
$$

---

## L-Diff-1（已证：固定 $a,b$ 时箱内解数上界）

设整数 $a\ge 0$、$b\ge 1$ 固定，令 $D=D(a,b)$。则对一切 $X\ge 2$ 与一切 $\varepsilon>0$，
$$
\mathcal{N}_D(X)\ll_{a,b,\varepsilon} X^{7/6+\varepsilon}.
$$
更一般地，若仅假设 $|D|\le X$（$a,b$ 可随 $X$ 变化），则同一证明给出**对 $D$ 均匀**的界
$$
\mathcal{N}_D(X)\ll_{\varepsilon} X^{7/6+\varepsilon}.
$$

**证明.** 对每一组 $(x_1,x_2,y_1,y_2)$ 令
$$
D_z=D-(x_1^4-x_2^4)-(y_1^3-y_2^3).
$$
满足箱约束的四元组数目
$$
\ll X^{1/4}\cdot X^{1/4}\cdot X^{1/3}\cdot X^{1/3}=X^{7/6}.
$$

**情形 A：** $D_z\neq 0$。方程化为 $z_1^2-z_2^2=D_z$，即
$$
(z_1-z_2)(z_1+z_2)=D_z.
$$
$D_z$ 的因子对数 $\ll_{\varepsilon}|D_z|^{\varepsilon}$。每组同号因子至多决定一对非负 $(z_1,z_2)$（由 $z_1-z_2$ 与 $z_1+z_2$ 的和差反演，并要求二者同奇偶且非负）。在箱内 $|D_z|\ll X+|D|$；当 $|D|\le X$ 或 $a,b$ 固定时 $|D_z|\ll_{a,b} X$，故每组四元组贡献 $\ll_{\varepsilon} X^{\varepsilon}$ 个 $z$-解。于是本情形
$$
\ll_{\varepsilon} X^{7/6+\varepsilon}.
$$

**情形 B：** $D_z=0$。则 $z_1=z_2$（非负），且
$$
x_1^4-x_2^4+y_1^3-y_2^3=D.
$$
自由变量 $z_1\le X^{1/2}$ 贡献因子 $\ll X^{1/2}$。对固定 $(y_1,y_2)$ 令 $D_x=D-(y_1^3-y_2^3)$。

- 若 $D_x\neq 0$：方程 $x_1^4-x_2^4=D_x$ 经
  $$
  x_1^4-x_2^4=(x_1-x_2)(x_1+x_2)(x_1^2+x_2^2)
  $$
  的因子分解，非负整数解数 $\ll_{\varepsilon}|D_x|^{\varepsilon}\ll_{\varepsilon} X^{\varepsilon}$（与箱相交后仍然）。对 $(y_1,y_2)$ 求和得
  $$
  \ll_{\varepsilon} X^{2/3}\cdot X^{\varepsilon}.
  $$
  再乘 $z$-自由因子：$\ll_{\varepsilon} X^{1/2+2/3+\varepsilon}=X^{7/6+\varepsilon}$。

- 若 $D_x=0$：则 $x_1=x_2$，$y_1^3-y_2^3=D$。差立方的因子分解给出 $(y_1,y_2)$ 至多 $\ll_{\varepsilon}|D|^{\varepsilon}$ 解；$x_1\le X^{1/4}$ 自由。贡献
  $$
  \ll_{\varepsilon}|D|^{\varepsilon}\,X^{1/4}\cdot X^{1/2}=|D|^{\varepsilon} X^{3/4}.
  $$
  在 $|D|\le X$ 或 $a,b$ 固定时吸收为 $\ll_{\varepsilon} X^{3/4+\varepsilon}$。

合并情形 A、B 即得断言。证毕。

**定位.** 这是对丢番图方程在各向异性箱 $B(X)$ 内的**多项式型**解数上界（指数 $7/6=1.1\overline{6}$，相对平凡 $|B(X)|^2\asymp X^{13/6}$ 节省 $X$）。固定 $a,b$ 时常数可依赖 $D$；窗应用取 $|D|\le N\asymp X$ 时用均匀版。**不**直接给出 $D\notin\mathcal{R}-\mathcal{R}$，也**不**单独推出 $\mathcal{F}_0$ 有限（对照 L08）。

---

## L-Diff-2（已证：退化切片的 $\tau$-型精细界）

保持 $D=D(a,b)$ 固定。将 $\mathcal{N}_D(X)$ 按「主导抵消」分层：

1. **纯平方差**（$x_1=x_2$，$y_1=y_2$）：$z_1^2-z_2^2=D$，解数
   $$
   \ll \tau(|D|)\,X^{1/4+1/3}\ll_{\varepsilon}|D|^{\varepsilon} X^{7/12}.
   $$
2. **纯立方差**（$x_1=x_2$，$z_1=z_2$）：$y_1^3-y_2^3=D$，解数
   $$
   \ll_{\varepsilon}|D|^{\varepsilon} X^{1/4+1/2}=|D|^{\varepsilon} X^{3/4}.
   $$
3. **纯四次差**（$y_1=y_2$，$z_1=z_2$）：$x_1^4-x_2^4=D$，解数
   $$
   \ll_{\varepsilon}|D|^{\varepsilon} X^{1/3+1/2}=|D|^{\varepsilon} X^{5/6}.
   $$

**证明.** 各款均由 $u^n-v^n=D$（$n\in\{2,3,4\}$）的标准因子分解：因子对数 $\ll_{\varepsilon}|D|^{\varepsilon}$，其余两个坐标在箱中自由。证毕。

**解读.** 退化族至多 $X^{5/6+\varepsilon}$（四次差主导）；L-Diff-1 的 $X^{7/6+\varepsilon}$ 来自「$x,y$ 均动、$z$ 由因子锁定」的主项。若未来对非退化差曲面施以 Det-G5 / 行列式，期望把总指数压到 $1$ 以下，与窗对数尺度 $K\asymp\log X$ 对接。

---

## L-Diff-3（已证：整窗 $\Rightarrow$ 二进差分整落入 $E-E$）

若 $N\in\mathcal{F}_0$，$K=\lfloor\log_2(N-1)\rfloor$，则对一切满足 $\lceil K/2\rceil\le k<\ell\le K$ 的整数 $k,\ell$，
$$
D(k,\ell-k)=2^\ell-2^k\in E-E,
$$
从而
$$
\kappa_E(N;K)=\binom{M_K}{2}.
$$
等价表述：整窗迫使差集 $\Delta_K$ 在「有序对计数」意义下被 $E-E$ **完全吞噬**。

**证明.** $N\in\mathcal{F}_0$ 给出 $N-2^k,N-2^\ell\in E$。取 $e_1=N-2^k$、$e_2=N-2^\ell$，则
$$
e_1-e_2=2^\ell-2^k=D(k,\ell-k)\in E-E.
$$
对 $A_K$ 内每对 $\alpha<\beta$ 计一次，即得 $\kappa_E=\binom{M_K}{2}$。此即 L-Ekill-A2-1 的差集改写。证毕。

**与 $\mathcal{R}-\mathcal{R}$ 的对照.** 同一差分 $D(k,\ell-k)$ **可以**同时属于 $\mathcal{R}-\mathcal{R}$（L-Diff-1 允许有解）与 $E-E$；二者并非互补。整窗约束的是 $E-E$ 侧的累积，而非「不能写成两混合幂之差」。后者是 $\mathcal{R}-\mathcal{R}$ 的否定，服务的是「两窗点不能同时可表」的独立集障碍，方向与 E-kill 相反（见下节缺口）。

---

## L-Diff-4（条件式：差分集几乎全落在 $E-E$ 外 $\Rightarrow\mathcal{F}_0$ 有限）

**假设 Diff-Out$_\eta$（$\eta\in(0,1]$）.** 存在 $K_0$ 使对一切 $K\ge K_0$ 与一切满足 $2^K<N\le 2^{K+1}$ 的 $N$，
$$
\kappa_E(N;K)\le(1-\eta)\binom{M_K}{2}.
$$
即：半窗二进差分集中，落在 $E-E$ 内的有序对至多占 $(1-\eta)$ 比例——**几乎（正比例）全落在 $E-E$ 外**。

**结论.** $\mathcal{F}_0$ 有限。再由 L07，得 $x=0$ 型充分大全体可表。

**证明.** 若存在任意大的 $N\in\mathcal{F}_0$，取 $K=\lfloor\log_2(N-1)\rfloor\to\infty$，则 L-Diff-3 给出 $\kappa_E(N;K)=\binom{M_K}{2}$，与 Diff-Out$_\eta$ 矛盾。故此类 $N$ 的 $K$ 有界，$\mathcal{F}_0$ 有限。L07 同上。证毕。

**等价表述（集合语言）.** 令
$$
\Delta_K^{\mathrm{out}}(N)=\bigl\{D(\alpha,\beta-\alpha):\alpha<\beta\in A_K,\ D(\alpha,\beta-\alpha)\notin E-E\bigr\}
$$
（按有序对计重时与 $\binom{M_K}{2}-\kappa_E$ 一致）。Diff-Out$_\eta$ 即
$$
\binom{M_K}{2}-\kappa_E(N;K)\ge\eta\binom{M_K}{2},
$$
「$\Delta_K$ 的正比例部分落在 $E-E$ 外」。L-Diff-3 说整窗时该外集必须空；故外集正比例 $\Rightarrow$ 无整窗。

**缺口 Diff-G1.** 对**真实** $E$，Diff-Out$_\eta$ 未证。L08 表明存在密度零的抽象例外集使 $\mathcal{F}_0$ 无限，此时 $\kappa_E=\binom{M_K}{2}$ 对无限多 $N$ 成立，故 Diff-Out 必须使用 $\mathcal{R}_{4,3,2}$ 的算术结构（不能只靠密度）。

---

## L-Diff-5（条件式：由差分方程解数控制 $E-E$ 吞噬 —— 累积接口）

欲从 L-Diff-1 类上界走向 Diff-Out，需把「方程有解」与「窗差落入 $E-E$」联结。定义指示

$$
\mathbf{1}_{\mathcal{R}-\mathcal{R}}(D)=1\iff \mathcal{N}_D(C N)>0
\quad\text{（某绝对常数 $C$，箱盖住 $[0,N]$ 级混合幂）}.
$$

**假设 Diff-Link.** 存在 $\eta>0$、$K_0$，使对 $K\ge K_0$、$2^K<N\le 2^{K+1}$，
$$
\#\bigl\{(\alpha,\beta)\in A_K^2:\alpha<\beta,\
D(\alpha,\beta-\alpha)\in(E-E)\cap(\mathcal{R}-\mathcal{R})\bigr\}
\le(1-\eta)\binom{M_K}{2}.
$$
（直观：即便二进差分可写成混合幂之差，真实 $E$ 仍不能让太多这样的差分同时来自**同一**整窗的两个例外点。）

**条件结论.** Diff-Link $\Rightarrow$ Diff-Out$_\eta$（因 $(E-E)\cap(\mathcal{R}-\mathcal{R})\subset E-E$，更强的计上界推出较弱的 $\kappa_E$ 上界）$\stackrel{\mathrm{L\text{-}Diff\text{-}4}}{\Rightarrow}\mathcal{F}_0$ 有限。

**另一路径 Diff-Thin$_E$.** 若真实 $E$ 满足差集稀疏
$$
\#\bigl((E-E)\cap[1,2^K]\bigr)=o\bigl(K^2\bigr)
\quad(K\to\infty),
$$
则因 $|\Delta_K|\asymp M_K^2\asymp K^2$，对大 $K$ 自动有正比例的 $\Delta_K$ 落在 $E-E$ 外，即 Diff-Out$_\eta$，从而 $\mathcal{F}_0$ 有限。

**缺口 Diff-G2.** Diff-Thin$_E$ 对真实 $E$ 未知；薄集亦可有厚差集（加法组合论）。L-Diff-1 控制的是纤维 $\mathcal{N}_D(X)$（每个固定 $D$ 的表示数），**不是** $|(\mathcal{R}-\mathcal{R})\cap\Delta_K|$ 的下界，也**不是** $|(E-E)\cap\Delta_K|$ 的上界。缺口是：从单差分方程的解数上界，升级到差族 $\{\Delta_K\}$ 上的一致反相关 / 非吞噬。

**缺口 Diff-G3（与 Det-G5 接口）.** 对联立族
$$
f(\mathbf{u}_{ij})-f(\mathbf{v}_{ij})=D(\alpha_i,\beta_j-\alpha_i)
$$
施以多水平行列式（Det-G5），若能证明「过多对 $(\alpha,\beta)$ 同时满足 $N-2^\alpha,N-2^\beta\in E$」与箱体积不相容，则直接验证 Diff-Out 或 Diff-Link。此估计尚未建立。

---

## 约束如何累积（路线图）

| 步骤 | 内容 | 状态 |
|------|------|------|
| 单差分上界 | 固定 $D=D(a,b)$：$\mathcal{N}_D(X)\ll_{\varepsilon} X^{7/6+\varepsilon}$ | **已证** L-Diff-1/2 |
| 整窗 $\Rightarrow$ 全吞噬 | $N\in\mathcal{F}_0\Rightarrow\kappa_E=\binom{M_K}{2}$ | **已证** L-Diff-3（=A2-1 改写） |
| 正比例外逃 $\Rightarrow$ E-kill | Diff-Out$_\eta\Rightarrow\mathcal{F}_0$ 有限 | **条件式** L-Diff-4（蕴含已证） |
| 方程解数 $\to$ 差族反吞噬 | Diff-Link / Diff-Thin$_E$ / Det-G5 | **未证** Diff-G1–G3 |

总判：
$$
\mathrm{Diff\text{-}Out}_\eta
\ \stackrel{\mathrm{L\text{-}Diff\text{-}4}}{\Longrightarrow}\
\mathcal{F}_0\text{ 有限}
\ \stackrel{\mathrm{L07}}{\Longrightarrow}\
x=0\text{ 型充分大全体可表}.
$$
已证块是「单 $D$ 解数」+「整窗的 $E-E$ 全吞噬恒等式」；E-kill 的增量在于对真实 $E$ 验证 Diff-Out（或更强的 Diff-Link / Diff-Thin$_E$）。

---

## 与既有 P1 引理的关系

- **L-Ekill-A2**：L-Diff-3/4 是 A2-1/A2-2 的差集–丢番图语言改写；本路线把「相关和 $\mathcal{C}_E$」换成 $\kappa_E$ 与方程 $f(\mathbf{u})-f(\mathbf{v})=D(a,b)$。
- **L-Det-Surface / Det-G5**：差分超曲面正是 L-Diff 的几何载体；L-Diff-1 的初等 $7/6$ 是 Det 升级前的可引用基线。
- **L-Ekill-Struct / FW**：Diff-Thin$_E$ 与结构稀疏、低频均匀性平行，同属「真实 $E$ 不能整窗相关」族。
- **不**替代 P2 假设 H；本路线纯属 P1。

---

## 状态一览

| 编号 | 状态 | 备注 |
|------|------|------|
| L-Diff-1 | 已证 | 固定 / 均匀 $D$：$\mathcal{N}_D(X)\ll_{\varepsilon} X^{7/6+\varepsilon}$ |
| L-Diff-2 | 已证 | 退化切片 $\tau(D)$ 型；最劣 $X^{5/6+\varepsilon}$ |
| L-Diff-3 | 已证 | 整窗 $\Rightarrow\Delta_K$ 全落入 $E-E$（$\kappa_E$ 饱和） |
| L-Diff-4 | 条件式 | Diff-Out$_\eta\Rightarrow\mathcal{F}_0$ 有限（「差集落 $E-E$ 外则矛盾」） |
| L-Diff-5 | 条件式 | Diff-Link / Diff-Thin$_E$；缺口 Diff-G1–G3 |

**原猜想（含 $x>0$）仍开放。**
