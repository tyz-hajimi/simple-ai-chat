# L-Biq-*：四次 Weyl 差分完备化与凸壁（路线 R6-Biquadrate-Completion）

> 路线 **R6-Biquadrate-Completion**（P09 攻关轮次 6，服务 **P2 = 假设 H**）。  
> 新想法：对 $f_4$ 做一次（或二次）Weyl 差分，把四次和式完备化为三次型 $S(\alpha;h)$（再至二次型），再与已有 $f_3$、$f_2$ 均值拼成多重积分，试图突破 $\beta/2=13/24$。  
> **结论先行：** 差分后朴素多重积分形式指数为 $35/48>13/24$；把差分回收为 $\|f_4\|_4$ 恰得 $13/24$；在「差分 + 次临界华氏/Parseval + Hölder/CS」族内 **差分不破凸壁**。  
> 可引用 L-Dec-2（$N^{13/24+\varepsilon}$）、L-Hua-1…3（华氏与凸障碍）。**不声称假设 H 已证；不声称原猜想已证。**

## 0. 记号

沿用 L-Circ / L-Dec / L-Hua：$P_j=\lfloor N^{1/j}\rfloor$，
$$
f_j(\alpha)=\sum_{1\le u\le P_j}e(\alpha u^j),\qquad j=2,3,4,
$$
$\beta=1/4+1/3+1/2=13/12$，凸终点 $\beta/2=13/24$。目标积分
$$
I:=\int_0^1|f_4(\alpha)f_3(\alpha)f_2(\alpha)|\,\mathrm{d}\alpha.
$$

对 $h\in\mathbb{Z}$、$|h|<P_4$，记一次差分和（三次型）
$$
S(\alpha;h):=\sum_{x\in I_h}e\bigl(\alpha\bigl((x+h)^4-x^4\bigr)\bigr),
$$
其中 $I_h=\{x:1\le x,x+h\le P_4\}$；约定 $S(\alpha;0)=P_4$。展开
$$
(x+h)^4-x^4=4hx^3+6h^2x^2+4h^3x+h^4,
$$
故 $h\neq 0$ 时 $S(\cdot;h)$ 是长度 $\asymp P_4$、首项系数 $\asymp h$ 的**三次**指数和。

---

## L-Biq-1（已证）— Weyl 一次差分

对任意 $\alpha\in\mathbb{R}$，
$$
|f_4(\alpha)|^2
\ll P_4\sum_{|h|<P_4}|S(\alpha;h)|.
$$
（对角 $h=0$ 贡献 $P_4\cdot P_4$；非对角为标准 Weyl 差分，见 Vaughan *The Hardy–Littlewood Method* Ch.2。）

**推论（二次差分接口）.** 对固定 $h\neq 0$，再差分一次得二次型 $T(\alpha;h,\ell)$，满足
$$
|S(\alpha;h)|^2
\ll P_4\sum_{|\ell|<P_4}|T(\alpha;h,\ell)|,
$$
其中 $T$ 为长度 $\asymp P_4$ 的二次指数和（可完备化为 Gauss 和）。本文件主线只用一次差分；二次差分仅作对照（L-Biq-4）。

---

## L-Biq-2（已证）— 差分后多重积分形式

由 Cauchy–Schwarz，
$$
I
=\int|f_4|\,|f_3f_2|
\le\Bigl(\int|f_4|^2\,|f_3f_2|\Bigr)^{1/2}
\Bigl(\int|f_3f_2|\Bigr)^{1/2},
$$
故
$$
I^2
\le\Bigl(\int|f_4|^2\,|f_3f_2|\Bigr)
\Bigl(\int|f_3f_2|\Bigr).
$$
代入 L-Biq-1，
$$
\int|f_4|^2\,|f_3f_2|
\ll P_4\sum_{|h|<P_4}\int_0^1|S(\alpha;h)|\,|f_3(\alpha)f_2(\alpha)|\,\mathrm{d}\alpha.
$$
因此差分路线的核心对象是三重型积分族
$$
\mathcal{J}(h):=\int_0^1|S(\alpha;h)|\,|f_3(\alpha)|\,|f_2(\alpha)|\,\mathrm{d}\alpha,
\qquad
\sum_{|h|<P_4}\mathcal{J}(h).
$$

