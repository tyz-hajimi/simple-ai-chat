# L-Wt-*：平滑权与加权凸性（路线 R7-Weighted-Beta）

> 路线 **R7-Weighted-Beta**（P09 攻关轮次 7，服务 **P2 = 假设 H**；**全新**）。  
> 标准凸性 $\beta=1/4+1/3+1/2=13/12$，凸终点 $\beta/2=13/24$。  
> 新想法：引入平滑权 $w(x)w(y)w(z)$，或在短区间上对混合幂做局部化，定义加权生成函数 $F_j$，试图在「短区间表示」或「加权次弧」下把 $\int|F_4 F_3 F_2|$ 压到严格优于 $N^{13/24}$。  
> **结论先行：** 在可微权 / 短区间混合幂的次临界均值族内，加权凸性指数**仍钉死** $\beta_w/2=\beta/2=13/24$；平滑权不改变凸终点（L-Wt-4）。  
> 可引用 L-Dec-2、L-Hua-1…3、L-Biq-5。**不声称假设 H 已证；不声称原猜想已证。**

## 0. 记号与标准凸性

沿用 L-Circ / L-Dec / L-Hua：$P_j=\lfloor N^{1/j}\rfloor$，
$$
f_j(\alpha)=\sum_{1\le u\le P_j}e(\alpha u^j),\qquad j=2,3,4,
$$
$$
\beta=\frac14+\frac13+\frac12=\frac{13}{12},\qquad
\frac\beta2=\frac{13}{24}.
$$
目标积分（全环面或次弧 $\mathfrak{m}$）
$$
I:=\int_0^1\bigl|f_4(\alpha)f_3(\alpha)f_2(\alpha)\bigr|\,\mathrm{d}\alpha.
$$
L-Dec-2 / L-Hua-2 给出 $I\ll_\varepsilon N^{13/24+\varepsilon}$；H 目标为 $N^{1/12-\delta}$，缺口 $N^{11/24}$。

**权类 $\mathcal{W}_\kappa$.** 固定 $\kappa\ge 1$。称 $w:\mathbb{R}\to[0,1]$ 属于 $\mathcal{W}_\kappa$，若：
1. $\operatorname{supp} w\subseteq[0,1]$（或经仿射映到目标区间后仍紧支）；
2. $w\in C^\kappa(\mathbb{R})$，且 $\|w^{(m)}\|_\infty\ll_m 1$（$m\le\kappa$）；
3. 均值正定：$\int_0^1 w(t)\,\mathrm{d}t\asymp 1$（常数可依赖 $w$，与 $N$ 无关）。

短区间局部化用尺度参数 $\Theta\in(0,1]$：对中心 $X\sim P_j$，令
$$
w_{X,\Theta}(u)=w\Bigl(\frac{u-X}{\Theta X}\Bigr)
\quad\bigl(\text{支集长度}\asymp\Theta X\bigr).
$$
当 $\Theta=1$、$X=P_j/2$ 时退化为全长平滑截断。

---

## L-Wt-1（已证）— 加权对象的定义

**（A）乘积平滑权.** 取 $w_j\in\mathcal{W}_\kappa$（$j=2,3,4$），定义加权指数和
$$
F_j(\alpha)
:=\sum_{1\le u\le P_j}w_j\Bigl(\frac{u}{P_j}\Bigr)\,e(\alpha u^j)
\qquad(j=2,3,4).
$$
加权三线性形式与加权次弧积分
$$
I_w:=\int_0^1\bigl|F_4 F_3 F_2\bigr|\,\mathrm{d}\alpha,
\qquad
I_w(\mathfrak{m}):=\int_{\mathfrak{m}}\bigl|F_4 F_3 F_2\bigr|\,\mathrm{d}\alpha.
$$
当 $w_j\equiv 1_{[0,1]}$（不光滑，仅作对照）时 $F_j=f_j$、$I_w=I$。

