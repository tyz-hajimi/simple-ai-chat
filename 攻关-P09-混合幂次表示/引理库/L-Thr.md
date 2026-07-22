# L-Thr：局部到全局的 SS-阈值（路线 R5-Local-Threshold）

> 路线 **R5-Local-Threshold**（P09 攻关轮次 5，服务 **P1**；响应对抗审查 R4：L-SSO-5 的 $\max\mathfrak{S}\gg 1$ **缺阈值**故对 E-kill 无效）。  
> 目标：建立或**条件式**建立
> $$
> \mathfrak{S}(m)\ge(\log m)^{-A}\ \Longrightarrow\ m\in\mathcal{R}_{4,3,2}
> $$
> （充分大 $m$）。全证明当前不可能（次弧距 $m^{\beta-1}$ 仍差幂次；见 L-Dec / L-Hua）。本文件拆成：主弧下界（已证）、次弧假设 $\mathrm{H}_{\mathrm{thr}}$（条件式）、二者拼合的蕴含引理（已证）。  
> **不**声称原猜想、SS-Sync、或 $\mathrm{H}_{\mathrm{thr}}$ 本身已证。禁止数值程序。

---

## 0. 符号

沿用：
$$
\mathcal{R}_{4,3,2}=\{x^4+y^3+z^2:x,y,z\in\mathbb{N}_0\},
\qquad
E=\mathbb{N}_0\setminus\mathcal{R}_{4,3,2},
\qquad
\beta=\tfrac14+\tfrac13+\tfrac12=\tfrac{13}{12}.
$$
对 $m\ge 1$ 令 $P_j=\lfloor m^{1/j}\rfloor$（$j=2,3,4$），
$$
f_j(\alpha)=\sum_{1\le u\le P_j}e(\alpha u^j),
\qquad
r(m)=\sum_{\substack{x\le P_4\\ y\le P_3\\ z\le P_2\\ x^4+y^3+z^2=m}}1
=\int_0^1 f_4(\alpha)f_3(\alpha)f_2(\alpha)\,e(-m\alpha)\,\mathrm{d}\alpha.
$$
（箱截断与 $\mathbb{N}_0$ 无截断在 $m$ 充分大时差 $O(m^{\varepsilon})$ 的边界项，不影响下文阈值形结论；与 L-Det 的 $r(m)$ 同阶约定。）

局部密度 $\sigma_p(m)$ 与奇异级数 $\mathfrak{S}(m)=\prod_p\sigma_p(m)$ 同 L-SSO / L-Ekill-SS。奇异积分（连续主项核）
$$
\mathfrak{J}(m)
=\int_{-\infty}^{\infty}v_4(\beta)v_3(\beta)v_2(\beta)\,e(-m\beta)\,\mathrm{d}\beta,
$$
其中 $v_j(\beta)=\int_0^{m^{1/j}}e(\beta\xi^j)\,\mathrm{d}\xi$（标准生成核；差一有界因子的等价定义皆可）。

主弧 / 次弧：固定参数 $Q=Q(m)\ge 1$，按宽度 $Q/(q m)$ 的 Farey 剖分定义 $\mathfrak{M}(Q)$、$\mathfrak{m}(Q)=[0,1)\setminus\mathfrak{M}(Q)$（与 L-Circ / L-Dec 一致）。写
$$
r(m)=r_{\mathfrak{M}}(m)+r_{\mathfrak{m}}(m),
\qquad
r_{\mathfrak{M}}=\int_{\mathfrak{M}}F\,e(-m\alpha)\,\mathrm{d}\alpha,\quad
r_{\mathfrak{m}}=\int_{\mathfrak{m}}F\,e(-m\alpha)\,\mathrm{d}\alpha,
$$
其中 $F=f_4f_3f_2$。

**量级字典.** $\beta-1=1/12$。期望主项为 $\mathfrak{S}(m)\,\mathfrak{J}(m)\asymp\mathfrak{S}(m)\,m^{1/12}$。

---

## L-Thr-1（已证）— 奇异积分正性与主弧贡献下界

### （A）奇异积分（已证，解析）

存在绝对常数 $c_{\mathfrak{J}},C_{\mathfrak{J}}>0$ 使对一切充分大 $m$，
$$
c_{\mathfrak{J}}\,m^{\beta-1}
\le
\mathfrak{J}(m)
\le
C_{\mathfrak{J}}\,m^{\beta-1}.
$$
特别地 $\mathfrak{J}(m)\gg m^{1/12}>0$。

