# L-Det-Surface：Bombieri–Pila / Heath-Brown 行列式法与二进窗薄性

> 路线 **R1-Det-Surface**（轮次 1）。目标：把真实例外集
> $$
> E=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2},\qquad
> \mathcal{R}_{4,3,2}=\{x^4+y^3+z^2:x,y,z\in\mathbb{N}_0\}
> $$
> 在二进窗上的「薄性」写成条件式上界，并精确登记行列式估计缺口。
> **不**声称原猜想已证；下列含「假设 Det-†」的条目均为条件式。

## 符号

固定 $N\ge 3$，令 $K=\lfloor\log_2(N-1)\rfloor$，二进窗
$$
W(N)=\{N-2^k:1\le k\le K\}.
$$
失败集 $\mathcal{F}_0=\{N\ge 2:W(N)\subseteq E\}$。窗内例外计数
$$
\rho_E(N;K)=\#\{1\le k\le K:N-2^k\in E\},
\qquad
\rho_{\mathcal{R}}(N;K)=K-\rho_E(N;K).
$$
对 $m\in\mathbb{N}_0$ 写仿射曲面（混合次数）
$$
S_m:\quad X^4+Y^3+Z^2=m\subset\mathbb{A}^3,
$$
以及箱
$$
B(m)=\bigl\{(x,y,z)\in\mathbb{N}_0^3:
x\le m^{1/4},\ y\le m^{1/3},\ z\le m^{1/2}\bigr\}
$$
（约定 $m=0$ 时箱为 $\{(0,0,0)\}$）。纤维计数
$$
r(m)=\#\bigl(S_m(\mathbb{Z})\cap B(m)\bigr).
$$
故 $m\in E\iff r(m)=0$（在非负箱约定下；$m$ 充分大时与 $\mathbb{Z}$ 点是否存在一致到可忽略的符号变体，下文一律用非负箱）。

关联三维超曲面（$N$ 固定）
$$
\mathcal{V}_N:\quad X^4+Y^3+Z^2+W=N\subset\mathbb{A}^4.
$$
窗点 $N-2^k\in\mathcal{R}_{4,3,2}$ 当且仅当存在 $(x,y,z)\in B(N-2^k)$ 使 $(x,y,z,2^k)\in\mathcal{V}_N(\mathbb{Z})$。

---

## L-Det-1（已证：$\theta$-薄窗 $\Rightarrow$ E-kill $\Rightarrow$ L07）

设存在 $\theta<1$、$K_0$、$C$ 使对一切 $K\ge K_0$ 与一切满足 $2^K<N\le 2^{K+1}$ 的 $N$，
$$
\rho_E(N;K)\le C\,K^{\theta}.
$$
则 $\mathcal{F}_0$ 有限。再由 L07，得 **$x=0$ 型充分大全体可表**。

**证明.** 若 $N\in\mathcal{F}_0$ 且 $K=\lfloor\log_2(N-1)\rfloor$，则 $\rho_E(N;K)=K$。当 $K\ge K_0$ 且 $K>C K^{\theta}$ 时矛盾。故此类 $N$ 的 $K$ 有界，从而 $\mathcal{F}_0$ 有限。L07 给出 $x=0$ 型充分大全体可表。证毕。

**定位.** 该结论推进 E-kill-1；相对原猜想（允许 $x>0$ 的四次项参与表示）仍是较弱的窗口型归约产物，**不得**写成原猜想已证。

---

## L-Det-2（已证：整窗的多曲面空虚表述）

若 $N\in\mathcal{F}_0$、$K=\lfloor\log_2(N-1)\rfloor$，则对每一个 $1\le k\le K$ 曲面 $S_{N-2^k}$ 在箱 $B(N-2^k)$ 内无非负整点：
$$
r(N-2^k)=0\qquad(1\le k\le K).
$$
等价地，$\mathcal{V}_N$ 上不存在满足 $W=2^k$（$1\le k\le K$）的非负整点。

**证明.** 由 $\mathcal{F}_0$ 与 $E$ 的定义即得。证毕。