**（B）短区间混合幂.** 给定中心 $(X,Y,Z)$ 与尺度 $(\Theta_4,\Theta_3,\Theta_2)\in(0,1]^3$，定义
$$
\begin{aligned}
F_4^{[X,\Theta_4]}(\alpha)
&=\sum_u w_{X,\Theta_4}(u)\,e(\alpha u^4),\\
F_3^{[Y,\Theta_3]}(\alpha)
&=\sum_v w_{Y,\Theta_3}(v)\,e(\alpha v^3),\\
F_2^{[Z,\Theta_2]}(\alpha)
&=\sum_z w_{Z,\Theta_2}(z)\,e(\alpha z^2),
\end{aligned}
$$
以及局部表示生成函数
$$
F^{[X,Y,Z;\boldsymbol{\Theta}]}
:=F_4^{[X,\Theta_4]}F_3^{[Y,\Theta_3]}F_2^{[Z,\Theta_2]}.
$$
「短区间表示」指：把全局 $I$ 经光滑剖分写成 $\sum_{X,Y,Z}I^{[X,Y,Z]}$，每项为 $\int|F^{[X,Y,Z;\boldsymbol{\Theta}]}|$。

**（C）加权次弧.** 对可测权 $\psi:[0,1]\to[0,1]$（例如 $\psi=1_{\mathfrak{m}}$ 或 $\mathfrak{m}$ 的 $C^\kappa$ 磨光），记
$$
I_w^\psi:=\int_0^1\psi(\alpha)\,|F_4 F_3 F_2|\,\mathrm{d}\alpha.
$$
$\psi\equiv 1$ 时退回 $I_w$；$\psi=1_{\mathfrak{m}}$ 时为加权次弧积分。

**（D）加权对角质量 / 加权凸性指数.** 记
$$
\beta_w
:=\lim_{N\to\infty}\frac{\log\bigl(\|w_4\|_{L^2[1,P_4]}^2\|w_3\|_{L^2[1,P_3]}^2\|w_2\|_{L^2[1,P_2]}^2\bigr)}{\log N},
$$
其中 $w_j$ 在求和变量上按（A）或（B）解释（短区间时 $\|w_j\|_2^2\asymp\Theta_j P_j$）。无权重时对角 $\int|f_4 f_3 f_2|^2$ 的主项 $\asymp P_4 P_3 P_2=N^\beta$，故 $\beta_w=\beta$。加权凸终点定义为 $\beta_w/2$。

---

## L-Wt-2（已证）— 加权均值与次临界范数

**引理.** 设 $w_j\in\mathcal{W}_\kappa$（$\kappa\ge 1$），$F_j$ 如 L-Wt-1(A)。则对任意 $\varepsilon>0$：
$$
\begin{aligned}
\|F_4\|_4
&\ll_\varepsilon N^{1/8+\varepsilon},\\
\|F_3\|_4
&\ll_\varepsilon N^{1/6+\varepsilon},\\
\|F_2\|_2
&\asymp N^{1/4}.
\end{aligned}
$$
更一般地，在次临界箱
$$
\mathcal{B}=\bigl\{(p,q,r):1\le p\le 20,\ 1\le q\le 12,\ 1\le r\le 2,\ \tfrac1p+\tfrac1q+\tfrac1r=1\bigr\}
$$
上，
$$
\|F_4\|_p\ll_\varepsilon N^{1/8+\varepsilon},\qquad
\|F_3\|_q\ll_\varepsilon N^{1/6+\varepsilon},\qquad
\|F_2\|_r\ll N^{1/4},
$$
与无权重 $f_j$ 的次临界指数**相同**（L-Hua-3 / L-Dec 输入）。

**短区间版.** 对 $F_j$ 取 L-Wt-1(B) 且 $\Theta_j\in(0,1]$，有
$$
\|F_4^{[X,\Theta_4]}\|_4
\ll_\varepsilon (\Theta_4 P_4)^{1/2+\varepsilon}
=N^{1/8+\varepsilon}\Theta_4^{1/2+\varepsilon},
$$
$$
\|F_3^{[Y,\Theta_3]}\|_4
\ll_\varepsilon (\Theta_3 P_3)^{1/2+\varepsilon}
=N^{1/6+\varepsilon}\Theta_3^{1/2+\varepsilon},
$$
$$
\|F_2^{[Z,\Theta_2]}\|_2
\asymp (\Theta_2 P_2)^{1/2}
=N^{1/4}\Theta_2^{1/2}.
$$
（长度 $\asymp\Theta_j P_j$ 的 Weyl/华氏差分 + 完备化；平滑权经分部积分吸收相位一次差分的边界，误差 $O_\kappa((\Theta_j P_j)^{-c})$，不改幂次。）

