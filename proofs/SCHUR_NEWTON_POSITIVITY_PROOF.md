# Coordinatewise Newton multiplication preserves two-variable Schur positivity

**Status:** complete elementary proof draft, 2026-10-30 around 12:56 UTC;
independent root review passed on 2026-10-30 around 13:00 UTC (see c12_run6/audit/ROOT_AUDIT_04_SCHUR_NEWTON.md). Root supplied the decisive reflected-window
comparison; this branch independently checked it and supplied the symmetric
decomposition of the both-membership boundary. No external theorem is a premise
apart from elementary binomial identities and the definition of two-variable
Schur polynomials. Finite tests are not premises.

## 1. Product and claim

Put

\[
K_n(i,j)=
\begin{cases}
n!/((n-i)!(n-j)!(i+j-n)!),&\max(i,j)\le n\le i+j,\\
0,&\text{otherwise},
\end{cases}
\]

including zero for negative indices. Define the coordinatewise Newton product
by

\[
x^iy^j\diamond_2 x^ky^\ell
 =\sum_{n,m}K_n(i,k)K_m(j,\ell)x^ny^m.
\]

For p>=q>=0,

\[
s_{(p,q)}(x,y)=\sum_{i=q}^{p}x^iy^{p+q-i}.
\]

**Theorem.** If two symmetric polynomials in x,y are nonnegative linear
combinations of these Schur polynomials, so is their coordinatewise Newton
product.

By bilinearity, it suffices to consider s_(p,q) and s_(r,s).

## 2. A reflected-window boundary lemma

Let n>=l>=0 and u>=v>=0. Let T>=0 and let J=[alpha,beta] be an integer interval
with alpha+beta=T. We may intersect J with [0,T]; if it is nonempty this
intersection is still centered at T/2. Define

\[
L=\sum_{j\in J}
 \bigl[K_n(u,j)K_l(v,T-j)-K_n(v,j)K_l(u,T-j)\bigr].
\tag{1}
\]

Then L>=0.

If any of

\[
a=n+l-T,\quad b=n+l-u-v,\quad c=u+v+T-n-l
\]

is negative, all terms are zero. Assume they are nonnegative. Put

\[
A=\binom nu\binom lv,\quad B=\binom nv\binom lu,\quad
d=u-v,\quad D=n-l.
\]

If B=0, L>=0 directly from (1). If B>0, all four binomial coefficients
defining A and B are positive and A>=B by the TP2 property of the Pascal
matrix. Explicitly, since u>=v,

\[
\frac{A}{B}
=\prod_{h=v}^{u-1}\frac{n-h}{l-h}\ge1.
\tag{2}
\]

The empty product for u=v is one.

For

\[
w_t=\binom ut\binom v{c-t},\qquad
W=[\alpha-n+u,\ \beta-n+u],
\]

expand the two K factors after choosing the first set. Explicitly,

\[
K_n(u,j)=\binom nu\binom u{u+j-n},\qquad
K_l(v,T-j)=\binom lv\binom v{v+T-j-l}.
\]

Setting t=u+j-n makes the two lower binomial arguments t and c-t.
In the second term, interchange u,v and then replace its common-red count
by c-t. This gives exactly

\[
L=A\sum_{t\in W}w_t-B\sum_{t\in W+D}w_t.
\tag{3}
\]

The center of W is (c+d-D)/2. Consequently W+D is its reflection under

\[
t\longmapsto c+d-t.
\]

For every integer t<=(c+d)/2,

\[
w_t\ge w_{c+d-t}.
\tag{4}
\]

To prove (4), only the case w_(c+d-t)>0 needs consideration. Its support
conditions imply d<=t<=u and t>=c-v. Together with t<=(c+d)/2 they imply
c>=d and t<=c. Thus w_t is also positive. Cancellation of factorials yields

\[
\frac{w_t}{w_{c+d-t}}
 =\frac{(c+d-t)!(t-d)!}{t!(c-t)!}
 =\prod_{h=1}^{d}\frac{c-t+h}{t-d+h}\ge1.
\tag{5}
\]

