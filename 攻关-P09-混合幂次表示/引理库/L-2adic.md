# L-2adic：混合幂 $2$-进像集与整窗相关（路线 R7-2adic-Lift）

> 路线 **R7-2adic-Lift**（P09 攻关轮次 7，服务 **P1**，全新局部算术）。  
> 问题：真实例外集 $E=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2}$ 是否可能被 $2$-进条件大幅约束？定理 A 已含 $\mathcal{R}\bmod 8,16,32$ 满；本文件处理**不带** $2^k$ 的像集
> $$
> I_\nu:=\bigl\{x^4+y^3+z^2\bmod 2^\nu:x,y,z\in\mathbb{Z}/2^\nu\mathbb{Z}\bigr\},
> \qquad
> \delta_\nu:=\frac{|I_\nu|}{2^\nu},
> $$
> 并讨论窗点 $\{N-2^k\}$ 的高 $2$-进相关与「整窗全落 $E$」。  
> **不**声称 E-kill-1 / 原猜想已证。禁止数值穷举程序；小 $\nu$ 仅作结构核对（手算规模）。

---

## 0. 符号

沿用：
$$
\mathcal{R}_{4,3,2}=\{x^4+y^3+z^2:x,y,z\in\mathbb{N}_0\},
\qquad
E=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2},
$$
$$
W(N)=\{N-2^k:1\le k\le K\},
\quad
K=\lfloor\log_2(N-1)\rfloor,
\quad
\mathcal{F}_0=\{N\ge 2:W(N)\subseteq E\}.
$$
对每个 $\nu\ge 1$ 记禁类
$$
F_\nu:=(\mathbb{Z}/2^\nu\mathbb{Z})\setminus I_\nu,
\qquad
\varepsilon_\nu:=\frac{|F_\nu|}{2^\nu}=1-\delta_\nu.
$$
称 $N$ 被 **$\nu$-进强制整窗埋入 $E$**，若
$$
\forall\,1\le k\le K,\qquad
N-2^k\bmod 2^\nu\in F_\nu
$$
（此时每个窗点落在永不可表的剩余类中，故自动 $W(N)\subseteq E$，即 $N\in\mathcal{F}_0$）。

**与定理 A 的关系.** 定理 A 断言 $\mathcal{R}=\mathcal{R}_{4,3,2}+\{2^k\}$ 在 $m\in\{8,16,32\}$ 上满。本路线处理更强的对象 $I_\nu$（无 $2^k$）；若 $\delta_\nu=1$，则定理 A 在 $2$-幂上成为直接推论。

**与 L-Ekill-SS-1 的关系.** SS-1 的 $\sigma_2(m)\ge 2^{-2}$ 断言每个 $m$ 有正 $2$-进局部密度；本文件给出**像集层面**的初等群论证明 $\delta_\nu=1$，不依赖奇异级数正规化常数。

---

## L-2adic-1（已证：单位群上立方自同构）

设 $\nu\ge 3$。乘法群
$$
U_\nu:=(\mathbb{Z}/2^\nu\mathbb{Z})^\times
$$
满足标准同构
$$
U_\nu\;\cong\;C_2\times C_{2^{\nu-2}}
$$
（例如 $U_\nu=\{\pm 1\}\times\langle 5\rangle$，其中 $\langle 5\rangle$ 阶为 $2^{\nu-2}$）。于是映射
$$
\varphi:U_\nu\to U_\nu,\qquad u\mapsto u^3
$$
是群自同构；特别地 $\varphi$ **双射**，故每个奇剩余类皆为立方剩余。

**证明.** 写 $U_\nu\cong C_2\times C_{2^{\nu-2}}$。  
- 在 $C_2=\{1,-1\}$ 上，$(-1)^3=-1$，故立方为恒等（从而双射）。  
- 在循环 $2$-群 $C_{2^{\nu-2}}$ 上，立方等于指数乘 $3$。因 $\gcd(3,2^{\nu-2})=1$，$3$ 在 $\mathbb{Z}/2^{\nu-2}\mathbb{Z}$ 上可逆，故立方双射。  
二者直积上立方仍双射。证毕。

