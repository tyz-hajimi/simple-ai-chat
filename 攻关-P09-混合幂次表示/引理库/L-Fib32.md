# L-Fib32-*：$(3,2)$-纤维阈值与 $f_4$-卷积（路线 R11-Fiber-32-Threshold）

> 路线 **R11-Fiber-32-Threshold**（P09 攻关轮次 11；对抗审查 R10 建议；服务 **P2 旁路 / 阈值弱化**，兼对接 L-Thr 的 $\mathrm{H}_{\mathrm{thr}}$）。  
> 新角度：先对固定 $x$（或对 $x^4$ 求和后）把问题降为
> $$
> t=y^3+z^2
> $$
> 的表示；再在圆法中把 $f_4$ **留在**主弧/次弧分解**之外**，对 $H:=f_3f_2$ 做 DH 型主/次弧分析，最后与 $f_4$ 卷积。  
> **总判决（一句话）.** 「多数 $t$ 上 $\mathfrak{S}_{3,2}(t)$ 不太小 $\Rightarrow t=y^3+z^2$」**假**（$\beta_{3,2}=5/6<1$，密度零；对照 L-CRB-2）；可检验的卷积主项把纤维和抬回 $m^{1/12}$，但次弧用 $L^2(f_4)\times L^2(H)$ **恰回收**全混合凸壁 $13/24$，**不**无条件绕开 L-Dec-2。破壁需 Fib32-G1–G3（纤维次弧真节省）。  
> **不**声称假设 H、$\mathrm{H}_{\mathrm{thr}}$、原猜想已证。禁止数值程序。

---

## 0. 符号

沿用：$P_j=\lfloor m^{1/j}\rfloor$（$j=2,3,4$），
$$
f_j(\alpha)=\sum_{1\le u\le P_j}e(\alpha u^j),\qquad
F=f_4f_3f_2,\qquad
H:=f_3f_2.
$$
全混合指数 $\beta=1/4+1/3+1/2=13/12$，凸终点 $\beta/2=13/24$。  
$(3,2)$-纤维指数
$$
\beta_{3,2}=\tfrac13+\tfrac12=\tfrac56,\qquad
\frac{\beta_{3,2}}{2}=\tfrac{5}{12}.
$$
纤维表示函数与混合表示函数
$$
\begin{aligned}
r_{3,2}(t)
&=\sum_{\substack{y\le P_3\\ z\le P_2\\ y^3+z^2=t}}1
=\int_0^1 H(\alpha)\,e(-t\alpha)\,\mathrm{d}\alpha,\\
r(m)
&=\sum_{\substack{x\le P_4\\ y\le P_3\\ z\le P_2\\ x^4+y^3+z^2=m}}1
=\int_0^1 F(\alpha)\,e(-m\alpha)\,\mathrm{d}\alpha.
\end{aligned}
$$
局部密度：$\sigma_p^{(3,2)}(t)$、$\mathfrak{S}_{3,2}(t)=\prod_p\sigma_p^{(3,2)}(t)$ 为形 $y^3+z^2$ 的奇异级数；全混合 $\mathfrak{S}(m)$、$\mathfrak{J}(m)$ 同 L-Thr。

主弧/次弧：本路线默认对 **$H$**（而非 $F$）取 Farey 剖分参数 $Q$，写
$$
\mathfrak{M}_{3,2}(Q),\qquad
\mathfrak{m}_{3,2}(Q)=[0,1)\setminus\mathfrak{M}_{3,2}(Q),
$$
并分解 $H=H_{\mathfrak{M}}+H_{\mathfrak{m}}$（积分限制在对应集合上）。$f_4$ **不**参与该剖分的定义。

---

## L-Fib32-1（已证）— 离散卷积恒等式与纤维重写