Each numerator is at least its denominator because c+d-2t>=0.
For d=0 this is equality.

Since D>=0, W is the left interval and W+D the right interval. Their common
part cancels. Reflection pairs the left-exclusive part with the right-exclusive
part, and every left-exclusive point is <=(c+d)/2. Therefore (4) gives

\[
\sum_Ww_t\ge\sum_{W+D}w_t.
\]

Together with A>=B this proves (3) nonnegative.

The same lemma remains valid if v=-1: both terms in (1) are identically zero.
This convention is useful when an original Schur band has lower endpoint zero.

## 3. The homogeneous coefficient and its boundary difference

Set

\[
P=p+q,\quad R=r+s,\quad N=n+m.
\]

Let H_n be the coefficient of x^n y^(N-n) in the product. It is nonnegative
and symmetric: H_n=H_(N-n). The Schur coefficient at (n,N-n), n>=N-n, is

\[
H_n-H_{n+1}.
\tag{6}
\]

For m=0, this is just H_N>=0, because H_(N+1)=0. Assume m>=1 and write
l=m-1. In particular n>=m implies n>=l.

A product coefficient counts a covering pair of subsets on the red atoms
and a covering pair on the blue atoms, with the two input red cardinalities
in [q,p] and [s,r]. Distinguish the last blue atom and move it to the red
side. Its membership in the two subsets is one of

\[
(1,0),\quad(0,1),\quad(1,1).
\]

Let

\[
A(i)=1_{[q,p]}(i),\quad A'(i)=1_{[q-1,p-1]}(i),
\]
\[
B(j)=1_{[s,r]}(j),\quad B'(j)=1_{[s-1,r-1]}(j).
\]

The exact difference (6) is the sum of the following three membership
contributions.

### First-only

\[
D_{10}=\sum_{j=s}^{r}
 \bigl[K_n(p,j)K_l(q-1,R-j)
       -K_n(q-1,j)K_l(p,R-j)\bigr]\ge0.
\tag{7}
\]

Apply the boundary lemma with u=p,v=q-1,T=R and the centered interval [s,r].
When q=0 both terms vanish by the negative-index convention.

### Second-only

The expression is obtained by swapping the two subsets and the two input
bands. The same boundary lemma gives D_(01)>=0.

### Both

The remaining kernel is

\[
W(i,j)=K_n(i,j)K_l(P-1-i,R-1-j).
\]

The both-membership contribution is

\[
D_{11}=\sum_{i,j}W(i,j)\bigl(A(i)B(j)-A'(i)B'(j)\bigr).
\tag{8}
\]

Use the exact algebraic identity

\[
AB-A'B'=\frac12\bigl[(A-A')(B+B')+(A+A')(B-B')\bigr].
\tag{9}
\]

Now A-A'=delta_p-delta_(q-1), while

\[
B+B'=1_{[s-1,r]}+1_{[s,r-1]}.
\tag{10}
\]

Both intervals in (10) are centered at (R-1)/2; an empty interval contributes
zero. Thus the first summand in (9), summed against W, is a sum of two
boundary-lemma expressions with u=p,v=q-1,T=R-1.
The second summand is the symmetric counterpart, because

\[
A+A'=1_{[q-1,p]}+1_{[q,p-1]}
\]

is a sum of centered intervals about (P-1)/2 and
B-B'=delta_r-delta_(s-1). Hence both summands in (9) are nonnegative.

If P=0 or R=0, no atom can belong to both subsets and D_(11)=0. Otherwise
T=P-1 or R-1 is nonnegative as needed. When s=0 or q=0, any interval with a
negative lower endpoint is simply intersected with the corresponding natural
count range; the intersection is the full centered interval. Negative-index
delta terms contribute zero. No boundary term is discarded.

We have proved D_(11)>=0. Combining the three types establishes (6), and
therefore proves the theorem.

## 4. Corollary: common Newton multiplication preserves partial synchronization

Let A,D,C be nonnegative finite LC sequences with interval support, and suppose
A,D are partially synchronized:

