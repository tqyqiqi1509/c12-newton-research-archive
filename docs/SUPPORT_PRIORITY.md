# 精确Newton支撑：查新、证明定位与价值评估

日期：2026-11-03。对象是ERS原始完整墙τ_m(A,B)的普通Newton系数，a_j=Δ^jτ(0)，所有gcd；不是三角基、Newton多面体或固定m的墙方向支撑。本分支未使用新的2026结论作为证明前提。

## 结论

**建议保留，而且它适合成为Newton主定理之后的独立结构定理／主要应用。** 它给出完整原墙、所有gcd的精确支撑，数学陈述简洁，直接确定C12真正尚待比较的全部指标。相较只保留参数域渐近结果，它更统一。

但是需要分层归属：固定m非消失已有前人成果；首个Newton指标是这些成果与C11正性的简短推论；**无内部零需要额外论证**，不由“正展开”或固定m非消失自动给出。应把潜在新增贡献定位在后者及完整的支撑合成，而不是笼统声称首次非消失。

本轮查到的原始来源没有直接写出这一精确Newton区间等价式；有限检索不能证明全球首创，优先权状态为未最终认证。

## 准确陈述与直接作用

固定A,B>0，D=A+B−1，写τ_m(A,B)=Σ_(j=0)^D a_j binom(m,j)。候选定理为

    a_j>0 ⇔ s≤j≤D，s=ceil((A²+B²−1)/(AB))。

它同时给：a_0=…=a_(s−1)=0；a_s>0；其后直到最高次无零。若进一步证明正支撑内部LC，单峰性随即成立。它没有给a_j²≥a_(j−1)a_(j+1)的数值比较。

例如A=B时s=2（A=B=1则s=1）；这清楚区分仿射m=2完整墙的高倍数非消失与稳定DT高倍数消失。若采用过度简化的“稳定对象非零等于原墙非零”，会漏掉这个边界。

## 原始文献核对

### 1. Akagi固定版本：已有C11，不是全Newton支撑

Ryota Akagi，*Some coefficients of rank 2 cluster scattering diagrams*，arXiv:2507.21916v3。官方摘要页确认v3为2025-12-02，当前所列最新版本；v2修订主定理并改进Prop4.3，v3小修。

- Prop1.3汇总C1、2、3、5、6、11、15及其他部分结果。
- Remark1.4明确Prop4.3的完整C11证明由Burcroff–Lee–Mou提出。
- §4.2 Prop4.3断言次数D及普通二项式基正展开。
- 证明式(45)用完整Euler指数q_j的外选择乘积，再利用binomial-positive多项式乘法及复合的保正性；式(47)–(49)写q_j的profile表达。

本分支已读§4.2的完整显示证明。它不声明系数没有内部零，更不直接给首阶s。故不能以Prop4.3中的“positively”直接替代我们的NIZ步骤，也不能把C11归为本项目新定理。

