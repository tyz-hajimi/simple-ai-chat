# L-Osc-*：次弧缺项振荡积分（路线 R5-Minor-Oscillation）

> 路线 **R5-Minor-Oscillation**（P09 攻关轮次 5，服务 **P2**；来源：R4 审计建议 Dec-R4-1 /「破 $\beta/2$」）。  
> 目标形：在次弧上控制带缺项相位的振荡积分
> $$
> \Xi=\int_{\mathfrak{m}} f_4(\alpha)f_3(\alpha)f_2(\alpha)g(\alpha)e(-n\alpha)\,\mathrm{d}\alpha
> $$
> 至 $|\Xi|\ll N^{13/24-\delta}$，或给出**严格强于绝对值积分**的可发表部分取消。  
> 方法尝试：van der Corput / 指数对、stationary phase 失败时的双线性化、$g$ 尖峰对齐二进主弧后真次弧 Weyl 差分。  
> 状态标记：`已证` / `条件式` / `缺口`。**不声称假设 H、H′ 或原猜想已证。**

---

## 0. 记号与尺度

沿用 L-Circ / L-Dec / L-Lac：
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
主弧 $\mathfrak{M}(Q)$、次弧 $\mathfrak{m}(Q)$ 按宽度 $Q/(qN)$（$1\le Q\le N^{1/2}$）。圆法含缺项目标尺度
$$
\mathfrak{M}_{\mathrm{targ}}:=K\,N^{1/12}.
$$
写
$$
I_E(m):=\int_E F(\alpha)e(-m\alpha)\,\mathrm{d}\alpha,\qquad
\Xi:=\int_{\mathfrak{m}(Q)} F(\alpha)g(\alpha)e(-n\alpha)\,\mathrm{d}\alpha.
$$
对照绝对值包络
$$
\Xi_{\mathrm{abs}}(Q):=\int_{\mathfrak{m}(Q)}|Fg|\,\mathrm{d}\alpha.
$$
由 L-Dec-2（全环面）与 $|g|\le K$，
$$
\Xi_{\mathrm{abs}}(Q)\ll_{\varepsilon} K\,N^{13/24+\varepsilon}.
$$
闭合圆法误差需 $|\Xi|=o(\mathfrak{M}_{\mathrm{targ}})$；相对绝对值包络的幂次缺口仍为 $N^{11/24}$（H-gap）。

**二进主弧（本路线）.** 对参数 $R\le K$、$W\ge 1$，
$$
\mathfrak{M}_2(R,W):=\bigcup_{1\le r\le R}\bigcup_{\substack{0\le a<2^r\\ \gcd(a,2^r)=1}}\Bigl\{\alpha:\Bigl\|\alpha-\frac{a}{2^r}\Bigr\|\le\frac{W}{2^r N}\Bigr\},
$$
并记真次弧
$$
\mathfrak{m}^*:=\mathfrak{m}(Q)\setminus\mathfrak{M}_2(R,W).
$$
（与 L-Lac-5 的 Peak-Maj 接口兼容；本文件给可计算的 Weyl 拼合。）

---

## L-Osc-1（已证）— 缺项展开与频率采样

对任意可测 $E\subseteq[0,1)$，
$$
\int_E F(\alpha)g(\alpha)e(-n\alpha)\,\mathrm{d}\alpha
=\sum_{k=1}^{K} I_E(n-2^k).
$$
特别地
$$
\Xi=\sum_{k=1}^{K} I_{\mathfrak{m}(Q)}(n-2^k).
$$

**证明.** 把 $g=\sum_k e(\alpha 2^k)$ 代入并交换有限和与积分。证毕。

**注.** 于是 $\Xi$ 是 $F$ 在次弧截断后的 Fourier 系数在** lacuna 点集** $\{n-2^k\}_{k\le K}$ 上的采样和。绝对值方法对应 $\sum_k |I|$ 或 $\int|Fg|$；振荡方法试图利用诸 $I(n-2^k)$ 的符号/相位抵消。

---

## L-Osc-2（已证）— $L^2(g)$ 部分取消：具体指数 $K^{1/2}N^{13/24}$

