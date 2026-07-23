# 严格证明稿：四个无条件/条件定理（第 11 轮，经对抗审查）

> 变量均取 $\mathbb N_0=\{0,1,2,\dots\}$（Sun 设定）。$R=\{x^4+y^3+z^2\}$，$r,r_{4,3}$ 表示数，$E=\mathbb N_0\setminus R$，$\mathcal F_0=\{N:\forall k\le\log_2 N,\ N-2^k\in E\}$（=Sun 例外集）。公式 `$...$` / `$$...$$`。

## 定理 A（加性能量，无条件，初等）
$$T(X)=\sum_{n\le X}r_{4,3}(n)^2\asymp X^{7/12}.$$
**证.** $T(X)=\#\{(x_1,y_1,x_2,y_2)\in\mathbb N_0^4:x_1^4+y_1^3=x_2^4+y_2^3\le X\}$。
- 对角 $(x_1,y_1)=(x_2,y_2)$：$=\#\{x^4+y^3\le X\}\asymp X^{1/4}X^{1/3}=X^{7/12}$。
- **引理 A**：$D\ne0$ 时 $\#\{(x_1,x_2)\in\mathbb N_0^2:x_1^4-x_2^4=D\}\ll_\varepsilon|D|^\varepsilon$。证：设 $e=x_1-x_2\mid D$，$s=x_1+x_2$，则 $s(s^2+e^2)=2D/e$，左端关于 $s$ 严增，至多一根；对 $e\mid D$ 求和，$\tau(|D|)\ll|D|^\varepsilon$。
- **引理 B**：$D\ne0$ 时 $\#\{(y_1,y_2):y_1^3-y_2^3=D\}\ll_\varepsilon|D|^\varepsilon$。证：$k=y_1-y_2\mid D$，$3y_2^2+3ky_2+k^2=D/k$ 二次至多两根。
- Off-diagonal：$D=x_1^4-x_2^4=y_2^3-y_1^3\ne0$。**因 $y\ge0$**，$x_i^4\le X$ 故 $\ll X^{1/2}$ 对 $(x_1,x_2)$，$|D|\le X$；引理 B 给每对 $\ll X^\varepsilon$，故 off-diag $\ll X^{1/2+\varepsilon}=o(X^{7/12})$。
⟹ $T(X)\asymp X^{7/12}$。$\square$（**关键**：非负性保证 $|D|\le X$ 与 $X^{1/2}$ 计数；负 $y$ 会失效。）

## 定理 B（$R$ 密度，无条件，初等）
$$|R\cap[1,X]|\gg_\varepsilon X^{1-\varepsilon}.$$
**证.** (i) $\sum_{n\le X}r(n)=\#\{x^4+y^3+z^2\le X\}\asymp X^{13/12}$（非负箱体）。 (ii) $C(0;X)=\sum r(n)^2=\#\{6\text{ 变量相等}\le X\}$，按 $D=(x_2^4+y_2^3)-(x_1^4+y_1^3)$ 分：$D\ne0$ 给 $z_1^2-z_2^2=D$，除数界 $\ll X^\varepsilon$/tuple、tuple 数 $\ll X^{7/6}$ ⟹ $X^{7/6+\varepsilon}$；$D=0$ 给 $\ll X^{1/2}\cdot T(X)=X^{13/12}$。故 $C(0;X)\ll X^{7/6+\varepsilon}$。 (iii) Cauchy–Schwarz：$|R\cap[1,X]|\ge(\sum r)^2/\sum r^2\gg X^{13/6-7/6-\varepsilon}=X^{1-\varepsilon}$。$\square$（弱于 Roth 密度 1，但纯初等无圆法。）

## 定理 C（局部因子，订正）
$$\boxed{\sigma_p(m)=1+O(p^{-1/2})\ \text{(严格)};\quad 1+O(p^{-1})\ \text{(条件于二维 Deligne)}.}$$
**证/状态.** $A(p)=p^{-2}N_p(m)-1$，$N_p(m)=p^2+S$，$S=\sum_{x,y\bmod p}\big(\tfrac{m-x^4-y^3}{p}\big)$。
- **严格**：按 $x$ 纤维化，$\sum_y\big(\tfrac{c-y^3}{p}\big)\ll\sqrt p$（Hasse，椭圆曲线 $w^2=c-y^3$），求和 $|S|\ll p\cdot\sqrt p=p^{3/2}$；等价曲面 Lang–Weil $N_p=p^2+O(p^{3/2})$。⟹ $\sigma_p=1+O(p^{-1/2})$（经典）。
- **条件**：$|S|\ll p$（即 $\sum_x a_p(E_{m-x^4})\ll p$，椭圆曲线族的 Frobenius 迹相消）须**二维 Deligne**、且须处理首项 $-x^4$ 的退化——很可能真，**本稿未证**。⟹ $O(p^{-1})$ 待定。
**影响**：一致 $\inf_m\mathfrak S>0$ 与 G-SS 的 $(\log n)^{1-o(1)}$ 强化**依赖**上述条件二维 Deligne，非无条件。

## 定理 D（Sun 例外集，无条件）
$$|\mathcal F_0\cap[1,X]|\ll_\varepsilon X^{13/14+\varepsilon}.$$
**证.** $N\in\mathcal F_0\Rightarrow N-2\in E$（$k=1$）；单射 $N\mapsto N-2$；引 Brüdern(1991) $|E\cap[1,X]|\ll X^{13/14+\varepsilon}$。$\square$
> **注（待核实）**：Brüdern 对 $x^2+y^3+z^4$ 的确切指数可能是 $11/14$（更强）；若是则 $|\mathcal F_0|\ll X^{11/14+\varepsilon}$。文献指数需最终核对。

## 定理 T-BDH（条件，新）
若 $E$ 满足 Barban–Davenport–Halberstam 型 level-of-distribution 于 $\vartheta>1/14$（即 $\sum_{q\le X^\vartheta}\sum_a(E(X;q,a)-|E|/q)^2\ll|E|X^\vartheta X^\varepsilon$），则经 Linnik 色散得配对相关 $\Psi(2;X)\ll|E|^2/X=X^{2\cdot13/14-1+\varepsilon}=X^{6/7+\varepsilon}$，从而
$$|\mathcal F_0\cap[1,X]|\ll X^{6/7+\varepsilon}\quad(\text{击败 }X^{13/14}).$$
**缺口**：该 BDH 本身是对混合形式例外集的二阶矩定理，属 shifted-convolution 同难度档；AP 的**线性**均匀性**不**自动给**双线性**配对相关（类比 BV 推不出孪生素数）。