主源：[Akagi v3全文](https://arxiv.org/html/2507.21916v3#S4.SS2)、[官方版本页](https://arxiv.org/abs/2507.21916)。

### 2. BLM Appendix B：固定初始函数、固定m的非消失

Amanda Burcroff–Kyungyong Lee–Lang Mou，*Positivity of generalized cluster scattering diagrams*，arXiv:2503.03719v1（2025-03-05；官方页只列v1，尝试v2为404，不能据此制造新版）。

Appendix B Theorem B.1给非负初始系数、Badlands中的本原方向(a,b)、满足初始次数整除的k之墙系数的显式正下界；Corollary B.2给全部有理Badlands方向出现。其证明通过tight grading构造并含affine边界。本文Appendix B还明确追溯skew-symmetric情况的Gross–Pandharipande2010密度与Davison–Mandel2021各墙系数严格正，以及Gräfnitz–Luo的更一般结果。

本分支已读Theorem B.1、证明及CorB.2。它是在固定初始多项式上比较壁函数单项式系数，不是在箭头参数m上取有限差分；不是普通Newton系数NIZ定理。

主源：[BLM v1 Appendix B](https://arxiv.org/html/2503.03719v1#A2)。章节链接在不同渲染中可能变化，精确定位为Theorem B.1与CorB.2。

### 3. ERS原文及BLMMR期刊

ERS arXiv2404.11381v4 §3的C11正二项式展开、C12凹性原目标已核。BLMMR 2026期刊页（DOI10.1112/jlms.70642）Remark1.5也指出Akagi Prop4.3证明C11，并说明其自身方法不处理C11。该2026页本轮只用作书目交叉核对，没有在未强审前将其新增定理导入支撑证明。

## 首阶与无内部零：两项不同内容

局部proof.md的固定m非消失判据为

    τ_m(A,B)>0 ⇔ A²+B²−mAB≤1。

已知a_j≥0时，整数m下τ_m=Σ_(j≤m) a_j binom(m,j)，每个binom(m,j)>0。因此τ_0=…=τ_(s−1)=0且τ_s>0等价于首正Newton指标为s。**这部分是短归约，已有非消失结果应给足归属。**

但固定m取值在s以后一直正，只保证a_s>0，不能阻止更高a_j中间零。无内部零的本地完整证明另用：

1. 全支持稳定表示拆分顶点保持稳定；偶Euler tower用足够多不同stable simples的泛型细分，得到profile-alpha正支撑在palette坐标中向上闭。
2. 单profile m^(−1)binom(m,p)binom(m,q)的Newton支撑恰为[max(p,q),p+q−1]。向上闭路径使这些正区间连接到顶角，完整整数Euler指数q_n的Newton支撑为区间。
3. 对非负整数、区间正支撑的f，binom(f,ell)的Newton支撑为[min{m:f(m)≥ell},ell deg f]：用“替换共享颜色”或“增加对象大小”逐色增加覆盖。
4. 完整Euler系数是各外选择乘积之和；每个分拆项的支撑均与直接q_(kn0)区间相交，故总行支撑连通。不能将rho/m当tau，也不能将有理单profile当整数原子。

这些是本地support_bps/proof.md §§1–7的完整链，本分支重新读完，未发现新的局部阻断；alpha–DT身份、MR/FR、整数性与C11仍需随正式稿逐源核准。此前追加审核已有规范及affine边界检查，本轮查新未推翻该结论。

## 与Newton主定理的关系和选稿

Newton乘法与整数选择复合说明：一旦实际原子已经LC，各Euler分拆乘积可以合法装配。但实际原子LC与不同分拆正和补偿仍未证。

支撑定理更弱，却已在真实原墙上完成。它不需要假设原子LC；其“逐色增加”独立证明了NIZ。因此主文可以按以下逻辑组织：一般Newton保性 → 有限整数选择与支撑 → 原墙精确支撑及条件LC应用。若纳入真实原墙支撑，必须真正给出所需几何/组合身份，而非只附一个没有证明出处的定理。

建议将精确支撑作为有证明的应用定理，而不是与尚无自足短证明的渐近结论混放成“无证明成果列表”。若正文因此过长，可把alpha–DT与支撑证明置技术附录并准确引用源；其地位仍比仅列表的渐近结果高。

## 对抗性检查和不应声称之事

- “正展开”不等于全部下标严格正。
- 固定m非消失不等于Newton NIZ。
- affine时稳定高倍数消失不能推出完整墙高倍数消失。
- 全gcd原墙不能替换成primitive、connected、BPS指数。
- 三角基support conjecture（LLRZ/量子系数e(p,q)）与本问题不同。此次搜索命中Qiyue Tang的该类稿件，属用户相邻项目，不能当作本精确Newton支撑的独立竞争结论。
- Hexagon的用户本人Badlands增长率、代数性、C4分母稿件也不是本定理；未重新强审，不作外部支撑输入。

## 查询覆盖

本轮做了普通web检索、官方arXiv版本与正文核对；另对Zenodo、aiXiv、Hexagon、MathDB作站点限定查询。未命中与全文阅读有明确区别，未遍历站内全库。原查询和结果范围在SUPPORT_SEARCH_LOG.json。没有做全球穷尽或首创认证。