**证明概要.** 对 $v_j$ 作标准缩放 $\beta=m^{-1}t$（或等价地 Mellin / Γ-因子分解）：
$$
\mathfrak{J}(m)=m^{\beta-1}\int_{-\infty}^{\infty}\prod_{j\in\{2,3,4\}}
\Bigl(\int_0^1 e(t u^j)\,\mathrm{d}u\Bigr)\,e(-t)\,\mathrm{d}t
+\text{端点误差}.
$$
被积核在 $t=0$ 邻域 $\asymp 1$，且因 $\sum 1/j=\beta>1$ 绝对可积于无穷；端点 / 截断误差 $o(m^{\beta-1})$。故主项系数为正常数。证毕。

（出处形：Vaughan *The Hardy–Littlewood Method* Ch.2；Davenport *Analytic Methods for Diophantine Equations* 对混合次的奇异积分缩放。）

### （B）主弧近似包（已证，经典圆法）

存在绝对常数 $\theta_0\in(0,1/12)$ 与 $C_{\mathrm{maj}}<\infty$，使得当
$$
1\le Q\le m^{\theta_0}
$$
时，对一切充分大 $m$，
$$
r_{\mathfrak{M}(Q)}(m)
=
\mathfrak{S}(m)\,\mathfrak{J}(m)
+O\bigl(m^{\beta-1}Q^{-\delta_0}\bigr)
+O\bigl(m^{\beta-1-\eta_0}\bigr),
$$
其中 $\delta_0,\eta_0>0$ 绝对（来自 Gauss 和完备化误差、Farey 邻域逼近、以及 L-SSO-2(A) 型积尾把截断奇异级数换成全 $\mathfrak{S}$ 的一致误差）。

**证明概要.**  
1. 在每条主弧 $\alpha=a/q+\beta$（$q\le Q$，$|\beta|\le Q/(qm)$）上，用完整 Gauss 和替换 $f_j$（误差由 Weyl / 差分控制，对 $Q\le m^{\theta_0}$ 可吸收进 $m^{\beta-1-\eta_0}$）。  
2. 对 $\beta$ 的积分给出 $\mathfrak{J}$ 的局部片；对 $a,q$ 求和给出截断奇异级数 $\mathfrak{S}_{\le Q}$（或等价的 Ramanujan 和形）。  
3. 由 L-SSO-2(A)（绝对收敛框架）：存在与 $m$ 无关的 $P_\varepsilon$ 使 $|T_{P_\varepsilon}-1|\le\varepsilon$。取 $Q\ge P_\varepsilon$ 且 $Q\le m^{\theta_0}$，得 $\mathfrak{S}_{\le Q}=\mathfrak{S}\cdot(1+O(\varepsilon))$。取 $\varepsilon=1/2$ 固定，误差并入 $O(m^{\beta-1}Q^{-\delta_0})$ 或吸收进隐含常数。证毕。

### （C）主弧下界（已证推论）

固定满足 $P_{1/4}\le Q\le m^{\theta_0}$ 的剖分参数（例如 $Q=m^{\theta_0}$）。则存在 $c_0>0$ 与 $m_0$，使一切 $m\ge m_0$，
$$
r_{\mathfrak{M}(Q)}(m)
\ge
c_0\,\mathfrak{S}(m)\,m^{\beta-1}
-
C_{\mathrm{maj}}\,m^{\beta-1}Q^{-\delta_0}.
$$
从而当 $\mathfrak{S}(m)\ge 2c_0^{-1}C_{\mathrm{maj}}Q^{-\delta_0}$ 时，
$$
r_{\mathfrak{M}(Q)}(m)
\gg
\mathfrak{S}(m)\,m^{\beta-1}.
$$
特别地：对任意固定 $A<\infty$，取 $Q=m^{\theta_0}$，则 $Q^{-\delta_0}=m^{-\theta_0\delta_0}$ 远小于 $(\log m)^{-A}$，故
$$
\mathfrak{S}(m)\ge(\log m)^{-A}
\quad\Longrightarrow\quad
r_{\mathfrak{M}(Q)}(m)
\gg_A
\mathfrak{S}(m)\,m^{\beta-1}
\gg_A
\frac{m^{\beta-1}}{(\log m)^{A}}
$$
对充分大 $m$ 成立。

**定位.** 本条给出「局部 Euler 积不太小 $\Rightarrow$ 主弧已贡献超过主项一半」的**已证**半边；**不**控制次弧，故**不**单独推出 $r(m)>0$。

---

## L-Thr-2（条件式假设）— 次弧阈值误差 $\mathrm{H}_{\mathrm{thr}}$