**小 $\nu$ 核对（手算，非程序）.**  
- $\nu=1$：奇类仅 $1\equiv(-1)^3$。  
- $\nu=2$：$U_2=\{1,3\}$，$1^3=1$，$3^3=27\equiv 3$。  
- $\nu=3$：$1,3,5,7$ 的立方依次 $\equiv 1,3,5,7\pmod 8$。  
与同构陈述一致。

**推论（奇类全落像）.** 对一切 $\nu\ge 1$ 与一切奇数 $a\in\mathbb{Z}/2^\nu\mathbb{Z}$，存在 $y$ 使 $y^3\equiv a$。取 $x=z=0$，得 $a\in I_\nu$。故一切奇类属于 $I_\nu$。

---

## L-2adic-2（已证：$\delta_\nu=1$；最优下界）

对一切整数 $\nu\ge 1$，
$$
I_\nu=\mathbb{Z}/2^\nu\mathbb{Z},
\qquad
\delta_\nu=1,
\qquad
F_\nu=\emptyset,
\qquad
\varepsilon_\nu=0.
$$
特别地，一致下界
$$
\inf_{\nu\ge 1}\delta_\nu=1
$$
已达绝对上界，无法再改进。

**证明.** 固定 $m\in\mathbb{Z}/2^\nu\mathbb{Z}$。  
**情形 A（$m$ 奇）.** 由 L-2adic-1 的推论，$m=y^3$ 对某 $y$ 成立。取 $x=z=0$，得 $m\in I_\nu$。  

**情形 B（$m$ 偶）.** 取 $z=1$，则 $z^2=1$，并令 $a:=m-1$。此时 $a$ 为奇数，再由情形 A 得 $a=y^3$。取 $x=0$，则
$$
x^4+y^3+z^2\equiv y^3+1\equiv m\pmod{2^\nu}.
$$
故 $m\in I_\nu$。  

两情形穷尽，得 $I_\nu$ 满，即 $\delta_\nu=1$。证毕。

**弱下界旁注（不依赖立方双射）.** 仅用平方：$U_\nu$ 中平方子群指数为 $4$（$\nu\ge 3$），奇平方类恰有 $2^{\nu-3}$ 个，故
$$
\delta_\nu\ge\frac{2^{\nu-3}}{2^\nu}=\frac18
$$
（取 $x=y=0$，$z$ 奇）。L-2adic-2 将此 $1/8$ 提升至 $1$。

**结构性后果.**  
1. **无 $2$-进禁类.** 不存在剩余类 $a\bmod 2^\nu$ 使 $a+2^\nu\mathbb{Z}\subseteq E$ 仅由局部像集空缺所强制。  
2. **与定理 A 兼容.** 因 $I_\nu$ 已满，$\mathcal{R}_{4,3,2}+2^k$ 在 $2$-幂上当然满（定理 A 的 $8,16,32$ 段）。  
3. **不蕴含整点可表.** $m\in I_\nu$ 仅说存在 $2$-进（或模 $2^\nu$）解，**不**说 $m\in\mathcal{R}_{4,3,2}$。故 $\delta_\nu=1$ **不**把 $E$ 逼成空集，也不单独杀 $\mathcal{F}_0$（对照 L08）。

---

## L-2adic-3（已证：窗点的 $2$-进相关结构）

设 $\nu\ge 1$、$N\in\mathbb{Z}$、$K\ge 1$。定义窗残向量
$$
\pi_\nu(N):=\bigl(N-2^k\bmod 2^\nu\bigr)_{1\le k\le K}\in\bigl(\mathbb{Z}/2^\nu\mathbb{Z}\bigr)^K.
$$

**(A) 分段公式.** 对每个 $k$，
$$
N-2^k\bmod 2^\nu
=
\begin{cases}
N-2^k\bmod 2^\nu,&\text{若 }1\le k<\nu,\\[4pt]
N\bmod 2^\nu,&\text{若 }k\ge\nu.
\end{cases}
$$
特别地：当 $K\ge\nu$ 时，坐标 $k=\nu,\nu+1,\ldots,K$ **全部相等**，皆等于 $N\bmod 2^\nu$。