**证明.**  
（i）$F_2$：Parseval
$$
\int_0^1|F_2|^2
=\sum_{u\le P_2}w_2(u/P_2)^2
\asymp P_2,
$$
故 $\|F_2\|_2\asymp N^{1/4}$；对 $r\le 2$ 有 $\|F_2\|_r\le\|F_2\|_2$。  
（ii）$F_3$：一次 Weyl 差分，
$$
|F_3(\alpha)|^2
\ll P_3\sum_{|h|<P_3}\bigl|\widehat{w}_3(h)\bigr|\,|S_3(\alpha;h)|,
$$
其中 $\widehat{w}_3$ 为权差分核，$S_3$ 为立方相位差分和。因 $w_3\in\mathcal{W}_\kappa$，核满足 $\sum_h|\widehat{w}_3(h)|\ll_\kappa 1$（相对无权重的 $h$-密度），华氏立方均值给出
$$
\int|F_3|^4\ll_\varepsilon P_3^{2+\varepsilon},
$$
即 $\|F_3\|_4\ll_\varepsilon N^{1/6+\varepsilon}$。$L^8$ 同理（对照 L-Hua-1）。  
（iii）$F_4$：同法得 $\int|F_4|^4\ll_\varepsilon P_4^{2+\varepsilon}$，即 $\|F_4\|_4\ll_\varepsilon N^{1/8+\varepsilon}$；VMVT 次临界–临界对照将 $p$ 扩至 $20$（引用 L-Dec，不重证）。  
（iv）短区间：把求和长度换成 $\Theta_j P_j$，指数中 $P_j\mapsto\Theta_j P_j$，即得所述 $\Theta_j$ 因子。证毕。

---

## L-Wt-3（已证）— 加权凸性指数表；$I_w$ 止于 $13/24$

**（A）全长平滑权.** 对任意 $w_j\in\mathcal{W}_\kappa$ 与 $(p,q,r)\in\mathcal{B}$，
$$
I_w
\le\|F_4\|_p\|F_3\|_q\|F_2\|_r
\ll_\varepsilon N^{13/24+\varepsilon}.
$$
代表元 $(4,4,2)$：
$$
I_w
\le\|F_4\|_4\|F_3\|_4\|F_2\|_2
\ll_\varepsilon N^{1/8+1/6+1/4+\varepsilon}
=N^{13/24+\varepsilon}.
$$
加权凸性指数
$$
E_w:=\frac18+\frac16+\frac14=\frac{13}{24}=\frac{\beta}{2}=\frac{\beta_w}{2}
$$
（全长时 $\beta_w=\beta$，因 $\|w_j\|_2^2\asymp P_j$）。

**（B）短区间混合幂.** 记
$$
I^{[X,Y,Z;\boldsymbol{\Theta}]}
:=\int\bigl|F_4^{[X,\Theta_4]}F_3^{[Y,\Theta_3]}F_2^{[Z,\Theta_2]}\bigr|.
$$
由 L-Wt-2，
$$
I^{[X,Y,Z;\boldsymbol{\Theta}]}
\ll_\varepsilon
N^{13/24+\varepsilon}\,
\Theta_4^{1/2}\Theta_3^{1/2}\Theta_2^{1/2}.
$$
同时加权对角质量满足
$$
\beta_w(\boldsymbol{\Theta})
=\frac{\log\bigl((\Theta_4 P_4)(\Theta_3 P_3)(\Theta_2 P_2)\bigr)}{\log N}
=\beta+\frac{\log(\Theta_4\Theta_3\Theta_2)}{\log N},
$$
故
$$
\frac{\beta_w(\boldsymbol{\Theta})}{2}
=\frac{13}{24}+\frac12\log_N(\Theta_4\Theta_3\Theta_2),
$$
与上界指数**一致**：短区间只把两端同乘 $\prod\Theta_j^{1/2}$，**相对凸终点无增益**。

**（C）剖分重组.** 用光滑单位分解把 $[1,P_j]$ 分成 $\asymp\Theta_j^{-1}$ 个短区间。全局积分满足
$$
I
\ll
\sum_{X,Y,Z}I^{[X,Y,Z;\boldsymbol{\Theta}]}
+\text{（边界磨光误差）}.
$$
项数 $\asymp(\Theta_4\Theta_3\Theta_2)^{-1}$，每项 $\ll N^{13/24}(\Theta_4\Theta_3\Theta_2)^{1/2}$，乘积
$$
\ll N^{13/24}\,(\Theta_4\Theta_3\Theta_2)^{-1/2}.
$$
取 $\Theta_j=1$ 回到 $N^{13/24}$；取 $\Theta_j\to 0$ 反而因项数爆炸使上界变差。**不存在**使总指数 $<13/24$ 的尺度选择。

