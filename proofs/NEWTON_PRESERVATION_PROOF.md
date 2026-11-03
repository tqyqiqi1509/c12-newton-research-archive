# 普通 Newton 对数凹性：一般减常数乘子与所有外幂

本文件收录本轮的一般定理及完整证明，并附上唯一继承输入——普通 Newton 乘法保性——的完整初等证明，因此可以独立阅读。两个独立复核文件和根审核另列。有限计算不参与一般证明。该定理只解决已识别的代数组装步骤，不等于 C12；不作书目首创性声明。

## 本轮证明

# Independent reconstruction: a supported shifted multiplier and every exterior selection

2026-10-31, Asia/Shanghai. The general multiplier argument was proposed by the root after the branch's exterior-square theorem. This note independently reconstructs every step, including all minors across zeros, leading-support cancellation, constants, and the induction for arbitrary selection multiplicity. It is an AI mathematical audit and proof reconstruction, not external peer review or formal verification. No novelty claim is made.

## 1. Ordinary Newton notation and the inherited lemma

Let `B_i(m)=binom(m,i)` and write

\[
A(m)=\sum_i a_i B_i(m),\qquad E(m)=\sum_i e_i B_i(m).
\]

All coefficient rows below are finite and extended by zero. `LC/NIZ` means nonnegative, log-concave, and with no internal zeros. The zero row is allowed as an output.

The ordinary Newton product is

\[
C_n(a,e)=\sum_{\max(i,j)\le n\le i+j}
\frac{n!}{(n-i)!(n-j)!(i+j-n)!}\,a_i e_j.
\tag{1}
\]

For a fixed row `a`, define the lower-triangular kernel

\[
M_a(n,i)=\binom ni\sum_{j=0}^i\binom ij a_{n-i+j}
\quad(0\le i\le n),
\qquad M_a(n,i)=0\quad(i>n).
\tag{2}
\]

Then `C_n(a,e)=sum_i M_a(n,i)e_i`, and two special entries are

\[
M_a(n,n)=A(n),\qquad M_e(n,0)=e_n.
\tag{3}
\]

The inherited ordinary Newton product proof gives the following facts:

1. If `a` is LC/NIZ, every two-by-two minor of `M_a` is nonnegative (global TP2, including its zero boundary).
2. If `a,e` are LC/NIZ, then `c_n=C_n(a,e)` is LC/NIZ. Its support is `[max(L_a,L_e),U_a+U_e]`.
3. Put `a_i^+=a_(i+1)` and `e_i^+=e_(i+1)`. On the positive support of `c`, each of

\[
\frac{C_n(a^+,e)}{c_n},\qquad
\frac{C_n(a,e^+)}{c_n},\qquad
\frac{C_n(a^+,e^+)}{c_n}
\tag{4}
\]

is nonnegative and nonincreasing with `n`.

For clarity about zero entries, (4) is an inequality between cross-products of finite polynomial expressions. For strictly positive input rows it follows by the kernel's TP2 property and decreasing input ratios. The doubly shifted quotient is a product of two such quotients. Replace each interval-supported row by positive geometric tails, as in the inherited proof, and pass each cross-product inequality to the limit. This proves (4) without dividing by a zero intermediate product.

These facts and their elementary proof are in namespace `run6`, logical path `agents/newton_union_product/research/ORDINARY_NEWTON_LC_PROOF.md`, SHA-256 `d74cb6d5a7354f2aea6db70f02cc9878ae481a857af2bc0d29405c445d31145e`. They are the sole inherited mathematical lemma used in the new preservation proof.

## 2. General shifted-multiplier theorem

**Theorem.** Suppose `a` and `e` are nonzero finite LC/NIZ rows, and the positive support of `e` is `[L,U]`. Let

\[
0\le\lambda\le A(L).
\tag{5}
\]

Then the ordinary Newton row of

\[
F(m)=(A(m)-\lambda)E(m)
\tag{6}
\]

is nonnegative LC/NIZ, or identically zero.

For `lambda=0` this is the inherited product theorem. If `A` is constant, it is multiplication by the nonnegative scalar `A-lambda`. Otherwise, assume `lambda>0`, and let `V=deg A>=1`. The support is `[L,U+V]` if `A(L)>lambda`, and `[L+1,U+V]` if `A(L)=lambda`.

### 2.1 Nonnegativity and the support

