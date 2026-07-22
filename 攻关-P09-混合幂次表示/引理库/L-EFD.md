# L-EFD：例外集连续 Fourier 衰减与二进采样偏差（路线 R9-E-Fourier-Decay）

> 路线 **R9-E-Fourier-Decay**（P09 攻关轮次 9，服务 **P1 = E-kill-1**）。  
> 对象：真实例外集指示函数在整数变量上的**连续** Fourier 变换
> $$
> \widehat{1_E}(\alpha;X)=\sum_{m\le X}1_E(m)\,e(\alpha m),
> $$
> 并经缺项核 $g_N$ 导出二进采样 $\sum_k 1_E(N-2^k)$ 的偏差，从而条件式杀 $\mathcal{F}_0$。  
> **与 L-FW 正交**：L-FW 研究尺度 $K$ 上的采样序列 Fourier $\Phi_N(\alpha)=\sum_k 1_E(N-2^k)e(\alpha k)$（频率作用在指数下标 $k$）；本路线频率作用在**环境整数** $m$，再与 lacuna 核耦合。禁止把本文件写成 L-FW 的复述。  
> 状态：`已证` / `条件式` / `缺口`。**不声称原猜想已证。**

---

## 0. 记号

沿用：$E=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2}$，$K=\lfloor\log_2(N-1)\rfloor$，
$$
W(N)=\{N-2^k:1\le k\le K\},\qquad
\mathcal{F}_0=\{N\ge 2:W(N)\subseteq E\}.
$$
$e(\theta)=e^{2\pi i\theta}$。对 $X\ge 2$ 写截断 Fourier
$$
\widehat{1_E}(\alpha;X)=\sum_{m=1}^{X}1_E(m)\,e(\alpha m),\qquad
\widehat{f_E}(\alpha;X)=\sum_{m=1}^{X}\bigl(1_E(m)-\delta_E(X)\bigr)\,e(\alpha m),
$$
其中 $\delta_E(X)=|E\cap[1,X]|/X$。骨架 Roth 界（定理 B）
$$
|E\cap[1,X]|\ll\frac{X}{(\log X)^{1/20}}\qquad\Rightarrow\qquad\delta_E(X)\ll(\log X)^{-1/20}.
$$
缺项核（与 L-Circ-9 / L-Osc 相同）
$$
g_N(\alpha)=\sum_{k=1}^{K}e(\alpha 2^k),\qquad
\int_0^1|g_N|^2\,\mathrm{d}\alpha=K.
$$
主弧 / 次弧：固定参数 $Q=Q(X)\ge 1$，按宽度 $Q/(qX)$ 的 Farey 剖分写 $\mathfrak{M}_E(Q)$、$\mathfrak{m}_E(Q)=[0,1)\setminus\mathfrak{M}_E(Q)$。  
（下标 $E$ 强调：此处剖分服务 **$1_E$ 的加性 Fourier**，不必与圆法表示函数 $f_4f_3f_2$ 的 $\mathfrak{M}(Q)$ 取同一 $Q$；对接时再对齐。）

二进采样和（L-FW 的 $\Phi_N(0)$）
$$
S_E(N)=\sum_{k=1}^{K}1_E(N-2^k)=\#\bigl(W(N)\cap E\bigr).
$$
偏差
$$
\mathrm{Dev}_E(N)=S_E(N)-\delta_E(2^{K+1})\,K.
$$

---

## L-EFD-1（已证）— Plancherel 与 Roth 尺度结算

**(A) Plancherel.**
$$
\int_0^1\bigl|\widehat{1_E}(\alpha;X)\bigr|^2\,\mathrm{d}\alpha
=\sum_{m=1}^{X}1_E(m)
=|E\cap[1,X]|.
$$
对平衡函数同理
$$
\int_0^1\bigl|\widehat{f_E}(\alpha;X)\bigr|^2\,\mathrm{d}\alpha
=\sum_{m=1}^{X}\bigl(1_E(m)-\delta_E(X)\bigr)^2
=|E\cap[1,X]|\,\bigl(1-\delta_E(X)\bigr)
\asymp|E\cap[1,X]|.
$$

