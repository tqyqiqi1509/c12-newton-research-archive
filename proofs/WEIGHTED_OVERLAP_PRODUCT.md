# Weighted overlap extension of the proved ordinary Newton product lemma

## Statement and direct derivation

For lambda>=0 define

`C_n^lambda(a,b)=sum n! / ((n−i)!(n−j)!(i+j−n)!) * lambda^(i+j−n) * a_i b_j`,

with max(i,j)<=n<=i+j. For nonnegative LC interval-supported inputs, this output is also LC. At lambda=1 this is the ordinary Newton product; at lambda=0 it is binomial convolution (only disjoint pairs survive). No source theorem is needed beyond the elementary proof in the newton_union_product branch.

To verify the extension, replace B_i by `(I+lambda Shift)^i b`. The neighbor-sum LC defect decomposes as the first old defect plus lambda times the old cross difference plus lambda^2 times the second old defect, hence remains nonnegative. The adjacent kernel minor, after its positive binomial factor is removed, is exactly

`(k+1)B(k)^2 + lambda B(k)B(k+1) − kB(k−1)B(k+1)`

`= k*(B(k)^2−B(k−1)B(k+1)) + B(k)^2 + lambda B(k)B(k+1) >=0`.

The same TP2 and shifted-ratio argument applies. Partitioning the last element into first-only, second-only and both now gives

`C_(n+1)^lambda = C_n^lambda(a+,b)+C_n^lambda(a,b+)+lambda*C_n^lambda(a+,b+)`.

The quotient is the sum of two decreasing ratios and lambda times their decreasing product. Positive epsilon-tail approximation treats zeros exactly as in the main proof. For lambda>0 the positive support is `[max(La,Lb),Ua+Ub]`; for lambda=0 it is `[La+Lb,Ua+Ub]`, so there are no internal zeros in either case.

## Why the theorem has the right strength, and its limit

It is weaker than PF preservation. With A=B=1000+t, the ordinary product is `1000000+2001t+2t^2`. It is LC, with residual 2004001, but has negative discriminant −3995999. Thus no real-rootedness is silently asserted.

The overlap parameter is a possible interface for endpoint fusion in the actual cut recursion, where disjointness and overlap of color subsets matter. **No equality between the whole endpoint-gluing operation and this one-parameter kernel has been proved.** The extension is retained as a toolbox result, not as a newly closed C12 sum arrow. The complete unit-cut comparison and all-gcd extraction remain open.

Wolfram independently checked the weighted-minor identity and the displayed integer control. Its actual receipt is in `computations/wolfram_weighted_product_identity.json`. These checks calibrate identities and are not new wall coverage.
