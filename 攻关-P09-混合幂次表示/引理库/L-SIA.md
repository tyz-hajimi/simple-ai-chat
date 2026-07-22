# L-SIA-*：短二进窗几乎所有（路线 R15-Short-Interval-Almost）

> 路线 **R15-Short-Interval-Almost**（P09 攻关轮次 15；服务**弱于原猜想**的可发表强化，**非**原猜想）。  
> 想法：定理 B 只保证几乎所有 $n$ 可写 $n=x^4+y^3+z^2+2$（固定 $k=1$）。本路线证明：对几乎所有 $n$，**短二进窗**
> $$
> \{n-2^k:K-K^{\theta}\le k\le K\}
> $$
> （$\theta\in(0,1)$）内已有可表点；进而几乎所有 $n$ 在该窗内有 $(1-o(1))$ 比例的击中。  
> **总判决（一句话）.** Roth 例外集密度 $O((\log)^{-1/20})$ 与窗长 $L\asymp K^{\theta}$ 的 Markov 平均即得短窗几乎所有；这**强化**定理 B（大 $k$ 近 $\log n$）与 L-Bin-5（全窗 $\asymp\log n$ 个可用 $k$ 锐化为短窗），但**不达**充分大全体（$\theta=1$ 充分大 $=$ 原猜想难度）。

---

## 0. 符号

$$
\begin{aligned}
\mathcal{R}_{4,3,2}&=\{x^4+y^3+z^2:x,y,z\in\mathbb{N}_0\},\\
E&=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2},\\
\mathcal{R}&=\{x^4+y^3+z^2+2^k:x,y,z\in\mathbb{N}_0,\ k\in\mathbb{N}_1\}.
\end{aligned}
$$
对 $n\ge 3$，令
$$
K=K(n):=\lfloor\log_2(n-1)\rfloor,
$$
故 $2^K\le n-1<2^{K+1}$，且 $1\le k\le K$ 时 $n-2^k\ge 1$。  
固定 $\theta\in(0,1]$，短指数窗与短二进点集
$$
\begin{aligned}
I(n;\theta)&:=\bigl\{k\in\mathbb{N}:K-K^{\theta}\le k\le K\bigr\},\\
W(n;\theta)&:=\bigl\{n-2^k:k\in I(n;\theta)\bigr\}.
\end{aligned}
$$
窗长
$$
L(n;\theta):=\#I(n;\theta)=\bigl\lfloor K^{\theta}\bigr\rfloor+1\asymp K^{\theta}.
$$
击中计数
$$
\rho_{\theta}(n):=\#\bigl\{k\in I(n;\theta):n-2^k\in\mathcal{R}_{4,3,2}\bigr\}
=L(n;\theta)-\#\bigl\{k\in I(n;\theta):n-2^k\in E\bigr\}.
$$
二进段 $I_K:=[2^K,2^{K+1})$（或闭区间 $[2^K,2^{K+1}]$；差 $O(1)$ 不影响密度）。

**Roth 骨架（定理 B 输入）.**
$$
M(X):=\lvert E\cap[1,X]\rvert\ll\frac{X}{(\log X)^{1/20}}\qquad(X\ge 3).
$$
特别地固定 $k=1$ 得几乎所有 $n\ge 2$ 属于 $\mathcal{R}$（**Thm-B**）。

**弱于原猜想（本文件一律遵守）.** 几乎所有 + 短窗（即便 $\theta$ 任意接近 $1$）**不**蕴含充分大全体；充分大短窗 CRB-Short$_\theta$（每个大 $n$ 击中 $I(n;\theta)$）与原猜想同级（见 L-CRB-4/6）。

**与 L-CRB-5.** 本文件把 L-CRB-5 的草案拼合升级为带定量例外集 / 比例击中的正式定理族，并标明相对 Thm-B、L-Bin-5 的强化关系。

---

## L-SIA-1（已证·引用：Roth 例外集与定理 B）

