# L-Trans-*：好模 CRT 拼接与 $2^k$ 乘法提升（路线 R17-Transfer-Moduli）

> 路线 **R17-Transfer-Moduli**（P09 攻关轮次 17，服务 **P1 = E-kill-1 / 可表**，全新）。  
> 想法：用中国剩余定理把「好模」上的局部像拼成乘积模上的同步条件；已知定理 A′ 断言目标集
> $$
> \mathcal{R}=\{x^4+y^3+z^2+2^k\}
> $$
> 在 $63,72$ 上满剩余。研究是否存在模数序列 $(q_j)$ 与提升引理，使若 $n$ 在足够多 $q_j$ 上「局部像可表」，则存在 $k$ 使 $n-2^k\in\mathcal{R}_{4,3,2}$。  
> **硬约束.** 一般「分模满 $\Rightarrow$ 乘积模同步满」已否证（对抗审查 §2；$B=\{0,\ldots,71\}\subset\mathbb{Z}/504\mathbb{Z}$）；本路线**必须**调用 $2^k$ 在奇模单位群中的乘法动态，禁止把集合投影满当作自动粘合。  
> **总判决（一句话）.** 有限个奇模上的指数轨道可经 CRT **同步**；有限乘积上的「局部像可表」可拼成模 $Q$ 同余条件，且目标集 $\mathcal{R}$ 对任意固定模皆满（经 $\mathcal{R}_{4,3,2}$ 局部满 + 固定 $k$，**非**分模投影）。从「任意大乘积上局部像」到「整点 $n-2^k\in\mathcal{R}_{4,3,2}$」需尺度控制，记为条件式无限提升缺口。  
> 状态：`已证` / `条件式` / `缺口`。**不声称原猜想 / E-kill / 充分大全体已证。**

---

## 0. 符号

$$
\begin{aligned}
\mathcal{R}_{4,3,2}&=\{x^4+y^3+z^2:x,y,z\in\mathbb{N}_0\},\\
E&=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2},\\
\mathcal{R}&=\mathcal{R}_{4,3,2}+\{2^k:k\ge 1\},\\
W(n)&=\{n-2^k:1\le k\le K\},\quad K=\lfloor\log_2(n-1)\rfloor,\\
\mathcal{F}_0&=\{n\ge 2:W(n)\subseteq E\}.
\end{aligned}
$$

对奇数 $q\ge 1$，记
$$
I(q):=\{x^4+y^3+z^2\bmod q:x,y,z\in\mathbb{Z}\}\subseteq\mathbb{Z}/q\mathbb{Z},
$$
以及乘法阶
$$
P_q:=\mathrm{ord}_q(2)=\min\{t\ge 1:2^t\equiv 1\pmod{q}\}
$$
（当 $\gcd(2,q)=1$ 时在 $(\mathbb{Z}/q\mathbb{Z})^\times$ 内有定义；若 $q$ 不整除奇数则对 CRT 分解到奇素幂分量）。对两两互素的奇模 $q_1,\ldots,q_J$，令
$$
Q_J:=\prod_{j=1}^J q_j,\qquad
P^{(J)}:=\mathrm{lcm}(P_{q_1},\ldots,P_{q_J})=\mathrm{ord}_{Q_J}(2).
$$

**「局部像可表」（本路线工作定义）.** 称 $n$ 在模 $q$ 上对指数类 $\kappa\bmod P_q$ **局部像可表**，若
$$
n-2^\kappa\bmod q\ \in\ I(q).
$$
（若指定好子集 $G_q\subseteq I(q)$，则要求落入 $G_q$；无特殊声明时取 $G_q=I(q)$。）

**引用骨架.**
- 定理 A / A′：$\mathcal{R}$ 在 $m\in\{7,8,9,13,16,32\}$ 及 $63,72$ 上满剩余。
- L-Poly-Res：任意 $q$，$I(q)=\mathbb{Z}/q\mathbb{Z}$，且有代表元 $m\in\mathcal{R}_{4,3,2}$，$0\le m\le 3(q-1)^4$。
- L-SSO-3：窗点 $n-2^k\bmod q$ 由乘法轨道 $k\mapsto 2^k\bmod q$ 决定。
- 对抗审查：分模投影满 $\not\Rightarrow$ 乘积同步满。

