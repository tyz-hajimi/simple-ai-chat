# L-Floor：奇异级数轨道地板（R11-SS-Floor-Orbit）

> 路线 **R11-SS-Floor-Orbit**（P09 攻关轮次 11；对抗审查 R10 §6 建议；服务 **P1 / SSO-G4**）。  
> 专攻：把 L-SSO-5 的弱结论 $\max_k\mathfrak{S}(n-2^k)\gg 1$ 提升到 SS-Sync 形
> $$
> \max_k\mathfrak{S}(n-2^k)\gg(\log n)^{-c},
> $$
> 方法：**截断 Euler 积的一致地板**、**二进轨道上的对数平均**、以及（条件式）**大素处等分布 / Mean-Log**。  
> 与次弧阈值 $\mathrm{H}_{\mathrm{thr}}$ **脱钩**：本文件只产出 $\mathfrak{S}$-地板，不声称可表。  
> 状态严格区分：**已证** / **条件式** / **缺口**。原猜想未证。

---

## 0. 记号与目标

沿用 L-SSO：窗口 $W(n)=\{n-2^k:1\le k\le K\}$，$K=\lfloor\log_2(n-1)\rfloor$，
$$
\mathfrak{S}(m)=\prod_p\sigma_p(m),\qquad
\mathfrak{S}_{\le P}(m)=\prod_{p\le P}\sigma_p(m),\qquad
T_P(m)=\prod_{p>P}\sigma_p(m).
$$
写窗上对数平均
$$
\mathcal{A}_n(\phi)=\frac1K\sum_{k=1}^K\phi(n-2^k).
$$
**SSO-G4 目标.** 存在绝对 $c<\infty$ 使对充分大 $n$，
$$
\max_{1\le k\le K}\mathfrak{S}(n-2^k)\gg(\log n)^{-c}.
$$
（SS-Sync 的陈述形；比「固定 $\eta_0$-极小阻断」更贴 L-Ekill-SS-2 / L-Thr-3 的对数门槛。）

---

## L-Floor-1（已证）— 截断 Euler 积的一致正地板

**假设.** L-SSO-2(A)（奇异级数 Euler 积对 $m$ **一致**绝对收敛）与 L-Ekill-SS-1（$\sigma_p(m)\ge p^{-2}$）。

取 $\varepsilon=1/2$。由 L-SSO-2(A) 存在绝对常数 $P_\ast=P_{1/2}<\infty$（不依赖 $m$）使
$$
\sup_m\lvert T_{P_\ast}(m)-1\rvert\le\tfrac12.
$$
对一切 $m$，
$$
\mathfrak{S}_{\le P_\ast}(m)
=\prod_{p\le P_\ast}\sigma_p(m)
\ge\prod_{p\le P_\ast}p^{-2}
=\exp\bigl(-2\,\theta(P_\ast)\bigr),
$$
其中 $\theta(x)=\sum_{p\le x}\log p\le C_\theta P_\ast$（Chebyshev）。故
$$
\mathfrak{S}(m)
=\mathfrak{S}_{\le P_\ast}(m)\,T_{P_\ast}(m)
\ge\exp\bigl(-2\,\theta(P_\ast)\bigr)\cdot\tfrac12.
$$
令
$$
c_{\mathfrak{S}}
:=\tfrac12\exp\bigl(-2\,\theta(P_\ast)\bigr)>0
$$
（绝对正常数）。则
$$
\inf_{m\in\mathbb{Z}}\mathfrak{S}(m)\ge c_{\mathfrak{S}}.
$$

**证明.** 上列不等式链即证。证毕。

**备注.**

1. 此界来自「固定截断高度 + 一致积尾 + 逐素 $p^{-2}$」，**不**需 LS、AP、Tail-Weil、等分布。  
2. 常数 $c_{\mathfrak{S}}$ 可能极小（随 $P_\ast$ 指数衰减），但对一切固定 $A$ 仍有 $c_{\mathfrak{S}}\ge(\log m)^{-A}$（$m$ 充分大）——恰够喂 L-Thr-3 / SS-2 的对数门槛。  
3. 若撤回 L-SSO-2(A) 的**一致性**，本条失效；改走 L-Floor-5/7/8。

---

## L-Floor-2（已证）— 窗最大地板；SSO-G4 / SS-Sync（框架形）

