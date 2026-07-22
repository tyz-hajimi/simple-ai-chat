# L-Slowx：缓增 $x\le(\log N)^A$ 失败集（路线 R4-Slow-x）

> 路线 **R4-Slow-x**（P09 攻关轮次 4，服务 **P1**，旁路 **A4**＝对抗审查阻断「有界 $x$ 的 CS $\Rightarrow$ 几乎所有」）。  
> 允许四次项系数缓增 $x\le(\log N)^A$，定义失败集 $\mathcal{F}_A$，并与 $A=0$ 的 $\mathcal{F}_0$ 比较；登记 Roth / 结构假说下的密度结论，以及**已证**的计数下界/障碍。  
> **命名隔离：** 本路线代号 `R4-Slow-x`，**勿**与 Gap 文献中的记号 $R^{(2)}$（或任何二阶间隙残量）混淆。  
> **不**声称原猜想已证；禁止数值程序。

---

## 0. 符号

$$
\mathcal{S}=\{y^3+z^2:y,z\in\mathbb{N}_0\},
\qquad
\mathcal{R}_{4,3,2}=\{x^4+y^3+z^2:x,y,z\in\mathbb{N}_0\},
\qquad
E=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2}.
$$
对 $N\ge 2$ 令 $K(N)=\lfloor\log_2 N\rfloor$（下文常写 $K$）。对固定 $A\ge 0$ 定义**缓增失败集**
$$
\mathcal{F}_A
=\Bigl\{
N\ge 2:
\ \forall\,k\le\log_2 N,\ 
\forall\,x\in\mathbb{N}_0\text{ 且 }x\le(\log N)^A,\ 
\ N-2^k-x^4\notin\mathcal{S}
\Bigr\}.
$$
**约定：** $A=0$ 时取 $x\le(\log N)^0$ 理解为 **仅** $x=0$（纯零四次项切片），即
$$
\mathcal{F}_0
=\bigl\{N\ge 2:\ \forall\,k\le\log_2 N,\ N-2^k\notin\mathcal{S}\bigr\}.
$$
（若改用字面 $(\log N)^0=1$ 允许 $x\in\{0,1\}$，则所得集 $\subseteq\mathcal{F}_0$，下文单调与 $o(X)$ 差集结论不变。）

对照仓库既有 **E-kill 失败集**（勿混用）
$$
\mathcal{F}_0^{\mathrm{kill}}
=\{N\ge 2:W(N)\subseteq E\},
\qquad
W(N)=\{N-2^k:1\le k\le\lfloor\log_2(N-1)\rfloor\}.
$$
缓增可表集（全局，不计失败逻辑）
$$
\mathcal{R}_{\le L}
=\{x^4+y^3+z^2+2^k:x,y,z\in\mathbb{N}_0,\ k\in\mathbb{N}_0,\ x\le L\}.
$$
写 $L_A(X)=\lfloor(\log X)^A\rfloor$。

---

## L-Slowx-1（已证：$\mathcal{F}_A$ 与 $\mathcal{F}_0$ 的单调包含）

设 $0\le A\le A'<\infty$。则
$$
\mathcal{F}_{A'}\subseteq\mathcal{F}_A\subseteq\mathcal{F}_0.
$$
进而对一切 $A\ge 0$，
$$
\mathcal{F}_0^{\mathrm{kill}}\subseteq\mathcal{F}_A.
$$

**证明.**  
（单调）若 $N\in\mathcal{F}_{A'}$，则对一切 $k\le\log_2 N$ 与一切 $x\le(\log N)^{A'}$ 有 $N-2^k-x^4\notin\mathcal{S}$。因 $A\le A'$ 时 $\{x:x\le(\log N)^A\}\subseteq\{x:x\le(\log N)^{A'}\}$，故同一条件对 $x\le(\log N)^A$ 成立，即 $N\in\mathcal{F}_A$。  
若 $N\in\mathcal{F}_A$（任意 $A\ge 0$），取 $x=0\le(\log N)^A$，得 $\forall k,\ N-2^k\notin\mathcal{S}$，故 $N\in\mathcal{F}_0$。

（与 kill）若 $N\in\mathcal{F}_0^{\mathrm{kill}}$，则对窗内每个 $m=N-2^k$ 有 $m\notin\mathcal{R}_{4,3,2}$。但
$$
x^4+\mathcal{S}\subseteq\mathcal{R}_{4,3,2}
\qquad(x\in\mathbb{N}_0),
$$
故对一切 $x$ 有 $N-2^k-x^4\notin\mathcal{S}$，从而 $N\in\mathcal{F}_A$。证毕。