**引理.** 对一切 $m\ge 1$，
$$
r(m)
=\sum_{x\le P_4}r_{3,2}(m-x^4)
=\int_0^1 f_4(\alpha)\,H(\alpha)\,e(-m\alpha)\,\mathrm{d}\alpha.
$$
（约定 $t<0$ 时 $r_{3,2}(t)=0$；箱截断与 $\mathbb{N}_0$ 无截断差 $O(m^\varepsilon)$ 边界项，同 L-Thr。）

**证明.** 把 $r(m)$ 按 $x$ 分层即得第一式。第二式：
$$
\sum_{x\le P_4}r_{3,2}(m-x^4)
=\sum_{x\le P_4}\int_0^1 H(\alpha)\,e\bigl(-(m-x^4)\alpha\bigr)\,\mathrm{d}\alpha
=\int_0^1\Bigl(\sum_{x\le P_4}e(\alpha x^4)\Bigr)H(\alpha)\,e(-m\alpha)\,\mathrm{d}\alpha.
$$
证毕。

**组织含义.** 「固定 $x$ 看 $m-x^4=y^3+z^2$」与「对 $x^4$ 求和后再看」在计数上等价于同一卷积；圆法上对应**保留** $f_4$ 为外因子、只对 $H$ 做主/次弧。

---

## L-Fib32-2（已证·否证）— 纯 $(3,2)$-阈值「多数 $t$」为假

**错误断言（Fiber-False）.** 存在 $A<\infty$ 与密度 $1$ 的集合 $\mathcal{T}$，使一切充分大 $t\in\mathcal{T}$ 满足
$$
\mathfrak{S}_{3,2}(t)\ge(\log t)^{-A}
\quad\Longrightarrow\quad
t=y^3+z^2\text{ 对某 }y,z\in\mathbb{N}_0.
$$

**定理（否证）.** Fiber-False **不成立**。更强地：像集
$$
\mathcal{S}=\{y^3+z^2:y,z\in\mathbb{N}_0\}
$$
满足 $\#(\mathcal{S}\cap[1,X])\ll X^{5/6}$（L-CRB-2 箱计数），故几乎所有 $t$ **不可**写成 $y^3+z^2$，无论 $\mathfrak{S}_{3,2}(t)$ 是否「不太小」。

**补充（奇异积分尺度）.** 形 $y^3+z^2$ 的连续主项核满足启发式
$$
\mathfrak{J}_{3,2}(t)\asymp t^{\beta_{3,2}-1}=t^{-1/6}\to 0,
$$
故即便局部密度有下界，主项 $\mathfrak{S}_{3,2}\mathfrak{J}_{3,2}$ **趋向零**，不能支撑「几乎所有」或「多数 + 阈值」叙事。Davenport–Heilbronn 处理的是 $\beta>1$ 的三元形（L-CRB-1：两平方+立方 / 一平方+两立方），**不是** $\beta_{3,2}=5/6$ 的二元形。

**判决.** 路线不得写成「先证 $(3,2)$-阈值再对 $x$ 平均」；必须保留**对 $x$ 的求和/卷积**，用 $\asymp m^{1/4}$ 条纤维把 $t^{-1/6}$ 抬回 $m^{1/12}$（见 L-Fib32-4）。

---

## L-Fib32-3（已证·组织）— 留 $f_4$ 于剖分外的圆法分裂

**定义.** 固定剖分 $Q=Q(m)\ge 1$，令
$$
\begin{aligned}
r^{\mathrm{fib}}_{\mathfrak{M}}(m)
&:=\int_{\mathfrak{M}_{3,2}(Q)}f_4(\alpha)\,H(\alpha)\,e(-m\alpha)\,\mathrm{d}\alpha,\\
r^{\mathrm{fib}}_{\mathfrak{m}}(m)
&:=\int_{\mathfrak{m}_{3,2}(Q)}f_4(\alpha)\,H(\alpha)\,e(-m\alpha)\,\mathrm{d}\alpha.
\end{aligned}
$$
则 $r(m)=r^{\mathrm{fib}}_{\mathfrak{M}}(m)+r^{\mathrm{fib}}_{\mathfrak{m}}(m)$。