在 L-Floor-1 的同一假设下，对一切 $n\ge 3$，
$$
\max_{1\le k\le K}\mathfrak{S}(n-2^k)
\ge c_{\mathfrak{S}}\gg 1.
$$
特别地，对任意固定 $c<\infty$，
$$
\max_{1\le k\le K}\mathfrak{S}(n-2^k)
\gg(\log n)^{-c}.
$$
故 **SSO-G4 在 L-SSO-2(A)+SS-1 框架下闭合**；SS-Sync 的陈述形成立。

**证明.** 由 L-Floor-1，每个窗点 $\mathfrak{S}(n-2^k)\ge c_{\mathfrak{S}}$，最大元同下界。与 $(\log n)^{-c}\to 0$ 比较即得第二式。证毕。

**与 L-SSO-5 的关系.** L-SSO-5 在 LS+AP 下阻断「长段 $\eta_0$-极小」并得弱 $\max\gg 1$；本条以截断积直接给出**逐点**地板，强度不低于 L-SSO-5 的接口，且不依赖 LS/AP。R4 所忧的「多数点 $(\log)^{-C}$-小、一点偶发 $O(1)$」图景与一致地板不相容。

**明确非声称.** $\mathfrak{S}\ge c_{\mathfrak{S}}$ **不**蕴涵 $m\in\mathcal{R}_{4,3,2}$（缺 $\mathrm{H}_{\mathrm{thr}}$ / 次弧）；对 E-kill 仍须阈值（见 L-Floor-9）。

---

## L-Floor-3（已证）— 二进轨道上的对数平均分解

在 Euler 积收敛的点 $m$ 上，$\log\mathfrak{S}(m)=\sum_p\log\sigma_p(m)$（条件收敛时先截断再取极限）。对窗平均，在 L-SSO-2(A) 下可交换求和：
$$
\mathcal{A}_n(\log\mathfrak{S})
=\sum_p\mathcal{A}_n(\log\sigma_p)
=\sum_{p\le P}\mathcal{A}_n(\log\sigma_p)
+\mathcal{A}_n(\log T_P).
$$
由 L-SSO-2(A)，对任意 $\varepsilon>0$ 存在 $P_\varepsilon$ 使
$$
\sup_m\lvert\log T_{P_\varepsilon}(m)\rvert\le\varepsilon,
$$
从而
$$
\bigl\lvert\mathcal{A}_n(\log\mathfrak{S})-\sum_{p\le P_\varepsilon}\mathcal{A}_n(\log\sigma_p)\bigr\rvert\le\varepsilon.
$$

**证明.** 有限和与平均可交换；积尾一致控制给出余项。证毕。

---

## L-Floor-4（已证）— 单素因子在二进轨道上的均值下界

固定奇数素数 $p\notin\mathfrak{B}$，$P_p=\mathrm{ord}_p(2)$。由 L-SSO-3，$k\mapsto n-2^k\bmod p$ 是圆周 $\langle 2\rangle$ 上的等步采样。

### （A）整周期均值

若连续 $L$ 个指数覆盖整数个周期（$L=qP_p$），则
$$
\frac1L\sum_{j=0}^{L-1}\log\sigma_p(n-2^{k_0+j})
=\frac1{P_p}\sum_{h\in\langle 2\rangle}\log\sigma_p(n-h).
$$
由 $\sigma_p\ge p^{-2}$，
$$
\frac1{P_p}\sum_{h\in\langle 2\rangle}\log\sigma_p(n-h)
\ge -2\log p.
$$

### （B）对 $K=\lfloor\log_2(n-1)\rfloor$ 的窗平均

写 $K=qP_p+r$、$0\le r<P_p$。则
$$
\mathcal{A}_n(\log\sigma_p)
\ge -2\log p-\frac{P_p}{K}\cdot O(\lvert\log\sigma_p\rvert)_{\mathrm{bound}},
$$
其中用 $\lvert\log\sigma_p\rvert\ll\log p$（因 $p^{-2}\le\sigma_p\ll 1+O(1)$ 的圆法局部上界；本仓库用 $\sigma_p\le C_\sigma$ 的平凡上包络时 $\lvert\log\sigma_p\rvert\le 2\log p+O(1)$）。故当 $K\ge P_p$ 时
$$
\mathcal{A}_n(\log\sigma_p)\ge -C_1\log p
$$
（$C_1$ 绝对）。若仅要下界，更粗的
$$
\mathcal{A}_n(\log\sigma_p)\ge -2\log p
$$
对**任意** $K\ge 1$ 亦真（逐项 $\log\sigma_p\ge -2\log p$）。

