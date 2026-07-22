# L-Dec-*：双线性/三线性解耦与次弧拼合（路线 R1-Bilinear-Decouple）

> 服务目标：**P2 = 假设 H**（次弧 $\int_{\mathfrak{m}}|f_4 f_3 f_2|\ll n^{1/12-\delta}$）。  
> 本文件为**新路线**：视 $|f_4 f_3|$ 为双线性形式，用 Bourgain–Demeter–Guth / Vinogradov 均值给出可引用 $L^p$ 界，再与 $f_2$ 的 Gauss 节省拼合。  
> 状态标记：`已证` / `缺口`。**不声称假设 H 已证；不声称原猜想已证。**

## 0. 记号与引用底座

沿用 L-Circ：$P_j=\lfloor N^{1/j}\rfloor$，
$$
f_j(\alpha)=\sum_{1\le u\le P_j}e(\alpha u^j),\qquad j=2,3,4,
$$
主弧 $\mathfrak{M}(Q)$、次弧 $\mathfrak{m}(Q)$ 按标准宽度 $Q/(qN)$（$1\le Q\le N^{1/2}$）。记 $\beta=1/4+1/3+1/2=13/12$。

**引用（可检形式）.**

1. **Vinogradov 均值定理（VMVT / BDG）.** 对整数 $k\ge 2$、$s\ge 1$、$X\ge 1$，
   $$
   J_{s,k}(X):=\int_0^1\Bigl|\sum_{n\le X}e(\alpha n^k)\Bigr|^{2s}\mathrm{d}\alpha
   \ll_\varepsilon X^{s+\varepsilon}+X^{2s-\frac{k(k+1)}{2}+\varepsilon}.
   $$
   出处：Bourgain–Demeter–Guth, *Ann. of Math.* **184** (2016)；等价形式见 Wooley 高效同余法综述。  
   特例：$J_{10,4}(P_4)\ll_\varepsilon P_4^{10+\varepsilon}$，$J_{6,3}(P_3)\ll_\varepsilon P_3^{6+\varepsilon}$；次临界 $J_{2,4}(P_4)\ll_\varepsilon P_4^{2+\varepsilon}$，$J_{2,3}(P_3)\ll_\varepsilon P_3^{2+\varepsilon}$。

2. **二次 Gauss 次弧点态（L-Circ-7）.** $\alpha\in\mathfrak{m}(Q)$ 时
   $$
   |f_2(\alpha)|\ll N^{1/2}Q^{-1/2}(\log 2N)^{1/2}.
   $$

3. **Parseval.** $\int_0^1|f_2|^2=P_2\asymp N^{1/2}$，故 $\|f_2\|_{L^2([0,1])}\asymp N^{1/4}$；对 $1\le r\le 2$ 有 $\|f_2\|_r\le\|f_2\|_2$。

---

## L-Dec-1（已证）— $|f_4 f_3|$ 的临界双线性均值

对任意 $\varepsilon>0$，
$$
\int_0^1|f_4(\alpha)f_3(\alpha)|^{15/2}\,\mathrm{d}\alpha\ll_\varepsilon N^{35/16+\varepsilon}.
$$
等价地
$$
\|f_4 f_3\|_{L^{15/2}([0,1])}\ll_\varepsilon N^{7/24+\varepsilon}.
$$

**证明.** Hölder：取共轭 $a=20/p$、$b=12/p$，并令 $p=15/2$，则 $1/a+1/b=p/20+p/12=1$，且
$$
\int|f_4 f_3|^p
\le\Bigl(\int|f_4|^{20}\Bigr)^{p/20}\Bigl(\int|f_3|^{12}\Bigr)^{p/12}
=\bigl(J_{10,4}(P_4)\bigr)^{3/8}\bigl(J_{6,3}(P_3)\bigr)^{5/8}.
$$
由 VMVT：$J_{10,4}(P_4)\ll_\varepsilon P_4^{10+\varepsilon}=N^{5/2+\varepsilon}$，$J_{6,3}(P_3)\ll_\varepsilon P_3^{6+\varepsilon}=N^{2+\varepsilon}$。故
$$
\int|f_4 f_3|^{15/2}
\ll_\varepsilon N^{(5/2)\cdot(3/8)+(2)\cdot(5/8)+\varepsilon}
=N^{15/16+5/4+\varepsilon}=N^{35/16+\varepsilon}.
$$
取 $L^{15/2}$ 范数：指数 $(35/16)\cdot(2/15)=7/24$。证毕。

