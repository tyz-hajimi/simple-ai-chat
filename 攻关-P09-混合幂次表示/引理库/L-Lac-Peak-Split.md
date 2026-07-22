# L-Lac-*：缺项尖峰/平坦分裂（路线 R4-Lac-Peak-Split）

> 路线 **R4-Lac-Peak-Split**（P09 攻关轮次 4，服务 **P2 / H′**）。  
> 底座：L-Circ-9（$\int|g|^2=K$）与对抗审查 §4（$\sqrt K$ 不够破 $\beta=13/12<2$）。  
> 新想法：把 $[0,1)$ 分裂为尖峰集 $\mathrm{Peak}$ 与平坦集 $\mathrm{Flat}$，分别做主弧型/相位对齐与点态 $|g|$ 改进。  
> 状态标记：`已证` / `条件式` / `缺口`。**不声称假设 H、H′ 或原猜想已证。**

---

## 0. 记号

沿用 L-Circ / L-Dec：
$$
P_j=\lfloor N^{1/j}\rfloor,\qquad
f_j(\alpha)=\sum_{1\le u\le P_j}e(\alpha u^j),\qquad
F:=f_4f_3f_2,
$$
$$
\beta=\tfrac14+\tfrac13+\tfrac12=\tfrac{13}{12},\qquad
K=\lfloor\log_2 N\rfloor,\qquad
g(\alpha)=\sum_{k=1}^{K}e(\alpha 2^k).
$$
主弧 $\mathfrak{M}(Q)$、次弧 $\mathfrak{m}(Q)$ 按宽度 $Q/(qN)$（$1\le Q\le N^{1/2}$）。圆法目标尺度（含缺项）为
$$
\mathfrak{M}_{\mathrm{targ}}:=K\,N^{1/12}
$$
（主项期望量级；次弧需 $o(\mathfrak{M}_{\mathrm{targ}})$ 才有希望闭合充分大表示）。

固定参数 $\delta\in(0,1/4]$。定义
$$
\lambda:=K^{1/2+\delta},\qquad
\mathrm{Peak}:=\bigl\{\alpha\in[0,1):|g(\alpha)|\ge\lambda\bigr\},\qquad
\mathrm{Flat}:=[0,1)\setminus\mathrm{Peak}.
$$
因而在 $\mathrm{Flat}$ 上点态 $|g|\le K^{1/2+\delta}$。

**弱次弧输入族（条件式，非定理）.** 对 $\theta\ge 0$，记假设
$$
\mathrm{F\text{-}weak}(\theta):\qquad
\int_{\mathfrak{m}(Q)}|F|\,\mathrm{d}\alpha\ll_{\varepsilon} N^{1/12+\theta+\varepsilon}
$$
（对某一固定可取的 $Q=N^{\kappa}$，$\kappa\in(0,1/2]$）。特别地：L-Dec-2 给出无条件 $\theta=11/24$（略 $\varepsilon$）；假设 H 对应某 $\theta=-\delta'<0$（**未证**）。

---

## L-Lac-1（已证）— Chebyshev 尖峰测度

由 L-Circ-9，$\int_0^1|g|^2=K$，故对任意 $\lambda>0$，
$$
\mathrm{meas}(\mathrm{Peak})=\mathrm{meas}\{|g|\ge\lambda\}\le\frac{K}{\lambda^2}.
$$
取 $\lambda=K^{1/2+\delta}$ 得
$$
\mathrm{meas}(\mathrm{Peak})\le K^{-2\delta}.
$$

**证明.** Markov/Chebyshev：$K=\int|g|^2\ge\lambda^2\mathrm{meas}(\mathrm{Peak})$。证毕。

**注.** 相对平凡 $|g|\le K$（此时「Peak」可为全环面），本界把尖峰测度压到 $(\log N)^{-2\delta}$ 级；**仅是对数小，不是 $N$ 的负幂。**

---