**第二因子（可引用）.**
$$
\int|f_3f_2|
\le\|f_3\|_4\|f_2\|_{4/3}
\le\|f_3\|_4\|f_2\|_2
\ll_\varepsilon N^{1/6+1/4+\varepsilon}
=N^{5/12+\varepsilon},
$$
其中 $\|f_3\|_4\ll_\varepsilon N^{1/6+\varepsilon}$（L-Hua-1），$\|f_2\|_2\asymp N^{1/4}$。

---

## L-Biq-3（已证）— 朴素差分多重积分的形式指数 $=35/48$

**引理.** 仅用三次华氏 $L^4$、Parseval 与对 $h$ 的 Cauchy，有
$$
\sum_{|h|<P_4}\mathcal{J}(h)
\ll_\varepsilon P_4^{3/2}N^{5/12+\varepsilon},
$$
从而
$$
\int|f_4|^2\,|f_3f_2|
\ll_\varepsilon P_4\cdot P_4^{3/2}N^{5/12+\varepsilon}
=P_4^{5/2}N^{5/12+\varepsilon}
=N^{25/24+\varepsilon},
$$
并得
$$
I\ll_\varepsilon N^{35/48+\varepsilon}.
$$
因 $35/48=17.5/24>13/24$，本路径**严格劣于** L-Dec-2 / L-Hua-2。

**证明.** 对每个 $h$，华氏立方均值（与 $f_3$ 同证：一次差分 + 完备化；首项系数 $4h$ 经 $\alpha\mapsto 4h\alpha$ 吸收）给出
$$
\int|S(\alpha;h)|^4\,\mathrm{d}\alpha\ll_\varepsilon P_4^{2+\varepsilon}
\qquad(h\neq 0),
$$
且 $h=0$ 时 $|S|=P_4$，$\int|S|^4=P_4^4$ 可单独估为 $O(P_4\cdot N^{5/12})$ 量级，不改善总指数。Parseval：$\int|S|^2\asymp\#I_h\asymp P_4$。

用 Hölder（指数 $(4,4,2)$）：
$$
\mathcal{J}(h)
\le\|S(\cdot;h)\|_4\|f_3\|_4\|f_2\|_2
\ll_\varepsilon P_4^{1/2+\varepsilon}N^{5/12+\varepsilon}.
$$
对 $h$ 再 Cauchy（或直接 $\#h\ll P_4$）：
$$
\sum_h\mathcal{J}(h)
\le\Bigl(\sum_h\int|S|^4\Bigr)^{1/4}
\Bigl(\sum_h\int|f_3f_2|^{4/3}\Bigr)^{3/4}.
$$
左：$\sum_h\int|S|^4\ll_\varepsilon P_4\cdot P_4^{2+\varepsilon}=P_4^{3+\varepsilon}$，故 $(\cdots)^{1/4}\ll_\varepsilon P_4^{3/4+\varepsilon}$。  
右：$\|f_3f_2\|_{4/3}\le\|f_3\|_4\|f_2\|_2\ll_\varepsilon N^{5/12+\varepsilon}$（因 $3/4=1/4+1/2$），故
$$
\sum_h\int|f_3f_2|^{4/3}
=P_4\|f_3f_2\|_{4/3}^{4/3}
\ll_\varepsilon P_4 N^{5/9+\varepsilon},
$$
$(\cdots)^{3/4}\ll_\varepsilon P_4^{3/4}N^{5/12+\varepsilon}$。乘积得 $\sum\mathcal{J}\ll_\varepsilon P_4^{3/2}N^{5/12+\varepsilon}$。

代入 L-Biq-2：
$$
I^2
\ll_\varepsilon N^{25/24+\varepsilon}\cdot N^{5/12+\varepsilon}
=N^{35/24+\varepsilon},
$$
即 $I\ll_\varepsilon N^{35/48+\varepsilon}$。证毕。

