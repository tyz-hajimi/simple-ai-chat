# L-RShift：Roth 圆法误差与二进平移的双点相关（路线 R16-Roth-Shift-Correlation）

> 路线 **R16-Roth-Shift-Correlation**（P09 攻关轮次 16，服务 **P1 = E-kill-1**）。  
> 问题：Roth（1949）证明几乎所有 $m\in\mathcal{R}_{4,3,2}$，其圆法结构是否**隐含**例外集 $E$ 与二进平移 $h=2^k$ 的弱相关（形如 LSW-Corr / AE-Corr）？  
> 方法：基于标准 Hardy–Littlewood 主弧/次弧分解做**可检验**推导；**不**声称已逐行精读 Roth 原文每一估计，只使用与 L-Thr / L-Eff / L-CRB-1(C) / L-Dec 兼容的圆法骨架。  
> **总判决（一句话）.** Roth 的均值平方仅控制**单点**大次弧误差的稀薄性；主弧逼近误差在尺度 $h\ll m^{\theta}$ 上近乎同步，**不**制造反相关；次弧双点相关恰等于 $\int_{\mathfrak{m}}|F|^2 e(h\alpha)$，平凡 CS **无亏缺**——故「几乎所有」**不**隐含二进弱相关。条件式 RShift-Osc$_\eta$ / RShift-SS$_\eta$ 才接到 LSW-Corr。  
> 状态：`已证` / `条件式` / `缺口`。**不声称原猜想 / E-kill / LSW-Corr 已证。**

---

## 0. 记号与 Roth 圆法骨架（可检验约定）

沿用：$E=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2}$，$\beta=13/12$，
$$
F(\alpha)=f_4(\alpha)f_3(\alpha)f_2(\alpha),\qquad
r(m)=\int_0^1 F(\alpha)\,e(-m\alpha)\,\mathrm{d}\alpha.
$$
固定剖分参数 $1\le Q\le m^{\theta_0}$（$\theta_0$ 同 L-Thr-1 / L-Eff），写
$$
r(m)=r_{\mathfrak{M}}(m)+r_{\mathfrak{m}}(m).
$$
主弧包（L-Thr-1(B)/L-Eff-1）：
$$
r_{\mathfrak{M}}(m)
=
\mathfrak{S}(m)\,\mathfrak{J}(m)
+E_{\mathrm{maj}}(m),
\qquad
|E_{\mathrm{maj}}(m)|
\ll
m^{1/12}\bigl(Q^{-\delta_0}+m^{-\eta_0}\bigr),
$$
且 $\mathfrak{J}(m)\asymp m^{1/12}$。次弧
$$
r_{\mathfrak{m}}(m)=\int_{\mathfrak{m}(Q)}F(\alpha)\,e(-m\alpha)\,\mathrm{d}\alpha.
$$

**Roth 型几乎所有（引用骨架；L-CRB-1(C) / Thm-B）.**
$$
M(X):=|E\cap[1,X]|\ll\frac{X}{(\log X)^{1/20}}.
$$
经典路径（标准转述，**不**依赖原文逐行）：  
1. 奇异级数过小的集合 $E_{\mathrm{SS}}$ 对数稀；  
2. 主弧在 $\mathfrak{S}(m)\ge(\log m)^{-A}$ 时给出 $\gg_A m^{1/12}/(\log m)^{A}$；  
3. 次弧贡献的**均值平方**（或等价 Hölder–华氏矩）使 $|r_{\mathfrak{m}}(m)|$ 大到盖住主项的 $m$ 稀薄；  
4. 并集得 $E$ 的对数节省。