---

## L-Trans-1（已证：变量级 CRT ≠ 集合投影 CRT）

**(A) 集合投影机制（否证型提醒）.** 设 $q,r\ge 1$，$L=\mathrm{lcm}(q,r)$，$B\subseteq\mathbb{Z}/L\mathbb{Z}$。若投影
$$
\pi_q(B)=\mathbb{Z}/q\mathbb{Z},\qquad \pi_r(B)=\mathbb{Z}/r\mathbb{Z},
$$
**一般不**蕴含 $B=\mathbb{Z}/L\mathbb{Z}$。反例（审查 §2）：$q=63$，$r=72$，$L=504$，$B=\{0,1,\ldots,71\}$ 分别投影满，但 $100\notin B$。

**(B) 变量级 CRT（本形可用）.** 设 $q_1,\ldots,q_J$ 两两互素，$Q=\prod q_j$。若对每个 $j$ 存在 $(x_j,y_j,z_j)$ 使
$$
x_j^4+y_j^3+z_j^2\equiv a_j\pmod{q_j},
$$
则由 CRT 存在 $(x,y,z)$ 模 $Q$ 使
$$
x\equiv x_j,\ y\equiv y_j,\ z\equiv z_j\pmod{q_j}
\quad\Rightarrow\quad
x^4+y^3+z^2\equiv a\pmod{Q},
$$
其中 $a$ 是唯一满足 $a\equiv a_j\pmod{q_j}$ 的类。特别地：若每个 $I(q_j)=\mathbb{Z}/q_j\mathbb{Z}$，则 $I(Q)=\mathbb{Z}/Q\mathbb{Z}$。

**(C) 与 L-Poly-Res 对齐.** 由 L-Ekill-SS-1（$\sigma_p\ge p^{-2}>0$）+ 素幂粘合，已得任意 $q$ 上 $I(q)$ 满；故对任意有限奇乘积 $Q_J$，
$$
I(Q_J)=\mathbb{Z}/Q_J\mathbb{Z}.
$$

**证明.** （A）见审查反例。（B）标准 CRT 作用于三元组坐标。（C）引 L-Poly-Res。证毕。

**结算.** 「定理 A′ 的 $63$ 满 + $72$ 满」**不能**经（A）推出 $\mathcal{R}$ 模 $504$ 满；若要乘积满，必须（i）变量级拼 $\mathcal{R}_{4,3,2}$，或（ii）直接验证同步类，或（iii）用固定 $k$ + $I(L)$ 满（下条）。禁止再写分模投影自动合并。

---

## L-Trans-2（已证：有限奇模上 $2^k$ 指数 CRT 同步）

设 $q_1,\ldots,q_J$ 为两两互素的奇数，$Q=Q_J$，$P=P^{(J)}=\mathrm{ord}_Q(2)$。给定
$$
b_j\in\langle 2\rangle\subseteq(\mathbb{Z}/q_j\mathbb{Z})^\times\qquad(j=1,\ldots,J),
$$
下列等价：

1. 存在整数 $k$ 使对一切 $j$，
$$
2^k\equiv b_j\pmod{q_j};
$$
2. 存在 $b\bmod Q$ 使 $b\equiv b_j\pmod{q_j}$ 且 $b\in\langle 2\rangle\subseteq(\mathbb{Z}/Q\mathbb{Z})^\times$；
3. 对一切 $i,j$，若 $t_{ij}$ 满足 $2^{t_{ij}}\equiv 1\pmod{\gcd(q_i,q_j)}$（此处 $\gcd=1$，条件空），则 $b_i,b_j$ 经 CRT 兼容，且
$$
b_j\equiv 2^{\kappa_j}\pmod{q_j}
$$
对某 $\kappa_j$ 时，诸 $\kappa_j$ 在
$$
\kappa_i\equiv\kappa_j\pmod{\gcd(P_{q_i},P_{q_j})}
$$
下有公共解 $\kappa\bmod P$。

