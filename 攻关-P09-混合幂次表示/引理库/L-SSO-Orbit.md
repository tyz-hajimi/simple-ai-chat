# L-SSO：奇异级数二进轨道（R2-SS-Orbit）

> 服务 P1 / SS-Sync 局部。不改写、不重复 L-Ekill-SS-1 的 $\sigma_p\ge p^{-2}$ 证明；下文可引用该下界。  
> 窗口 $W(n)=\{n-2^k:1\le k\le K\}$，$K=\lfloor\log_2(n-1)\rfloor$。  
> 状态严格区分：**已证** / **条件式** / **缺口**。原猜想与 SS-Sync 本身均未证。

---

## 记号

对 $f=x^4+y^3+z^2$，设局部密度
$$
\sigma_p(m)=\lim_{h\to\infty}p^{-2h}\,\#\{(x,y,z)\bmod p^h:x^4+y^3+z^2\equiv m\pmod{p^h}\}
$$
（极限存在时；本文件在「奇异级数按 Euler 积定义」的标准圆法框架下工作）。奇异级数
$$
\mathfrak{S}(m)=\prod_p\sigma_p(m).
$$
对截断高度 $P\ge 3$，写
$$
\mathfrak{S}_{\le P}(m)=\prod_{p\le P}\sigma_p(m),\qquad
T_P(m)=\prod_{p>P}\sigma_p(m),
$$
从而 $\mathfrak{S}(m)=\mathfrak{S}_{\le P}(m)\,T_P(m)$（积收敛时）。

称素数 $p=2$ 及使 Hensel 提升阶或奇异纤维结构需抬高幂次的有限集为**坏模素**；下文「去掉有限坏模」指固定有限集 $\mathfrak{B}$（至少含 $2$，可含 $3$）后，仅对 $p\notin\mathfrak{B}$ 使用模 $p$（或固定幂 $p^{e_p}$，$e_p$ 仅依赖次数）的局部因子。

---

## L-SSO-1（已证）— 有限截断的严格周期性

固定 $P\ge 3$ 与各 $p\le P$ 的提升阶 $e_p\ge 1$（$e_p$ 仅依赖 $f$ 的次数与 $p$，与 $m$ 无关；坏素 $p\in\mathfrak{B}$ 取充分大但有限的 $e_p$）。令
$$
M_P=\prod_{p\le P}p^{e_p}.
$$
则映射 $m\mapsto\mathfrak{S}_{\le P}(m)$ 仅依赖 $m\bmod M_P$，故在 $\mathbb{Z}$ 上以 $M_P$ 为周期：
$$
m\equiv m'\pmod{M_P}\implies\mathfrak{S}_{\le P}(m)=\mathfrak{S}_{\le P}(m').
$$

**证明.** 对每个 $p\le P$，局部计数模 $p^{e_p}$（及更高幂的稳定化）完全由 $m\bmod p^{e_p}$ 决定，故 $\sigma_p(m)$ 亦然。有限积对模 $M_P$ 的中国剩余类恒定。证毕。

**备注.** 此即「去掉积尾后」的 Bohr / 周期几乎周期性的精确有限形式；不涉及 $T_P$。

---

## L-SSO-2（已证 + 标准局部尾假设下的定量）— Euler 积尾控制

### （A）定性控制（已证，在绝对收敛框架下）

设奇异级数 Euler 积对所有 $m$ **绝对收敛**（三项混合幂 $\sum 1/\deg=13/12>1$ 的标准圆法设定），即
$$
\sum_p\lvert\sigma_p(m)-1\rvert<\infty
$$
对每个 $m$ 成立，且上界对 $m$ 一致（由局部因子的次数型估计保证）。则对任意 $\varepsilon>0$ 存在 $P_\varepsilon$（不依赖 $m$）使
$$
\sup_{m\in\mathbb{Z}}\lvert\log T_{P_\varepsilon}(m)\rvert\le\varepsilon,
$$
从而
$$
\sup_m\lvert T_{P_\varepsilon}(m)-1\rvert\le 2\varepsilon\quad(\varepsilon\le 1/2).
$$
故 $\mathfrak{S}(m)$ 在去掉有限坏模（并截断至 $P_\varepsilon$）后，由周期函数 $\mathfrak{S}_{\le P_\varepsilon}$ 在相对误差 $O(\varepsilon)$ 内决定。

