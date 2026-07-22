# L-Ekill-SS：奇异级数局部

## L-Ekill-SS-1（已证）

对 $f=x^4+y^3+z^2$，局部密度（若按通常奇异级数定义存在）满足
$$
\sigma_p(m)\ge p^{-2}
$$
对所有素数 $p$ 与所有整数 $m$。故无单素数局部不可解阻碍。

**证明概要.** 模 $p$ 存在非奇异解后 Hensel 提升。$p=2,3$ 直接检查；$p\ge 5$ 用 Cauchy–Davenport 得 $A+B+C=\mathbb{F}_p$，并取非奇异代表。

## L-Ekill-SS-2（条件式）

若存在 $A>0$ 使 $\mathfrak{S}(m)\ge(\log m)^{-A}\Rightarrow m\in\mathcal{R}_{4,3,2}$（充分大），则充分大 $N\in\mathcal{F}_0$ 时
$$
\max_{1\le k\le K/2}\mathfrak{S}(N-2^k)\ll_A(\log N)^{-A}.
$$

**缺口.** 圆法阈值：奇异级数对数下界 $\Rightarrow$ 可表。  
**R5 改写.** 该前置在假设 $\mathrm{H}_{\mathrm{thr}}(A)$ 下由 **L-Thr-3**（已证蕴含）给出；主弧半边见 **L-Thr-1**（已证）。全阈值仍开放（Thr-G1）。详见 `L-Thr.md`。