**证明.** （A）轨道周期性（L-SSO-3）+ SS-1。（B）逐项下界无需周期性；整周期式用于与 Mean-Log 比较。证毕。

---

## L-Floor-5（已证）— 窗上对数平均下界（已证平均）

在 L-SSO-2(A)+SS-1 下，取 $P_\ast=P_{1/2}$ 如 L-Floor-1。则
$$
\mathcal{A}_n(\log\mathfrak{S})
=\mathcal{A}_n(\log\mathfrak{S}_{\le P_\ast})+\mathcal{A}_n(\log T_{P_\ast})
\ge -2\,\theta(P_\ast)-\log 2.
$$
令 $C_0:=2\theta(P_\ast)+\log 2<\infty$。则对一切充分大 $n$，
$$
\mathcal{A}_n(\log\mathfrak{S})\ge -C_0,
$$
从而几何平均
$$
\exp\bigl(\mathcal{A}_n(\log\mathfrak{S})\bigr)
=\Bigl(\prod_{k=1}^K\mathfrak{S}(n-2^k)\Bigr)^{1/K}
\ge e^{-C_0}.
$$

**推论（已证平均 $\Rightarrow$ 最大）.**
$$
\max_{k\le K}\mathfrak{S}(n-2^k)
\ge\exp\bigl(\mathcal{A}_n(\log\mathfrak{S})\bigr)
\ge e^{-C_0}\gg 1.
$$

**证明.** L-Floor-3 截断 + 逐项 $\log\mathfrak{S}_{\le P_\ast}\ge -2\theta(P_\ast)$ + $\lvert\log T_{P_\ast}\rvert\le\log 2$。几何平均 $\le$ 最大元。证毕。

**定位.** 本条是「Euler 积在二进轨道上的对数平均」的已证核心；与 L-Floor-1/2 等价量级，但平均形可对接条件式 Mean-Log（L-Floor-7）而不必先取 $\inf_m$。

---

## L-Floor-6（已证）— 窗上算术平均下界

同假设下，由 Jensen（或由 L-Floor-1 逐点）
$$
\mathcal{A}_n(\mathfrak{S})
=\frac1K\sum_{k=1}^K\mathfrak{S}(n-2^k)
\ge\exp\bigl(\mathcal{A}_n(\log\mathfrak{S})\bigr)
\ge e^{-C_0},
$$
且更直接地 $\mathcal{A}_n(\mathfrak{S})\ge c_{\mathfrak{S}}$。

**证明.** Jensen 于 $\log$ 凹性；或逐点地板平均。证毕。

---

## L-Floor-7（条件式）— Mean-Log + 大素等分布下的定量点态地板

### 输入假设

**Mean-Log（ML$_\delta$）.** 存在 $C,\delta>0$、$p_0$，使对一切素数 $p\ge p_0$，
$$
\frac1p\sum_{r=0}^{p-1}\log\sigma_p(r)\ge -C\,p^{-1-\delta}.
$$

**Equi$_2$（二进轨道等分布）.** 存在 $B_0$，使对一切 $p\le(\log n)^{B_0}$ 与 $K\ge p$，
$$
\Bigl\lvert
\mathcal{A}_n(\log\sigma_p)
-\frac1p\sum_{r}\log\sigma_p(r)
\Bigr\rvert
\le p^{-1-\delta/2}
$$
（当 $\mathrm{ord}_p(2)$ 整除窗长的主项时，由 L-SSO-3 的整周期采样自动成立到 $O(P_p/K)$；一般 $n$ 需 Kloosterman / 不完全轨道误差，标为条件式）。

**Tail-Weil.** 同 L-SSO-2(B)：$\lvert\sigma_p-1\rvert\le C p^{-1-\delta}$。

### 陈述（条件式）

