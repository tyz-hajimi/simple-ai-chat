# L-Pack：三邻窗 / 倍窗装填与条件式 Roth 冲突（路线 R8-Triple-Window-Pack）

> 路线 **R8-Triple-Window-Pack**（P09 攻关轮次 8，服务 **P1 = E-kill-1**）。  
> 强化既有 Pack / A2 / AE 的「窗点相关」思路，但给出**新**的多窗装填引理：考察邻窗族 $\{W(N),W(N+1),W(N+2)\}$ 或倍窗 $\{W(N),W(2N)\}$，利用
> $$
> (N-2^k)-(N'-2^{k'})\in\text{小集合}
> $$
> 的加性关系，把「$\mathcal{F}_0$ 无限」升级为「$E$ 在多个平移窗上同时厚」。  
> **必须避开 L08**：抽象密度零集可把整窗稀疏散植（无邻窗、无倍窗联动），故与 Roth 的冲突**仅**在混合幂结构假设或显式联动条件下成立。  
> **不**声称原猜想已证；含「假设 Pack-† / Mix-†」的条目为条件式。

---

## 0. 符号与对象

沿用：
$$
\mathcal{R}_{4,3,2}=\{x^4+y^3+z^2:x,y,z\in\mathbb{N}_0\},
\qquad
E=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2},
$$
$$
W(N)=\{N-2^k:1\le k\le K(N)\},\qquad
K(N)=\lfloor\log_2(N-1)\rfloor,
$$
$$
\mathcal{F}_0=\{N\ge 2:W(N)\subseteq E\}.
$$
对 $N\ge 3$ 简写 $K=K(N)$。窗占据
$$
\rho_E(N;K)=\#\{1\le k\le K:N-2^k\in E\}.
$$
（整窗 $\Leftrightarrow\rho_E(N;K)=K$。）

对固定平移 $h\in\mathbb{Z}$ 与尺度 $K$，定义**差型小集合**
$$
\mathcal{S}(h;K)=\bigl\{2^{\ell}-2^{k}-h:1\le k,\ell\le K\bigr\}.
$$
显然 $|\mathcal{S}(h;K)|\le K^2$，且每个元素有刚性二进形状 $2^{\min(k,\ell)}(2^{|k-\ell|}\mathrm{sgn}-1)-h$。

**历史对照（非本文件新证）.** 单窗 $\Delta_K$-相关装填已见于 L-Ekill-A2-1 / L-AE-1（下文称 **Pack-单窗层**）。本文件从 **L-Pack-3** 起为三邻 / 倍窗新层。

---

## L-Pack-3（已证：邻窗差的加性恒等式与几乎不交）

设整数 $N\ge 4$、$h\in\{1,2\}$，并设 $K=\lfloor\log_2(N-1)\rfloor$、$K_h=\lfloor\log_2(N+h-1)\rfloor$。则对一切 $1\le k\le K$、$1\le\ell\le K_h$，
$$
(N-2^k)-\bigl((N+h)-2^{\ell}\bigr)=2^{\ell}-2^{k}-h\in\mathcal{S}(h;\max(K,K_h)).
$$
进而：

1. **$h=1$：** $W(N)\cap W(N+1)=\varnothing$。  
   （若 $N-2^k=(N+1)-2^{\ell}$ 则 $2^{\ell}-2^{k}=1$；对 $k,\ell\ge 1$ 无非负整数解。）

2. **$h=2$：** $W(N)\cap W(N+2)$ 至多一点，且仅当 $\{2,1\}\subset\{1,\ldots,K\}\cap\{1,\ldots,K_2\}$ 时可能取到
   $$
   N-2=N+2-4=(N+2)-2^{2}.
   $$
   （方程 $2^{\ell}-2^{k}=2$ 在 $k,\ell\ge 1$ 上仅解 $(\ell,k)=(2,1)$。）

3. 若 $2^{K}<N\le 2^{K+1}-2$（保证 $K(N)=K(N+1)=K(N+2)=K$），则
   $$
   \bigl|W(N)\cup W(N+1)\cup W(N+2)\bigr|
   \ge 3K-1.
   $$

**证明.** 恒等式为直接展开。(1)(2) 由二进差分方程的唯一性。(3) 由 (1)(2)：三窗两两交至多贡献一次重叠，故
$$
|W(N)|+|W(N+1)|+|W(N+2)|-|W(N)\cap W(N+2)|
\ge 3K-1.
$$
证毕。

