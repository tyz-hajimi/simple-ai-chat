# L-LSW：二进稀疏采样的大筛二次型与整窗计数（路线 R14-Large-Sieve-Window）

> 路线 **R14-Large-Sieve-Window**（P09 攻关轮次 14，服务 **P1 = E-kill-1**）。  
> 把二进窗点集 $\{N-2^k\}_{k\le K}$ 视为**稀疏采样点**，对例外集指示 $1_E$ 的二次型
> $$
> \sum_N\Bigl|\sum_k 1_E(N-2^k)\,c_k\Bigr|^2
> $$
> 给出大筛型上界，从而限制「许多 $N$ 同时整窗」的个数；在真实 $E$ 的 Roth 密度下得 $|\mathcal{F}_0\cap[1,X]|$ 的**定量上界**（可仍发散，但不依赖未证伪随机）。  
> **正交于** L-FW（$k$-谱指纹）、L-EFD（点态/加权次弧衰减杀窗）、L-AE / L-Inc（能量–团）、L-Pack（邻/倍窗装填）。本路线主轴是**全局二次型大筛**，不是单窗 Fourier 指纹。  
> 状态：`已证` / `条件式` / `缺口`。**不声称原猜想已证；不声称 $\mathcal{F}_0$ 有限。**

---

## 0. 记号与对象

沿用：$E=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2}$，$K=\lfloor\log_2(N-1)\rfloor$，
$$
W(N)=\{N-2^k:1\le k\le K\},\qquad
\mathcal{F}_0=\{N\ge 2:W(N)\subseteq E\}.
$$
二进采样和
$$
S_E(N)=\sum_{k=1}^{K}1_E(N-2^k)=\#\bigl(W(N)\cap E\bigr).
$$
整窗 $\Leftrightarrow S_E(N)=K$（L-FW-1）。对 $K\ge 2$ 写二进段
$$
I_K:=(2^K,\,2^{K+1}],\qquad
E_{\le Y}:=E\cap[1,Y],\qquad
M(Y):=|E_{\le Y}|.
$$
骨架 Roth 界（定理 B）
$$
M(Y)\ll\frac{Y}{(\log Y)^{1/20}}.
$$

对有限支撑复序列 $a=(a_m)_{m\in\mathbb{Z}}$ 与系数 $c=(c_k)_{1\le k\le K}$，定义**二进采样二次型**
$$
Q_K(a;c)
:=\sum_{N\in\mathbb{Z}}\Bigl|\sum_{k=1}^{K}a_{N-2^k}\,c_k\Bigr|^2.
$$
缺项核（与 L-Circ-9 / L-EFD 一致）
$$
g_c(\alpha)=\sum_{k=1}^{K}c_k\,e(-\alpha 2^k),\qquad
e(\theta)=e^{2\pi i\theta}.
$$
差表示
$$
r_a(d)=\sum_{m\in\mathbb{Z}}a_m\,\overline{a_{m+d}}.
$$
二进差集（半窗版同 L-AE；全窗版）
$$
\Delta_K^{\mathrm{full}}=\{2^k-2^\ell:1\le\ell<k\le K\}.
$$

**假设 LSW-Corr$_\eta$（二进差相关亏缺；条件式输入）.** 存在 $\eta>0$ 使对充分大 $K$ 与一切 $d\in\Delta_K^{\mathrm{full}}$，
$$
r_{1_E}(d)\le\frac{M(2^{K+1})}{K^\eta}.
$$
（近随机启发式：$r_E(d)\asymp M^2/2^K$ 更强；本假设仅要相对对角 $M$ 的多项式亏缺。）

**假设 LSW-Flat$_\theta$（缺项核 Flat 质量；条件式输入）.** 存在 $\theta\in(0,1/2]$ 与可测 $\mathrm{Flat}_K\subset[0,1)$，使
$$
|g_{(1,\ldots,1)}(\alpha)|\le K^{1-\theta}\quad(\alpha\in\mathrm{Flat}_K),
\qquad
\int_{\mathrm{Peak}_K}\bigl|\widehat{1_E}(\alpha;2^{K+1})\bigr|^2\,\mathrm{d}\alpha
\le K^{-2\theta}\,M(2^{K+1}),
$$
其中 $\mathrm{Peak}_K=[0,1)\setminus\mathrm{Flat}_K$。  
（对照 L-Lac Peak/Flat 测度引理；此处额外要求 $\widehat{1_E}$ 在 Peak 上的 $L^2$ 质量按 $K^{-2\theta}$ 衰减——强于仅 Roth 的全局 Plancherel。）