**等价写法（同一指数）.** 由
$$
I\ll P_4^{1/2}\int\Bigl(\sum_h|S(h)|\Bigr)^{1/2}|f_3f_2|
\le P_4^{1/2}\Bigl(\int\sum_h|S|\Bigr)^{1/2}\|f_3f_2\|_2,
$$
及 $\int\sum_h|S|\ll_\varepsilon P_4^{3/2+\varepsilon}$、$\|f_3f_2\|_2\ll_\varepsilon N^{5/12+\varepsilon}$（$\|f_3\|_4\|f_2\|_4$，$\int|f_2|^4\ll_\varepsilon P_2^{2+\varepsilon}$），同样得到 $I\ll_\varepsilon N^{35/48+\varepsilon}$。

---

## L-Biq-4（已证）— 差分回收 $L^4(f_4)$ 恰得 $13/24$；二次差分不优

**（A）一次差分 $\Rightarrow$ 华氏 $L^4(f_4)$.} 经典计算（Hua / Vaughan）：由 L-Biq-1 与 $\sum_h\int|S|^2\ll_\varepsilon P_4^{2+\varepsilon}$，
$$
\int_0^1|f_4|^4\,\mathrm{d}\alpha
\ll_\varepsilon P_4^{2+\varepsilon},
$$
即 $\|f_4\|_4\ll_\varepsilon P_4^{1/2+\varepsilon}=N^{1/8+\varepsilon}$。再取 Hölder 三元组 $(4,4,2)$：
$$
I\le\|f_4\|_4\|f_3\|_4\|f_2\|_2
\ll_\varepsilon N^{1/8+1/6+1/4+\varepsilon}
=N^{13/24+\varepsilon}.
$$
此即 L-Hua-2 的代表元；**差分完备化的最优回收恰为凸终点 $13/24$**，不优于 L-Dec-2。

**（B）二次差分 $\Rightarrow$ 二次型 / 华氏 $L^8$.} 对 $S$ 再差分并完备化为 Gauss 和，经典得
$$
\int|f_4|^8\ll_\varepsilon P_4^{5+\varepsilon},
\qquad
\|f_4\|_8\ll_\varepsilon P_4^{5/8+\varepsilon}=N^{5/32+\varepsilon}.
$$
因 $5/32>1/8=4/32$，纯 $L^8$ 范数劣于 $L^4$。代入任一 $1/p+1/q+1/r=1$ 且用 $\|f_4\|_8$ 替代次临界半幂的三元组，形式指数 **$>13/24$**（与 L-Hua-2 表中越出次临界箱的行一致）。若要把二次差分拉回 $13/24$，必须重新进入（A）的 $L^4$ 路径，无新增益。

**（C）与点态 Weyl 对照.** 二次差分给出次弧点态 $|f_4|\ll_\varepsilon P_4^{1+\varepsilon}Q^{-1/8}$，拼合后落入 L-Dec-3 / L-Circ-8 凸族，最优端点仍是 $13/24$ 或更差（$61/96$ 等）。

---

## L-Biq-5（已证）— 障碍引理：差分不破凸壁

**定义（R6-Biq 方法族）.** 凡由下列操作得到的 $I$ 上界：
1. 以 L-Biq-1（或二次差分）替换 $|f_4|^{2^\ell}$；
2. 经 Hölder / Cauchy–Schwarz 化为 $S$、$T$、$f_3$、$f_2$ 的多重积分；
3. 估计时**仅**使用次临界输入：三次华氏 $L^4$（$\|S\|_4\ll P_4^{1/2+\varepsilon}$）、二次 Parseval/Gauss（$\|f_2\|_r\ll N^{1/4}$，$r\le 2$）、以及由差分导出的 $\|f_4\|_4\ll N^{1/8+\varepsilon}$（或更弱的 $\|f_4\|_8$）；
4. 对差分变量 $h$（及 $\ell$）仅作基数 $\ll P_4$ 的求和或 Cauchy。

