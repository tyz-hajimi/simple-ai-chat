# L-Eff：主弧有效化与条件式有效范围（路线 R8-Major-Effective）

> 路线 **R8-Major-Effective**（P09 攻关轮次 8，服务 **半无条件拼接**；加固 L-Thr 的 Thr-G2）。  
> 目标：在假设 $\mathrm{H}(\delta)$ 或 $\mathrm{H}_{\mathrm{thr}}(A)$ 下，把主弧贡献写成显式
> $$
> r_{\mathfrak{M}}(n)\ge c_0\,\mathfrak{S}(n)\,n^{1/12}-O(\text{误差}),
> $$
> 并**追踪** $c_0$ 与主弧宽度 $Q$ 的依赖，给出有效化引理：若 $\mathrm{H}$ 以具体 $\delta$ 成立且 $\mathfrak{S}(n)\ge(\log n)^{-A}$，则存在可描述的 $N_0(\delta,A)$ 使 $n\ge N_0$ 可表。  
> **定位.** 条件式有效范围（半无条件拼合的主弧半边），**不是**原猜想；**不**证明 $\mathrm{H}$ / $\mathrm{H}_{\mathrm{thr}}$。禁止数值穷举。

---

## 0. 符号与主弧宽度

沿用 L-Thr / L-Circ：
$$
\mathcal{R}_{4,3,2}=\{x^4+y^3+z^2:x,y,z\in\mathbb{N}_0\},
\qquad
\beta=\tfrac{13}{12},\qquad \beta-1=\tfrac{1}{12},
$$
$$
F=f_4f_3f_2,\qquad
r(n)=\int_0^1 F(\alpha)\,e(-n\alpha)\,\mathrm{d}\alpha
=r_{\mathfrak{M}}+r_{\mathfrak{m}}.
$$
奇异级数 $\mathfrak{S}(n)$、奇异积分 $\mathfrak{J}(n)$ 同 L-Thr-1。主弧 $\mathfrak{M}(Q)$ 按宽度 $Q/(qn)$ 的 Farey 剖分（$1\le Q\le n^{1/2}$）。

**量级.** 期望主项 $\mathfrak{S}(n)\,\mathfrak{J}(n)\asymp\mathfrak{S}(n)\,n^{1/12}$。

**假设 $\mathrm{H}(\delta)$（W-Circ 参数化）.** 存在 $C_{\mathrm{H}}<\infty$ 与 $n_{\mathrm{H}}$，使一切 $n\ge n_{\mathrm{H}}$，在下文固定的同一剖分 $Q$ 下，
$$
\bigl|r_{\mathfrak{m}(Q)}(n)\bigr|
\le
C_{\mathrm{H}}\,n^{1/12-\delta}.
$$
（绝对值变体 $\int_{\mathfrak{m}}|F|\le C_{\mathrm{H}}n^{1/12-\delta}$ 更强，同样适用。）

**假设 $\mathrm{H}_{\mathrm{thr}}(A)$.** 同 L-Thr-2：次弧 $\le n^{1/12}/(\log n)^{A+1}$。

---

## L-Eff-1（已证）— 主弧包的显式常数追踪

沿用 L-Thr-1(A)(B) 的绝对常数：
$$
c_{\mathfrak{J}}\,n^{1/12}
\le
\mathfrak{J}(n)
\le
C_{\mathfrak{J}}\,n^{1/12}
\quad(n\ge n_{\mathfrak{J}}),
$$
以及：存在 $\theta_0\in(0,1/12)$、$\delta_0,\eta_0>0$、$C_{\mathrm{maj}}<\infty$，使当 $1\le Q\le n^{\theta_0}$ 且 $n$ 充分大时
$$
r_{\mathfrak{M}(Q)}(n)
=
\mathfrak{S}(n)\,\mathfrak{J}(n)
+E_{\mathrm{maj}}(n;Q),
$$
其中误差满足
$$
\bigl|E_{\mathrm{maj}}(n;Q)\bigr|
\le
C_{\mathrm{maj}}\,n^{1/12}Q^{-\delta_0}
+
C_{\mathrm{maj}}\,n^{1/12-\eta_0}.
$$

**定义（本路线的主弧常数）.**
$$
c_0:=\tfrac12\,c_{\mathfrak{J}}.
$$
固定剖分宽度
$$
Q(n):=n^{\theta_0}
$$
（亦允许任意满足 $P_{1/4}\le Q(n)\le n^{\theta_0}$ 且 $Q(n)\to\infty$ 的选择；下文以 $Q=n^{\theta_0}$ 为标准）。

