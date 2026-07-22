# P09 对抗审查 · R13-Floor-Audit（奇异级数一致地板）

> 角色：对抗审查智能体。对象：L-Floor-1 / L-Floor-2（及同构依赖的 L-Floor-5/6 框架声称）。  
> 压力测试：在框架 L-SSO-2(A)+SS-1 下是否真有 $\inf_m\mathfrak{S}(m)\ge c>0$。  
> 判决档：`通过` / `需降级` / `否证`。不削弱骨架 Thm-A/A′/B、L07、L08、CS-弱、L-Ekill-SS-1；原猜想保持开放。

---

## 总表

| 条目 | 判决 | 一句话 |
|------|------|--------|
| L-Floor-1（$\inf_m\mathfrak{S}\ge c_{\mathfrak{S}}>0$） | **否证（论证）+ 降级（陈述）** | SS-1 最坏积 $\to 0$；截断逃生依赖的 L-SSO-2(A) 对混合幂不成立 |
| L-Floor-2（窗 $\max\mathfrak{S}\gg 1$ / SSO-G4 闭合） | **否证（论证）+ 降级** | 全依赖 L-Floor-1；SSO-G4 **未**被本框架闭合 |
| L-Floor-5/6（同假设下的窗平均 $\gg 1$） | **需降级** | 同一 $P_\ast$ 来自 SSO-2(A)；平均形可另证，但现证同构失效 |
| L-SSO-2(A)（$13/12>1\Rightarrow$ 一致绝对收敛积尾） | **否证（框架声称）** | Weyl 只给 $|A(q)|\ll q^{-1/12+\varepsilon}$，$\sum|A|$ 发散 |
| L-Floor-7/8（条件式备份） | **通过**（定位） | 恰为正确的 SSO-G4 替代路径；应升为主路而非备份 |
| 「绝对收敛 + 每因子 $\ge 1-\varepsilon$」用于 $x^4+y^3+z^2$ | **否证** | 不由 $\sum 1/\deg>1$ 推出；需 Tail-Weil 级 $|\sigma_p-1|\ll p^{-1-\delta}$ |

本轮对 L-Floor-1/2 的**证明链**达到 `否证`；对「是否存在绝对 $c_{\mathfrak{S}}>0$」本身在 Tail-Weil 下可条件式复活，故陈述档记为 **降级为条件式**，而非几何事实的无条件否定。

---

## 0. 指控句与审查标准

**被审指控（L-Floor-1/2）.**  
在 L-SSO-2(A)+L-Ekill-SS-1 下，
$$
\inf_{m\in\mathbb{Z}}\mathfrak{S}(m)\ge c_{\mathfrak{S}}>0,
$$
从而对一切 $n\ge 3$，
$$
\max_{k\le K}\mathfrak{S}(n-2^k)\ge c_{\mathfrak{S}}\gg(\log n)^{-c},
$$
并据此宣称 **SSO-G4 / SS-Sync 框架闭合**。

**审查标准.**

1. SS-1 的逐素下界 $\sigma_p\ge p^{-2}$ **单独**能否给出一致正地板。  
2. 奇异级数的 Euler 积结构下，个别 $m$ 是否可因多素同时偏小而使 $\mathfrak{S}(m)$ 任意小。  
3. 「绝对收敛 + 大素因子 $\ge 1-\varepsilon$」对混合幂 $x^4+y^3+z^2$ 是否由 $\sum_i 1/\deg_i=13/12>1$ 保证。  
4. 判决后须给出**可证替代引理**（平均 / 概率 / $(\log)^{-c}$ 型），不得只拆不建。

---

## 1. 检查点 A：$\prod_p p^{-2}$ 发散 —— SS-1 不能单独喂地板

### 1.1 无限积