**解读（本路线几何语言）.** 「整窗落入 $E$」= 对数多张水平曲面 $\{S_{N-2^k}\}_{k\le K}$ **同时空虚**。对偶地，若能证明在 $\mathcal{V}_N$ 的二进切片上整点「过度集中」于过少的 $W$-纤维不可能与箱体积相容，则强制 $\rho_{\mathcal{R}}(N;K)\ge K-C K^{\theta}$，即 L-Det-1 的假设。

---

## L-Det-3（条件式：单纤维行列式上界 $\Rightarrow$ 全局图像大）

**假设 Det-Fib.** 存在 $\delta\in[0,1)$ 与 $C_{\varepsilon}$ 使对一切充分大 $m$ 与一切 $\varepsilon>0$，
$$
r(m)\le C_{\varepsilon}\,m^{\delta+\varepsilon}.
$$
（典型期望：Heath-Brown / Salberger 型给出 $\delta=0$ 的 $m^{\varepsilon}$ 界，或至少 $\delta$ 足够小。）

则对充分大 $X$，令
$$
R_{\max}(X)=\max_{0\le m\le X} r(m)\ll_{\varepsilon} X^{\delta+\varepsilon}.
$$
满足 $x^4+y^3+z^2\le X$ 的非负整点数目 $\asymp X^{13/12}$，故
$$
\bigl|\mathcal{R}_{4,3,2}\cap[1,X]\bigr|
\ge\min\Bigl(X,\ c\,\frac{X^{13/12}}{R_{\max}(X)}\Bigr)
\gg_{\varepsilon}\min\bigl(X,\ X^{13/12-\delta-\varepsilon}\bigr).
$$
若 $\delta<1/12$，该下界触及平凡顶 $X$（与「平均纤维 $\asymp X^{1/12}$」相容，说明此时 Det-Fib 已强到逼近全覆盖）。无论如何，**仅由 Det-Fib 推出的是全局图像下界**，与 Roth 型几乎所有同级或更弱，**不足以**杀 $\mathcal{F}_0$（L08）。

**缺口指针.** 见 §缺口 Det-G1、Det-G2。

---

## L-Det-4（条件式：窗上「反过度集中」假设 $\Rightarrow\theta$-薄）

把窗可表写成 $\mathcal{V}_N$ 上二进纤维的占据。令
$$
\Pi_2(N;K)=\bigl\{(x,y,z,k)\in\mathbb{N}_0^3\times\{1,\ldots,K\}:
x^4+y^3+z^2=N-2^k\bigr\},
$$
投影 $\pi_W(\Pi_2)=\{k:\exists(x,y,z)\ (x,y,z,k)\in\Pi_2\}$，故 $|\pi_W(\Pi_2)|=\rho_{\mathcal{R}}(N;K)$。

几何解读：若 $\rho_E$ 大（许多窗点在 $E$），则 $\pi_W$ 小，即箱内本可分散到 $\asymp K$ 张水平面 $S_{N-2^k}$ 上的整点被强制集中到过少的 $W$-纤维——是为「过度集中」。行列式法限制单纤维 $r(m)$；要得到反集中（$\rho_{\mathcal{R}}$ 大），还需占据下界。

**假设 Det-Win′（窗薄，强形式）.** 存在 $\theta<1$、$C$、$N_0$ 使当 $N\ge N_0$、$K=\lfloor\log_2(N-1)\rfloor$ 时
$$
\rho_E(N;K)\le C K^{\theta}
\qquad\bigl(\Leftrightarrow\ \rho_{\mathcal{R}}(N;K)\ge K-C K^{\theta}\bigr).
$$
则由 L-Det-1 得 $\mathcal{F}_0$ 有限，并由 L07 得 $x=0$ 型充分大全体可表。

**弱可检形 Det-Win′′（纤维上界 + 占据）.** 假设同时：
1. Det-Fib 以指数 $\delta$ 成立，且对窗内 $m=N-2^k$ 均匀 $r(m)\le R_*(N)\ll N^{\delta+\varepsilon}$；
2. **假设 Det-Occ（窗占据）.** 存在 $\eta\in(0,1]$ 使 $\#\Pi_2(N;K)\ge K^{\eta}$ 对充分大 $N$ 成立。