**(B) Roth 代入.** 在骨架界下
$$
\int_0^1\bigl|\widehat{1_E}(\alpha;X)\bigr|^2\,\mathrm{d}\alpha
\ll\frac{X}{(\log X)^{1/20}}.
$$
因而对任意可测 $\mathfrak{m}\subset[0,1)$，
$$
\int_{\mathfrak{m}}\bigl|\widehat{1_E}(\alpha;X)\bigr|^2\,\mathrm{d}\alpha
\ll\frac{X}{(\log X)^{1/20}}.
$$

**(C) 目标形尺度校正.** 用户形目标
$$
\int_{\mathfrak{m}}\bigl|\widehat{1_E}\bigr|^2\ll\frac{X^2}{(\log X)^{c}}
$$
对稀疏 $E$ **弱于** (B)：因 $X/(\log)^{1/20}=o\!\bigl(X^2/(\log)^{c}\bigr)$。故「可引用的次弧 $L^2$ 积分 $\ll X^2/(\log)^c$」在 Roth 下已平凡成立，**不**构成对 E-kill 的新杠杆。  
本路线的有效硬度核改为：

1. **点态次弧界**（EFD-Pt$_{c}$）：$\alpha\in\mathfrak{m}_E(Q)$ 时 $|\widehat{1_E}(\alpha;X)|\ll X/(\log X)^{c}$ 或 $\ll|E|/L$；  
2. **缺项加权次弧界**（EFD-$L^2_g(c)$）：见 L-EFD-5。

**证明.** (A) 展开平方，正交性消去交叉项。(B) 用定理 B。(C) 比较两个上界。证毕。

**定位.** L-EFD-1 把「次弧 $L^2$ 积分 $\ll X^2/(\log)^c$」标为**已结算的过弱目标**；真正要证明的是点态或 $g$-加权衰减。

---

## L-EFD-2（已证）— 与可表集指示的关系

令 $\mathcal{R}_{4,3,2}^{\le X}=\mathcal{R}_{4,3,2}\cap[1,X]$。则对 $m\in\{1,\ldots,X\}$，
$$
1_E(m)=1-1_{\mathcal{R}_{4,3,2}}(m)
$$
（约定 $1\notin\mathcal{R}_{4,3,2}$ 时两边一致；有限初值不影响渐近）。因而
$$
\widehat{1_E}(\alpha;X)=D_X(\alpha)-\widehat{1_{\mathcal{R}}}(\alpha;X),
$$
其中 $D_X(\alpha)=\sum_{m=1}^{X}e(\alpha m)$，$|D_X(\alpha)|\le\min(X,1/(2\|\alpha\|))$，且
$$
\widehat{1_{\mathcal{R}}}(\alpha;X)=\sum_{m\le X}1_{\mathcal{R}_{4,3,2}}(m)\,e(\alpha m).
$$

**注.** $\widehat{1_{\mathcal{R}}}$ **不是**圆法生成函数 $F=f_4f_3f_2$：后者编码表示数 $r(m)$，而此处仅编码支撑。由 $r(m)\ge 1_{\mathcal{R}}(m)$ 得比较
$$
\bigl|\widehat{1_{\mathcal{R}}}(\alpha;X)\bigr|
\le\sum_{m\le X}r(m)=\bigl(P_4+1\bigr)\bigl(P_3+1\bigr)\bigl(P_2+1\bigr)
\asymp X^{\beta},\qquad\beta=\tfrac{13}{12},
$$
但该上界远大于 $X$，对次弧衰减**无用**。有效控制必须走「薄集 $E$」侧（L-EFD-1）或「$1_{\mathcal{R}}$ 的伪随机 / 圆法支撑结构」侧（缺口 EFD-G1）。

**证明.** 指示恒等式逐点成立；Dirichlet 核界标准。证毕。

---

## L-EFD-3（已证）— 二进采样的连续 Fourier 表示（桥引理）

