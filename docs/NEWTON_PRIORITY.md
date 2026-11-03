# Newton主定理：查新与对抗性比较

日期：2026-11-03。范围为A：普通Newton乘法保LC；B：支撑阈值减常数乘子；C：所有整数选择复合。本报告不作全球首创认证。检索原式及实际读取范围见NEWTON_PRIORITY_SEARCH.json。

## 1. 最重要的新定位：覆盖卷积是已知Heisenberg卷积

已取得Aguiar、Ferrer Santos、Moreira作者主页全文：

https://pi.math.cornell.edu/~maguiar/heisenberg.pdf

作者副本44页；本次具体读§1的species定义、§1.2 Proposition1.3及其证明，以及后续对称群表示的定义与对称函数定位。§1定义

    (p # q)[I] = ⊕_(I=S∪T) p[S] ⊗ q[T]。

Proposition1.3明确给出维数卷积

    c_n = Σ_(max(i,j)≤n≤i+j) n! a_i b_j /[(n−i)!(n−j)!(i+j−n)!]。

这与本项目普通Newton乘法核逐字母等价：只把a_i、b_j解释成输入species在i、j元素集合上的维数。因而**覆盖运算、结合性、三类末标签分解的组合背景均不是本项目发明的新乘法**。应引用已知Heisenberg product，并将主张精确表述为它的维数序列LC保持及支撑阈值扩展。公开作者PDF另存并有实际下载回执。

这一步不自动认定A已知：该原文这里给出卷积和表示构造，没有在所读段落给出“仅LC/NIZ维数输入→LC/NIZ维数输出”的定理。a_i允许非负实数的推广也只是代数推广，不能单靠它成为足够新颖性。

## 2. Walkup1976：真正尚未排除的优先权风险

官方元数据：D. W. Walkup，*Pólya sequences, binomial convolution and the union of random sets*，Journal of Applied Probability 13(1), 1976, 76–85，DOI10.2307/3212667。

本次先用内置web广搜，再实际读取Cambridge官方页面；发现citation_pdf_url并请求官方PDF，得到HTTP200但被重定向回摘要HTML，PDF magic=false。因此**没有取得Walkup全文**。请求、终止URL、类型、字节数、SHA和UTC时间记录在newton_priority_sources/Walkup_retrieval.json。

出版社摘要明确谈PF序列、指数生成函数的binomial convolution、随机集合并覆盖概率，但仅凭摘要不能判断它是否已经证明本项目A，或其性质是另一个阶乘规范。因此下列两种说法均不能写：

- “Walkup完全没有此结果，故本定理首创”；
- “Walkup已经证明本定理，所以A没有价值”。

正确结论：**A存在必须解决的经典优先权缺口；B、C也尚未获得穷尽优先权认证。** 获取Walkup正文是正式投稿前的第一项书目工作；不需要为此重开C12长跑。

## 3. Wagner／Brändén：实根输入的已知定理，不覆盖一般LC输入

本次读Brändén固定arXiv:1410.6601v1，§7.1 Theorem7.6及上下文。其归因Wagner1992的准确陈述为：若E(F)、E(G)的全部根都位于[-1,0]，则E(FG)也如此。E按binomial基到幂基的转换定义。

这确实包含本项目A的一个重要实根子类，但本项目只假设普通Newton行LC/NIZ，未假设E(F)实根。例如

    F(m)=1+m+binom(m,2)，E(F)=1+x+x²，

行(1,1,1)LC/NIZ而生成多项式非实根。因此该已知保根定理不能直接证明本项目全部A。它也不是带支撑阈值的减常数B或全部整数选择C。

对Wagner原始1992完整证明本次没有重新读到；本次核实的是Brändén明确引用的定理陈述与范围，不能标作原文全证审核。

## 4. 本轮命中的2026近邻：Liu–Mao的W规范

新命中：Yanxin Liu、Jianxi Mao，*Preservation of log-concavity under Hadamard products*，arXiv:2609.11589v1，2026-09-10。

原文：https://arxiv.org/html/2609.11589v1

本次读定义、Theorem1.2、Lemma2.1的核、Bernstein矩阵证明链的主要接口与§4；没有重证全篇及所有边界，故此2026文献**不进入我们主定理的数学依赖**。它在查新中必须列为直接近邻并仔细区分对象。

其W(p)定义为

    Σ_(n≥0) p(n)x^n = W(p)(x)/(1−x)^(deg p+1)。

Theorem1.2的假设与结论是W(p)、W(q)、W(pq)幂系数的LC/NIZ，等价于固定degree的移位二项式基binom(m+d−i,d)，不是变degree的普通Newton基binom(m,i)。对任意d次F，

    W(F)(x)=(1−x)^d E(F)(x/(1−x))。

前述F给E(F)=1+x+x²而W(F)=1−x+x²，已不满足其非负假设。因此不能把Liu–Mao直接当成本项目A已被覆盖。反之也不能声称A立即解决其W问题：基变换没有一般保持所需正性。

Brändén–Ferroni–Jochemko arXiv:2408.12386v2（2025-11-14）Theorem1.2同样是W规范的ULC保持，不是本项目普通Newton行的LC。该文精确指出ULC与LC及NIZ边界，所读定义、引言及主定理已与本项目分开。不同规范之间的推论必须证明，不能凭同样叫“Hadamard/diamond/binomial”而认定相同。

## 5. B、C的优先权与数学内容

本次围绕Newton/binomial basis、shifted multiplier、binomial composition、falling factorial及Heisenberg LC关键词定向检索，未取得一个可验证、精确覆盖B或C的先行定理。只能写“本次已读来源未找到”，不写全球未有。

B的输入：F、G非负LC/NIZ普通Newton行，G首正阶L，0≤λ≤F(L)；结论(F−λ)G同类或零。最有识别度的是整个值F(L)的阈值和相消边界，而不是泛泛的乘法闭包。

C的输入：D非负整数LC/NIZ普通Newton行；对每个k≥0，binom(D(m),k)仍同类且整数。它由B归纳，具有比单个k或外平方更一般的结构性。应把B、C作为论文最具辨识度的核心，A作为基础；即使以后发现A已有，仍需独立审查B、C的先行覆盖。

本次对既有证明没有发现新的阻断：注意λ=0且F(L)=0时必须回归一般乘积支撑公式；常数F、D、零输出单列；B的非负λ和C的整数性不能删。本报告没有新增数值扫描，也没有把旧有限检验当一般证明。

## 6. 补充的二变量Schur锥：值得候选，但经典比较尚未完成

读本轮补漏提取的SCHUR_NEWTON_POSITIVITY_PROOF.md及Heisenberg作者副本相关定义。我们的diamond_2按x、y两坐标分别施加数值覆盖卷积，并询问它是否保持有限二变量GL2-Schur锥。Heisenberg原文中的Schur正性来自对称群表示的Frobenius特征，Schur基在无限对称函数字母中，属于不同范畴。

两者不能仅凭同一名称认定等价。要用经典Heisenberg Schur正性覆盖我们的定理，必须构造兼容diamond_2、次数切片与GL2 Schur正性的具体函子或同态。本次没有得到这种识别；也没有搜到明确表述完全相同的两变量定理。故建议列为**密切相关候选，书目归属待查**，而不是新颖性已经确定的额外主定理。

主代理另外已在Hu–Wang–Zhao–Zhao固定原文 https://arxiv.org/html/1507.08430v2 核对Definition3.2：本项目使用的partial synchronization关系本身是既有定义，不能宣称新引入；其Theorem3.7的保持运算是普通Cauchy卷积，尚不能无转换地覆盖Newton/Heisenberg卷积保持。此条源核由主代理完成，本分工仅记录其交叉核查结论，没有冒称本分工另读全篇。

## 7. 跨平台覆盖边界

实际执行了Zenodo、Hexagon、aiXiv、MathDB、OpenAI math、Jihao Liu域名限定查询，详见JSON的28个原样检索式。结果没有提供足以确认A–C先行覆盖的正文。Hexagon返回的通用目录含其他簇代数或Newton主题，未当成本项目命中。此处仅为搜索引擎站点限定，没有穷尽站内历史、所有版本或未索引材料；相关平台的全范围主审核由主代理另行汇总。

## 建议写入总输出的结论

1. 选Newton主线合理，但准确新颖性仍需解决Walkup全文与B/C先行覆盖。
2. 覆盖核明确引用经典Heisenberg product；不宣称创造新的Newton乘法。
3. 论文核心突出阈值减常数与所有整数选择，保留A的完整初等证明以便自足。
4. Wagner、W规范的2025/2026结果都列入比较，并给出规范差异；未强复核的2026主定理不作前提。
5. 二变量Schur保性可以候选，不能把不同范畴的经典Schur正性一笔带过。