**命题（Roth-234）.** （K. F. Roth, J. London Math. Soc. **24** (1949), 4–13。）
$$
M(X)\ll\frac{X}{(\log X)^{1/20}}.
$$
几乎所有正整数属于 $\mathcal{R}_{4,3,2}$。

**推论（Thm-B）.** 几乎所有 $n\ge 2$ 可写成
$$
n=x^4+y^3+z^2+2
$$
（取 $k=1$）。例外集满足
$$
\#\{n\le X:n-2\in E\}\le M(X)\ll\frac{X}{(\log X)^{1/20}}.
$$

**证明.** 直接引用；详见 L-CRB-1(C)。证毕。

---

## L-SIA-2（已证：二进段上单平移的例外密度）

**引理.** 固定整数 $j$ 使 $0\le j\le K$ 且 $K\ge 2$。则
$$
\#\bigl\{n\in I_K:n-2^{K-j}\in E\bigr\}
\le M(2^{K+1})
\ll\frac{2^{K}}{K^{1/20}}.
$$
特别地该集合在 $I_K$ 内的比例 $\ll K^{-1/20}$。

**证明.** 对 $n\in I_K$ 有 $1\le n-2^{K-j}<2^{K+1}$，故
$$
\{n\in I_K:n-2^{K-j}\in E\}
\subseteq
\bigl\{m+2^{K-j}:m\in E\cap[1,2^{K+1}]\bigr\}
$$
与 $I_K$ 的交，基数 $\le M(2^{K+1})$。代入 Roth 界即得。证毕。

**注.** 取 $j=0$（即 $k=K$）已给出：几乎所有 $n\in I_K$ 满足 $n-2^K\in\mathcal{R}_{4,3,2}$，从而几乎所有 $n$ 在**最大**二进平移处可表。这已是「短窗至少一个」的特款（窗只要含 $k=K$）。

---

## L-SIA-3（已证：短窗空击中的例外集）— **弱主定理**

**定理.** 固定 $\theta\in(0,1]$。定义短窗失败集
$$
\mathcal{B}_{\theta}
:=\bigl\{n\ge 3:\rho_{\theta}(n)=0\bigr\}
=\bigl\{n\ge 3:W(n;\theta)\subseteq E\bigr\}.
$$
则
$$
\lvert\mathcal{B}_{\theta}\cap[1,X]\rvert
\ll\frac{X}{(\log X)^{1/20}}.
$$
特别地几乎所有 $n$ 满足 $\rho_{\theta}(n)\ge 1$，即存在
$$
k\in I(n;\theta)
\quad\text{使}\quad
n=x^4+y^3+z^2+2^k
$$
对某 $x,y,z\in\mathbb{N}_0$ 成立。

**证明梗概.** 若 $n\in\mathcal{B}_{\theta}\cap I_K$，则特别地 $n-2^K\in E$（因 $K\in I(n;\theta)$）。由 L-SIA-2（$j=0$）
$$
\lvert\mathcal{B}_{\theta}\cap I_K\rvert
\le\#\{n\in I_K:n-2^K\in E\}
\ll\frac{2^{K}}{K^{1/20}}.
$$
对 $K\le\log_2 X$ 求和，主项由最大二进段贡献，得
$$
\lvert\mathcal{B}_{\theta}\cap[1,X]\rvert\ll\frac{X}{(\log X)^{1/20}}.
$$
证毕。

**相对定理 B 的强化.** Thm-B 用**固定小**缺项 $2^1=2$；本条保证几乎所有 $n$ 可用**接近 $\log n$ 的短指数弧**上的某个 $2^k$。二者均来自同一 Roth 界，但采样尺度不同：前者 $n-2\sim n$，后者 $n-2^K\asymp n$ 的低位截断。

**弱于全体.** 例外集上界与 Thm-B 同级（Roth $1/20$），**不**排除无限例外，更不排除 $\mathcal{F}_0$ 无限（对照 L08 / L-LSW-5）。

---

## L-SIA-4（已证：短窗平均漏击与 Markov）