**证明.** 绝对收敛 $\Rightarrow\sum_p\sup_m\lvert\log\sigma_p(m)\rvert<\infty$（对充分大 $p$ 用 $\lvert\log\sigma_p\rvert\asymp\lvert\sigma_p-1\rvert$）。尾和 $\sum_{p>P}\sup_m\lvert\log\sigma_p(m)\rvert\to 0$（$P\to\infty$）。证毕。

### （B）可引用的幂次尾（条件式：Weil / 点计）

**假设 Tail-Weil.** 存在绝对常数 $C,\delta>0$，使对一切素数 $p\notin\mathfrak{B}$ 与一切 $m$，
$$
\lvert\sigma_p(m)-1\rvert\le C\,p^{-1-\delta}.
$$

则（已证其蕴含）
$$
\sup_m\lvert\log T_P(m)\rvert\ll_\delta P^{-\delta},
$$
且 L-SSO-1 的周期逼近误差为 $O(P^{-\delta})$。

**缺口 Tail-Weil.** 需对仿射曲面 $x^4+y^3+z^2=m$ 的 $\mathbb{F}_p$-点计给出一致幂次节省（Lang–Weil / Deligne 型）；本仓库未单独核验常数 $\delta$。SS-1 的 $\sigma_p\ge p^{-2}$ **不**单独给出 $|\sigma_p-1|\ll p^{-1-\delta}$。

---

## L-SSO-3（已证）— 窗口上的二进乘法轨道

令 $q$ 为奇数（可取 $q=M_P$ 的奇部）。则
$$
n-2^k\equiv n-2^\ell\pmod{q}\iff 2^k\equiv 2^\ell\pmod{q/(q,\text{相关因子})}
$$
更干净地：在 $(2,q)=1$ 时，
$$
n-2^k\bmod q
$$
由 $2^k\bmod q$ 唯一确定，且
$$
k\mapsto 2^k\bmod q
$$
是乘法群 $(\mathbb{Z}/q\mathbb{Z})^\times$ 中子群 $\langle 2\rangle$ 上的轨道，周期为 $P_q:=\mathrm{ord}_q(2)$。

因此截断奇异级数沿窗口的序列
$$
\bigl(\mathfrak{S}_{\le P}(n-2^k)\bigr)_{1\le k\le K}
$$
是周期为 $P_{M_P^\mathrm{odd}}$ 的序列（对固定 $n\bmod M_P$），即二进乘法作用下的有限轨道采样。

**证明.** $n-2^{k+1}=n-2\cdot 2^k$，模奇 $q$ 时乘 $2$ 可逆；差 $2^k-2^\ell=2^\ell(2^{k-\ell}-1)$。序 $\mathrm{ord}_q(2)$ 的标准定义给出周期性。再与 L-SSO-1 合成即得。证毕。

---

## L-SSO-4（已证）— 单素局部「极小」不能覆盖长连续指数弧

固定奇数素数 $p\notin\mathfrak{B}$，以及阈值 $c_0\in(0,1)$。定义坏剩余类
$$
B_p(c_0)=\{r\in\mathbb{Z}/p\mathbb{Z}:\sigma_p(r)\le c_0\}.
$$
令 $H_p=\langle 2\rangle\le\mathbb{F}_p^\times$，$P_p=\lvert H_p\rvert=\mathrm{ord}_p(2)$。对固定 $n\not\equiv 0\pmod{p}$（若 $n\equiv 0$ 则 $n-2^k\equiv -2^k$，仍落在一维乘法轨道上，论证平行），考察
$$
r_k=n-2^k\bmod p.
$$

