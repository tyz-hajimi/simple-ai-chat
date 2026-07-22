# L-Circ-7/8/9：次弧子估计

记号：$P_j=\lfloor N^{1/j}\rfloor$，$f_j(\alpha)=\sum_{u\le P_j}e(\alpha u^j)$；主弧 $\mathfrak{M}(Q)$、次弧 $\mathfrak{m}(Q)$ 按标准 $Q/(qN)$ 定义。

## L-Circ-7（已证）

对 $\alpha\in\mathfrak{m}(Q)$（$1\le Q\le N^{1/2}$），
$$
|f_2(\alpha)|\ll N^{1/2}Q^{-1/2}(\log 2N)^{1/2},
$$
且
$$
\int_{\mathfrak{m}(Q)}|f_4f_3f_2|\ll N^{19/24}Q^{-1/2}(\log 2N)^{1/2}.
$$

出处形式：Vaughan *HL Method* Ch.2；Iwaniec–Kowalski §8。

## L-Circ-8（已证）

Weyl：$|f_j(\alpha)|\ll_{\varepsilon} P_j^{1+\varepsilon}Q^{-1/2^{j-1}}$（$j=3,4$，$\alpha\in\mathfrak{m}(Q)$，$Q\le P_j$）。故 $Q\le N^{1/4}$ 时
$$
\int_{\mathfrak{m}}|f_4f_3f_2|\ll_\varepsilon\min\bigl(N^{19/24+\varepsilon}Q^{-1/2},\ N^{17/24+\varepsilon}Q^{-1/4},\ N^{2/3+\varepsilon}Q^{-1/8}\bigr).
$$
取 $Q=N^{1/4}$ 最好约 $N^{61/96+\varepsilon}$，距 $N^{1/12}$ 差约 $N^{53/96}$。

## L-Circ-9（已证）

$g=\sum_{k=1}^K e(\alpha 2^k)$ 满足 $\int|g|^2=K$，故 $\|g\|_1\le K^{1/2}$，且
$$
\mathrm{meas}\{|g|\ge\lambda\}\le K/\lambda^2.
$$
严格强于平凡 $|g|\le K$ 的均值后果；约 $\sqrt{K}$ 杠杆，不破 $\beta=13/12<2$ 墙。

## 状态
H 仍为条件式；以上仅为子估计。