**解读.** 邻窗几乎不交 ⇒ 多点落入 $\mathcal{F}_0$ 时，$E$ 必须在长度 $\asymp N$ 的区间上同时装下 $\asymp(\#\text{邻窗})\,K$ 个例外点——这是「多平移窗同时厚」的组合核。

---

## L-Pack-4（已证：倍窗 $N$ 与 $2N$ 的加性关系）

设 $N\ge 3$，$K=K(N)$、$K_2=K(2N)$（故 $K_2\in\{K,K+1\}$）。对 $1\le k\le K$、$1\le\ell\le K_2$，
$$
\bigl(2N-2^{\ell}\bigr)-\bigl(N-2^{k}\bigr)=N+2^{k}-2^{\ell}.
$$
记倍窗差型集合
$$
\mathcal{S}_{\times 2}(N;K)=\bigl\{N+2^{k}-2^{\ell}:1\le k\le K,\ 1\le\ell\le K_2\bigr\}.
$$
则：

1. $|\mathcal{S}_{\times 2}(N;K)|\le K\cdot K_2\ll K^2$。  
2. 若 $N\in\mathcal{F}_0$ 且 $2N\in\mathcal{F}_0$，则 $W(N)\cup W(2N)\subset E$，且
   $$
   \bigl|W(N)\cup W(2N)\bigr|\ge K+K_2-r_{\cap},
   $$
   其中重叠数
   $$
   r_{\cap}=\#\bigl\{(k,\ell):N-2^{k}=2N-2^{\ell}\bigr\}=\#\bigl\{(k,\ell):2^{\ell}-2^{k}=N\bigr\}.
   $$
   对每个固定 $k$，方程 $2^{\ell}=N+2^{k}$ 至多一解，故 $r_{\cap}\le K$。特别地
   $$
   \bigl|W(N)\cup W(2N)\bigr|\ge K_2\ge K.
   $$
   若再设 $N$ 非二进近邻（$N+2^{k}$ 对一切 $k\le K$ 皆非纯幂 $2^{\ell}$），则 $r_{\cap}=0$，并集基数 $=K+K_2$。

**证明.** 恒等式直接；(2) 由容斥与「固定 $k$ 至多一个 $\ell$」。证毕。

**注.** 倍窗把「同一尺度的邻移」换成「尺度翻倍的轨道」；L08 型稀疏散植通常沿超指数中心 $N_j=2^{2^j}+1$，使 $2N_j$ 远离开下一中心，从而**不**触发倍窗双整窗。

---

## L-Pack-5（已证：多窗装填 $\Rightarrow$ 局部厚度下界）

### （A）三邻整窗

设 $2^{K}<N\le 2^{K+1}-2$ 且 $\{N,N+1,N+2\}\subset\mathcal{F}_0$。令
$$
I_N^{\mathrm{tr}}:=[N-2^{K},\,N+2]\cap\mathbb{Z}.
$$
则
$$
\bigl|E\cap I_N^{\mathrm{tr}}\bigr|
\ge
\bigl|W(N)\cup W(N+1)\cup W(N+2)\bigr|
\ge 3K-1.
$$

### （B）双邻整窗

若仅 $|\{N,N+1,N+2\}\cap\mathcal{F}_0|\ge 2$，不妨 $\{N,N+h\}\subset\mathcal{F}_0$（$h\in\{1,2\}$），则在
$$
I_N^{(h)}:=[N-2^{K},\,N+h]
$$
上仍有
$$
\bigl|E\cap I_N^{(h)}\bigr|\ge 2K-1_{\{h=2\}}.
$$

### （C）倍窗双整窗

若 $\{N,2N\}\subset\mathcal{F}_0$，则在 $J_N:=[N-2^{K},\,2N]\cap\mathbb{Z}$ 上
$$
\bigl|E\cap J_N\bigr|\ge\bigl|W(N)\cup W(2N)\bigr|\ge K
$$
（L-Pack-4）；无纯幂重叠时 $\ge 2K-O(1)$。

**证明.** 窗点均落入所述区间（因 $1\le 2^{k}\le 2^{K}<N$ 或对 $2N$ 同理），再引 L-Pack-3/4。证毕。

**一句话.** $\mathcal{F}_0$ 的邻簇 / 倍簇强制 $E$ 在对应平移窗并集上达到 $\asymp K$ 或 $\asymp 3K$ 的局部厚度。

---

## L-Pack-6（已证：双计数 — 装填簇对全局 $|E|$ 的贡献）

对 $X\ge 4$ 定义三邻整窗簇计数
$$
\mathcal{T}(X)=\#\bigl\{N\le X:2^{K(N)}<N\le 2^{K(N)+1}-2,\ \{N,N+1,N+2\}\subset\mathcal{F}_0\bigr\},
$$
以及倍窗簇计数
$$
\mathcal{D}(X)=\#\bigl\{N\le X:\{N,2N\}\subset\mathcal{F}_0\bigr\}.
$$
则存在绝对常数 $c>0$ 使
$$
\bigl|E\cap[1,2X]\bigr|
\ge
c\cdot\frac{1}{\log X}\Bigl(
\sum_{\substack{N\le X\\\{N,N+1,N+2\}\subset\mathcal{F}_0}}K(N)
+\sum_{\substack{N\le X\\\{N,2N\}\subset\mathcal{F}_0}}K(N)
\Bigr).
$$
特别地，若 $\mathcal{T}(X)\ge 1$ 取到某个 $N\asymp X$，则已有 $|E\cap[1,2X]|\ge 3K(N)-1\gg\log X$（局部结论）；若进一步
$$
\sum_{\substack{N\le X\\ N\in\mathcal{T}\text{-簇}}}K(N)\gg\frac{X}{(\log X)^{\kappa}}
$$
则
$$
\bigl|E\cap[1,2X]\bigr|\gg\frac{X}{(\log X)^{\kappa+1}}.
$$

**证明.** 每个三邻簇贡献 $\ge 3K-1$ 个（带重数的）例外点落在 $\bigcup W$。每个定点 $m\in E$ 至多属于 $O(K_{\max})$ 个窗 $W(N)$（$N=m+2^{k}$，$k\le K(N)\ll\log X$），故除以 $O(\log X)$ 即得去重下界。倍窗簇同理。证毕。

**定位.** 本条是纯组合双计数；**尚未**与 Roth 冲突——冲突需要簇和式足够大（见 L-Pack-7），而 L08 恰使簇和式 $\ll(\log X)^{O(1)}$。

---

## L-Pack-7（条件式：Mix-Link + Clash$_{*}$ + Roth $\Rightarrow\mathcal{F}_0$ 有限；显式避开 L08）

对数级多窗加厚（L-Pack-5/6）**单独不破** Roth：$|E|$ 下界至多 $\asymp\#(\text{簇})\cdot\log X$，而 L08 簇数 $O(\log\log X)$。与 Roth 冲突必须吃进混合幂结构。采用下列假设。

### 假设 Pack-Mix-Link$_{c}$（混合幂联动）

存在 $c\in(0,1]$、$N_0$，使对一切 $N\ge N_0$，若 $N\in\mathcal{F}_0$，则下列至少一款成立：

- **（邻移）** $\max\{\rho_E(N+1;K),\rho_E(N+2;K),\rho_E(N-1;K)\}\ge c\,K$；或  
- **（倍移）** $\rho_E(2N;K(2N))\ge c\,K(2N)$，或（$N$ 偶数时）$\rho_E(N/2;K(N/2))\ge c\,K(N/2)$。

（意图：真实 $E=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2}$ 因混合幂差集 / 局部可表，不能把整窗孤立散植；抽象 $E$ 不在本假设内。）