**断言.** 若存在长度 $L$ 的连续整数区间 $I\subset\{1,\ldots,K\}$ 使
$$
\forall k\in I,\qquad r_k\in B_p(c_0),
$$
则 $L\le P_p$，且轨道弧 $\{2^k:k\in I\}$ 整段落在使 $n-2^k\in B_p(c_0)$ 的余集约束下；特别地，若
$$
\frac{\lvert B_p(c_0)\cap(n-H_p)\rvert}{P_p}\le 1-\kappa_p
\quad(\kappa_p>0),
$$
则最长连续命中坏类的长度满足
$$
L\le (1-\kappa_p)P_p.
$$
（在循环轨道上：连续坏弧不能超过坏点总数。）

**证明.** $\{r_k\}$ 沿 $k$ 逐步乘以 $2^{-1}$（或等价地 $2^k$ 逐步乘 $2$），故为圆周 $H_p$ 上的等步采样。连续 $L$ 个命中对应圆周上一条长 $L$ 的弧落在坏集中，故 $L$ 不超过坏点个数，亦即 $\le(1-\kappa_p)P_p$。证毕。

**推论（已证）.** 单靠**一个**固定素数的局部因子 $\sigma_p\le c_0$，无法使长度 $>P_p$ 的连续窗口段上处处「局部极小」。要压制长段，必须动员**多个**素数或让坏集占满几乎整个轨道（与 $\kappa_p>0$ 冲突）。

---

## L-SSO-5（条件式，G-SS 型）— 长段同步极小与 Euler 统计冲突

### 极小约定

称 $\mathfrak{S}(m)$ **$\eta$-极小**，若 $\mathfrak{S}(m)\le\eta$。对窗口点写 $\mathfrak{S}_k=\mathfrak{S}(n-2^k)$。

### 局部统计假设 LS（条件式输入）

存在绝对常数 $\kappa\in(0,1)$、$c_0\in(0,1)$、$p_0$，使对所有素数 $p\ge p_0$：
$$
\frac{\lvert\{r\bmod p:\sigma_p(r)\le c_0\}\rvert}{p}\le 1-\kappa.
$$
（等价叙述：使 $\sigma_p$「显着偏小」的剩余类有一致正比例的补集。）

### 积尾 / 截断假设 AP

取 $P$ 充分大（由 L-SSO-2）使 $\sup_m\lvert T_P(m)-1\rvert\le 1/2$，且 $\mathfrak{S}_{\le P}$ 的值集有限（L-SSO-1）。再设存在 $\eta_0>0$ 使「$\mathfrak{S}(m)\le\eta$ 且 $\eta\le\eta_0$」蕴含
$$
\mathfrak{S}_{\le P}(m)\le 2\eta
$$
且进一步（**鸽笼形式**）：存在有限素集 $\mathcal{P}_\ast\subset(p_0,P]$ 与阈值 $\alpha\in(0,1)$，使 $\mathfrak{S}(m)\le\eta$ 时至少一个 $p\in\mathcal{P}_\ast$ 满足 $\sigma_p(m)\le c_0$，或
$$
\prod_{p\le P}\sigma_p(m)\le\eta^{\alpha}
$$
由 $\ge c\log P$ 个互异 $p$ 上的 $\sigma_p\le c_0$ 共同贡献（两种分包均可；下用前一种强形式便于陈述）。

### G-SS 陈述（条件式）

**假设 LS + AP 的强鸽笼形式.** 则存在常数 $c=c(\kappa,c_0,P)>0$，使对充分大 $n$，**不存在**长度
$$
L\ge c\log n
$$
的连续指数区间 $I$，满足
$$
\forall k\in I,\qquad \mathfrak{S}(n-2^k)\le\eta_0.
$$

