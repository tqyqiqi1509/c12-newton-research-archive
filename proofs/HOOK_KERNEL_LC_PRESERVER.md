# A fixed-degree hook-to-ordinary-Newton LC preserver

Status: **general proof candidate, exact symbolic certificate verified by Python
and the actual Wolfram kernel; independent mathematical audit requested.**
This does not prove that the actual all-gcd raw-wall hook row satisfies the
hypotheses. No new original wall row, actual hook grid, or novelty claim occurs.

## 1. Statement and exact relevance to C12

For an integer n>=1, set

\[
H_{n,k}(m)=m^{n-k}(m)_k,\qquad 1\le k\le n.
\]

Let d_1,...,d_n be a nonnegative log-concave sequence with no internal zeros,
allowing zero prefixes and suffixes. Write

\[
F_n(m)=\sum_{k=1}^n d_kH_{n,k}(m)
       =\sum_{r=0}^n A_{n,r}\binom mr.
\]

**Theorem HK-PLC.** The ordinary Newton row (A_(n,r)) is nonnegative,
log-concave, and has no internal zeros. More precisely,

\[
A_{n,r}=r!\sum_{k\le r}d_k\left\{{n\atop r}\right\}_k,
\tag{1}
\]

where the subscript k requires the first k labels to occupy distinct blocks.
If the first nonzero d_k is at k=s, the output support is [s,n].

Thus an actual raw wall tau(m)=c_0 sum_k d_k H_(D,k)(m), c_0>0, satisfies
C12 whenever its unique d row is nonnegative LC/NIZ. A PF hypothesis on d
also suffices, because PF implies LC/NIZ. **No PF conclusion for the output
is asserted here.** The theorem does not follow just from total
nonnegativity of the matrix K_n(r,k)=r!{n over r}_k.

The counting identity (1) and total nonnegativity of K_n are inherited from
archived AWS-C1. The proof below uses the counting identity, not total
nonnegativity. It provides the additional LC closure asked for by root.

## 2. Reduction by induction to one boundary inequality

For a fixed input row d, its prefix d_1,...,d_(n-1) remains LC/NIZ. Also

\[
F_n(m)=mF_{n-1}(m)+d_n(m)_n.\tag{2}
\]

Multiplication by m sends an ordinary Newton row u to

\[
v_r=r(u_r+u_{r-1}).\tag{3}
\]

This preserves nonnegative LC/NIZ. Indeed put s_r=u_r+u_(r-1). Then

\[
\begin{aligned}
s_r^2-s_{r-1}s_{r+1}
={}&(u_r^2-u_{r-1}u_{r+1})
 +(u_{r-1}^2-u_{r-2}u_r)\\
 &+(u_{r-1}u_r-u_{r-2}u_{r+1})\ge0.
\end{aligned}\tag{4}
\]

The third term is nonnegative by the separated-index LC inequality,
which is valid across zero boundaries for LC/NIZ rows. The sequence r,
extended by zero at negative indices, is LC/NIZ, so multiplying s_r by r
preserves LC. Its support is an interval.

In (2), the added term contributes only n!d_n to A_(n,n). Therefore all
LC comparisons at r<=n-2 follow by induction. The only new comparison is
at r=n-1. The cases n=1 and n=2 have no nontrivial missing boundary and
can be read directly. The argument below also covers the n=2 boundary.

The top three entries are

\[
\begin{aligned}
A_{n,n}&=n! S,& S&=\sum_{k=1}^n d_k,\\
A_{n,n-1}&=(n-1)! B,& B&=\sum_{k=1}^n b_kd_k,\\
A_{n,n-2}&=(n-2)! C,& C&=\sum_{k=1}^n c_kd_k,
\end{aligned}\tag{5}
\]

where

\[
b_k=\frac{n(n-1)-k(k-1)}2,
\qquad
c_k=\frac{((n-1)(n-2)-k(k-1))^2}{8}
 +\frac{(n-2)(n-1)(2n-3)-(k-1)k(2k-1)}{12}.
\tag{6}
\]

For k<=n-2, these are h_1(k,...,n-1) and h_2(k,...,n-2), respectively.
The displayed polynomial formulas also give b_n=0 and c_(n-1)=c_n=0.
They therefore correctly include every boundary column. The complete
homogeneous formulas follow by encoding a restricted set partition as a
path: at each existing block height j, a repeated label has j choices;
the D-r repetitions distribute among heights k,...,r.

The remaining desired inequality is exactly

\[
(n-1)B^2-nCS\ge0,\tag{7}
\]

because the ordinary LC defect is (n-1)!(n-2)! times (7).