### 假设 Pack-Clash$_{*}$（二选一，均排除 L08）

- **Pack-Power-Cover$_{β}$：** 存在 $\beta<1/20$，使无穷多 $N\in\mathcal{F}_0$ 在 Pack-Mix-Link 迭代下产生近整窗链，满足
  $$
  \bigl|E\cap[1,2N]\bigr|\gg\frac{N}{(\log N)^{\beta}}.
  $$
  （典型实现：联动沿邻移生成长度 $\gg N/(\log N)^{\beta}$ 的区间，且该区间上 $E$ 密度 $\gg 1$。）  
- **Pack-AP-Link：** 存在 $q\ll(\log X)^{C}$（某绝对 $C<1/20$ 足够小，或 $q$ 有界）与剩余 $a$，使
  $$
  \#\bigl(\mathcal{F}_0\cap(a+q\mathbb{Z})\cap[1,X]\bigr)\gg\frac{X}{q}
  $$
  对无穷多 $X$ 成立。

### 结论（条件式）

在骨架 Roth 界 $|E\cap[1,X]|\ll X/(\log X)^{1/20}$ 下：
$$
\mathrm{Pack\text{-}Mix\text{-}Link}_{c}+\mathrm{Pack\text{-}Clash}_{*}
\implies
\mathcal{F}_0\text{ 有限}.
$$

**证明（Power-Cover 枝）.** 假设 $\mathcal{F}_0$ 无限且 Pack-Power-Cover$_{β}$ 给出无穷多 $N$ 使 $|E\cap[1,2N]|\gg N/(\log N)^{\beta}$。取 $\beta<1/20$，则对大 $N$ 与 Roth 上界 $O\!\bigl(N/(\log N)^{1/20}\bigr)$ 矛盾。故 $\mathcal{F}_0$ 有限。

