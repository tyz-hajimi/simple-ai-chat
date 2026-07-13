# Erdős Distinct Subset Sums：从 Conway–Guy 数值提炼的引理

设 \(A=\{a_1,\ldots,a_n\}\subset[1,N]\) 的全部 \(2^n\) 个子集和互异（dissociated），
\(\Sigma(A)\) 为其子集和集。目标猜想是 \(N\ge c\,2^n\)。

当前最佳通用下界仍是
\[
N\ge\binom{n}{\lfloor n/2\rfloor}
=\Bigl(\sqrt{\tfrac2\pi}+o(1)\Bigr)\frac{2^n}{\sqrt n}.
\]

本文记录从 Conway–Guy 可行集数值解剖中提炼、并已严格证明的引理，
以及核心候选引理的精确缺口。

---

## 0. Conway–Guy 模型（测试床）

\[
u_0=0,\quad u_1=1,\quad
r_m=\Bigl\lfloor\sqrt{2m}+\tfrac12\Bigr\rfloor,\quad
u_{m+1}=2u_m-u_{m-r_m}.
\]
第 \(n\) 个可行集为
\[
A_n=\{u_n-u_j:0\le j<n\},\qquad N_n=u_n.
\]
Bohman 已证 \(A_n\) dissociated，且
\[
\frac{N_n}{2^n}\longrightarrow c_{\mathrm{CG}}=0.2351252848111748\ldots.
\]

数值现象（验证至 \(n\le23\)）：

| 特征 | 渐近趋势 |
|------|----------|
| \(N/2^n\) | \(\to c_{\mathrm{CG}}\) |
| \(T/N=\sum a_i/N\) | \(\to n-1\) |
| \(L_2^2/N^2\) | \(\to n-5/3\) |
| Harper 真实边界 \(H/C_n\) | \(\to 1\) |
| 最密 \(N\)-窗口 \(W/C_n\) | \(\to 1\) |
| 模能量 \(E_{2N}/2^n\) | 缓增，似 \(\to\sim 2.6\) |
| 单位间隙比例 | \(\gtrsim 0.72\) |
| 缺陷 \(\Delta_n/N\) | \(2^{-\Theta(\sqrt n)}\) |

要点：CG 达到 \(N\asymp 2^n\)，但其 Harper 边界、\(N\)-窗口与排序带宽仍只有 \(2^n/\sqrt n\)。
缺失因子藏在整数空位与进位结构中。

---

## 1. 加权表示恒等式（已证）

**定义.**
\[
Q_A(h)
=\sum_{\substack{\varepsilon\in\{-1,0,1\}^n\\ \varepsilon\cdot a=h}}
2^{-|\operatorname{supp}\varepsilon|}.
\]

**引理 1.1.** \(|\Sigma(A)\cap(\Sigma(A)-h)|=2^n Q_A(h)\)。

**证明.** \(s\in\Sigma(A)\) 且 \(s+h\in\Sigma(A)\) 对应有序对 \((S,T)\) 使 \(\sum T-\sum S=h\)。
令 \(\varepsilon_i=+1\)（\(i\in T\setminus S\)）、\(-1\)（\(i\in S\setminus T\)）、否则 \(0\)。
则 \(\varepsilon\cdot a=h\)。反过来，固定 \(\varepsilon\)，在 \(\operatorname{supp}\varepsilon\) 上 \(S,T\) 被钉死，
补集上有 \(2^{n-|\operatorname{supp}\varepsilon|}\) 种公共选择。故
\[
|\Sigma(A)\cap(\Sigma(A)-h)|
=\sum_{\varepsilon\cdot a=h}2^{n-|\operatorname{supp}\varepsilon|}
=2^n Q_A(h).
\]

**推论 1.2.** 若 \(\Delta_i\) 为 \(\Sigma(A)\) 排序相邻间隙，则
\[
\#\{i:\Delta_i=1\}=2^n Q_A(1).
\]