## L-Lac-2（已证）— Peak / Flat 分裂引理（可引用形）

对任意可测 $E\subseteq[0,1)$ 与任意可积 $F$，
$$
\int_E|Fg|
=\int_{E\cap\mathrm{Peak}}|Fg|
+\int_{E\cap\mathrm{Flat}}|Fg|.
$$
进而有可引用上界
\begin{align}
\int_{E\cap\mathrm{Flat}}|Fg|
&\le K^{1/2+\delta}\int_E|F|,\\[4pt]
\int_{E\cap\mathrm{Peak}}|Fg|
&\le K\int_{E\cap\mathrm{Peak}}|F|
\le K\cdot\mathrm{meas}(\mathrm{Peak})^{1-1/p}\|F\|_{L^p(E)}
\end{align}
对任意 $p\in[1,\infty]$（$p=\infty$ 时约定 $\mathrm{meas}^{0}=1$）。特别取 $p=1$、Chebyshev 与 $p=2$：
\begin{align}
\int_{E\cap\mathrm{Peak}}|Fg|
&\le K\int_E|F|,\\[2pt]
\int_{E\cap\mathrm{Peak}}|Fg|
&\le K\cdot K^{-\delta}\|F\|_{L^2(E)}
=K^{1-\delta}\|F\|_{L^2(E)},\\[2pt]
\int_{E\cap\mathrm{Peak}}|Fg|
&\le K\cdot K^{-2\delta}\,\|F\|_{L^\infty(E)}
=K^{1-2\delta}\,\|F\|_{L^\infty(E)}.
\end{align}

**证明.** Flat 点态界即定义；Peak 用 $|g|\le K$ 与 Hölder。第二条用 $\mathrm{meas}(\mathrm{Peak})^{1/2}\le K^{-\delta}$（L-Lac-1）。证毕。

**相对平凡对照.** 若处处用 $|g|\le K$，则 $\int_E|Fg|\le K\int_E|F|$。分裂后 Flat 段把因子 $K$ 换成 $K^{1/2+\delta}$，**节省因子** $K^{1/2-\delta}=(\log N)^{1/2-\delta}$；Peak 段测度 $\le K^{-2\delta}$，但若只喂 $\|F\|_1$ 或 $\|F\|_\infty$，仍见下表——**对数节省不能替代幂次缺口。**

---

## L-Lac-3（已证）— Flat 段与 $F$ 拼合的无条件界

取 $E=\mathfrak{m}(Q)$ 或 $E=[0,1)$。由 L-Dec-2 的**全环面**界（次弧积分不超过全环面；R4 审计标签）与 L-Lac-2，
$$
\int_{\mathrm{Flat}}|Fg|\ll_{\varepsilon} K^{1/2+\delta}N^{13/24+\varepsilon}.
$$
与目标 $\mathfrak{M}_{\mathrm{targ}}=K N^{1/12}$ 的比值为
$$
\frac{K^{1/2+\delta}N^{13/24}}{K N^{1/12}}
=K^{-1/2+\delta}\,N^{11/24}.
$$
故 Flat 单独贡献仍比目标大约 $N^{11/24}/(\log N)^{O(1)}$；**H-gap 的幂次部分原样残留。**

若改用平凡 $|g|\le K$，同一 $L^1(F)$ 输入给出比目标大约 $N^{11/24}$（无对数改善）。因此分裂在 Flat 上相对平凡 **仅多出 $(\log N)^{1/2-\delta}$ 杠杆**，与 L-Circ-9 的 $\sqrt K$ 同族。

---

## L-Lac-4（已证）— Peak 段：测度/范数型无条件界（无相位输入）

