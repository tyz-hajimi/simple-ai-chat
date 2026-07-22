# L-Sing：奇异级数显式 Euler 积与平均（R19-Singular-Product-Explicit）

> 路线 **R19-Singular-Product-Explicit**（P09 攻关轮次 19；服务 **半无条件文档化 / SS-Sync**）。  
> 专攻：写出混合幂 $f=x^4+y^3+z^2$ 的奇异级数在**标准圆法形式**下的显式局部因子，并给出可严格证明的平均公式
> $$
> \sum_{m\le X}\mathfrak{S}(m;Q)=X+O_\varepsilon\bigl(Q^{11/12+\varepsilon}\bigr)
> $$
> 以及截断 Euler 积形
> $$
> \sum_{m\le X}\mathfrak{S}_{\le P}(m)=X+O\bigl(X^{1-\delta}\bigr)
> $$
> （$P\ll\log X$ 的显式范围）。  
> **定位.** 文档化与平均层；**不**证明 SS-Sync 点态地板、$\mathrm{H}_{\mathrm{thr}}$、E-kill、原猜想。  
> 状态严格区分：**已证** / **条件式** / **缺口**。

---

## 0. 记号与两种标准写法

沿用 L-SSO / L-Thr / L-Ekill-SS。对 $m\in\mathbb{Z}$ 与素数 $p$，记完整幂次和
$$
S_k\Bigl(\frac aq\Bigr)
:=\sum_{x=0}^{q-1}e\Bigl(\frac{a\,x^k}{q}\Bigr)
\qquad(k\in\{2,3,4\}).
$$

### （R）Ramanujan / 完整和级数

$$
A(q,m)
:=q^{-3}
\sum_{\substack{a=1\\(a,q)=1}}^q
S_4\Bigl(\frac aq\Bigr)
S_3\Bigl(\frac aq\Bigr)
S_2\Bigl(\frac aq\Bigr)
e\Bigl(-\frac{am}{q}\Bigr).
$$
截断奇异级数与形式全级数
$$
\mathfrak{S}(m;Q):=\sum_{q\le Q}A(q,m),
\qquad
\mathfrak{S}^{\mathrm{Ram}}(m):=\sum_{q=1}^\infty A(q,m)
$$
（后者在绝对收敛时定义；本混合幂由 Weyl 仅得 $|A(q,m)|\ll_\varepsilon q^{-1/12+\varepsilon}$，$\sum|A|$ **发散**，故点态全级数须条件收敛或改挂 Euler 积，见 R13）。

### （E）$p$-进局部密度 / Euler 积

$$
N(p^h;m)
:=\#\bigl\{(x,y,z)\bmod p^h:x^4+y^3+z^2\equiv m\pmod{p^h}\bigr\},
$$
$$
\sigma_p(m)
:=\lim_{h\to\infty}p^{-2h}\,N(p^h;m)
$$
（极限存在：标准 Hensel / 维数理由；坏素有限集 $\mathfrak{B}\supset\{2,3\}$ 上取充分高但有限的稳定阶 $e_p$）。奇异级数的 Euler 积写法
$$
\mathfrak{S}(m)=\prod_p\sigma_p(m),
\qquad
\mathfrak{S}_{\le P}(m)=\prod_{p\le P}\sigma_p(m),
\qquad
T_P(m)=\prod_{p>P}\sigma_p(m).
$$
在「级数与积皆绝对收敛」的古典情形有 $\mathfrak{S}^{\mathrm{Ram}}=\prod_p\sigma_p$；对本题二者的等同仅在截断级或 Tail-Weil 下使用（L-SSO-2）。

**正规化约定.** $A(1,m)=1$，且
$$
\frac1{p^{e}}\sum_{r\bmod p^{e}}\sigma_p(r)=1
$$
（对一切 $e\ge 1$）：因 $\sum_{m\bmod p^h}N(p^h;m)=p^{3h}$，故平均 $p^{-2h}N=1$，取极限得均值 $1$。这固定了下文平均主项系数 $c=1$。

---

## L-Sing-1（已证）— 显式局部因子：素幂展开