**假设 $\mathrm{H}_{\mathrm{thr}}(A)$.** 存在 $m_1=m_1(A)$，使对一切 $m\ge m_1$，在 L-Thr-1 所用的同一剖分 $Q=m^{\theta_0}$ 下，
$$
\bigl|r_{\mathfrak{m}(Q)}(m)\bigr|
\le
\frac{m^{\beta-1}}{(\log m)^{A+1}}.
$$

**弱变体 $\mathrm{H}_{\mathrm{thr}}^{\mathrm{abs}}(A)$.** 同一结论，但以绝对值积分代替振荡积分：
$$
\int_{\mathfrak{m}(Q)}|f_4f_3f_2|\,\mathrm{d}\alpha
\le
\frac{m^{\beta-1}}{(\log m)^{A+1}}.
$$
显然 $\mathrm{H}_{\mathrm{thr}}^{\mathrm{abs}}(A)\Rightarrow\mathrm{H}_{\mathrm{thr}}(A)$。

**与假设 H / H′ 的关系.**

| 假设 | 要害尺度 | 相对 $\mathrm{H}_{\mathrm{thr}}$ |
|------|----------|-------------------------------|
| H（W-Circ） | $\int_{\mathfrak{m}}|F|\ll m^{1/12-\delta}$ | **严格强于** $\mathrm{H}_{\mathrm{thr}}$（幂次节省 vs 仅对数） |
| H′/Lac | 几乎-H 的 $F$ + Peak-Maj | 若成立则对大 $A$ 推出 $\mathrm{H}_{\mathrm{thr}}(A)$（经 L-Lac-6 表） |
| L-Dec-2 已证界 | $\int_0^1|F|\ll_\varepsilon m^{13/24+\varepsilon}$ | **远弱于** $\mathrm{H}_{\mathrm{thr}}$：差 $m^{11/24}/(\log)^{O(1)}$ |

**缺口 Thr-G1.** $\mathrm{H}_{\mathrm{thr}}(A)$ 对任意 $A<\infty$ **未证**。L-Dec / L-Hua 凸终点钉死可引用指数 $13/24$；对数杠杆（L-Lac Flat）不足以填 $m^{11/24}$。本假设与「圆法充分大可表」同级硬度核，**不是**比 H 明显更弱的免费中间式——仅在对数 vs 幂次上略宽，对现存次弧技术无帮助。

---

## L-Thr-3（已证蕴含）— $\mathrm{H}_{\mathrm{thr}}+\mathfrak{S}$ 下界 $\Rightarrow$ 可表

**引理 L-Thr-3.** 固定 $A<\infty$。设 $\mathrm{H}_{\mathrm{thr}}(A)$ 成立。则存在 $m_2=m_2(A)$，使一切 $m\ge m_2$ 满足
$$
\mathfrak{S}(m)\ge(\log m)^{-A}
\quad\Longrightarrow\quad
m\in\mathcal{R}_{4,3,2}.
$$

**证明.** 取 L-Thr-1(C) 的剖分 $Q=m^{\theta_0}$。由该条，当 $m$ 充分大且 $\mathfrak{S}(m)\ge(\log m)^{-A}$ 时，
$$
r_{\mathfrak{M}}(m)
\ge
c_A\,\frac{m^{\beta-1}}{(\log m)^{A}}
$$
对某 $c_A>0$。由 $\mathrm{H}_{\mathrm{thr}}(A)$，
$$
\bigl|r_{\mathfrak{m}}(m)\bigr|
\le
\frac{m^{\beta-1}}{(\log m)^{A+1}}.
$$
故
$$
r(m)
=r_{\mathfrak{M}}+r_{\mathfrak{m}}
\ge
m^{\beta-1}(\log m)^{-A}
\Bigl(c_A-\frac{1}{\log m}\Bigr)
>0
$$
对充分大 $m$。从而存在非负整点表示，$m\in\mathcal{R}_{4,3,2}$。证毕。

**状态.** 蕴含箭头本身 **已证**；前置 $\mathrm{H}_{\mathrm{thr}}(A)$ **条件式**。合写：
$$
\mathrm{H}_{\mathrm{thr}}(A)
\ +\ 
\mathfrak{S}(m)\ge(\log m)^{-A}
\ \Longrightarrow\ 
m\in\mathcal{R}_{4,3,2}
\quad(m\gg_A 1).
$$

---

## L-Thr-4（已证接口）— 对接 L-Ekill-SS-2 / SSO-G5 / 弱 $\max\mathfrak{S}$