**引理 L-Eff-1.** 对一切 $n\ge n_{\ast}$（$n_{\ast}$ 仅依赖 $\theta_0,\delta_0,\eta_0,C_{\mathrm{maj}},c_{\mathfrak{J}}$），
$$
r_{\mathfrak{M}(Q)}(n)
\ge
c_0\,\mathfrak{S}(n)\,n^{1/12}
-
C_{\mathrm{maj}}\,n^{1/12}Q^{-\delta_0}
-
C_{\mathrm{maj}}\,n^{1/12-\eta_0}
-
\tfrac12\,c_{\mathfrak{J}}\,\mathfrak{S}(n)\,n^{1/12}\cdot\mathbf{1}_{\{\mathfrak{S}(n)>2\}},
$$
更实用的统一形（用 $\mathfrak{S}(n)\le C_{\mathfrak{S}}$ 的平凡上界，或把过大 $\mathfrak{S}$ 的情形单独吸收）：存在绝对 $C_E<\infty$ 使
$$
\boxed{
r_{\mathfrak{M}(Q)}(n)
\ge
c_0\,\mathfrak{S}(n)\,n^{1/12}
-
C_E\,n^{1/12}\bigl(Q^{-\delta_0}+n^{-\eta_0}\bigr).
}
$$

**证明概要.** 由 $r_{\mathfrak{M}}=\mathfrak{S}\mathfrak{J}+E_{\mathrm{maj}}$ 与 $\mathfrak{J}\ge c_{\mathfrak{J}}n^{1/12}$，
$$
r_{\mathfrak{M}}
\ge
c_{\mathfrak{J}}\,\mathfrak{S}\,n^{1/12}
-|E_{\mathrm{maj}}|
\ge
c_0\,\mathfrak{S}\,n^{1/12}
+\tfrac12 c_{\mathfrak{J}}\,\mathfrak{S}\,n^{1/12}
-C_{\mathrm{maj}}n^{1/12}(Q^{-\delta_0}+n^{-\eta_0}).
$$
当 $\mathfrak{S}(n)\ge 0$（奇异级数非负，L-SSO 框架）时后一项非负；即使仅用 $|\mathfrak{S}|\ll 1$ 的截断理论，亦可把 $\tfrac12 c_{\mathfrak{J}}|\mathfrak{S}|n^{1/12}$ 并入误差常数得统一 $C_E$。证毕。

**宽度依赖（追踪表）.**

| 量 | 依赖 | 备注 |
|----|------|------|
| $c_0$ | $=\frac12 c_{\mathfrak{J}}$ | **不**依赖 $Q$；仅依赖奇异积分下界 |
| $Q^{-\delta_0}$ | $Q=n^{\theta_0}\Rightarrow n^{-\theta_0\delta_0}$ | 主弧逼近误差主项 |
| $n^{-\eta_0}$ | Weyl/完备化残差 | 限制 $\theta_0$ 可取范围 |
| $C_E$ | $C_{\mathrm{maj}},c_{\mathfrak{J}}$ | 绝对；可发表化属 Eff-G1 |

**与 L-Thr-1(C) 的关系.** L-Thr-1(C) 的「$\gg_A$」即本条在 $\mathfrak{S}\ge(\log)^{-A}$、$Q=n^{\theta_0}$ 下误差 $o\bigl(\mathfrak{S}\,n^{1/12}\bigr)$ 的渐近叙述；本条保留减号后的显式误差，供有效 $N_0$ 使用。

---

## L-Eff-2（已证）— $\mathfrak{S}$ 下界下主弧压过误差的门槛

**引理 L-Eff-2.** 设 $Q=n^{\theta_0}$，$n\ge n_{\ast}$。若
$$
\mathfrak{S}(n)
\ge
(\log n)^{-A}
$$
且
$$
n^{\theta_0\delta_0}
\ge
\frac{4C_E}{c_0}\,(\log n)^{A},
\qquad
n^{\eta_0}
\ge
\frac{4C_E}{c_0}\,(\log n)^{A},
$$
则
$$
r_{\mathfrak{M}(Q)}(n)
\ge
\tfrac12\,c_0\,\mathfrak{S}(n)\,n^{1/12}
\ge
\tfrac12\,c_0\,n^{1/12}(\log n)^{-A}.
$$