**CG 下界.** 对 \(n\ge 8\)，缺陷前缀给出
\[
Q_{A_n}(1)\ge\frac{43}{64},
\]
故单位间隙比例 \(\ge 43/64\)。

---

## 2. 厚化与 Cauchy–Schwarz（已证）

设 \(B_H=\{0,\ldots,H-1\}\)，\(\Delta_1,\ldots,\Delta_{2^n-1}\) 为相邻间隙。

**引理 2.1.**
\[
|\Sigma(A)+B_H|=H+\sum_i\min(\Delta_i,H).
\]

**证明.** \(\Sigma(A)+B_H=\bigcup_j[s_j,s_j+H-1]\)。
总跨度 \(s_{m-1}-s_0+H=\sum\Delta_i+H\)；每个 \(\Delta_i>H\) 空出 \(\Delta_i-H\) 个点，故
\[
|\Sigma(A)+B_H|
=H+\sum_i\bigl(\Delta_i-\max(0,\Delta_i-H)\bigr)
=H+\sum_i\min(\Delta_i,H).
\]

**引理 2.2.** 令
\[
D_H=H+2\sum_{h=1}^{H-1}(H-h)Q_A(h).
\]
则
\[
|\Sigma(A)+B_H|\ge\frac{2^n H^2}{D_H}.
\]

**证明.** \(f=1_{\Sigma(A)}*1_{B_H}\)，\(\sum f=2^n H\)，\(\operatorname{supp}f=\Sigma(A)+B_H\)。
Cauchy–Schwarz：
\[
(2^n H)^2\le|\operatorname{supp}f|\sum_y f(y)^2.
\]
而
\[
\sum_y f(y)^2
=\sum_{s,s'\in\Sigma(A)}\max\bigl(0,H-|s-s'|\bigr)
=2^n D_H,
\]
其中用到引理 1.1。

**推论 2.3.** 若 \(Q_A(h)\le\eta\)（\(1\le h<H\)）且 \(A\subset[1,N]\)，则
\[
nN+H\ge\frac{2^n H}{1+\eta(H-1)}.
\]

这给出“小近关系少 \(\Rightarrow\) 大跨度”的二分接口；反向“近关系多 \(\Rightarrow\) 零关系”尚未闭合。

---

## 3. 缺陷坐标与无进位约束（已证）

写 \(a_i=N-b_i\)，\(B=\sum b_i=hN+\Delta\)，\(0\le\Delta<N\)。
记 \(\beta(S)=\sum_{i\in S}b_i\)，
\[
L_r(t)=\#\{S:|S|=r,\ \beta(S)\le t\},
\qquad
\Delta_k=B-kN.
\]

**引理 3.1（度限制）.** 若 \(B\le\tfrac32 N\)，则子集和碰撞只能发生在基数差 \(0\) 或 \(1\)。

**证明.** \(\bigl||I|-|J|\bigr|N=\bigl|\beta(I)-\beta(J)\bigr|\le B\le\tfrac32 N\)，故基数差 \(\le 1\)。

**引理 3.2（无 \(k\)-进位）.** 若不存在 \(|T|=|S|+k\) 使 \(\beta(T)=\beta(S)+kN\)，则对任意 \(r\)，
\[
L_r(\Delta_k)+L_{n-r-k}(\Delta_k)\le\Delta_k+1.
\]

**证明.** \(\Delta_k<0\) 时两边为零。否则令
\[
\mathcal A=\{ \beta(S):|S|=r,\ \beta(S)\le\Delta_k\},
\]
\[
\mathcal B=\{ \beta(T)-kN:|T|=r+k,\ \beta(T)\ge kN\}.
\]
二者落入 \(\{0,\ldots,\Delta_k\}\)；若相交则产生 \(k\)-进位。取补集得 \(|\mathcal B|=L_{n-r-k}(\Delta_k)\)。

**推论 3.3.** 当 \(B=N+\Delta<2N\) 时，dissociation 等价于：