**例外集的解析分裂（定义，非声明互斥）.** 对固定 $A<\infty$ 与充分大 $m$，令
\begin{align*}
E_{\mathrm{SS}}(A)
&=\{m:\mathfrak{S}(m)<(\log m)^{-A}\},\\
E_{\mathrm{min}}(A)
&=\{m:|r_{\mathfrak{m}}(m)|\ge\tfrac12 c_0\,m^{1/12}(\log m)^{-A}\},\\
E_{\mathrm{maj}}^{\sharp}
&=\{m:|E_{\mathrm{maj}}(m)|\ge\tfrac14 c_0\,m^{1/12}(\log m)^{-A}\},
\end{align*}
其中 $c_0$ 同 L-Eff-1。则在 L-Thr-3 型主弧下界下，
$$
E\setminus\bigl(E_{\mathrm{SS}}(A)\cup E_{\mathrm{maj}}^{\sharp}\bigr)
\subseteq E_{\mathrm{min}}(A)
$$
（对充分大元）：若主项够大且主弧误差小，则 $r(m)=0$ 迫使次弧大。$E_{\mathrm{maj}}^{\sharp}$ 在 $Q=m^{\theta_0}$ 时对固定 $A$ **最终空**（幂次误差压倒对数），故渐近上真实例外由 $E_{\mathrm{SS}}$ 与 $E_{\mathrm{min}}$ 主导。

**双点相关对象.** 对 $h\ge 1$、$X\ge 1$，
$$
R_E(h;X)
:=\sum_{1\le m\le X}1_E(m)\,1_E(m+h),
$$
以及解析次弧相关
$$
R_{\mathfrak{m}}(h;X)
:=\sum_{1\le m\le X}r_{\mathfrak{m}}(m)\,\overline{r_{\mathfrak{m}}(m+h)}.
$$
二进特款 $h=2^k$（$1\le k\le\lfloor\log_2 X\rfloor$）。对接 L-LSW：
$$
r_{1_E}(h)=\sum_m 1_E(m)1_E(m+h)
$$
（无限支撑差表示；截断版即 $R_E(h;X)$）。

**假设 RShift-Osc$_\eta$（次弧振荡亏缺；条件式）.** 存在 $\eta>0$ 使对充分大 $K$ 与一切 $1\le k\le K$，在 $X=2^{K+1}$、$Q=X^{\theta_0}$ 下
$$
\Bigl|\int_{\mathfrak{m}(Q)}|F(\alpha)|^2 e(2^k\alpha)\,\mathrm{d}\alpha\Bigr|
\le
K^{-\eta}\int_{\mathfrak{m}(Q)}|F(\alpha)|^2\,\mathrm{d}\alpha.
$$

**假设 RShift-SS$_\eta$（奇异级数双点稀；条件式）.** 存在 $\eta>0$ 使对充分大 $K$ 与 $h=2^k\le 2^K$，
$$
\bigl|E_{\mathrm{SS}}(A)\cap\bigl(E_{\mathrm{SS}}(A)-h\bigr)\cap[1,2^{K+1}]\bigr|
\le
K^{-\eta}\,M_{\mathrm{SS}}(2^{K+1}),
$$
其中 $M_{\mathrm{SS}}(Y)=|E_{\mathrm{SS}}(A)\cap[1,Y]|$（$A$ 固定足够大）。

---

## L-RShift-1（已证）— 次弧误差的双点 Plancherel 恒等式

设 $h\in\mathbb{Z}$，并设 $F$ 在 $\mathfrak{m}=\mathfrak{m}(Q)$ 上的截断使 $r_{\mathfrak{m}}$ 有限支撑于 $[1,X]$ 的光滑化无关紧要（标准：用平滑权 $\psi_X$ 后差 $O_\varepsilon(X^{\beta-1+\varepsilon})$，下文隐去）。则
$$
\sum_{m\in\mathbb{Z}}r_{\mathfrak{m}}(m)\,\overline{r_{\mathfrak{m}}(m+h)}
=
\int_{\mathfrak{m}}|F(\alpha)|^2\,e(h\alpha)\,\mathrm{d}\alpha.
$$
特别地 $h=0$ 时
$$
\sum_m|r_{\mathfrak{m}}(m)|^2
=
\int_{\mathfrak{m}}|F|^2.
$$

**证明.** 展开
$$
r_{\mathfrak{m}}(m)=\int_{\mathfrak{m}}F(\alpha)e(-m\alpha)\,\mathrm{d}\alpha,
$$
对 $m$ 求和用正交性：
$$
\sum_m e\bigl((- \alpha+\beta)m\bigr)\,e(-h\beta)
$$
迫使 $\alpha\equiv\beta\pmod 1$，留下 $\int_{\mathfrak{m}}|F(\alpha)|^2 e(h\alpha)\,\mathrm{d}\alpha$。证毕。