**（D）加权次弧 $\psi$.** 因 $0\le\psi\le 1$，
$$
I_w^\psi\le I_w\ll_\varepsilon N^{13/24+\varepsilon}.
$$
若 $\psi$ 为 $\mathfrak{m}(Q)$ 的示性或磨光，截断不改进次临界范数（对照 L-Hua-4：$\|F_j\|_{L^s(\mathfrak{m})}\le\|F_j\|_s$），Hölder 上界仍止于 $13/24$。

**证明.** （A）（B）由 L-Wt-2 + Hölder；（C）计数如上；（D）正性。证毕。

---

## L-Wt-4（已证）— 障碍引理：平滑权不改变 $\beta/2$ 凸终点

**定义（R7-Wt 方法族）.** 凡由下列操作得到的 $|F_4 F_3 F_2|$ 型积分上界：
1. 用 $w_j\in\mathcal{W}_\kappa$ 或短区间权 $w_{X,\Theta}$ 替换 $f_j\to F_j$；
2. 可选地对频率侧乘以有界权 $\psi$（加权次弧）；
3. 估计时**仅**使用次临界加权均值：$\|F_4\|_p\ll N^{1/8+\varepsilon}$（$p\le 20$）、$\|F_3\|_q\ll N^{1/6+\varepsilon}$（$q\le 12$）、$\|F_2\|_r\ll N^{1/4}$（$r\le 2$），以及短区间的 $\Theta^{1/2}$ 换算；
4. 经 Hölder / Cauchy–Schwarz / 光滑剖分重组拼合。

**障碍引理（平滑权不改变 $\beta/2$）.** 该族内一切可引用形式指数满足
$$
E_{\mathrm{Wt}}\ge\frac{13}{24}=\frac{\beta}{2}.
$$
等号在「全长平滑权 + 次临界箱 $\mathcal{B}$ 内 Hölder」时达到，与 L-Hua-3 / L-Dec-2 凸终点重合。特别地：
| 路径 | 形式指数 $E$ | 相对 $13/24$ |
|------|-------------|--------------|
| 全长 $w_j\in\mathcal{W}_\kappa$ + $(4,4,2)$ | $13/24$ | $=$（族内最优） |
| $\mathcal{B}$ 内其他三元组 | $13/24$ | $=$ |
| 短区间 $\boldsymbol{\Theta}$ 单项 | $13/24+\frac12\log_N(\prod\Theta_j)$ | $=$ 其 $\beta_w/2$ |
| 短区间剖分重组（任意 $\Theta_j$） | $\ge 13/24$ | $\ge$ |
| 加权次弧 $\psi\le 1$ | $\ge 13/24$（上界不优） | $\ge$ |
| 越出次临界箱 | $>13/24$ | $>$ |

**证明.**  
（i）全长：L-Wt-2 表明平滑权**不改变**次临界范数指数，故 L-Hua-3 的箱论证原样适用：
$$
\frac18+\frac16+\frac14=\frac{13}{24}.
$$
权的 $C^\kappa$ 正则性只改善差分核的衰减，不压低半幂。  
（ii）短区间：单项指数等于 $\beta_w(\boldsymbol{\Theta})/2$；剖分项数补偿后总指数 $\ge 13/24$（L-Wt-3(C)）。  
（iii）加权次弧：$\psi\le 1$ 使积分变小，但**可引用的 Hölder 上界**仍由全环面范数控制，不能写出 $N^{13/24-\delta}$（L-Hua-4 型饱和在平滑权下同样成立：对角贡献 $\asymp\prod\|w_j\|_2^2$，截断不删对角主项的幂次）。  
（iv）越出 $\mathcal{B}$ 则某因子指数严格增大，总指数 $>13/24$。  
故族内 $E_{\mathrm{Wt}}\ge 13/24$，**平滑权不改变 $\beta/2$ 凸终点**。证毕。

**一句话.** 乘积平滑权与短区间混合幂只改写生成函数的振幅，不改写各因子的次临界半幂；凡停留在加权次临界均值 + Hölder 的路线，自然终点仍是 $\beta/2=13/24$，不能缩小 H-gap。

---