此时公共解 $\kappa$ 在模 $P$ 上唯一确定一个类，且对一切整数 $\ell$，
$$
k=\kappa+\ell P
$$
给出同一组 $(b_j)$。

**证明.** 因 $q_j$ 两两互素，$\prod q_j=Q$ 上 CRT 给出唯一 $b\bmod Q$。又
$$
\langle 2\rangle_Q\ \xrightarrow{\pi_{q_j}}\ \langle 2\rangle_{q_j}
$$
为满同态（阶为 $P_{q_j}\mid P$），故 $b\in\langle 2\rangle_Q$ 当且仅当各投影 $b_j\in\langle 2\rangle_{q_j}$ 且指数在 $\mathrm{lcm}$ 意义下兼容。指数同余组
$$
\kappa\equiv\kappa_j\pmod{P_{q_j}}
$$
有解 $\Leftrightarrow$ $\kappa_i\equiv\kappa_j\pmod{\gcd(P_{q_i},P_{q_j})}$；解空间模 $P=\mathrm{lcm}_j P_{q_j}$ 恰一类。证毕。

**与窗采样.** 对固定 $n$，条件 $n-2^k\equiv a_j\pmod{q_j}$ 等价于
$$
2^k\equiv n-a_j\pmod{q_j}
$$
（需 $n-a_j$ 与 $q_j$ 互素，或落到 $2$ 的轨道可及类）；故「各模选定目标差类 $a_j\in I(q_j)$」能否被**同一** $k$ 实现，正是本引理的指数 CRT。这是本路线相对「无 $2^k$ 的死集合投影」的全部动态增量。

---

## L-Trans-3（已证：有限 CRT 拼引理 — 局部像 $\Rightarrow$ 乘积模同步像）

设 $q_1,\ldots,q_J$ 两两互素奇数，$Q=Q_J$。设对每个 $j$ 给定 $a_j\in I(q_j)$，并假设存在整数 $k$ 使
$$
n-2^k\equiv a_j\pmod{q_j}\qquad(j=1,\ldots,J)
$$
（即 L-Trans-2 的指数同步成立）。则：

**(A) 乘积同余.** 存在唯一 $a\bmod Q$ 使 $a\equiv a_j\pmod{q_j}$，且
$$
n-2^k\equiv a\pmod{Q},\qquad a\in I(Q).
$$

**(B) 变量实现.** 存在 $(x,y,z)\in\mathbb{Z}^3$ 使
$$
x^4+y^3+z^2\equiv a\equiv n-2^k\pmod{Q}.
$$

**(C) 有界整代表（弱）.** 存在 $m\in\mathcal{R}_{4,3,2}$ 使
$$
m\equiv a\pmod{Q},\qquad 0\le m\le 3(Q-1)^4.
$$
（一般 $m\neq n-2^k$；仅同余。）

**证明.** （A）CRT 得 $a$；由 L-Trans-1(B)(C) 知 $a\in I(Q)$。同步假设给出 $n-2^k\equiv a_j$ 故 $\equiv a\pmod{Q}$。（B）$I(Q)$ 的定义。（C）L-Poly-Res。证毕。

**解读.** 这是「有限 CRT 拼」的全部已证内容：把各模局部像 $a_j$ 与**同一** $2^k$ 粘成模 $Q$ 的像条件。它**不**给出 $n-2^k\in\mathcal{R}_{4,3,2}$，因为同余解的代表元可达 $O(Q^4)$，而 $|n-2^k|\asymp n$ 与 $Q$ 无强制相等。

---

## L-Trans-4（已证：$\mathcal{R}$ 对任意固定模满 — 用 $2^k$ 动态 + $I(q)$，非分模投影）

**定理.** 对任意整数 $M\ge 1$ 与任意剩余类 $r\bmod M$，存在 $x,y,z\in\mathbb{N}_0$ 与 $k\ge 1$ 使
$$
x^4+y^3+z^2+2^k\equiv r\pmod{M}.
$$
即 $\mathcal{R}$ 在每一个模 $M$ 上满剩余。特别地，$\mathcal{R}$ 模 $504=\mathrm{lcm}(63,72)$ 满。

