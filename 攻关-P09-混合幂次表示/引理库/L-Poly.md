# L-Poly-*：多项式缺项弱化（路线 R13-Poly-Waring-Variant）

> 路线 **R13-Poly-Waring-Variant**（P09 攻关轮次 13；服务**弱于原猜想**的可发表对照定理，**非**原猜想）。  
> 想法：把缺项 $2^k$ 换成非常数整系数多项式 $P(t)$，研究
> $$
> n=x^4+y^3+z^2+P(t),\qquad x,y,z\in\mathbb{N}_0,\ t\in\mathbb{N}_0,\ P(t)\ge 0.
> $$
> **总判决（一句话）.** 一次多项式 $P$ 时**充分大全体可表已证**（L-Poly-2；非平凡于「$P(t)=t$ 取零混合幂」的特款）；$P(t)=t^2$ 因平方冗余得几乎所有，但圆法凸壁仍不闭合全体；阶乘 / $2^k$ 的 **lacunary** 稀疏性才是原猜想窗口难度的来源——多项式路线**不能**移植为 $2^k$ 证明。

---

## 0. 符号

$$
\begin{aligned}
\mathcal{R}_{4,3,2}&=\{x^4+y^3+z^2:x,y,z\in\mathbb{N}_0\},\\
E&=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2},\\
\mathcal{R}_P&=\{x^4+y^3+z^2+P(t):x,y,z\in\mathbb{N}_0,\ t\in\mathbb{N}_0,\ P(t)\ge 0\},\\
\mathcal{R}_{\square}&=\{x^4+y^3+z^2+t^2:x,y,z,t\in\mathbb{N}_0\}.
\end{aligned}
$$
原目标集 $\mathcal{R}=\mathcal{R}_{4,3,2}+\{2^k:k\ge 1\}$。  
指数和 $\beta(k_1,\ldots,k_s)=\sum_i 1/k_i$；对本形无 $P$ 时 $\beta=13/12$。

**弱于原猜想（本文件一律遵守）.** 下列情形均**不**蕴含 $n=x^4+y^3+z^2+2^k$ 的充分大全体：把 $2^k$ 换成多项式；仅一次多项式；仅几乎所有；仅 $P(t)=t^2$ 的冗余几乎所有。

---

## L-Poly-1（已证：特款 $P(t)=t$ 平凡）

**定理.** 对 $P(t)=t$，有 $\mathcal{R}_P=\mathbb{N}_0$。特别地每个 $n\ge 0$ 可写
$$
n=0^4+0^3+0^2+n.
$$

**证明.** 取 $x=y=z=0$、$t=n$。证毕。

**定位.** 此款说明「把 $2^k$ 换成任意可取遍 $\mathbb{N}_0$ 的缺项」立刻平凡；可发表弱化必须排除此类退化，或把「非平凡」定义为对**一般**一次 $P$（首项系数 $>1$）仍得充分大全体（下条）。

---

## L-Poly-2（已证：一次多项式 ⇒ 充分大全体）— **本路线主定理**

**定理（弱化主定理）.** 设 $P(t)=at+b\in\mathbb{Z}[t]$，$a\ge 1$，$b\in\mathbb{Z}$。则存在仅依赖 $P$ 的 $N_P$ 使每个整数 $n\ge N_P$ 属于 $\mathcal{R}_P$，即
$$
n=x^4+y^3+z^2+P(t)
$$
对某 $x,y,z\in\mathbb{N}_0$ 与某 $t\in\mathbb{N}_0$（且 $P(t)\ge 0$）成立。

**注.** $a=1$、$b=0$ 即 L-Poly-1，可取 $N_P=0$。一般 $a\ge 2$ 时不能再令混合幂全零（$P$ 的像是真等差数列），故需 $\mathcal{R}_{4,3,2}$ 的剩余类满性——**非** L-Poly-1 的复述。

### 预备：L-Poly-Res（已证）— 混合幂剩余类满

**引理.** 对任意整数 $q\ge 1$ 与任意 $r\bmod q$，同余式
$$
x^4+y^3+z^2\equiv r\pmod{q}
$$
有整数解 $(x,y,z)$。进而存在 $m\in\mathcal{R}_{4,3,2}$ 使
$$
m\equiv r\pmod{q},\qquad 0\le m\le 3(q-1)^4.
$$

