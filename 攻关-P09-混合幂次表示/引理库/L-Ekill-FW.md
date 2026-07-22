# L-Ekill-FW：二进特征 / Walsh–Fourier 整窗检测（路线 R1-Fourier-Walsh）

> 服务目标：**P1 = E-kill-1**（真实 $E$ 上 $\mathcal{F}_0$ 有限）。  
> 本文件为**新路线**，不改写 L-Ekill-A2-1/SS-1；与 A2 的「差集相关」正交，改用尺度 $K$ 上的特征检测量。  
> 状态标记：`已证` / `条件式` / `缺口`。**不声称原猜想已证。**

## 0. 记号

沿用全局符号：$E=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2}$，$K=\lfloor\log_2(N-1)\rfloor$，
$$
W(N)=\{N-2^k:1\le k\le K\},\qquad
\mathcal{F}_0=\{N\ge 2:W(N)\subseteq E\}.
$$
令 $e(\theta)=e^{2\pi i\theta}$。对 $N\ge 3$ 写二进采样指示序列
$$
a_N(k)=1_E(N-2^k),\qquad 1\le k\le K.
$$
**Fourier 型检测量**（加性频率 $\alpha\in\mathbb{R}/\mathbb{Z}$）
$$
\Phi_N(\alpha)=\sum_{k=1}^{K}a_N(k)\,e(\alpha k).
$$
**Walsh / 乘性检测量**：设 $\mathcal{X}_M$ 为模 $M$ 的 Dirichlet 特征全体（含主特征 $\chi_0$），对 $\chi\in\mathcal{X}_M$ 令
$$
\Phi_N(\chi)=\sum_{k=1}^{K}a_N(k)\,\chi(k)
$$
（约定 $k$ 与 $M$ 不互素时 $\chi(k)=0$，若需完全支撑可改用 $\chi(|k|)$ 于 $1\le k\le K$ 的完全乘性扩张或直接用 Walsh–Paley 系，见 L-FW-2 注）。  
区间 Dirichlet 核
$$
D_K(\alpha)=\sum_{k=1}^{K}e(\alpha k)=e\bigl(\tfrac{\alpha(K+1)}{2}\bigr)\frac{\sin(\pi K\alpha)}{\sin(\pi\alpha)}\quad(\alpha\notin\mathbb{Z}),
$$
并约定 $D_K(0)=K$。标准界
$$
|D_K(\alpha)|\le\min\Bigl(K,\ \frac{1}{2\|\alpha\|}\Bigr).
$$

---

## L-FW-1（已证）— 平凡特征检测整窗

对任意 $N\ge 3$，
$$
\Phi_N(0)=\sum_{k=1}^{K}a_N(k)=\#\bigl(W(N)\cap E\bigr).
$$
因而
$$
N\in\mathcal{F}_0\iff\Phi_N(0)=K\iff\bigl|\Phi_N(0)\bigr|=K.
$$
若 $\chi_0$ 为主特征且在 $\{1,\ldots,K\}$ 上恒为 $1$（取 $M=1$ 或忽略非互素截断），则同样有 $\Phi_N(\chi_0)=K\iff N\in\mathcal{F}_0$。

**证明.** 由 $a_N(k)\in\{0,1\}$ 得 $\sum_k a_N(k)=K$ 当且仅当每个 $a_N(k)=1$，即 $W(N)\subseteq E$。证毕。

---

## L-FW-2（已证）— Plancherel / 二进采样能量恒等式

**(A) 连续 Fourier.** 以 $\mathbb{R}/\mathbb{Z}$ 上 Haar 测度（总质量 $1$）计，
$$
\int_0^1\bigl|\Phi_N(\alpha)\bigr|^2\,\mathrm{d}\alpha=\sum_{k=1}^{K}a_N(k)=\Phi_N(0).
$$

**(B) 有限加性群.** 令 $M\ge K$，在 $\mathbb{Z}/M\mathbb{Z}$ 上令 $\widehat a_N(r)=\sum_{k=1}^{K}a_N(k)\,e(rk/M)$，则
$$
\frac{1}{M}\sum_{r=0}^{M-1}\bigl|\widehat a_N(r)\bigr|^2=\sum_{k=1}^{K}a_N(k).
$$

**(C) Walsh–Paley 注记.** 若 $\{w_j\}_{j<2^m}$ 为定义在 $\{0,1\}^m$ 上的 Walsh 正交系，并将 $k\in[1,K]$（$K\le 2^m$）视为其二进位向量，则
$$
\frac{1}{2^m}\sum_{j}\Bigl|\sum_{k=1}^{K}a_N(k)w_j(k)\Bigr|^2=\sum_{k=1}^{K}a_N(k).
$$

