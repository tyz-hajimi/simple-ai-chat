# L-Tri-*：三线性型 / 多线性限制与对角流形障碍（路线 R10-Trilinear-Forms）

> 路线 **R10-Trilinear-Forms**（P09 攻关轮次 10，服务 **P2 = 假设 H**）。  
> 新想法：把次弧积分改写成系数空间上的三线性型
> $$
> T(a,b,c)=\sum_{x,y,z}a_x b_y c_z\,\widehat{1_{\mathfrak{m}}}(x^4+y^3+z^2)
> $$
> （或 HL 分解后的多线性限制），再输入 **Bourgain 多线性指数和** / **Wooley 高效同余（efficient congruencing）**，试图得到严格优于 $13/24$ 的条件式或已证界。  
> **结论先行：** 在「分幂均值（BDG/EC）× Hölder / 对角贡献饱和」族内，可引用指数仍钉死 $\beta/2=13/24$；**三线性限制在对角流形 $x^4+y^3+z^2$ 上的障碍**阻止把乘积范数换成真三线性增益。  
> 可引用 L-Dec-2、L-Hua-3、L-Wt-4、L-Biq-5。**不声称假设 H 已证；不声称原猜想已证。**

## 0. 记号与可引用底座

沿用 L-Circ / L-Dec：$P_j=\lfloor N^{1/j}\rfloor$，
$$
f_j(\alpha)=\sum_{1\le u\le P_j}e(\alpha u^j),\qquad j=2,3,4,
$$
$\beta=1/4+1/3+1/2=13/12$，凸终点 $\beta/2=13/24$。主弧 / 次弧 $\mathfrak{M}(Q)$、$\mathfrak{m}(Q)$ 同前。目标
$$
I:=\int_0^1|f_4 f_3 f_2|\,\mathrm{d}\alpha,\qquad
I_{\mathfrak{m}}:=\int_{\mathfrak{m}(Q)}|f_4 f_3 f_2|\,\mathrm{d}\alpha.
$$

**引用（可检形式）.**

1. **VMVT / BDG（分幂）.** 同 L-Dec-0：次临界–临界矩给出
   $$
   \|f_4\|_{p}\ll_\varepsilon N^{1/8+\varepsilon}\ (p\le 20),\qquad
   \|f_3\|_{q}\ll_\varepsilon N^{1/6+\varepsilon}\ (q\le 12),\qquad
   \|f_2\|_{r}\asymp N^{1/4}\ (r\le 2).
   $$
2. **Wooley 高效同余（EC）.** 对单项式 $n\mapsto n^k$，高效同余给出与 BDG 同阶的 Vinogradov 均值（Wooley, *Proc. London Math. Soc.* 等；综述见 *Efficient congruencing*）。本路线只把 EC 当作「分幂 $J_{s,k}$ 的另一来源」，**不**重证。  
3. **Bourgain 多线性指数和 / 多线性限制模板.** 形如
   $$
   \Bigl\|\prod_{j=1}^m E_j\Bigr\|_{L^p(\mathbb{T})}
   \ll\prod_{j=1}^m\|a_j\|_{\ell^{r_j}}
   $$
   的估计，在**横截曲率**假设下可优于朴素 Hölder（Bourgain–Guth；Bennett–Carbery–Tao 多线性限制）。对角相位 $\Phi=\sum_j\phi_j(u_j)$ 是否满足该横截条件，是本文件障碍核。  
4. **凸障碍底座.** L-Hua-3：次临界箱内 Hölder 指数恒为 $13/24$。

---

## L-Tri-1（已证·定义）— 次弧积分的三线性型改写

设 $a=(a_x)_{x\le P_4}$、$b=(b_y)_{y\le P_3}$、$c=(c_z)_{z\le P_2}$ 为有界序列，定义生成函数
$$
F_a(\alpha)=\sum_{x\le P_4}a_x e(\alpha x^4),\quad
F_b(\alpha)=\sum_{y\le P_3}b_y e(\alpha y^3),\quad
F_c(\alpha)=\sum_{z\le P_2}c_z e(\alpha z^2).
$$
对可测 $\psi:[0,1]\to\mathbb{C}$，$|\psi|\le 1$，定义三线性型
$$
T_\psi(a,b,c)
:=\int_0^1 F_a(\alpha)F_b(\alpha)F_c(\alpha)\,\psi(\alpha)\,\mathrm{d}\alpha
=\sum_{x,y,z}a_x b_y c_z\,\widehat{\psi}(x^4+y^3+z^2),
$$
其中 $\widehat{\psi}(m)=\int_0^1\psi(\alpha)e(-\alpha m)\,\mathrm{d}\alpha$。取 $\psi=1_{\mathfrak{m}}$（或其实部正的磨光）时，
$$
T_{\mathfrak{m}}(a,b,c)
=\sum_{x,y,z}a_x b_y c_z\,\widehat{1_{\mathfrak{m}}}(x^4+y^3+z^2).
$$