**与全混合分裂的区别.**
| 对象 | 剖分作用在 | 次弧假设形 |
|------|------------|------------|
| L-Thr / L-Dec | $F=f_4f_3f_2$ | $\mathrm{H}_{\mathrm{thr}}$ / H：$\int_{\mathfrak{m}}|F|$ |
| 本路线 | 仅 $H=f_3f_2$；$f_4$ 外置 | 纤维次弧：$\lvert r^{\mathrm{fib}}_{\mathfrak{m}}\rvert$ 或 $\int_{\mathfrak{m}_{3,2}}|f_4 H|$ |

**可执行策略.**  
1. 在 $\mathfrak{M}_{3,2}$ 上用完整 Gauss 和近似 $f_3,f_2$，得 $H$ 的 DH 型主弧展开；  
2. 对 $\alpha$ 积分后与 $f_4$ 卷积，期望主项 $\asymp\mathfrak{S}(m)\,m^{1/12}$（L-Fib32-4）；  
3. 次弧误差单独用纤维估计（L-Fib32-5），**允许**弱于全混合 $\mathrm{H}_{\mathrm{thr}}$ 的点态输入，但须强到能吃掉主项。

---

## L-Fib32-4（已证·可检验卷积主项）— 纤维和的启发式主项尺度

### （A）单纤维尺度（已证计数）

对 $1\le t\le m$，
$$
\sum_{t\le m}r_{3,2}(t)
=\#\{(y,z):y^3+z^2\le m\}
\asymp m^{5/6},
$$
故「平均」$r_{3,2}(t)$ 的 $L^1$-均值 $\asymp t^{-1/6}$。特别地**不**存在绝对常数 $c>0$ 使几乎所有 $t$ 有 $r_{3,2}(t)\ge c$（与 L-Fib32-2 一致）。

### （B）与四次的卷积主项（已证尺度同构）

**引理（卷积尺度）.** 记形式主项
$$
\mathcal{M}(m)
:=\sum_{x\le P_4}\mathfrak{S}_{3,2}(m-x^4)\,(m-x^4)_+^{\beta_{3,2}-1}.
$$
若对「局部密度在 $x$ 上缓变」作标准 Euler 积拼合（与 L-Thr-1 同一框架：截断奇异级数 + 积尾），则存在绝对 $c_{\mathcal{M}},C_{\mathcal{M}}>0$ 使当 $\mathfrak{S}(m)\gg 1$ 时启发式
$$
c_{\mathcal{M}}\,\mathfrak{S}(m)\,m^{1/12}
\le
\mathcal{M}(m)
\le
C_{\mathcal{M}}\,\mathfrak{S}(m)\,m^{1/12}
$$
在忽略 $o(m^{1/12})$ 的光滑误差下成立。粗算：
$$
\#\{x\le P_4\}\cdot m^{-1/6}
\asymp
m^{1/4}\cdot m^{-1/6}
=m^{1/12}.
$$

**可检验陈述（卷积引理 · 主弧半边）.** 存在 $\theta_1\in(0,1/12)$、$c_1>0$，使得当 $1\le Q\le m^{\theta_1}$ 且 $\mathfrak{S}(m)\ge(\log m)^{-A}$ 时，对充分大 $m$，
$$
\bigl|r^{\mathrm{fib}}_{\mathfrak{M}(Q)}(m)
-
\mathfrak{S}(m)\,\mathfrak{J}(m)\bigr|
\ll_A
m^{1/12}Q^{-\delta_1}
+m^{1/12-\eta_1}
$$
（$\delta_1,\eta_1>0$ 绝对）。因而
$$
r^{\mathrm{fib}}_{\mathfrak{M}(Q)}(m)
\gg_A
\frac{m^{1/12}}{(\log m)^{A}}.
$$