设 $N\ge 3$，$K=\lfloor\log_2(N-1)\rfloor$，并取 $X\ge N-2$（例如 $X=2^{K+1}$）。则对每个 $1\le k\le K$ 有 $1\le N-2^k\le X$，且
$$
S_E(N)
=\int_0^1\widehat{1_E}(\alpha;X)\,e(-\alpha N)\,g_N(\alpha)\,\mathrm{d}\alpha.
$$
等价地，用平衡函数
\begin{align*}
S_E(N)
&=\delta_E(X)\,K
+\int_0^1\widehat{f_E}(\alpha;X)\,e(-\alpha N)\,g_N(\alpha)\,\mathrm{d}\alpha
\\
&\quad+\delta_E(X)\Bigl(\int_0^1 D_X(\alpha)\,e(-\alpha N)\,g_N(\alpha)\,\mathrm{d}\alpha-K\Bigr).
\end{align*}
当 $X\ge N-2$ 且 $N-2^k\in[1,X]$ 时，末项括号为 $0$（因 $\int D_X e(-\alpha(N-2^k))=1$），故
$$
S_E(N)=\delta_E(X)\,K+\int_0^1\widehat{f_E}(\alpha;X)\,e(-\alpha N)\,g_N(\alpha)\,\mathrm{d}\alpha,
$$
即
$$
\mathrm{Dev}_E(N)=\int_0^1\widehat{f_E}(\alpha;X)\,e(-\alpha N)\,g_N(\alpha)\,\mathrm{d}\alpha
$$
（取 $\delta_E$ 在 $X=2^{K+1}$ 时与定义一致，差 $o(K\delta_E)$ 可吸收）。

**证明.** 反演：对每个 $k$，
$$
1_E(N-2^k)=\int_0^1\widehat{1_E}(\alpha;X)\,e\bigl(-\alpha(N-2^k)\bigr)\,\mathrm{d}\alpha.
$$
对 $k$ 求和得
$$
\sum_k e\bigl(-\alpha(N-2^k)\bigr)=e(-\alpha N)\,g_N(\alpha).
$$
平衡形式：把 $1_E=\delta_E+(1_E-\delta_E)$ 代入，主项给出 $\delta_E K$。证毕。

**与 L-FW 对照.** L-FW-2 的 Plancherel 是对 $\Phi_N(\alpha)=\sum_k a_N(k)e(\alpha k)$ 在频率 $\alpha$（对 $k$）积分；本式把同一 $S_E(N)=\Phi_N(0)$ 写成 **$m$-侧** Fourier 与 $g_N$ 的内积。二者共享检测对象 $S_E$，分析轴不同。

---

## L-EFD-4（已证）— 主弧 / 次弧分裂与平凡次弧贡献

固定 $Q\ge 1$，写
$$
\mathrm{Dev}_E(N)=\mathrm{Dev}_{\mathfrak{M}}+\mathrm{Dev}_{\mathfrak{m}},
$$
$$
\mathrm{Dev}_{\mathfrak{M}}
=\int_{\mathfrak{M}_E(Q)}\widehat{f_E}(\alpha;X)\,e(-\alpha N)\,g_N(\alpha)\,\mathrm{d}\alpha,
\quad
\mathrm{Dev}_{\mathfrak{m}}
=\int_{\mathfrak{m}_E(Q)}\cdots.
$$

**(A) 次弧平凡 CS 界（已证）.** 由 Cauchy–Schwarz、L-EFD-1 与 $\int|g_N|^2=K$，
\begin{align*}
\bigl|\mathrm{Dev}_{\mathfrak{m}}\bigr|
&\le\Bigl(\int_{\mathfrak{m}_E}\bigl|\widehat{f_E}\bigr|^2\Bigr)^{1/2}
\Bigl(\int_{\mathfrak{m}_E}|g_N|^2\Bigr)^{1/2}
\\
&\le\Bigl(\int_0^1\bigl|\widehat{f_E}\bigr|^2\Bigr)^{1/2}K^{1/2}
\ll\bigl(|E\cap[1,X]|\bigr)^{1/2}K^{1/2}
\ll\frac{X^{1/2}K^{1/2}}{(\log X)^{1/40}}.
\end{align*}
对二进窗尺度 $X\asymp N\asymp 2^K$，右端 $\asymp 2^{K/2}K^{1/2}/K^{O(1)}$，**远大于** $K$，故**不能**排除 $\mathrm{Dev}_E=K(1-\delta_E)$（整窗）。