在次弧 $E=\mathfrak{m}(Q)$ 上，结合 L-Circ-7 的点态
$$
|F(\alpha)|\ll N^{13/12}Q^{-1/2}(\log 2N)^{1/2}
\qquad(\alpha\in\mathfrak{m}(Q))
$$
（$f_3,f_4$ 取平凡界）与 L-Lac-2 的 $L^\infty$ 形，
$$
\int_{\mathrm{Peak}\cap\mathfrak{m}(Q)}|Fg|
\ll K^{1-2\delta}N^{13/12}Q^{-1/2}(\log 2N)^{1/2}.
$$
取 $Q=N^{1/2}$ 得 $\ll K^{1-2\delta}N^{13/12-1/4}(\log N)^{O(1)}=K^{1-2\delta}N^{5/6}(\log N)^{O(1)}$，对目标比
$$
\frac{K^{1-2\delta}N^{5/6}}{K N^{1/12}}
=K^{-2\delta}N^{3/4}\to\infty.
$$
改用 $L^2$ 形：以自然尺度 $\|F\|_2\ll_{\varepsilon}N^{7/12+\varepsilon}$（由 $\|f_4f_3\|_2\|f_2\|_\infty$ 与 L-Dec-1 注同阶控制，或 Cauchy 于 Parseval），
$$
\int_{\mathrm{Peak}}|Fg|\ll_{\varepsilon} K^{1-\delta}N^{7/12+\varepsilon},
$$
对目标比 $\asymp K^{-\delta}N^{1/2}\to\infty$。

**结论（无相位）.** 仅用 Chebyshev 测度 + $F$ 的已有 $L^p$/Weyl 点态，Peak 误差 **远大于** $\mathfrak{M}_{\mathrm{targ}}$；分裂本身不关闭 Peak。

---

## L-Lac-5（条件式接口）— 主弧型 / $2^k$ 相位对齐模板

**结构事实（标准，可引用框架）.** 若 $|g(\alpha)|$ 显著大于 $K^{1/2}$，则 $\alpha$ 在倍映射下不能长期远离整数：存在整数 $m\le K$ 与整数 $a$，使得
$$
\bigl\|2^m\alpha-a\bigr\|\ll_{\varepsilon} K^{O(1)}\lambda^{-2+\varepsilon}
$$
（或等价地 $\alpha$ 落入某个分母为 $2^{O(m)}$ 的二进主弧 $\mathfrak{M}_{2}$）。证明路线：展开
$$
|g|^2=K+2\mathrm{Re}\sum_{1\le j<k\le K}e\bigl(\alpha\,2^j(2^{k-j}-1)\bigr),
$$
大值迫使某些差 $2^j(2^{b}-1)$ 的相位对齐，从而 $\alpha$ 靠近 $2$-进有理点。记
$$
\mathrm{Peak}\subseteq\mathfrak{M}_{2}(\eta)\cup\mathcal{E}_{\mathrm{err}},
$$
其中 $\eta=\eta(K,\delta)$ 为对齐宽度，$\mathrm{meas}(\mathfrak{M}_{2}(\eta))\ll K^{O(1)}\eta$。

**条件式 Peak 处理（Peak-Maj）.** 若进一步有
$$
\mathrm{Peak}\cap\mathfrak{m}(Q)\subseteq\mathcal{E}_{\mathrm{err}}
\quad\text{且}\quad
\int_{\mathcal{E}_{\mathrm{err}}}|Fg|=o\bigl(K N^{1/12}\bigr),
$$
则 Peak 对次弧的贡献可吸收；Peak 落入 $\mathfrak{M}(Q)$ 的部分并入主弧奇异级数分析（**非**次弧误差）。

**缺口 Lac-G1.** 二进主弧 $\mathfrak{M}_{2}$ 与多项式主弧 $\mathfrak{M}(Q)$ **不对齐**：存在 $\alpha$ 使 $g$ 尖峰但 $\alpha\in\mathfrak{m}(Q)$（分母 $2^m$ 相对于 $Q$「错误」或宽度不足）。无额外定理不能断言 $\mathrm{Peak}\subset\mathfrak{M}(Q)$。  
**缺口 Lac-G2.** 即使 $\mathrm{Peak}\subset\mathfrak{M}_{2}$，仍需对 $\mathfrak{M}_{2}\cap\mathfrak{m}(Q)$ 上的 $F$ 给出强于 L-Dec 的节省，或证明该交的测度为 $N^{-c}$；Chebyshev 的 $K^{-2\delta}$ 不够。