**证明概要.** 在每条 $(3,2)$-主弧上用 Gauss 和替换 $f_3,f_2$；对 $\beta$ 积分给出纤维奇异积分片；对 $a/q$ 求和给出截断 $\mathfrak{S}_{3,2}$。再与 $f_4$ 的主弧/完整和卷积：因四次完整和在同一 Farey 邻域与全混合主弧展开兼容（L-Thr-1(B) 的 $f_4$ 因子），拼合后奇异级数升为全混合 $\mathfrak{S}(m)$，奇异积分升为 $\mathfrak{J}(m)\asymp m^{1/12}$。误差项同 L-Thr-1 / L-Eff-1 的 $Q^{-\delta}$ 与幂次余项。证毕。

**状态.** 主弧半边与 L-Thr-1 **同级已证**（仅改写为「先 $H$ 后卷积 $f_4$」）；**不**控制 $r^{\mathrm{fib}}_{\mathfrak{m}}$。

---

## L-Fib32-5（已证）— 纤维次弧的可引用界与指数表

**引理 A（全环面 $H$）.** 对任意 $\varepsilon>0$，
$$
\int_0^1|H(\alpha)|\,\mathrm{d}\alpha
=\int_0^1|f_3f_2|\,\mathrm{d}\alpha
\ll_\varepsilon N^{5/12+\varepsilon}
$$
（$N=m$；引用 L-Biq-2：$\|f_3\|_4\|f_2\|_2$）。此即 $(3,2)$ 凸终点 $\beta_{3,2}/2$。

**引理 B（$f_4$ 外置的粗卷积）.**
$$
\int_0^1|f_4 H|\,\mathrm{d}\alpha
\le
\|f_4\|_\infty\int_0^1|H|
\ll_\varepsilon
P_4\cdot N^{5/12+\varepsilon}
=N^{1/3+\varepsilon}.
$$
特别地对任意 $Q$，
$$
\int_{\mathfrak{m}_{3,2}(Q)}|f_4 H|
\ll_\varepsilon N^{1/3+\varepsilon}.
$$

**引理 C（$L^2$ 卷积回收全混合凸壁）.**
$$
\int_0^1|f_4 H|
\le
\|f_4\|_2\|H\|_2.
$$
由 Parseval $\|f_4\|_2\asymp P_4^{1/2}=N^{1/8}$，且
$$
\|H\|_2\le\|f_3\|_4\|f_2\|_4
\ll_\varepsilon N^{1/6+1/4+\varepsilon}=N^{5/12+\varepsilon}
$$
（$\int|f_2|^4\ll_\varepsilon P_2^{2+\varepsilon}$），故
$$
\int|f_4 H|
\ll_\varepsilon N^{1/8+5/12+\varepsilon}
=N^{13/24+\varepsilon},
$$
与 L-Dec-2 **同一指数**。

**引理 D（次弧点态 $f_2$ 节省的纤维形）.** 若 $\alpha\in\mathfrak{m}_{3,2}(Q)$ 且采用与 L-Circ-7 相同的 Diophantine 定义，则
$$
|f_2(\alpha)|\ll N^{1/2}Q^{-1/2}(\log 2N)^{1/2},
$$
从而
$$
\int_{\mathfrak{m}_{3,2}(Q)}|H|
\ll_\varepsilon
N^{1/2}Q^{-1/2}N^{1/6+\varepsilon}
=N^{2/3+\varepsilon}Q^{-1/2}
$$
（用 $\|f_3\|_1\le\|f_3\|_2\ll_\varepsilon N^{1/6+\varepsilon}$ 的粗插值；可经华氏 $L^4$ 微调常数，不改下方结算量级）。再乘 $\|f_4\|_\infty$：
$$
\int_{\mathfrak{m}_{3,2}}|f_4 H|
\ll_\varepsilon
N^{1/4+2/3+\varepsilon}Q^{-1/2}
=N^{11/12+\varepsilon}Q^{-1/2},
$$
**劣于**引理 B 的 $N^{1/3}$（因 $\|f_3\|_1$ 过粗）。用 $\|f_3\|_4$ 平衡可得
$$
\int_{\mathfrak{m}_{3,2}}|H|
\ll_\varepsilon N^{5/12+\varepsilon}Q^{-\delta}
\quad(\delta\le 1/2\text{ 视剖分}),
$$
故
$$
\bigl|r^{\mathrm{fib}}_{\mathfrak{m}}\bigr|
\le
\int_{\mathfrak{m}_{3,2}}|f_4 H|
\ll_\varepsilon
N^{1/3+\varepsilon}Q^{-\delta}.
$$