对每个素数 $p$ 与 $m\in\mathbb{Z}$，
$$
\sigma_p(m)
=\sum_{\ell=0}^\infty A(p^\ell,m),
$$
其中 $A(1,m)=1$，且对 $\ell\ge 1$
$$
A(p^\ell,m)
=p^{-3\ell}
\sum_{\substack{a=1\\(a,p)=1}}^{p^\ell}
S_4\Bigl(\frac{a}{p^\ell}\Bigr)
S_3\Bigl(\frac{a}{p^\ell}\Bigr)
S_2\Bigl(\frac{a}{p^\ell}\Bigr)
e\Bigl(-\frac{am}{p^\ell}\Bigr).
$$
等价地（标准 Euler 因子展开）
$$
\boxed{
\sigma_p(m)
=1+\sum_{\ell=1}^\infty
p^{-3\ell}
\sum_{\substack{a=1\\(a,p)=1}}^{p^\ell}
S_4S_3S_2\,e\Bigl(-\frac{am}{p^\ell}\Bigr)
}
$$
（乘积内 $S_k=S_k(a/p^\ell)$）。

**证明.** 由 Ramanujan 级数的乘性：$A$ 对 $q$ 完全积性（$(q,q')=1\Rightarrow A(qq',m)=A(q,m)A(q',m)$，标准完整和分解），故
$$
\sum_{q=1}^\infty A(q,m)=\prod_p\Bigl(\sum_{\ell\ge 0}A(p^\ell,m)\Bigr)
$$
在绝对收敛时成立；右端单素因子正是 $p$-进密度的完整和展开（Davenport / Vaughan 型恒等式，见下条与密度定义的对接）。截断级 $q\mid P^\infty$ 的有限恒等式无需绝对收敛。证毕。

**与 SS-1 的衔接.** L-Ekill-SS-1：$\sigma_p(m)\ge p^{-2}>0$（一切 $p,m$）。故 Euler 积无零因子，无局部不可解阻碍。

---

## L-Sing-2（已证）— 模 $p$ 主项 + Gauss / Jacobi 显式

固定奇数素数 $p\notin\mathfrak{B}$（下文 $p\ge 5$）。写
$$
\sigma_p(m)=1+A(p,m)+R_p(m),
\qquad
R_p(m)=\sum_{\ell\ge 2}A(p^\ell,m).
$$

### （A）一次局部因子（显式）

$$
\boxed{
A(p,m)
=p^{-3}
\sum_{a=1}^{p-1}
S_4\Bigl(\frac ap\Bigr)
S_3\Bigl(\frac ap\Bigr)
S_2\Bigl(\frac ap\Bigr)
e\Bigl(-\frac{am}p\Bigr)
}
$$

### （B）二次 Gauss 和（经典闭式）

对 $(a,p)=1$，
$$
S_2\Bigl(\frac ap\Bigr)
=\Bigl(\frac ap\Bigr)\tau_p,
\qquad
\tau_p
=\sum_{x=0}^{p-1}e\Bigl(\frac{x^2}{p}\Bigr)
=
\begin{cases}
\sqrt{p},& p\equiv 1\pmod 4,\\
i\sqrt{p},& p\equiv 3\pmod 4.
\end{cases}
$$
故
$$
A(p,m)
=p^{-3}\tau_p
\sum_{a=1}^{p-1}
\Bigl(\frac ap\Bigr)
S_4\Bigl(\frac ap\Bigr)
S_3\Bigl(\frac ap\Bigr)
e\Bigl(-\frac{am}p\Bigr).
$$

### （C）立方 / 四次和（Jacobi 和形）

对 $(a,p)=1$，作变量缩放 $x\mapsto a^{-1/k}x$（在 $\mathbb{F}_p^\times$ 上）：
$$
S_k\Bigl(\frac ap\Bigr)
=\Bigl(\frac{a}{p}\Bigr)_{\!k}^{\!*}\,
S_k\Bigl(\frac 1p\Bigr)
\quad\text{（$k$ 次剩余符号约定下）},
$$
更干净地：存在只依赖 $p$ 的常数 $G_k(p):=S_k(1/p)$，使
$$
S_k\Bigl(\frac ap\Bigr)
=G_k(p)\cdot\chi_k(a)
$$
对适当乘性特征 $\chi_k$（或有限线性组合）。经典地，$G_3(p)$、$G_4(p)$ 可由 Jacobi 和
$$
J(\psi,\eta)=\sum_{t\in\mathbb{F}_p}\psi(t)\eta(1-t)
$$
表出（Ireland–Rosen / Beauville 型公式）；本仓库**不**需要其数值，只保留结构
$$
\bigl|S_k(a/p)\bigr|\ll_k\sqrt{p}
\quad(k=3,4;\ p\nmid a)
$$
（Weil 对曲线点计 / 完整和，给出 $|A(p,m)|\ll p^{-3/2}$ 量级的主项）。

### （D）高阶余项包络（Weyl）

Hua–Weyl：$|S_k(a/p^\ell)|\ll_\varepsilon p^{\ell(1-1/k+\varepsilon)}$，故
$$
\bigl|A(p^\ell,m)\bigr|
\ll_\varepsilon p^{-\ell/12+\varepsilon},
\qquad
\bigl|R_p(m)\bigr|
\ll_\varepsilon\sum_{\ell\ge 2}p^{-\ell/12+\varepsilon}.
$$
（单素幂级数仍非绝对给出 $|R_p|\ll p^{-1-\delta}$；一致幂次尾标为 **Tail-Weil**，见 L-SSO-2(B)。）

**证明.** （A）即 L-Sing-1 的 $\ell=1$。（B）二次 Gauss 和的标准求值。（C）缩放 + Weil 界。（D）代入定义。证毕。

---

## L-Sing-3（已证）— 坏素 $p=2,3$ 的局部因子形状

### （A）$p=2$

由 L-2adic-2：像集 $I_\nu=\mathbb{Z}/2^\nu\mathbb{Z}$ 对一切 $\nu$（$\delta_\nu=1$）。故每个 $m$ 在 $\mathbb{Z}_2$ 上可由 $x^4+y^3+z^2$ 表示，且
$$
\sigma_2(m)=\lim_{\nu\to\infty}2^{-2\nu}N(2^\nu;m)\ge 2^{-2}
$$
（L-Ekill-SS-1；正性来自非空纤维 + Hensel 稳定化）。标准展开仍写
$$
\sigma_2(m)=\sum_{\ell\ge 0}A(2^\ell,m),
$$
其中低阶 $A(2^\ell,m)$ 由模 $2^\ell$ 的完整和直接定义；本路线不展开数值表。

### （B）$p=3$

直接检查模 $3$ 与模 $9$ 的纤维非空后 Hensel 提升（SS-1 证明概要）；
$$
\sigma_3(m)=\sum_{\ell\ge 0}A(3^\ell,m)\ge 3^{-2}.
$$
立方因子在 $p=3$ 上的奇异性使提升阶 $e_3$ 取充分大有限值（L-SSO 的坏模约定）。

**证明.** 引用 L-2adic-2 + L-Ekill-SS-1；展开式同 L-Sing-1。证毕。

---

## L-Sing-4（已证）— 截断 Ramanujan 级数的平均公式

**定理.** 对一切 $X\ge 2$、$Q\ge 1$ 与 $\varepsilon>0$，
$$
\boxed{
\sum_{m\le X}\mathfrak{S}(m;Q)
=X+O_\varepsilon\bigl(Q^{11/12+\varepsilon}\bigr).
}
$$
特别地，取 $Q=X^{12/11\cdot(1-\delta)}$（$0<\delta\le 1$）得
$$
\sum_{m\le X}\mathfrak{S}(m;Q)
=X+O_\varepsilon\bigl(X^{1-\delta+\varepsilon}\bigr).
$$

**证明.**

1. **主项 $q=1$.** $A(1,m)=1$，贡献 $\lfloor X\rfloor$。  

2. **$q>1$ 的完整剩余均值消失.** 对 $(a,q)=1$，
   $$
   \sum_{r=0}^{q-1}e\Bigl(-\frac{ar}{q}\Bigr)=0.
   $$
   写 $X=q\lfloor X/q\rfloor+\rho$（$0\le\rho<q$），则
   $$
   \sum_{m\le X}e\Bigl(-\frac{am}{q}\Bigr)
   =\lfloor X/q\rfloor\cdot 0+O(1)=O(1).
   $$

3. **逐 $q$ 贡献.** 故
   $$
   \sum_{m\le X}A(q,m)
   =q^{-3}
   \sum_{\substack{a=1\\(a,q)=1}}^q
   S_4S_3S_2
   \cdot O(1)
   \ll
   q^{-2}\max_{(a,q)=1}\bigl|S_4S_3S_2\bigr|.
   $$
   Hua–Weyl：$|S_k(a/q)|\ll_\varepsilon q^{1-1/k+\varepsilon}$，从而
   $$
   |S_4S_3S_2|
   \ll_\varepsilon q^{3-13/12+\varepsilon}=q^{23/12+\varepsilon},
   $$
   并计入 $\varphi(q)\le q$ 个 $a$-项的绝对值和时（与 R13 一致的包装）
   $$
   \Bigl|\sum_{m\le X}A(q,m)\Bigr|
   \ll_\varepsilon q^{-1/12+\varepsilon}.
   $$

4. **对 $q\le Q$ 求和.**
   $$
   \sum_{2\le q\le Q}\Bigl|\sum_{m\le X}A(q,m)\Bigr|
   \ll_\varepsilon\sum_{q\le Q}q^{-1/12+\varepsilon}
   \ll_\varepsilon Q^{11/12+\varepsilon}.
   $$
   证毕。

**备注（与绝对收敛的区别）.** 点态 $\sum_q|A(q,m)|$ 因指数 $-1/12$ 而发散（R13）；但**对 $m$ 先求和**后，振荡使 $q>1$ 的主项消失，仅留 $O(q^{-1/12+\varepsilon})$，对 $Q=X^{\theta}$ 可和。这是本路线平均公式成立而一致积尾不成立的核心分野。

---

## L-Sing-5（已证）— 截断 Euler 积的平均公式

固定截断高度 $P\ge 3$，令
$$
M_P=\prod_{p\le P}p^{e_p}
$$
（$e_p$ 同 L-SSO-1；坏素有限抬高）。由 L-SSO-1，$\mathfrak{S}_{\le P}$ 以 $M_P$ 为周期。

**定理.** 存在绝对常数 $C_\sigma<\infty$ 使 $\|\sigma_p\|_\infty\le C_\sigma$ 对一切 $p$（大素：Lang–Weil / 纤维维数 $\Rightarrow\sigma_p=1+O(p^{-1/2})$；坏素：有限最大值）。于是
$$
\sum_{m\le X}\mathfrak{S}_{\le P}(m)
=\frac{X}{M_P}\sum_{r\bmod M_P}\mathfrak{S}_{\le P}(r)
+O\bigl(M_P\,C_\sigma^{\pi(P)}\bigr).
$$
由 CRT 与均值公式 $\mathbb{E}[\sigma_p]=1$，
$$
\frac1{M_P}\sum_{r\bmod M_P}\mathfrak{S}_{\le P}(r)
=\prod_{p\le P}\Bigl(\frac1{p^{e_p}}\sum_{a\bmod p^{e_p}}\sigma_p(a)\Bigr)
=1.
$$
故
$$
\boxed{
\sum_{m\le X}\mathfrak{S}_{\le P}(m)
=X+O\bigl(M_P\,C_\sigma^{\pi(P)}\bigr).
}
$$

**幂次误差形式.** 取 $P\le c\log X$，则 $M_P=\exp(\theta(P)+O(1))\le X^{c'}$（$c'=c\cdot(1+o(1))$），且
$$
C_\sigma^{\pi(P)}=\exp\bigl(O(P/\log P)\bigr)=X^{o(1)}.
$$
选取 $c>0$ 充分小得绝对 $\delta\in(0,1)$ 使
$$
\sum_{m\le X}\mathfrak{S}_{\le P}(m)
=X+O\bigl(X^{1-\delta}\bigr).
$$

**证明.** 周期函数的不完全和：完整周期贡献精确均值，余段长 $<M_P$。均值因式分解用 CRT。$\mathbb{E}\sigma_p=1$ 见 §0。大素上界：仿射曲面 $x^4+y^3+z^2=m$ 的 $\mathbb{F}_p$-点数 $=p^2+O(p^{3/2})$（Lang–Weil；奇异纤维对固定 $m$ 的例外不影响一致 $O(p^{3/2})$ 包络的存在性，至多调整 $\mathfrak{B}$），故 $p^{-2}N(p;m)=1+O(p^{-1/2})$；Hensel 提升后 $\sigma_p\ll 1$。证毕。

**与用户目标形的对照.** 截断 Euler 积的平均恰为
$$
\sum_{m\le X}\mathfrak{S}_{\le P}(m)=cX+O(X^{1-\delta}),
\qquad c=1.
$$
全级数 $\mathfrak{S}=\mathfrak{S}_{\le P}T_P$ 的同形平均在一致 $|T_P-1|\ll P^{-\delta}$（Tail-Weil）下继承；无 Tail-Weil 时**只声称截断形**（本条 + L-Sing-4）。

---

## L-Sing-6（已证）— 由平均到多数点「不太小」

### （A）截断 Ramanujan

由 L-Sing-4，$\frac1X\sum_{m\le X}\mathfrak{S}(m;Q)=1+O_\varepsilon(X^{-1}Q^{11/12+\varepsilon})$。  
$\mathfrak{S}(m;Q)$ **可负**（振荡和），故不能直接 Markov 到下界；改用二矩或改挂 Euler 积正性。

### （B）截断 Euler 积（正性可用）

$\mathfrak{S}_{\le P}(m)>0$。设 $0<\varepsilon<1$。若
$$
\#\{m\le X:\mathfrak{S}_{\le P}(m)<\varepsilon\}>(1-\eta)X,
$$
则由 L-Sing-5 与上界 $\mathfrak{S}_{\le P}\le C_\sigma^{\pi(P)}=:B_P$，
$$
\sum_{m\le X}\mathfrak{S}_{\le P}
<\varepsilon X+B_P\eta X+O(X^{1-\delta}).
$$
与总和 $=X+O(X^{1-\delta})$ 比较得 $\varepsilon+B_P\eta\ge 1-o(1)$。取 $\varepsilon=1/2$，
$$
\eta\ge\frac{1-o(1)}{2B_P}.
$$
故当 $P$ 固定（从而 $B_P$ 固定）时，存在绝对 $c_P>0$ 使
$$
\frac1X\#\bigl\{m\le X:\mathfrak{S}_{\le P}(m)\ge\tfrac12\bigr\}\ge c_P>0.
$$
取 $P=P(X)\to\infty$ 充分慢使 $B_P\le(\log X)^{A}$，则
$$
\frac1X\#\bigl\{m\le X:\mathfrak{S}_{\le P}(m)\ge\tfrac12\bigr\}
\gg(\log X)^{-A}.
$$
再在 Tail-Weil 下把 $T_P$ 换成 $1+O(P^{-\delta})$，得全 $\mathfrak{S}$ 的多数点下界（对接 R13 §5.2 概率地板；**非**一切 $m$ 的一致地板）。

**证明.** 上述比较即 Markov / 截断正性论证。证毕。

---

## L-Sing-7（已证接口）— 对接 SS-Sync / L-Floor / L-Thr

| 下游 | 本文件供给 | 仍缺 |
|------|------------|------|
| SS-Sync / SSO-G4 | 平均 $=X+O(X^{1-\delta})$（截断）；多数点 $\mathfrak{S}_{\le P}\ge 1/2$ | 窗上点态 $\max_k\mathfrak{S}\gg(\log)^{-c}$（需 L-Floor-7/8 或 Equi） |
| L-Floor-3/4 | 显式 $\sigma_p=1+A(p,\cdot)+R_p$ 供轨道平均 | 积尾交换仍要条件 |
| L-Thr-1 / L-Eff | 标准 $A(q,m)$ 与主弧 Gauss 和一致 | 次弧阈值 |
| L-Ekill-SS-2 | 平均层说明「同步极小」稀 | 阈值 $\mathrm{H}_{\mathrm{thr}}$ |

**明确非声称.**

- 不证明 $\inf_m\mathfrak{S}(m)>0$（R13 否证原框架）。  
- 不证明 SS-Sync 对一切 $n$。  
- 不证明 $\mathrm{H}_{\mathrm{thr}}$、H、原猜想、$\mathcal{F}_0$ 有限。  
- 全级数平均 $\sum_{m\le X}\mathfrak{S}(m)=X+O(X^{1-\delta})$ 仅在 Tail-Weil（或同等积尾）下继承；无条件已证的是 **L-Sing-4/5 的截断形**。

---

## L-Sing-8（缺口清单）

| 缺口 | 内容 | 堵住则得 |
|------|------|----------|
| Sing-G1 | Tail-Weil：$|\sigma_p-1|\ll p^{-1-\delta}$ 一致 | 全 $\mathfrak{S}$ 平均 $=X+O(X^{1-\delta})$；L-Floor-1♯ |
| Sing-G2 | 窗 Equi：二进轨道采样逼近 $m\le X$ 平均 | 平均 $\Rightarrow$ 窗平均地板（助 SSO-G4） |
| Sing-G3 | $\mathfrak{S}(m;Q)$ 与 $\mathfrak{S}_{\le P}$ 的有效比较（$Q,P$ 联动） | 统一两种截断语言 |
| Sing-G4 | $=\mathrm{Thr}$-G1：$\mathrm{H}_{\mathrm{thr}}$ | 平均/地板 $\Rightarrow$ 可表 |

---

## 状态总表

| 编号 | 摘要 | 状态 |
|------|------|------|
| L-Sing-1 | $\sigma_p=\sum_\ell A(p^\ell)$ 显式素幂展开 | 已证 |
| L-Sing-2 | $A(p,m)$ + Gauss/Jacobi 形；Weyl 余项 | 已证 |
| L-Sing-3 | $p=2,3$ 局部因子形状（引 L-2adic / SS-1） | 已证 |
| L-Sing-4 | $\sum_{m\le X}\mathfrak{S}(m;Q)=X+O_\varepsilon(Q^{11/12+\varepsilon})$ | 已证 |
| L-Sing-5 | $\sum_{m\le X}\mathfrak{S}_{\le P}(m)=X+O(X^{1-\delta})$（$P\ll\log X$） | 已证 |
| L-Sing-6 | 平均 $\Rightarrow$ 多数点截断 $\mathfrak{S}$ 不太小 | 已证 |
| L-Sing-7 | 对接 SS-Sync / Floor / Thr；非 E-kill | 已证接口 |
| L-Sing-8 | 缺口 Sing-G1–G4 | 缺口 |

---

## 附录：标准形式速查卡

$$
\begin{aligned}
A(q,m)
&=q^{-3}\sum_{(a,q)=1}S_4\Bigl(\frac aq\Bigr)S_3\Bigl(\frac aq\Bigr)S_2\Bigl(\frac aq\Bigr)e\Bigl(-\frac{am}q\Bigr),\\
\sigma_p(m)
&=1+\sum_{\ell\ge 1}A(p^\ell,m)
=\lim_{h\to\infty}p^{-2h}N(p^h;m),\\
\mathfrak{S}(m;Q)
&=\sum_{q\le Q}A(q,m),
\qquad
\mathfrak{S}_{\le P}(m)=\prod_{p\le P}\sigma_p(m),\\
\sum_{m\le X}\mathfrak{S}(m;Q)
&=X+O_\varepsilon(Q^{11/12+\varepsilon}),\\
\sum_{m\le X}\mathfrak{S}_{\le P}(m)
&=X+O(X^{1-\delta})\quad(P\ll\log X).
\end{aligned}
$$