**定位.** $\mathcal{F}_A$ 随 $A$ **缩小**（失败更难）；它介于「纯 $x=0$ 失败」与「任意 $x$ 的 E-kill 失败」之间：
$$
\mathcal{F}_0^{\mathrm{kill}}
\subseteq\mathcal{F}_A
\subseteq\mathcal{F}_0.
$$

---

## L-Slowx-2（已证：CS 覆盖上界 — 缓增仍密度零）

对任意固定 $A\ge 0$ 与一切 $X\ge 3$，
$$
\bigl|\mathcal{R}_{\le L_A(X)}\cap[1,X]\bigr|
\ll
X^{5/6}\,(\log X)^{A+1}.
$$
特别地
$$
\bigl|\mathcal{R}_{\le L_A(X)}\cap[1,X]\bigr|=o(X).
$$

**证明.** 若 $n=x^4+y^3+z^2+2^k\le X$ 且 $x\le L_A(X)$，则 $s:=y^3+z^2\le X$，故
$$
0\le y\le X^{1/3},\qquad 0\le z\le X^{1/2},
$$
从而
$$
|\mathcal{S}\cap[1,X]|
\le\bigl(\lfloor X^{1/3}\rfloor+1\bigr)\bigl(\lfloor X^{1/2}\rfloor+1\bigr)
\ll X^{5/6}.
$$
对固定 $x,k$，集合 $x^4+\mathcal{S}+2^k$ 在 $[1,X]$ 内的点数 $\le|\mathcal{S}\cap[1,X]|$。  
$x$ 至多 $L_A(X)+1\ll(\log X)^A$ 个取值，$k$ 至多 $\lfloor\log_2 X\rfloor+1\ll\log X$ 个取值，故
$$
\bigl|\mathcal{R}_{\le L_A(X)}\cap[1,X]\bigr|
\ll(\log X)^A\cdot\log X\cdot X^{5/6}.
$$
证毕。

**推论（失败集上密度）.** 若 $N\le X$ 且 $N\notin\mathcal{F}_A$，则存在 $k\le\log_2 N$ 与 $x\le(\log N)^A\le L_A(X)$ 使 $N\in\mathcal{R}_{\le L_A(X)}$。因此
$$
\bigl|[1,X]\setminus\mathcal{F}_A\bigr|
\le
\bigl|\mathcal{R}_{\le L_A(X)}\cap[1,X]\bigr|
=o(X),
$$
即 $\mathcal{F}_A$ 在 $[1,X]$ 内的计数密度趋于 $1$。同理 $\mathcal{F}_0$ 亦然。

---

## L-Slowx-3（已证：$\mathcal{F}_A$ 相对 $\mathcal{F}_0$ **无**密度级缩小）

对任意固定 $A\ge 0$，
$$
\bigl|(\mathcal{F}_0\setminus\mathcal{F}_A)\cap[1,X]\bigr|
\ll X^{5/6}\,(\log X)^{A+1}=o(X).
$$
因此
$$
\frac{|\mathcal{F}_A\cap[1,X]|}{X}
=1-o(1)
=\frac{|\mathcal{F}_0\cap[1,X]|}{X}.
$$
换言之：虽有严格包含 $\mathcal{F}_A\subseteq\mathcal{F}_0$，在自然密度尺度上 $\mathcal{F}_A$ **并不**明显更小。

**证明.** 若 $N\in\mathcal{F}_0\setminus\mathcal{F}_A$，则 $\forall k,\ N-2^k\notin\mathcal{S}$，但存在某 $k$ 与某 $1\le x\le(\log N)^A$ 使 $N-2^k-x^4\in\mathcal{S}$。故
$$
N\in\mathcal{R}_{\le L_A(X)}\cap[1,X]
$$
（对 $N\le X$）。由 L-Slowx-2 即得计数 $o(X)$。密度断言由 L-Slowx-2 推论与本估计给出。证毕。

**与阻断 A4 的关系.** 对抗审查第 3 条否定「**有界** $x$ $\Rightarrow$ 几乎所有」。L-Slowx-2/3 表明：把有界换成**任意固定**缓增指数 $A$ 的 $(\log N)^A$，CS 上界仍是 $X^{5/6}(\log X)^{O(1)}=o(X)$，**同一阻断仍然有效**。旁路 A4 不能仅靠缓增 $x$ 越过「几乎所有」。

---

## L-Slowx-4（已证对照 + 条件式澄清：Roth / 结构假说下 $\mathcal{F}_A$ 是否更小）

