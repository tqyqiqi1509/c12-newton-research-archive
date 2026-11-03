# Supplementary statements on scattering coefficients

This is a catalogue of statements recorded in companion research notes, prepared for an appendix without proofs. It is not a claim that the statements follow from the Newton closure theorems in the main text. A submitted version must supply precise, reviewer-accessible references to the corresponding proofs. Results whose inherited inputs have not been fully incorporated remain identified below.

## Notation

For positive integers A and B, let τ_m(A,B) be the coefficient of the corresponding monomial in the original wall function of the rank-two cluster scattering diagram with exchange matrix [[0,m],[-m,0]]. Its polynomial extension in m has the ordinary Newton expansion

\[
\tau_m(A,B)=\sum_{j=0}^{D}a_j(A,B)\binom mj,
\qquad D=A+B-1,\qquad a_j=\Delta^j\tau(0),
\]

where Δf(m)=f(m+1)−f(m). The coefficients are not divided by j!. A row is log-concave if a_j²≥a_{j−1}a_{j+1}; strict log-concavity below refers to indices whose three coefficients are positive. All logarithms are natural.

## A. Uniform prefix for integer slopes

There exists an absolute integer A★ such that, for all integers A≥A★ and r≥8, the row with B=rA+1 satisfies a_0=⋯=a_r=0, a_{r+1}>0, and

\[
a_j^2>a_{j-1}a_{j+1}>0
\quad\text{for}\quad
r+2\le j\le r+\left\lfloor\frac{A}{96\log A}\right\rfloor-1.
\]

The threshold is independent of r and is not numerically specified. The proof in `UNIFORM_SLOPE_PREFIX_THEOREM.md` uses the actual Euler/MPS identity, real-parameter entropy curvature, a uniform complex saddle estimate and ordinary finite differences. Those inputs are separate from the abstract Newton closure theorem.

## B. Eventual whole-row log-concavity at a fixed integer slope

For every fixed integer r≥8 there exists A₀(r) such that, for all integers A≥A₀(r), the entire ordinary Newton row for (A,rA+1) is nonnegative, log-concave and unimodal, and is strictly log-concave inside its positive support.

This combines A with the historical primitive bulk estimate. It does not assert a whole-row threshold independent of r. The historical bulk proof and its external inputs must accompany this statement.

## C. Eventual whole-row log-concavity for residue two

For every integer A≥3 there exists an integer K₀(A) such that, for all k≥K₀(A), the ordinary Newton row for (A,Ak−2) is nonnegative, log-concave and unimodal. Its positive support is

\[
k\le j\le Ak+A-3,
\]

and its internal log-concavity is strict. When A is even, this includes gcd(A,Ak−2)=2. The threshold has not been numerically specified.

The proof uses the total-charge-two transportation polynomial, the actual-wall limiting identity, Weyl symmetry, a finite-head argument and a historical uniform high-tail estimate. The tail estimate has not been replaced by a consequence of the Newton closure theorem.

## D. Primitive bulk at bounded aspect ratio

For every fixed ρ≥1 there exists D₀(ρ) such that, whenever A,B≥2 are coprime,

\[
\frac{\max(A,B)}{\min(A,B)}\le\rho,
\qquad D=A+B-1\ge D_0(\rho),
\]

one has strict log-concavity at every integer j satisfying

\[
80(\rho+1)\sqrt D+1\le j\le D-1.
\]

Here “bulk” means a large-scale range of coefficient indices, not a separate normalization or a sum of coefficients. In particular, each fixed proportional range j≈δD, with δ>0, is eventually included. The low-index boundary and finite parameter region are not covered by this statement. This is an inherited result whose full source chain remains to be integrated.

## E. A high-tail statement without a coprimality assumption

Fix integers A≥2 and 0≤c<A. Define

\[
C_A=2^{16A}A^{12A},\qquad B=Ak-c,\qquad D=A+B-1.
\]

The recorded R216 result, with its stated ROOT25/26 identity inputs, asserts that if

\[
k\ge\max\{2A,(64C_A)^2\},
\]

then, for every integer s with 2A≤s≤D−k−1 and R=k+s,

\[
\log\frac{a_R^2}{a_{R-1}a_{R+1}}\ge\frac1{8s}>0.
\]

“All gcds” means that no coprimality assumption is imposed on A and B. It does not remove the displayed restrictions. “High tail” is measured by the surplus s=R−k and can contain many indices; it does not mean only the last two coefficients. This is a recorded result with inherited inputs, not an independently re-established unconditional theorem in the present note.

## F. Conditional applications

### Hook coordinates

Let n≥1 and (m)_k=m(m−1)⋯(m−k+1). If a wall polynomial admits the exact fixed-degree expansion

\[
\tau_m=\sum_{k=1}^{n}d_k m^{n-k}(m)_k
\]

with d_k nonnegative, log-concave and without internal zeros, then its ordinary Newton row is nonnegative, log-concave and without internal zeros. When the first positive hook coefficient is d_s, the output support is [s,n]. The hypothesis on the actual hook coordinates is not established for all walls.

### A root-region criterion

Let f be a real polynomial with positive leading coefficient, divisible by (m)_s for an integer s≥1. If every zero ζ of f/(m)_s satisfies

\[
\operatorname{Re}\zeta\le s,
\qquad (\operatorname{Im}\zeta)^2
\le(s+1-\operatorname{Re}\zeta)^2-\tfrac12,
\]

then its ordinary Newton row is nonnegative, log-concave and without internal zeros. A uniform root-region theorem for the actual wall polynomials remains unproved.

### Positive Euler factors

Fix a primitive ray and the exact original-wall factorization T_m(z)=∏_{j≥1}(1+z^j)^{q_j(m)}. Assume that each required actual q_j has a nonnegative integer, log-concave ordinary Newton row without internal zeros. The binomial-selection and product theorems imply the same properties for every partition contribution

\[
\prod_j\binom{q_j(m)}{\ell_j},\qquad \sum_jj\ell_j=k.
\]

They do not imply log-concavity of the sum over partitions. Actual atom log-concavity and the final collective comparison remain separate obligations. If a parity Euler factorization is used instead, the q_j must first include the prescribed binary-cover conversion; raw even exponents cannot be silently substituted.