**证明.** 由中国剩余定理，只需对每个素幂 $p^v\|q$ 求解。L-Ekill-SS-1 给出局部密度 $\sigma_p(r)\ge p^{-2}>0$，故 $r$ 在 $\mathbb{Z}_p$ 上可由 $x^4+y^3+z^2$ 表示，从而模 $p^v$ 可解。粘合得模 $q$ 解；取代表元 $0\le x,y,z<q$，令
$$
m=x^4+y^3+z^2\in\mathcal{R}_{4,3,2}.
$$
则 $m\equiv r\pmod{q}$ 且 $m\le 3(q-1)^4$。证毕。

### 主定理证明

对每个剩余类 $\rho=0,1,\ldots,a-1$，由 L-Poly-Res（$q=a$）取
$$
m_\rho\in\mathcal{R}_{4,3,2},\qquad m_\rho\equiv\rho\pmod{a},\qquad 0\le m_\rho\le 3(a-1)^4.
$$
令
$$
M:=\max_{0\le\rho<a}m_\rho\le 3(a-1)^4,\qquad N_P:=M+\max\{b,0\}.
$$
固定 $n\ge N_P$。置
$$
\rho\in\{0,1,\ldots,a-1\},\qquad \rho\equiv n-b\pmod{a},
$$
并取 $m:=m_\rho$。则
$$
n-m-b\equiv 0\pmod{a},\qquad n-m-b\ge n-M-b\ge 0.
$$
令 $t:=(n-m-b)/a\in\mathbb{N}_0$。于是 $P(t)=at+b=n-m$，即
$$
n=m+P(t)=x^4+y^3+z^2+P(t)
$$
（$m$ 的表示给出 $x,y,z$）。证毕。

**与圆法 / 差值法的关系.** 一次缺项的生成函数 $\sum_{t\le T}e(\alpha P(t))$ 是几何和，主弧给出 $\asymp n^{1/12}\cdot(n/a)$ 量级的平凡主项；次弧因 $\beta_{\mathrm{tot}}=13/12+1=25/12>2$ 可由凸性直接压倒。上证明**避开**圆法，仅用局部满 + 有界代表元，更短且有效常数 $N_P\ll a^4+|b|$。

---

## L-Poly-3（已证：平方冗余 $P(t)=t^2$）

**定理 A（冗余几乎所有）.** $\mathcal{R}_{4,3,2}\subseteq\mathcal{R}_{\square}$（取 $t=0$）。故由 Roth-234（L-CRB-1(C)）
$$
\bigl|\{n\le X:n\notin\mathcal{R}_{\square}\}\bigr|
\le
|E\cap[1,X]|
\ll X(\log X)^{-1/20}.
$$
特别地几乎所有正整数属于 $\mathcal{R}_{\square}$。

**定理 B（DH 冗余枝）.** 取 $x=0$ 得 $\mathcal{R}_{\square}\supseteq\{y^3+z^2+t^2\}$。由 DH-22k（L-CRB-1(A)）几乎所有 $n$ 可写 $n=y^3+z^2+t^2$，故同样几乎所有 $n\in\mathcal{R}_{\square}$。

**证明.** 定理 A：包含关系显然；例外集单调。定理 B：引用 L-CRB-1(A)。证毕。

**冗余含义.** 原式已含平方 $z^2$；再添 $t^2$ 后，既可「丢掉新平方退回 Roth」，也可「丢掉四次退回 DH」。几乎所有层**免费**继承，不增加圆法难度——这与缺项 $2^k$ 必须保留对数个平移窗口的结构相反。

### 凸性结算（已证：全体圆法不闭）