本条 **不**提供已证的 Peak 次弧界；仅登记「相位对齐 ⇒ 主弧吸收」的条件式接口。

---

## L-Lac-6（条件式）— 与 $F=f_4f_3f_2$ 拼合的节省表

在假设 $\mathrm{F\text{-}weak}(\theta)$ 下，取 $E=\mathfrak{m}(Q)$，由 L-Lac-2：
$$
\int_{\mathrm{Flat}\cap\mathfrak{m}}|Fg|
\ll_{\varepsilon} K^{1/2+\delta}N^{1/12+\theta+\varepsilon}.
$$
相对目标 $K N^{1/12}$ 的过剩因子为
$$
\Xi_{\mathrm{Flat}}(\theta,\delta):=K^{-1/2+\delta}\,N^{\theta}.
$$
要 $\Xi_{\mathrm{Flat}}\le(\log N)^{-A}$（任意固定 $A$），必须
$$
\theta\log N\le\bigl(\tfrac12-\delta\bigr)\log K+O_A(\log\log N),
$$
即
$$
\theta\le\frac{(\tfrac12-\delta)\log\log N+O(1)}{\log N}=o(1).
$$
**任何固定 $\theta>0$ 都使 Flat 在 $N\to\infty$ 时爆炸。**

| 输入 $\theta$（$\mathrm{F\text{-}weak}$） | Flat 过剩 $\Xi_{\mathrm{Flat}}$ | Peak（无相位，L-Lac-4） | 相对平凡 $|g|\le K$ 的净增益 | 能否 $\ll\mathfrak{M}_{\mathrm{targ}}$ |
|--:|--:|--:|--:|--:|
| $11/24$（L-Dec-2，无条件） | $K^{-1/2+\delta}N^{11/24}$ | $\gg N^{1/2}K^{-O(1)}$ | Flat 多 $(\log N)^{1/2-\delta}$ | 否 |
| $1/8$（示意弱次弧） | $K^{-1/2+\delta}N^{1/8}$ | 同左列阶或更大 | 同上对数 | 否 |
| $c\frac{\log\log N}{\log N}$ | $(\log N)^{O(1)}$ | 仍需 Peak 定理 | 对数级 | Flat 临界；Peak 仍开 |
| $0$（恰 $N^{1/12}$） | $K^{-1/2+\delta}$ | 需 Peak-Maj | Flat 已 $o(1)$ 若再降 $\delta$ | **仅当 Peak 被主弧吸收** |
| $-\delta'<0$（假设 H） | $K^{-1/2+\delta}N^{-\delta'}$ | 同上 | 强于目标的 Flat | **H′ 仍要 Peak 接口** |

**H′ 的可陈述条件式形（登记，未证）.**  
$$
\mathrm{H}'(\delta,A):\quad
\int_{\mathfrak{m}}|Fg|\,\mathrm{d}\alpha\ll K N^{1/12}(\log N)^{-A}.
$$
由上表：$\mathrm{F\text{-}weak}(\theta)+\text{L-Lac-2}$ 推出 H′ **当且仅当** $\theta$ 已是 $o(\log\log N/\log N)$ **且** Peak 由 Lac-G1/G2 关闭。故 H′ **不是**「弱于 H 的免费推论」；它把 H 的负担拆成「几乎-H 的 $F$ 积分 + 尖峰主弧吸收」。

---

## L-Lac-7（结算）— 半无条件「显式 $N\ge N_0$」不可达