**(B) 主弧模型项（已证形式）.** 在 $0$ 附近的主弧上，$\widehat{f_E}(\alpha;X)$ 的主贡献来自均值零的平衡；若仅取中心弧 $|\alpha|\le Q/X$ 并用 $|g_N|\le K$，得
$$
\bigl|\mathrm{Dev}_{\mathfrak{M}\cap\{|\alpha|\le Q/X\}}\bigr|
\ll\frac{Q}{X}\cdot\|f_E\|_{\ell^1}\,K
\ll Q\,\delta_E(X)\,K,
$$
在 $Q=(\log X)^{O(1)}$、$\delta_E\ll(\log)^{-1/20}$ 时为 $o(K)$。非零有理主弧 $a/q$（$q\le Q$）的贡献取决于 $\widehat{f_E}(a/q+\beta)$ 的局部结构——**无额外输入时不可一律 $o(K)$**（对照 L08：结构化薄集可在有理点携带大 Fourier 质量）。

**证明.** (A) CS + Plancherel + L-Circ-9 的 $\int|g|^2=K$。(B) $|\widehat{f_E}|\le\|f_E\|_1\le 2|E|$ 与弧长 $O(Q/X)$。证毕。

**结算.** 仅用 Roth+$L^2$ 全环面能量，次弧贡献的 CS 上界过大；杀整窗需要 **点态** 或 **$|g_N|$ 加权** 的真衰减（L-EFD-5/6）。

---

## L-EFD-5（条件式）— 缺项加权次弧衰减 $\Rightarrow$ 偏差 $o(K)$

**假设（EFD-$L^2_g(c)$）.** 存在 $c>0$、$Q=Q(X)\ge 1$、$X_0$，使对一切 $X\ge X_0$ 与一切满足 $X/2<N\le X$ 的 $N$（或至少一切二进段 $2^K<N\le 2^{K+1}$，$X=2^{K+1}$），
$$
\int_{\mathfrak{m}_E(Q)}\bigl|\widehat{f_E}(\alpha;X)\bigr|^2\,|g_N(\alpha)|^2\,\mathrm{d}\alpha
\ll\frac{K^2\,|E\cap[1,X]|}{(\log X)^{c}}
\quad\text{或更强}\quad
\ll\frac{K^2}{(\log X)^{c}}.
$$
（弱形右端含 $|E|$ 时，配合 $\delta_E\ll(\log)^{-1/20}$ 仍可能够用，见下。）

**结论.** 若另有主弧控制假设 **EFD-Maj$_\eta$**：
$$
\bigl|\mathrm{Dev}_{\mathfrak{M}}\bigr|\le K^{1-\eta}\qquad(\eta>0,\ K\ge K_0),
$$
则对大 $K$，
$$
\bigl|\mathrm{Dev}_E(N)\bigr|\le\tfrac12 K,
$$
从而 $S_E(N)\le\delta_E K+K/2<K$（因 $\delta_E\le 1/2$ 对大 $X$），故 $N\notin\mathcal{F}_0$。特别地，若对所有大二进段上一切 $N$ 成立，则 $\mathcal{F}_0$ 有限。

**证明.** 由 CS，
$$
\bigl|\mathrm{Dev}_{\mathfrak{m}}\bigr|
\le\Bigl(\int_{\mathfrak{m}}\bigl|\widehat{f_E}\bigr|^2|g_N|^2\Bigr)^{1/2}
\ll\frac{K}{(\log X)^{c/2}}
\quad\text{（强形）},
$$
或弱形 $\ll K\,(|E|/X)^{1/2}/(\log)^{c/2}\ll K/(\log)^{1/40+c/2}$。取 $K$ 大使该量 $<K/4$，再与 EFD-Maj$_\eta$ 的 $<K/4$ 相加。证毕。

**缺口.** EFD-$L^2_g(c)$ 与 EFD-Maj$_\eta$ 对真实 $E$ 均未证。弱于「全环面把 $|g_N|^2$ 权重随便加上」：L-EFD-4(A) 表明无次弧截断时权重积分可与 $|E|K$ 同阶，给出 $\mathrm{Dev}\ll(|E|K)^{1/2}$ 过大。

---

## L-EFD-6（条件式）— 点态次弧界 $\Rightarrow\mathcal{F}_0$ 有限

**假设（EFD-Pt$_{c,\theta}$）.** 存在 $c>0$、$\theta\in(0,1)$、$Q=X^{\theta}$，使对一切大 $X$ 与一切 $\alpha\in\mathfrak{m}_E(Q)$，
$$
\bigl|\widehat{f_E}(\alpha;X)\bigr|
\ll\frac{X}{(\log X)^{c}}.
$$