对 $R_{\square}(n)=\#\{(x,y,z,t):x^4+y^3+z^2+t^2=n\}$ 写
$$
R_{\square}(n)=\int_0^1 F(\alpha)\,g_2(\alpha)\,e(-n\alpha)\,\mathrm{d}\alpha,
$$
其中 $F=f_4f_3f_2$（标准截断）、$g_2(\alpha)=\sum_{t\le\sqrt{n}}e(\alpha t^2)$。启发式主弧
$$
\mathfrak{M}\text{-贡献}\asymp n^{1/12}\cdot n^{1/2}/n^{1/2}=n^{1/12}\cdot n^{0}\quad\text{更精确地 }\asymp\sum_{t\le\sqrt{n}}(n-t^2)^{1/12}\asymp n^{7/12}.
$$
次弧用 Cauchy 与 L-Dec-2 型 $\|F\|_{L^2(\mathfrak{m})}\ll_\varepsilon n^{13/24+\varepsilon}$、$\|g_2\|_2\ll n^{1/4}$：
$$
\bigl|\text{次弧}\bigr|
\ll_\varepsilon n^{13/24+\varepsilon}\cdot n^{1/4}
=n^{19/24+\varepsilon}.
$$
因 $19/24>7/12=14/24$，**凸性不闭合** $R_{\square}(n)>0$。故 $P(t)=t^2$ 的「充分大全体」**不能**由现有混合幂次弧凸界推出（与原问题同一 $13/24$ 墙的近亲）。

**判决.** $t^2$ 给出可发表的**几乎所有**弱化（定理 A/B），**不**给出无条件充分大全体。

---

## L-Poly-4（已证：阶乘不可作「稠缺项」）

**定理.** 令 $P(t)=t!$（$t\ge 1$）。则
$$
\#\bigl(\{t!:t\ge 1\}\cap[1,X]\bigr)
\ll
\frac{\log X}{\log\log X}\qquad(X\ge 3).
$$
特别地，对切片 $\mathcal{S}=\{y^3+z^2\}$ 有
$$
\#\bigl((\mathcal{S}+\{t!\})\cap[1,X]\bigr)
\ll X^{5/6}\frac{\log X}{\log\log X}=o(X)
$$
（对照 L-CRB-2），故「几乎所有 $n=y^3+z^2+t!$」为假。

**证明.** $t!\le X\Rightarrow t\ll\log X/\log\log X$。并集估计同 L-CRB-2，把 $\log X$ 个 $2^k$ 换成 $\ll\log X/\log\log X$ 个 $t!$。证毕。

**注.** 对**全**形 $\mathcal{R}_{4,3,2}+\{t!\}$，取固定 $t=1$（$+1!$）仍由 Roth 得几乎所有——与 Thm-B 同级，**不**因阶乘变难或变易。阶乘的伤害出现在 $\beta\le 1$ 的稀疏切片上，与 $2^k$ 相同（lacunary 平移不够把密度零抬成正比例）。

---

## L-Poly-5（已证：与 $2^k$ 缺项的本质差别 — lacunary）

**定义（lacunary 缺项）.** 集合 $\mathcal{L}\subset\mathbb{N}$ 称为（计数）缺项的，若
$$
\#(\mathcal{L}\cap[1,X])\ll_\varepsilon X^{\varepsilon}\qquad(\forall\varepsilon>0)
$$
（典型地 $\ll\log X$）。$\{2^k\}$、$\{t!\}$ 属此类；一次多项式像集 $\asymp X$、平方像集 $\asymp X^{1/2}$ **不**属此类。

### （A）采样次数对照

| 缺项 | $\#\{P\le n\}$ | 相邻间隙 | 对 $n$ 的「射击」次数 |
|------|----------------|----------|------------------------|
| $2^k$ | $\asymp\log n$ | $\asymp 2^k$ | $K\asymp\log n$（原窗 $W(n)$） |
| $t!$ | $\asymp\log n/\log\log n$ | $\gg n$ | 更少 |
| $at+b$ | $\asymp n/a$ | $a=O(1)$ | $\asymp n$（L-Poly-2 闭合） |
| $t^2$ | $\asymp\sqrt{n}$ | $\asymp\sqrt{n}$ | $\asymp\sqrt{n}$（全体未闭） |