则由 $|\pi_W|\ge \#\Pi_2/R_*$ 得
$$
\rho_{\mathcal{R}}(N;K)\gg\frac{K^{\eta}}{N^{\delta+\varepsilon}}.
$$
当 $\delta=0$ 时 $\rho_{\mathcal{R}}\gg K^{\eta}$，故 $\rho_E\le K-c K^{\eta}$。欲升级为 $\rho_E\le C K^{\theta}$（$\theta<1$），需更强占据
$$
\#\Pi_2(N;K)\ge c\,K\cdot R_*(N)
\quad\text{或直接}\quad
\#\Pi_2\ge K-C K^{\theta}.
$$
**Det-Occ 是存在性下界，行列式法不直接提供**；列为缺口 Det-G4（相对 L08 的本质增量）。

---

## L-Det-5（条件式：多水平曲面的 Bombieri–Pila 切片）

设 $k_1<\cdots<k_R\le K$，$m_i=N-2^{k_i}$。对固定有理平面铅笔（或固定坐标切片）$\ell_{u,v}$，令曲线
$$
C_{i,u,v}=S_{m_i}\cap\ell_{u,v}.
$$
若 $C_{i,u,v}$ 是次数 $\le d$ 的平面绝对不可约曲线，则 Bombieri–Pila 给出
$$
\#\bigl(C_{i,u,v}(\mathbb{Z})\cap[-B,B]^2\bigr)\ll_{d,\varepsilon} B^{1/d+\varepsilon}.
$$

**假设 Det-Slice.** 存在切片族 $\mathcal{L}$、$d$、$\varepsilon_0$，使对「可表」的 $m_i$ 能选出 $\ell\in\mathcal{L}$ 令 $C_{i}$ 绝对不可约、次数 $\le d$，且
$$
\sum_{i=1}^{R} r(m_i)
\ll_{d,\varepsilon} R^{\alpha} N^{\beta+\varepsilon}
$$
带 $\alpha<1$ 或 $\beta$ 足够小（由各曲线 BP 界与切片数聚合）。

**条件结论.** 若再并入占据下界 $\sum_{i:m_i\notin E} r(m_i)\ge \#\Pi_2(N;K)\ge K^{\eta}$（Det-Occ），则与 Det-Slice 聚合上界比较可强制 $R=\rho_{\mathcal{R}}$ 不能过小，从而 $\rho_E=K-R\le C K^{\theta}$。

**缺口.** 混合次数曲面 $X^4+Y^3+Z^2=m$ 的切片曲线次数、绝对不可约性对 $m=N-2^{k}$ 的均匀控制，见 Det-G2、Det-G3。

---

## L-Det-6（条件式：Heath-Brown 行列式法模板）

记单项式序（各向异性权重 $\mathrm{wt}(X)=3$，$\mathrm{wt}(Y)=4$，$\mathrm{wt}(Z)=6$，使 $X^4,Y^3,Z^2$ 权重均为 $12$）下的格点矩阵：对箱内点列 $P_1,\ldots,P_M\in B(m)\cap S_m(\mathbb{Z})$ 与单项式表 $(1,\ldots)$ 基数 $s$，形成 $M\times s$ 矩阵 $\mathcal{M}$。Heath-Brown 行列式法的核心是：若 $M$ 大，则某 $s\times s$ 子式的 $p$-进或阿基米德大小迫使所有 $P_j$ 落入真子簇。

**假设 Det-HB($m$).** 对充分大 $m$，若 $r(m)>m^{\delta+\varepsilon}$，则 $S_m$ 含有一个定义于 $\overline{\mathbb{Q}}$ 的真子簇 $\mathcal{Y}\subset S_m$，其上集中 $\gg r(m)$ 个箱内整点，且 $\mathcal{Y}$ 的次数 / 高度由 $m$ 多项式控制。

在 $S_m$ 绝对不可约且奇点受控时，迭代剔除子簇应导出 Det-Fib。对二进窗，需要对 $m\in W(N)$ **均匀**的 Det-HB($m$)（常数不依赖 $k$）。

**条件结论.** 均匀 Det-HB + 不可约性 $\Rightarrow$ 均匀 Det-Fib；再与 Det-Occ / Det-Win′ 衔接后经 L-Det-1、L07 得 $x=0$ 型充分大全体可表。

---

## 精确缺口清单（行列式估计）