**证明.** 展开平方：对角项给出 $\sum_k a_N(k)^2=\sum_k a_N(k)$；交叉项在正交性下消失。证毕。

**推论.** $\Phi_N(0)=K$ 时采样能量取最大可能值 $K$，且全部 $L^2$ 质量由「满支撑」序列承载；任意缺失 $k$ 使能量严格下降。

---

## L-FW-3（已证）— 整窗的谱指纹

设 $N\in\mathcal{F}_0$。则对一切 $\alpha\in\mathbb{R}/\mathbb{Z}$，
$$
\Phi_N(\alpha)=D_K(\alpha),
$$
因而
$$
\max_{\alpha}\bigl|\Phi_N(\alpha)\bigr|=K,
$$
且对任意 $\theta\in(0,1)$，在低频带 $\mathcal{L}_K(\theta)=\{\alpha:0<\|\alpha\|\le K^{-1+\theta}\}$ 上有
$$
\inf_{\alpha\in\mathcal{L}_K(\theta)}\bigl|\Phi_N(\alpha)\bigr|\ge c_\theta\,K^{1-\theta}
$$
（例如取 $\|\alpha\|=c'K^{-1+\theta}$ 使 $\sin(\pi K\alpha)/\sin(\pi\alpha)$ 的下界 $\ge c_\theta K^{1-\theta}$；常数 $c_\theta>0$ 仅依赖 $\theta$）。

对 Dirichlet 特征：若 $\chi$ 在 $\{1,\ldots,K\}$ 上处处非零且 $N\in\mathcal{F}_0$，则 $\Phi_N(\chi)=\sum_{k=1}^{K}\chi(k)$。

**证明.** $N\in\mathcal{F}_0\Rightarrow a_N\equiv 1$，故 $\Phi_N=D_K$。低频下界由 Dirichlet 核在 $\|\alpha\|\asymp K^{-1+\theta}$ 处的标准估计得出。乘性情形同理。证毕。

**要点.** 整窗并非「所有非平凡频率皆小」；相反，它在**低频非零**频率上仍给出 $|\Phi|\gg K^{1-\theta}$ 的刚性指纹。此与「高均匀性 / 伪随机」采样（高频与低频非主项皆小）相区分。

---

## L-FW-4（已证）— 由谱接近反演整窗

设 $0<\theta<\delta<1$。若某 $N$ 满足
$$
\bigl|\Phi_N(0)-K\bigr|<1
$$
（因 $\Phi_N(0)\in\mathbb{Z}$ 即 $\Phi_N(0)=K$），则 $N\in\mathcal{F}_0$。  
更一般地，若仅假设存在 $\alpha\in\mathcal{L}_K(\theta)$ 使
$$
\bigl|\Phi_N(\alpha)-D_K(\alpha)\bigr|<c_\theta K^{1-\theta},
$$
**不能**单独推出整窗；但若对**所有** $k\in\{1,\ldots,K\}$ 有 Fourier 反演控制
$$
\Bigl|a_N(k)-1\Bigr|=\Bigl|\int_0^1\bigl(\Phi_N(\alpha)-D_K(\alpha)\bigr)e(-\alpha k)\,\mathrm{d}\alpha\Bigr|<1,
$$
则 $a_N\equiv 1$，即 $N\in\mathcal{F}_0$。

**实用充分条件（已证其蕴含）.** 若
$$
\int_0^1\bigl|\Phi_N(\alpha)-D_K(\alpha)\bigr|\,\mathrm{d}\alpha<1,
$$
则对每个 $k$ 有 $|a_N(k)-1|<1$，故 $N\in\mathcal{F}_0$。

**证明.** 反演公式 $a_N(k)=\int\Phi_N(\alpha)e(-\alpha k)\,\mathrm{d}\alpha$，$1=\int D_K(\alpha)e(-\alpha k)\,\mathrm{d}\alpha$。差值绝对值 $\le\int|\Phi_N-D_K|$。若该积分 $<1$ 且 $a_N(k)\in\{0,1\}$，则 $a_N(k)=1$。证毕。

**缺口（精确）.** 将「积分 $<1$」减弱为「仅在 $\mathcal{L}_K(\theta)$ 上的点态下界 / $L^2$ 带通控制」需额外的带限逼近引理；尚未对真实 $E$ 验证。

---

## L-FW-5（条件式）— 低频均匀性 $\Rightarrow\mathcal{F}_0$ 有限