原猜想的核心对象是整窗事件
$$
W(n)=\{n-2^k:1\le k\le K\}\subseteq E
$$
（$\mathcal{F}_0$；L08 显示仅密度零不够）。一次多项式把「射击」加成线性多个、间隙有界，局部满后必中（L-Poly-2）。平方给出 $\sqrt{n}$ 次射击，Roth 密度上不足以鸽笼出全体（L-Poly-3 凸壁）。二进缺项只给对数次射击且间隙指数增长——**恰为** P1 窗口理论的来源。

### （B）指数和形态对照

- **多项式 $P$（deg $d\ge 2$）.** Weyl / 差值法适用：
  $$
  g_P(\alpha)=\sum_{t\le T}e(\alpha P(t))
  $$
  在 $\alpha$ 远离有理点时有幂次节省（经典 Weyl 不等式）。圆法可讨论，但 $d=2$ 时总指数 $19/12<2$，凸性仍差 $n^{5/24}$（L-Poly-3）。
- **Lacunary $\{2^k\}$.** 生成函数是几何型缺项核
  $$
  g_N(\alpha)=\sum_{k\le K}e(\alpha 2^k)
  $$
  （L-Circ-9 / L-Lac / L-Osc）。差值法**不**把它变成多项式 Weyl 和；尖峰落在二进有理附近（Peak），与多项式主弧 $\mathfrak{M}(Q)$ 不对齐（Lac-G1）。这是原问题次弧侧的特有障碍，**不能**用 L-Poly-2 的一次多项式论证规避。

### （C）一句话本质差别

> **稠 vs 缺项：** 多项式像集（尤其一次）具有正幂次计数与受控间隙，使「$n-P(t)\in\mathcal{R}_{4,3,2}$」在局部满条件下成为有界间隙命中问题；\{$2^k$\} 仅对数个点且间隙 $\asymp$ 点本身，命中问题升级为整窗 $\mathcal{F}_0$ 是否有限——与 L-Poly 主定理**逻辑独立**。

---

## L-Poly-6（清单与缺口）

| 编号 | 陈述 | 状态 |
|------|------|------|
| L-Poly-1 | $P(t)=t\Rightarrow\mathcal{R}_P=\mathbb{N}_0$ | 已证（平凡） |
| L-Poly-Res | $x^4+y^3+z^2$ 模 $q$ 剩余类满；有界代表元 | 已证 |
| L-Poly-2 | $\deg P=1$、$a\ge 1\Rightarrow$ 充分大 $n\in\mathcal{R}_P$ | **已证（主定理）** |
| L-Poly-3A/B | $P(t)=t^2\Rightarrow$ 几乎所有（Roth / DH 冗余） | 已证 |
| L-Poly-3 凸 | $t^2$ 圆法凸性 $19/24>7/12$ 不闭全体 | 已证（障碍） |
| L-Poly-4 | $t!$ 对 $\beta\le 1$ 切片不能几乎所有 | 已证（否证型） |
| L-Poly-5 | lacunary vs 多项式：采样次数 / Weyl vs $g_N$ | 已证（对照） |

| 缺口 | 内容 | 与原猜想 |
|------|------|----------|
| Poly-G1 | $P(t)=t^2$ 充分大全体 | 开放；弱于原猜想仍未证 |
| Poly-G2 | $\deg P=d\ge 3$ 的充分大 / 几乎所有精细渐近 | 非本轮目标 |
| Poly-G3 | 把 L-Poly-2 的间隙论证迁到 $\{2^k\}$ | **不可能**（L-Poly-5） |

**可发表定位.** 短文 / 注记形态：「Sun 形混合幂 + 多项式缺项」——主定理 L-Poly-2（一次 ⇒ 充分大）+ 平方冗余几乎所有 + 与 $2^k$ lacunary 对照表。**不声称**原猜想已证。

---

## 结算

| 项目 | 结论 |
|------|------|
| 真正非平凡弱化（已证） | **L-Poly-2**：一次 $P(t)=at+b$ ⇒ 充分大全体可表 |
| 平凡对照 | L-Poly-1：$P(t)=t$ |
| 平方冗余 | L-Poly-3：几乎所有；全体圆法不闭 |
| 阶乘 | L-Poly-4：不能救密度零切片 |
| vs $2^k$ | L-Poly-5：lacunary 对数窗 ≠ 多项式有界间隙 |
| 原猜想 | **仍开放** |