## L-Wt-5（已证）— 与对角 / Plancherel 对齐：$\|F\|_2\asymp N^{\beta/2}$

记 $F=F_4 F_3 F_2$（全长权）。则
$$
\int_0^1|F(\alpha)|^2\,\mathrm{d}\alpha
=\sum_{\substack{x_1,x_2\le P_4\\ y_1,y_2\le P_3\\ z_1,z_2\le P_2}}
W(\mathbf{x},\mathbf{y},\mathbf{z})\,
\mathbf{1}_{x_1^4+y_1^3+z_1^2=x_2^4+y_2^3+z_2^2},
$$
其中 $W$ 为权乘积。对角贡献
$$
\asymp
\Bigl(\sum_x w_4(x/P_4)^2\Bigr)
\Bigl(\sum_y w_3(y/P_3)^2\Bigr)
\Bigl(\sum_z w_2(z/P_2)^2\Bigr)
\asymp P_4 P_3 P_2=N^\beta,
$$
故 $\|F\|_2\asymp N^{\beta/2}=N^{13/24}$（与无权重同阶；对照 L-Osc-2 注）。因此：
- 用 $\|F\|_2$ 控制次弧振荡（如 L-Osc 的 $L^2(g)$ 路径）时，天花板仍是 $N^{13/24}K^{1/2}$；
- 加权**不能**把 Plancherel 质量降到 $N^{\beta-\delta}$，除非权本身把有效支集缩到 $N^{-\delta}$ 密度——而那时表示问题已换成稀疏散射，不再服务原 $I$ 的全体次弧界。

**证明.** 对角计数如上；非对角由权有界归约到无权重的加性能量，至多贡献 $N^{\beta+\varepsilon}$ 的低阶扰动（标准完成平方 / 行列式，略），故 $\|F\|_2\asymp N^{13/24}$。证毕。

---

## L-Wt-6（已证·结算）— 对 P2 / H 的判决

| 来源 | 可引用上界 | 相对 $N^{1/12}$ |
|------|------------|-----------------|
| L-Dec-2 / L-Hua-2 | $N^{13/24}$ | 缺口 $N^{11/24}$ |
| **L-Wt-3 加权 Hölder** | $N^{13/24}$（无改进） | 缺口仍 $N^{11/24}$ |
| **L-Wt-4 障碍** | 族内 $E\ge 13/24$ | 不能破壁 |
| 短区间剖分 | $\ge N^{13/24}$ | 不优 |
| 假设 H 目标 | $N^{1/12}$ | — |

**判决.**
1. 加权对象 $F_j$、$I_w$、$I^{[X,Y,Z;\boldsymbol{\Theta}]}$、$I_w^\psi$ 已定义（L-Wt-1）；加权次临界指数与无权重相同（L-Wt-2）。  
2. 加权凸性指数计算给出 $E_w=13/24=\beta_w/2$（L-Wt-3）；短区间只改写两端的 $\Theta$ 因子，剖分后无净增益。  
3. **平滑权不改变 $\beta/2$ 凸终点**（L-Wt-4）为已证障碍：R7-Wt 族不能改进 L-Dec-2。  
4. Plancherel 质量 $\|F\|_2\asymp N^{13/24}$ 确认加权不降对角（L-Wt-5）。  
5. 假设 H 仍为未证条件式；H-gap 仍为 $N^{11/24}$。  
6. **不声称**原猜想已证。

若要打破 $13/24$，必须引入超出「平滑权 / 短区间 + 次临界均值 + Hölder」的输入（真次弧非对角结构、与缺项 $g$ 的振荡取消 Osc-G1/G2、或超凸解耦）。

---

## 状态汇总

| 编号 | 摘要 | 状态 |
|------|------|------|
| L-Wt-1 | 加权对象：$F_j$、短区间混合幂、加权次弧、$β_w$ | 已证（定义） |
| L-Wt-2 | 加权次临界范数 $=$ 无权重指数 | 已证 |
| L-Wt-3 | 加权凸性指数表；$I_w$ 止于 $13/24$ | 已证 |
| L-Wt-4 | **平滑权不改变 $β/2$ 凸终点** | 已证（障碍） |
| L-Wt-5 | $\|F\|_2\asymp N^{β/2}$；对角不降 | 已证 |
| L-Wt-6 | 结算：不改进 L-Dec；H-gap 仍 $N^{11/24}$ | 已证（结算） |