### （A）Roth 型几乎所有（针对 $\mathcal{R}_{4,3,2}$，已采纳骨架）

由定理 B / Roth 型界 $|E\cap[1,X]|\ll X/(\log X)^{1/20}$：几乎所有整数属于 $\mathcal{R}_{4,3,2}$，从而（固定 $k=1$）几乎所有 $n\ge 2$ 属于 $\mathcal{R}_{4,3,2}+\{2\}$，亦即 $\mathcal{F}_0^{\mathrm{kill}}$ 密度为零。

**但：** 上述几乎所有使用的见证 $x$ 可大至 $\asymp n^{1/4}$。对缓增失败集，L-Slowx-2 已给出
$$
dens(\mathcal{F}_A)=1
$$
（上密度意义）。故 **Roth 不蕴涵** $\mathcal{F}_A$ 密度变小，更不蕴涵 $\mathcal{F}_A$ 有限。

### （B）结构假说 Struct-E⁺ / L-Ekill-Struct-1（条件式）

Struct-E⁺（或 L-Det-1 的 $\rho_E\le C K^{\theta}$）$\Rightarrow\mathcal{F}_0^{\mathrm{kill}}$ 有限（条件式，已登记）。由 L-Slowx-1 仅得
$$
\mathcal{F}_0^{\mathrm{kill}}\subseteq\mathcal{F}_A,
$$
**有限的小集**被更大的 $\mathcal{F}_A$ 包含；**不能**推出 $\mathcal{F}_A$ 有限，也不能推出 $dens(\mathcal{F}_A)<1$。

### （C）何种增长才「明显」打破障碍（已证阈值）

若允许 $x\le L(X)$ 且 $L(X)\ge X^{\delta}$，$\delta>0$ 固定，则 L-Slowx-2 的证明只给出
$$
\bigl|\mathcal{R}_{\le L(X)}\cap[1,X]\bigr|
\ll L(X)\,X^{5/6}\log X.
$$
当 $\delta>1/6$ 时右端 $\gg X$，上界失去 $o(X)$ 结论（方法失效，**不**自动得到几乎所有）。  
缓增 $L(X)=(\log X)^A$ 对应「$\delta=0$」，永远停在 $o(X)$ 区。

**结论.** 在 Roth / Struct-E⁺ 下，$\mathcal{F}_0^{\mathrm{kill}}$ 可变稀或有限，但 $\mathcal{F}_A$ **不**随之明显变小（密度仍为 $1$）。欲使缓增路线在密度上优于 $\mathcal{F}_0$，需要远超对数的 $x$-预算，或全新的结构输入（非本文件所证）。

---

## L-Slowx-5（已证计数：下界与障碍对照）

### （障碍，已证）

对每个固定 $A\ge 0$，
$$
\#\bigl(\mathcal{R}_{\le L_A(X)}\cap[1,X]\bigr)
\ll X^{5/6}(\log X)^{A+1}=o(X).
$$
（即 L-Slowx-2。）这是旁路 A4 的**主障碍**：缓增四次项不能把可表集抬到正比例。

### （下界，已证 — 相对 $A=0$ 无幂次增益）

记
$$
\mathcal{R}^{(0)}=\{y^3+z^2+2^k:y,z,k\in\mathbb{N}_0\}.
$$
则对一切 $L\ge 0$，
$$
\mathcal{R}^{(0)}\subseteq\mathcal{R}_{\le L},
$$
故
$$
\#\bigl(\mathcal{R}_{\le L}\cap[1,X]\bigr)
\ge
\#\bigl(\mathcal{R}^{(0)}\cap[1,X]\bigr).
$$
由 CS 弱结果（骨架已采纳）
$$
\#\bigl(\mathcal{R}\cap[1,X]\bigr)\gg_{\varepsilon}X^{5/6-\varepsilon}
$$
**不能**直接下放为 $\mathcal{R}_{\le L_A(X)}$ 的同阶下界（因 CS 弱允许 $x$ 大至 $X^{1/4}$）。  
对纯立方–平方切片，平凡上界与构造给出
$$
X^{1/2}\ll|\mathcal{S}\cap[1,X]|\ll X^{5/6}
$$
（下界取 $y=0$、$z\le X^{1/2}$）。加入 $O(\log X)$ 个二进平移至多再乘 $\log X$ 因子（重叠未除），因此
$$
\#\bigl(\mathcal{R}^{(0)}\cap[1,X]\bigr)
\gg X^{1/2},
$$
且
$$
\#\bigl(\mathcal{R}_{\le L_A(X)}\cap[1,X]\bigr)
\gg X^{1/2}.
$$
若进一步利用「固定 $x$ 的切片 $x^4+\mathcal{S}$ 在 $x\le L_A(X)$、$x^4\le X/2$ 时各自贡献 $\asymp|\mathcal{S}\cap[1,X/2]|$」，因缺乏已证的切片几乎不交，**不能**把下界乘上 $(\log X)^A$ 写成定理。故：