---

## L-LSW-1（已证）— 二次型展开与 Parseval 恒等式

设 $a$ 有限支撑，$c\in\mathbb{C}^K$。则

**(A) 差展开.**
$$
Q_K(a;c)
=\sum_{1\le k,\ell\le K}c_k\,\overline{c_\ell}\,r_a(2^k-2^\ell)
=\|c\|_2^2\sum_m|a_m|^2
+\sum_{k\neq\ell}c_k\,\overline{c_\ell}\,r_a(2^k-2^\ell).
$$

**(B) Parseval.** 令 $\widehat{a}(\alpha)=\sum_m a_m e(\alpha m)$，则
$$
Q_K(a;c)
=\int_0^1\bigl|\widehat{a}(\alpha)\bigr|^2\bigl|g_c(\alpha)\bigr|^2\,\mathrm{d}\alpha.
$$

**(C) 缺项核矩.**
$$
\int_0^1|g_c|^2\,\mathrm{d}\alpha=\|c\|_2^2,
\qquad
\|g_c\|_\infty\le\|c\|_1.
$$

**证明.** (A) 展开平方并平移 $m=N-2^\ell$。(B) 写
$$
\sum_k a_{N-2^k}c_k
=\int_0^1\widehat{a}(\alpha)\,e(-\alpha N)\,g_c(\alpha)\,\mathrm{d}\alpha,
$$
对 $N$ 用 Plancherel（或直接把 (A) 的 $r_a(d)=\int|\hat a|^2 e(-\alpha d)$ 代回）。(C) 因 $2^k$ 两两不同，
$$
\int e(\alpha(2^k-2^\ell))\,\mathrm{d}\alpha=\mathbf{1}_{k=\ell};
$$
$\|g_c\|_\infty$ 为三角不等式。证毕。

**定位.** L-LSW-1 是本路线的恒等式核；后续大筛界均由此出发。与 L-EFD-3（单点 $S_E(N)=\langle\hat{1_E},e(-N\cdot)g_N\rangle$）兼容，但本文件处理**$N$-平均二次型**而非单点偏差。

---

## L-LSW-2（已证）— 初等大筛 / CS 上界

对任意有限支撑 $a$ 与 $c\in\mathbb{C}^K$，
$$
Q_K(a;c)
\le K\,\|c\|_2^2\sum_m|a_m|^2.
$$
特别地取 $c_k\equiv 1$（故 $\|c\|_2^2=K$），
$$
\sum_{N\in\mathbb{Z}}S_a(N)^2
\le K^2\sum_m|a_m|^2,
$$
其中 $S_a(N)=\sum_{k=1}^K a_{N-2^k}$（约定 $a_m=0$ 于支撑外）。

**证明.** 对固定 $N$，Cauchy–Schwarz 得
$$
\Bigl|\sum_k a_{N-2^k}c_k\Bigr|^2
\le\|c\|_2^2\sum_{k=1}^K|a_{N-2^k}|^2.
$$
对 $N$ 求和：每个固定 $k$ 有 $\sum_N|a_{N-2^k}|^2=\sum_m|a_m|^2$，共 $K$ 个 $k$，故得界。证毕。

**注.** 由 L-LSW-1(B)(C) 亦得更粗的 $\|c\|_1^2\sum|a|^2$；当 $c_k\equiv 1$ 时 $\|c\|_1^2=K^2$，与本引理同阶。真正的「大筛增益」需对 $|g_c|$ 的 Peak 质量或 $r_a$ 的二进差亏缺（L-LSW-6/7）。

---

## L-LSW-3（已证）— 稀疏点集形式（算子范数）

把二进采样写成关联：对支撑在 $[1,Y]$ 的 $a$，以及求和范围 $N\in I_K$（取 $Y=2^{K+1}$），定义线性映射
$$
(Tc)_N=\sum_{k=1}^{K}a_{N-2^k}c_k,\qquad N\in I_K.
$$
则
$$
\|T\|_{\ell^2(c)\to\ell^2(N)}^2
\le K\sum_{m\le Y}|a_m|^2.
$$
等价地：对一切 $c$，
$$
\sum_{N\in I_K}\Bigl|\sum_{k=1}^{K}a_{N-2^k}c_k\Bigr|^2
\le K\|c\|_2^2\sum_{m\le Y}|a_m|^2.
$$