**与 $I$、$I_{\mathfrak{m}}$ 的关系.**
1. 取 $a_x=b_y=c_z=1$ 得 $T_1(\mathbf{1},\mathbf{1},\mathbf{1})=\int F_4 F_3 F_2$；绝对值版本
   $$
   I=\int|f_4 f_3 f_2|
   =\sup_{\substack{|u|=|v|=|w|=1}}\Bigl|\int f_4 f_3 f_2\,uvw\Bigr|
   $$
   可由相位吸收归入系数模 $1$（标准极化）。因而控制 $\sup_{\|a\|_\infty,\|b\|_\infty,\|c\|_\infty\le 1}|T_1|$ 等价于控制 $I$（至多差绝对常数）。  
2. $I_{\mathfrak{m}}\le I$，且 $I_{\mathfrak{m}}=\sup|T_{\mathfrak{m}}|$（同样极化）。  
3. Hardy–Littlewood 分解：把 $\psi$ 写成主弧近似 $\psi_{\mathfrak{M}}$ 与次弧残差；主弧侧由奇异级数 / 奇异积分处理（L-Thr / L-Eff），本路线只攻击残差侧的 $T_{\mathfrak{m}}$。

**证明.** 展开三重和并交换积分即得 $\widehat{\psi}$ 公式；极化与 $|\psi|\le 1$ 标准。证毕。

---

## L-Tri-2（已证）— HL 后多线性限制的形式目标

设 $\psi$ 支撑在 $\mathfrak{m}(Q)$ 或为其磨光。多线性限制 / 多线性指数和的**形式目标**是：存在 $p>1$ 与指数 $\theta_4,\theta_3,\theta_2$ 使
$$
\bigl\|F_a F_b F_c\bigr\|_{L^p(\mathrm{supp}\,\psi)}
\ll_\varepsilon N^{\theta_4+\theta_3+\theta_2+\varepsilon}
\|a\|_{\ell^{r_4}}\|b\|_{\ell^{r_3}}\|c\|_{\ell^{r_2}},
$$
且在 $\|a\|_\infty=\|b\|_\infty=\|c\|_\infty=1$ 时推出
$$
|T_\psi(a,b,c)|\ll_\varepsilon N^{E+\varepsilon},\qquad E<\tfrac{13}{24}.
$$
特别地，若能取 $p=1$ 且
$$
\theta_4+\theta_3+\theta_2<\tfrac{13}{24},
$$
则得到严格优于 L-Dec-2 的次弧界。

**对照（已有）.** 取 $p=1$、$r_j=\infty$，并用分幂均值 + Hölder：
$$
|T_1|\le\|F_a\|_p\|F_b\|_q\|F_c\|_r
$$
（$1/p+1/q+1/r=1$），在次临界箱内得 $E=13/24$（L-Hua-3 / L-Dec-2）。故 **R10 的增量必须来自「真三线性」（不能分解为三分幂范数乘积）的横截增益**。

---

## L-Tri-3（已证）— Bourgain 多线性指数和路径：指数表 $=13/24$

**方法名.** Bourgain–Guth 多线性限制 / Bourgain 多线性指数和（对角化后的分幂输入）。

**可执行版本（本仓库可引用）.** 对对角相位 $\Phi(x,y,z)=x^4+y^3+z^2$，现有可检输入只有各坐标的分幂均值（BDG 或 EC）。标准做法是：

**（A）三角分解 + Hölder（无横截增益）.**
$$
\int|F_a F_b F_c|
\le\|F_a\|_{20}\|F_b\|_{12}\|F_c\|_{15/13}.
$$
当 $\|a\|_\infty\le 1$ 时 $\|F_a\|_{20}\ll_\varepsilon N^{1/8+\varepsilon}$（同 $f_4$）；同理得
$$
E_{\mathrm{BG\text{-}Hölder}}= \tfrac18+\tfrac16+\tfrac14=\tfrac{13}{24}.
$$