**证明（AP-Link 枝）.** 设 $a+q\mathbb{Z}$ 上有 $\gg X/q$ 个 $\mathcal{F}_0$ 点，$q\ll(\log X)^{C}$。取同尺度内间距 $\ge 2^{K/2}$ 的稀疏子列（重叠损失 $O(1)$），由 L-Pack-3 与 Mix-Link 第二窗，L-Pack-6 型双计数给出
$$
\bigl|E\cap[1,2X]\bigr|
\gg
\frac{X}{q\,(\log X)^{O(1)}}.
$$
当 $C$ 与隐含对数幂之和 $<1/20$ 时破 Roth。证毕。

**注.** 若仅有 Mix-Link 而无 Clash$_{*}$，则每个整窗只强迫 $O(K)$ 额外例外点，全局仍可与 Roth 及 L08 相容。Clash$_{*}$ 要求**多项式级**（或 $X/(\log)^{\beta}$，$\beta<1/20$）加厚，是相对 L08 的本质增量。

---

## L-Pack-8（已证对照：L08 抽象反例恰好打破联动）

L08 构造（审查 T1）：取 $N_j=2^{2^j}+1$，令 $E=\bigcup_j W(N_j)$。则：

1. $|E\cap[1,X]|=O(\log X)=o(X)$，与任意 Roth 型上界相容。  
2. $\mathcal{F}_0$ 无限（每个 $N_j\in\mathcal{F}_0$）。  
3. **无三邻簇：** 对充分大 $j$，$N_j+1,N_j+2\notin\mathcal{F}_0$（其窗点大量落在 $E^{c}$，因下一中心超指数远离）。  
4. **无倍窗簇：** $2N_j$ 的窗不落在 $\bigcup_i W(N_i)$ 内（尺度错位）。  
5. 故 Pack-Mix-Link$_{c}$ 与 Pack-Clash$_{*}$ **均失败**；L-Pack-7 的前提不满足。

**一句话.** 「$\mathcal{F}_0$ 无限 $\Rightarrow$ 多窗同时厚 $\Rightarrow$ 破 Roth」对抽象 $E$ 为假；只对带混合幂联动 / 覆盖型 Clash 的 $E$ 可条件式成立。本路线**不**把 L08 误杀。

---

## L-Pack-9（缺口登记 Pack-G1–G4）

| 编号 | 内容 | 状态 |
|------|------|------|
| **Pack-G1** | **Pack-Mix-Link$_{c}$.** 真实 $E=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2}$ 上整窗是否强制邻窗或倍窗高占据。需混合幂差分 / 圆法局部结构；不能从密度推出（L08）。 | 未证 |
| **Pack-G2** | **Pack-Clash$_{*}$.** Power-Cover$_{β}$（$|E|\gg N/(\log N)^{\beta}$，$\beta<1/20$）或 AP-Link（失败集在短模 AP 上正密度）。强度接近或超过 E-kill 本体。 | 未证 |
| **Pack-G3** | 联动窗与主窗在全局双计数中的重叠控制（何时除以 $\log X$ 可升级为 $X^{\theta}$）。 | 未证 |
| **Pack-G4** | 与 AE-Corr / Diff-Out / FW-Unif 的同构度：多窗装填是否给出**新**的可证输入，或仅改写同一伪随机核。 | 对照中 |

**不可写为定理的部分.** 「仅 $\mathcal{F}_0$ 无限 + Roth $\Rightarrow$ 矛盾」；「仅邻窗组合装填 $\Rightarrow$ E-kill」。二者均被 L-Pack-8 / L08 阻断。

---

## 结算

| 编号 | 状态 | 摘要 |
|------|------|------|
| L-Pack-3 | 已证 | 邻窗差 $\in\mathcal{S}(h;K)$；三窗几乎不交，$|{\bigcup}|\ge 3K-1$ |
| L-Pack-4 | 已证 | 倍窗差 $=N+2^{k}-2^{\ell}$；双整窗并集下界 |
| L-Pack-5 | 已证 | 邻簇 / 倍簇 $\Rightarrow$ 局部 $|E\cap I|\gg K$ 或 $\gg 3K$ |
| L-Pack-6 | 已证 | 簇和式 $\to$ 全局 $|E|$ 双计数下界 |
| L-Pack-7 | 条件式 | Mix-Link + Clash$_{*}$ + Roth $\Rightarrow\mathcal{F}_0$ 有限 |
| L-Pack-8 | 已证对照 | L08 无邻/倍簇，恰破联动；路线避开抽象反例 |
| L-Pack-9 | 缺口 | Pack-G1–G4 |

**本轮结论.** 新引理层 L-Pack-3…6 把「多平移窗同时厚」写成可引用组合事实；与 Roth 的冲突必须经 Pack-Mix-Link / Pack-Clash$_{*}$ 吃进混合幂结构（L-Pack-7），并由 L-Pack-8 显式声明 L08 不在杀伤范围内。E-kill-1 仍开放；原猜想保持开放。