**引理（平均漏击）.** 固定 $\theta\in(0,1]$，$K\ge 2$。令
$$
\mu_K(\theta)
:=\frac{1}{\lvert I_K\rvert}
\sum_{n\in I_K}
\#\bigl\{k\in I(n;\theta):n-2^k\in E\bigr\}.
$$
则
$$
\mu_K(\theta)
\ll\frac{L_K}{K^{1/20}},
\qquad
L_K:=\lfloor K^{\theta}\rfloor+1,
$$
从而平均漏击比例
$$
\frac{\mu_K(\theta)}{L_K}\ll K^{-1/20}\to 0\quad(K\to\infty).
$$

**证明.** 交换求和：
$$
\sum_{n\in I_K}
\#\{k\in I(n;\theta):n-2^k\in E\}
=
\sum_{\substack{0\le j\le\lfloor K^{\theta}\rfloor\\K-j\ge 1}}
\#\{n\in I_K:n-2^{K-j}\in E\}.
$$
由 L-SIA-2，每项 $\ll 2^K/K^{1/20}$，项数 $\le L_K$，且 $\lvert I_K\rvert\asymp 2^K$，故
$$
\mu_K(\theta)\ll L_K\cdot K^{-1/20}.
$$
证毕。

**Markov 推论.** 对任意 $\varepsilon\in(0,1)$，
$$
\#\bigl\{n\in I_K:\#\{k\in I(n;\theta):n-2^k\in E\}>\varepsilon L_K\bigr\}
\le\frac{\mu_K(\theta)}{\varepsilon L_K}
\ll_{\varepsilon} K^{-1/20}\lvert I_K\rvert.
$$

---

## L-SIA-5（已证：短窗比例击中）— **主定理**

**定理（短二进窗几乎所有·比例版）.** 固定 $\theta\in(0,1]$。则对几乎所有 $n\ge 3$，
$$
\rho_{\theta}(n)=(1-o(1))\,L(n;\theta),
$$
即
$$
\frac{\rho_{\theta}(n)}{L(n;\theta)}\to 1
$$
沿几乎所有 $n$。等价地：短窗 $W(n;\theta)$ 内几乎所有二进点落在 $\mathcal{R}_{4,3,2}$。

**证明梗概.** 由 L-SIA-4 的 Markov 推论：对每个固定 $\varepsilon>0$，使漏击超过 $\varepsilon L_K$ 的 $n\in I_K$ 比例 $\ll_{\varepsilon} K^{-1/20}\to 0$。令 $\varepsilon=\varepsilon_K\to 0$ 足够慢（例如 $\varepsilon_K=K^{-1/40}$），则几乎所有 $n\in I_K$ 满足漏击 $o(L_K)$，即 $\rho_{\theta}(n)=(1-o(1))L_K$。对二进段求和得全局几乎所有。证毕。

**特别地（至少一个）.** 取 $\varepsilon=1/2$：几乎所有 $n$ 有 $\rho_{\theta}(n)>\tfrac12 L(n;\theta)\ge 1$，回收 L-SIA-3。

**相对 L-Bin-5.** L-Bin-5：几乎所有 $n$ 在**全**窗 $1\le k\le K$（长 $\asymp\log n$）上有 $\asymp\log n$ 个可用 $k$。本条：同一结论限制在任意正幂短弧 $I(n;\theta)$（长 $K^{\theta}=o(K)$）上仍有 $(1-o(1))$ 比例击中——把「多数可用 $k$」**局域化**到近顶端指数。

---

## L-SIA-6（已证对照：与定理 B / 整窗 / 充分大的关系）

### （A）强化层级

| 结论 | 窗 | 断言 | 状态 |
|------|----|------|------|
| Thm-B | $\{2\}$（固定 $k=1$） | 几乎所有 $n\in\mathcal{R}$ | 已证（Roth） |
| L-Bin-5 | 全窗 $1\le k\le K$ | a.e. 有 $\asymp K$ 个可用 $k$ | 已证（骨架） |
| L-SIA-3 | 短窗 $I(n;\theta)$ | a.e. 至少一个可用 $k$ | **已证** |
| L-SIA-5 | 短窗 $I(n;\theta)$ | a.e. $(1-o(1))$ 比例可用 | **已证** |
| 充分大短窗 | $I(n;\theta)$ | **每个**大 $n$ 至少一个 | **未证**（近原猜想） |
| 原猜想 | 全窗 | 每个 $n\ge 2$ | **开放** |