> **已证下界改进：无**（相对 $A=0$，缓增不提供可引用的额外幂次或额外正幂 $\log$ 因子下界）。  
> **已证障碍：有**（上界仍 $o(X)$，且 $|\mathcal{F}_0\setminus\mathcal{F}_A|=o(X)$）。

### （阈值锐性）

存在绝对常数 $c>0$，使若某一证明给出
$$
\#\bigl(\mathcal{R}_{\le L}\cap[1,X]\bigr)\ge cX
\qquad\bigl(L=L(X)\bigr),
$$
则必须 $L(X)\gg X^{1/6}/\mathrm{polylog}(X)$（否则与 L-Slowx-2 型估计矛盾）。对数缓增被排除在「正比例覆盖」之外。

---

## L-Slowx-6（条件式接口：何种假说才杀 $\mathcal{F}_A$）

**假设 Slowx-Win$_\theta$（$0\le\theta<1$）.** 存在 $C$ 使对一切大 $N$，
$$
\#\bigl\{k\le\log_2 N:
\exists\,x\le(\log N)^A\text{ 使 }N-2^k-x^4\in\mathcal{S}
\bigr\}
\ge K-C K^{\theta},
$$
其中 $K=\lfloor\log_2(N-1)\rfloor$（即缓增 $x$ 下窗内「未击中」至多 $O(K^{\theta})$）。

**结论（条件式）.** Slowx-Win$_\theta$ $\Rightarrow\mathcal{F}_A$ 有限。

**证明.** $N\in\mathcal{F}_A$ 时左端为 $0$。若 $K>C K^{\theta}$ 则矛盾。故此类 $N$ 的 $K$ 有界，$\mathcal{F}_A$ 有限。证毕。

**缺口 Slowx-G1.** Slowx-Win$_\theta$ 对真实 $\mathcal{S}$ **未证**；L-Slowx-2 表明平均意义下绝大多数 $N$ 的左端为 $0$，故该假设与 CS 平均图像冲突，除非 $A$ 随 $N$ 增长到超对数。本条件式仅作「与 L-Det-1 平行」的接口登记，**不是**可行闭合。

**缺口 Slowx-G2.** 欲修复 A4，需 $x$ 的多项式级预算或把问题退回无限制 $x$ 的 $\mathcal{F}_0^{\mathrm{kill}}$（既有 P1 主线）。缓增路线不构成对阻断「有界 $x$」的有效旁路。

---

## 结算

| 编号 | 状态 | 摘要 |
|------|------|------|
| L-Slowx-1 | 已证 | $\mathcal{F}_{A'}\subseteq\mathcal{F}_A\subseteq\mathcal{F}_0$；$\mathcal{F}_0^{\mathrm{kill}}\subseteq\mathcal{F}_A$ |
| L-Slowx-2 | 已证 | $|\mathcal{R}_{\le L_A(X)}\cap[1,X]|\ll X^{5/6}(\log X)^{A+1}=o(X)$ |
| L-Slowx-3 | 已证 | $|\mathcal{F}_0\setminus\mathcal{F}_A|=o(X)$；密度上 $\mathcal{F}_A$ 不更小 |
| L-Slowx-4 | 已证对照 | Roth/Struct 杀 $\mathcal{F}_0^{\mathrm{kill}}$ **不**杀 $\mathcal{F}_A$；需 $x\gg X^{1/6}$ 才越障 |
| L-Slowx-5 | 已证 | 障碍 $o(X)$；下界无缓增增益；正比例覆盖的 $L$-阈值 |
| L-Slowx-6 | 条件式 | Slowx-Win$_\theta\Rightarrow\mathcal{F}_A$ 有限（与平均图像冲突；缺口 G1–G2） |

**本轮结论.** $\mathcal{F}_A$ 集合论上小于 $\mathcal{F}_0$，但 CS 计数证明二者仅差 $o(X)$；Roth/结构假说不使 $\mathcal{F}_A$ 明显变稀。缓增 $x$ **不能**旁路「有界 $x\Rightarrow$ 几乎所有」阻断。原猜想保持开放；P1 仍应主攻 $\mathcal{F}_0^{\mathrm{kill}}$。
