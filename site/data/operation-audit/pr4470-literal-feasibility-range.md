# A derived non-win prefix for the selected literal PR4470 construction

This note combines a necessary native-work count with a competing-source upper bound. It does not choose a switch threshold and call that threshold a crossover. The adjacent certificate is issued only after both underlying proofs and the unlimited-input reference repair have passed their closure checks.

## The precisely scoped quantity

Fix the declared XOR–AND model, AND cost 1 and XOR cost rho>0. Fix the optimized GMP 6.3.0 Tiger Lake source profile, its effective Skylake tuning table, and the exact-constant unlimited continuation identified by `gmp-630-native-skylake-unbounded-exact-constants-v2`. Its native data limbs remain 64 bits. Public indices and the two explicitly identified large correction quantities have exact mathematical representations. All required input-dependent work is charged.

Consider the family of correct enhancements that execute this same GMP circuit when the selected PR4470 supplier is inactive, and retain at least one unreduced dense invocation of that supplier when it is active. The supplier has N=2^H, H=64215200000000. Fixed wiring is free; scalar arithmetic is retained. Algebraic compression, deletion of known-zero work, smaller suppliers and a different faster inactive algorithm define different families.

Let F(rho) be the least input length n>=2 at which **some** enhancement in this family has strictly smaller cost than the reference. This is the earliest attainable strict improvement in the declared family. It is not the exact first crossing of one fully counted all-size implementation. A first eventual threshold can be defined separately. The same bounds below apply, but those two quantities need not coincide.

## Opposite cost bounds establish a real exclusion

The pinned native-work census proves that an active invocation contains

    c =630412*(64620^1024-10928^1024)/53692

real ADDs per common complex coefficient coordinate, with c>=2^16366. A complete N-axis field has at least 2^N coordinates. The retained ripple lowering therefore has

    AND_candidate >=c*2^N,
    XOR_candidate >=3c*2^N,
    W_candidate >=(1+3rho)c*2^N.

This is a lower count of a specified literal program, not a lower bound for multiplication as a function.

The separate optimized-GMP upper module supplies, under its explicitly completed circuit semantics and ordinary finite native correctness/halting contracts,

    AND_GMP(n), XOR_GMP(n) <=2^(2^73)*(n+1)^16.

Its huge coefficient is derived from finite native execution and a source-counted recursive envelope. It is not a benchmark extrapolation, a chosen runtime switch, or a realistic estimate of the actual GMP coefficient. Its use is conservative: a faster implementation of those same source operations only strengthens this exclusion.

Consequently put

    r(rho) =floor_16th_root[ ((1+3rho)/(1+rho))*c*2^(N-2^73) ].

The floor root is unambiguous: it is the largest integer r for which

    (1+rho)*r^16 <=(1+3rho)*c*2^(N-2^73).

For every n<=r(rho)-1 the competing upper is no greater than the active candidate lower. No active candidate can be strictly faster there. An inactive candidate has exactly the reference cost. Thus **no policy in this family can win anywhere in that prefix**, independently of its size-dispatch rule:

    F(rho) >=r(rho).

The formula can be kept exact in compressed integer arithmetic. It need not be expanded into an impossible array of digits. With rho=a/b it compares `(a+b)r^16` with `(b+3a)c*2^(N-2^73)`. The cost slider therefore changes the proven lower expression through the exact factor `(b+3a)/(b+a)`, which lies strictly between 1 and 3. It does not supply the still-unknown actual crossing.

## An explicit tariff-independent numerical lower

For a convenient exact power endpoint define

    z =N/16-2^69+1022,
    L0=2^z=2^(2^64215199999996-2^69+1022).

This endpoint is derived by substituting the two counted cost bounds. It is not an implementation threshold. H>=80 ensures z is a positive integer. For n<=L0-1,

    log2(2^(2^73)*(n+1)^16)
        <=2^73+16z
         =N+16352
         <N+16366.

An active candidate is therefore more expensive by a factor of at least 2^14 in this entire prefix, even before its other work is included. The implication is uniform for all positive tariffs. In particular

    F(rho) >=L0.

This replaces the trivial lower 2 for this explicit literal-core enhancement family. It says nothing comparable about every algorithm that could use the PR4470 research idea.

## Combine with the independently counted eventual upper

The existing nested-realization theorem supplies a correct candidate whose cost is strictly below the corrected reference for all sufficiently large n, under the retained native and analytic contracts. The reference repair preserves the root geometry and mandatory native additions used in that lower-cost comparison; its extra operations are nonnegative. The previously proved sufficient endpoint consequently transfers:

    M_N=2^(9HN), A=1400000001,
    U=2^(M_N^A/256)
     =2^(2^(809111520577936800000000*2^64215200000000-8)).

Using that witness in the declared family gives

    2^(2^64215199999996-2^69+1022) <=F(rho)<=U.

This is a very wide conditional feasibility range. It is not a realistic narrow crossover estimate, a hardware-time prediction, a universal barrier for PR4470, or evidence that the source's sufficient rank is minimal. The lower comes from unavoidable work **when this literal supplier is used**, and a genuine upper on the competitor. The upper comes from one complete, explicitly counted large-size construction. The required contracts are part of the claim.

## Reading the historical plots

The plot coordinate is Y=log2 log2 log2 n. L0 is near Y=log2(64215199999996), while U is near Y=64215200000079.42. A trillion-bit operand is near Y=2.41. These points describe the bounds just derived, not observations of the true crossing. Changes in kappa alone do not determine either endpoint. Other PRs receive a number only after an analogous construction-specific derivation; an uncosted entry has no numerical y-value.

All derivations here are AI-assisted written mathematical arguments with source hashes and executable exact checks. They are not Lean formalization or independent human review.