**假设（FW-Unif$_{E}(\delta,\theta)$）.** 存在 $\delta>\theta>0$ 与 $K_0$，使对一切 $K\ge K_0$、一切满足 $2^K<N\le 2^{K+1}$ 的整数 $N$、以及一切 $\alpha\in\mathcal{L}_K(\theta)$，
$$
\bigl|\Phi_N(\alpha)\bigr|\le K^{1-\delta}.
$$

**结论.** 在假设 FW-Unif$_{E}(\delta,\theta)$ 下，$\mathcal{F}_0$ 有限。

**证明.** 若 $N\in\mathcal{F}_0$ 且 $K=\lfloor\log_2(N-1)\rfloor\ge K_0$，则由 L-FW-3，
$$
\exists\,\alpha\in\mathcal{L}_K(\theta):\quad\bigl|\Phi_N(\alpha)\bigr|\ge c_\theta K^{1-\theta}.
$$
取 $K$ 充分大使 $c_\theta K^{1-\theta}>K^{1-\delta}$（因 $\delta>\theta$），与 FW-Unif 矛盾。故此类 $N$ 的 $K$ 有界，即 $\mathcal{F}_0$ 有限。证毕。

**缺口.** 假设 FW-Unif$_{E}(\delta,\theta)$ 对**真实**例外集 $E=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2}$ 尚未证明。该假设断言：$E$ 沿任意二进轨道 $\{N-2^k\}_{k\le K}$ 的采样，在低频加性特征下表现得像稀疏/伪随机序列，而不能接近满窗 Dirichlet 核。Roth 型上密度零**不足以**推出 FW-Unif（对照 L08：抽象密度零集可有无限 $\mathcal{F}_0$，此时在 $\mathcal{F}_0$ 点上 $|\Phi_N(\alpha)|=|D_K(\alpha)|$ 低频仍大）。

---

## L-FW-6（条件式）— $L^2$ 平均型杀伤准则

**假设（FW-$L^2$）.** 存在 $\delta>0$、$K_0$，使对一切 $K\ge K_0$，
$$
\frac{1}{2^K}\sum_{2^K<N\le 2^{K+1}}\ \sup_{\alpha\in\mathcal{L}_K(\theta)}\bigl|\Phi_N(\alpha)\bigr|^2\ \le\ K^{2-2\delta}
$$
对某个固定 $\theta\in(0,\delta)$ 成立。

**结论.** $\mathcal{F}_0$ 有限。

**证明.** 每个 $N\in\mathcal{F}_0\cap(2^K,2^{K+1}]$ 由 L-FW-3 贡献
$$
\sup_{\alpha\in\mathcal{L}_K(\theta)}\bigl|\Phi_N(\alpha)\bigr|^2\ge c_\theta^2 K^{2-2\theta}.
$$
故
$$
\frac{1}{2^K}\#\bigl(\mathcal{F}_0\cap(2^K,2^{K+1}]\bigr)\cdot c_\theta^2 K^{2-2\theta}\le K^{2-2\delta}.
$$
从而
$$
\#\bigl(\mathcal{F}_0\cap(2^K,2^{K+1}]\bigr)\le C\,2^K K^{-2(\delta-\theta)}.
$$
此上界 alone 不迫使计数为零。**加强版假设**：将左边的平均限制在「候选整窗」或改为
$$
\sum_{2^K<N\le 2^{K+1}}\sup_{\alpha\in\mathcal{L}_K(\theta)}\bigl|\Phi_N(\alpha)\bigr|^2\ \le\ K^{2-2\delta},
$$
（无 $2^K$ 归一；即总能量 $O(K^{2-2\delta})$）则右端 $<c_\theta^2 K^{2-2\theta}$（$K\gg 1$）迫使该二进段内 $\mathcal{F}_0$ 为空。下文记此加强为 **FW-$L^2$♯**。在 FW-$L^2$♯ 下 $\mathcal{F}_0$ 有限。证毕。

**缺口.** FW-$L^2$♯ 强于密度平均；需对真实 $E$ 的二进采样建立低频 $L^2$ 界。与 L-Ekill-A2-2 的反相关准则平行但谱侧重点不同：A2 控制差集对相关，FW 控制单轨道 Fourier 质量。

---

## L-FW-7（已证）— 与密度偏差的联结