**指数对照表.**

| 路径 | 可引用上界 | 相对目标 $m^{1/12}$ | 相对 $13/24$ |
|------|------------|---------------------|-------------|
| L-Dec-2 全混合 Hölder | $N^{13/24+\varepsilon}$ | 缺口 $N^{11/24}$ | $=$ |
| Fib $\|f_4\|_\infty\|H\|_1$ | $N^{1/3+\varepsilon}$ | 缺口 $N^{1/4}$ | **优**（$1/3<13/24$） |
| Fib $L^2\times L^2$ | $N^{13/24+\varepsilon}$ | 缺口 $N^{11/24}$ | $=$ |
| Fib 次弧 $Q^{-\delta}$（引理 D 粗） | $N^{1/3}Q^{-\delta}$ | 要 $Q\gg N^{1/(4\delta)}$ | 条件依赖 |

**注.** 引理 B 的 $N^{1/3}$ 是**绝对值**全环面/次弧均可用的粗界，已优于 L-Dec-2 的 $13/24$，但距 $\mathrm{H}_{\mathrm{thr}}$ 仍差 $N^{1/4}/(\log)^{O(1)}$；**单独不足以**关闭阈值。

---

## L-Fib32-6（已证·障碍）— 不能无条件绕开全混合 $13/24$ 壁

**命题.** 在「对 $H$ 做主/次弧 + 与 $f_4$ 卷积、且次弧仅用分幂均值 / Hölder / Parseval / 点态 Gauss」的方法族内：

1. **$L^2$ 卷积枝**给出的次弧天花板**恰好**为 $N^{13/24+\varepsilon}$（L-Fib32-5(C)），与 L-Dec-2、L-Hua-3、L-Tri-5 同壁。  
2. **$\|f_4\|_\infty$ 枝**给出更优的 $N^{1/3+\varepsilon}$，但  
   - 缺口仍为幂次 $N^{1/4}$（非对数）；  
   - 若靠放大 $Q$ 换 $Q^{-\delta}$ 填缺口，则 $Q\gg N^{\Theta(1)}$ 与 L-Fib32-4 要求的 $Q\le m^{\theta_1}$（$\theta_1<1/12$）**冲突**，主弧误差吞掉 $\mathfrak{S}\,m^{1/12}$；  
   - 该枝**不**使用 $f_4$ 的振荡，无法继续压到 $m^{1/12}$。  
3. **DH 型「几乎所有 $(3,2)$」输入不可用**（L-Fib32-2）；不能把纤维次弧误差当成「例外集对数稀」而免费删除。

**一句话.** 纤维改写**改变组织**（阈值可写成 $\sum_x r_{3,2}(m-x^4)>0$），**不**自动提供优于凸壁的次弧技术；要绕开 $13/24$，必须有对 $r^{\mathrm{fib}}_{\mathfrak{m}}$ 的**真纤维节省**（Fib32-G1–G3），而非再次落入全混合分幂 Hölder。

---

## L-Fib32-7（条件式）— 纤维阈值假设与蕴含