### （B）为何不达全体

1. **例外集仍可为无限.** L-SIA-3 仅给 $X/(\log X)^{1/20}$；与 L-LSW-5 同级，L08 表明抽象密度零 $E$ 可有无限整窗失败。  
2. **短窗充分大 $\neq$ 几乎所有.** 把「a.e.」升为「一切充分大」需反整窗 / E-kill 级输入；$\theta<1$ 只减少可用 $k$，**不降低**本质难度（L-CRB-4 W4）。  
3. **与 $\mathcal{F}_0$.** $\mathcal{F}_0$ 要求**全**窗落入 $E$；短窗失败集 $\mathcal{B}_{\theta}\supseteq\mathcal{F}_0$（当 $\theta=1$ 时 $I(n;1)$ 覆盖全窗至多差 $O(1)$ 端点约定）。L-SIA **不**证明 $\mathcal{F}_0$ 有限。

### （C）可发表表述（诚实弱化）

> **定理（可引用）.** 设 $|E\cap[1,X]|\ll X(\log X)^{-1/20}$。则对任意 $\theta\in(0,1]$，几乎所有正整数 $n$ 可写成 $n=x^4+y^3+z^2+2^k$ 且 $k$ 落在区间 $[K-K^{\theta},K]$；进一步，该短窗内可用指数的比例趋于 $1$。

输入仅为 Roth 例外集上界 + 窗长平均；**不**声称原猜想。

---

## L-SIA-7（缺口与优先级）

| 代号 | 内容 | 优先级 | 备注 |
|------|------|--------|------|
| SIA-G0 | 短窗几乎所有 / 比例击中 | **已闭合** | L-SIA-3/5 |
| SIA-G1 | 充分大短窗（每个大 $n$ 击中 $I(n;\theta)$） | 高·近原猜想 | $=\mathrm{CRB}$-G2 |
| SIA-G2 | 例外集幂次节省 $M(X)\ll X^{1-\delta}$ | 中·可发表 | 仍几乎所有层；不杀 $\mathcal{F}_0$（L08） |
| SIA-G3 | 短窗失败集的更优对数幂 | 低 | 单点 $k=K$ 已钉死 Roth $1/20$ 天花板 |
| SIA-G4 | 与 LSW / FW 联立把短窗失败升为整窗有限 | 高·P1 | 需额外相关假设 |

**勿写.** 「几乎所有短窗 $\Rightarrow$ 充分大全体」；「$\theta\to 1$ 即原猜想」。

---

## 结算

| 编号 | 状态 | 摘要 |
|------|------|------|
| L-SIA-1 | 已证（引用） | Roth + Thm-B |
| L-SIA-2 | 已证 | 二进段单平移例外密度 $\ll K^{-1/20}$ |
| L-SIA-3 | **已证（弱主定理）** | 短窗空击中例外 $\ll X/(\log)^{1/20}$；a.e. 至少一个 |
| L-SIA-4 | 已证 | 平均漏击 $\ll L_K/K^{1/20}$；Markov |
| L-SIA-5 | **已证（主定理）** | a.e. 短窗比例击中 $(1-o(1))$ |
| L-SIA-6 | 已证（对照） | 强化 Thm-B / L-Bin-5；不达全体 |
| L-SIA-7 | 缺口表 | G0 闭；充分大短窗开放 |

**本轮结论.** R15 把「定理 B 的几乎所有」强化为「几乎所有 $n$ 的短二进窗 $\{n-2^k:K-K^{\theta}\le k\le K\}$ 含可表点（且比例趋于全窗）」。证明仅用 Roth 例外集 + 窗长平均 / Markov；**可发表弱化已闭合**。充分大全体与充分大短窗仍开放。**不声称**原猜想已证。
