# L-Hua-*：华氏不等式 / 立方均值与 Hölder 三元组（路线 R2-Hua-Cube）

> 服务目标：**P2 = 假设 H**（次弧 $\int_{\mathfrak{m}}|f_4 f_3 f_2|\ll n^{1/12-\delta}$）。  
> 本文件为**新路线**：以经典华氏不等式（立方四次均值）及可引用的次临界 VMVT 为输入，系统扫描 Hölder 三元组 $(p,q,r)$，并检验次弧截断华氏是否打破 $13/24$。  
> **不**重复 L-Circ-7/8 与 L-Dec 的 $13/24$ 拼合计算本身；可引用其结论（L-Dec-2：$N^{13/24+\varepsilon}$；H-gap $=N^{11/24}$）。  
> 状态标记：`已证` / `缺口`。**不声称假设 H 已证；不声称原猜想已证。**

## 0. 记号与可引用底座

沿用 L-Circ / L-Dec：$P_j=\lfloor N^{1/j}\rfloor$，
$$
f_j(\alpha)=\sum_{1\le u\le P_j}e(\alpha u^j),\qquad j=2,3,4,
$$
主弧 $\mathfrak{M}(Q)$、次弧 $\mathfrak{m}(Q)$ 按标准宽度 $Q/(qN)$（$1\le Q\le N^{1/2}$）。记 $\beta=1/4+1/3+1/2=13/12$。

**引用（可检形式）.**

1. **华氏不等式（立方，$L^4$）.** 对任意 $\varepsilon>0$，
   $$
   \int_0^1|f_3(\alpha)|^4\,\mathrm{d}\alpha\ll_\varepsilon P_3^{2+\varepsilon}.
   $$
   出处：Hua, *Additive Theory of Prime Numbers*（华氏引理的低矩形式）；等价地由一次 Weyl 差分 + 完备化得，见 Vaughan *The Hardy–Littlewood Method* Ch.2–4。  
   等价范数：$\|f_3\|_4\ll_\varepsilon P_3^{1/2+\varepsilon}=N^{1/6+\varepsilon}$。

2. **华氏引理（立方，$L^8$）.** 
   $$
   \int_0^1|f_3|^{8}\,\mathrm{d}\alpha\ll_\varepsilon P_3^{5+\varepsilon},
   $$
   故 $\|f_3\|_8\ll_\varepsilon P_3^{5/8+\varepsilon}=N^{5/24+\varepsilon}$。

3. **次临界 VMVT（四次 / 立方）.** 
   $$
   J_{2,4}(P_4)=\int|f_4|^4\ll_\varepsilon P_4^{2+\varepsilon},\qquad
   J_{2,3}(P_3)=\int|f_3|^4\ll_\varepsilon P_3^{2+\varepsilon}
   $$
   （后者与华氏 $L^4$ 同阶；前者即使不用满 BDG 临界矩亦可由差分得到）。故对 $p\le 4$ 有 $\|f_4\|_p\le\|f_4\|_4\ll_\varepsilon N^{1/8+\varepsilon}$；对 $p\le 20$ 的满临界界 $\|f_4\|_p\ll_\varepsilon N^{1/8+\varepsilon}$ 见 L-Dec（BDG），本路线**仅在对照表中引用**，不重证。

4. **Parseval / Gauss.** $\int|f_2|^2=P_2$，故 $\|f_2\|_r\le\|f_2\|_2\asymp N^{1/4}$（$1\le r\le 2$）。次弧点态 $|f_2|\ll N^{1/2}Q^{-1/2}(\log 2N)^{1/2}$ 见 L-Circ-7（只作对照，不重算拼合）。

---

## L-Hua-1（已证）— 华氏立方均值与范数表

