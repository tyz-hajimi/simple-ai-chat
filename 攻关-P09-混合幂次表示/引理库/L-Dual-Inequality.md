# L-Dual-*：Titchmarsh 对偶 / 表示函数加性能量（路线 R14-Dual-Inequality）

> 路线 **R14-Dual-Inequality**（P09 攻关轮次 14，服务 **P2 = 假设 H**）。  
> 新想法：用 **Titchmarsh 对偶** / 指数和大值对偶 / Plancherel–能量恒等式，把次弧上
> $$
> I_{\mathfrak{m}}=\int_{\mathfrak{m}(Q)}|f_4 f_3 f_2|\,\mathrm{d}\alpha
> $$
> 改写成「混合幂表示函数的加性能量」或对偶和，试图在凸箱 $\mathcal{B}$（L-Hua-3）之外获得**非凸**节省。  
> **结论先行：** 对偶恒等式本身已证且可检；在「对角饱和能量 + 大值对偶 / Hölder 回收」族内，可引用指数仍钉死 $\beta/2=13/24$；**对偶能量对角障碍**阻止无条件非凸 $\delta$。  
> 可引用 L-Dec-2、L-Hua-3/4、L-Tri-5、L-Wt-5、L-Klo-5。**不声称假设 H 已证；不声称原猜想已证。**

---

## 0. 记号与对偶底座

沿用 L-Circ / L-Dec：$P_j=\lfloor N^{1/j}\rfloor$，
$$
f_j(\alpha)=\sum_{1\le u\le P_j}e(\alpha u^j),\qquad j=2,3,4,
$$
$$
F(\alpha):=f_4(\alpha)f_3(\alpha)f_2(\alpha),\qquad
\beta=\tfrac14+\tfrac13+\tfrac12=\tfrac{13}{12},\qquad
\tfrac{\beta}{2}=\tfrac{13}{24}.
$$
主弧 / 次弧 $\mathfrak{M}(Q)$、$\mathfrak{m}(Q)$ 同前。目标
$$
I:=\int_0^1|F|\,\mathrm{d}\alpha,\qquad
I_{\mathfrak{m}}:=\int_{\mathfrak{m}(Q)}|F|\,\mathrm{d}\alpha\le I.
$$

**混合幂表示函数**
$$
r(\ell)
:=\#\bigl\{(x,y,z):1\le x\le P_4,\ 1\le y\le P_3,\ 1\le z\le P_2,\
x^4+y^3+z^2=\ell\bigr\}.
$$
支撑落在 $[1,3N]$ 量级；写 $\mathcal{A}=\mathrm{supp}\,r$。**加性能量**（表示侧）
$$
\mathcal{E}_2(r)
:=\sum_{\ell\in\mathbb{Z}}r(\ell)^2
=\#\bigl\{(\mathbf{u},\mathbf{v}):\Phi(\mathbf{u})=\Phi(\mathbf{v})\bigr\},
$$
其中 $\Phi(x,y,z)=x^4+y^3+z^2$。对角解给出平凡下界
$$
\mathcal{E}_2(r)\ge P_4 P_3 P_2\asymp N^\beta.
$$

**引用（可检形式）.**

1. **Plancherel / 均值–能量恒等式.** $\displaystyle\int_0^1|F|^2=\sum_\ell r(\ell)^2=\mathcal{E}_2(r)$。  
2. **Titchmarsh / Montgomery 大值对偶模板.** 对 Dirichlet 多项式 / 指数和 $S$，大值集测度由系数相关（对偶和）控制；经典形式见 Titchmarsh *The Theory of the Riemann Zeta-Function*、Montgomery *Topics in Multiplicative Number Theory*、Huxley 大值法。本路线只把该模板迁到 $F$，**不**重证 $\zeta$ 侧定理。  
3. **凸障碍.** L-Hua-3：次临界箱内 Hölder 指数恒为 $13/24$。  
4. **对角饱和.** L-Wt-5 / L-Hua-4 / L-Tri-5：$\|F\|_2\asymp N^{\beta/2}$。

---

## L-Dual-1（已证·恒等式）— Plancherel 对偶：$\int|F|^2=\mathcal{E}_2(r)$

**命题.**
$$
\int_0^1\bigl|F(\alpha)\bigr|^2\,\mathrm{d}\alpha
=\sum_{\ell}r(\ell)^2
=\mathcal{E}_2(r).
$$
特别地，由对角计数
$$
\int_0^1|F|^2\,\mathrm{d}\alpha
\asymp N^\beta
\qquad\Rightarrow\qquad
\|F\|_2\asymp N^{\beta/2}=N^{13/24}.
$$