Put `c_n=C_n(a,e)`, so the output coefficients are

\[
f_n=c_n-\lambda e_n.
\tag{7}
\]

Because `A(L)>0`, the input support of `a` begins at or before `L`. Thus `c` is positive precisely on `[L,U+V]`. For `L<=n<=U`, the contribution of the column `i=n` in (2) is `A(n)e_n`; all other contributions are nonnegative. Since the binomial coefficients `a_i` are nonnegative, `A(n)` is nondecreasing for integer `n>=0`. Therefore

\[
c_n\ge A(n)e_n\ge\lambda e_n.
\tag{8}
\]

Above `U`, `e_n=0` and `f_n=c_n`. At `n=L`, only the input `e_L` can contribute, hence

\[
f_L=(A(L)-\lambda)e_L.
\tag{9}
\]

In the nonconstant case under consideration, `A(n+1)>A(n)` for every `n>=L`. Indeed, if the positive support of `a` starts at `s>=1`, then `s<=L` and `a_s binom(n,s-1)>0` occurs in `Delta A(n)`. If it starts at zero, LC/NIZ and nonconstancy give `a_1>0`. Thus all later `f_n` within the stated support are positive. This proves the support claim before any ratio is used.

### 2.2 Subtracting the diagonal preserves TP2 on the needed rows

Restrict row indices to `n>=L` and define

\[
N(n,i)=M_a(n,i)-\lambda\,\mathbf1_{n=i}.
\tag{10}
\]

Every entry is nonnegative: the only changed entries are `A(n)-lambda>=0`. The whole matrix `N` is TP2. Here is a direct proof for arbitrary rows `n<m` and columns `i<j`; it does not infer global TP2 merely from adjacent minors across zeros.

* If no entry of the minor is a changed diagonal entry, its determinant equals the nonnegative `M_a` minor.
* If `j=n`, only the upper-right entry is reduced, and the determinant increases by `lambda M_a(m,i)`.
* If `i=n` or `j=m`, the upper-right entry is zero by lower triangularity. The determinant is a product of two nonnegative entries of `N`.
* If `i=m`, the upper row is entirely zero, so the determinant is zero.

These exhaust all possible changed diagonal positions, including simultaneous upper-left and lower-right changes. Hence `N` is globally TP2 on rows `n>=L`.

### 2.3 The shifted-input quotient for `N`

LC/NIZ of `e` implies, for every `i<j`,

\[
e_{i+1}e_j-e_{j+1}e_i\ge0.
\tag{11}
\]

This includes `i=L-1`, where `e_i=0`, and all other zero cases. Write

\[
P_n=\sum_i N(n,i)e_{i+1},\qquad
f_n=\sum_i N(n,i)e_i.
\]

For consecutive rows, pairing terms indexed by `(i,j)` and `(j,i)` yields

\[
P_n f_{n+1}-P_{n+1}f_n
=\sum_{i<j}(e_{i+1}e_j-e_{j+1}e_i)
\bigl(N(n,i)N(n+1,j)-N(n,j)N(n+1,i)\bigr)\ge0.
\tag{12}
\]

Thus `P_n/f_n` is nonnegative and nonincreasing throughout the positive output support. No undefined ratio at the canceled first entry is used.

### 2.4 The diagonal-to-product quotient

Set `u_n=e_n/c_n` on the positive support of `c`. Formula (3) and TP2 for `M_e` give

\[
\begin{aligned}
e_n c_{n+1}-e_{n+1}c_n
&=\sum_j a_j\bigl(M_e(n,0)M_e(n+1,j)
-M_e(n,j)M_e(n+1,0)\bigr)\\
&\ge0.
\end{aligned}
\tag{13}
\]

The term with `j=0` is zero. Equation (13) is valid even when an `e_n` vanishes. Consequently `u_n` is nonincreasing. On the positive support of `f`,

\[
\frac{c_n}{f_n}=\frac1{1-\lambda u_n}
\tag{14}
\]

is positive and nonincreasing, because `lambda>=0` and the denominators are positive there.

### 2.5 The output ratio is a sum of three decreasing ratios

The same last-label membership decomposition as for the Newton product gives

\[
c_{n+1}=C_n(a^+,e)+C_n(a,e^+)+C_n(a^+,e^+).
\]