**证明.** 与 L-LSW-2 相同，仅把 $N$-求和限制在 $I_K$；因 $N\in I_K$、$k\le K$ 时 $1\le N-2^k\le 2^{K+1}=Y$（$N>2^K\Rightarrow N-2^K\ge 1$），支撑不越界。证毕。

**解读.** $\{N-2^k\}_{k\le K}$ 作为稀疏点集，其采样算子的 Hilbert–Schmidt / 算子范数由「每点至多落入 $K$ 个窗槽」控制——这是大筛「间距 / 重数」侧的初等版本。

---

## L-LSW-4（已证）— 整窗二次型下界 $\Rightarrow$ 二进段计数

设 $K\ge 2$。则
$$
\sum_{N\in I_K}S_E(N)^2
\ge K^2\bigl|\mathcal{F}_0\cap I_K\bigr|.
$$
因而由 L-LSW-2（$a=1_E$、$c\equiv 1$、$Y=2^{K+1}$），
$$
\bigl|\mathcal{F}_0\cap I_K\bigr|
\le M(2^{K+1}).
$$
同理由一阶双计数（每个 $m\in E_{\le 2^{K+1}}$ 至多属于 $K$ 个形如 $W(N)$、$N\in I_K$ 的窗）：
$$
K\bigl|\mathcal{F}_0\cap I_K\bigr|
=\sum_{\substack{N\in\mathcal{F}_0\cap I_K}}\lvert W(N)\rvert
\le\sum_{m\in E_{\le 2^{K+1}}}\#\{k\le K:m+2^k\in I_K\}
\le K\,M(2^{K+1}),
$$
再得同一界 $|\mathcal{F}_0\cap I_K|\le M(2^{K+1})$。

**证明.** 整窗项 $S_E(N)=K$；非整窗项非负，故二次和下界成立。L-LSW-2 给出
$$
\sum_{N\in I_K}S_E(N)^2\le K^2 M(2^{K+1}).
$$
两式比较即得。一阶双计数：对固定 $m$，使 $m+2^k\in I_K$ 的 $k$ 至多 $K$ 个。证毕。

**定位.** 大筛二次型与平凡双计数在**无相关假设**时给出同阶整窗计数上界；增益必须来自非对角 $r_E(2^k-2^\ell)$ 或 Peak 质量（下文条件式）。

---

## L-LSW-5（已证）— Roth 密度下 $|\mathcal{F}_0\cap[1,X]|$ 的定量上界

对一切 $X\ge 4$，
$$
\bigl|\mathcal{F}_0\cap[1,X]\bigr|
\ll\frac{X}{(\log X)^{1/20}}.
$$
更精细地，对每个 $K\ge 2$，
$$
\bigl|\mathcal{F}_0\cap I_K\bigr|
\ll\frac{2^K}{K^{1/20}},
$$
且
$$
\bigl|\mathcal{F}_0\cap[1,X]\bigr|
\le\sum_{2\le K\le\lfloor\log_2 X\rfloor}\bigl|\mathcal{F}_0\cap I_K\bigr|
+O(1).
$$

**证明.** L-LSW-4 + 定理 B：$M(2^{K+1})\ll 2^K/K^{1/20}$。对 $K\le\log_2 X$ 求和，主项由最大二进段贡献，得 $X/(\log X)^{1/20}$。证毕。

**判决.** 本界与 $|E\cap[1,X]|$ **同阶**；由 L08，抽象密度零集可使 $\mathcal{F}_0$ 无限，故 L-LSW-5 **不**蕴含 $\mathcal{F}_0$ 有限。它给出的是：在真实 Roth 密度下，整窗 $N$ 的计数**不能厚于例外集本身**——「许多 $N$ 同时整窗」已被大筛/双计数限制到 $O\big(X/(\log X)^{1/20}\big)$。

**与 L-Rand 对照.** 独立 Bernoulli 模型下期望 $|\widetilde{\mathcal{F}}_0\cap I_K|\ll 2^K\exp(-cK\log K)$（L-Rand-2/3），远小于 L-LSW-5；本引理是最坏情形（允许窗完全耦合）的确定性上界，对应 L-Rand-4/5 的 Fréchet / 种植侧。