**证明.** 取固定 $k=1$。由 L-Poly-Res（$q=M$）取 $m\in\mathcal{R}_{4,3,2}$ 使
$$
m\equiv r-2\pmod{M},\qquad 0\le m\le 3(M-1)^4.
$$
则 $m+2\in\mathcal{R}$ 且 $m+2\equiv r\pmod{M}$。证毕。

**注（为何仍要写 $63/72$.）** 定理 A′ 是历史骨架；本条用更强的 $I(M)$ 满一次证完所有 $M$。关键点：满剩余的正确证明路径是「固定 $k$ + 混合幂局部满」，**不是**「$63$ 满与 $72$ 满的集合投影」。若禁止引用 L-Poly-Res、仅允许 A′，则模 $504$ 仍须直接验证或改走变量级同步，不能调用审查反例所否证的投影推理。

**与目标猜想的距离.** 本条只说每个算术级数都碰到 $\mathcal{R}$；原猜想要求每个充分大（实为每个 $\ge 2$）的 $n$ 本身属于 $\mathcal{R}$，即 $W(n)\not\subseteq E$。满剩余对 $\mathcal{F}_0$ **零杀伤**（对照 L08）。

---

## L-Trans-5（已证：有限模局部条件对整窗无强制）

设 $Q\ge 1$ 固定（可奇可偶）。因 $I(Q)=\mathbb{Z}/Q\mathbb{Z}$（L-Poly-Res），对任意 $n$ 与任意 $k$，
$$
n-2^k\bmod Q\ \in\ I(Q)
$$
**恒成立**。因此：

1. 「在模 $Q$ 上局部像可表」对 $G_Q=I(Q)$ **不提供**任何筛选；每个窗点都局部像可表。  
2. 不存在由「有限个好模上像集缺口」强制的整窗中心（与 L-2adic-4 在 $p=2$ 上的结论同型；奇模更空）。  
3. 若要把局部条件作成真正筛子，必须换用**真子集** $G_q\subsetneq I(q)$（例如奇异级数截断大类、主弧可达类、或有效代表元高度受限类）。

**证明.** $I(Q)$ 满 $\Rightarrow$ 每个剩余类皆像。证毕。

**推论（筛子必须加严）.** 本路线若仅用 $G_q=I(q)$，则「足够多 $q_j$ 上局部像可表」对一切 $n$ 自动成立，**不能**推出 $\exists k:\ n-2^k\in\mathcal{R}_{4,3,2}$。有效转移必须进入下方条件式（好类真瘦 + 尺度提升）。

---

## L-Trans-6（已证：好类真子集下的有限同步准则）

设对每个奇模 $q$ 指定 $G_q\subseteq I(q)$。称 $n$ 在模 $q$ 上 **$G$-局部可表**，若存在 $\kappa\bmod P_q$ 使
$$
n-2^\kappa\bmod q\ \in\ G_q.
$$
记可实现指数集
$$
\mathcal{K}_q(n;G):=\bigl\{\kappa\bmod P_q:n-2^\kappa\in G_q\bigr\}.
$$

**有限同步引理.** 设 $q_1,\ldots,q_J$ 两两互素奇数。则存在公共 $k$ 使
$$
n-2^k\bmod q_j\ \in\ G_{q_j}\quad(\forall j)
$$
当且仅当指数同余组
$$
\kappa\equiv\kappa_j\pmod{P_{q_j}},\qquad \kappa_j\in\mathcal{K}_{q_j}(n;G)
$$
有解，即诸 $\mathcal{K}_{q_j}$ 在
$$
\prod_j(\mathbb{Z}/P_{q_j}\mathbb{Z})
$$
上经 L-Trans-2 的兼容条件非空。此时全体公共解构成模 $P^{(J)}$ 的有限并条算术级数。

**证明.** 直接代入 L-Trans-2：$b_j\equiv n-a_j$ 对某 $a_j\in G_{q_j}$。证毕。