**注.** 同法得 $L^2$ 界：由 CS 与次临界 VMVT，
$$
\int|f_4|^2|f_3|^2\le\bigl(J_{2,4}(P_4)\bigr)^{1/2}\bigl(J_{2,3}(P_3)\bigr)^{1/2}
\ll_\varepsilon P_4 P_3\,N^\varepsilon=N^{7/12+\varepsilon},
$$
即 $\|f_4 f_3\|_2\ll_\varepsilon N^{7/24+\varepsilon}$，与临界 $L^{15/2}$ 上界同阶。因而**单靠提高 $|f_4 f_3|$ 的可积指数，在全环面 $L^1$ 层面不改进 Cauchy–Schwarz**。

---

## L-Dec-2（已证）— 三线性 Hölder + VMVT（全环面）

对任意 $\varepsilon>0$，
$$
\int_0^1|f_4 f_3 f_2|\,\mathrm{d}\alpha
\ll_\varepsilon N^{13/24+\varepsilon}.
$$
特别地，对任意 $Q$，
$$
\int_{\mathfrak{m}(Q)}|f_4 f_3 f_2|\,\mathrm{d}\alpha
\ll_\varepsilon N^{13/24+\varepsilon}.
$$

**证明.** 取 Hölder 指数 $(u,v,w)=(20,12,15/13)$（因 $1/20+1/12+13/15=1$）。则
$$
\int|f_4 f_3 f_2|
\le\|f_4\|_{20}\|f_3\|_{12}\|f_2\|_{15/13}.
$$
由 L-Dec-1 的 VMVT 特例：
$$
\|f_4\|_{20}=\bigl(J_{10,4}(P_4)\bigr)^{1/20}\ll_\varepsilon P_4^{1/2+\varepsilon}=N^{1/8+\varepsilon},
$$
$$
\|f_3\|_{12}=\bigl(J_{6,3}(P_3)\bigr)^{1/12}\ll_\varepsilon P_3^{1/2+\varepsilon}=N^{1/6+\varepsilon}.
$$
又 $15/13\le 2$，故 $\|f_2\|_{15/13}\le\|f_2\|_2\asymp N^{1/4}$。相乘得
$$
N^{1/8+1/6+1/4+\varepsilon}=N^{3/24+4/24+6/24+\varepsilon}=N^{13/24+\varepsilon}.
$$
限制到 $\mathfrak{m}(Q)$ 只减小积分区域。证毕。

**对照.** $13/24=\beta/2$：本界恰为凸性指数的平方根尺度，是「临界矩 + Hölder」方法族的自然终点。

---

## L-Dec-3（已证）— 与 Gauss 点态的凸插值族

设 $0\le\theta\le 1$，$1\le Q\le N^{1/4}$。则对任意 $\varepsilon>0$，
$$
\int_{\mathfrak{m}(Q)}|f_4 f_3 f_2|
\ll_\varepsilon N^{2/3-\theta/8+\varepsilon}\,Q^{-(1-\theta)/8}(\log 2N)^{(1-\theta)/2}.
$$
端点：
- $\theta=0$：回到 L-Circ-8 第三项 $N^{2/3+\varepsilon}Q^{-1/8}$；
- $\theta=1$：回到 L-Dec-2 的 $N^{13/24+\varepsilon}$（与 $Q$ 无关）。

**证明.** 写 $|f_4|=|f_4|^{1-\theta}|f_4|^\theta$。由 L-Circ-8 型 Weyl（$j=4$，$\alpha\in\mathfrak{m}(Q)$，$Q\le P_4$）
$$
|f_4(\alpha)|\ll_\varepsilon P_4^{1+\varepsilon}Q^{-1/8}=N^{1/4+\varepsilon}Q^{-1/8},
$$
故
$$
\int_{\mathfrak{m}}|f_4 f_3 f_2|
\le\|f_4\|_{L^\infty(\mathfrak{m})}^{1-\theta}
\int_0^1|f_4|^\theta|f_3||f_2|.
$$
对后一积分用 Hölder，指数满足 $\theta/20+1/12+1/w=1$，即 $w=60/(55-3\theta)\in[12/11,15/13]\subset(1,2]$。则
$$
\int|f_4|^\theta|f_3||f_2|
\le\|f_4\|_{20}^\theta\|f_3\|_{12}\|f_2\|_w
\ll_\varepsilon N^{\theta/8+1/6+1/4+\varepsilon}.
$$
乘上 $\|f_4\|_\infty^{1-\theta}\ll_\varepsilon\bigl(N^{1/4}Q^{-1/8}\bigr)^{1-\theta}(\log)^{O(1)}$，总指数为
$$
\frac{1-\theta}{4}+\frac{\theta}{8}+\frac{1}{6}+\frac{1}{4}=\frac{2}{3}-\frac{\theta}{8},
$$
$Q$ 幂为 $-(1-\theta)/8$。证毕。