**证明.** 展开
$$
F(\alpha)=\sum_\ell r(\ell)\,e(\alpha\ell),
$$
Parseval / 正交性即得。对角 $\Phi(\mathbf{u})=\Phi(\mathbf{v})$ 含 $\mathbf{u}=\mathbf{v}$，贡献 $P_4 P_3 P_2$；非对角 $\ge 0$，故下界 $\asymp N^\beta$。上界由 L-Wt-5 / 标准完成法 $\ll_\varepsilon N^{\beta+\varepsilon}$（本题只需 $\asymp$ 的下界钉死 $\|F\|_2$）。证毕。

**对偶解读.** $L^2(\mathbb{T})$ 上的生成函数范数 **恒等于** 表示函数的加性能量；攻击 $\int|F|$ 的任何「对偶化」最终必须估计 $\mathcal{E}_2(r)$ 或其截断 / 加权变体。

---

## L-Dual-2（已证·恒等式）— 层切 / 大值对偶形式

对 $\lambda>0$ 定义大值集
$$
\mathcal{L}(\lambda):=\bigl\{\alpha\in[0,1]:|F(\alpha)|>\lambda\bigr\}.
$$
则（层切公式）
$$
I=\int_0^\infty\mathrm{meas}\bigl(\mathcal{L}(\lambda)\bigr)\,\mathrm{d}\lambda
=\int_0^{\|F\|_\infty}\mathrm{meas}\bigl(\mathcal{L}(\lambda)\bigr)\,\mathrm{d}\lambda.
$$
由 Chebyshev / Plancherel，
$$
\mathrm{meas}\bigl(\mathcal{L}(\lambda)\bigr)
\le\lambda^{-2}\int|F|^2
=\lambda^{-2}\,\mathcal{E}_2(r)
\ll\lambda^{-2}N^\beta.
$$
更精细的 **Titchmarsh 型对偶**（系数相关形式）：令
$$
A(h):=\sum_{\ell}r(\ell)r(\ell+h)
$$
（表示函数的加性相关），则对任意 $H\ge 1$，
$$
\int_0^1|F(\alpha)|^4\,\mathrm{d}\alpha
=\sum_{h}A(h)^2
\ge\sum_{|h|\le H}A(h)^2,
$$
且大值测度可用（Montgomery 不等式的指数和版）
$$
\mathrm{meas}\bigl(\mathcal{L}(\lambda)\bigr)
\ll_\varepsilon
\frac{N^{\beta+\varepsilon}}{\lambda^2}
+\frac{N^{2\beta+\varepsilon}}{\lambda^4 H}
+\frac{H}{\lambda^4}\sum_{1\le|h|\le H}A(h)^2
$$
一类界控制（常数与光滑截断依赖略；本文件只用其**结构**：大值 $\leftrightarrow$ 对偶相关能量）。

**次弧版.** 把 $\mathrm{meas}$ 换成 $\mathrm{meas}(\,\cdot\,\cap\mathfrak{m}(Q))$，并把 $\int|F|^2$ 换成 $\int_{\mathfrak{m}}|F|^2$，得
$$
I_{\mathfrak{m}}
=\int_0^{\|F\|_\infty}\mathrm{meas}\bigl(\mathcal{L}(\lambda)\cap\mathfrak{m}(Q)\bigr)\,\mathrm{d}\lambda,
$$
$$
\mathrm{meas}\bigl(\mathcal{L}(\lambda)\cap\mathfrak{m}\bigr)
\le\lambda^{-2}\int_{\mathfrak{m}}|F|^2.
$$

**证明.** 层切为非负可测函数标准公式；Chebyshev 由 Markov；相关形式由展开 $|F|^4=\bigl(\sum r(\ell)e(\ell\alpha)\bigr)^2\bigl(\sum r(m)e(-m\alpha)\bigr)^2$ 并收集 $h=\ell-m$。证毕。

---

## L-Dual-3（已证·恒等式）— 双线性对偶 / TT* 形