**证明.** 由 L-Eff-1，
$$
r_{\mathfrak{M}}
\ge
c_0\mathfrak{S}\,n^{1/12}
-C_E n^{1/12}(n^{-\theta_0\delta_0}+n^{-\eta_0}).
$$
两门槛恰使每个误差项 $\le \tfrac14 c_0\mathfrak{S}\,n^{1/12}$，故总误差 $\le \tfrac12 c_0\mathfrak{S}\,n^{1/12}$。证毕。

**有效门槛函数.** 定义
$$
N_{\mathrm{maj}}(A)
:=
\min\Bigl\{
N\ge n_{\ast}:
\forall n\ge N,\ 
n^{\min(\theta_0\delta_0,\eta_0)}
\ge
\frac{4C_E}{c_0}(\log n)^{A}
\Bigr\}.
$$
则 $n\ge N_{\mathrm{maj}}(A)$ 且 $\mathfrak{S}(n)\ge(\log n)^{-A}$ 时 L-Eff-2 的结论成立。特别地
$$
N_{\mathrm{maj}}(A)
\ll_{A}
\exp\bigl(O(A\log A)\bigr)
\quad\text{（粗估；精确依赖 Eff-G1 常数）},
$$
更紧的多项式级下界：存在仅依赖 $(\theta_0,\delta_0,\eta_0,c_0,C_E)$ 的 $C_{\mathrm{poly}}$ 使
$$
N_{\mathrm{maj}}(A)
\le
\max\bigl\{n_{\ast},\ \bigl(C_{\mathrm{poly}}(\log(2+A))^{A}\bigr)^{1/\min(\theta_0\delta_0,\eta_0)}\bigr\}
$$
在「先取 $n$ 大到 $\log n\le n^{\varepsilon}$」的标准 bootstrapping 下可写成显式（细节属有效解析数论惯例，此处登记形式即可）。

---

## L-Eff-3（已证拼合）— 在 $\mathrm{H}(\delta)$ 下的显式正性

**引理 L-Eff-3.** 设 $\mathrm{H}(\delta)$ 以常数 $C_{\mathrm{H}},n_{\mathrm{H}}$ 成立。固定 $A<\infty$。若 $n$ 满足
$$
n\ge\max\{n_{\mathrm{H}},N_{\mathrm{maj}}(A)\}
\quad\text{且}\quad
\mathfrak{S}(n)\ge(\log n)^{-A},
$$
以及次弧压过条件
$$
\tfrac12\,c_0\,n^{1/12}(\log n)^{-A}
>
C_{\mathrm{H}}\,n^{1/12-\delta},
$$
即
$$
n^{\delta}
>
\frac{2C_{\mathrm{H}}}{c_0}\,(\log n)^{A},
$$
则
$$
r(n)=r_{\mathfrak{M}}+r_{\mathfrak{m}}>0,
$$
从而 $n\in\mathcal{R}_{4,3,2}$。

**证明.** L-Eff-2 给 $r_{\mathfrak{M}}\ge\tfrac12 c_0 n^{1/12}(\log n)^{-A}$；$\mathrm{H}(\delta)$ 给 $|r_{\mathfrak{m}}|\le C_{\mathrm{H}}n^{1/12-\delta}$。相减即正。证毕。

---

## L-Eff-4（有效化引理，条件式）— $N_0(\delta,A)$

**定义.**
$$
N_0(\delta,A)
:=
\min\Bigl\{
N\ge\max\{n_{\mathrm{H}},N_{\mathrm{maj}}(A)\}:
\forall n\ge N,\ 
n^{\delta}
\ge
\frac{2C_{\mathrm{H}}}{c_0}\,(\log n)^{A}+1
\Bigr\}.
$$
（若采用 $\mathrm{H}_{\mathrm{thr}}(A)$ 而非 $\mathrm{H}(\delta)$，则把次弧门槛换成 $(\log n)^{A+1}\ge 2/c_0$，见 L-Eff-5。）

**引理 L-Eff-4（条件式有效范围）.**  
假设 $\mathrm{H}(\delta)$ 成立（带具体 $\delta>0$ 与隐含常数 $C_{\mathrm{H}}$）。则对任意固定 $A<\infty$，一切满足
$$
n\ge N_0(\delta,A)
\quad\text{且}\quad
\mathfrak{S}(n)\ge(\log n)^{-A}
$$
的整数 $n$ 皆属于 $\mathcal{R}_{4,3,2}$。

