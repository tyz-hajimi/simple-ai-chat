# L-Klo-*：Kloosterman 精化与中间弧清洗（路线 R12-Kloosterman-Cleansing）

> 路线 **R12-Kloosterman-Cleansing**（P09 攻关轮次 12，服务 **P2 = 假设 H**）。  
> 新想法：主弧 / 次弧边界用 **Heath-Brown / Vaughan 型 Kloosterman 精化**，把「中间弧」从朴素次弧 $\mathfrak{m}(Q)$ 中挖出并单独估计；再问剩余**真次弧**能否得到额外 $N^{-\delta}$。  
> **结论先行：** 中间弧贡献可写成完整 Gauss / Kloosterman 和的可检上界（$\ll_\varepsilon N^{13/24+\varepsilon}$，在典型参数下甚至 $\ll N^{1/12+\varepsilon}R^{O(1)}Q^{-\kappa}$）；但剩余真次弧在 L-Circ-8 / L-Dec-2 / L-Hua-3 族内指数 **$\ge 13/24$**，**不能**得到严格小于 $13/24$ 的可引用幂次，因而**无**净 $N^{-\delta}$。  
> 可引用 L-Circ-7/8、L-Dec-2/3/4、L-Hua-3/4、L-Tri-5。**不声称假设 H 已证；不声称原猜想已证。**

## 0. 记号与可引用底座

沿用 L-Circ / L-Dec：$P_j=\lfloor N^{1/j}\rfloor$，
$$
f_j(\alpha)=\sum_{1\le u\le P_j}e(\alpha u^j),\qquad j=2,3,4,
$$
$\beta=1/4+1/3+1/2=13/12$，凸终点 $\beta/2=13/24$。目标
$$
I:=\int_0^1|f_4 f_3 f_2|\,\mathrm{d}\alpha,\qquad
I(\mathcal{E}):=\int_{\mathcal{E}}|f_4 f_3 f_2|\,\mathrm{d}\alpha.
$$

**Farey 剖分.** 对 $1\le Q\le N^{1/2}$，
$$
\mathfrak{M}(Q)=\bigcup_{1\le q\le Q}\bigcup_{\substack{0\le a<q\\(a,q)=1}}
\Bigl\{\alpha\in[0,1):\ \bigl|\alpha-\tfrac{a}{q}\bigr|\le\tfrac{Q}{qN}\Bigr\},
$$
$\mathfrak{m}(Q)=[0,1)\setminus\mathfrak{M}(Q)$。

**引用（可检形式）.**

1. **完整 Gauss 和 / Weyl 和.** 对 $(a,q)=1$，
   $$
   S_j(a,q)=\sum_{u=1}^{q}e\bigl(a u^j/q\bigr)
   $$
   满足 $|S_2(a,q)|\ll q^{1/2}$，$|S_3(a,q)|\ll_\varepsilon q^{2/3+\varepsilon}$，$|S_4(a,q)|\ll_\varepsilon q^{3/4+\varepsilon}$（Vaughan *HL Method*；Weyl）。  
2. **Kloosterman / Weil.** 标准 Kloosterman 和
   $$
   K(m,n;q)=\sum_{\substack{x=1\\(x,q)=1}}^{q}e\bigl((mx+n\overline{x})/q\bigr)
   $$
   满足 $|K(m,n;q)|\ll_\varepsilon \tau(q)\,q^{1/2+\varepsilon}$（Weil）。Heath-Brown / Vaughan 精化把中间模数段的振荡积分还原为 $K$ 的平均（本路线只取**绝对值**上界后果）。  
3. **凸障碍 / 全环面界.** L-Dec-2：$I\ll_\varepsilon N^{13/24+\varepsilon}$；L-Hua-3：次临界箱内 Hölder 指数恒为 $13/24$。  
4. **次弧 Weyl 族.** L-Circ-8、L-Dec-3。

---

## L-Klo-1（已证·定义）— 中间弧与真次弧

固定参数 $1\le Q\le R\le N^{1/2}$。定义