**优化（固定 $Q=N^{1/4}$）.** 指数函数
$$
\frac{2}{3}-\frac{\theta}{8}-\frac{1-\theta}{32}=\frac{2}{3}-\frac{1}{32}-\frac{3\theta}{32}
$$
对 $\theta$ **严格递减**，故本族最优在 $\theta=1$，给出 $N^{13/24+\varepsilon}$。Gauss 点态在本插值族中**不能**击败纯 VMVT 端点。

---

## L-Dec-4（已证）— 拼合结算：次弧积分指数与 H-缺口

取 $Q=N^{1/4}$（与 L-Circ-8 同一主射程）。则

| 来源 | 次弧积分上界（略 $\varepsilon,\log$） | 相对 $N^{1/12}$ 的缺口 |
|------|--------------------------------------|------------------------|
| L-Circ-8 最优 | $N^{61/96}$ | $N^{53/96}$ |
| **L-Dec-2 / L-Dec-3($\theta=1$)** | **$N^{13/24}=N^{52/96}$** | **$N^{11/24}=N^{44/96}$** |
| 假设 H 目标 | $N^{1/12}=N^{8/96}$ | $1$ |

具体算术：
$$
\frac{13}{24}-\frac{1}{12}=\frac{13}{24}-\frac{2}{24}=\frac{11}{24}=\frac{44}{96},
$$
$$
\frac{61}{96}-\frac{52}{96}=\frac{9}{96}=\frac{3}{32}.
$$
即：相对 L-Circ-8，本路线把可引用次弧指数从 $61/96$ **改进到** $13/24$，缺口由 $53/96$ **缩小到** $11/24$；仍差因子 $N^{11/24}$，**不足以推出假设 H**。

**结构原因（缺口说明，非否证）.** 临界对角贡献使
$$
\int_{\mathfrak{m}}|f_k|^{2s_{\mathrm{crit}}}\asymp\int_0^1|f_k|^{2s_{\mathrm{crit}}}
$$
（对角项对 $\alpha$ 均匀），故次弧截断在临界矩层面**不产生额外幂次节省**；L-Dec-2 已是「BDG 临界矩 + 三线性 Hölder」在本符号下的终点，与 $\beta/2=13/24$ 对齐。若要继续压缩 $11/24$，需超出本方法族的输入（例如真次弧上的非对角结构、或与 $2^k$ 缺项 $g$ 的联合估计 H′/Lac）。

---

## L-Dec-5（已证）— 与 $f_2$ 的 $L^q$（$q\ge 2$）Gauss 插值不改进 $13/24$

设 $q\in[2,\infty]$，$p=q/(q-1)\in[1,2]$，$\alpha\in\mathfrak{m}(Q)$。由 $L^2$–$L^\infty$ 插值与 L-Circ-7，
$$
\|f_2\|_{L^q(\mathfrak{m})}
\ll\bigl(N^{1/2}Q^{-1/2}\bigr)^{1-2/q}N^{1/(2q)}(\log 2N)^{O(1)}.
$$
若仅用 $\|f_4 f_3\|_p\le\|f_4 f_3\|_2\ll_\varepsilon N^{7/24+\varepsilon}$（L-Dec-1 注），则
$$
\int_{\mathfrak{m}}|f_4 f_3 f_2|
\le\|f_4 f_3\|_p\|f_2\|_q
\ll_\varepsilon N^{13/24+\theta/4+\varepsilon}Q^{-\theta/2},
$$
其中 $\theta=1-2/q\in[0,1]$。于 $Q=N^{1/4}$ 指数为 $13/24+\theta/8\ge 13/24$，**恒不优于** L-Dec-2。

**证明.** 直接代入 $\theta=1-2/q$：$N$ 幂为
$$
\frac{7}{24}+\frac{\theta}{2}+\frac{1-\theta}{4}=\frac{13}{24}+\frac{\theta}{4},
$$
再减 $Q$ 贡献 $\theta/2\cdot(1/4)=\theta/8$。证毕。

---

## 状态汇总

| 编号 | 摘要 | 状态 |
|------|------|------|
| L-Dec-1 | $\int|f_4 f_3|^{15/2}\ll N^{35/16+\varepsilon}$ | 已证（引 BDG/VMVT） |
| L-Dec-2 | $\int|f_4 f_3 f_2|\ll N^{13/24+\varepsilon}$（含次弧） | 已证 |
| L-Dec-3 | Weyl–VMVT 凸族；最优端点即 L-Dec-2 | 已证 |
| L-Dec-4 | 拼合后指数 $13/24$，距 $1/12$ 差 $11/24$ | 已证（结算） |
| L-Dec-5 | Gauss $L^q$（$q\ge 2$）插值不改进 $13/24$ | 已证 |

**对 H 的判决：** 本路线将 H-gap 从 $N^{53/96}$ 缩至 $N^{11/24}$，**H 仍为未证条件式**。
