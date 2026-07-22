# L-Rand：Roth 密度随机模型与 E-kill 边界（路线 R5-Random-Model-Boundary）

> 路线 **R5-Random-Model-Boundary**（P09 攻关轮次 5，对抗性 + 构造，服务理解真实 $E$ 难度）。  
> 目标：在「Roth 级」边际密度 $\delta_m\approx c/(\log m)^\kappa$ 下，计算整窗概率与失败级数，写出可检验边界引理 **L-Rand-***；澄清「Roth $1/20$ 指数」与「E-kill 所需」的定量鸿沟。  
> **不是**原猜想证明；**不**声称真实 $E$ 上 $\mathcal{F}_0$ 有限；禁止数值模拟（仅解析计算）。

---

## 0. 符号与两种随机模型

沿用：
$$
W(N)=\{N-2^k:1\le k\le K\},\qquad
K=\lfloor\log_2(N-1)\rfloor,\qquad
\mathcal{F}_0=\{N\ge 2:W(N)\subseteq E\}.
$$
随机例外集记为 $\widetilde{E}$，随机失败集
$$
\widetilde{\mathcal{F}}_0=\{N\ge 2:W(N)\subseteq\widetilde{E}\}.
$$

固定常数 $c>0$、指数 $\kappa>0$，取边际
$$
\delta_m=\frac{c}{(\log(m+2))^\kappa}\qquad(m\in\mathbb{N}_0).
$$
（$+2$ 仅避免 $\log 1$；渐近同 $c/(\log m)^\kappa$。）此选择模拟 Roth 型上界
$$
|E\cap[1,X]|\ll\frac{X}{(\log X)^{1/20}}
$$
的**平均密度轮廓**（骨架定理 B 取 $\kappa=1/20$）。

### 模型 R（完全独立 Bernoulli）

各 $m$ **独立**，且 $\mathbb{P}(m\in\widetilde{E})=\delta_m$。

### 模型 S（边际预算内的尺度种植 / 极大窗耦合）

选取稀疏中心 $N_K=2^K+2^{\lfloor K/2\rfloor}$（$K\ge K_0$ 充分大），使窗 $W(N_K)$ 两两不相交。令
$$
p_K:=\min_{m\in W(N_K)}\delta_m\asymp\frac{c}{K^\kappa}.
$$
独立掷币 $\xi_K\sim\mathrm{Bernoulli}(p_K)$：若 $\xi_K=1$ 则强制 $W(N_K)\subset\widetilde{E}$；对其余点（及种植失败的窗点）再独立补入 Bernoulli 残差，使全体边际仍为 $\mathbb{P}(m\in\widetilde{E})=\delta_m$。  
（可行性：种植对单点贡献概率 $\le p_K\le\delta_m$，残差概率 $\delta_m-p_K^{(\mathrm{hit})}\ge 0$。）

---

## L-Rand-1（已证：整窗概率的精确式与期望计数）

在模型 R 下，对任意 $N\ge 3$，
$$
\mathbb{P}\bigl(W(N)\subseteq\widetilde{E}\bigr)
=\prod_{m\in W(N)}\delta_m
=\prod_{k=1}^{K}\frac{c}{\bigl(\log(N-2^k+2)\bigr)^\kappa}.
$$
从而期望失败计数（可为 $+\infty$）
$$
\mathbb{E}\bigl[|\widetilde{\mathcal{F}}_0|\bigr]
=\sum_{N\ge 2}\mathbb{P}(N\in\widetilde{\mathcal{F}}_0)
=\sum_{N\ge 2}\prod_{k=1}^{K(N)}\delta_{N-2^k}.
$$

**证明.** 独立性把交集概率写成乘积；取期望并对示性函数用 Fubini（非负）即得级数。证毕。

---

## L-Rand-2（已证：乘积的对数渐近）