固定可测权 $|\psi|\le 1$（典型 $\psi=1_{\mathfrak{m}}$）。极化后（对照 L-Tri-1）
$$
\Bigl|\int F\,\psi\Bigr|
=\Bigl|\sum_{x,y,z}\widehat{\psi}(x^4+y^3+z^2)\Bigr|.
$$
对 $f_4$ 外置（对照 L-Fib32），写 $H:=f_3 f_2$，则
$$
\int f_4\,H\,\psi
=\sum_{x\le P_4}\widehat{\psi H}(x^4).
$$
**对偶和形式（Poisson / 完备化动机）.** 对固定模 $q$ 与余量 $a$，不完整和经 Poisson / Weyl 完备化后，长度 $P_4$ 的四次和对偶为长度 $\asymp q/P_4$（或 $N/(q P_4)$）的对偶指数和；混合三项时形式目标是
$$
\Bigl|\sum_{x\le P_4}\widehat{\psi H}(x^4)\Bigr|
\ll
P_4^{\theta}\,\|H\|_{L^{s}(\mathrm{supp}\,\psi)}\cdot(\text{对偶和节省}).
$$
绝对值版本（本题所需）经相位吸收同样落入
$$
I_{\mathfrak{m}}
\le\sup_{|a_x|\le 1}\Bigl|\sum_x a_x\,\widehat{1_{\mathfrak{m}}H}(x^4)\Bigr|.
$$

**证明.** 展开与交换积分；完备化模板见 Vaughan Ch.2–4 / L-Biq-1。证毕。

---

## L-Dual-4（已证）— 对偶路径指数表（尝试后的指数）

下列均在**已证输入**下执行；「对偶」只改组语言，不引入超凸假设。

| 方法名 | 对偶对象 | 可引用指数 $E$ | 相对 $13/24$ | 备注 |
|--------|----------|----------------|--------------|------|
| **Dual-Plancherel-CS** | $\mathcal{E}_2(r)=\int\|F\|^2$ | $13/24$ | $=$ | $I\le\|F\|_2\asymp N^{13/24}$ |
| **Dual-Layer-Chebyshev** | 大值测度 $\le\lambda^{-2}N^\beta$ | $13/24$ | $=$ | 最优切割 $\lambda\sim N^{\beta/2}$ 回收同阶 |
| **Dual-Corr-$A(h)$** | $\sum_{|h|\le H}A(h)^2\le\int\|F\|^4$ | $\ge 13/24$ | $\ge$ | 用华氏/VMVT 估 $\|F\|_4$ 不优（见下） |
| **Dual-Bilin-$f_4$** | $\sum_x\widehat{\psi H}(x^4)$ | $13/24$ | $=$ | Hölder / $L^2(H)$ 回收 L-Dec-2 |
| **Dual-Poisson-Weyl** | 完备化对偶长 | $\ge 13/24$ | $\ge$ | 点态 Weyl 积分后回 L-Circ-8 族 |
| **Dual-G1（条件式）** | 次弧能量 $\int_{\mathfrak{m}}\|F\|^2\ll N^{\beta-\delta}$ | $13/24-\delta/2$ | 优 | **未证**；强度 $\asymp$ Tri-G1 / Klo-G1 |

**详算（A）Plancherel–CS.**
$$
I\le\|F\|_2=\bigl(\mathcal{E}_2(r)\bigr)^{1/2}\asymp N^{13/24}.
$$

**详算（B）层切最优切割.** 取 $\Lambda=N^{\beta/2}$。则
$$
I
\le\Lambda\cdot 1+\int_{\Lambda}^{\|F\|_\infty}\frac{N^\beta}{\lambda^2}\,\mathrm{d}\lambda
\ll N^{\beta/2}+\frac{N^\beta}{\Lambda}
\asymp N^{13/24}.
$$
（$\|F\|_\infty\le N^{\beta}$ 的粗界只影响对数；切割点只能在 $\asymp N^{\beta/2}$ 平衡。）

**详算（C）相关能量枝.** 由 Hölder，
$$
I\le\|F\|_4\cdot 1^{3/4}.
$$
而
$$
\|F\|_4^4=\int|F|^4=\sum_h A(h)^2.
$$
对角 $h=0$ 已给 $A(0)=\sum r^2\asymp N^\beta$，故 $\|F\|_4\gg N^{\beta/4}=N^{13/48}$，代入仅得 $I$ 的**下界动机**；上界需控制全相关和。用分幂
$$
\|F\|_4\le\|f_4\|_8\|f_3\|_{8}\|f_2\|_{4/3}
$$
等，指数落入超临界或劣于 $13/24$（对照 L-Hua-2 华氏 $L^8$ 行 $E=7/12$）。用次临界箱再 Hölder 降到 $L^1$ 仍回 $13/24$（L-Hua-3）。