假设 ML$_\delta$ + Equi$_2$ + Tail-Weil。则存在绝对 $c=c(\delta,C,B_0)<\infty$ 与 $N_0$，使 $n\ge N_0$ 时
$$
\mathcal{A}_n(\log\mathfrak{S})\ge -c,
$$
从而
$$
\max_{k\le K}\mathfrak{S}(n-2^k)\gg(\log n)^{0}\asymp 1
$$
（实际上仍 $\gg 1$）；若仅假设弱型
$$
\frac1p\sum_r\log\sigma_p(r)\ge -C\frac{\log p}{p}
\quad(p\le(\log n)^{B}),
$$
则
$$
\mathcal{A}_n(\log\mathfrak{S})\ge -C'\log\log\log n
\quad\text{（或 $-C'\log B$）},
$$
故
$$
\max_k\mathfrak{S}(n-2^k)\gg(\log\log n)^{-C'}
$$
或（取 $B$ 固定）$\gg(\log n)^{0}$ 的任意负幂——即 SSO-G4 的对数地板形。

**证明概要（条件式蕴含）.**  
取 $P=(\log n)^{B}$。Tail-Weil $\Rightarrow\lvert\log T_P\rvert\ll P^{-\delta}$。对 $p\le P$，Equi$_2$+ML 给出
$$
\sum_{p\le P}\mathcal{A}_n(\log\sigma_p)
\ge -C\sum_{p\le P}p^{-1-\delta}-O\Bigl(\sum_{p\le P}p^{-1-\delta/2}\Bigr)
\ge -C''.
$$
弱型 ML 则 $\sum_{p\le P}(\log p)/p\asymp\log\log P\ll\log\log\log n$。再由几何平均 $\le$max 得点态地板。证毕。

**备注.** 在已有 L-Floor-1 时本条对 SSO-G4 **非必需**；其价值在于：(i) 给出不依赖「最坏 $p^{-2}$ 积」的**平均型常数**；(ii) 当一致性积尾被质疑时，仍可能保住 $(\log)^{-c}$ 地板。

---

## L-Floor-8（条件式）— 软鸽笼下由「固定 $\eta_0$」升至「$(\log)^{-c}$」

### 动机

L-SSO-5 的 AP 强形式把「$\mathfrak{S}\le\eta_0$」压到**有限**素集 $\mathcal{P}_\ast$ 上的局部坏，从而只阻断固定 $\eta_0$。若允许「$(\log n)^{-A}$-小」来自 $P=(\log n)^{B}$ 内**多个**中等素各损一点，则需软版鸽笼。

### 软 AP（条件式输入 Soft-AP$_{A,B}$）

存在 $\alpha\in(0,1)$，使若 $\mathfrak{S}(m)\le(\log m)^{-A}$，则
$$
\#\bigl\{p\le(\log m)^{B}:\sigma_p(m)\le c_0\bigr\}
\ge \alpha A\log\log m
$$
（或 $\prod_{p\le(\log m)^{B}}\sigma_p(m)\le(\log m)^{-\alpha A}$）。

### 陈述

假设 LS + Soft-AP$_{A,B}$ + L-SSO-4。则存在 $c=c(\kappa,c_0,\alpha,B)$，使充分大 $n$ 上**不存在**长度 $L\ge c\log n$ 的连续段使
$$
\forall k\in I,\qquad\mathfrak{S}(n-2^k)\le(\log n)^{-A}.
$$
特别地（取整窗）
$$
\max_{k\le K}\mathfrak{S}(n-2^k)\gg(\log n)^{-A}.
$$
此即「LS+AP+轨道乘性 $\Rightarrow$ 对数地板」（R10 目标形）；$A$ 可取任意固定正数，故 SSO-G4 的 $\exists c$ 成立。

**证明概要.** 与 L-SSO-5 相同：软 AP 把每个极小点分摊到 $\asymp\log\log n$ 个坏素；LS+L-SSO-4 限制单素连续坏弧长 $\le(1-\kappa)P_p\le(1-\kappa)p$。总覆盖预算
$$
\sum_{p\le(\log n)^{B}}(1-\kappa)p\ll(\log n)^{2B}
$$
与「整窗 $K\asymp\log n$ 段皆对数极小」所需的命中量比较；选取 $A,B$ 使二者冲突（或改为：不能覆盖长度 $c\log n$ 的连续段）。证毕。

**与 L-Floor-2 比较.** L-Floor-2 更强且少假设；本条保留为「不引一致积尾」时的条件式备份，并精确实现 R10 建议的拼链形。

---

## L-Floor-9（已证接口）— 对接 L-Thr / L-Ekill-SS-2；非 E-kill

### （A）阈值拼合

若 $\mathrm{H}_{\mathrm{thr}}(A)$ 成立，则由 L-Thr-3：$\mathfrak{S}(m)\ge(\log m)^{-A}\Rightarrow m\in\mathcal{R}_{4,3,2}$。  
由 L-Floor-2，窗上 $\max\mathfrak{S}\ge c_{\mathfrak{S}}\ge(\log)^{-A}$（$n$ 大），故最大点可表，从而 $n\notin\mathcal{F}_0^{\mathrm{kill}}$。

**推论（条件式，同 L-Thr-4b 的强化版）.**
$$
\mathrm{H}_{\mathrm{thr}}(A)
\ \Longrightarrow\ 
\mathcal{F}_0^{\mathrm{kill}}\text{ 仅有限}
$$
（轨道侧改用 L-Floor-2，**不再**需要 LS+AP）。再经 L07 得 $x=0$ 型充分大。

### （B）与 SS-2 上界的对撞

L-Ekill-SS-2：在阈值前置下，坏窗满足 $\max\mathfrak{S}\ll_A(\log)^{-A}$。  
L-Floor-2：$\max\mathfrak{S}\ge c_{\mathfrak{S}}$。二者对撞 $\Rightarrow$ 充分大坏窗不存在（条件于阈值）。

### （C）R4 降级保留

无 $\mathrm{H}_{\mathrm{thr}}$ 时，地板**不**杀窗、**不**证原猜想。禁止写「SSO-G4 已闭合故 E-kill 完成」。

---

## L-Floor-10（草案 / 缺口清单）

| 缺口代号 | 内容 | 堵住则得 |
|----------|------|----------|
| Floor-G0 | （若质疑）L-SSO-2(A) 积尾对 $m$ 的一致性 | L-Floor-1/2 的框架前提 |
| Floor-G1 | ML$_\delta$：大素上 $\mathbb{E}_r\log\sigma_p$ 的幂次负均值 | L-Floor-7 平均型常数 |
| Floor-G2 | Equi$_2$：二进轨道对 $\log\sigma_p$ 的等分布误差 | 增长截断 $P=(\log n)^{B}$ |
| Floor-G3 | Soft-AP：对数极小 $\Rightarrow$ 多素局部坏的有效计数 | L-Floor-8（无一致积尾备份） |
| Floor-G4 | $=\mathrm{Thr}$-G1：$\mathrm{H}_{\mathrm{thr}}$ | 地板 $\Rightarrow$ 可表 / E-kill |

**SSO-G4 状态（本路线）.**  
- 在 L-SSO-2(A)+SS-1 下：**已闭合**（L-Floor-1/2/5）。  
- 无一致积尾时：降为条件式 L-Floor-7/8。  
- 对接 E-kill 仍缺 Floor-G4（$=\mathrm{H}_{\mathrm{thr}}$）。

**明确非声称.**

- 不证明 $\mathrm{H}_{\mathrm{thr}}$、H、原猜想、$\mathcal{F}_0$ 有限（无阈值时）。  
- 不声称「$\mathfrak{S}\gg 1\Rightarrow m\in\mathcal{R}_{4,3,2}$」无条件成立。  
- 不改写 L-Ekill-SS-1 的 $p^{-2}$ 证明。

---

## 状态总表

| 编号 | 摘要 | 状态 |
|------|------|------|
| L-Floor-1 | 截断积一致地板 $\inf_m\mathfrak{S}\ge c_{\mathfrak{S}}>0$ | 已证（框架：SSO-2(A)+SS-1） |
| L-Floor-2 | $\max_k\mathfrak{S}(n-2^k)\gg 1$；SSO-G4 / SS-Sync 形 | 已证（框架） |
| L-Floor-3 | 窗对数平均 $=\sum_p$ 单素轨道平均 | 已证 |
| L-Floor-4 | 单素轨道均值 $\ge -O(\log p)$ | 已证 |
| L-Floor-5 | $\mathcal{A}_n(\log\mathfrak{S})\ge -C_0$；几何平均 $\gg 1$ | 已证（平均下界） |
| L-Floor-6 | $\mathcal{A}_n(\mathfrak{S})\ge e^{-C_0}$ | 已证（平均下界） |
| L-Floor-7 | ML+Equi+Tail-Weil $\Rightarrow$ 定量地板 | 条件式 |
| L-Floor-8 | LS+Soft-AP $\Rightarrow\max\mathfrak{S}\gg(\log)^{-A}$ | 条件式（R10 形） |
| L-Floor-9 | 对接 Thr/SS-2；无阈值不杀窗 | 已证接口 |
| L-Floor-10 | 缺口 Floor-G0–G4 | 缺口 |