由 SS-1，
$$
\sigma_p(m)\ge p^{-2}\qquad(\forall p,\,\forall m).
$$
若对**全体**素数取最坏下界，则
$$
\prod_p\sigma_p(m)
\ \ge\
\prod_p p^{-2}
$$
的右端在 Euler 积意义下
$$
\prod_p p^{-2}=\exp\Bigl(-2\sum_p\log p\Bigr)
$$
因 $\sum_p\log p=\infty$ 而 **发散到 $0$**。故
$$
\text{SS-1 单独}\quad\not\Longrightarrow\quad\inf_m\mathfrak{S}(m)>0.
$$

### 1.2 L-Floor-1 的「截断逃生」在写什么

L-Floor-1 并不取无限最坏积。它写：由 L-SSO-2(A) 取绝对 $P_\ast<\infty$ 使
$$
\sup_m\lvert T_{P_\ast}(m)-1\rvert\le\tfrac12,
$$
再仅对有限集 $\{p\le P_\ast\}$ 用 $\sigma_p\ge p^{-2}$，得
$$
\mathfrak{S}(m)
\ge
\tfrac12\exp\bigl(-2\,\theta(P_\ast)\bigr)=:c_{\mathfrak{S}}>0.
$$
**有限积** $\prod_{p\le P_\ast}p^{-2}$ 确为正。故本检查点的杀伤力不在有限段算术，而在：

> **若不存在与 $m$ 无关的 $P_\ast$ 使积尾一致靠近 $1$，则截断高度 $P(m)$ 被迫随 $m$ 趋于无穷，于是**
> $$
> \exp\bigl(-2\,\theta(P(m))\bigr)\to 0,
> $$
> **一致正地板崩塌。**

L-Floor-1 的全部载荷压在 L-SSO-2(A) 的一致性积尾上（见 §3）。SS-1 只负责有限段；**无限段的「假装已经 $=1$」不是 SS-1 给的。**

---

## 2. 检查点 B：$\sigma_p$ 均值 $\sim 1$，个别 $m$ 能否让 $\mathfrak{S}$ 任意小？

### 2.1 定义回顾

标准写法
$$
\mathfrak{S}(m)=\sum_{q=1}^\infty A(q,m)
=\prod_p\sigma_p(m)
$$
（后一式在 Euler 积收敛时）。单素因子均值
$$
\frac1p\sum_{r\bmod p}\sigma_p(r)\asymp 1
$$
（圆法正规化）**不**阻止点态左尾。

### 2.2 CRT 赤字机制