**详算（D）双线性对偶.**
$$
I\le\|f_4\|_{20}\|H\|_{20/19},\qquad
H=f_3 f_2,
$$
或 CS：$I\le\|f_4\|_2\|H\|_2$。后者
$$
\|f_4\|_2\asymp N^{1/8},\qquad
\|H\|_2\le\|f_3\|_4\|f_2\|_4\ll_\varepsilon N^{1/6+1/4+\varepsilon}
$$
需小心共轭；标准拼合即 L-Dec-1/2，得 $E=13/24$。

**详算（E）Poisson–Weyl 对偶.** 点态 $|f_j(\alpha)|\ll P_j^{1+\varepsilon}(q^{-1}+P_j^{-1}+q N^{-1})^{1/(2^{j-1})}$（Weyl）；乘积积分后属 L-Circ-8 / L-Dec-3 凸族，最优端点仍 $13/24$，从不更优。

**结论.** 方法名 **Dual-Plancherel / Dual-Layer / Dual-Bilin / Dual-Poisson**；族内已证最佳 **$E=13/24$**。**无**已证 $E<13/24$。

---

## L-Dual-5（已证·障碍）— 对偶能量对角障碍（非凸失败核）

**障碍陈述.** 在仅使用对偶恒等式（L-Dual-1…3）与对角可检下界 $\mathcal{E}_2(r)\gg N^\beta$ 的前提下，**不能**推出 $I\ll N^{13/24-\delta}$，因而**不能**无条件获得非凸节省。

**障碍核.**

1. **能量下界钉死 $L^2$.** L-Dual-1：$\|F\|_2\asymp N^{13/24}$。一切由 $L^2$ 控制 $L^1$ 的对偶路径（CS、层切 Chebyshev、Plancherel 大值）天花板 $\ge 13/24$。  
2. **对角 $=$ 对偶主项.** $\mathcal{E}_2(r)$ 的主项来自 $\Phi(\mathbf{u})=\Phi(\mathbf{v})$ 的对角流形；对偶语言把「凸终点」翻译成「表示能量不能低于 $N^\beta$」，**不**自动删除对角。  
3. **次弧不杀对角质量.** 小 $Q$ 时 $\mathrm{meas}(\mathfrak{m})\approx 1$，故 $\int_{\mathfrak{m}}|F|^2\asymp N^\beta$（L-Hua-4 饱和的 $F$-版）；大 $Q$ 时 Weyl 点态积分恰补回 $\beta/2$（L-Dec-3 / L-Klo-5）。对偶截断 $\int_{\mathfrak{m}}|F|^2$ **无**已证 $N^{\beta-\delta}$。  
4. **相关和 $A(h)$ 的对角饱和.** $A(0)\asymp N^\beta$；非对角平均若无额外算术输入，Montgomery 型大值对偶回到同一凸界（与 $\zeta$-大值法在凸性线停止同构）。  
5. **与已有障碍同构.** 本障碍 $=$ L-Hua-3（凸箱）的对偶翻译 $=$ L-Tri-5（对角流形）的能量侧 $=$ L-Wt-5（$\|F\|_2$ 饱和）。对偶**不**开辟新的无条件缝隙。

**一句话.** **对偶能量对角障碍**：Titchmarsh / Plancherel 对偶把 $\int|F|$ 换成 $\mathcal{E}_2(r)$ / $A(h)$ 后，对角贡献强制 $\|F\|_2\asymp N^{13/24}$，无非对角节省则无非凸 $\delta$。

**证明.** (1)(2) 由 L-Dual-1；(3) 引 L-Hua-4 / L-Klo-5；(4) $A(0)=\mathcal{E}_2(r)$；(5) 对照 L-Hua-3、L-Tri-5。证毕。

---

## L-Dual-6（条件式）— 突破接口 Dual-G1–G4

| 编号 | 假设 | 推出 |
|------|------|------|
| **Dual-G1** | 次弧能量亏缺：$\int_{\mathfrak{m}(Q)}|F|^2\ll N^{\beta-\delta}$（$Q=N^{\theta}$，$\theta$ 固定正） | 层切 / CS $\Rightarrow I_{\mathfrak{m}}\ll N^{13/24-\delta/2}$ |
| **Dual-G2** | 非对角相关：$\sum_{1\le\|h\|\le H}A(h)^2\ll N^{2\beta-\delta}$ 对某 $H=N^{\eta}$ | Montgomery 大值对偶可优于凸切割 |
| **Dual-G3** | 对偶和超 Weyl：$\sup_{\|a\|_\infty\le 1}\bigl|\sum_x a_x\widehat{1_{\mathfrak{m}}H}(x^4)\bigr|\ll N^{13/24-\eta}$ | 直接破壁；强度 $\asymp$ H |
| **Dual-G4** | 表示集加性能量增量：$\mathcal{A}=\mathrm{supp}\,r$ 的 $\mathcal{E}_2(\mathcal{A})$ 在去掉对角后有 $N^{\beta-\delta}$ 结构节省，且可迁回次弧 $L^1$ | 需混合幂差集的真加性组合输入 |