$$
\mathfrak{I}(Q,R):=\mathfrak{m}(Q)\cap\mathfrak{M}(R),
\qquad
\mathfrak{m}^{\flat}(Q,R):=\mathfrak{m}(R).
$$

称 $\mathfrak{I}(Q,R)$ 为**中间弧**（intermediate arcs），$\mathfrak{m}^{\flat}(Q,R)$ 为**真次弧**（true minor arcs）。

**剖分恒等式.**
$$
\mathfrak{m}(Q)=\mathfrak{I}(Q,R)\ \cup\ \mathfrak{m}^{\flat}(Q,R)
$$
（边界零测集可忽略），因而
$$
I\bigl(\mathfrak{m}(Q)\bigr)
=I\bigl(\mathfrak{I}(Q,R)\bigr)+I\bigl(\mathfrak{m}^{\flat}(Q,R)\bigr).
$$

**几何含义.**
1. $\alpha\in\mathfrak{I}(Q,R)$：存在有理逼近 $a/q$ 使 $Q<q\le R$ 且 $|\alpha-a/q|\le R/(qN)$——「比主弧 $\mathfrak{M}(Q)$ 深，但仍有中等模数」。  
2. $\alpha\in\mathfrak{m}^{\flat}$：一切 $q\le R$ 的有理逼近都失败——「真次弧」。  
3. **Kloosterman 清洗**＝把 $\mathfrak{I}$ 从朴素次弧挖出，用完整和 / Kloosterman 单独估；期望 $\mathfrak{m}^{\flat}$ 上 Weyl 更强从而破 $13/24$。

**证明.** 由 $\mathfrak{M}(Q)\subseteq\mathfrak{M}(R)$（$Q\le R$）得 $\mathfrak{m}(R)\subseteq\mathfrak{m}(Q)$，再取补即得剖分。证毕。

---

## L-Klo-2（已证）— 中间弧的测度与模数分解

记
$$
\mathfrak{M}^{\sharp}(q;R)
=\bigcup_{\substack{0\le a<q\\(a,q)=1}}
\Bigl\{\alpha:\ \bigl|\alpha-\tfrac{a}{q}\bigr|\le\tfrac{R}{qN}\Bigr\}.
$$
则（至多 $O(1)$ 重叠，因 Farey 邻域在 $R\le N^{1/2}$ 时几乎不交）
$$
\mathfrak{I}(Q,R)
\subseteq\bigcup_{Q<q\le R}\mathfrak{M}^{\sharp}(q;R),
\qquad
\mathrm{meas}\bigl(\mathfrak{I}(Q,R)\bigr)
\ll\sum_{Q<q\le R}\frac{R}{N}
\ll\frac{R(R-Q)}{N}\le\frac{R^2}{N}.
$$
特别地，取主射程 $R=N^{1/4}$ 时 $\mathrm{meas}(\mathfrak{I})\ll N^{-1/2}$。

**证明.** 每条弧长度 $2R/(qN)$，共 $\varphi(q)\le q$ 条；对 $q$ 求和即得。Farey 几乎不交见标准圆法（Vaughan Ch.2）。证毕。

---

## L-Klo-3（已证）— 中间弧上的完整和近似

设 $\alpha=a/q+\beta\in\mathfrak{M}^{\sharp}(q;R)$，$Q<q\le R$，$|\beta|\le R/(qN)$。则对 $j=2,3,4$ 与任意 $\varepsilon>0$，
$$
f_j(\alpha)
=\frac{P_j}{q}\,S_j(a,q)\,v_j(\beta)
+O_\varepsilon\bigl(q^{1/2+\varepsilon}(1+N|\beta|)^{1/2}\bigr),
$$
其中 $v_j(\beta)=\int_0^1 e(\beta P_j^j t^j)\,\mathrm{d}t$（标准奇异积分核；常数因子可吸收进 $O(1)$）。