**假设 $\mathrm{H}_{\mathrm{fib}}(A)$.** 存在 $m_0=m_0(A)$，使一切 $m\ge m_0$ 在 L-Fib32-4 的剖分 $Q=m^{\theta_1}$ 下
$$
\bigl|r^{\mathrm{fib}}_{\mathfrak{m}(Q)}(m)\bigr|
\le
\frac{m^{1/12}}{(\log m)^{A+1}}.
$$

**弱变体 $\mathrm{H}_{\mathrm{fib}}^{\mathrm{abs}}(A)$.**
$$
\int_{\mathfrak{m}_{3,2}(Q)}|f_4 H|\,\mathrm{d}\alpha
\le
\frac{m^{1/12}}{(\log m)^{A+1}}.
$$

**与 $\mathrm{H}_{\mathrm{thr}}$ / H 的关系.**

| 假设 | 剖分对象 | 强度 |
|------|----------|------|
| H | 全混合次弧 $\|F\|_1$ 幂次节省 | 最强 |
| $\mathrm{H}_{\mathrm{thr}}(A)$ | 全混合次弧对数节省 | 强 |
| $\mathrm{H}_{\mathrm{fib}}(A)$ | 纤维次弧（$f_4$ 外置）对数节省 | **形式上可弱于** $\mathrm{H}_{\mathrm{thr}}$（允许 $|f_4|$ 与 $H_{\mathfrak{m}}$ 的振荡取消） |
| L-Fib32-5 已证 | $N^{1/3}$ 或 $N^{13/24}$ | 远弱于 $\mathrm{H}_{\mathrm{fib}}$ |

**引理 L-Fib32-7（已证蕴含）.** 固定 $A<\infty$。若 $\mathrm{H}_{\mathrm{fib}}(A)$ 成立，则存在 $m_1=m_1(A)$ 使
$$
\mathfrak{S}(m)\ge(\log m)^{-A}
\quad\Longrightarrow\quad
m\in\mathcal{R}_{4,3,2}
\qquad(m\ge m_1).
$$

**证明.** L-Fib32-4 给 $r^{\mathrm{fib}}_{\mathfrak{M}}\gg_A m^{1/12}(\log m)^{-A}$；$\mathrm{H}_{\mathrm{fib}}(A)$ 给 $|r^{\mathrm{fib}}_{\mathfrak{m}}|\le m^{1/12}(\log m)^{-(A+1)}$；相加得 $r(m)>0$。证毕。

**目标形（审查建议的阈值）.** 合写
$$
\exists\,A,N_0:\ 
\mathfrak{S}(m)\ge(\log m)^{-A}
\ \Longrightarrow\ 
\sum_{x\le m^{1/4}}r_{3,2}(m-x^4)>0
\quad(m\ge N_0),
$$
在 $\mathrm{H}_{\mathrm{fib}}(A)$ 下已证；次弧输入**只**要求纤维级 $\mathrm{H}_{\mathrm{fib}}$，允许陈述上弱于全 $F$ 的 $\mathrm{H}_{\mathrm{thr}}$——但**硬度上**仍与「主项尺度次弧」同级（见下缺口）。

---

## L-Fib32-8（已证结算）— 缺口清单与对 $13/24$ 的判决

### 结算

| 编号 | 摘要 | 状态 |
|------|------|------|
| L-Fib32-1 | $r=\sum_x r_{3,2}(m-x^4)=\int f_4 H e(-m\alpha)$ | 已证 |
| L-Fib32-2 | 纯 $(3,2)$-「多数+阈值」**否证**；DH 不适用 | 已证（否证） |
| L-Fib32-3 | $f_4$ 外置的主/次弧组织 | 已证（组织） |
| L-Fib32-4 | 卷积主项 $\asymp\mathfrak{S}\,m^{1/12}$（主弧半边） | 已证 |
| L-Fib32-5 | 纤维次弧指数表：$N^{1/3}$ / $N^{13/24}$ / $Q^{-\delta}$ | 已证 |
| L-Fib32-6 | **不**无条件绕开 $13/24$；$N^{1/3}$ 仍差 $N^{1/4}$ | 已证（障碍） |
| L-Fib32-7 | $\mathrm{H}_{\mathrm{fib}}+\mathfrak{S}$ 下界 $\Rightarrow$ 可表 | 已证蕴含；假设条件式 |
| L-Fib32-8 | 本结算 | 已证 |