**定位.** 双点相关**不是**新的圆法对象——它就是 $|F|^2\mathbf{1}_{\mathfrak{m}}$ 在频率 $h$ 的 Fourier 系数。Roth 控制的是 $h=0$ 的 $L^2$ 质量（或由此推出的单点 Markov），**不是** $h=2^k$ 的振荡积分。

---

## L-RShift-2（已证·结算）— Roth 均值平方 $\not\Rightarrow$ 二进弱相关

**(A) 单点 Markov（Roth 骨架已用形）.** 对 $\lambda>0$，
$$
\#\bigl\{m\le X:|r_{\mathfrak{m}}(m)|\ge\lambda\bigr\}
\le
\lambda^{-2}\sum_{m\le X}|r_{\mathfrak{m}}(m)|^2
=
\lambda^{-2}\int_{\mathfrak{m}}|F|^2
$$
（截断误差忽略）。取 $\lambda\asymp X^{1/12}/(\log X)^{A}$ 即得 $E_{\mathrm{min}}(A)$ 的上界；与 $E_{\mathrm{SS}}$ 合并复述 Thm-B 量级（具体指数 $1/20$ 依赖原文矩选择，本条**不**重算）。

**(B) 双点无自动亏缺.** 由 L-RShift-1 与三角不等式，
$$
\bigl|R_{\mathfrak{m}}(h;X)\bigr|
\le
\int_{\mathfrak{m}}|F|^2
=
\sum_m|r_{\mathfrak{m}}(m)|^2.
$$
右端恰为对角（$h=0$）质量。故**仅**有 Roth 型次弧 $L^2$ 界时，对任意 $h$（含 $h=2^k$）
$$
\bigl|R_{\mathfrak{m}}(h;X)\bigr|
\le
\sum_m|r_{\mathfrak{m}}(m)|^2,
$$
**零亏缺**：不能推出
$$
\bigl|R_{\mathfrak{m}}(2^k;X)\bigr|
\le
K^{-\eta}\sum_m|r_{\mathfrak{m}}(m)|^2
$$
这类 LSW-Corr / AE-Corr 形陈述。

**(C) 指示相关更弱.** 即使控制了 $R_{\mathfrak{m}}(h;X)$，由 $1_E\le 1_{E_{\mathrm{SS}}}+1_{E_{\mathrm{min}}}+1_{E_{\mathrm{maj}}^{\sharp}}$ 展开 $R_E(h;X)$ 仍需处理交叉项；Roth 只给 $\sum 1_E\ll X/(\log)^{1/20}$，由 Cauchy
$$
R_E(h;X)
\le
M(X+h)
\ll
\frac{X}{(\log X)^{1/20}},
$$
与「随机型」$R_E(h;X)\asymp M(X)^2/X\ll X/(\log)^{1/10}$ 相比，Fréchet 上界 $R_E\le M$ **更弱**（对照 L-Rand-4 / L-LSW-5），且对**一切** $h$ 一视同仁——**不**识别二进滞后。

**判决.** 「Roth 证明几乎所有」**不**隐含例外集与 $m\mapsto m+2^k$ 的弱相关。已证的仅是单点稀薄 + 平移不变的 Fréchet 界。

---

## L-RShift-3（已证·障碍）— 主弧/次弧误差对「双点同时小」无阻碍

问：圆法中主弧误差 $E_{\mathrm{maj}}$ 与次弧 $r_{\mathfrak{m}}$ 是否**阻碍** $r(m)$ 与 $r(m+2^k)$ **同时**落入例外机制（即同时使 $r$ 接近 $0$）？

### （A）主弧逼近误差：同步，非反相关