**密度形式（有限 $J$）.** 若各 $\mathcal{K}_{q_j}$ 的密度
$$
\delta_j:=\frac{|\mathcal{K}_{q_j}(n;G)|}{P_{q_j}}
$$
满足独立模型启发 $\prod\delta_j>0$，**不**自动给出同步非空（需轨道相关）；但若 $G_q$ 对乘法平移足够对称，可用字符和估计同步密度——此属缺口 Trans-G2，本条只钉死**有限**判定形。

---

## L-Trans-7（条件式：无限提升 Trans-Lift$_\theta$）

### 假设 Trans-Lift$_\theta$（$\theta\in[0,1)$）

存在序列两两互素奇模 $(q_j)_{j\ge 1}$、好类族 $(G_{q_j})$、以及函数 $J(n)\to\infty$，使对充分大 $n$ 下列成立：

1. **同步局部.** 存在 $k=k(n)$ 使对一切 $j\le J(n)$，
$$
n-2^k\bmod q_j\ \in\ G_{q_j};
$$
2. **有效代表.** 令 $Q=Q_{J(n)}=\prod_{j\le J(n)}q_j$。存在 $m\in\mathcal{R}_{4,3,2}$ 使
$$
m\equiv n-2^k\pmod{Q},\qquad |n-2^k-m|\le Q^{\theta}.
$$

（当 $\theta=0$ 时要求 $m=n-2^k$，即已是整点可表——假设坍缩为目标。）

### 条件式结论

若 Trans-Lift$_\theta$ 对某 $\theta<1$ 成立，且沿该序列有 $Q_{J(n)}\to\infty$，则对充分大 $n$，一旦
$$
Q^{1-\theta}>1\quad\text{且}\quad |n-2^k-m|<Q
$$
（由 $|n-2^k-m|\le Q^{\theta}$、$Q\to\infty$ 对大 $n$ 自动），必有
$$
n-2^k=m\in\mathcal{R}_{4,3,2}.
$$
特别地 $n\in\mathcal{R}$。若对**一切**充分大 $n$ 皆然，则原猜想的充分大断言成立；若仅对 $n\notin\mathcal{F}_0$ 的补集，则得 $\mathcal{F}_0$ 有限的一条条件式路径。

**证明（形式蕴含）.** 同余 $n-2^k\equiv m\pmod{Q}$ 与 $|n-2^k-m|\le Q^{\theta}<Q$（大 $Q$）迫使差为 $0$。证毕。

**状态.** 蕴含箭头正确；前置 Trans-Lift$_\theta$ **未证**。硬度集中在：同步选取 $k$ 使差 $n-2^k$ 落入越来越细的 CRT 类，同时仍有 $\mathcal{R}_{4,3,2}$ 的代表元落在 $Q^{\theta}$ 邻域——这本质接近圆法主弧/有效代表，或 Diophantine 逼近式提升。

---

## L-Trans-8（条件式：瘦好类 + 轨道密度 $\Rightarrow$ 同步非空）

### 假设 Trans-Dense$_c$

存在绝对常数 $c>0$ 与奇模序列 $q_j$（$P_{q_j}=\mathrm{ord}_{q_j}(2)$），使对充分大 $n$ 与一切 $j\le J$（$J$ 可随 $n$ 增），
$$
\frac{|\mathcal{K}_{q_j}(n;G)|}{P_{q_j}}\ge c,
$$
且字符和型相关
$$
\sum_{\chi\bmod P^{(J)}}^\ast\ \prod_{j\le J}\Bigl(\frac{1}{P_{q_j}}\sum_{\kappa_j\in\mathcal{K}_{q_j}} \chi_j(\kappa_j)\Bigr)
$$
给出同步密度 $\ge c^{O(1)}>0$（精确式列为缺口 Trans-G2）。

### 条件式结论

Trans-Dense$_c$ $\Rightarrow$ L-Trans-6 的同步指数集对 $J$ 个模非空；再与 Trans-Lift$_\theta$ 拼合 $\Rightarrow$ 大 $n$ 可表。