---

## L-LSW-6（条件式）— 二进差相关亏缺 $\Rightarrow$ 整窗计数增益

假设 LSW-Corr$_\eta$（$\eta>0$）成立。则对充分大 $K$，
$$
\sum_{N\in I_K}S_E(N)^2
\le K\,M(2^{K+1})+K^{2-\eta}\,M(2^{K+1}),
$$
从而
$$
\bigl|\mathcal{F}_0\cap I_K\bigr|
\ll_\eta\frac{M(2^{K+1})}{K}+\frac{M(2^{K+1})}{K^\eta}.
$$
在 Roth 下
$$
\bigl|\mathcal{F}_0\cap I_K\bigr|
\ll_\eta\frac{2^K}{K^{1+\min(1,\eta)-1/20+\varepsilon}}\qquad(\varepsilon=0\text{ 若记隐常数依赖 }\eta),
$$
更干净地写
$$
\bigl|\mathcal{F}_0\cap I_K\bigr|
\ll\frac{2^K}{K^{1/20}\cdot K^{\min(1,\eta)}}.
$$
累加后仍有
$$
\bigl|\mathcal{F}_0\cap[1,X]\bigr|
\ll\frac{X}{(\log X)^{1/20+\min(1,\eta)}},
$$
**可仍发散**（级数 $\sum_K 2^K/K^{c}$ 的部分和 $\asymp X/(\log)^c$）。

**证明.** 由 L-LSW-1(A)，$c\equiv 1$，
$$
\sum_{N}S_E(N)^2
=K\,M+\sum_{k\neq\ell}r_E(2^k-2^\ell).
$$
限制 $N\in I_K$ 时，对角贡献 $\le K M(2^{K+1})$（因每点至多 $K$ 个槽，或直接用 $\sum_{N\in I_K}\sum_k 1_E(N-2^k)\le K M$）。非对角：对每对 $k\neq\ell$，差 $d=2^k-2^\ell\in\Delta_K^{\mathrm{full}}\cup(-\Delta_K^{\mathrm{full}})$，且
$$
\sum_{N\in I_K}1_E(N-2^k)1_E(N-2^\ell)
\le r_E(2^k-2^\ell)
\le\frac{M(2^{K+1})}{K^\eta}
$$
（LSW-Corr$_\eta$；符号差同阶）。对数 $\le K^2$，故非对角 $\le K^{2-\eta}M$。与整窗下界 $K^2|\mathcal{F}_0\cap I_K|$ 比较即得。Roth 代入同 L-LSW-5。证毕。

**注.** 若 $\eta>1$ 且希望 $\sum_K|\mathcal{F}_0\cap I_K|<\infty$，本界仍不足：需要指数型小或 $M(2^K)\ll 2^K/K^{1+\delta}$ 且 $\delta+\min(1,\eta)>1$ 并对**每个** $K$ 有 $|\mathcal{F}_0\cap I_K|\ll K^{-1-\varepsilon}$。在仅有多项式相关亏缺时，L-LSW-6 只改善对数幂次。

---

## L-LSW-7（条件式）— Peak/Flat 大筛 $\Rightarrow$ 二次型增益

假设 LSW-Flat$_\theta$（$\theta\in(0,1/2]$）成立。取 $a=1_E$、$Y=2^{K+1}$、$c\equiv 1$。则
$$
\sum_{N\in I_K}S_E(N)^2
\le\int_0^1\bigl|\widehat{1_E}(\alpha;Y)\bigr|^2|g(\alpha)|^2\,\mathrm{d}\alpha
\le K^{2-2\theta}\,M(Y)+K^2\cdot K^{-2\theta}\,M(Y)
\ll K^{2-2\theta}\,M(Y),
$$
其中 $g=g_{(1,\ldots,1)}$。因而
$$
\bigl|\mathcal{F}_0\cap I_K\bigr|
\ll K^{-2\theta}\,M(2^{K+1}).
$$
在 Roth 下
$$
\bigl|\mathcal{F}_0\cap I_K\bigr|
\ll\frac{2^K}{K^{1/20+2\theta}},
\qquad
\bigl|\mathcal{F}_0\cap[1,X]\bigr|
\ll\frac{X}{(\log X)^{1/20+2\theta}}.
$$