设 $\|F\|_{L^2([0,1])}\ll_{\varepsilon} N^{13/24+\varepsilon}$（由均值主项：$\int|F|^2$ 的对角贡献 $\asymp P_4P_3P_2=N^{\beta}=N^{13/12}$，故 $\|F\|_2\asymp N^{\beta/2}=N^{13/24}$；上界可由华氏/VMVT 次临界矩经 Hölder 得到，与 L-Hua-2、L-Dec-1 注同阶）。则对任意 $Q$，
$$
|\Xi|
=\Bigl|\int_{\mathfrak{m}(Q)} Fg\,e(-n\alpha)\,\mathrm{d}\alpha\Bigr|
\le\|F\|_{L^2(\mathfrak{m})}\|g\|_{L^2(\mathfrak{m})}
\le\|F\|_2\|g\|_2
\ll_{\varepsilon} N^{13/24+\varepsilon}K^{1/2}.
$$
（末步用 L-Circ-9：$\int|g|^2=K$。）

**与绝对值对照.**
$$
\frac{N^{13/24}K^{1/2}}{K\,N^{13/24}}=K^{-1/2}=(\log N)^{-1/2}.
$$
故本界比 $\Xi_{\mathrm{abs}}$ **强因子 $(\log N)^{1/2}$**，是可发表的部分取消；**不是** $N^{-\delta}$ 幂次节省。

**相对目标.**
$$
\frac{N^{13/24}K^{1/2}}{K\,N^{1/12}}
=N^{11/24}K^{-1/2}\to\infty.
$$
距 $\mathfrak{M}_{\mathrm{targ}}$ 仍差 $N^{11/24}/(\log N)^{1/2}$。**不足以推出 H。**

---

## L-Osc-3（已证）— Hölder–矩族对 $(F,g)$ 的凸障碍（钉死 $K^{1/2}N^{13/24}$）

设已知矩输入不超过
$$
\|F\|_2\ll_{\varepsilon} N^{13/24+\varepsilon},\qquad
\int|g|^2=K,\qquad
\int|g|^4\ll K^{2},
\qquad |g|\le K.
$$
（末条 $\int|g|^4\ll K^{2}$：方程 $2^{k_1}+2^{k_2}=2^{k_3}+2^{k_4}$ 的解数 $\asymp K^{2}$，因二进和式本质唯一。）则对一切满足 $1/p+1/q=1$ 的 $p\in[1,2]$，
$$
\|F\|_p\|g\|_q
\gg_{\mathrm{scale}}
N^{13/24}K^{1/2}
$$
在已知上界下**不能改进**：凡用 $\|F\|_p\le\|F\|_2$ 与
$$
\|g\|_q\le\|g\|_2^{2/q}\|g\|_\infty^{1-2/q}\le K^{1/q}\cdot K^{1-2/q}=K^{1-1/q}
$$
（$q\in[2,\infty]$）者，乘积指数为
$$
N^{13/24}K^{1-1/q},
$$
于 $q=2$ 取最小值 $N^{13/24}K^{1/2}$；于 $q=\infty$ 退回 $N^{13/24}K$。特别取 $q=4$（$\|g\|_4\ll K^{1/2}$）仍得同阶。

**结论.** 在「仅用 $F$ 的 $L^2$ 均值 + $g$ 的 $L^{q\ge 2}$ 矩」方法族内，振荡积分的自然终点是
$$
|\Xi|\ll_{\varepsilon} N^{13/24+\varepsilon}K^{1/2},
$$
与 L-Osc-2 重合。**本族无法达到 $N^{13/24-\delta}$。**

**证明.** 由 $p\le 2\Rightarrow\|F\|_p\le\|F\|_2$ 与上列 $\|g\|_q$ 插值；$\int|g|^4\ll K^{2}$ 给出 $\|g\|_4\ll K^{1/2}$，与 $q=2$ 同阶。证毕。

**注（与 L-Hua-3 平行）.** L-Hua-3 钉死绝对值积分的 $\beta/2=13/24$；L-Osc-3 钉死「$F$–$g$ Hölder」振荡版本的对数终点 $K^{1/2}$。二者合成：无额外结构时
$$
|\Xi|\ll_{\varepsilon} N^{13/24+\varepsilon}K^{1/2}
\quad\text{是矩方法天花板}.
$$