设 $h=2^k$ 满足 $1\le h\le m^{1/2}$（窗内典型：$h\le N$、$m=N-2^\ell$）。主弧包中 $\mathfrak{J}(m)\asymp m^{1/12}$ 对 $m\mapsto m+h$ 改变
$$
\bigl|(m+h)^{1/12}-m^{1/12}\bigr|
\ll
h\,m^{1/12-1}
\ll
m^{-1/2+o(1)},
$$
远小于主项 $m^{1/12}$。误差项 $E_{\mathrm{maj}}(m)$ 的隐含常数来自 Gauss 和完备化与 Farey 宽度，在 $|\beta|\le Q/(qm)$ 的局部坐标下对 $m$ 光滑依赖；差
$$
E_{\mathrm{maj}}(m+h)-E_{\mathrm{maj}}(m)
$$
在 $h=o(m/Q)$ 尺度上是**低阶扰动**，同号同阶的典型行为是**同步变大/变小**，而非一正一负相消。

因而：若 $|E_{\mathrm{maj}}(m)|$ 已小到可忽略，则 $|E_{\mathrm{maj}}(m+h)|$ 通常同样可忽略——**主弧误差不构成「不能同时小」的障碍**；它也不提供 $1_E(m)1_E(m+h)$ 的节省。

### （B）奇异级数主项：局部几乎独立，但非圆法次弧所证

$\mathfrak{S}(m)$ 与 $\mathfrak{S}(m+h)$ 的联合小概率由 Euler 积的双点局部密度控制（见 L-RShift-6）。这是**算术**输入，不是主/次弧分析误差项的推论。圆法宽度 $Q^{-\delta_0}$ 对二者同时施加同一幂次门槛，**同样不制造反相关**。

### （C）次弧：同时大才是例外机制；同时小是常态

可表性失败（在 $\mathfrak{S}$ 不太小时）需要 $|r_{\mathfrak{m}}|$ **大**。故「双点相关」关心的是
$$
1_{E_{\mathrm{min}}}(m)\,1_{E_{\mathrm{min}}}(m+h)
$$
（同时**大**），而非次弧同时小。次弧同时小恰恰对应双点都可表（在主项够大时）——这是几乎所有结论的友好侧，**不**阻碍例外对的存在。

对「同时大」：L-RShift-2(B) 显示次弧 $L^2$ 质量可完全集中在与 $e(h\alpha)$ 同相的方向上；平凡 CS **允许**
$$
R_{\mathfrak{m}}(h;X)
=
\sum_m|r_{\mathfrak{m}}(m)|^2
$$
（完全相关）。因此标准次弧估计**不阻碍** $m$ 与 $m+2^k$ 同时落入 $E_{\mathrm{min}}$。

**判决.** 主弧/次弧误差结构对「$m$ 与 $m+2^k$ 同时例外」**无自动阻碍**；要阻碍必须额外的振荡（RShift-Osc）或奇异级数双点稀（RShift-SS）。

---

## L-RShift-4（条件式）— RShift-Osc$_\eta$ $\Rightarrow$ 次弧双点亏缺

假设 RShift-Osc$_\eta$。则对 $X=2^{K+1}$、$1\le k\le K$，
$$
\bigl|R_{\mathfrak{m}}(2^k;X)\bigr|
\le
K^{-\eta}\sum_{m}|r_{\mathfrak{m}}(m)|^2
=
K^{-\eta}\int_{\mathfrak{m}}|F|^2.
$$

**证明.** L-RShift-1 + 假设。证毕。

**注.** 这是把「频率 $2^k$ 在次弧支撑上振荡」写成可对接 LSW 的输入；**未证**。启发式：$\mathfrak{m}$ 上 $|F|^2$ 若无高度集中于 $\alpha\bmod 2^{-k}$ 的尖峰，则相位 $e(2^k\alpha)$ 平均取消。与 L-Lac Peak（缺项核尖峰）不同：此处尖峰属于 $|F|^2$，属 P2 次弧几何。

---

## L-RShift-5（条件式）— 解析例外对的相关 $\Rightarrow$ 近 LSW-Corr

设 $A$ 固定足够大，使 Thm-B 证明中 $E\setminus(E_{\mathrm{SS}}(A)\cup E_{\mathrm{min}}(A))$ 的充分大部落入可忽略集（势 $\ll X/(\log X)^{100}$，吸收进 Roth 常数）。假设 RShift-Osc$_\eta$。