\[
a_md_n+a_nd_m\ge a_{m+1}d_{n-1}+a_{n-1}d_{m+1}\qquad(m\ge n).
\tag{11}
\]

Equation (11) says exactly that

\[
F(x,y)=A(x)D(y)+A(y)D(x)
\]

is Schur-positive in two variables. LC of C says that C(x)C(y) is
Schur-positive: along every homogeneous diagonal its coefficient difference
is c_m c_n-c_(m+1)c_(n-1)>=0. The no-internal-zero hypothesis handles support
boundaries of this last inequality.

The theorem gives Schur positivity of

\[
F\diamond_2(C(x)C(y))
=(A\diamond C)(x)(D\diamond C)(y)
 +(A\diamond C)(y)(D\diamond C)(x).
\]

Thus the two output rows satisfy all partial synchronization inequalities.
Their individual LC and interval support follow from the root-reviewed
ordinary Newton multiplication theorem. This proves preservation of partial
synchronization by every common LC Newton factor.

In contrast, preservation of **strong** synchronization and of
Gross-style ratio-dominance is false, by the positive-input family
A=(a,1,1), D=C=(1,1,1), 0<a<1. Global likelihood-ratio order alone is
preserved by the fixed-factor TP2 kernel.

## 5. Weighted overlap and exact scope

For a nonnegative overlap weight lambda, replace K_n(i,j) by
lambda^(i+j-n) K_n(i,j). On fixed homogeneous input degrees P,R and output
degree N, the entire coefficient polynomial is multiplied by
lambda^(P+R-N). This is nonnegative. Hence the two-variable Schur theorem
and the common-factor partial-synchronization corollary also hold for every
lambda>=0, including lambda=0 with the usual convention for zero overlap.

This closes a general comparison-preservation arrow. It does not establish
that the actual EN children or all complete blocks are partially synchronized,
nor that their endpoint fusion is a common scalar Newton factor. The unit-cut
formula uses different binomial factors on different linked children; that
actual comparison and the all-gcd extraction remain separate obligations.

The proof makes no claim of bibliographic novelty. The accessible Heisenberg
product source identifies the one-variable cover kernel but does not supply
the two-variable proof above. None of the searched 2026 papers is a premise.


## 6. Polarized corollary: a sum of the two product pairings

For two rows U,V define the partial-synchronization defect

\[
\mathcal D_{m,n}(U,V)
=u_mv_n+u_nv_m-u_{m+1}v_{n-1}-u_{n-1}v_{m+1},
\qquad m\ge n.
\]

Suppose A,B,C,D are finite nonnegative LC/NIZ rows, with A,B partially
synchronized and C,D partially synchronized. Put

\[
U=A\diamond C,\quad V=B\diamond D,\quad
S=A\diamond D,\quad T=B\diamond C.
\]

Then, for every m>=n,

\[
\boxed{\mathcal D_{m,n}(U,V)+\mathcal D_{m,n}(S,T)\ge0.}
\tag{12}
\]

Indeed the Schur-positive polynomial

\[
(A(x)B(y)+A(y)B(x))\diamond_2
(C(x)D(y)+C(y)D(x))
\]

expands exactly as

\[
U(x)V(y)+U(y)V(x)+S(x)T(y)+S(y)T(x).
\]

Its Schur coefficient at (m,n) is the left side of (12). This proof includes
all zero boundaries and also applies to the nonnegative overlap-weighted
product.

At m=n=r, (12) is the nonnegativity of the sum of the two ordinary
adjacent-rank mixed defects,

\[
\begin{aligned}
&2u_rv_r-u_{r+1}v_{r-1}-u_{r-1}v_{r+1}\\
&\quad+2s_rt_r-s_{r+1}t_{r-1}-s_{r-1}t_{r+1}\ge0.
\end{aligned}
\]

This is a **collective** comparison. It does not assert partial synchronization
of U,V individually, or of S,T individually. To apply it to an actual complete
cut sum, both product pairings and their exact weights must occur, or a
separate positive allocation must supply them without double counting. No such
identification for the full C12 recursion is proved in this branch.