---

## L-Osc-4（已证）— 双线性化（$f_4$ vs 其余）回收同一天花板

写 $H:=f_3f_2 g\,e(-n\cdot)$。由
$$
\Xi=\int_{\mathfrak{m}} f_4(\alpha)H(\alpha)\,\mathrm{d}\alpha
=\sum_{x\le P_4}\widehat{H\cdot 1_{\mathfrak{m}}}(-x^4),
$$
Cauchy 得
$$
|\Xi|^2
\le P_4\int_{\mathfrak{m}}|H|^2
\le P_4\int_0^1|f_3f_2 g|^2\,\mathrm{d}\alpha.
$$
用 $\int|f_3|^4\ll_{\varepsilon} P_3^{2+\varepsilon}$（华氏）与 $\int|f_2|^4\ll_{\varepsilon} P_2^{2+\varepsilon}N^{\varepsilon}$（平方和均值）及 Hölder，
$$
\int|f_3f_2|^2
\le\bigl(\int|f_3|^4\bigr)^{1/2}\bigl(\int|f_2|^4\bigr)^{1/2}
\ll_{\varepsilon} N^{1/3+1/2+\varepsilon}=N^{5/6+\varepsilon}.
$$
再以 $|g|\le K$ 得 $\int|H|^2\ll_{\varepsilon} K^2 N^{5/6+\varepsilon}$，从而
$$
|\Xi|^2\ll_{\varepsilon} N^{1/4}K^2 N^{5/6+\varepsilon}=K^2 N^{13/12+\varepsilon},
\qquad
|\Xi|\ll_{\varepsilon} K\,N^{13/24+\varepsilon}
$$
（绝对值级，无振荡增益）。若改用 $\int|f_3f_2|^2|g|^2$ 的粗估并借 $\int|g|^2=K$，在对角主导下仍回到
$$
|\Xi|\ll_{\varepsilon} N^{13/24+\varepsilon}K^{1/2}
$$
（与 L-Osc-2 一致；严格写需把 $|g|^2$ 展开为 lacuna 差分并控制 $\int|f_3f_2|^2 e(\alpha(2^k-2^{k'}))$，主项 $k=k'$ 给出因子 $K\cdot N^{5/6}$，开方后乘 $P_4^{1/2}$ 得 $K^{1/2}N^{13/24}$）。

**stationary phase 失败.** 次弧上 $\alpha\notin\mathfrak{M}(Q)$，连续奇异积分类相位的驻点落在主弧；在 $\mathfrak{m}$ 上「无驻点」所预言的额外衰减，一经把 $f_j$ 换为 Weyl/华氏均值，即落入 L-Dec-3 的凸插值族，最优端点仍为全环面 $N^{13/24}$（R4：次弧截断无临界矩增益）。故 **vdC / 驻相失败 $\not\Rightarrow$ 自动得到 $N^{13/24-\delta}$**。

---

## L-Osc-5（已证）— Weyl / 指数对点态插入不破天花板

沿用 L-Dec-3：对 $\theta\in[0,1]$、$Q\le N^{1/4}$，
$$
\int_{\mathfrak{m}(Q)}|F|
\ll_{\varepsilon}
N^{13/24+\varepsilon}
\bigl(N^{1/4}Q^{-1/8}\bigr)^{1-\theta}
N^{-(1-\theta)/8}
$$
一类凸族（精确式见 L-Dec-3），对 $\theta$ **严格递减**，最优于 $\theta=1$，即 $N^{13/24+\varepsilon}$。将 $|g|\le K$ 或 L-Osc-2 的 $\|g\|_2=K^{1/2}$ 乘入后，指数对（van der Corput 对 $(\kappa,\lambda)$）至多改进点态 Weyl 的 $Q$ 幂，从而只影响 $\theta<1$ 枝；**不能把 $\theta=1$ 端点压到 $N^{13/24-\delta}$**。

取 $Q=N^{1/4}$ 时 L-Circ-8 的 $\min(N^{19/24}Q^{-1/2},\ldots)=N^{61/96+\varepsilon}$ 乘 $K^{1/2}$ 得
$$
|\Xi|\ll_{\varepsilon} N^{61/96+\varepsilon}K^{1/2},
$$
而 $61/96-13/24=61/96-52/96=9/96>0$，**劣于** L-Osc-2。故在「点态 Weyl + 振荡 $L^2(g)$」下，仍应引用 L-Osc-2 而非 L-Circ-8。

---

## L-Osc-6（已证）— 尖峰对齐后真次弧的可引用拼合

固定 $\delta\in(0,1/4]$，Peak / Flat 如 L-Lac。分裂
$$
\Xi=\Xi_{\mathrm{Peak}}+\Xi_{\mathrm{Flat}},
$$
其中积分分别限制在 $\mathfrak{m}(Q)\cap\mathrm{Peak}$ 与 $\mathfrak{m}(Q)\cap\mathrm{Flat}$。

**(Flat).** 由 $|g|\le K^{1/2+\delta}$ 与 L-Dec-2，
$$
|\Xi_{\mathrm{Flat}}|
\le\int_{\mathrm{Flat}\cap\mathfrak{m}}|Fg|
\ll_{\varepsilon} K^{1/2+\delta}N^{13/24+\varepsilon}.
$$
与 L-Osc-2 同型；相对 $\mathfrak{M}_{\mathrm{targ}}$ 比值为 $N^{11/24}K^{-1/2+\delta}\to\infty$。

**(Peak ∩ 真次弧).** 在 $\mathfrak{m}^*$ 上用 $|g|\le K$ 与 L-Circ-8（$Q=N^{1/4}$）
$$
\int_{\mathfrak{m}^*}|F|
\le\int_{\mathfrak{m}(Q)}|F|
\ll_{\varepsilon} N^{61/96+\varepsilon},
$$
得
$$
|\Xi_{\mathrm{Peak}\cap\mathfrak{m}^*}|
\ll_{\varepsilon} K\,N^{61/96+\varepsilon}.
$$
相对 $\mathfrak{M}_{\mathrm{targ}}$：
$$
\frac{K\,N^{61/96}}{K\,N^{1/12}}=N^{61/96-8/96}=N^{53/96}\to\infty
$$
（即回到 L-Circ-8 的旧缺口，未用振荡）。若对 Peak 段改用 L-Osc-2 型 $L^2$，因 $\mathrm{meas}(\mathrm{Peak})\le K^{-2\delta}$（L-Lac-1）**不**自动改进 $\|F\|_{L^2(\mathrm{Peak})}$（$F$ 质量可集中在 Peak 上），无免费 $N^{-\rho}$。

**(Peak ∩ $\mathfrak{M}_2$).** 并入二进主弧分析（奇异级数 / 局部密度）；**不属于**次弧误差 $\Xi$ 的最终预算。此步依赖条件 Peak-Maj（L-Lac-5）：$\mathrm{Peak}\subseteq\mathfrak{M}_2(R,W)$（或对称差可忽略）。

**结算.** 无条件可引用的次弧振荡界仍是
$$
|\Xi|\ll_{\varepsilon} N^{13/24+\varepsilon}K^{1/2+\delta}
$$
（Flat + 全 Peak 用 L-Osc-2 / L-Lac）；真次弧 Weyl  alone 不提供优于 $13/24$ 的幂次。要去掉 Peak 必须 Peak-Maj（条件式）。

---

## L-Osc-7（条件式）— 突破天花板的接口

以下任一输入可把 $|\Xi|$ 压到 $o(\mathfrak{M}_{\mathrm{targ}})$ 或 $N^{13/24-\delta}K^{O(1)}$；**均未证**。

| 代号 | 陈述 | 若成立的后果 |
|------|------|----------------|
| Osc-G1 | lacuna 相关：$\bigl|\sum_{k\le K} I_{\mathfrak{m}}(n-2^k)\bigr|\ll_{\varepsilon} N^{13/24-\delta+\varepsilon}K^{1/2}$ 对几乎所有／一切大正 $n$ | 直接得目标形幂次；强于 L-Osc-2 |
| Osc-G2 | 非对角均值：$\sum_{k\neq k'}\bigl|I_{\mathfrak{m}}(n-2^k)\overline{I_{\mathfrak{m}}(n-2^{k'})}\bigr|\ll N^{13/12-\delta'}$ | Cauchy 展开破 L-Osc-3 |
| Osc-G3 | Peak-Maj（=Lac-G1）：$\mathrm{Peak}\subseteq\mathfrak{M}_2$ 至可忽略误差 | Peak 出次弧；Flat 留 $K^{1/2+\delta}N^{13/24}$，仍需几乎-H 的 $F$ 才闭合 |
| Osc-G4 | 真次弧幂次：$\int_{\mathfrak{m}^*}|F|\ll N^{1/12-\delta}$ | 即使 $|g|\le K$ 亦闭合 H 型；超出本路线矩方法 |

**兼容改写.** 假设 H（$\int_{\mathfrak{m}}|F|\ll N^{1/12-\delta}$）$\Rightarrow|\Xi|\ll K N^{1/12-\delta}=o(\mathfrak{M}_{\mathrm{targ}})$；本路线未证明 H。Osc-G1 是「只在 lacuna 采样点上」的弱 H，形式上弱于均匀 $|I(m)|$ 界，但是针对 $\Xi$ 的精确需求。

---

## L-Osc-8（已证）— 路线结算与障碍表

| 对象 | 可引用上界（略 $\varepsilon$） | 相对 $\Xi_{\mathrm{abs}}\le K N^{13/24}$ | 相对 $\mathfrak{M}_{\mathrm{targ}}=K N^{1/12}$ |
|------|-------------------------------|------------------------------------------|---------------------------------------------|
| L-Dec-2 绝对值 | $K N^{13/24}$ | $=$ | 缺口 $N^{11/24}$ |
| **L-Osc-2（本路线）** | **$K^{1/2} N^{13/24}$** | **强 $(\log N)^{1/2}$** | **缺口 $N^{11/24}/(\log N)^{1/2}$** |
| L-Circ-8 + $K^{1/2}$ | $K^{1/2} N^{61/96}$ | 劣于 L-Osc-2 | 缺口 $N^{53/96}/(\log N)^{1/2}$ |
| 目标 $N^{13/24-\delta}$ | — | 需 Osc-G1/G2 或超矩输入 | — |

**已证贡献.**
1. 振荡积分比绝对值积分强 $(\log N)^{1/2}$（L-Osc-2）；具体指数 $K^{1/2}N^{13/24}$。  
2. Hölder–矩族与 $f_4$-双线性化均钉死同一天花板（L-Osc-3/4）；vdC/指数对/驻相失败不自动破 $\beta/2$（L-Osc-5）。  
3. 尖峰–二进主弧分裂后，无条件段仍停在同一对数终点（L-Osc-6）。

**未证.** Osc-G1–G4；假设 H；原猜想。

**障碍一句话.** 破 $N^{13/24}$ 需 lacuna 频率上 $I_{\mathfrak{m}}(n-2^k)$ 的**非对角取消**（Osc-G1/G2），或 Peak-Maj + 几乎-H；二者皆超出「VMVT/华氏矩 + $g$ 的 $L^2$」工具包——与 R4 审计 Dec-R4-1 对齐。

---

## 状态总表

| 编号 | 陈述摘要 | 状态 |
|------|----------|------|
| L-Osc-1 | $\Xi=\sum_k I_{\mathfrak{m}}(n-2^k)$ | 已证 |
| L-Osc-2 | $|\Xi|\ll N^{13/24+\varepsilon}K^{1/2}$（部分取消） | 已证 |
| L-Osc-3 | $(F,g)$ Hölder–矩凸障碍：不能优于 L-Osc-2 | 已证 |
| L-Osc-4 | $f_4$-双线性化 / 驻相失败 $\Rightarrow$ 同天花板 | 已证 |
| L-Osc-5 | Weyl–指数对插入不破 $13/24$；L-Circ-8 枝更劣 | 已证 |
| L-Osc-6 | Peak/Flat + 真次弧 Weyl 拼合；无条件无 $N^{-\delta}$ | 已证 |
| L-Osc-7 | Osc-G1–G4 突破接口 | 条件式 |
| L-Osc-8 | 结算：对数取消已得；幂次墙仍在 | 已证（结算） |