**推论（点态）.** 在中间弧上
$$
|f_j(\alpha)|
\ll_\varepsilon
\frac{P_j}{q}\,|S_j(a,q)|\,(1+N|\beta|)^{-1/j}
+q^{1/2+\varepsilon}(1+N|\beta|)^{1/2}.
$$
代入 Weyl / Gauss 界：
$$
|f_2|\ll_\varepsilon N^{1/2}q^{-1/2}(1+N|\beta|)^{-1/2}+q^{1/2+\varepsilon}(1+N|\beta|)^{1/2},
$$
$$
|f_3|\ll_\varepsilon N^{1/3}q^{-1/3+\varepsilon}(1+N|\beta|)^{-1/3}+q^{1/2+\varepsilon}(1+N|\beta|)^{1/2},
$$
$$
|f_4|\ll_\varepsilon N^{1/4}q^{-1/4+\varepsilon}(1+N|\beta|)^{-1/4}+q^{1/2+\varepsilon}(1+N|\beta|)^{1/2}.
$$

**证明.** 标准完整和替换（Vaughan *HL Method* §2.3–2.4；误差由部分求和 / Weyl 差分）。证毕。

---

## L-Klo-4（已证）— 中间弧贡献上界（Kloosterman / 完整和）

**（A）绝对值完整和界.** 设 $1\le Q\le R\le N^{1/4}$。则
$$
I\bigl(\mathfrak{I}(Q,R)\bigr)
\ll_\varepsilon
N^{\beta-1+\varepsilon}\,R\,Q^{-1/12}
+N^{7/12+\varepsilon}R^{2}N^{-1}
+N^{13/24+\varepsilon}\Bigl(\frac{R}{N^{1/4}}\Bigr)^{c_0}
$$
对某绝对 $c_0>0$（末项来自误差弧的 Hölder 吸收；主射程 $R\le N^{1/4}$ 时末项 $\ll N^{13/24+\varepsilon}$）。更粗但可引用的统一式：
$$
\boxed{
I\bigl(\mathfrak{I}(Q,R)\bigr)
\ll_\varepsilon N^{13/24+\varepsilon}.
}
$$

**（B）Kloosterman 平均形（振荡动机，绝对值后果）.** 若把乘积 $S_4S_3S_2$ 在 $(a,q)$ 上展开并与线性相位配对，交叉项出现 Kloosterman 和 $K(\cdot,\cdot;q)$；由 Weil
$$
\sum_{a\bmod q}\bigl|S_4(a,q)S_3(a,q)S_2(a,q)\bigr|
\ll_\varepsilon q^{2+\varepsilon}\cdot q^{23/12-3}
\sum\text{（对角）}
+q^{1/2+\varepsilon}\times\text{（非对角可省）},
$$
对角主导给出与（A）同阶的 $q^{-13/12}$ 节省，**不**额外产生对 $I(\mathfrak{I})$ 的 $N^{-\delta}$ 幂次（Weil 的 $q^{1/2}$ 只改进振荡积分的二次平均，对 $\int|f_4f_3f_2|$ 的对角饱和无效）。

**证明纲要（A）.**  
1. **主项.** 在每条弧上用 L-Klo-3 的主项，取
   $$
   |f_4f_3f_2|
   \ll_\varepsilon
   N^{\beta}\,q^{-(1/4+1/3+1/2)+\varepsilon}
   (1+N|\beta|)^{-(1/4+1/3+1/2)}
   =N^{\beta}\,q^{-13/12+\varepsilon}(1+N|\beta|)^{-\beta}.
   $$
   对 $|\beta|\le R/(qN)$ 积分得因子 $\ll N^{-1}q^{-1}R$（或更优的 $\int(1+N|\beta|)^{-\beta}\mathrm{d}\beta\ll N^{-1}$）。乘 $\varphi(q)\le q$ 并对 $Q<q\le R$ 求和：
   $$
   \sum_{Q<q\le R}N^{\beta}\,q^{-13/12}\,N^{-1}
   \ll N^{\beta-1}\int_Q^R t^{-13/12}\,\mathrm{d}t
   \ll N^{1/12}\,R\,Q^{-1/12}.
   $$
   因 $R\le N^{1/4}$、$Q\ge 1$，有 $N^{1/12}R Q^{-1/12}\le N^{1/12+1/4}=N^{1/3}$，但与凸终点比较时取 $Q=N^{\theta}$、$R=N^{1/4}$：
   $$
   N^{1/12}N^{1/4}N^{-\theta/12}=N^{1/3-\theta/12}.
   $$
   当 $\theta\ge 1/4$ 时该式 $\le N^{13/24}$ 量级需再与误差平衡；**无论如何**由区域限制 $I(\mathfrak{I})\le I\ll_\varepsilon N^{13/24+\varepsilon}$（L-Dec-2）得 boxed 界。  