特别地：$N_0(\delta,A)<\infty$ 且满足粗糙上界
$$
N_0(\delta,A)
\le
\max\Biggl\{
n_{\mathrm{H}},\
N_{\mathrm{maj}}(A),\ 
\Biggl(\frac{4C_{\mathrm{H}}}{c_0}(\log M)^{A}\Biggr)^{1/\delta}
\Biggr\}
$$
其中 $M$ 为使 $(\log M)^{A/\delta}\le M^{1/2}$ 的任意固定门槛（标准自洽选取）。

**状态.** 蕴含箭头与 $N_0$ 的**形式可定义性**已证；前置 $\mathrm{H}(\delta)$ **条件式**。合写：
$$
\mathrm{H}(\delta)
\ +\ 
\mathfrak{S}(n)\ge(\log n)^{-A}
\ \Longrightarrow\ 
n\in\mathcal{R}_{4,3,2}
\quad\bigl(n\ge N_0(\delta,A)\bigr).
$$

**半无条件拼接语义.**  
- **无条件半边**：主弧包 L-Eff-1/2（已证；常数依赖登记于 Eff-G1）。  
- **条件半边**：次弧 $\mathrm{H}(\delta)$（或 $\mathrm{H}_{\mathrm{thr}}$）。  
- **拼合输出**：显式有效范围 $n\ge N_0(\delta,A)$（相对 L-Thr-3 的「充分大」多了 $\delta$-依赖的可追踪门槛）。  
这**不是**「无条件 $n\ge N_0\Rightarrow$ 可表」；无 $\mathrm{H}$ 时 $N_0$ 公式中的 $C_{\mathrm{H}},n_{\mathrm{H}}$ 不存在。

---

## L-Eff-5（已证变体）— $\mathrm{H}_{\mathrm{thr}}$ 版有效门槛

**引理 L-Eff-5.** 设 $\mathrm{H}_{\mathrm{thr}}(A)$ 成立。定义
$$
N_0^{\mathrm{thr}}(A)
:=
\max\Bigl\{
N_{\mathrm{maj}}(A),\ 
m_1(A),\ 
\min\{N:\forall n\ge N,\ \log n\ge 2/c_0\}
\Bigr\},
$$
其中 $m_1(A)$ 为 L-Thr-2 中 $\mathrm{H}_{\mathrm{thr}}$ 的起始点。则一切
$$
n\ge N_0^{\mathrm{thr}}(A)
\quad\text{且}\quad
\mathfrak{S}(n)\ge(\log n)^{-A}
$$
满足 $n\in\mathcal{R}_{4,3,2}$。

**证明.** 同 L-Thr-3，但用 L-Eff-2 的显式主弧下界替换「$\gg_A$」：  
$$
r_{\mathfrak{M}}\ge\tfrac12 c_0 n^{1/12}(\log n)^{-A},\qquad
|r_{\mathfrak{m}}|\le n^{1/12}(\log n)^{-(A+1)},
$$
故当 $\log n>2/c_0$ 时 $r(n)>0$。证毕。

**对照.**

| 次弧假设 | 有效门槛主因 | 相对主项 |
|----------|--------------|----------|
| $\mathrm{H}(\delta)$ | $n^{\delta}\gg(\log n)^{A}$ | 幂次节省 $\Rightarrow$ $N_0$ 多项式/亚指数于 $1/\delta$ |
| $\mathrm{H}_{\mathrm{thr}}(A)$ | $\log n\gg 1/c_0$ | 仅对数；门槛几乎由 $N_{\mathrm{maj}}(A)$ 决定 |

---

## L-Eff-6（已证接口）— 对接 L-Thr / SS-2 / 半无条件叙事

### （A）与 L-Thr-3 的精细化

L-Thr-3 断言存在某 $m_2(A)$；L-Eff-4/5 把 $m_2$ **改写为**依赖表 $(c_0,C_E,\theta_0,\delta_0,\eta_0,C_{\mathrm{H}},\delta,A)$ 的 $N_0$。逻辑强度相同；可发表常数属 Eff-G1。

### （B）填入 L-Ekill-SS-2

同 L-Thr-4a：若 $\mathrm{H}(\delta)$ 或 $\mathrm{H}_{\mathrm{thr}}(A)$ 成立，则「$\mathfrak{S}\ge(\log)^{-A}\Rightarrow$ 可表」对 $n\ge N_0$ 有效成立，从而 SS-2 的坏窗同步结论在有效范围内可用。