**证明概要（条件式推演，已证其蕴含关系）.**  
若连续 $L$ 段皆 $\eta_0$-极小，则对每个 $k\in I$，存在 $p(k)\in\mathcal{P}_\ast$ 使 $\sigma_{p(k)}(n-2^k)\le c_0$。素集 $\mathcal{P}_\ast$ 有限，故存在固定 $p\in\mathcal{P}_\ast$ 与子段 $I'\subset I$，
$$
\lvert I'\rvert\ge L/\lvert\mathcal{P}_\ast\rvert,
$$
使该 $p$ 对所有 $k\in I'$ 皆坏。由 L-SSO-4 与 LS，
$$
\lvert I'\rvert\le(1-\kappa)P_p\le(1-\kappa)p.
$$
取 $c$ 使 $L/\lvert\mathcal{P}_\ast\rvert>(1-\kappa)\max\{p:p\in\mathcal{P}_\ast\}$ 即矛盾。若改用「多素分担」弱鸽笼，则对每个贡献素应用 L-SSO-4，再用 $P_p\le p\le P$ 的长度上限与 $L\ge c\log n$ 比较；当 $c\log n$ 超过 $\sum_{p\le P}(1-\kappa)P_p$ 的可覆盖预算时同样冲突。证毕。

**与 SS-Sync 的接口.** 若全体窗口（长 $\asymp\log n$）皆 $\eta$-极小，则更含连续 $\ge c\log n$ 段极小，与 G-SS 冲突；故在 LS+AP 下
$$
\max_{1\le k\le K}\mathfrak{S}(n-2^k)\gg 1
$$
（或 $\gg\eta_0$）。**注意：** 这仍弱于目标 SS-Sync 的 $(\log n)^{-c}$ 量级表述，且依赖 LS；**不**推出 SS-Sync，更**不**推出原猜想。

---

## L-SSO-6（草案 / 缺口清单）— 通往 SS-Sync 的剩余障碍

| 缺口代号 | 内容 | 堵住则得 |
|----------|------|----------|
| SSO-G1 | Tail-Weil：一致 $\|\sigma_p-1\|\ll p^{-1-\delta}$ | L-SSO-2(B) 定量 |
| SSO-G2 | LS：坏类比例 $\le 1-\kappa$ 对大 $p$ 一致 | L-SSO-5 的输入 |
| SSO-G3 | 极小 $\Rightarrow$ 有限素集上局部坏的有效鸽笼（无「无限多素各损一点」逃逸） | 强化 G-SS |
| SSO-G4 | 由 $\max\mathfrak{S}\gg 1$ 升至 $\max\mathfrak{S}\gg(\log n)^{-c}$ | 接近 SS-Sync |
| SSO-G5 | SS-阈值（同 L-Ekill-SS-2）：$\mathfrak{S}(m)\ge(\log m)^{-A}\Rightarrow m\in\mathcal{R}_{4,3,2}$ | 对接 E-kill；**R5 改写为 Thr-G1**（$\mathrm{H}_{\mathrm{thr}}$）+ 已证 L-Thr-3，见 `L-Thr.md` |

**明确非声称.** 本文件不证明 SS-Sync，不证明 $\mathcal{F}_0$ 有限，不证明原猜想。

---

## 状态总表

| 编号 | 摘要 | 状态 |
|------|------|------|
| L-SSO-1 | $\mathfrak{S}_{\le P}$ 模 $M_P$ 周期 | 已证 |
| L-SSO-2(A) | 绝对收敛下积尾一致小 | 已证（框架假设下） |
| L-SSO-2(B) | 幂次尾 $O(P^{-\delta})$ | 条件式（Tail-Weil） |
| L-SSO-3 | 窗口 = 二进乘法轨道采样 | 已证 |
| L-SSO-4 | 单素坏类不能盖住长于轨道坏弧的连续段 | 已证 |
| L-SSO-5 | G-SS：连续 $\ge c\log n$ 极小 $\Rightarrow$ 与 LS 冲突 | 条件式 |
| L-SSO-6 | 缺口 SSO-G1–G5 | 缺口 |