### （A）阈值填入 SS-2

L-Ekill-SS-2 的前置恰为「存在 $A$ 使 $\mathfrak{S}(m)\ge(\log m)^{-A}\Rightarrow m\in\mathcal{R}_{4,3,2}$」。由 L-Thr-3：该前置在 $\mathrm{H}_{\mathrm{thr}}(A)$ 下成立。故

**推论 L-Thr-4a（条件式）.** 若 $\mathrm{H}_{\mathrm{thr}}(A)$ 成立，则 L-Ekill-SS-2 的结论成立：充分大 $N\in\mathcal{F}_0$ 时
$$
\max_{1\le k\le K/2}\mathfrak{S}(N-2^k)\ll_A(\log N)^{-A}.
$$

### （B）与 L-SSO-5 弱 $\max\mathfrak{S}\gg 1$ 的拼合

L-SSO-5（G-SS，本身依赖 LS+AP）在其假设下给出
$$
\max_{k\le K}\mathfrak{S}(n-2^k)\gg 1.
$$
取 $A=1$：$\gg 1$ 强于 $(\log)^{-1}$。若再有 $\mathrm{H}_{\mathrm{thr}}(1)$，则由 L-Thr-3，该最大点 $m_\ast=n-2^{k_\ast}$ 可表，从而 $n\notin\mathcal{F}_0^{\mathrm{kill}}$（窗不能整埋于 $E$）。

**推论 L-Thr-4b（条件式）.**
$$
\mathrm{LS}+\mathrm{AP}+\mathrm{H}_{\mathrm{thr}}(1)
\ \Longrightarrow\ 
\mathcal{F}_0^{\mathrm{kill}}\text{ 仅有限}
$$
（经 L-SSO-5 的弱 $\max\mathfrak{S}\gg 1$ + L-Thr-3）。再经 L07 得 $x=0$ 型充分大可表。

**尖锐提醒（R4 审计保留）.** 无 $\mathrm{H}_{\mathrm{thr}}$ 时，$\max\mathfrak{S}\gg 1$ **不**蕴涵窗点可表——这正是本路线存在的理由。L-Thr-4b 把「轨道统计」与「圆法阈值」拆成**独立**载荷；二者皆未对真实输入关闭。

### （C）缺口 SSO-G5 的改写

| 原 SSO-G5 | 本路线改写 |
|-----------|------------|
| 直接要 SS-阈值全证 | 拆为 Thr-G1（$=\mathrm{H}_{\mathrm{thr}}$）+ 已证 L-Thr-3 |
| 「$\mathfrak{S}$ 下界 $\Rightarrow$ 可表」单块 | 主弧半边已证（L-Thr-1）；次弧为条件式 |

---

## L-Thr-5（已证结算）— 为何全阈值不可证；与次弧墙的精确距离

**命题.** 在仅使用本仓库已证次弧界（L-Circ-7/8、L-Dec-2、L-Hua-3/5、L-Lac-1…4）的前提下，**不能**推出任何 $A<\infty$ 的 $\mathrm{H}_{\mathrm{thr}}(A)$，因而**不能**无条件推出 SS-阈值。

**理由.**

1. **绝对值对照.** $\mathrm{H}_{\mathrm{thr}}^{\mathrm{abs}}(A)$ 要求 $\int_{\mathfrak{m}}|F|\ll m^{1/12}/(\log m)^{A+1}$。L-Dec-2 仅给
   $$
   \int_0^1|F|\ll_\varepsilon m^{13/24+\varepsilon},
   $$
   故次弧积分 $\ll_\varepsilon m^{13/24+\varepsilon}$。比值
   $$
   \frac{m^{13/24}}{m^{1/12}/(\log m)^{A+1}}
   =m^{11/24}(\log m)^{A+1}
   \to\infty.
   $$
2. **华氏凸障碍.** L-Hua-3/5：次临界 Hölder 箱内指数恒为 $13/24$，无对数级逃逸。  
3. **Lac 分裂.** L-Lac-3/7：Flat 仅 $(\log)^{O(1)}$ 杠杆；固定弱次弧下无半无条件 $m\ge m_0$。  
4. **振荡亦不免费.** 即使保留 $e(-m\alpha)$，无新的 Weyl/非对角输入（属建议路线 R5-Minor-Oscillation），不能从 $L^1$ 界 $m^{13/24}$ 落到 $m^{1/12}(\log)^{-O(1)}$。