### （C）与 L-Lac-7 的区分（防误读）

| 命题 | 内容 | 本路线 |
|------|------|--------|
| L-Lac-7 | 固定弱次弧 $\theta>0$ **无**无条件半无条件 $N\ge N_0$ | **不冲突**：彼处无假设 H |
| L-Eff-4 | **假定** $\mathrm{H}(\delta)$ 后有条件式 $N_0(\delta,A)$ | 条件式；服务拼接 |

---

## L-Eff-7（草案 / 缺口）

| 缺口代号 | 内容 | 堵住则得 |
|----------|------|----------|
| **Eff-G1** | $c_{\mathfrak{J}},\theta_0,\delta_0,\eta_0,C_{\mathrm{maj}},C_E$ 的可发表数值/显式不等式 | 数值级 $N_0$ 上界（仍条件于 H） |
| Eff-G2 | 最优主弧宽度 $Q=n^{\theta}$ 的 $\theta$-平衡（与次弧技术联动） | 略小的 $N_0$ |
| Eff-G3 | 将 $N_0(\delta,A)$ 写入 SS-Sync / E-kill 有效窗长 | 定量坏窗定理 |
| **Thr-G1**（外部） | 证明任一 $\mathrm{H}(\delta)$ 或 $\mathrm{H}_{\mathrm{thr}}(A)$ | 无条件有效范围（= 原猜想充分大） |

**明确非声称.**

- 不证明 $\mathrm{H}$、$\mathrm{H}_{\mathrm{thr}}$、原猜想。  
- 不声称存在无条件的绝对 $N_0$ 使一切 $n\ge N_0$ 可表。  
- 不声称 $c_0$ 的十进制数值已算出（仅追踪到 $c_{\mathfrak{J}}/2$）。  
- 「半无条件」此处 $=$「主弧无条件 + 次弧假设 $\Rightarrow$ 有效范围」；$\ne$ L-Lac-7 所否证的捷径。

---

## 状态总表

| 编号 | 摘要 | 状态 |
|------|------|------|
| L-Eff-1 | $r_{\mathfrak{M}}\ge c_0\mathfrak{S}\,n^{1/12}-C_E n^{1/12}(Q^{-\delta_0}+n^{-\eta_0})$；$c_0=\frac12 c_{\mathfrak{J}}$ | 已证 |
| L-Eff-2 | $\mathfrak{S}\ge(\log)^{-A}$ + 宽度门槛 $\Rightarrow r_{\mathfrak{M}}\ge\frac12 c_0\mathfrak{S}\,n^{1/12}$ | 已证 |
| L-Eff-3 | $\mathrm{H}(\delta)$ 下显式正性条件 | 已证拼合 |
| L-Eff-4 | **L-Eff-***：$\mathrm{H}(\delta)+\mathfrak{S}\ge(\log)^{-A}\Rightarrow n\ge N_0(\delta,A)$ 可表 | 条件式（有效化） |
| L-Eff-5 | $\mathrm{H}_{\mathrm{thr}}$ 版 $N_0^{\mathrm{thr}}(A)$ | 条件式 |
| L-Eff-6 | 对接 L-Thr / SS-2；与 L-Lac-7 区分 | 已证接口 |
| L-Eff-7 | 缺口 Eff-G1–G3；外部 Thr-G1 | 缺口 |

---

## 链条图（条件式有效范围）

$$
\begin{CD}
\mathfrak{S}(n)\ge(\log n)^{-A}
@>{\mathrm{L\text{-}Eff\text{-}1/2}}>>
r_{\mathfrak{M}}\ge \tfrac12 c_0\,\mathfrak{S}\,n^{1/12} \\
@V{\mathrm{H}(\delta)\ \text{或}\ \mathrm{H}_{\mathrm{thr}}}VV @VV{\mathrm{L\text{-}Eff\text{-}4/5}}V \\
|r_{\mathfrak{m}}|\le C_{\mathrm{H}}n^{1/12-\delta}
@>>>
n\ge N_0(\delta,A)\ \Rightarrow\ r(n)>0
\end{CD}
$$

**常数依赖一览.**
$$
c_0=\tfrac12 c_{\mathfrak{J}},
\qquad
Q=n^{\theta_0},
\qquad
N_0=N_0\bigl(\delta,A;\,c_0,C_E,\theta_0\delta_0,\eta_0,C_{\mathrm{H}}\bigr).
$$