## 3. A general cumulative-coefficient certificate

For integers 1<=L<=U<=n define

\[
\Phi(n,L,U)=\sum_{i=L}^{U}
 \bigl((n-1)b_i b_{L+U-i}-nc_i\bigr).
\tag{8}
\]

**Lemma.** Phi(n,L,U)>=0 for every such triple.

Here is a finite polynomial certificate for the entire infinite domain.
Put ell=L-1, h=U-L and v=n-U. These are independent nonnegative integers.
Then

\[
\Phi(n,L,U)=\frac{h+1}{120}
\sum_{i,j,k}q_{i,j,k}
 \binom{\ell}{i}\binom hj\binom vk,\tag{9}
\]

where all omitted coefficients are zero and the nonzero coefficients are
the following. A row lists q_(i,j,k) in increasing k beginning at k=0.

| i | j | coefficient row in k |
|---:|---:|---|
| 0 | 0 | 0,120,1560,4560,4920,1800 |
| 0 | 1 | 0,1140,4080,4740,1800 |
| 0 | 2 | 200,2960,4120,1680 |
| 0 | 3 | 780,2970,1440 |
| 0 | 4 | 936,1032 |
| 0 | 5 | 360 |
| 1 | 0 | 0,840,3600,4560,1800 |
| 1 | 1 | 0,2340,3720,1620 |
| 1 | 2 | 240,2440,1320 |
| 1 | 3 | 420,870 |
| 1 | 4 | 192 |
| 2 | 0 | 0,1440,2880,1440 |
| 2 | 1 | 0,1680,1080 |
| 2 | 2 | 80,640 |
| 2 | 3 | 60 |
| 3 | 0 | 0,720,720 |
| 3 | 1 | 0,360 |

There are 43 strictly positive coefficients. Every factor in (9) is
nonnegative for ell,h,v>=0 integers, proving the lemma.

Identity (9) is an ordinary polynomial identity, not a finite numerical
check. It follows by substituting (6) into (8), summing powers of i through
degree four, and expanding in the three binomial bases. The exact full
coefficient list is in KERNEL_BOUNDARY_SYMBOLIC_DISCOVERY.json. The
Wolfram kernel independently summed the symbolic expression (8), built
the right side of (9) from the 43 integers, and returned residual 0 and
all coefficients positive integers. Formal bounds L,U were intentionally
symbolic; the kernel emitted an undefined-symbol warning for their names,
but evaluated the sum and identity exactly. The raw receipt is retained.

## 4. Abel summation applies the certificate to every LC input

Expand (7) and group pairs by t=i+j. For a fixed t, put

\[
g_i=(n-1)b_i b_{t-i}-nc_i,\qquad
w_i=d_i d_{t-i}.
\]

The indices run from a=max(1,t-n) to b=min(n,t-1), symmetrically about t/2.
Let M=floor(t/2). The values w_i are symmetric and nondecreasing for
a<=i<=M. Indeed

\[
d_i d_{t-i}\ge d_{i-1}d_{t-i+1}
\]

is precisely the separated-index LC inequality. This remains true if
some input entries vanish, by the no-internal-zeros assumption.

Set

\[
G_i=\sum_{j=i}^{t-i}g_j=\Phi(n,i,t-i)\ge0.
\]

After pairing symmetric indices, ordinary finite Abel summation gives

\[
\sum_{i=a}^{b}g_iw_i
 =G_aw_a+\sum_{i=a+1}^{M}G_i(w_i-w_{i-1})\ge0.
\tag{10}
\]

For t odd the central pair is counted twice in G_M; for t even the central
singleton is counted once. The formula above therefore handles both
parities without an additional factor. Summing (10) over t proves (7).
Together with the induction, this proves HK-PLC.

The zero row is allowed. For a nonzero interval-supported d row with
minimum index s, (1) is strictly positive for every s<=r<=n and zero
below s, which proves the support assertion independently of the LC
calculation.

## 5. Source and contribution boundary

The archived PC-C1 cone theorem and AWS-C1 counting kernel are reused.
Wang--Yeh, *Log-concavity and LC-positivity*, fixed math/0504164v7,
motivated the central-cumulative/Abel criterion; equation (10) is proved
here directly. No theorem from a 2026 source enters this proof.

The argument proves a genuine general kernel closure, rather than
assuming every positive mixture is LC. The actual wall step remains:

> For every charge, prove that the unique scalar hook coordinates of the
> original raw tau are nonnegative, LC and have no internal zeros.

Neither the old all-q deficiency majorant nor honest BPS character
positivity supplies that assertion. This theorem is therefore a concrete
conditional interface to C12, not a solution of C12.