对任意 $\varepsilon>0$：
$$
\|f_3\|_4\ll_\varepsilon N^{1/6+\varepsilon},\qquad
\|f_3\|_8\ll_\varepsilon N^{5/24+\varepsilon}.
$$
由 $L^4$–$L^\infty$ 插值（$\|f_3\|_\infty\le P_3=N^{1/3}$），对 $q\ge 4$，
$$
\|f_3\|_q\ll_\varepsilon N^{\frac13-\frac{2}{3q}+\varepsilon}.
$$
特别地 $q=12$ 时得 $N^{5/18+\varepsilon}$，**劣于** L-Dec 所引 VMVT 临界界 $\|f_3\|_{12}\ll_\varepsilon N^{1/6+\varepsilon}$；故纯华氏插值不能替代 BDG 临界矩。

**证明.** $L^4$、$L^8$ 即引用底座 1–2。插值：令 $1/q=(1-\theta)/4$，即 $\theta=1-4/q$，则
$$
\|f_3\|_q\le\|f_3\|_4^{1-\theta}\|f_3\|_\infty^\theta
\ll_\varepsilon N^{(1-\theta)/6+\theta/3+\varepsilon}
=N^{1/3-2/(3q)+\varepsilon}.
$$
证毕。

---

## L-Hua-2（已证）— Hölder 三元组指数表（华氏主输入）

设 $p,q,r\in[1,\infty]$，$1/p+1/q+1/r=1$。则
$$
\int_0^1|f_4 f_3 f_2|\,\mathrm{d}\alpha
\le\|f_4\|_p\|f_3\|_q\|f_2\|_r,
$$
限制到 $\mathfrak{m}(Q)$ 不增大上界。采用下列**可引用**范数指数（略 $\varepsilon$）：

| 因子 | 范围 | 指数 $\alpha$（$\|f_j\|_s\ll N^{\alpha}$） | 来源 |
|------|------|------------------------------------------|------|
| $f_4$ | $1\le p\le 4$ | $1/8$ | $J_{2,4}$ / 差分 |
| $f_4$ | $4<p\le 20$ | $1/8$ | VMVT 次临界–临界（对照 L-Dec） |
| $f_4$ | $p=\infty$（次弧） | $1/4-\frac{\log Q}{8\log N}$ | Weyl（L-Circ-8） |
| $f_3$ | $q=4$ | $1/6$ | **华氏 $L^4$** |
| $f_3$ | $q=8$ | $5/24$ | 华氏 $L^8$ |
| $f_3$ | $q>4$（纯华氏插值） | $1/3-2/(3q)$ | L-Hua-1 |
| $f_2$ | $1\le r\le 2$ | $1/4$ | Parseval |
| $f_2$ | $r=\infty$（次弧） | $1/2-\frac{\log Q}{2\log N}$ | L-Circ-7 |

**代表三元组与总指数 $E=\alpha_4+\alpha_3+\alpha_2$：**

| $(p,q,r)$ | $E$（略 $\varepsilon$） | 相对 $13/24$ | 备注 |
|-----------|-------------------------|--------------|------|
| $(4,4,2)$ | $1/8+1/6+1/4=13/24$ | $=$ | **纯华氏 + 次临界四次 + Parseval** |
| $(20,4,10/7)$ | $1/8+1/6+1/4=13/24$ | $=$ | 华氏 $q=4$ + BDG $f_4$ |
| $(20,12,15/13)$ | $13/24$ | $=$ | L-Dec-2（对照，非本路线新算） |
| $(8/3,8,2)$ | $1/8+5/24+1/4=7/12$ | 劣 $+1/24$ | 华氏 $L^8$ 端点 |
| $(20,8,40/33)$ | $7/12$ | 劣 $+1/24$ | 同上 |
| $(4/3,4,\infty)_{\mathfrak{m}}$ | $19/24-\frac12\log_N Q$ | 于 $Q=N^{1/4}$ 得 $2/3$ | 回退 L-Circ-7 型 |
| $(\infty,4,2)_{\mathfrak{m}}$ | $2/3-\frac18\log_N Q$ | 于 $Q=N^{1/4}$ 得 $15/24$ | 回退 L-Circ-8 型 |