设 $N\in(2^K,2^{K+1}]$，$K\ge 3$。记
$$
\Pi(N):=\prod_{k=1}^{K}\delta_{N-2^k}.
$$
则存在仅依赖 $c,\kappa$ 的常数 $C_1,C_2>0$，使对充分大 $K$，
$$
\exp\bigl(-C_1\,K\log K\bigr)
\le\Pi(N)
\le\exp\bigl(-C_2\,K\log K\bigr)
\le K^{-c'K}
$$
对某 $c'=c'(\kappa)>0$。特别地，对任意固定 $A<\infty$，
$$
\Pi(N)\ll_A N^{-A}.
$$

**证明.** 对 $1\le k\le K-2$ 有 $N-2^k\ge N-2^{K-2}>2^{K-1}$，故
$$
\log(N-2^k+2)\ge\log(2^{K-1})\ge (K-1)\log 2,
$$
从而
$$
\delta_{N-2^k}\le\frac{c}{((K-1)\log 2)^\kappa}.
$$
此种 $k$ 至少 $K-2$ 个，于是
$$
\Pi(N)
\le\Bigl(\frac{c}{((K-1)\log 2)^\kappa}\Bigr)^{K-2}
=\exp\bigl((K-2)(\log c-\kappa\log((K-1)\log 2))\bigr).
$$
对大 $K$ 括号内 $\le -\frac{\kappa}{2}\log K$，得上界 $\exp(-C_2 K\log K)$。

下界：每个因子 $\delta_{N-2^k}\ge c/(\log(N+2))^\kappa\ge c'/(K\log 2)^\kappa$，共 $K$ 个，同理得 $\exp(-C_1 K\log K)$。  
与多项式比较：$\exp(-C_2 K\log K)=K^{-C_2 K}\ll N^{-A}$。证毕。

---

## L-Rand-3（已证：模型 R 下级数收敛 — 任意 $\kappa>0$）

在模型 R 中，对**任意** $\kappa>0$ 与 $c>0$，
$$
\sum_{N\ge 2}\mathbb{P}(N\in\widetilde{\mathcal{F}}_0)<\infty,
$$
因而 $\mathbb{E}[|\widetilde{\mathcal{F}}_0|]<\infty$，且 $\widetilde{\mathcal{F}}_0$ **几乎必然有限**。

**证明.** 由 L-Rand-2，取 $A=2$，得 $\mathbb{P}(N\in\widetilde{\mathcal{F}}_0)\ll N^{-2}$，级数收敛。Borel–Cantelli 第一引理给出 a.s. 仅有限多个成功。证毕。

**注.** 收敛**不**需要 $\kappa>1$；$\kappa=1/20$（Roth）已落在本结论内。独立模型下「E-kill」的阈值是 $\kappa>0$，不是 $\kappa>1$。

---

## L-Rand-4（已证：边缘约束下的 Fréchet 窗概率界）

设 $\widetilde{E}$ 为**任意**随机集，仅要求 $\mathbb{P}(m\in\widetilde{E})=\delta_m$（允许任意相依）。则
$$
\mathbb{P}\bigl(W(N)\subseteq\widetilde{E}\bigr)
\le\min_{m\in W(N)}\delta_m
\ll\frac{1}{(\log N)^\kappa}.
$$
若窗事件可嵌套实现（存在事件 $A_N$ 使 $\{W(N)\subseteq\widetilde{E}\}=A_N$ 且 $\mathbb{P}(A_N)=\min\delta_m$），则上界可达阶 $(\log N)^{-\kappa}$。

**证明.** 事件 $\{W(N)\subseteq\widetilde{E}\}$ 含于每一个 $\{m\in\widetilde{E}\}$，$m\in W(N)$，故概率 $\le$ 最小边际。嵌套构造取 $m_\star=\mathrm{argmin}\,\delta_m$，令 $A_N=\{m_\star\in\widetilde{E}\}$ 并在 $A_N$ 上将其余窗点一并放入，即达上界（需与全局边际预算协调时改为尺度种植，见模型 S）。证毕。

---

## L-Rand-5（已证：模型 S 的级数临界指数 $\kappa=1$）

在模型 S 下，记种植失败示性 $\eta_K=1_{\{W(N_K)\subseteq\widetilde{E}\}}$。则 $\mathbb{P}(\eta_K=1)=p_K\asymp K^{-\kappa}$，且 $\{\eta_K\}$ 独立，并有
$$
\sum_{K\ge K_0}\mathbb{P}(N_K\in\widetilde{\mathcal{F}}_0)
=\sum_{K\ge K_0}p_K
\begin{cases}
<\infty,&\text{若 }\kappa>1,\\
=\infty,&\text{若 }\kappa\le 1.
\end{cases}
$$

因此：

1. **若 $\kappa>1$：** $\sum p_K<\infty\Rightarrow$ 几乎必然仅有限多个 $K$ 发生种植；残差独立 Bernoulli 部分由 L-Rand-3 对任意 $\kappa>0$ 贡献 a.s. 有限失败。故 $\widetilde{\mathcal{F}}_0$ **几乎必然有限**，且 $\mathbb{E}[|\widetilde{\mathcal{F}}_0|]<\infty$。  
2. **若 $\kappa\le 1$：** $\sum p_K=\infty$ 且独立，Borel–Cantelli 第二引理 $\Rightarrow$ a.s. 无穷多个种植成功 $\Rightarrow\widetilde{\mathcal{F}}_0$ **几乎必然无限**。

**证明.** 积分判别：$\sum_{K\ge 2}K^{-\kappa}<\infty\iff\kappa>1$。其余由模型 S 的定义与 L-Rand-3 拼合。证毕。

---

## L-Rand-6（已证：可检验断言汇总）

下列断言均可仅用 L-Rand-1…5 的解析估计检验（无数值实验）：

| 断言 | 模型 | 结论 |
|------|------|------|
| A | R（独立） | **任意** $\kappa>0$：$\,\mathbb{E}|\widetilde{\mathcal{F}}_0|<\infty$ 且 $\widetilde{\mathcal{F}}_0$ a.s. 有限 |
| B$_+$ | S（种植） | $\kappa>1$：$\widetilde{\mathcal{F}}_0$ a.s. 有限（期望失败集有限） |
| B$_-$ | S（种植） | $\kappa\le 1$：$\widetilde{\mathcal{F}}_0$ a.s. **无限** |
| C | 任意边际耦合 | $\mathbb{P}(W(N)\subseteq\widetilde{E})\le\min\delta_m\ll(\log N)^{-\kappa}$；二进子列上 $\sum_K\mathbb{P}\ll\sum K^{-\kappa}$，于 $\kappa>1$ 收敛 |

**与题述对照.** 「若 $\kappa>1$ 则期望失败集几乎必然有限；若 $\kappa\le 1$ 则可能无限」在**模型 S / 极大窗耦合**下成立且尖锐（B$_+$/B$_-$）。独立模型 R 更强：阈值降至 $\kappa>0$（断言 A）。

---

## L-Rand-7（已证对照：Roth $1/20$ 与 E-kill 的定量鸿沟）

骨架 Roth 型界对应密度指数 $\kappa_{\mathrm{Roth}}=1/20$。

1. **独立随机世界（模型 R）**  
   $\kappa_{\mathrm{Roth}}=1/20>0$，L-Rand-3 $\Rightarrow$ 随机 $\widetilde{\mathcal{F}}_0$ a.s. 有限。  
   故：**若**真实 $E$ 在二进窗上表现得像独立 Bernoulli，则现行 $1/20$ **已够** E-kill，无需把指数升到 $1$。

2. **边际预算内的对抗世界（模型 S）**  
   $\kappa_{\mathrm{Roth}}=1/20\le 1$，L-Rand-5 $\Rightarrow$ 存在与 Roth 同级边际相容的耦合，使 $\widetilde{\mathcal{F}}_0$ a.s. 无限。  
   即使把密度指数改进到任意 $\kappa\le 1$（例如 $1$、$1-\varepsilon$），对抗种植仍可使失败无限；只有 $\kappa>1$ 才从**尺度种植级数**上封死该机制。

3. **确定性密度世界（对照 L08）**  
   存在密度 $0$ 的抽象 $E$（远稀于任何 $X/(\log X)^\kappa$）使 $\mathcal{F}_0$ 无限。  
   故把 Roth 指数从 $1/20$ 升到 $1000$ **仍不**蕴涵确定性 E-kill。

4. **鸿沟的正确读法**  
   $$
   \underbrace{1/20}_{\text{Roth 密度幂}}
   \;<\;
   \underbrace{1}_{\text{尺度种植临界}}
   \;\ll\;
   \underbrace{+\infty}_{\text{L08：仅密度永远不够}}.
   $$
   - 「升到 $\kappa>1$」只关闭模型 S 的种植级数，**不是**真实 $E$ 的 E-kill 定理。  
   - 真实 E-kill 的缺失增量是**反整窗 / 二进伪随机**（排除最坏耦合），而非把 $1/20$ 改成 $>1$ 的密度指数。  
   - 启发式「Roth + 窗口随机 $\Rightarrow\mathcal{F}_0$ 有限」把模型 R 的结论误套到真实 $E$；对抗审查 T1 / L08 已否证该跳步。

**一句话.** Roth $1/20$ 在独立模型下已超 E-kill 阈值；在对抗边际模型下低于种植临界 $1$；在确定性范畴则任何有限指数都不够。定量鸿沟是**相依结构**，不是单一实数指数的差距。

---

## 缺口登记（本路线不关闭）

| 编号 | 内容 | 状态 |
|------|------|------|
| Rand-G1 | 真实 $E$ 的二进窗是否接近模型 R（混合/弱相关） | 未证；即 E-kill 本质增量 |
| Rand-G2 | 真实 $E$ 是否排除模型 S 型正种植率 $p_K\gg K^{-1}$ | 未证 |
| Rand-G3 | 由圆法/行列式导出窗上近似独立或反嵌套 | 未证（对接 FW-Unif / Det-Occ / AE-Corr） |

---

## 结算

| 编号 | 状态 | 摘要 |
|------|------|------|
| L-Rand-1 | 已证 | $\mathbb{P}(W(N)\subseteq\widetilde{E})=\prod\delta_m$；$\mathbb{E}|\widetilde{\mathcal{F}}_0|=\sum\prod\delta$ |
| L-Rand-2 | 已证 | $\Pi(N)=\exp(-\Theta(K\log K))\ll N^{-A}$ |
| L-Rand-3 | 已证 | 模型 R：任意 $\kappa>0\Rightarrow\sum\mathbb{P}<\infty$，a.s. 有限 |
| L-Rand-4 | 已证 | 任意耦合：$\mathbb{P}\le\min\delta_m\ll(\log N)^{-\kappa}$ |
| L-Rand-5 | 已证 | 模型 S：$\kappa>1$ a.s. 有限；$\kappa\le 1$ a.s. 无限 |
| L-Rand-6 | 已证 | 可检验断言 A / B$_+$ / B$_-$ / C |
| L-Rand-7 | 已证对照 | Roth $1/20$ vs 种植临界 $1$ vs L08；鸿沟在相依结构 |

**本轮结论.** 边界引理 L-Rand-* 写清：独立 Bernoulli 下任意正对数幂已杀 $\widetilde{\mathcal{F}}_0$；尺度种植模型在 $\kappa=1$ 尖锐；Roth $1/20$ 落在「对抗可无限、独立已有限」的夹缝。E-kill-1 对真实 $E$ 仍开放，需排除最坏耦合而非单纯抬升密度指数。原猜想保持开放。
