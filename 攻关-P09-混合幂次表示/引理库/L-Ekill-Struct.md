# L-Ekill-Struct：结构假说

## L-Ekill-Struct-1（条件式，已证其蕴含关系）

设奇数模 $Q$、$A\subset\mathbb{Z}/Q\mathbb{Z}$、$S\subset\mathbb{N}_0$ 使 $E\subset\{m:m\bmod Q\in A\}\cup S$。令 $P=\mathrm{ord}_Q(2)$，
$$
g_0=\min_r\#\{1\le j\le P:r-2^j\notin A\bmod Q\}>0,
$$
且 $\#\{1\le k\le K:N-2^k\in S\}\le B K^\theta$（$\theta<1$）。则 $\mathcal{F}_0$ 有限。

**证明.** 每个指数周期至少 $g_0$ 个点被迫落入 $S$，与 $o(K)$ 上界矛盾。

**缺口.** 真实 $E$ 是否具有此类覆盖未知；SS-1 表明不应主要来自固定素数局部类。