令 $\delta_E(X)=|E\cap[1,X]|/X$。对固定 $k$ 与 $N\in(2^K,2^{K+1}]$，$m=N-2^k$ 遍历长度为 $2^K$ 的区间 $I_{K,k}\subset[1,2^{K+1}]$。故
$$
\sum_{2^K<N\le 2^{K+1}}\Phi_N(0)=\sum_{k=1}^{K}\bigl|E\cap I_{K,k}\bigr|.
$$
若采用 Roth 型界 $|E\cap[1,X]|\ll X/(\log X)^{1/20}$（骨架已采纳），则
$$
\frac{1}{2^K}\sum_{N}\Phi_N(0)\ll\frac{K}{(\log 2^K)^{1/20}}.
$$
定义偏差
$$
\mathrm{Dev}_N=\Phi_N(0)-\delta_E(2^{K+1})\cdot K.
$$
则平均 $|\mathrm{Dev}|$ 不能排除个别 $\mathrm{Dev}_N=K(1-\delta_E)$（即整窗）。  
**特征形式偏差**（对 $\alpha\neq 0$）
$$
\mathrm{Dev}_N(\alpha)=\Phi_N(\alpha)-\delta_E(2^{K+1})\,D_K(\alpha)
$$
满足：若 $N\in\mathcal{F}_0$ 且 $\delta_E\le 1/2$，则对 $\alpha\in\mathcal{L}_K(\theta)$，
$$
\bigl|\mathrm{Dev}_N(\alpha)\bigr|\ge\bigl(1-\delta_E\bigr)c_\theta K^{1-\theta}-\delta_E\cdot O\bigl(K^{1-\theta}\bigr)\gg K^{1-\theta}.
$$

**证明.** $\Phi_N=D_K$，故 $\mathrm{Dev}_N(\alpha)=(1-\delta_E)D_K(\alpha)$；代入 L-FW-3 下界即得。证毕。

**推论（条件式接口）.** 若真实 $E$ 满足「二进采样伪随机性」
$$
\sup_{2^K<N\le 2^{K+1}}\ \sup_{\alpha\in\mathcal{L}_K(\theta)}\bigl|\mathrm{Dev}_N(\alpha)\bigr|\ll K^{1-\delta}\qquad(\delta>\theta),
$$
则与上式 $\gg K^{1-\theta}$ 矛盾，故 $\mathcal{F}_0$ 在大 $K$ 为空（同 L-FW-5）。此即用户所述：比较 $\sum_{k\le K}1_E(N-2^k)$ 及其特征变换与 $K\cdot\delta_E$ / $\delta_E D_K$ 的偏差。

---

## L-FW-8（草案 / 乘性变体）— Pólya–Vinogradov 型对照

设 $\chi\bmod M$ 非主特征，$M\le K^{O(1)}$。完全和 $\sum_{k=1}^{K}\chi(k)\ll\sqrt{M}\log M$（Pólya–Vinogradov）。  
若 $N\in\mathcal{F}_0$，则 $\Phi_N(\chi)=\sum_{k=1}^{K}\chi(k)$，故 **高模乘性特征不会对整窗给出「大」指纹**（与低频加性情形相反）。  
因此：欲用乘性特征杀伤 $\mathcal{F}_0$，应检测
$$
\Phi_N(\chi)-\sum_{k=1}^{K}\chi(k)=-\sum_{k:\,a_N(k)=0}\chi(k)
$$
的**非零性**（缺孔的特征和），或改用 **Walsh 位函数**（依赖 $k$ 的低位）以重新获得类似 L-FW-3 的大相关。  

**缺口.** 乘性路线需另建「缺孔检测」引理；本轮主杀伤建议锚定 **L-FW-5 / L-FW-6♯ 的加性低频均匀性**。

---

## 路线小结（对 P1）

| 编号 | 类型 | 对 E-kill-1 的作用 |
|------|------|-------------------|
| L-FW-1 | 已证 | 平凡特征 $|\Phi|=K\Leftrightarrow$ 整窗 |
| L-FW-2 | 已证 | 能量恒等式；满窗最大 $L^2$ |
| L-FW-3 | 已证 | 整窗 $\Rightarrow$ 低频 $|\Phi|\gg K^{1-\theta}$ |
| L-FW-4 | 已证（蕴含） | 谱接近 $\Rightarrow$ 整窗的反演准则 |
| L-FW-5 | 条件式 | FW-Unif $\Rightarrow\mathcal{F}_0$ 有限 |
| L-FW-6 | 条件式 | FW-$L^2$♯ $\Rightarrow\mathcal{F}_0$ 有限 |
| L-FW-7 | 已证 + 接口 | 偏差形式；连结 $\delta_E$ 与伪随机 |
| L-FW-8 | 草案 | 乘性特征需改写检测对象 |

**本路线未证原猜想。** 主缺口：真实 $E$ 的 FW-Unif / FW-$L^2$♯（二进轨道低频伪随机性）。