**结论.** 在华氏 $q=4$ 为主输入的所有使 $f_4,f_2$ 仍取次临界半幂的三元组上，$E$ **恒等于** $13/24$；改用华氏 $L^8$ 或次弧 $L^\infty$ 点态只使指数变差。本路线**未**得到严格优于 $13/24$ 的可引用指数。

**证明（$(4,4,2)$ 详算）.** $1/4+1/4+1/2=1$，且
$$
\|f_4\|_4\ll_\varepsilon N^{1/8+\varepsilon},\quad
\|f_3\|_4\ll_\varepsilon N^{1/6+\varepsilon},\quad
\|f_2\|_2\asymp N^{1/4},
$$
乘积 $N^{13/24+\varepsilon}$。其余行代入上表即得。证毕。

---

## L-Hua-3（已证）— 凸障碍引理

**引理（凸障碍）.** 设范数指数函数在「次临界箱」
$$
\mathcal{B}=\bigl\{(p,q,r):1\le p\le 20,\ 1\le q\le 12,\ 1\le r\le 2,\ \tfrac1p+\tfrac1q+\tfrac1r=1\bigr\}
$$
上满足
$$
\|f_4\|_p\ll_\varepsilon N^{1/8+\varepsilon},\qquad
\|f_3\|_q\ll_\varepsilon N^{1/6+\varepsilon},\qquad
\|f_2\|_r\ll N^{1/4}
$$
（华氏给出 $q=4$ 端点；VMVT 将 $q$ 扩至 $12$、$p$ 扩至 $20$）。则对一切 $(p,q,r)\in\mathcal{B}$，
$$
\int_0^1|f_4 f_3 f_2|\,\mathrm{d}\alpha\ll_\varepsilon N^{13/24+\varepsilon},
$$
且右端指数 **不依赖** 三元组在 $\mathcal{B}$ 内的选取。特别地，不存在 $(p,q,r)\in\mathcal{B}$ 使 Hölder 方法给出严格小于 $13/24$ 的幂次。

**证明.** 箱内三个范数指数均为常数，故乘积指数恒为
$$
\frac18+\frac16+\frac14=\frac{3+4+6}{24}=\frac{13}{24}.
$$
$\mathcal{B}$ 非空：例如 $(4,4,2)$、$(20,4,10/7)$、$(20,12,15/13)$ 均满足 $1/p+1/q+1/r=1$。若将某一坐标越出 $\mathcal{B}$（$p>20$ 或 $q>12$ 或 $r>2$），则对应因子的已知上界指数**严格增大**（超临界 VMVT 或 $f_2$ 的 $L^{r>2}$ 平凡增长），从而总指数 $>13/24$。证毕。

**注（与 $\beta/2$ 对齐）.** $13/24=\beta/2$。凸障碍表明：凡输入不超过「各因子次临界半幂」的 Hölder 拼合，自然终点就是 $\beta/2$；华氏路线与 L-Dec 的 BDG 路线在此终点**重合**，前者不能改进后者。

---

## L-Hua-4（已证）— 次弧截断华氏不改进上界

**（A）上界无增益.** 对任意可测 $\mathfrak{m}\subseteq[0,1]$，
$$
\int_{\mathfrak{m}}|f_3|^4\,\mathrm{d}\alpha
\le\int_0^1|f_3|^4\,\mathrm{d}\alpha
\ll_\varepsilon P_3^{2+\varepsilon}.
$$
因而 $\|f_3\|_{L^4(\mathfrak{m})}\ll_\varepsilon N^{1/6+\varepsilon}$ 与全环面华氏同阶。代入 L-Hua-2 的 $(4,4,2)$ 等三元组，次弧截断**不能**把 Hölder 上界压到 $N^{13/24-\delta}$。