Subtracting `lambda e_(n+1)` and using (10) gives the exact identity

\[
f_{n+1}=P_n+C_n(a^+,e)+C_n(a^+,e^+).
\tag{15}
\]

Therefore

\[
\frac{f_{n+1}}{f_n}
=\frac{P_n}{f_n}
+\frac{C_n(a^+,e)}{c_n}\frac{c_n}{f_n}
+\frac{C_n(a^+,e^+)}{c_n}\frac{c_n}{f_n}.
\tag{16}
\]

The first term decreases by (12). Each remaining term is the product of two nonnegative nonincreasing sequences, by (4) and (14), and therefore decreases. The sum in (16) is nonincreasing. This is exactly LC on the positive interval of `f`. Outside that interval the adjacent inequalities follow from zero extension. The theorem is proved.

## 3. Every exterior selection preserves ordinary Newton LC

**Corollary.** Let

\[
D(m)=\sum_i d_i\binom mi
\]

have a finite nonnegative **integer** LC/NIZ Newton row. Then for every integer `k>=0`,

\[
P_k(m)=\binom{D(m)}k
\tag{17}
\]

has a nonnegative LC/NIZ ordinary Newton row, or is zero.

The polynomial binomial in (17) is the falling polynomial `D(D-1)...(D-k+1)/k!`. It is not a coefficient in ordinary powers of `m`, nor a factorial-normalized Newton symbol.

**Proof.** If `D` is the constant nonnegative integer `c`, then `P_k=binom(c,k)` is constant or zero. Suppose `D` is nonconstant. It takes nonnegative integer values at every nonnegative integer, is nondecreasing there, and tends to infinity. Start with `P_0=1`, `P_1=D`.

Assume the row of `E=P_(k-1)` is nonnegative LC/NIZ, and let its first positive index be `L`. For any polynomial with a nonnegative Newton row, the first positive index equals its first positive value on nonnegative integers: all `binom(n,r)` vanish for `n<r`, while `binom(L,L)=1`. Applying this to `P_(k-1)`, and using the integer-valuedness of `D`, gives

\[
L=\min\{n\ge0:D(n)\ge k-1\}.
\tag{18}
\]

In particular `D(L)>=k-1`. The multiplier theorem with `A=D` and `lambda=k-1` applies to

\[
kP_k=(D-(k-1))P_{k-1}.
\tag{19}
\]

Division by the positive scalar `k` does not change LC or support. This completes the induction for all `k`. There is no assumption that the first positive coefficient `d_L` be at least `k-1`; the threshold (18) is a value of the whole polynomial, not a single input coefficient.

For nonconstant `D` of degree `V`, the positive support for `k>=1` is exactly

\[
\left[\min\{n\ge0:D(n)\ge k\},\ kV\right].
\tag{20}
\]

The lower endpoint follows from nonnegative coefficients and evaluation as above. The upper endpoint is the degree `kV` with positive leading coefficient. The theorem supplies the absence of interior zeros.

The output Newton coefficients are integers as well, since for every r they equal the finite difference

\[
[B_r]\binom{D(m)}k=\sum_{j=0}^{r}(-1)^{r-j}\binom rj\binom{D(j)}k\in\mathbb Z.
\]

Integer coefficients are a sufficient condition guaranteeing the needed integer values and the threshold interpretation. They must not be silently dropped: for `D(m)=3m/2`, the `B_1` coefficient of `binom(D,3)` is `binom(3/2,3)=-1/16<0`.

## 4. Normalization of the actual original wall

The precise inherited source is namespace `inherited/latest_input`, logical path `history/archive/research/closing_g4_challenge/audit.md`, especially §§2.1–2.2 and 5.1. It fixes a primitive positive ray `n_0=(d,e)` and proves, in the original ERS cluster convention,

\[
T_m(t)=1+\sum_{k\ge1}\tau^{m,m}(kd,ke)t^k
=\prod_{j\ge1}(1+t^j)^{q_j(m)},
\qquad q_j(m)=\frac{j\,u_{j n_0}(m,m)}m.
\tag{21}
\]

Here `u` is the dilogarithm exponent in the fixed negative-determinant convention. The entire `q_j` has nonnegative **integer** Newton coefficients and positive interval support. The integer claim is for the complete `q_j`; individual rational summands `m^(-1) binom(m,p)binom(m,q)` cannot serve as atom counts. This is not the palette wall `G=T^m`, its logarithm, or one open-stable Euler term.