**问题.** 相对平凡 $|g|\le K$，在「假设 $F$ 的弱次弧界 $\mathrm{F\text{-}weak}(\theta)$（固定 $\theta>0$）」下，Peak/Flat 分裂能否推出某显式 $N_0$ 使一切 $N\ge N_0$ 的次弧贡献 $<\tfrac12\mathfrak{M}_{\mathrm{targ}}$（半无条件有效范围）？

**答案：不能。**

**障碍（写清）.**

1. **Flat 只吃对数.** 分裂把 $|g|\le K$ 改进为 $|g|\le K^{1/2+\delta}$，过剩从 $N^{\theta}$ 降为 $N^{\theta}/(\log N)^{1/2-\delta}$。对固定 $\theta>0$（含已证最佳 $\theta=11/24$），$N^{\theta}/(\log N)^{C}\to\infty$，不存在有限 $N_0$ 使 Flat $<\tfrac12\mathfrak{M}_{\mathrm{targ}}$。
2. **Peak 测度非幂小.** $\mathrm{meas}(\mathrm{Peak})\le K^{-2\delta}$ 是 $(\log N)^{-O(1)}$；与需要的 $N^{-c}$（来自 $\|F\|_\infty\sim N^{13/12}$ 或 $\|F\|_2\sim N^{7/12}$）差一个真幂次。增大 $\delta$ 只改善对数，且 $\delta\le 1/4$ 时 $\lambda=K^{1/2+\delta}$ 仍 $\ll K$。
3. **弱次弧不蕴含相位对齐.** $\mathrm{F\text{-}weak}(\theta)$ 是关于 $F$ 的积分假设，不给出「$|g|$ 大 $\Rightarrow\alpha\in\mathfrak{M}(Q)$」。Lac-G1/G2 仍在；Peak 不能在「仅假设弱 $F$」下半无条件关闭。
4. **与对抗审查 §4 同墙.** 缺口核心仍是 $N^{11/24}$ 对 $\sqrt K$：分裂精修了 $\sqrt K$ 杠杆的使用位置（Flat），但不产生新的 $N^{-\rho}$ 因子。$\beta=13/12<2$ 的二阶墙未被触动。
5. **若把 $\theta$ 降到 $o(\log\log N/\log N)$.** 则已本质假设「几乎 H」，半无条件范围问题退化成 H 本身；Peak 仍需独立的主弧吸收定理——**不是**本分裂引理的推论。

**可保留的正面产出.**  
- L-Lac-1/2：可引用的分裂与测度引理（已证）。  
- L-Lac-6 表：把 H′ 精确改写为「$F$ 几乎达 $N^{1/12}$ + Peak-Maj」，避免「缺项免费闭合 H」的伪证明（对照审查阻断 5）。  
- 组织性：后续若证明 Peak$\subset\mathfrak{M}(Q)$ 的真定理，可直接插入 L-Lac-5 接口而不改 Flat 算术。

---

## 状态总表

| 编号 | 摘要 | 状态 |
|------|------|------|
| L-Lac-1 | $\mathrm{meas}(\mathrm{Peak})\le K^{-2\delta}$ | 已证 |
| L-Lac-2 | Peak/Flat 分裂与三类 Peak 范数界 | 已证 |
| L-Lac-3 | Flat + L-Dec-2：仍余 $N^{11/24}/(\log N)^{O(1)}$ | 已证 |
| L-Lac-4 | Peak 无相位：对目标比 $\to\infty$ | 已证 |
| L-Lac-5 | 相位对齐 / Peak-Maj 接口 | 条件式；缺口 Lac-G1/G2 |
| L-Lac-6 | $\mathrm{F\text{-}weak}(\theta)$ 节省表与 H′ 改写 | 条件式结算 |
| L-Lac-7 | 固定 $\theta>0$ 时无显式 $N\ge N_0$ | 已证（否证半无条件捷径） |

**假设 H、H′、原猜想：均保持未证。**