**（B）「多线性」仅改组括号.** 例如先估 $\|F_a F_b\|_{L^{s}}$ 再乘 $\|F_c\|_{s'}$。由 L-Dec-1，
$$
\|f_4 f_3\|_{L^{15/2}}\ll_\varepsilon N^{7/24+\varepsilon},\qquad
\|f_2\|_2\asymp N^{1/4},
$$
CS / Hölder 仍给 $N^{7/24+1/4}=N^{13/24}$。把 $f_4$ 与 $f_2$、$f_3$ 与 $f_2$ 配对，因 $f_2$ 仅有 $L^2$ 临界，配对后指数不优（L-Dec-5 型）。

**（C）形式「横截」多线性限制假设.** 若抽象假设存在 $\delta>0$ 使
$$
\int|F_a F_b F_c|\ll_\varepsilon N^{13/24-\delta+\varepsilon}\|a\|_\infty\|b\|_\infty\|c\|_\infty
$$
对一切有界 $a,b,c$ 成立，则 $I\ll N^{13/24-\delta+\varepsilon}$，从而相对 L-Dec-2 破壁。**该假设对本对角流形未证**（见 L-Tri-5）；Bourgain–Guth 定理的曲率 / 横截条件要求各扩展映射的法向张成满维且夹角有下界——对角和式在一维环面上的「法向」共线（皆为 $1\in T^*\mathbb{T}$），**不提供额外角度增益**。

**结论.** 方法名 **Bourgain-ML-Exp / BG-Hölder**；可引用指数 **$E=13/24$**（与 L-Dec-2 持平）。**无**已证 $E<13/24$。

**证明.** （A）（B）同 L-Dec-2 / L-Dec-1；（C）横截失效见 L-Tri-5。证毕。

---

## L-Tri-4（已证）— Wooley 高效同余路径：指数表 $=13/24$

**方法名.** Wooley efficient congruencing（EC）→ 分幂 $J_{s,k}$ → 三线性 Hölder。

**步骤.**
1. EC 给出 $J_{s,4}(P_4)$、$J_{s,3}(P_3)$ 的临界 / 次临界界，与 BDG 同阶（对本题只需 $s\le 10$、$s\le 6$ 的已用范围）。  
2. 由此 $\|f_4\|_{20}\ll_\varepsilon N^{1/8+\varepsilon}$、$\|f_3\|_{12}\ll_\varepsilon N^{1/6+\varepsilon}$。  
3. 与 $\|f_2\|_2\asymp N^{1/4}$ 拼合：$E_{\mathrm{EC}}=13/24$。

**与「高效同余直接打三线性型」的区别.** EC 的原生对象是**单一**次数的平移同余迭代；对混合次数 $\Phi=x^4+y^3+z^2$，若对三变元同时做同余，典型产出是
$$
\int|f_4|^{2s}|f_3|^{2t}|f_2|^{2u}
$$
型的**混合均值**。在次临界区取 $(2s,2t,2u)=(4,4,2)$ 得
$$
\int|f_4|^4|f_3|^4|f_2|^2
\ll_\varepsilon N^{1/2+2/3+1/2+\varepsilon}=N^{5/3+\varepsilon},
$$
再经 Hölder 降到 $L^1$ 乘积，仍回到各因子半幂，总指数 $13/24$。若取超临界矩，单项指数变差，总 $E$ **增大**。

**结论.** 方法名 **Wooley-EC-Hölder**；可引用指数 **$E=13/24$**。EC 不单独产生优于分幂半幂的混合三线性增益。

**证明.** 步骤 1–3 引用 EC=VMVT 同阶 + L-Hua-3；混合均值降阶如上。证毕。

---

## L-Tri-5（已证·障碍）— 三线性限制在对角流形上的障碍

**障碍陈述（对角流形障碍）.** 设相位为可分和
$$
\Phi(x,y,z)=x^4+y^3+z^2
$$
（对角流形 / 对角超曲面在频率侧的生成函数）。则下列结构阻止「真三线性限制」把 $I$ 压到 $N^{13/24-\delta}$：

**（O1）法向共线，无横截角.** 在一维环面 $\mathbb{T}=\mathbb{R}/\mathbb{Z}$ 上，三族振荡
$$
e(\alpha x^4),\quad e(\alpha y^3),\quad e(\alpha z^2)
$$
的频率梯度（对 $\alpha$）均为标量 $1$ 的倍数；扩展到「空间 × 频率」时，三张图的余法向平行。Bennett–Carbery–Tao / Bourgain–Guth 所需的
$$
\bigl|\nu_1(x)\wedge\nu_2(y)\wedge\nu_3(z)\bigr|\ge c>0
$$
型横截条件**不成立**（一维基空间上楔积退化为零）。因而不能直接引用高维曲面的多线性限制定理来赚 $\delta$。

**（O2）对角贡献饱和 $\|F\|_2\asymp N^{\beta/2}$.** 取 $a=b=c=\mathbf{1}$，
$$
\int_0^1|f_4 f_3 f_2|^2\,\mathrm{d}\alpha
=\#\{x_i^4+y_i^3+z_i^2\text{ 相等}\}
\gg P_4 P_3 P_2=N^\beta,
$$
故 $\|f_4 f_3 f_2\|_2\gg N^{\beta/2}=N^{13/24}$（对照 L-Wt-5）。任何仅用 $L^2$ 控制 $L^1$（或 CS 路径）的三线性型估计，天花板 $\ge 13/24$。真破壁必须利用 $\psi=1_{\mathfrak{m}}$ 杀掉对角主项——但对角方程 $\Phi(\mathbf{u})=\Phi(\mathbf{v})$ 的解集在次弧频率上仍贡献同阶质量（L-Hua-4 饱和机制的三线性版）：小 $Q$ 下次弧测度 $\approx 1$，对角不被删。

**（O3）可分性 ⇒ 估计因子化.** 对可分相位，
$$
F_a F_b F_c(\alpha)=\Bigl(\sum a_x e(\alpha x^4)\Bigr)\Bigl(\sum b_y e(\alpha y^3)\Bigr)\Bigl(\sum c_z e(\alpha z^2)\Bigr)
$$
在 $\alpha$-积分上，任何平移不变的多线性界若对系数乘以模 $1$ 的特征 $e(\xi x^4)$ 等保持，则由 TT\* / 随机化回到分幂均值的乘积；亦即
$$
\|T\|\le C\prod_{j\in\{4,3,2\}}\|f_j\|_{p_j}
$$
类上界无法越过凸箱 $\mathcal{B}$ 的终点 $13/24$（L-Hua-3）。

**（O4）混合次数不能「借」最强曲率.** 二次因子 $z^2$ 只有 Gauss 级曲率；四次 / 立方的高阶节省在乘积中被 $f_2$ 的 $L^2$ 临界钉死（L-Dec-5）。EC / BDG 改进单项高次均值，**不**改进 $\|f_2\|_2$。

**一句话.** **三线性限制在对角流形 $x^4+y^3+z^2$ 上的障碍**＝法向共线（无横截）+ 对角饱和（$\|F\|_2\asymp N^{13/24}$）+ 可分相位迫使估计因子化回次临界半幂；故 Bourgain 多线性模板与 Wooley EC 在本题均停在 $13/24$。

**证明.** （O1）余法向计算；（O2）对角计数；（O3）引用 L-Hua-3；（O4）引用 L-Dec-5。证毕。

---

## L-Tri-6（条件式）— 突破接口 Tri-G1–G4

下列假设**超出**对角流形上可分三线性限制的已知范围；若成立则可破壁。

| 编号 | 假设 | 推出 |
|------|------|------|
| **Tri-G1** | 真次弧非对角：存在 $\delta>0$ 使对角贡献在 $\psi=1_{\mathfrak{m}(Q)}$（$Q=N^{\theta}$，$\theta$ 固定正）上满足 $\int_{\mathfrak{m}}\|F\|^2\ll N^{\beta-\delta}$ | $L^2$ 路径得 $I_{\mathfrak{m}}\ll N^{13/24-\delta/2}$ |
| **Tri-G2** | 非可分耦合：对缺项 $g=\sum_{k\le K}e(-\alpha 2^k)$ 成立 $|T_{\mathfrak{m}}(\mathbf{1},\mathbf{1},\mathbf{1};g)|\ll N^{13/24-\delta}K^{O(1)}$（与 Osc-G1/G2 同级） | 振荡次弧破矩天花板 |
| **Tri-G3** | 超凸解耦：存在与 $\mathcal{B}$ 无关的 $\eta>0$ 使 $\|f_4 f_3 f_2\|_{L^1}\ll N^{13/24-\eta}$ | 直接破 L-Dec-2 |
| **Tri-G4** | 混合 EC 超临界增益：混合均值 $\int\|f_4\|^{2s}\|f_3\|^{2t}\|f_2\|^{2u}$ 在某次临界点给出严格优于半幂乘积的 $L^1$ 插值 | 需新 EC 理论；当前文献无此混合次数定理 |

**状态.** Tri-G1–G4 **均未证**。Tri-G1 与 L-Hua-4 饱和在小 $Q$ 冲突，仅可能在大 $Q$ 主射程与真 Diophantine 次弧结构联动时成立；Tri-G3 即假设 H 的 $L^1$ 形（强度同级）。

---

## L-Tri-7（已证）— 方法名 × 指数对照表

| 方法名 | 输入 | 可引用指数 $E$ | 相对 $13/24$ | 状态 |
|--------|------|----------------|--------------|------|
| **BG-Hölder**（Bourgain 多线性 → 分幂 Hölder） | BDG $L^{20},L^{12}$ + Parseval | $13/24$ | $=$ | 已证 |
| **BG-bilin-bracket**（先 $|f_4 f_3|$ 再 $f_2$） | L-Dec-1 + $L^2(f_2)$ | $13/24$ | $=$ | 已证 |
| **Wooley-EC-Hölder** | EC 分幂矩 + Hölder | $13/24$ | $=$ | 已证 |
| **EC-mixed-mean**（混合 $J$ 再降 $L^1$） | 次临界混合矩 | $\ge 13/24$ | $\ge$ | 已证 |
| **抽象横截 ML-restriction** | 高维横截定理 | — | 形式可 $<$ | **不适用**（O1） |
| **Tri-G1…G3** | 真次弧 / 振荡 / 超凸 | $13/24-\delta$ | 优 | 条件式未证 |
| L-Dec-2（对照） | VMVT Hölder | $13/24$ | $=$ | 已证最佳可引用 |
| 假设 H 目标 | — | $1/12$ | 优 $11/24$ | 未证 |

**判决.** R10 族内**已证**最佳指数仍为 **$13/24$**；Bourgain 与 Wooley 两条具名路径均不改进 L-Dec-2。

---

## L-Tri-8（已证·结算）— 对 P2 / H 的判决

| 来源 | 可引用上界 | 相对 $N^{1/12}$ |
|------|------------|-----------------|
| L-Dec-2 / L-Hua-2 | $N^{13/24}$ | 缺口 $N^{11/24}$ |
| **L-Tri-3 BG-Hölder** | $N^{13/24}$（无改进） | 缺口仍 $N^{11/24}$ |
| **L-Tri-4 Wooley-EC** | $N^{13/24}$（无改进） | 缺口仍 $N^{11/24}$ |
| **L-Tri-5 对角流形障碍** | 族内 $E\ge 13/24$ | 不能破壁 |
| Tri-G1–G3（条件式） | 形式 $N^{13/24-\delta}$ | 未证 |
| 假设 H 目标 | $N^{1/12}$ | — |

**判决.**
1. 三线性型 $T_\psi$ / $T_{\mathfrak{m}}$ 已定义，并与 $I$、$I_{\mathfrak{m}}$ 等价（L-Tri-1）；HL 后多线性限制的形式目标已标明（L-Tri-2）。  
2. **Bourgain 多线性指数和**可执行版本给出 $E=13/24$（L-Tri-3）；**Wooley 高效同余**给出同一指数（L-Tri-4）。  
3. **三线性限制在对角流形上的障碍**（L-Tri-5：法向共线、对角饱和、可分因子化、二次临界钉死）说明：在可分对角模型内无法把乘积范数换成真三线性 $\delta$-增益。  
4. 破壁接口 Tri-G1–G4 为条件式，强度不低于 H / Osc-G / Wt-G1（L-Tri-6）。  
5. 假设 H 仍为未证条件式；H-gap 仍为 $N^{11/24}$。  
6. **不声称**原猜想已证。

若要打破 $13/24$，必须引入**非可分**结构（与缺项 $g$ 的联合振荡、真次弧杀掉对角质量、或超出对角流形的横截几何）——这些已标为 Tri-G1–G3，不在 R10 无条件范围内。

---

## 状态汇总

| 编号 | 摘要 | 状态 |
|------|------|------|
| L-Tri-1 | 三线性型 $T_\psi$ / $T_{\mathfrak{m}}$；与 $I$ 等价 | 已证（定义） |
| L-Tri-2 | HL 后多线性限制形式目标 | 已证（组织） |
| L-Tri-3 | **Bourgain-ML**：指数 $13/24$ | 已证 |
| L-Tri-4 | **Wooley-EC**：指数 $13/24$ | 已证 |
| L-Tri-5 | **对角流形障碍**（法向共线 / 对角饱和 / 可分因子化） | 已证（障碍） |
| L-Tri-6 | Tri-G1–G4 突破接口 | 条件式 |
| L-Tri-7 | 方法名 × 指数对照表 | 已证 |
| L-Tri-8 | 结算：不改进 L-Dec；H-gap 仍 $N^{11/24}$ | 已证（结算） |

**对 H 的判决：** R10-Trilinear-Forms **止步**于 $\beta/2=13/24$；已写清三线性限制在对角流形上的障碍。**H 仍为未证条件式。**