设存在 $c_0\in(0,1)$ 与无限素集 $\mathcal{P}_{\mathrm{bad}}$，使得每个 $p\in\mathcal{P}_{\mathrm{bad}}$ 皆有坏类
$$
B_p(c_0)=\{r:\sigma_p(r)\le c_0\}\ne\varnothing.
$$
（L-SSO-4/5 的 LS 叙事**预设**这类坏类在大素上存在且比例 $\le 1-\kappa$。）对任意 $Y$，取有限集
$$
\mathcal{P}_Y=\{p\in\mathcal{P}_{\mathrm{bad}}:p\le Y\},
$$
由中国剩余定理存在 $m_Y$ 使
$$
\forall p\in\mathcal{P}_Y,\qquad m_Y\bmod p\in B_p(c_0).
$$
于是
$$
\mathfrak{S}_{\le Y}(m_Y)
=\prod_{p\le Y}\sigma_p(m_Y)
\le
c_0^{\#\mathcal{P}_Y}\prod_{\substack{p\le Y\\p\notin\mathcal{P}_{\mathrm{bad}}}}C_\sigma.
$$
若 $\#\mathcal{P}_Y\to\infty$（$Y\to\infty$），则截断积可任意小。

### 2.3 与积尾的合取

- **若**再有一致积尾 $\sup_m|T_Y-1|\to 0$（$Y\to\infty$），则
  $$
  \mathfrak{S}(m_Y)=\mathfrak{S}_{\le Y}(m_Y)\,T_Y(m_Y)
  $$
  可任意小，故
  $$
  \inf_m\mathfrak{S}(m)=0.
  $$
  此时 L-Floor-1 的**结论句**与「一致积尾 + 无限坏类」**逻辑不相容**。  
- **若**大素上 $|\sigma_p-1|\ll p^{-1-\delta}$（Tail-Weil）使固定 $c_0<1$ 的坏类对 $p\gg 1$ **空集**，则 CRT 只能打有限素，结论句可复活——但这已超出 SS-1+SSO-2(A)，进入 L-SSO-2(B)。

### 2.4 Lang–Weil 级误差下的启发式否证

对仿射曲面 $x^4+y^3+z^2=m$，Lang–Weil 型点计至多给
$$
\lvert\sigma_p(m)-1\rvert\ll p^{-1/2}
$$
（忽略奇异纤维的有限例外）。级数 $\sum_p p^{-1/2}$ **发散**，且对每个有限 $P$，
$$
\sum_{p>P}p^{-1/2}=\infty.
$$
若存在随 $m$ 可选的负号次项（CRT 选取使多素同时偏小一侧），则
$$
\prod_{P<p\le Z}\sigma_p(m)
\le
\exp\Bigl(-c\sum_{P<p\le Z}p^{-1/2}\Bigr)
$$
可随 $Z\to\infty$ 落到任意小。启发式：
$$
\inf_m\mathfrak{S}(m)=0
$$
在「仅 $p^{-1/2}$ 级一致误差、无 $p^{-1-\delta}$」的世界里是**预期真相**，与 L-Floor-1 的无条件正地板相反。

**小结.** 均值 $\sim 1$ **不**给出一致正下界；多素同时偏小是奇异级数点态小的标准机制。L-Floor-1 若要挡此机制，必须消灭「大素上的固定比例坏类」，即本质动用 Tail-Weil，而非 SS-1。

---

## 3. 检查点 C：绝对收敛 + 每因子 $\ge 1-\varepsilon$ 对混合幂成立吗？

### 3.1 L-SSO-2(A) 的声称

L-SSO-2(A) 写：由 $\sum 1/\deg=13/12>1$，奇异级数 Euler 积对 $m$ **一致绝对收敛**，故
$$
\exists P_\varepsilon<\infty:\quad
\sup_m\lvert\log T_{P_\varepsilon}(m)\rvert\le\varepsilon.
$$

### 3.2 Weyl / 完整和给出的真实指数

对 $f=x^4+y^3+z^2$，
$$
A(q,m)=q^{-3}\sum_{\substack{a=1\\(a,q)=1}}^q S_4\Bigl(\frac aq\Bigr)S_3\Bigl(\frac aq\Bigr)S_2\Bigl(\frac aq\Bigr)e\Bigl(-\frac{am}q\Bigr).
$$
Hua–Weyl：
$$
\bigl|S_k(a/q)\bigr|\ll_\varepsilon q^{1-1/k+\varepsilon},
$$
故
$$
|A(q,m)|
\ll_\varepsilon
q^{1-\sum_i 1/k_i+\varepsilon}
=q^{-1/12+\varepsilon}.
$$
于是
$$
\sum_{q=1}^\infty|A(q,m)|
$$
与 $\sum q^{-1/12}$ 同级，**发散**。  
标准事实：$\sum 1/k_i>1$ 控制的是主弧维数 / 期望表示阶 $m^{1/12}$，**不是** $\sum_q|A(q)|<\infty$。绝对收敛通常需要更强节省（粗略地 $|A(q)|\ll q^{-1-\delta}$，对应 $\sum 1/k_i>2$ 的 Weyl 形，或 Deligne 级完整和）。

### 3.3 Euler 积侧

即便改写 $\sigma_p=1+O(p^{-1/12+\varepsilon})$，仍有 $\sum_p p^{-1/12}=\infty$，Weierstrass 估计
$$
\lvert\log T_P\rvert
\le\sum_{p>P}\lvert\log\sigma_p\rvert
$$
对每个有限 $P$ 给出 $\infty$，**不能**推出 $\sup_m|T_P-1|\to 0$。  
「大素上 $\sigma_p(m)\ge 1-\varepsilon$ 对一切 $m$」需要
$$
\sup_m\lvert\sigma_p(m)-1\rvert\to 0\quad(p\to\infty),
$$
这正是 **Tail-Weil / L-SSO-2(B)**（$|\sigma_p-1|\ll p^{-1-\delta}$），仓库已标为**缺口**，且明文写：SS-1 **不**推出该式。

### 3.4 判决

| 声称 | 对 $x^4+y^3+z^2$ |
|------|------------------|
| $13/12>1\Rightarrow\sum_q|A(q)|<\infty$ | **假** |
| $13/12>1\Rightarrow$ 一致 $|T_P-1|\le\varepsilon$ | **未证；现有 Weyl 框架下不可得** |
| 大素 $\sigma_p\ge 1-\varepsilon$（一致） | **仅在 Tail-Weil 下；非 SSO-2(A)** |

故 L-Floor-1 前提中的「框架绝对收敛」对混合幂 **不成立**（作为已证框架）。检查点 C：**否证**。

---

## 4. 合取：L-Floor-1/2 证明链的崩点

```
SS-1: σ_p ≥ p^{-2}
        │
        ├─(无限最坏积)─→ 0          【不能给地板】
        │
        └─(有限截断 ≤P_*)─→ e^{-2θ(P_*)} > 0
                 │
                 └─ 需要 sup_m |T_{P_*}-1|≤1/2
                           │
                           └─ 诉诸 L-SSO-2(A)
                                     │
                                     └─ 13/12>1 ⇒ 绝对收敛？ 【否证】
```

L-Floor-2 是 L-Floor-1 的窗上特化；SSO-G4「框架闭合」标签随 L-Floor-1 一并失效。  
L-Floor-5/6 使用**同一** $P_\ast=P_{1/2}$ 与同一积尾，现证同构失效；其「几何平均 $\Rightarrow$max」的形式推理可保留到另证平均下界之后。

---

## 5. 正确的可证替代引理

下列替代不声称 $\inf_m\mathfrak{S}\ge c>0$，但足够服务 SS-Sync / SSO-G4 的**可用**载荷，并与 L-Thr-3 的 $(\log)^{-A}$ 门槛对齐。

### 5.1 替代 A（平均对数下界）— 建议标号 L-Floor-1♭

**假设.** 对一切充分大素数 $p$，
$$
\frac1p\sum_{r=0}^{p-1}\log\sigma_p(r)
\ge -C\frac{\log p}{p}
$$
（由局部密度展开 / 完整和均值；弱于点态 Tail-Weil）。则存在绝对 $C_0$ 使
$$
\frac1X\sum_{m\le X}\log\mathfrak{S}(m)
\ge -C_0\log\log\log X
\quad(X\ge X_0),
$$
特别地几何平均
$$
\exp\Bigl(\frac1X\sum_{m\le X}\log\mathfrak{S}(m)\Bigr)
\gg(\log\log X)^{-C_0}.
$$
（若均值 $\ge -C p^{-1-\delta}$，则右端可加强为 $\gg 1$。）

**与旧 L-Floor-1 的差别.** 控制的是 $\mathbb{E}_m\log\mathfrak{S}$，**不是** $\inf_m\mathfrak{S}$。

### 5.2 替代 B（概率型 $(\log)^{-c}$ 地板）— 建议标号 L-Floor-2♭

**假设.** 同 5.1，并设 $\mathrm{Var}_p(\log\sigma_p)\ll(\log p)^2/p$（或更弱的二矩可和）。则存在 $c,\delta>0$ 使
$$
\frac1X\#\bigl\{m\le X:\mathfrak{S}(m)\ge(\log X)^{-c}\bigr\}
\ge 1-O\bigl((\log X)^{-\delta}\bigr).
$$
等价叙述：$\mathfrak{S}(m)<(\log X)^{-c}$ 的 $m$ 构成薄集。

**窗上推论（仍需轨道输入）.** 若再有二进窗对乘性函数的准随机采样（L-SSO-3 + Equi 型），则
$$
\max_{k\le K}\mathfrak{S}(n-2^k)\gg(\log n)^{-c}
$$
以 $1-o(1)$ 的 $n$-比例成立；要**一切** $n$，需 L-Floor-8 的 Soft-AP / LS，或更强的均匀分布。

### 5.3 替代 C（已有条件式，升格为主路）

| 编号 | 结论 | 前置 |
|------|------|------|
| L-Floor-7 | $\mathcal{A}_n(\log\mathfrak{S})\ge -C$ 或 $-C\log\log\log n$；故 $\max_k\mathfrak{S}\gg(\log\log n)^{-C}$ | ML$_\delta$+Equi$_2$+Tail-Weil |
| L-Floor-8 | $\max_k\mathfrak{S}\gg(\log n)^{-A}$ | LS+Soft-AP+L-SSO-4 |

**R13 指令.** SSO-G4 的开放状态改回：**仅当 L-Floor-7 或 L-Floor-8 的前置被核验时闭合**；删除「SSO-2(A)+SS-1 已闭合 G4」的宣传。

### 5.4 条件式复活的一致地板（可选，L-Floor-1♯）

**假设 Tail-Weil**（L-SSO-2(B)）：$|\sigma_p(m)-1|\le C p^{-1-\delta}$ 对一切 $m$ 与 $p\notin\mathfrak{B}$。则存在 $P_\ast$ 使 $p>P_\ast\Rightarrow\sigma_p(m)\ge 1/2$，再与 SS-1 合取得
$$
\inf_m\mathfrak{S}(m)\ge c_{\mathfrak{S}}(C,\delta)>0.
$$
此为 **L-Floor-1 的合法条件化**；不得再标「仅 SSO-2(A)+SS-1 已证」。

---

## 6. 状态改写指令（入库）

| 条目 | 旧状态 | 新状态 |
|------|--------|--------|
| L-Floor-1 | 已证（框架） | **否证（原证）/ 条件式（需 Tail-Weil）** |
| L-Floor-2 | 已证（框架）；SSO-G4 闭合 | **否证（原证）/ 降级**；SSO-G4 **未闭合** |
| L-Floor-5/6 | 已证（平均） | **需降级**：现证失效；平均形改挂 ML 或 5.1 |
| L-Floor-7/8 | 条件式备份 | **条件式主路**（G4 唯一存活路径） |
| L-SSO-2(A) | 已证（框架） | **降级**：不得由 $13/12>1$ 宣称一致绝对收敛积尾 |
| SSO-G4 / SS-Sync | 框架已证 | **开放**（待 Floor-7/8 或 1♯） |

**明确保留.** L-Ekill-SS-1（$\sigma_p\ge p^{-2}$）本身未受本轮否证；L-SSO-1/3/4 的轨道/周期/单素坏弧控制保留。

---

## 7. 总判决

**否证或降级.**

1. **论证否证：** L-Floor-1/2 在「L-SSO-2(A)+SS-1」下的证明链不成立——SS-1 的无限最坏积发散到 0，截断所依的一致绝对收敛积尾不能由 $13/12>1$ 得到。  
2. **陈述降级：** $\inf_m\mathfrak{S}\ge c>0$ 至多作为 **Tail-Weil 条件式**（L-Floor-1♯）存活；SSO-G4 回到 L-Floor-7/8。  
3. **可证替代：** 平均对数下界（5.1）、概率型 $(\log)^{-c}$ 地板（5.2）、以及已有条件式 L-Floor-7/8。  
4. **混合幂特判：** 「绝对收敛 + 每因子 $\ge 1-\varepsilon$」对 $x^4+y^3+z^2$ **不**由圆法维数条件自动成立。

原猜想、$\mathrm{H}_{\mathrm{thr}}$、E-kill 保持开放；本轮不制造新的「已证充分大」。