**辅助输入.** 引用 L-Circ-9：$\|g_N\|_1\le K^{1/2}$ 不够；改用
$$
\int_{\mathfrak{m}_E}|g_N|
\le\mathrm{meas}(\mathfrak{m}_E)^{1/2}\|g_N\|_2
\le K^{1/2},
$$
仍得 $|\mathrm{Dev}_{\mathfrak{m}}|\ll X(\log)^{-c}K^{1/2}$，对 $X\asymp 2^K$ 更大。故 **单独 EFD-Pt 配平凡 $L^1(g)$ 不够**。

**加强点态假设（EFD-Pt♯$_{c}$）.** 存在 $c>1$ 使
$$
\sup_{\alpha\in\mathfrak{m}_E(Q)}\bigl|\widehat{f_E}(\alpha;X)\,g_N(\alpha)\bigr|
\ll\frac{K}{(\log X)^{c}},
$$
且 $\mathrm{meas}(\mathfrak{m}_E)\le 1$，则 $|\mathrm{Dev}_{\mathfrak{m}}|\ll K/(\log)^{c}$。

**更可用的混合形（EFD-Hyb$_{c}$）.** 存在 $c>0$ 使
$$
\int_{\mathfrak{m}_E(Q)}\bigl|\widehat{f_E}(\alpha;X)\,g_N(\alpha)\bigr|\,\mathrm{d}\alpha
\ll\frac{K}{(\log X)^{c}}.
$$

**结论.** 在 EFD-Hyb$_{c}$（$c>0$）+ EFD-Maj$_\eta$（$\eta>0$）下，$\mathcal{F}_0$ 有限（论证同 L-EFD-5）。EFD-Pt♯$_{c}$（$c>1$）蕴含 EFD-Hyb。

**证明.** $|\mathrm{Dev}_{\mathfrak{m}}|$ 被 Hyb 右端控制；与主弧假设拼合后 $|\mathrm{Dev}_E|<K/2$，同 L-EFD-5。证毕。

**与用户「点态界」的对齐.** 可引用目标应写成 EFD-Pt♯ / EFD-Hyb / EFD-$L^2_g$，而非裸 $|\widehat{1_E}|\ll X/(\log)^c$ 配 $|g|\le K$（后者次弧贡献 $\ll X K/(\log)^c\cdot\mathrm{meas}$，尺度错误）。

---

## L-EFD-7（已证）— 整窗迫使大偏差；与 L-FW-7 的接口

设 $N\in\mathcal{F}_0$，$X=2^{K+1}$，$\delta_E(X)\le 1/2$。则 $S_E(N)=K$，故
$$
\mathrm{Dev}_E(N)=K\bigl(1-\delta_E(X)\bigr)\ge\tfrac12 K.
$$
由 L-EFD-3，
$$
\Bigl|\int_0^1\widehat{f_E}(\alpha;X)\,e(-\alpha N)\,g_N(\alpha)\,\mathrm{d}\alpha\Bigr|\ge\tfrac12 K.
$$
因而：任一强制
$$
\sup_{2^K<N\le 2^{K+1}}\bigl|\mathrm{Dev}_E(N)\bigr|=o(K)
$$
的衰减假设（例如 L-EFD-5/6 的结论形）都与大 $K$ 整窗矛盾。

**对照 L-FW-7.** L-FW-7 在 **$k$-频率** 上写 $\mathrm{Dev}_N(\alpha)=\Phi_N(\alpha)-\delta_E D_K(\alpha)$，整窗给出低频 $|\mathrm{Dev}_N|\gg K^{1-\theta}$。本条在 **$m$-频率** 上写同一事件 $\mathrm{Dev}_E(N)\ge K/2$。二者可并行作为杀伤前提，但**证伪假设的解析输入不同**：FW-Unif 需二进轨道伪随机；EFD-Hyb 需 $1_E$ 的连续 Fourier 对 $g_N$ 加权取消。

**证明.** $N\in\mathcal{F}_0\Rightarrow S_E=K$；$\delta_E\le 1/2$ 时偏差 $\ge K/2$；代入 L-EFD-3。证毕。

---

## L-EFD-8（草案 / 结构）— 由混合幂圆法期待的衰减来源

启发式来源（**非定理**）：