1. 每个固定基数的 \(b\)-子集和互异；
2. 不存在 \(|T|=|S|+1\) 使 \(\beta(T)=\beta(S)+N\)；

且对每个 \(r\)，
\[
L_r(\Delta)+L_{n-r-1}(\Delta)\le\Delta+1.
\]

---

## 4. 模能量（已证部分）

定义
\[
\nu_q(r)=\#\{s\in\Sigma(A):s\equiv r\pmod q\},
\qquad
E_q=\sum_r\nu_q(r)^2,
\qquad
W_q=\frac{E_q}{2^n}.
\]

**引理 4.1（加权 alias）.**
\[
W_q
=\sum_{\substack{\varepsilon\in\{-1,0,1\}^n\\ q\mid\varepsilon\cdot a}}
2^{-|\operatorname{supp}\varepsilon|}.
\]

**证明.** \(E_q\) 计有序对 \((\xi,\xi')\) 使 \(q\mid(\xi-\xi')\cdot a\)。固定 \(\delta=\xi-\xi'\)，实现数为 \(2^{n-|\operatorname{supp}\delta|}\)。

**引理 4.2（CS）.** \(W_q\ge 2^n/q\)。特别地 \(W_{2N}\ge 2^n/(2N)\)；若 \(W_{2N}\le C\) 则 \(N\ge 2^{n-1}/C\)。

**引理 4.3（\(N\in A\) 时折半）.** 若 \(N\in A\)，则 \(E_{2N}=E_N/2\)。

**证明.** 切换最大元 \(N\) 使模 \(2N\) 余数平移 \(N\)，每个模 \(N\) 纤维均匀分裂为两个 lift，故 \(F_N(r)=2F_{2N}(r)\)（\(r<N\)），从而 \(E_N=4\sum F_{2N}^2\)，\(E_{2N}=2\sum F_{2N}^2\)。

**引理 4.4（平凡上界）.** \(W_{2N}\le\lfloor n/2\rfloor+1\)。

**证明.** \(\Sigma(A)\subset[0,\sum a_i]\)，\(\sum a_i\le nN\)，同一模 \(2N\) 类中至多 \(\lfloor n/2\rfloor+1\) 个点，故 \(\max\nu\le\lfloor n/2\rfloor+1\)，\(E\le(\max\nu)2^n\)。

**候选 4.5（未证，与目标等强）.** 存在绝对常数 \(C\) 使 \(W_{2N}\le C\)。

CG 与二进制均支持；平凡界已是 \(O(n)\)。弱化 \(W_{2N}\le C\sqrt n\) 亦未证，且足以推出当前最佳尺寸阶。

**部分进展（项式支撑）.** 若 \(2N\mid\varepsilon\cdot a=2Nm\neq 0\)，则
\[
|\operatorname{supp}\varepsilon|\ge 2|m|,
\]
故单项贡献 \(\le 4^{-|m|}\)。若能升级为总质量 \(c_{2Nm}\le 4^{-|m|}\)，则 \(W_{2N}\le 5/3\)。缺口正是别名个数的控制。

---

## 5. 宏观缺陷下的相邻重层互斥（已证）

**引理 5.1.** 设 \(B=N+\Delta\)，\(\Delta\ge\eta N\)，\(\gamma>(2+\eta)/(2(1+\eta))\)。
则不存在相邻的两个 \(\gamma\)-重层（\(\binom{n}{r}\ge\gamma(B+1)\)）。

**证明.** \(\gamma\)-重层 \(r\) 满足
\[
|\Sigma_r\cap[0,\Delta]|
\ge\binom{n}{r}+\Delta-(B+1)
\ge\gamma(B+1)-N.
\]
同理层 \(r+1\) 在 \([N,N+\Delta]\) 有同样下界。无一次进位迫使二者经 \(+N\) 后在 \([0,\Delta]\) 不交，故
\[
2\bigl(\gamma(B+1)-N\bigr)\le\Delta+1,
\]
整理得 \(\gamma\) 上界。

**推论 5.2.** 若 \(\Delta\ge\eta N\)，则
\[
N\ge c(\eta)\frac{2^n}{\sqrt n},
\]
其中 \(c(\eta)\) 优于无条件的 \(1/2\) 常数（接近 \(1/(1+\eta)\) 量级），但阶仍是 \(2^n/\sqrt n\)。

精确缺口：临界带宽 \(\Theta(\sqrt n)\) 的平均重数为 \(\Theta(\sqrt n)\)；相邻互斥只削常数因子。

---

## 6. 熵恒等式（已证）

令 \(X\) 为均匀随机子集和，\(X=NQ+R\)，\(0\le R<N\)。
因 dissociation，\(H(X)=n\)。定义
\[
D=\log_2 N-H(R\mid Q).
\]

**引理 6.1.** \(D=H(Q)+\log_2 N-n\)。

**证明.** \(X\leftrightarrow(Q,R)\) 双射，\(H(R\mid Q)=n-H(Q)\)。

**推论 6.2.** 候选 \(D\ge H(Q)-C\) 等价于 \(N\ge 2^{n-C}\)。

对 CG：\(H(Q)=H(\mathrm{Bin}(n,1/2))+o(1)\)，且
\[
D=\tfrac12\log_2\tfrac{\pi e n}{2}+\log_2 c_{\mathrm{CG}}+o(1),
\]
故任何适用于 CG 的常数须 \(C\ge -\log_2 c_{\mathrm{CG}}\approx 2.0885\)。

---

## 7. 候选结构二分（部分已证）

设 \(a_i=N-b_i\)，\(B=\sum b_i\)。

**分支 I（宏观重叠，\(\Delta\ge\eta N\)）.**  
已证改进常数的 Harper 型界（§5）；完整 \(c(\eta)2^n\) 缺“带内重数 \(O_\eta(1)\)”。

**分支 II（近临界，\(B=N+o(N)\)）.**  
CG 落在此分支，且满足可求和损失
\[
\frac{u_{n+1}}{2^{n+1}}
=\frac{u_n}{2^n}-2^{-r_n-1}\frac{u_{n-r_n}}{2^{n-r_n}},
\qquad\sum_n 2^{-r_n}<\infty.
\]
通用 renewal 引理未证：普通损失合并恒等式是重言式，不产生新下界。

---

## 8. 已证结果汇总

| 编号 | 陈述 | 强度 |
|------|------|------|
| 1.1–1.2 | \(Q_A\) 与单位间隙 | 精确恒等式 |
| 2.1–2.3 | 厚化 / \(D_H\) | 精确 + CS |
| 3.1–3.3 | 缺陷 / 无进位 \(L_r\) | 精确计数 |
| 4.1–4.4 | 模能量等价、CS、折半、\(O(n)\) | 部分 |
| 5.1–5.2 | \(\Delta\ge\eta N\) 相邻重层互斥 | 改进 Harper 常数 |
| 6.1–6.2 | 熵补偿恒等式 | 与目标等强的改写 |

**未证但与目标同强的最短候选：**
\[
W_{2N}=\sum_{2N\mid\varepsilon\cdot a}2^{-|\operatorname{supp}\varepsilon|}\le C.
\]

**次选候选：** 近临界缺陷的可求和 renewal；或中间层缺陷极差 \(O(N)\)。

---

## 9. 压力测试清单

任何新引理须通过：

1. 二进制 \(\{1,2,4,\ldots,2^{n-1}\}\)；
2. 平移二进制 \(\{M+2^{i-1}\}\)（\(M>2^n\)）；
3. Conway–Guy \(A_n\)；
4. \(\{3,5,6,7\}\)。

特别地：不能假设 \(\sum a_i^2=O(N^2)\)、不能假设长度 \(O(N)\) 窗口含 \(\Omega(2^n)\) 个和、
不能把模碰撞自动提升为整数零关系。