**(B) 值域极小.** $\pi_\nu(N)$ 完全由 $a:=N\bmod 2^\nu$ 决定；记该映射为 $a\mapsto\pi_\nu^\ast(a)$。故
$$
\bigl|\{\pi_\nu(N):N\in\mathbb{Z}\}\bigr|\le 2^\nu.
$$
当 $K\ge\nu$ 时，像落在子簇
$$
\Xi_\nu:=\Bigl\{\,(r_k)_{k\le K}:\ \exists\,a,\ 
r_k=a-2^k\ (k<\nu),\ 
r_k=a\ (k\ge\nu)\,\Bigr\}
$$
上，且 $|\Xi_\nu|=2^\nu$（$a$ 与向量一一对应）。

**(C) 低位差分刚性.** 对 $1\le k<\ell<\nu$，
$$
\bigl((N-2^k)-(N-2^\ell)\bigr)\bmod 2^\nu
=2^k(2^{\ell-k}-1)\bmod 2^\nu,
$$
右端**不依赖** $N$，且因 $\ell-k\ge 1$、$k<\nu$ 而 $\not\equiv 0\pmod{2^\nu}$。故窗内低位坐标两两差被绝对常数钉死。

**证明.** （A）若 $k\ge\nu$ 则 $2^k\equiv 0\pmod{2^\nu}$。若 $k<\nu$ 则按定义。  
（B）由（A）立即得出；不同 $a$ 给出不同向量（看 $k\ge\nu$ 的公共坐标）。  
（C）直接相减。证毕。

**解读.** 整窗在模 $2^\nu$ 上**不是** $K$ 个近独立采样，而是一条由单参数 $a=N\bmod 2^\nu$ 生成的刚性轨道；高位（$k\ge\nu$）完全同步。这是与 L-Rand 独立 Bernoulli 模型、以及 L-SSO 奇素乘法轨道相正交的 $2$-进几何。

---

## L-2adic-4（已证：$\nu$-进强制整窗的判定与空集）

设 $K\ge\nu\ge 1$。则 $N$ 被 $\nu$-进强制整窗埋入 $E$ 当且仅当
$$
a:=N\bmod 2^\nu
\quad\text{满足}\quad
a\in F_\nu
\quad\text{且}\quad
a-2^k\in F_\nu\ \text{对一切 }1\le k<\nu.
$$
等价地：$a$ 落在
$$
\mathrm{Bad}_\nu:=\bigl\{a\in\mathbb{Z}/2^\nu\mathbb{Z}:
\{a\}\cup\{a-2^k:1\le k<\nu\}\subseteq F_\nu\bigr\}.
$$
由 L-2adic-2，$F_\nu=\emptyset$，故
$$
\mathrm{Bad}_\nu=\emptyset.
$$
因此**不存在**被任何 $\nu$-进禁类强制的整窗中心 $N$。

**证明.** 由 L-2adic-3(A)：$k\ge\nu$ 的条件合并为单一条件 $a\in F_\nu$；$k<\nu$ 给出 $a-2^k\in F_\nu$。再代入 $F_\nu=\emptyset$。证毕。

**结算（对「$2$-进是否大幅约束 $E$」）.**  
- **强制扩 $E$ 方向：** 空。$\delta_\nu=1$ 消灭一切由像集缺口产生的算术级数型例外。  
- **强制缩 $E$ / 杀整窗方向：** 局部满**不**给出整点可表，故不能把窗点踢出 $E$。  
- **相关本身不制造整窗：** 高位同步只在 $F_\nu\neq\emptyset$ 时才可能把「一点禁类」放大成「多点同步禁类」；本形 $F_\nu=\emptyset$，放大因子无效。  

结论：真实 $E$ **不能**被本形 $2$-进像集条件大幅约束；$\mathcal{F}_0$ 的真正硬度仍在全局/伪随机层（L08、AE-G1、Rand-G1–G3 等），不在 $2$-进溶解度。