The earlier parity presentation in namespace `run4`, `agents/full_wall_assembly/report.md`, is

\[
T_m(t)=\prod_{j\text{ odd}}(1+t^j)^{D_j(m)}
\prod_{j\text{ even}}(1-t^j)^{-D_j(m)},\qquad D_j=jF_j.
\tag{22}
\]

These are consistent, not different target walls. Since

\[
(1-x)^{-D}=\prod_{\ell\ge0}(1+x^{2^\ell})^D
\]

coefficientwise as formal series, their relation is exactly

\[
q_n=D_n+\sum_{\substack{\ell\ge1\\2^{\ell+1}\mid n}}D_{n/2^\ell}.
\tag{23}
\]

The sum is finite for each `n`. Thus the `q_n` used in (21) already include the necessary binary towers. They must not be replaced silently by `D_n`. Nor does LC of every `D_n` automatically imply LC of the sum (23).

There is a genuine obstruction to applying a claimed rising-binomial version directly to the even factors of (22). The inherited exact record `run4/agents/actual_fullwall_invariant/newton_lc_binomial_probe.json` gives

\[
D(m)=B_1(m)+2B_2(m)+3B_3(m),
\]

whose ordinary Newton row is LC/NIZ, but the row of `binom(D(m)+3,4)` starts

\[
(0,1,33,1263,26211,\ldots).
\]

Its rank-two defect is `33^2-1*1263=-174`. This is an inherited artificial multiset counterexample, not a C12 counterexample. The present theorem proves distinct selections `binom(D,k)`, not multisets `binom(D+k-1,k)`. Its hypothesis `lambda>=0` and the positive Euler conversion (21) are essential. The same old file records 2,907 earlier exterior tests without failure; those tests are historical finite evidence, not a previously available proof and not new computation coverage here.

## 5. The new conditional all-gcd consequence and its exact limit

Suppose the ordinary Newton row of each actual `q_j` needed through total charge `k` is LC. Its nonnegative integer status and NIZ are inherited G4 inputs. For every charge partition `ell=(ell_1,...,ell_k)` satisfying `sum j ell_j=k`, the exact contribution is

\[
H_\ell(m)=\prod_{j=1}^k\binom{q_j(m)}{\ell_j}.
\tag{24}
\]

The new corollary proves LC/NIZ of **every factor for every multiplicity** `ell_j`. The ordinary Newton product theorem then proves LC/NIZ of each complete `H_ell`. Consequently repeated selection and the same-charge diagonal exclusions no longer require separate conjectures, conditional on actual atom LC.

The remaining original coefficient is still the full sum

\[
\tau^{m,m}(kd,ke)=\sum_{\sum j\ell_j=k}H_\ell(m).
\tag{25}
\]

This proof does not show LC of the actual `q_j`, and does not show LC of the sum (25). Actual per-partition synchronization already fails, as the inherited central direct-atom versus all-singleton control shows. The artificial example in `FINITE_DIFFERENCE_EULER_GATE.md` likewise remains valid even though each of its individual factors now falls under the general preservation theorem. No completed C12 proof is claimed.

## 6. Audit outcome

The root-origin general multiplier argument passes this independent reconstruction. The points requiring care have all been resolved explicitly: arbitrary TP2 minors after subtracting the diagonal; the `L-1` support of `e^+`; the direction of `c/f`; constant and zero cases; first-rank cancellation; the value threshold rather than a coefficient bound in the all-`k` induction; and the true positive Euler normalization including binary covers.

The earlier exterior-square file is retained byte-for-byte as a valid earlier lemma. This note extends its scope without withdrawing the earlier factorial-normalized PF counterexamples. General validity rests on the displayed proof and its stated inherited lemma, not on the large bounded gate. No external 2026 theorem or unverified plugin result is used.


---

## 附录：所依赖的普通 Newton 乘法完整证明

# Ordinary Newton multiplication preserves log-concavity

**Status:** self-contained proof, first complete draft 2026-10-30 12:01 UTC; algebra and boundary audit completed. No external theorem is used in the proof. The exact audit receipt is `../computations/proof_identity_audit.json`.

## Theorem

Let `a=(a_i)_{i>=0}` and `b=(b_j)_{j>=0}` be nonnegative, finitely supported, log-concave sequences, each having no internal zeros. Extend them by zero outside their supports. Define