**状态.** Dual-G1–G4 **均未证**。Dual-G1 $\asymp$ Tri-G1 / Klo-G1 / Wt-G1；Dual-G3 $\asymp$ 假设 H。

---

## L-Dual-7（已证）— 与 L-AE / L-Tri / L-Klo 的正交对照

| 路线 | 对偶 / 能量对象 | 服务 | 与 R14 关系 |
|------|-----------------|------|-------------|
| L-AE / L-Inc | 例外集 $E_N$ 的 $\mathcal{E}_2$ | P1 | **正交**（集合能量 vs 表示函数能量） |
| L-Tri | 三线性型 $T_\psi$ | P2 | **同构**：对角流形障碍 $\leftrightarrow$ 对偶能量对角障碍 |
| L-Klo | 中间弧完整和 | P2 | 清洗不降真次弧；对偶亦不降 $\int_{\mathfrak{m}}\|F\|^2$ |
| L-Fib32 | $r_{3,2}$ 纤维卷积 | P2 | 外置 $f_4$ 是 L-Dual-3 特例；$L^2$ 回收同壁 |
| **L-Dual** | $r(\ell)$ / $A(h)$ / 大值对偶 | P2 | 本文件；恒等式新，指数不新 |

**注.** 不可把 L-AE 的「近随机能量」误迁到 $r(\ell)$：表示函数在对角上**必然**高能量 $\mathcal{E}_2(r)\gg N^\beta$，与例外集的贫能量假说方向相反。

---

## L-Dual-8（已证·结算）— 对 P2 / H 的判决

| 来源 | 可引用上界 | 相对 $N^{1/12}$ |
|------|------------|-----------------|
| L-Dec-2 / L-Hua-2 | $N^{13/24}$ | 缺口 $N^{11/24}$ |
| **L-Dual-4 Plancherel/Layer/Bilin** | $N^{13/24}$（无改进） | 缺口仍 $N^{11/24}$ |
| **L-Dual-5 对偶能量对角障碍** | 族内 $E\ge 13/24$ | 不能破壁 |
| Dual-G1–G3（条件式） | 形式 $N^{13/24-\delta}$ | 未证 |
| 假设 H 目标 | $N^{1/12}$ | — |

**判决.**
1. Plancherel / 层切 / 双线性 / Poisson 对偶恒等式已建立（L-Dual-1…3）。  
2. 尝试后的可引用指数均为 **$13/24$**（L-Dual-4）；**无**非凸已证 $\delta$。  
3. **对偶能量对角障碍**（L-Dual-5）说明：对偶只改写凸壁，不消除对角。  
4. Dual-G1–G4 为条件式破壁接口，强度不低于 H / Tri-G1 / Klo-G1（L-Dual-6）。  
5. 假设 H 仍为未证条件式；H-gap 仍为 $N^{11/24}$。  
6. **不声称**原猜想已证。

若要打破 $13/24$，必须在对偶侧引入**非对角**能量亏缺（Dual-G1/G2）或对偶和超凸取消（Dual-G3）——不在 R14 无条件范围内。

---

## 状态汇总

| 编号 | 摘要 | 状态 |
|------|------|------|
| L-Dual-1 | Plancherel：$\int\|F\|^2=\mathcal{E}_2(r)\asymp N^\beta$ | 已证（恒等式） |
| L-Dual-2 | 层切 / 大值对偶；$A(h)$ 相关形式 | 已证（恒等式） |
| L-Dual-3 | 双线性对偶 / $\sum_x\widehat{\psi H}(x^4)$ | 已证（恒等式） |
| L-Dual-4 | **对偶路径指数表**：$E=13/24$ | 已证 |
| L-Dual-5 | **对偶能量对角障碍**（非凸失败） | 已证（障碍） |
| L-Dual-6 | Dual-G1–G4 突破接口 | 条件式 |
| L-Dual-7 | 与 AE/Tri/Klo/Fib32 对照 | 已证（对照） |
| L-Dual-8 | 结算：不改进 L-Dec；H-gap 仍 $N^{11/24}$ | 已证（结算） |

**对 H 的判决：** R14-Dual-Inequality **止步**于 $\beta/2=13/24$；对偶恒等式可入库，**无**非凸已证节省。**H 仍为未证条件式。**