---

## L-2adic-5（条件式：均匀正像密度 $+$ 可量化窗相关 $\Rightarrow$ 无强制整窗）

> 本条把 L-2adic-2/3/4 的逻辑写成**一般形**条件式，供对照「若像集仅有正密度而非满」的假想设定；在本题已由 L-2adic-2 以 $c=1$ 无条件闭合。

### 假设 2Ad-Dens$(c)$（像集均匀正密度）

存在绝对常数 $c\in(0,1]$ 使对一切 $\nu\ge 1$，
$$
\delta_\nu\ge c
\qquad\bigl(\text{即 }\varepsilon_\nu\le 1-c\bigr).
$$

### 假设 2Ad-Corr（窗相关可量化）

存在函数 $\Psi:\mathbb{N}\to\mathbb{R}_{\ge 0}$ 与绝对常数 $C_\Psi<\infty$，使对一切 $\nu\ge 1$、一切 $A\subseteq\mathbb{Z}/2^\nu\mathbb{Z}$，
$$
\frac{|\mathrm{Bad}_\nu(A)|}{2^\nu}
\le
\Psi(\nu)\Bigl(\frac{|A|}{2^\nu}\Bigr)^{\gamma}
\quad\text{或}\quad
\mathrm{Bad}_\nu(A)=\emptyset\text{ 当 }|A|/2^\nu<c_0,
$$
其中
$$
\mathrm{Bad}_\nu(A):=\bigl\{a:\{a\}\cup\{a-2^k:k<\nu\}\subseteq A\bigr\},
$$
且 $\gamma\ge 1$、$c_0>0$（量化「单参数轨道同时落入瘦集 $A$」的代价）。

**本题中的已证例.** 取 $A=F_\nu$。由 L-2adic-3，
$$
\frac{|\mathrm{Bad}_\nu|}{2^\nu}
\le
\mathbf{1}_{F_\nu\neq\emptyset}\cdot\min\bigl(1,\varepsilon_\nu\bigr)
$$
的粗界成立；更锐地，L-2adic-2 给出 $\varepsilon_\nu=0\Rightarrow\mathrm{Bad}_\nu=\emptyset$，即 2Ad-Corr 以「阈值阈值」成立（$\Psi$ 任意，$\gamma$ 任意）。

### 条件式结论

若 2Ad-Dens$(c)$ 与 2Ad-Corr 同时成立，且
$$
\Psi(\nu)\,(1-c)^{\gamma}<1
\quad\text{对一切充分大 }\nu
$$
（或直接 $\mathrm{Bad}_\nu(F_\nu)=\emptyset$），则对一切充分大 $N$，
$$
N\text{ 不被任何 }\nu\text{-进禁类强制整窗埋入 }E.
$$
特别地：**不存在**无限多的「纯 $2$-进强制」型 $\mathcal{F}_0$ 点。

**证明（形式蕴含）.** 强制整窗 $\Leftrightarrow N\bmod 2^\nu\in\mathrm{Bad}_\nu(F_\nu)$（L-2adic-4 的一般形）。由 2Ad-Dens 有 $|F_\nu|/2^\nu\le 1-c$；再由 2Ad-Corr 得 $|\mathrm{Bad}_\nu(F_\nu)|/2^\nu$ 严格小于 $1$ 或为零。若对一切大 $\nu$ 有 $\mathrm{Bad}_\nu(F_\nu)=\emptyset$，则无强制中心。证毕。

**本题代入.** 2Ad-Dens$(1)$ 已证（L-2adic-2）；2Ad-Corr 以 $\mathrm{Bad}_\nu=\emptyset$ 已证（L-2adic-4）。故条件式结论在 $c=1$ 时成为**无条件定理**：无 $2$-进强制整窗。