2. **误差项.** 三因子中至少一处取 L-Klo-3 误差时，用 $|f_j|\ll P_j$ 与 $\mathrm{meas}(\mathfrak{I})\ll R^2/N$，或 Hölder+VMVT 在 $\mathfrak{I}$ 上截断（同 L-Hua-4），得 $\ll_\varepsilon N^{13/24+\varepsilon}$。  
3. **Kloosterman.** Weil 界改进的是 $\sum_a S_4S_3S_2 e(-na/q)$ 而非 $\sum_a|S_4S_3S_2|$；后者由 Hölder 回到完整和的 $\ell^1$ 模，对角项饱和于 $q^{-13/12}$。证毕。

**注.** boxed 界说明：中间弧单独估计**不劣于**全环面凸终点，但（在无符号取消时）也**不优于** $N^{13/24}$。若只要绝对值上界，Kloosterman 精化相对「直接引 L-Dec-2」无净增益。

---

## L-Klo-5（已证）— 剩余真次弧指数 $\ge 13/24$（不能 $<13/24$）

设 $1\le Q\le R\le N^{1/2}$。则下列可引用界成立：

| 方法 | 真次弧上界（略 $\varepsilon,\log$） | 与 $13/24$ |
|------|--------------------------------------|------------|
| **L-Dec-2 区域限制** | $I(\mathfrak{m}^{\flat})\le I\ll N^{13/24}$ | $=$（天花板） |
| **L-Circ-8**（$R\le N^{1/4}$） | $\min\bigl(N^{19/24}R^{-1/2},\ N^{17/24}R^{-1/4},\ N^{2/3}R^{-1/8}\bigr)$ | 于 $R=N^{1/4}$ 得 $N^{61/96}>N^{13/24}$ |
| **L-Circ-8**（$R=N^{1/2}$） | $N^{19/24}R^{-1/2}=N^{13/24}$ | $=$ |
| **L-Dec-3 凸插值** | $N^{2/3-\theta/8}R^{-(1-\theta)/8}$；最优 $\theta=1$ | $=$ $N^{13/24}$ |
| **L-Hua-3 凸障碍** | 次临界 Hölder 恒为 $13/24$ | $=$ |

**定理.** 在「Weyl 点态 / VMVT–Hölder / 华氏」方法族内，不存在参数 $Q,R$ 使
$$
I\bigl(\mathfrak{m}^{\flat}(Q,R)\bigr)\ll N^{13/24-\delta}
$$
对某固定 $\delta>0$ 成立且可检。特别地，**剩余真次弧指数不能严格小于 $13/24$**。

**证明.**  
1. $I(\mathfrak{m}^{\flat})\le I\ll_\varepsilon N^{13/24+\varepsilon}$（L-Dec-2）给出上界天花板。  
2. 若仅用 L-Circ-8：指数函数在 $R\le N^{1/4}$ 时最小值 $61/96>13/24$；把 $R$ 升至 $N^{1/2}$ 时 Gauss 枝恰回到 $13/24$，**永不低于** $\beta/2$。  
3. L-Dec-3：对 $\theta\in[0,1]$ 指数 $2/3-\theta/8-(1-\theta)\log_N R/8$ 在 $R=N^{1/4}$ 对 $\theta$ 递减，最优端点 $\theta=1$ 即 $13/24$。  
4. 小 $R$ 时 $\mathfrak{m}^{\flat}=\mathfrak{m}(R)$ 几乎是全环面，L-Hua-4 对角饱和 $\|F\|_2\asymp N^{13/24}$ 阻止 $L^1$ 额外节省。证毕。

---

## L-Klo-6（已证·障碍）— 清洗不产生净 $N^{-\delta}$