**(A) 大值对计数（模板）.** 令 $\lambda(X)=c\,X^{1/12}(\log X)^{-A}$。则
\begin{align*}
\sum_{1\le m\le X}&1_{|r_{\mathfrak{m}}(m)|\ge\lambda}\,1_{|r_{\mathfrak{m}}(m+h)|\ge\lambda}\\
&\le
\lambda^{-2}\sum_{m\le X}|r_{\mathfrak{m}}(m)\,r_{\mathfrak{m}}(m+h)|
\\
&\le
\lambda^{-2}\bigl|R_{\mathfrak{m}}(h;X)\bigr|
+\text{（可用 CS 再拆；主路径用}\ |ab|\le\tfrac12(|a|^2+|b|^2)\ \text{仅回对角）}.
\end{align*}
更干净的路径：对非负权，
$$
\sum_m 1_{|r_{\mathfrak{m}}(m)|\ge\lambda}1_{|r_{\mathfrak{m}}(m+h)|\ge\lambda}
\le
\lambda^{-2}\sum_m |r_{\mathfrak{m}}(m)|\,|r_{\mathfrak{m}}(m+h)|.
$$
再由 Cauchy–Schwarz
$$
\sum_m |r_{\mathfrak{m}}(m)|\,|r_{\mathfrak{m}}(m+h)|
\le
\Bigl(\sum_m|r_{\mathfrak{m}}(m)|^2\Bigr)^{1/2}
\Bigl(\sum_m|r_{\mathfrak{m}}(m+h)|^2\Bigr)^{1/2}
=
\sum_m|r_{\mathfrak{m}}|^2,
$$
**仍无亏缺**。要得到亏缺，需对双线性形保留相位，例如
$$
\sum_m r_{\mathfrak{m}}(m)\,\overline{r_{\mathfrak{m}}(m+h)}
$$
的绝对值（L-RShift-4）控制**带符号**相关；指示函数相关还需：

**(B) 假设 RShift-Pt$_\theta$（点态次弧可比较；条件式加强）.** 存在 $\theta\in(0,1]$ 使在 $E_{\mathrm{min}}(A)$ 上
$$
|r_{\mathfrak{m}}(m)|\le X^{1/12}(\log X)^{\theta},
$$
且「大多数」例外由次弧贡献的**正质量**主导（符号问题：可用 $|r_{\mathfrak{m}}|^2$ 代替 $r_{\mathfrak{m}}$ 做非负相关——见下）。

**(C) 非负二矩相关（推荐接口）.** 定义
$$
R_{\mathfrak{m}}^{(2)}(h;X)
:=\sum_{m\le X}|r_{\mathfrak{m}}(m)|^2\,|r_{\mathfrak{m}}(m+h)|^2.
$$
展开为四重积分；对角主导时 $\asymp\bigl(\int_{\mathfrak{m}}|F|^2\bigr)^2$，非对角含 $e(h(\alpha-\beta))$。假设
$$
\textbf{RShift-Mom}_4(\eta):\quad
R_{\mathfrak{m}}^{(2)}(2^k;X)
\le
K^{-\eta}\Bigl(\sum_{m\le X}|r_{\mathfrak{m}}(m)|^2\Bigr)^2
$$
则由 Markov 型双点，
$$
\#\bigl\{m\le X:m,m+2^k\in E_{\mathrm{min}}(A)\bigr\}
\le
\lambda^{-4}R_{\mathfrak{m}}^{(2)}(2^k;X)
\ll
K^{-\eta}\frac{X}{(\log X)^{c}}
$$
（$c$ 依 Roth 矩）。从而对 $d=2^k\in\Delta_K^{\mathrm{full}}$，
$$
r_{1_{E_{\mathrm{min}}}}(d)
\ll
K^{-\eta}M(2^{K+1})+(\text{可忽略}),
$$
即 **LSW-Corr$_\eta$ 在 $E_{\mathrm{min}}$ 上的条件式版本**。

**证明要点.** (C) 由定义与 $\lambda$ 门槛；把 $E_{\mathrm{SS}}$ 用 RShift-SS$_\eta$ 另控（L-RShift-6）。证毕。

