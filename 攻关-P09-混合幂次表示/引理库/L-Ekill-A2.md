# L-Ekill-A2：二进差集相关

## L-Ekill-A2-1（已证）

令 $A_K=\{a:\lceil K/2\rceil\le a\le K\}$，$M_K=|A_K|$，
$$
\Delta_K=\{2^a-2^b:a,b\in A_K,\ a<b\}.
$$
局部相关
$$
\mathcal{C}_E(I,K)=\sum_{a<b}\sum_{t\in I}1_E(t)1_E(t+2^a-2^b).
$$
若 $N\in\mathcal{F}_0$，$K=\lfloor\log_2(N-1)\rfloor$，$I_N=[N-2^K,N-2^{\lceil K/2\rceil}]$，则
$$
\mathcal{C}_E(I_N,K)\ge\binom{M_K}{2}.
$$

**证明.** 对每个 $a\in A_K$ 有 $N-2^a\in E$。取 $t=N-2^a$，则 $t\in I_N$ 且 $t+2^a-2^b=N-2^b\in E$。每对 $a<b$ 贡献至少 $1$。证毕。

## L-Ekill-A2-2（条件式）

若存在 $\eta>0$、$K_0$，使对所有 $K\ge K_0$ 与 $2^K<N\le 2^{K+1}$，
$$
\mathcal{C}_E([N-2^K,N-2^{\lceil K/2\rceil}],K)\le(1-\eta)\binom{M_K}{2},
$$
则 $\mathcal{F}_0$ 有限。

**证明.** 与 A2-1 矛盾即得 $K$ 有界。

**缺口.** 真实 $E$ 的局部反相关估计。