**证明.** Parseval（L-LSW-1(B)）+ 拆 Peak/Flat：Flat 上 $|g|\le K^{1-\theta}$，Peak 上 $|g|\le K$ 且由假设 Peak 的 $|\hat{1_E}|^2$ 质量 $\le K^{-2\theta}M$。证毕。

**与 L-EFD / L-Lac 接口.** L-Lac-1 给出 $\mathrm{meas}(\mathrm{Peak})\ll K^{-2\delta}$（Chebyshev），**不**自动给出 $\int_{\mathrm{Peak}}|\hat{1_E}|^2\ll K^{-2\theta}M$——后者是对 $\widehat{1_E}$ 的额外无集中假设（接近 EFD-Hyb 的 $L^2$ 加权取消，但本处直接喂二次型）。若仅有测度小而无质量小，平凡界仍回到 L-LSW-5。

---

## L-LSW-8（条件式）— 强增益 $\Rightarrow\mathcal{F}_0$ 有限的阈值表

下列任一充分条件蕴含 $\mathcal{F}_0$ 有限（故经 L07 得 $x=0$ 型充分大可表）：

1. **LSW-Sum$_\varepsilon$：** 存在 $\varepsilon>0$ 使对充分大 $K$，
   $$
   \bigl|\mathcal{F}_0\cap I_K\bigr|\ll K^{-1-\varepsilon}.
   $$
2. **LSW-Exp$_c$：** 存在 $c>0$ 使 $|\mathcal{F}_0\cap I_K|\ll 2^{-cK}$。  
3. **LSW-Corr$_\eta$ + Roth$_\kappa$：** 若例外集满足更强密度 $M(Y)\ll Y/(\log Y)^\kappa$ 且 $\kappa+\min(1,\eta)>1$，则由 L-LSW-6，
   $$
   \sum_K\bigl|\mathcal{F}_0\cap I_K\bigr|<\infty.
   $$
   （骨架仅有 $\kappa=1/20$；即使 $\eta$ 任意大，$1/20+\eta$ 对累加 $\sum 2^K/K^{c}$ **仍发散**——此处「有限」需把 L-LSW-6 的结论加强为对 $|\mathcal{F}_0\cap I_K|$ 的**亚指数或 $K^{-1-\varepsilon}$ 型**界，例如再设窗近不交装填。详见下方注。）

**注（装填加强）.** 若另设：存在绝对常数 $C$ 使每个二进段 $I_K$ 内可取出 $|\mathcal{F}_0\cap I_K|/C$ 个两两窗不交的整窗中心（对照 L-Rand 模型 S 的种植间距；真实 $E$ 上未证），则一阶双计数升为
$$
\bigl|\mathcal{F}_0\cap I_K\bigr|\ll_C\frac{M(2^{K+1})}{K},
$$
在 Roth 下 $\ll 2^K/(K^{1+1/20})$，累加仍 $\asymp X/(\log)^{1+1/20}$，**仍不有限**。要有限必须回到 LSW-Sum / LSW-Exp，或 L-Rand-3 型的近独立乘积衰减。

**证明.** (1)(2) 级数收敛。(3) 在「$|\mathcal{F}_0\cap I_K|\ll M(2^K)/K^{\min(1,\eta)}$」且 $M(Y)\ll Y/(\log Y)^\kappa$ 时，若进一步有上界 $\ll K^{-1-\varepsilon}$（例如 $M(2^K)\ll 2^K\cdot\mathrm{poly}(K)$ **不再**使用，而改用随机型上界），则收敛；骨架 Roth 单独 + Corr **不能**把 $2^K/K^{C}$ 压到可和——故将「Roth$_\kappa$+Corr$\Rightarrow$有限」标为**需额外 Sum/Exp 或近独立**的条件式接口，而非已证蕴含。严格已证蕴含仅为：LSW-Sum$_\varepsilon$ 或 LSW-Exp$_c$ $\Rightarrow\mathcal{F}_0$ 有限。证毕。

---

## L-LSW-9（已证对照）— 与 FW / EFD / AE / Pack / Rand / L08 的正交性