**障碍引理.** 该族内一切可引用形式指数满足
$$
E_{\mathrm{Biq}}\ge\frac{13}{24}.
$$
特别地：
| 路径 | 形式指数 $E$ | 相对 $13/24$ |
|------|-------------|--------------|
| 朴素 $\sum_h\mathcal{J}(h)$ + CS（L-Biq-3） | $35/48$ | $>$ |
| 差分 $\Rightarrow\|f_4\|_4$ + $(4,4,2)$（L-Biq-4A） | $13/24$ | $=$（族内最优） |
| 二次差分 $\Rightarrow\|f_4\|_8$ + Hölder | $>13/24$ | $>$ |
| 点态 Weyl–VMVT 凸族（对照 L-Dec-3） | $\ge 13/24$ | $\ge$ |

**证明.**  
（i）L-Biq-3 给出朴素路径 $E=35/48>13/24$。  
（ii）族内最强次临界 $f_4$ 输入是 $\|f_4\|_4\ll N^{1/8+\varepsilon}$（二次差分的 $L^8$ 更弱）。与 $\|f_3\|_4\ll N^{1/6+\varepsilon}$、$\|f_2\|_2\asymp N^{1/4}$ 相乘，由 L-Hua-3 凸障碍，Hölder 指数钉死在
$$
\frac18+\frac16+\frac14=\frac{13}{24}.
$$
任何把 $h$-求和的 $P_4$ 因子留在积分外、却不用 $L^4(f_4)$ 均值吸收的估法，至少损失 $P_4^{1/2}$ 量级，落入 $35/48$ 型。  
（iii）故族内下界 $E\ge 13/24$，且等号仅在「差分回收为次临界半幂 + Hölder」时达到——与 L-Hua / L-Dec 凸终点重合，**不能**提供 $N^{-\delta}$ 以缩小 H-gap。证毕。

**一句话.** **差分不破凸壁：** Weyl 差分把 $f_4$ 变成三次/二次型后，与 $f_3$、$f_2$ 的已有均值拼合，形式指数恒 $\ge 13/24$；突破 $\beta/2$ 需超出本族的输入（真次弧非对角、与缺项 $g$ 的振荡、或超凸解耦）。

---

## L-Biq-6（已证·结算）— 对 P2 / H 的判决

| 来源 | 可引用上界 | 相对 $N^{1/12}$ |
|------|------------|-----------------|
| L-Dec-2 / L-Hua-2 | $N^{13/24}$ | 缺口 $N^{11/24}$ |
| **L-Biq-3 朴素差分** | $N^{35/48}$ | 更差 |
| **L-Biq-4/5 差分族最优** | $N^{13/24}$（无改进） | 缺口仍 $N^{11/24}$ |
| 假设 H 目标 | $N^{1/12}$ | — |

**判决.**
1. 一次差分多重积分的形式指数已算出：$35/48$（朴素）与 $13/24$（回收华氏）。  
2. **差分不破凸壁**（L-Biq-5）为已证障碍：R6-Biq 族不能改进 L-Dec-2。  
3. 假设 H 仍为未证条件式；H-gap 仍为 $N^{11/24}$。  
4. **不声称**原猜想已证。

---

## 状态汇总

| 编号 | 摘要 | 状态 |
|------|------|------|
| L-Biq-1 | Weyl 一次差分 $\|f_4\|^2\ll P_4\sum_h\|S(h)\|$ | 已证 |
| L-Biq-2 | CS 后多重积分形式；$\,\int\|f_3f_2\|\ll N^{5/12+\varepsilon}$ | 已证 |
| L-Biq-3 | 朴素路径形式指数 $35/48>13/24$ | 已证 |
| L-Biq-4 | 回收 $L^4$ 得 $13/24$；二次差分不优 | 已证 |
| L-Biq-5 | **差分不破凸壁**（族内 $E\ge 13/24$） | 已证（障碍） |
| L-Biq-6 | 结算：不改进 L-Dec；H-gap 仍 $N^{11/24}$ | 已证（结算） |