\[
 C_n(a,b)=\sum_{\substack{i,j\ge0\\\max(i,j)\le n\le i+j}}
 \frac{n!}{(n-i)!(n-j)!(i+j-n)!}\,a_i b_j.
\]

Then `c_n=C_n(a,b)` is nonnegative, log-concave, and has no internal zeros. This is the **ordinary** Newton product, with no factorial normalization of `c_n`.

If `a` and `b` are nonzero with positive supports `[L_a,U_a]` and `[L_b,U_b]`, then the positive support of `c` is exactly

\[
 [\max(L_a,L_b),\,U_a+U_b].
\]

## 1. Neighbor sums preserve log-concavity

For the moment all entries are strictly positive; infinite sequences are allowed because every `C_n` is a finite sum. If `u` is log-concave, so is `v_k=u_k+u_{k+1}`. For `k>=1`,

\[
\begin{aligned}
v_k^2-v_{k-1}v_{k+1}
={}&(u_k^2-u_{k-1}u_{k+1})
+(u_{k+1}^2-u_ku_{k+2})\\
&+(u_ku_{k+1}-u_{k-1}u_{k+2})\ge0.
\end{aligned}
\]

The last summand is nonnegative because the positive ratios `u_{r+1}/u_r` decrease with `r`. Consequently every sequence

\[
B_i(k):=\sum_{j=0}^{i}\binom{i}{j}b_{k+j},\qquad k\ge0,
\]

is log-concave: `B_0=b` and `B_{i+1}(k)=B_i(k)+B_i(k+1)`.

## 2. A two-by-two positive kernel

For fixed positive log-concave `b`, define the lower-triangular matrix

\[
M_b(n,i)=\begin{cases}
\displaystyle\binom ni B_i(n-i),&0\le i\le n,\\
0,&i>n.
\end{cases}
\]

Choosing the `i` elements of the first set, and then choosing the overlap with the second set, gives

\[
C_n(a,b)=\sum_{i\ge0}a_iM_b(n,i).
\]

For `0<=i<n`, put `k=n-i>=1` and abbreviate `B=B_i`. The adjacent minor is

\[
\begin{aligned}
&M_b(n,i)M_b(n+1,i+1)-M_b(n,i+1)M_b(n+1,i)\\
&\quad=\frac{\binom n{i+1}\binom{n+1}i}{k}
\bigl[(k+1)B(k)^2+B(k)B(k+1)-kB(k-1)B(k+1)\bigr]\ge0.
\end{aligned}
\]

Indeed `B(k)^2>=B(k-1)B(k+1)`, and the bracket is at least `B(k)^2+B(k)B(k+1)>0`. The factor follows from

\[
\frac{\binom ni\binom{n+1}{i+1}}
{\binom n{i+1}\binom{n+1}i}=\frac{k+1}{k}.
\]

For `i=n`, the adjacent minor is nonnegative because `M_b(n,n+1)=0`. Thus, for every fixed `n`, the ratios

\[
\frac{M_b(n+1,i)}{M_b(n,i)},\qquad 0\le i\le n,
\]

increase with `i`; the extra entry at `i=n+1` has zero weight in row `n`. It follows for every `i<j` that

\[
M_b(n,i)M_b(n+1,j)-M_b(n,j)M_b(n+1,i)\ge0.
\tag{TP2}
\]

Only adjacent **rows** of this TP2 kernel will be used below. For completeness, it is globally TP2 as well. For arbitrary rows `n<m` and columns `i<j`:

- If `i>n` or `j>m`, the determinant is zero.
- If `i<=n<j<=m`, the upper-right entry is zero and the determinant is nonnegative.
- If `j<=n`, all four entries are positive, and

\[
\frac{M_b(m,k)}{M_b(n,k)}
=\prod_{r=n}^{m-1}\frac{M_b(r+1,k)}{M_b(r,k)},\qquad k\in\{i,j\},
\]

is nondecreasing in `k` by the adjacent-row result. This proves the required global minor. For interval-supported nonnegative `b`, the same global TP2 property follows by the positive approximation in Section 5 and continuity of every minor; no unsupported inference from adjacent minors across zeros is needed.

## 3. A shifted-input quotient decreases