| 路线 | 主对象 | 与 L-LSW 关系 |
|------|--------|----------------|
| L-FW | $\Phi_N(\alpha)=\sum_k 1_E(N-2^k)e(\alpha k)$（$k$-频率） | 单窗谱；LSW 是 $N$-平均 $\|S_E\|_{\ell^2}^2$ |
| L-EFD | $\widehat{1_E}(\alpha;X)$ 点态/加权次弧 | Parseval 共享 $|g|^2$；EFD 要杀单点 Dev，LSW 要压整窗计数 |
| L-AE / L-Inc | $\mathcal{E}_2(E_N)$、$\Delta_K$-团 | 非对角 $r_E(d)$ 同族；AE 局部团，LSW 全局二次型 |
| L-Pack | 邻/倍窗装填 | Pack 抬升局部 $|E|$；LSW 直接上界 $|\mathcal{F}_0|$ |
| L-Rand | Bernoulli / 种植 | L-LSW-5＝确定性 Fréchet 侧；独立模型远强 |
| L08 | 抽象薄 $E$ 使 $\mathcal{F}_0$ 无限 | 与 L-LSW-5 兼容（上界可无限） |

**明确非声称.** 本文件不证明 LSW-Corr / LSW-Flat，不证明 $\mathcal{F}_0$ 有限，不证明原猜想。

---

## L-LSW-10（缺口）— LSW-G1–G4

| 编号 | 缺口 | 若解决则 |
|------|------|----------|
| LSW-G1 | 真实 $E$ 上 LSW-Corr$_\eta$（$\eta>0$） | L-LSW-6：对数幂增益 |
| LSW-G2 | LSW-Flat$_\theta$（Peak 上 $|\hat{1_E}|^2$ 质量） | L-LSW-7：幂 $K^{-2\theta}$ 增益；近 EFD |
| LSW-G3 | 二进段内整窗中心的近不交选代表 | 双计数 $\to|\mathcal{F}_0|\ll M/K$；仍未必有限 |
| LSW-G4 | LSW-Sum$_\varepsilon$ 或近独立窗（Rand-G1） | $\mathcal{F}_0$ 有限 $\stackrel{\mathrm{L07}}{\Rightarrow}x=0$ 充分大 |

**主缺口.** G4（有限性）；G1/G2 仅改善 L-LSW-5 的对数指数，在 Roth $1/20$ 下**不**单独关闭 E-kill。

---

## 小结

| 编号 | 摘要 | 状态 |
|------|------|------|
| L-LSW-1 | 二次型差展开 + Parseval；$g_c$ 矩 | 已证 |
| L-LSW-2 | $Q_K(a;c)\le K\|c\|_2^2\sum\|a\|^2$ | 已证 |
| L-LSW-3 | 稀疏采样算子范数 $\le K\sum\|a\|^2$ | 已证 |
| L-LSW-4 | $|\mathcal{F}_0\cap I_K|\le M(2^{K+1})$ | 已证 |
| L-LSW-5 | Roth $\Rightarrow|\mathcal{F}_0\cap[1,X]|\ll X/(\log X)^{1/20}$ | 已证（可无限） |
| L-LSW-6 | LSW-Corr$_\eta$$\Rightarrow|\mathcal{F}_0\cap I_K|\ll M/K^{\min(1,\eta)}$ | 条件式 |
| L-LSW-7 | LSW-Flat$_\theta$$\Rightarrow|\mathcal{F}_0\cap I_K|\ll K^{-2\theta}M$ | 条件式 |
| L-LSW-8 | Sum$_\varepsilon$ / Exp$_c$$\Rightarrow\mathcal{F}_0$ 有限 | 条件式 |
| L-LSW-9 | 与 FW/EFD/AE/Pack/Rand/L08 对照 | 已证（对照） |
| L-LSW-10 | 缺口 LSW-G1–G4 | 缺口 |

**链条（已证定量）.**
$$
\text{大筛/CS（L-LSW-2）}+\text{整窗下界（L-LSW-4）}+\text{Roth}
\stackrel{\mathrm{L\text{-}LSW\text{-}5}}{\Longrightarrow}
|\mathcal{F}_0\cap[1,X]|\ll\frac{X}{(\log X)^{1/20}}.
$$

**链条（条件式有限）.**
$$
\mathrm{LSW\text{-}Sum}_\varepsilon\text{ 或 }\mathrm{LSW\text{-}Exp}_c
\stackrel{\mathrm{L\text{-}LSW\text{-}8}}{\Longrightarrow}
\mathcal{F}_0\text{ 有限}
\stackrel{\mathrm{L07}}{\Longrightarrow}
x=0\text{ 型充分大可表}.
$$