1. **Roth 稀薄.** $E$ 密度 $\ll(\log)^{-1/20}$ 已写入 L-EFD-1；不足伪随机。  
2. **可表集的局部随机性.** 若 $1_{\mathcal{R}}$ 在次弧上接近其奇异级数均值，则 $\widehat{f_E}=-\widehat{f_{\mathcal{R}}}$ 在 $\mathfrak{m}_E$ 上应有取消；精确化需把支撑指示换成光滑权重（回到 $r(m)$ 与 $F=f_4f_3f_2$），并控制 $r(m)\in\{0,1\}$ 与 $r(m)\ge 2$ 的多重表示误差——缺口 EFD-G1。  
3. **与假设 H 的关系.** H 控制 $\int_{\mathfrak{m}}|F|$；EFD 控制 $\widehat{1_E}$。二者经 $1_{\mathcal{R}}\le r$ **不**互相蕴含：H 是 P2 充分大可表路线；EFD 是 P1 薄集 Fourier 路线。  
4. **L08 障碍.** 抽象密度零集可有 $|\widehat{1_E}(a/q)|\asymp|E|$ 于固定 $q$，使主弧外仍大；故 EFD-Maj / EFD-Hyb 必须吃进 $\mathcal{R}_{4,3,2}$ 结构，不能仅从密度推出（平行 L-Rand-7 / L-Pack-8）。

---

## L-EFD-9（缺口表）

| 编号 | 内容 | 对 E-kill 的作用 |
|------|------|------------------|
| **EFD-G1** | 由 $F=f_4f_3f_2$ / 圆法支撑结构推出真实 $E$ 的次弧 Fourier 衰减（点态或 $g$-加权） | 关闭 EFD-Hyb / $L^2_g$ |
| **EFD-G2** | 非零有理主弧上 $\widehat{f_E}(a/q+\beta)$ 的一致 $o(K/\|g\|)$ 控制（EFD-Maj$_\eta$） | 主弧半边 |
| **EFD-G3** | 证明 EFD-Hyb$_{c}$ 或 EFD-$L^2_g(c)$（$c>0$）对真实 $E$ | 条件式杀伤变无条件 |
| **EFD-G4** | 与 FW-Unif / AE-Rand 的蕴含图：是否 EFD-Hyb $\Rightarrow$ FW-Unif 或反之 | 路线合并 / 避免重复 |
| **EFD-G5** | 显式 $Q=X^{\theta}$ 与可发表 $c$ | 有效范围 |

**不可写为定理的部分.** 「Roth $\Rightarrow$ 次弧 $|\widehat{1_E}|$ 点态小」；「$\int_{\mathfrak{m}}|\widehat{1_E}|^2\ll X^2/(\log)^c\Rightarrow\mathcal{F}_0$ 有限」（左端已平凡，右端不随）。「L-EFD 已证原猜想」。

---

## 路线小结（对 P1）

| 编号 | 类型 | 对 E-kill-1 的作用 |
|------|------|-------------------|
| L-EFD-1 | 已证（结算） | Plancherel+Roth；校正 $X^2/(\log)^c$ 过弱 |
| L-EFD-2 | 已证 | $1_E=1-1_{\mathcal{R}}$；与 $F$ 的区别 |
| L-EFD-3 | 已证 | $S_E=\langle\widehat{1_E},e(-N\cdot)g_N\rangle$ 桥 |
| L-EFD-4 | 已证 | 主/次分裂；平凡 CS 次弧过大 |
| L-EFD-5 | 条件式 | EFD-$L^2_g$+Maj $\Rightarrow\mathcal{F}_0$ 有限 |
| L-EFD-6 | 条件式 | EFD-Hyb / Pt♯+Maj $\Rightarrow\mathcal{F}_0$ 有限 |
| L-EFD-7 | 已证 | 整窗 $\Rightarrow|\mathrm{Dev}_E|\ge K/2$；接 L-FW-7 |
| L-EFD-8 | 草案 | 衰减启发式；与 H / L08 边界 |
| L-EFD-9 | 缺口 | EFD-G1–G5 |

**本路线未证原猜想。** 主缺口：真实 $E$ 的连续 Fourier 对缺项核 $g_N$ 的次弧加权取消（EFD-G1/G3），以及非零主弧（EFD-G2）。与 L-FW 并行：FW 杀「$k$-谱指纹」，EFD 杀「$m$-谱 × lacuna」偏差。
