# A conjugate-root region sufficient for ordinary Newton log-concavity

Status: a general sufficient operator theorem, with a self-contained exact algebra certificate. **Its root-region hypothesis has not been proved for actual scattering walls.** This is not a solution of C12. No claim of literature novelty is made.

## 1. The rank operator

Let f(m)=sum_r a_r binom(m,r), where a is nonnegative and log-concave with interval support whose first positive index is s>=1. Extend a by zero outside its support. Multiplication by a real linear factor gives

    E((m-alpha) f)_r = (r-alpha)a_r+r a_(r-1).

Multiplication by a real conjugate quadratic q(m)=(m-alpha)^2+beta, beta>=0, gives

    b_r = ((r-alpha)^2+beta)a_r
          +r(2r-1-2alpha)a_(r-1)+r(r-1)a_(r-2).       (1)

These are identities for the **ordinary** Newton coefficients. There is no division by r! in either the hypotheses or the conclusion.

**Theorem.** The linear multiplication preserves nonnegativity, interval support and LC if alpha<=s. The quadratic multiplication preserves these properties if

    alpha<=s,       0<=beta<=(s+1-alpha)^2-1/2.       (2)

In particular, the simpler uniform condition alpha<=s and beta<=1/2 is sufficient.

## 2. General same-sum argument

Write u=r-alpha and

    v_r=(u^2+beta, r(2u-1), r(r-1)).

Expand b_r^2-b_(r-1)b_(r+1). A term from the first square with offsets i,j in{0,1,2} has trace ell=i+j, distance |i-j| and coefficient v_(r,i)v_(r,j). A cross term has the same trace, distance |i-j+2| and coefficient -v_(r-1,i)v_(r+1,j). Its two input indices are r-1-i and r+1-j. This completely specifies the coefficient expansion without any omitted multiplicities.

For fixed trace ell, sort the input products by increasing distance between their two indices. Since a is LC with no internal zeros, these products decrease in that order. Thus Abel summation proves that the trace contribution is nonnegative whenever all prefix sums of its coefficients are nonnegative. This is only a sufficient test; it is not claimed necessary for a general LC-preserving operator.

There are eleven such prefixes for the quadratic operator. For r>=s+1, condition(2) gives r>=2,u>=1 and

    0<=beta<=u^2-1/2.

The eleven prefixes are as follows, in the order of increasing distance within each trace:

| trace | prefix |
|---|---|
|0| (beta+u^2)^2 |
|0| 2u^2-2beta-1 |
|1| -1-beta-r-3beta r-2beta u+2beta r u+3u^2+r u^2-2u^3+2r u^3 |
|1| -2(2+2beta-r+2u-2ru-2u^2) |
|2| -r(1+beta+beta r-2u+2ru+u^2-3ru^2) |
|2| -3-r-3beta r+3r^2+beta r^2-4u+2ru+2r^2u+4u^2-3ru^2+r^2u^2 |
|2| -5-2beta+2r+2r^2-8u+8ru+2u^2 |
|3| (r-1)r(3+r-2u+2ru) |
|3| 2(r-1)(1+2r+2u) |
|4| (r-1)^2r^2 |
|4| 2(r-1)r |

The first is positive. Every other prefix is affine in beta or independent of it. At both endpoints beta=0 and beta=u^2-1/2, put r=R+2 and u=U+1. Each is then a polynomial with nonnegative rational coefficients in R,U. Hence every prefix is nonnegative throughout the interval. The exact expanded coefficient lists are in PREFIX_EXACT_CERTIFICATE.json. The 80-line independent script prefix_certificate.py constructs the two products from(1), groups their terms, forms their prefixes, substitutes the endpoints and verifies each coefficient; it does not take the displayed table as input. A distinct Wolfram symbolic computation returned the same eleven prefixes and endpoint positivity.

For example, at the upper endpoint the second prefix is zero, and the first three nontrivial remaining prefixes become

    (3/2)(1+R)+7(1+R)U+10(1+R)U^2+4(1+R)U^3,
    6(1+R)+4(1+R)U,
    1+(3/2)R+(1/2)R^2+(4+6R+2R^2)(U+U^2),

which illustrate the uniform sign certificate rather than a finite parameter test.

The r=s LC inequality is automatic because b_(s-1)=0; all inequalities below it are also zero. Nonnegativity follows directly from(1) on the support. The only possible vanished first coefficient occurs at alpha=s,beta=0; the next one is positive, and the other band coefficients ensure there are no internal zeros. The high endpoint increases by two. Thus the entire zero-extended sequence is LC.

For the linear factor use v_r=(u,r). Exactly the same argument has six prefixes, all with nonnegative coefficients after r=R+2,u=U+1. These are also generated independently in PREFIX_EXACT_CERTIFICATE.json. The support endpoint arguments are identical, with degree increase one.

## 3. A full-polynomial root criterion

Let f be a real polynomial with positive leading coefficient, f(0)=...=f(s-1)=0 and s>=1. Suppose every root zeta of

    f(m)/(m)_s

satisfies

    Re(zeta)<=s,
    (Im(zeta))^2 <= (s+1-Re(zeta))^2-1/2.          (3)

Then the ordinary Newton coefficients of f are nonnegative, have interval support and are LC.

Indeed (m)_s has the one-point Newton row a_s=s!. Factor the quotient over the reals into real linear factors and conjugate quadratics. Each real factor obeys the linear theorem. Every quadratic obeys(2). After any multiplication, the support start is at least the original s, which only weakens the needed conditions; therefore all factors may be applied successively. A positive overall scalar does not change LC. This proves the criterion without assuming real-rootedness of f.

For C12 take s to be the actual first nonzero Newton rank, so the mandatory integer roots follow from the vanishing of the first s integer values. A general proof of(3) for every original raw wall would therefore settle C12 for all gcd. This criterion does not use a palette power or connected-log substitute.

## 4. What has and has not been tested

One preregistered numerical discovery gate used nine existing complete wall rows, beginning with all five old known nonreal-raw examples. Wolfram solved the residual polynomials at60-digit working precision. All nine satisfy even the stronger rectangle Re<=s, |Im|<=1/sqrt(2) in that screening; the largest observed imaginary part was about0.057393. The selected charges, exact ordinary Newton inputs and full tool receipt are saved. This is **numerical screening**, not root isolation, a new wall computation, or a general root theorem. No domain expansion or extra degree sweep was performed.

The old raw-real-rootedness conjecture remains false, e.g.(5,13); the root criterion intentionally permits its conjugate pair. The generic real-rooted synthetic counterexample with Newton row(0,0,1,1,100) has a real root greater than its support start, so it does not satisfy(3).

The task for the next branch is an actual structural root-domain proof or an exact actual counterexample to(3). Rephrasing(3) as an unknown root bound is not by itself an advance beyond this newly proved operator. Appropriate next interfaces include a determinant/transfer representation whose numerical range lies in(3), or a zero-free theorem for the actual complete-wall recurrence. No such representation is claimed here.