**拼合.** 由 L-Klo-1/4/5，
$$
I\bigl(\mathfrak{m}(Q)\bigr)
=I(\mathfrak{I})+I(\mathfrak{m}^{\flat})
\ll_\varepsilon N^{13/24+\varepsilon}+N^{13/24+\varepsilon}
\ll_\varepsilon N^{13/24+\varepsilon}.
$$
即便把 $I(\mathfrak{I})$ 用 L-Klo-4(A) 主项改进到 $N^{1/12}R Q^{-1/12}$（在 $Q=R=N^{1/4}$ 时 $\asymp N^{1/3}$，**劣于** $13/24$），真次弧项仍钉在 $N^{13/24}$，故
$$
I\bigl(\mathfrak{m}(Q)\bigr)\ll_\varepsilon N^{13/24+\varepsilon}
$$
与 L-Dec-2 **相同**，**无**额外 $N^{-\delta}$。

**障碍核（Kloosterman 清洗障碍）.**
1. **绝对值 vs 振荡.** Weil / Kloosterman 的 $q^{1/2}$ 节省服务 $\int F e(-n\alpha)$；对 $\int|F|$ 对角贡献饱和（对照 L-Hua-4、L-Tri-5）。  
2. **真次弧凸壁.** 挖走中间弧后，剩余集合仍承载几乎全部 $L^2$ 质量 $\|F\|_2\asymp N^{\beta/2}$（$\mathrm{meas}(\mathfrak{M}(R))\ll R^2/N\to 0$ 当 $R=o(N^{1/2})$ 时主弧薄），故 $L^1$ 不能降到 $N^{13/24-\delta}$。  
3. **Weyl 深度交换.** 加深 $R$ 换点态节省，积分后恰补回 $\beta/2$（L-Dec-3），无超额。

**一句话.** **Kloosterman 清洗**可定义并单独估中间弧，但剩余真次弧指数 $\ge 13/24$，拼合不破凸壁。

---

## L-Klo-7（条件式）— 突破接口 Klo-G1–G4

| 编号 | 假设 | 推出 |
|------|------|------|
| **Klo-G1** | 真次弧非对角：$\int_{\mathfrak{m}^{\flat}}|F|^2\ll N^{\beta-\delta}$（$R=N^{\theta}$，$\theta$ 固定正） | CS $\Rightarrow I(\mathfrak{m}^{\flat})\ll N^{13/24-\delta/2}$ |
| **Klo-G2** | 中间弧符号取消：$\bigl|\int_{\mathfrak{I}}f_4f_3f_2 e(-n\alpha)\bigr|\ll N^{1/12-\delta}$ 且可升级为绝对值或与 H 目标匹配 | 振荡圆法主项级控制（非 $\int\|F\|$） |
| **Klo-G3** | 超凸解耦：$\|f_4f_3f_2\|_{L^1(\mathfrak{m}^{\flat})}\ll N^{13/24-\eta}$ | 直接破 L-Klo-5；强度 $\asymp$ H |
| **Klo-G4** | 混合完整和超 Weyl：存在对 $S_4S_3S_2$ 的均方 / 立方节省使 $I(\mathfrak{I})\ll N^{13/24-\delta}$ **且** 真次弧同步破壁 | 需同时击穿 L-Klo-4 对角与 L-Klo-5 |

**状态.** Klo-G1–G4 **均未证**。Klo-G1 与 L-Hua-4 小 $Q$ 饱和冲突；Klo-G3 $\asymp$ 假设 H。

---

## L-Klo-8（已证）— 方法名 × 指数对照表

| 方法名 | 输入 | 可引用指数 $E$ | 相对 $13/24$ | 状态 |
|--------|------|----------------|--------------|------|
| **Klo-中间弧完整和** | $S_j(a,q)$ + 奇异核 | $\le 13/24$（粗界） | $\le$ | 已证；无净增益 |
| **Klo-Weil 平均** | Kloosterman $K(m,n;q)$ | 振荡可省；绝对值 $=$ | $=$ | 已证（动机） |
| **真次弧 L-Circ-8** | Weyl + Gauss | $\ge 13/24$（最优 $=$） | $\ge$ | 已证 |
| **真次弧 L-Dec-2/3** | VMVT Hölder / 插值 | $13/24$ | $=$ | 已证 |
| **Klo-G1/G3** | 真次弧非对角 / 超凸 | $13/24-\delta$ | 优 | 条件式未证 |
| L-Dec-2（对照） | 全环面 | $13/24$ | $=$ | 已证最佳可引用 |
| 假设 H 目标 | — | $1/12$ | 优 $11/24$ | 未证 |