Write `a^+_i=a_{i+1}`. If `a` and `b` are positive and log-concave, then

\[
R_n(a,b):=\frac{C_n(a^+,b)}{C_n(a,b)}
\]

is nonincreasing in `n`. To see this, put `r_i=a_{i+1}/a_i`, so that `r_i` is nonincreasing. Expanding the numerator of `R_n-R_{n+1}` and pairing the terms indexed by `(i,j)` and `(j,i)` gives

\[
\begin{aligned}
&C_n(a^+,b)C_{n+1}(a,b)-C_{n+1}(a^+,b)C_n(a,b)\\
&\quad=\sum_{0\le i<j\le n+1}a_i a_j(r_i-r_j)
\bigl[M_b(n,i)M_b(n+1,j)-M_b(n,j)M_b(n+1,i)\bigr]\ge0.
\end{aligned}
\]

The two signs are supplied respectively by log-concavity of `a` and by (TP2). By symmetry,

\[
S_n(a,b):=\frac{C_n(a,b^+)}{C_n(a,b)}
\]

is also nonincreasing. Since `b^+` remains log-concave, the doubly shifted quotient is a product of nonnegative, nonincreasing sequences:

\[
T_n(a,b):=\frac{C_n(a^+,b^+)}{C_n(a,b)}
=R_n(a,b^+)S_n(a,b).
\]

Hence `T_n` is nonincreasing as well. This factorization avoids any assumption that the full two-dimensional endpoint law is stochastically increasing.

## 4. The Newton product quotient is the sum of these three quotients

For a pair `(S,T)` covering `[n+1]`, the final element belongs only to `S`, only to `T`, or to both. Removing it gives the exact identity

\[
C_{n+1}(a,b)=C_n(a^+,b)+C_n(a,b^+)+C_n(a^+,b^+).
\tag{1}
\]

Therefore

\[
\frac{C_{n+1}(a,b)}{C_n(a,b)}=R_n(a,b)+S_n(a,b)+T_n(a,b).
\]

The right-hand side is nonincreasing in `n`. Thus, for `n>=1`,

\[
C_n(a,b)^2\ge C_{n-1}(a,b)C_{n+1}(a,b).
\]

This proves the assertion for strictly positive sequences.

## 5. Zero entries and finite supports

Suppose a nonzero finite sequence `a` has positive support `[L,U]`. For sufficiently small `epsilon>0`, set

\[
a^{(\epsilon)}_k=\begin{cases}
a_L\epsilon^{L-k},&0\le k<L,\\
a_k,&L\le k\le U,\\
a_U\epsilon^{k-U},&k>U.
\end{cases}
\]

Its successive ratios are `epsilon^{-1}` on the initial tail, the original nonincreasing ratios within the support, and `epsilon` on the terminal tail. Taking `epsilon` smaller than every relevant positive internal ratio and the reciprocal of every such ratio makes the entire sequence positive and log-concave. A singleton support requires only `epsilon<=1`. Moreover `a^{(epsilon)}_k -> a_k` for each fixed `k`. Apply the same construction to `b`.

The established inequality for these positive approximants passes to the limit because each `C_r` is a finite polynomial in the input entries. If either input is identically zero, the conclusion is immediate.

Finally the coefficient `c_n` is zero outside `[max(L_a,L_b),U_a+U_b]`. For any integer `n` inside that interval choose

\[
i=\min(U_a,n),\qquad j=\min(U_b,n).
\]

Then `i` and `j` lie in their positive supports, `max(i,j)<=n`, and `i+j>=n`. Thus their summand is positive, proving that the output has no internal zeros.

## Scope for C12

This theorem proves the closure arrow

\[
\text{ordinary Newton-LC inputs}\quad\Longrightarrow\quad
\text{ordinary Newton-LC product}.
\]

It can replace a stronger W-LC premise at an actual product node when that node's factors are already known to have ordinary Newton-LC coefficients. It supplies **no closure under arbitrary positive sums**, no control of a cut sum without a separate invariant, and no control of nonprimitive or all-gcd extraction. It is an abstract structural lemma, not additional original-wall computation.

## Source and novelty status

The proof above is an independent elementary derivation. No result from a 2026 source, no inaccessible Walkup text, and no factorial-normalized substitute enters it. The searches conducted here did not identify this exact statement in an accessible primary source. This is not a claim of bibliographic novelty.