**（B）小 $Q$ 下的饱和下界.** 设 $1\le Q\le N^{1/6-\delta}$（$\delta>0$ 固定）。展开
$$
\int_{\mathfrak{m}(Q)}|f_3|^4
=\sum_{x_1,\ldots,x_4\le P_3}\int_{\mathfrak{m}(Q)}e\bigl(\alpha(x_1^3+x_2^3-x_3^3-x_4^3)\bigr)\,\mathrm{d}\alpha.
$$
记 $\Delta=x_1^3+x_2^3-x_3^3-x_4^3$。$\Delta=0$ 的解数 $\gg P_3^2$，且 $\int_{\mathfrak{m}}1=\mathrm{meas}(\mathfrak{m})\ge 1-O(Q^2/N)$，故对角贡献 $\gg P_3^2$。非对角项满足
$$
\Bigl|\int_{\mathfrak{m}}e(\alpha\Delta)\,\mathrm{d}\alpha\Bigr|
=\Bigl|\int_{\mathfrak{M}}e(\alpha\Delta)\,\mathrm{d}\alpha\Bigr|
\le\mathrm{meas}(\mathfrak{M})\ll Q^2/N,
$$
故非对角总贡献 $\ll P_3^4\cdot Q^2/N=N^{1/3}Q^2$。当 $Q\le N^{1/6-\delta}$ 时该项 $o(P_3^2)$，因此
$$
\int_{\mathfrak{m}(Q)}|f_3|^4\,\mathrm{d}\alpha\gg P_3^2.
$$
即截断华氏在幂次上与全环面**同阶**（饱和）。

**（C）圆法主射程 $Q=N^{1/4}$.} 虽（B）的粗糙非对角估计在 $Q=N^{1/4}$ 失效，但（A）的上界始终有效：截断不能提供优于 $P_3^{2+\varepsilon}$ 的**可引用**四次均值，故对 $\int_{\mathfrak{m}}|f_4 f_3 f_2|$ 的 Hölder 上界仍止于 $N^{13/24+\varepsilon}$。

**证明.** （A）由正性；（B）如上计数；（C）由（A）+ L-Hua-2。证毕。

---

## L-Hua-5（已证）— 结算：无改进，$H$ 仍开放

| 来源 | 次弧积分可引用上界 | 相对 $N^{1/12}$ |
|------|-------------------|-----------------|
| L-Circ-8（引用） | $N^{61/96}$ | 缺口 $N^{53/96}$ |
| L-Dec-2（引用） | $N^{13/24}$ | 缺口 $N^{11/24}$ |
| **L-Hua-2 / 凸障碍** | **$N^{13/24}$（无改进）** | **缺口仍 $N^{11/24}$** |
| 假设 H 目标 | $N^{1/12}$ | — |

**判决.**
1. 经典华氏 $L^4$ 与次临界四次均值给出新三元组 $(4,4,2)$，指数恰为 $13/24$，与 L-Dec-2 **持平**，不优。  
2. 凸障碍（L-Hua-3）说明：一切停留在次临界箱 $\mathcal{B}$ 内的 Hölder 拼合被钉死在 $\beta/2=13/24$。  
3. 次弧截断华氏（L-Hua-4）不提供额外幂次节省。  
4. **假设 H 仍为未证条件式**；本路线不缩小 H-gap。

若要打破 $13/24$，必须引入超出「华氏 / 次临界均值 + Hölder」族的输入（例如真次弧上的非对角结构、与缺项 $g$ 的联合估计 H′/Lac，或强于凸性的解耦）。

---

## 状态汇总

| 编号 | 摘要 | 状态 |
|------|------|------|
| L-Hua-1 | 华氏 $L^4$/$L^8$ 与插值范数表 | 已证 |
| L-Hua-2 | Hölder 三元组指数表；最优 $=13/24$ | 已证 |
| L-Hua-3 | **凸障碍**：次临界箱内指数恒为 $13/24$ | 已证 |
| L-Hua-4 | 次弧截断华氏无上界增益；小 $Q$ 饱和 | 已证 |
| L-Hua-5 | 结算：不改进 L-Dec；H-gap 仍 $N^{11/24}$ | 已证（结算） |

**对 H 的判决：** 本路线确认华氏路径与 L-Dec 凸终点重合，**H 仍为未证条件式**。