**状态.** 结构接口；未验证任何具体 $G_q$（候选：$G_q=\{\,a:\mathfrak{S}_{\le P}(a)\ge(\log)^{-A}\,\}$ 对接 L-SSO / L-Floor；或主弧可达类对接 L-Thr）。

---

## L-Trans-9（已证对照：与 SSO / 2adic / Poly / 审查的正交性）

| 对象 | 说了什么 | 对「分模→乘积」 |
|------|----------|-----------------|
| 审查 §2 | 集合投影满一般假（$63/72/504$） | **禁止**投影推理 |
| L-Trans-1/4 | 变量 CRT + 固定 $k$ ⇒ $\mathcal{R}$ 任意模满 | **允许**；不经投影 |
| L-Poly-Res / L-Trans-5 | $I(q)$ 恒满 | 纯像集局部条件空 |
| L-SSO-3 / L-Trans-2 | $k\mapsto 2^k$ 乘法轨道 | **本路线动态核** |
| L-2adic-3/4 | $p=2$ 高位同步；禁类空 | 偶模侧无强制整窗 |
| L-Trans-7/8 | 瘦类 + 尺度提升 | 条件式；开放 |

**一句话.** 有限 CRT 拼在「同一 $2^k$ + 变量级像」下已闭；无限提升与瘦好类密度是缺口；路线存活于 P1 接口层，**不**替代伪随机 / 圆法。

---

## 缺口表（Trans-G）

| 代号 | 内容 | 若解决则得 |
|------|------|------------|
| Trans-G1 | 构造真瘦 $G_q\subsetneq I(q)$ 使「$G$-局部」对真实可表性有预测力（候选：截断 $\mathfrak{S}$、主弧类） | 局部筛子非空话 |
| Trans-G2 | 乘法轨道上多模同步密度的字符和 / 相关估计（Trans-Dense$_c$） | 有限→增长 $J$ 的同步 $k$ |
| Trans-G3 | Trans-Lift$_\theta$（$\theta<1$）的有效代表：$n-2^k$ 的 $\mathcal{R}_{4,3,2}$ 逼近 | 经 L-Trans-7 ⇒ 可表 |
| Trans-G4 | 将 $G_q$ 与 SS-Sync / L-Floor-7/8 / L-Thr-3 对接 | 条件式 E-kill 链 |
| Trans-G5 | 非互素模（如 $63,72$）的 $\gcd$ 兼容指数提升，不经假投影 | 骨架 A′ 的同步强化 |

**主缺口.** Trans-G1 + Trans-G3：无真瘦好类则局部条件空（L-Trans-5）；无尺度提升则 CRT 只给同余不给整点（L-Trans-3(C)）。二者皆开 ⇒ **不**得原猜想。

---

## 本轮结论

| 编号 | 状态 | 摘要 |
|------|------|------|
| L-Trans-1 | 已证 | 变量 CRT ≠ 投影 CRT；审查反例保留；$I(Q)$ 满 |
| L-Trans-2 | 已证 | 有限奇模 $2^k$ 指数 CRT 同步 |
| L-Trans-3 | 已证 | 局部像 + 同步 $k$ ⇒ 乘积模同步像（有界代表仅同余） |
| L-Trans-4 | 已证 | $\mathcal{R}$ 任意模满（固定 $k$+$I(M)$；含 $504$） |
| L-Trans-5 | 已证 | $G=I$ 时有限局部条件空；无强制整窗 |
| L-Trans-6 | 已证 | 真子集 $G$ 下有限同步判定形 |
| L-Trans-7 | 条件式 | Trans-Lift$_\theta$ ⇒ $n-2^k\in\mathcal{R}_{4,3,2}$ |
| L-Trans-8 | 条件式 | Trans-Dense$_c$ ⇒ 同步非空接口 |
| L-Trans-9 | 已证对照 | 与审查 / SSO / 2adic / Poly 正交结算 |

**对 P1 的判决.** 有限 CRT 拼引理（L-Trans-1…6）已入库，且正确使用了 $2^k$ 乘法动态；一般分模投影合并仍禁止。无限提升 Trans-Lift / Dense 开放，强度接近有效可表 / SS 阈值。原猜想与 E-kill-1 保持开放。