**结论.** SS-阈值的全证 $\Leftrightarrow$ 本质关闭次弧到主项尺度（Thr-G1）；主弧与蕴含引理已就绪，等待点在 $\mathrm{H}_{\mathrm{thr}}$。

---

## L-Thr-6（草案 / 缺口清单）

| 缺口代号 | 内容 | 堵住则得 |
|----------|------|----------|
| **Thr-G1** | $\mathrm{H}_{\mathrm{thr}}(A)$（任固定 $A$，或等价 $\mathrm{H}_{\mathrm{thr}}^{\mathrm{abs}}$） | L-Thr-3 $\Rightarrow$ SS-阈值 |
| Thr-G2 | 主弧误差中 $\theta_0,\delta_0$ 的显式可发表常数（可选加固） | 有效 $m_0(A)$；形式追踪见 **R8 / L-Eff-1…5**（$N_0(\delta,A)$）；数值级属 Eff-G1 |
| Thr-G3 | 将 L-SSO-5 的 $\gg 1$ 升至 $(\log)^{-c}$（= SSO-G4）后与 $\mathrm{H}_{\mathrm{thr}}(c)$ 拼合 | **G4 开放**（R13 否证 L-Floor-1/2）；主路 L-Floor-7/8；拼合仍待 Thr-G1 |
| Thr-G4 | 真实 $E$ 上验证 LS+AP（SSO-G1–G3） | 经 L-Thr-4b 得 $\mathcal{F}_0$ 有限 |

**明确非声称.**

- 不证明 $\mathrm{H}_{\mathrm{thr}}$、H、H′。  
- 不证明 SS-Sync，不证明 $\mathcal{F}_0$ 有限，不证明原猜想。  
- 不声称「$\mathfrak{S}(m)\gg 1\Rightarrow m\in\mathcal{R}_{4,3,2}$」已无条件成立。

---

## 状态总表

| 编号 | 摘要 | 状态 |
|------|------|------|
| L-Thr-1(A) | $\mathfrak{J}(m)\asymp m^{\beta-1}>0$ | 已证 |
| L-Thr-1(B)(C) | 主弧 $r_{\mathfrak{M}}=\mathfrak{S}\mathfrak{J}+O(\cdots)$；$\mathfrak{S}\ge(\log)^{-A}\Rightarrow r_{\mathfrak{M}}\gg\mathfrak{S}\,m^{\beta-1}$ | 已证 |
| L-Thr-2 | 假设 $\mathrm{H}_{\mathrm{thr}}(A)$：次弧 $\ll m^{\beta-1}/(\log)^{A+1}$ | 条件式 |
| L-Thr-3 | $\mathrm{H}_{\mathrm{thr}}(A)+\mathfrak{S}\ge(\log)^{-A}\Rightarrow m\in\mathcal{R}_{4,3,2}$ | 已证（蕴含） |
| L-Thr-4a/b | 填入 SS-2；LS+AP+$\mathrm{H}_{\mathrm{thr}}\Rightarrow\mathcal{F}_0$ 有限 | 条件式接口 |
| L-Thr-5 | 已证次弧界 $\not\Rightarrow\mathrm{H}_{\mathrm{thr}}$（差 $m^{11/24}$） | 已证（结算） |
| L-Thr-6 | 缺口 Thr-G1–G4 | 缺口 |

---

## 链条图（条件式）

$$
\begin{CD}
\mathfrak{S}(m)\ge(\log m)^{-A}
@>{\mathrm{L\text{-}Thr\text{-}1}}>>
r_{\mathfrak{M}}\gg \mathfrak{S}\,m^{\beta-1} \\
@V{\mathrm{H}_{\mathrm{thr}}(A)}VV @VV{\mathrm{L\text{-}Thr\text{-}3}}V \\
|r_{\mathfrak{m}}|\le m^{\beta-1}/(\log)^{A+1}
@>>>
r(m)>0\ \Rightarrow\ m\in\mathcal{R}_{4,3,2}
\end{CD}
$$

与 P1 对接（另需轨道侧）：
$$
\mathrm{LS+AP}
\stackrel{\mathrm{L\text{-}SSO\text{-}5}}{\Longrightarrow}
\max\mathfrak{S}\gg 1
\stackrel{\mathrm{L\text{-}Thr\text{-}3}+\mathrm{H}_{\mathrm{thr}}(1)}{\Longrightarrow}
\text{窗点可表}
\Longrightarrow
\mathcal{F}_0^{\mathrm{kill}}\text{ 有限}
\stackrel{\mathrm{L07}}{\Longrightarrow}
x=0\text{ 型充分大}.
$$