**与「不能整窗」的语义边界（必读）.**  
本条件式阻断的是
$$
W(N)\subseteq\bigcup_{a\in F_\nu}(a+2^\nu\mathbb{Z})\subseteq E
$$
这类**局部禁类制造的整窗**。它**不**阻断 $W(N)\subseteq E$ 但窗点皆落在 $I_\nu$（可表类）上的整窗——后者恰是真实 $\mathcal{R}_{4,3,2}$ 的全局例外机制（Roth 稀例外沿刚性二进轨道对齐），硬度与 L08 / Rand 种植同级。故：

> **$\delta_\nu\ge c>0$ 均匀 $+$ 窗相关可量化 $\Rightarrow$ 不能「禁类强制整窗」；$\not\Rightarrow$ 真实 $\mathcal{F}_0$ 有限。**

---

## L-2adic-6（已证对照：与奇素轨道 / 随机模型的正交性）

| 对象 | 窗采样几何 | 局部满时对整窗的杀伤 |
|------|------------|----------------------|
| $p=2$（本路线） | 高位同步：$k\ge\nu\Rightarrow N-2^k\equiv N$（L-2adic-3） | 像满 $\Rightarrow$ 禁类空 $\Rightarrow$ 无强制整窗；**不**杀全局例外整窗 |
| $p$ 奇（L-SSO-3/4） | $k\mapsto 2^k\bmod p$ 乘法圆周 | 单素坏弧长 $\le(1-\kappa_p)P_p$；需多素同步才压长窗 |
| 独立 Bernoulli（L-Rand-3） | 近独立稀疏 | 任意 $\kappa>0$ 已 a.s. 杀 $\widetilde{\mathcal{F}}_0$ |
| 尺度种植（L-Rand-5） | 整窗团块耦合 | $\kappa\le 1$ 可无限；与 $2$-进禁类机制无关 |

**一句话.** $2$-进路线澄清：局部算术在 $p=2$ 上对 $\mathcal{R}_{4,3,2}$ **零阻力**（$\delta_\nu=1$）；整窗问题的 $2$-进侧面是「相关但不禁类」，不能替代反整窗伪随机假设。

---

## 缺口表（2Ad-G）

| 代号 | 内容 | 若解决则得 |
|------|------|------------|
| 2Ad-G1 | 将「模 $2^\nu$ 可表」有效抬升为「整点可表」的 $2$-进 Hensel$+$拱条件（本质回到圆法/SS-阈值） | 单点可表；仍未必杀整窗 |
| 2Ad-G2 | 量化真实 $E$ 在固定类 $a\bmod 2^\nu$ 内的分布（超纯像集） | 可能得类内反整窗 |
| 2Ad-G3 | 窗相关与 FW/AE 联立：同步残类上的加性能量 / 低频指纹 | 条件式 E-kill 接口 |

**主缺口.** 2Ad-G1–G3 均超出「像集密度」；本路线已证块在 $\delta_\nu=1$ 与强制整窗空集处**闭合**，对 E-kill-1 无增量定理。

---

## 本轮结论

| 编号 | 状态 | 摘要 |
|------|------|------|
| L-2adic-1 | 已证 | $U_\nu$ 上 $u\mapsto u^3$ 自同构；奇类皆立方 |
| L-2adic-2 | 已证 | $I_\nu$ 满，$\delta_\nu=1=\inf_\nu\delta_\nu$ |
| L-2adic-3 | 已证 | 窗残向量单参数；$k\ge\nu$ 完全同步 |
| L-2adic-4 | 已证 | $\mathrm{Bad}_\nu=\emptyset$；无 $2$-进强制整窗 |
| L-2adic-5 | 条件式（本题 $c=1$ 已闭合） | 若 $\delta_\nu\ge c>0$ 均匀且窗相关可量化 $\Rightarrow$ 无禁类强制整窗 |
| L-2adic-6 | 已证对照 | 与 SSO / Rand 正交结算 |

**对 P1 的判决.** 真实 $E$ **不被** $x^4+y^3+z^2$ 的 $2$-进像集缺口大幅约束（缺口不存在）。窗相关是真实的，但在 $\delta_\nu=1$ 下**不能**据此制造或消灭真实整窗。E-kill-1 仍开放。原猜想保持开放。
