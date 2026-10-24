# What a lower and upper crossover bound can mean for the new PR4470 realization

This note excludes API/ABI limits. Fix one baseline algorithm B extended to
arbitrary public input lengths, and one common cost model. An “optimized GMP”
comparison must specify that extension: dispatch tables/profile, limb width,
instruction lowering and the costs being counted. A proof about a particular
unrolled circuit is not a wall-clock theorem, and no universal n*log(n) lower
bound for integer multiplication is assumed.

The separate inventory audit proves D_N<2^(9HN) for a new source-permitted
nested compiler, with H=64215200000000 and N=2^H. Write M_N=2^(9HN). Let A be
an integer for which a **separate complete validity and comparison proof**
establishes the candidate bound for p>=P=M_N^A. This note does not certify
that gate or invent a missing optimized-GMP coefficient.

## Exact integer endpoint of the precision gate

For the current packing p(n)=256ceil(log2n), put

    B0=P/256,
    L=2^(B0-1)+1,
    U=2^B0.

P is a power of two divisible by256. For integer n>=1,

    p(n)>=P  iff  ceil(log2n)>=B0
               iff  n>2^(B0-1)
               iff  n>=L.

In particular p(L-1)=P-256, p(L)=P and p(U)=P. Thus L is the exact smallest
operand length meeting this precision prescription. The simpler sufficient
endpoint U is less than twice L: U=2(L-1). This precision-bin endpoint is
not, by itself, a natural crossover lower bound.

## A defined hybrid can have an exact first strict model-cost crossover

Define a hybrid H_B that executes **the exact same baseline program B** for
n<L and the selected candidate C for n>=L. Suppose the fully charged model
cost satisfies T_C(n)<T_B(n) for every n>=L. Then

    T_HB(n)=T_B(n) for n<L,
    T_HB(n)<T_B(n) for n>=L.

Its actual first strict crossover in that model is therefore exactly L.
This is mathematically legitimate, but it is the chosen branch switch.
It does not discover the natural earliest crossover of an unmodified
candidate or prove that the candidate could not have won earlier. Changing
the switch changes this engineered statistic. It should be labeled
“first strict crossover of the specified hybrid,” not “the first PR4470
crossover.”

Public-size dispatch is free for the nonuniform circuit family. In a model
charging dispatch, allocation, copying or calls, those charges must be in
the candidate upper. Identical fallback must mean identical baseline cost
under the same input/size policy; worst-case and per-input comparisons must
not be mixed silently. The claim remains conditional on the retained native
PR4470 contracts and the separately proved arithmetic envelopes.

## The optimized-baseline coefficient that is still required

Suppose, in the chosen model,

    T_C(n,rho) <= a_C(rho)*n*p^(1-kappa),   p>=P,
    T_B(n,rho) >= b_B(rho)*n*log2n,        n>=n_B,
    kappa=60403/20000000, b_B(rho)>0.

Since log2n>p/256-1, for p>256 the ratio is strictly less than

    [256 a_C(rho)/b_B(rho)] *p^(-kappa)/(1-256/p).      (1)

The p-dependent part decreases on p>256: the derivative sign of
p^(1-kappa)/(p-256) is -kappa*p-256(1-kappa)<0. Consequently checking (1)
at P suffices for the whole tail. A simpler sufficient condition is

    P>=512,
    P>[512 a_C(rho)/b_B(rho)]^(1/kappa),
    L>=n_B.                                           (2)

If those conditions and all candidate validity conditions hold, the hybrid
theorem applies at the exact endpoint L. Otherwise increase the switch gate
until they do; declaring fallback does not supply the missing domination.

For example, if a separate candidate tail proof gives a_C(rho)=1+rho, and
the specified optimized baseline has lower coefficient
b_B(rho)=g_AND+g_XOR*rho with both g constants positive, then uniformly for
rho>0,

    (1+rho)/(g_AND+g_XOR*rho)
       <=max(1/g_AND,1/g_XOR)=1/min(g_AND,g_XOR).

Thus 512/min(g_AND,g_XOR) is a sufficient universal ratio coefficient in
(2). Until these source-specific lower constants and their validity domain
are derived, this is a conditional formula, not a numerical optimized-GMP
crossover. Merely knowing that some unspecified positive coefficient exists
does not instantiate it.

## A weaker activation lower bound needs less prefix information

Ignoring all ABI limits, a literal selected uniform invocation needs N
selected binary Gaussian axes. Under the unchanged packing and outer
exponents epsilon=1-1/1400000000, beta=1-3/1400000000, earlier exact arithmetic
gives necessary activation conditions

    main target supplier: n>2^(2^64215200045860),
    interior Gaussian group: n>2^(2^64215200137596).

For a hybrid defined to execute B unchanged until its corresponding literal
template can activate, its first strict improvement cannot precede that
activation. This is meaningful for that specified family, independently of
the large sufficient proof gate. It is not a lower bound for a smaller
compiler, different packing or another profitable earlier branch. The
stronger group condition applies only when the hybrid explicitly waits
for that group-level selected template; one must not apply it to a branch
using only an earlier component.

Without an identical-baseline prefix or independently bounded prefix costs,
the candidate's tail upper envelope gives a sufficient eventual upper
bound and does not locate the actual first strict crossover. Nothing in a
tail upper bound excludes an earlier correct, cheaper execution. Defining
fallback repairs the missing prefix information for a chosen hybrid;
it does not prove a fundamental earliest input size.

The new `.py/.json` checks 13 exact precision bins, both selected activation
offsets and 27 positive-tariff inequalities. It binds the inventory JSON.
No old published certificate or site was changed.
