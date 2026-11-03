# Rooted binomial multiplication preserves ordinary Newton LC

Root derivation, 2026-10-30, during the live five-hour run. This is an elementary general lemma and its exact application to the existing canonical packet formula. It is not a novelty claim, a proof of donor LC, or a proof of C12. Independent review completed at15:48:33UTC and admitted all three claims; see agents/rooted_multiplier_independent_audit/research/INDEPENDENT_AUDIT.md. The boundary wording below incorporates its editorial correction.

## 1. A support-sensitive affine multiplier

Write B_r(m)=binom(m,r). Let P(m)=sum_r p_r B_r(m), with a finite nonnegative log-concave coefficient row of interval support [L,U]. Extend the row by zero outside this interval. Let a be a nonnegative integer and assume L>=a. Multiplication by m-a gives

    Q(m)=(m-a)P(m),
    q_r=(r-a)p_r+r p_(r-1).

Every coefficient is nonnegative. If L>a then the new support is [L,U+1]; if L=a then it is [a+1,U+1]. The zero polynomial is harmless.

For r>=a+1 put t=r-a, u=p_(r-2), v=p_(r-1), w=p_r and z=p_(r+1). The exact defect decomposition is

    q_r^2-q_(r-1)q_(r+1)
      =(t^2-1)(w^2-vz)
       +(r^2-1)(v^2-uw)
       +(r-1)(t+1)(vw-uz)
       +(w+v)^2.

All three coefficients are nonnegative. Ordinary LC and interval support imply w^2>=vz, v^2>=uw, and vw>=uz. The last inequality is the standard outer-versus-inner two-step consequence of the decreasing adjacent ratios; it also holds when any index lies outside the interval, by the zero extension. Thus Q is LC on r>=a+1. For r<=a, q_r=q_(r-1)=0, so these boundary defects vanish; q_(a+1) may be positive. This proves ordinary Newton LC preservation, without any real-rootedness hypothesis.

The premise L>=a is essential to this formulation. Arbitrary affine multipliers with a negative constant term are not being admitted.

## 2. The rooted multiplier B_v(m)/m

Let v>=1 and assume P has nonnegative LC Newton coefficients with interval support [L,U], L>=1. Then

    B_v(m)P(m)/m = P(m)/v! product_(a=1)^(v-1)(m-a).

Apply the lemma successively for a=1,...,v-1. Before the step indexed by a, the support begins at max(L,a), so its hypothesis holds. The result has nonnegative LC Newton coefficients and support

    [max(L,v), U+v-1].

In particular, division by m in this expression is not being treated as an arbitrary LC-preserving inverse operation. The entire rooted binomial multiplier is handled as a positive sequence of supported affine operations. The case v=1 is the identity, and the resulting expression is polynomial.

## 3. Exact application to canonical fringe packets

The independently reviewed packet formula is

    P_gamma(m)=R_gamma(m)/m product_p K_(h_p;M_p)(m).

Here R_gamma is the product of binomial weights at all unchanged horizontal positions and all vertical positions; moving a whole red batch over zero grades leaves its vertical binomial weight unchanged. In a complete frame with positive red total, at least one vertical grade v is positive, so R_gamma has a factor B_v. Remove exactly this factor and denote the remaining product, including all donor K factors, by Q_gamma.

If each donor factor has an ordinary nonnegative LC Newton row, then the already reviewed Newton-product theorem proves that Q_gamma has such a row. Its constant coefficient is zero: the complete frame has positive blue total, and at least one positive horizontal weight is present, either as an unchanged B_h with h>0 or inside a donor K with h>0. Such a K vanishes at m=0 because every summand has positive total degree in the binomial factors. Hence the support of nonzero Q_gamma begins at L>=1.

The rooted-multiplier theorem now applies to

    P_gamma=(B_v/m) Q_gamma.

Therefore **donor-factor ordinary Newton LC would imply LC of every normalized canonical fringe packet**. No further generic division-by-m theorem is needed for these packets.

This removes one conditional interface in the packet route. It does not establish the donor premise, and it does not repair the exact negative cross-packet partial-synchronization defect already found on the actual EENENENN frame. The outer sum over normal forms, vertical data and terminal grades remains open. The separate all-gcd root T=G^(1/m) is unrelated to the scalar factor 1/m handled here and remains untouched.

## 4. Deduplication and verification scope

The inherited run5 primitive sink-extension note already records the same affine coefficient action and a PF-preserving support-threshold observation; the inherited run4 Schur-refinement report uses the action for support positivity. They are:

* run5 agents/wholewall_charge_interlacing/SINK_EXTENSION_INTERFACE.md, SHA 4084eecc5cb55120eb8ea35282dd85e75fc3fb8599d43dc90f1d52a02da48869;
* run4 agents/schur_refinement_closure/report.md, SHA f01b3e506df1550fd0ac5be3ec25950cf7e244f6ae83fcd12d67bb684bfadc0c.

The present contribution is the explicit ordinary-LC defect identity and its application to the current complete packet formula. The inherited action is not advertised as newly discovered. No new original-wall row or donor grid is computed. A single exact Wolfram identity control and a fresh mathematical review will be attached separately.