### 缺口

| 代号 | 内容 | 堵住则得 |
|------|------|----------|
| **Fib32-G1** | $\mathrm{H}_{\mathrm{fib}}(A)$（任固定 $A$） | 纤维版 SS-阈值（L-Fib32-7） |
| **Fib32-G2** | 真纤维取消：$\lvert\int_{\mathfrak{m}_{3,2}}f_4 H e(-m\alpha)\rvert\ll m^{1/3-\delta}$（用 $f_4$ 与 $H_{\mathfrak{m}}$ 的振荡，而非 $\|f_4\|_\infty$） | 破 $N^{1/3}$ 粗壁；仍可能不够 $m^{1/12}$ |
| **Fib32-G3** | 短和/多数 $x$：$\#\{x\le P_4:|r_{3,2}^{\mathfrak{m}}(m-x^4)|$ 过大$\}$ 稀，使纤维和仍正 | 弱于逐点 $\mathrm{H}_{\mathrm{fib}}$ 的平均形阈值 |
| Fib32-G4 | 证明 $\mathrm{H}_{\mathrm{fib}}\Rightarrow\mathrm{H}_{\mathrm{thr}}$ 或严格更弱（比较二者） | 澄清「旁路」含金量 |

### 对「能否绕开 $13/24$」的最终回答

- **组织上：** 能——阈值次弧可改写为仅作用于 $H$ 的 $\mathrm{H}_{\mathrm{fib}}$，不再强制全混合 $\int_{\mathfrak{m}}|F|$。  
- **指数上：** 标准矩方法**不能**——$L^2(f_4)L^2(H)$ 回收 $13/24$；$\|f_4\|_\infty$ 得 $1/3$，优于 $13/24$ 但仍差 $N^{1/4}$，且与主弧 $Q$ 窗口冲突。  
- **DH 上：** **不能**借用「几乎所有 $y^3+z^2$」——断言为假。  
- **对 H / $\mathrm{H}_{\mathrm{thr}}$：** 本路线给出**可检验卷积引理**与条件式阈值；**不**缩短已证次弧到 $m^{1/12}$ 的幂次缺口至零。

**明确非声称.** 不证明 H、$\mathrm{H}_{\mathrm{thr}}$、$\mathrm{H}_{\mathrm{fib}}$、SS-Sync、$\mathcal{F}_0$ 有限、原猜想。

---

## 链条图

$$
\begin{CD}
\mathfrak{S}(m)\ge(\log m)^{-A}
@>{\mathrm{L\text{-}Fib32\text{-}4}}>>
r^{\mathrm{fib}}_{\mathfrak{M}}\gg \mathfrak{S}\,m^{1/12} \\
@V{\mathrm{H}_{\mathrm{fib}}(A)}VV @VV{\mathrm{L\text{-}Fib32\text{-}7}}V \\
|r^{\mathrm{fib}}_{\mathfrak{m}}|\le m^{1/12}/(\log)^{A+1}
@>>>
\sum_{x}r_{3,2}(m-x^4)>0
\end{CD}
$$

与纯 $(3,2)$ 对照（已否证）：
$$
\mathfrak{S}_{3,2}(t)\ge(\log)^{-A}
\ \not\Rightarrow\ 
t\in\mathcal{S}
\qquad\text{（L-Fib32-2；密度零）}.
$$

与全混合凸壁对照：
$$
\|f_4\|_2\|H\|_2
\ll
N^{13/24}
=\|F\|_{L^1\text{ 凸终点}},
\qquad
\|f_4\|_\infty\|H\|_1
\ll
N^{1/3}
\ \text{（优但不够）}.
$$