**诚实标注.** L-RShift-4 的复相关亏缺**不足以**单独推出指示相关亏缺（相位/符号）；P1 接口应以 **RShift-Mom$_4$** 或 RShift-SS+Osc 的组合为准。L-RShift-4 仍有独立价值：排除「仅凭 Plancherel 对角线」的幻想，并把缺口精确化为频率 $2^k$ 的四矩/振荡。

---

## L-RShift-6（已证结构 + 条件式）— 奇异级数双点与 $E_{\mathrm{SS}}$

**(A) 已证结构（Euler 积）.** 写 $\mathfrak{S}(m)=\prod_p\sigma_p(m)$。对奇数素数 $p\nmid h$，平移 $m\mapsto m+h$ 在 $\mathbb{Z}/p^\nu$ 上是双射，故
$$
\mathbb{E}_{m\bmod p^\nu}\bigl[f(\sigma_p(m))g(\sigma_p(m+h))\bigr]
=
\mathbb{E}[f(\sigma_p)]\,\mathbb{E}[g(\sigma_p)]
$$
对任意由 $\sigma_p$ 决定的函数（有限矩）。因而奇数处局部因子在差 $h=2^k$ 下**渐近独立**。

**(B) $2$-进.** 由 L-2adic-2，$\delta_\nu=1$（像集满）；$h=2^k$ 在高 $2$-进上改变赋值，但**不**产生强制同时落入坏类（L-2adic-4：$\mathrm{Bad}_\nu=\emptyset$）。故 $2$-进不制造「整窗级」的 $E_{\mathrm{SS}}$ 团，也不自动给出 $R_{E_{\mathrm{SS}}}(2^k;X)$ 的幂次节省。

**(C) 条件式 RShift-SS$_\eta$.** 若 RShift-SS$_\eta$ 成立，则
$$
R_{E_{\mathrm{SS}}}(2^k;2^{K+1})
\le
K^{-\eta}M_{\mathrm{SS}}(2^{K+1}).
$$
启发式：独立模型下 $M_{\mathrm{SS}}(Y)\ll Y/(\log)^A$，双点 $\asymp M_{\mathrm{SS}}^2/Y\ll Y/(\log)^{2A}$，对大 $A$ 强于 $M_{\mathrm{SS}}/K^{\eta}$；**真实证明**需大筛/均值定理控制截断奇异级数的水平分布，超出 Roth 原文的几乎所有论证。

**(D) 拼合到 $R_E$.** 
$$
R_E(h;X)
\le
R_{E_{\mathrm{SS}}}(h;X)+R_{E_{\mathrm{min}}}(h;X)+O\bigl(X/(\log X)^{100}\bigr).
$$
RShift-SS$_\eta$ + RShift-Mom$_4(\eta)$（L-RShift-5）$\Rightarrow$
$$
R_E(2^k;2^{K+1})
\ll
K^{-\eta}M(2^{K+1}),
$$
即 **LSW-Corr$_\eta$ 的条件式推出**（喂入 L-LSW-6）。

---

## L-RShift-7（已证对照）— 与 LSW / AE / EFD / Pack / Rand 的正交性

| 路线 | 主对象 | 与 L-RShift 关系 |
|------|--------|------------------|
| L-LSW | $Q_K=\sum_N|\sum_k 1_E(N-2^k)|^2$；假设 LSW-Corr | RShift 试图从**圆法误差**导出 Corr；LSW 把 Corr 当黑箱 |
| L-AE / A2 | $\Delta_K$-团相关 $\mathcal{C}$ | 整窗$\Rightarrow$最大相关已证；RShift 讨论真实 $E$ 是否反相关 |
| L-EFD | $\widehat{1_E}$ 与 $g_N$ | EFD 在 $E$ 指示侧；RShift 在表示误差 $r_{\mathfrak{m}}$ 侧——**桥接需** $1_E\approx 1_{|r_{\mathfrak{m}}|\ge\lambda}$ |
| L-Pack | 邻/倍窗装填抬 $|E|$ | Pack 组合抬升；RShift 解析相关 |
| L-Rand | Bernoulli 近独立 | 独立模型下双点自动弱；RShift 说明 Roth **达不到**该模型 |
| L-Thr / L-Eff | 主弧半边 | 提供 $E_{\mathrm{maj}}$ 可忽略与主项尺度；不提供双点 |