| 代号 | 缺口内容 | 堵住后可达 |
|------|----------|------------|
| **Det-G1** | **混合次数的加权齐次化.** $X^4+Y^3+Z^2-m$ 非齐次；需在加权射影空间 $\mathbb{P}(3,4,6,1)$（或等价嵌入）中控制「无穷远处」分量与奇点，使 HB/Salberger 行列式的次数–维数假设成立。 | 均匀 Det-Fib |
| **Det-G2** | **绝对不可约性对 $m=N-2^k$ 均匀.** 需排除对许多 $k$ 同时出现 $S_m$ 可约 / 含有理直线丛的情形；可约时 BP/HB 常数与主项会恶化。 | L-Det-5/6 可用 |
| **Det-G3** | **各向异性箱的行列式大小.** 标准 HB 常写于边长可比的阿基米德箱；此处边长 $m^{1/4},m^{1/3},m^{1/2}$ 失衡，需加权高度或仿射变换后重估 $|\det|$ 的上界，缺口是显式指数 $\delta$。 | 明确 $\delta$ |
| **Det-G4** | **占据下界 Det-Occ / Det-Win′.** 行列式法提供整点**上界**与子簇结构，不提供「$\mathcal{V}_N$ 上二进整点非空且 $\gg K^{1-\theta}$」。无 Det-Occ 则即便 $\delta=0$ 仍无法越过 L08（全局稀 $\not\Rightarrow$ 窗击中）。 | $\rho_E\le C K^{\theta}$ |
| **Det-G5** | **多水平联立行列式.** 将 $\{S_{N-2^{k_i}}\}_{i\le R}$ 或差分超曲面 $$X_1^4+Y_1^3+Z_1^2-X_2^4-Y_2^3-Z_2^2=2^{k}-2^{\ell}$$ 做成联立行列式时，需均匀于 $(k,\ell)\in A_K\times A_K$；与 L-Ekill-A2 的 $\Delta_K$-相关对接的估计尚未建立。 | 条件式反相关或 $\theta$-薄 |

**总判.** R1-Det-Surface 将 E-kill 重述为：
$$
\text{Det-G1–G3（纤维上界）}+\text{Det-G4（窗占据）}
\ \Longrightarrow\ \rho_E\le C K^{\theta}\ (\theta<1)
\ \stackrel{\mathrm{L\text{-}Det\text{-}1}}{\Longrightarrow}\ \mathcal{F}_0\text{ 有限}
\ \stackrel{\mathrm{L07}}{\Longrightarrow}\ x=0\text{ 型充分大全体可表}.
$$
其中 Det-G4 是相对 L08 的本质增量；仅关闭 G1–G3 只恢复/加强几乎所有，不构成 E-kill。

---

## 与既有 P1 引理的关系

- 对偶于 **L-Ekill-A2**：A2 走「$E$ 上差集相关」；本路线走「$\mathcal{V}_N$ / $S_m$ 整点几何」。Det-G5 是二者接口。
- 强化 **L-Ekill-Struct-1** 中残差 sparseness 假设 $\#\{k:N-2^k\in S\}\le B K^{\theta}$：若能证真实 $E$ 的 $\rho_E\le C K^{\theta}$，则 Struct 的 $S=E$、$A=\varnothing$ 情形直接给出 $\mathcal{F}_0$ 有限（与 L-Det-1 一致）。
- **不**替代 P2 假设 H；本路线纯属 P1。

---

## 状态一览

| 编号 | 状态 | 备注 |
|------|------|------|
| L-Det-1 | 已证 | $\theta$-薄 $\Rightarrow\mathcal{F}_0$ 有限 $\Rightarrow$ L07 |
| L-Det-2 | 已证 | 整窗 $\Leftrightarrow$ 多水平 $S_{N-2^k}$ 同时空虚 |
| L-Det-3 | 条件式 | 需 Det-Fib；只到全局图像 |
| L-Det-4 | 条件式 | 需 Det-Win′ / Det-Occ |
| L-Det-5 | 条件式 | 需 Det-Slice + BP 均匀 |
| L-Det-6 | 条件式 | 需 Det-HB 均匀模板 |

**原猜想（含 $x>0$）仍开放。**