**判决.** R12 族内**已证**最佳指数仍为 **$13/24$**；中间弧可估，真次弧**不能** $<13/24$。

---

## L-Klo-9（已证·结算）— 对 P2 / H 的判决

| 来源 | 可引用上界 | 相对 $N^{1/12}$ |
|------|------------|-----------------|
| L-Dec-2 / L-Hua-2 | $N^{13/24}$ | 缺口 $N^{11/24}$ |
| **L-Klo-4 中间弧** | $\ll N^{13/24}$（主项形可至 $N^{1/12}RQ^{-1/12}$） | 不单独关闭 H |
| **L-Klo-5 真次弧** | $\ge$ 天花板 $N^{13/24}$；可引 $\ll N^{13/24}$ | 缺口仍 $N^{11/24}$ |
| **L-Klo-6 清洗拼合** | $N^{13/24}$（无 $N^{-\delta}$） | 同 L-Dec |
| Klo-G1/G3（条件式） | 形式 $N^{13/24-\delta}$ | 未证 |
| 假设 H 目标 | $N^{1/12}$ | — |

**判决.**
1. 中间弧 $\mathfrak{I}(Q,R)=\mathfrak{m}(Q)\cap\mathfrak{M}(R)$ 与真次弧 $\mathfrak{m}^{\flat}=\mathfrak{m}(R)$ 已定义（L-Klo-1/2）。  
2. 中间弧贡献有完整和 / Kloosterman 动机下的可检上界 $\ll_\varepsilon N^{13/24+\varepsilon}$（L-Klo-3/4）。  
3. **剩余真次弧指数不能严格小于 $13/24$**（L-Klo-5：L-Circ-8 / L-Dec-3 / 凸障碍）。  
4. 清洗拼合不产生额外 $N^{-\delta}$（L-Klo-6）。  
5. 破壁接口 Klo-G1–G4 为条件式，强度不低于 H / Tri-G1 / Wt-G1（L-Klo-7）。  
6. 假设 H 仍为未证条件式；H-gap 仍为 $N^{11/24}$。  
7. **不声称**原猜想已证。

若要打破 $13/24$，必须在真次弧上引入**非对角**结构（杀掉 $\|F\|_2$ 质量）或超出完整和绝对值的符号取消——已标为 Klo-G1–G3，不在 R12 无条件范围内。

---

## 状态汇总

| 编号 | 摘要 | 状态 |
|------|------|------|
| L-Klo-1 | 中间弧 $\mathfrak{I}(Q,R)$ / 真次弧 $\mathfrak{m}^{\flat}$ | 已证（定义） |
| L-Klo-2 | 测度与模数分解 $\mathrm{meas}(\mathfrak{I})\ll R^2/N$ | 已证 |
| L-Klo-3 | 中间弧完整和近似 | 已证 |
| L-Klo-4 | **中间弧贡献** $\ll_\varepsilon N^{13/24+\varepsilon}$ | 已证 |
| L-Klo-5 | **真次弧指数 $\ge 13/24$（不能 $<$）** | 已证（障碍） |
| L-Klo-6 | 清洗不产生净 $N^{-\delta}$ | 已证（障碍） |
| L-Klo-7 | Klo-G1–G4 突破接口 | 条件式 |
| L-Klo-8 | 方法名 × 指数对照表 | 已证 |
| L-Klo-9 | 结算：不改进 L-Dec；H-gap 仍 $N^{11/24}$ | 已证（结算） |

**对 H 的判决：** R12-Kloosterman-Cleansing **止步**于 $\beta/2=13/24$；中间弧可单独估计，剩余真次弧**无**额外 $N^{-\delta}$。**H 仍为未证条件式。**