**明确非声称.** 本文件不证明 RShift-Osc / Mom$_4$ / SS，不证明 LSW-Corr，不证明 $\mathcal{F}_0$ 有限。

---

## L-RShift-8（缺口）— RShift-G1–G4

| 编号 | 缺口 | 若解决则 |
|------|------|----------|
| RShift-G1 | RShift-Osc$_\eta$ 或 RShift-Mom$_4(\eta)$ | 次弧例外对亏缺（L-RShift-4/5） |
| RShift-G2 | RShift-SS$_\eta$（截断 $\mathfrak{S}$ 双点水平分布） | $E_{\mathrm{SS}}$ 对相关（L-RShift-6） |
| RShift-G3 | $1_E$ 与 $1_{E_{\mathrm{min}}}$ / $1_{E_{\mathrm{SS}}}$ 的对称差可忽略且保持双点 | 把解析相关迁到真实 $E$（接 LSW-Corr） |
| RShift-G4 | LSW-Corr$_\eta$ + Sum/Exp（经 L-LSW-6/8） | $\mathcal{F}_0$ 有限（仍可能需超 Roth $1/20$ 的额外可和；见 L-LSW-8） |

**主缺口.** G1+G2（圆法/算术双点）；即使全开，G4 在仅有对数 Corr 时仍可能不杀 $\mathcal{F}_0$（L-LSW-8 装填注）。本路线**结算**的是：Roth 几乎所有**不是** G1 的免费来源。

---

## 小结

| 编号 | 摘要 | 状态 |
|------|------|------|
| L-RShift-1 | $R_{\mathfrak{m}}(h)=\int_{\mathfrak{m}}|F|^2 e(h\alpha)$ | 已证 |
| L-RShift-2 | Roth 均值平方 $\not\Rightarrow$ 二进弱相关；Fréchet 对一切 $h$ | 已证（结算） |
| L-RShift-3 | 主弧误差同步；次弧 CS 无亏缺；无「同时例外」阻碍 | 已证（障碍） |
| L-RShift-4 | RShift-Osc$_\eta$$\Rightarrow$ 次弧复相关亏缺 | 条件式 |
| L-RShift-5 | Mom$_4$/Pt + Osc $\Rightarrow$ $E_{\mathrm{min}}$ 上近 LSW-Corr | 条件式 |
| L-RShift-6 | $\mathfrak{S}$ 奇素独立结构；RShift-SS$_\eta$$\Rightarrow$$E_{\mathrm{SS}}$ 相关 | 已证结构+条件式 |
| L-RShift-7 | 与 LSW/AE/EFD/Pack/Rand 对照 | 已证（对照） |
| L-RShift-8 | 缺口 RShift-G1–G4 | 缺口 |

**链条（已证否定式）.**
$$
\text{Roth 单点 }L^2\text{ Markov}
\ \not\Longrightarrow\
\text{LSW-Corr / AE-Corr 型二进弱相关}.
$$

**链条（条件式正通向）.**
$$
\mathrm{RShift\text{-}Mom}_4(\eta)+\mathrm{RShift\text{-}SS}_\eta
\stackrel{\mathrm{L\text{-}RShift\text{-}5/6}}{\Longrightarrow}
\mathrm{LSW\text{-}Corr}_\eta
\stackrel{\mathrm{L\text{-}LSW\text{-}6}}{\Longrightarrow}
|\mathcal{F}_0\cap I_K|\ll\frac{M}{K^{\min(1,\eta)}}
$$
（有限性仍要 L-LSW-8 的 Sum/Exp 或更强近独立）。

**阅读式提取（可入库一句）.**  
Roth 圆法中，主弧误差在二进平移下近同步、次弧双点相关等于 $\int_{\mathfrak{m}}|F|^2 e(2^k\alpha)$，平凡界无亏缺——故主/次弧误差**不**阻碍 $m$ 与 $m+2^k$ 同时例外；弱相关是**额外**振荡/水平分布假设，不是几乎所有定理的隐含结论。
