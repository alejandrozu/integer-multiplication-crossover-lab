# PR4470: complete-job cancellation and a bounded suspended Clifford stack

This is a further **conditional** sufficient upper for the original PR4470
rank N=2^64215200000000 and kappa=60403/20000000. It supersedes neither its
source contracts nor the frozen backup proofs. It is an AI-assisted written
derivation and exact arithmetic, not Lean formalization or human review.
The model is the previously fixed nonuniform XOR–AND circuit family, with
free wiring and size-only synthesis, charged data arithmetic and no claimed
hardware time. The source native and analytic contracts remain premises.

The refinement uses two exact cancellations: rank mass across the **whole**
compiled supplier, and completed Clifford endpoints between suspended native
prefixes. It never treats the total compiler inventory as a precision guard.

## 1. Parameters and preserved interfaces

```
H=64215200000000, N=2^H, m=145^1024,
k=33010, l=4497, g=floor(H/l), J=mH,
Qstop=1400000000, A=1400000001, delta=1/Qstop.
```

As in the independent rank-mass proof, the completed mixed unit has positive
integer surplus Delta=239886^1024-239134^1024, at least one. Its full finite
scalar/phase/adapter allowance is below K^2, where K=32(R*+1)<2^k. Its
completed productive floor is 21^1024>2^4497, and its maximum paid rank is
below m/2. The raw minimum productive rank4 is not confused with this floor.

The source compiler retains its original ordinary bases. Its nonbase
complement and exit child ranks are at most (1-1/m) times the parent rank.
The exact Bernoulli argument in the replication-depth backup gives at most
J recursive compiler edges and at most g+1 live flow classes per level.
Denominator copies and distinct native unit instances in one class use the
same chronological lockstep stages, with separately tagged owned banks.

## 2. Whole-word rank mass bounds normalized work directly

Apply the first-moment telescope to the **fully expanded** finite supplier,
not separately to its recursion nodes. Every mixed-unit instance at positive
integer column c contributes Delta*c. Every internal job match, including
compiler complement and exit substitution, cancels its exact equal rank.
Disjoint splitting and completion preserve mass. Productive boundary mass
is W*N; the only final paid jobs have rank one, with total mass P. Therefore

```
Delta*sum_all_completed_unit_instances(c) = W*N-P <= W*N.
```

Since c>=1 and Delta>=1, the total number of completed mixed-unit instances
divided by W is at most N. A unit's fresh scalar/phase/whole-job adapter
allowance is below K^2. Ordinary-base rank-one calls are already in P and are
not charged again as fresh scalar work. Compiler adapters are bounded by the
source/paid-edge budget per unit; in this model each final monomial is wiring
plus at most two real NEGs per coordinate. Hence

```
G/W <= K^2*N.
```

An explicit conservative adapter ledger is
`G<=(10^9+64)R* I_total+16P+16W`. Each nonbase compiler invocation contains
at least one mixed unit; its source/complement/exit adapter fields are bounded
by the fixed productive/paid role count times those unit instances. Adapters
at ordinary bases are bounded by their nonzero rank-one leaf count. Unit
centers and whole-child normalizers remain included. Since
`(10^9+64)R*+32<K^2`, P/W<N and I_total/W<=N, the displayed bound follows.

This bound includes the initialized/cleared owned centers. No per-array
input copy receives output credit. W and the full inventory can still be
enormous; neither is asserted small.

## 3. The exact Clifford endpoint lemma

The retained source closure specifies exact Clifford normal forms, independent
role arrays, and parent selected coordinate blocks with complete spectators.
See `FINITE-TEMPLATE-CLOSURE.md` section2 and the pinned compiler sections1,
3,4,6. The Gaussian kernel C1 with entries (1+i)/2 and (1-i)/2 is unitary
Clifford. Binary affine address permutations and its permitted exact phase
normal forms are Clifford. Here a diagonal quadratic Clifford phase has
linear terms modulo4 and **even cross terms** 2*x_i*x_j. An arbitrary phase
i^(x_i*x_j), controlled-S, would not justify this lemma. The source exact
Clifford normal-form contract, rather than the loose phrase quadratic phase,
is the premise used here; absolute phases are retained.

An exact generated Clifford on L selected binary axes has nonzero entries
2^(-h/2)*zeta8^t, with h<=L and t integral. The exactly recorded source
generators belong to the finite Clifford phase group (absolute phases are
powers of zeta8), and their complete matrix entries lie in Z[i,1/2]. Thus each entry
has Gaussian denominator exponent at most L+1. This follows also from h/t
parity: for even h only Gaussian-unit phases remain, and for odd h an odd
eighth-root phase pairs with sqrt2 to yield a Gaussian dyadic denominator.
Unitarity gives induced infinity norm at most 2^(L/2) by Cauchy–Schwarz.
Thus a completed Clifford segment adds at most L+1 grid bits and L magnitude
bits, regardless of how many completed calls it represents.

This is a **per-role** assertion. A whole-field role permutation preserves
that direct-sum structure. Complete native endpoints act independently by
the specified Clifford job on each productive role, and restore owned banks
to zero. They need not be unitary on arbitrary dirty owned inputs: the source
owned-bank precondition is retained, and dead zero banks are omitted at the
completed boundary. A suspended parent's nonzero owned center remains a live
productive field for its child, whose separate banks are initialized/cleared.

The parent selected-subspace invariant is essential. A rank-n job and its
all-column lift act on the parent's n*f selected axes and fix complete
external spectators. The allowed role permutations do not mix role-label
bits into address bits. Batching may repartition row views **inside** a child,
but its completed endpoint recombines them into the same parent C job before
the parent resumes. Stock axes are completed outside an already completed
active job. Thus segment closure is used only within one live context's
fixed whole-field partition; no arbitrary controlled role-dependent operation
on the whole FFT array is silently asserted Clifford.

## 4. Prefix decomposition along the suspended stack

At an arbitrary prefix, replace every completed native unit, complete child
program and complete sibling class by its exact endpoint. Consecutive such
endpoints in a fixed live context collapse into a per-role Clifford segment.
The only remaining fresh scalar instructions belong to prefixes of currently
suspended native units. Count ADD, SCALE, COPY, CLEAR and owned/role resets as
separators, including instructions with zero height. For one class, unit
copies run the same scalar word in lockstep on distinct fields, so their
height and scalar-layer budgets take a maximum rather than their total count.
Source paid-round barriers prevent inter-copy causal chaining.

There are at most (g+1)(J+1) live class contexts along a compiler chain. Each
has fresh scalar-layer and logarithmic height budget at most K^2. Entering a
child row partition or restoring a parent contributes at most two additional
segment boundaries per context, covered by the factor below. A prefix is
therefore a product with at most O(K^2(g+1)(J+1)) Clifford segments and fresh
scalar layers. Each segment lives on at most N*f parent-selected axes.
The exact endpoint lemma, scalar allowance and max-plus propagation give

```
prefix guard <= 16*K^2*(g+1)*(J+1)*N*f.
```

The constant16 also covers ordinary base prefixes (completed C axes plus one
currently executing elementary kernel), zero fields, segment endpoints and
the L+1 versus L distinction, since N*f>=1. Disjoint copies take a maximum.
In detail, if Cctx=(g+1)(J+1), fresh weighted separators are at most
S=K^2*Cctx. At most S+2Cctx+1<=2K^2*Cctx segments occur. Each contributes
at most2Nf grid bits; fresh scalar heights contribute at most K^2*Cctx.
Their sum is at most5K^2*Cctx*Nf. The factor16 exceeds this sum plus the
elementary/endpoint allowances. No unspecified exponential constant is used.

For ordinary supplier recursion at selected dimension d, only one child is
unfinished along a dependency path. The other child calls are replaced by
their exact completed Clifford endpoints. The selected dimensions down that
ordinary chain sum to at most2d because N>=2. Direct remainder/stock kernels
and the collapsed Hadamard conversion add only a fixed multiple of d. Hence
the following deliberately loose all-size semantic guard is valid:

```
Delta_native <= Cstack*d,
Cstack = 2^20*K^2*(g+1)*(J+1).
```

Set `Eguard=22+2k+bit_length(g+1)+bit_length(J+1)`. Then Cstack<2^Eguard.
This proof concerns exact fine-grid arithmetic, not rounding after every
completed call. It does not require materializing a dense Clifford matrix.

## 5. All-size work and row stock

Retain a=ceil(log2 W)<=9HN. The existing width proof implies
log2(a+1)<2H. The occupied recurrence is

```
c(e)<=(P/W)c(floor(e/N))+8G/W+40N.
```

Using G/W<=K^2N in the original weighted-tree proof and widening stored/native
operands to33p gives a safe active/Hadamard per-type coefficient
2^48*K^2*N^2. Row-stock cost80a is included, since K^2>9H. The small-selected-
dimension fallback uses

```
d0<=2^(Qstop(H+1)),
coefficient <=2^(12+Qstop(H+1)).
```

This retains the conservative bound 1-s<1; improving it is unnecessary here.
Padding still occurs only once and has factor below two. No W factor is
discarded from the genuine occupied work; it cancels only in G/W.

## 6. Closed interface majorant and all seven outer rows

Define the finite integer

```
Enew = Qstop(H+1)+2H+2k+Eguard+1729^12+179200000000+1000,
Bnew = 2^Enew.
```

It dominates the active and fallback runtime coefficients, Cstack, the
explicit HvH helper constant and the source prime-start gate. Bnew is an
interface majorant, **not** a total inventory or productive-width bound.
The explicit HvH helper's fixed logarithmic constant1729^12 is now the
largest term; this is disclosed rather than replaced by an empirical constant.

The same seven outer-row formulas, exponent gaps and protected q=32p,
w<=33p construction from `pr4470-nested-precision.py` apply with Bnew
replacing the prior interface majorant. All rows use only native runtime,
semantic guard, integer-helper and separately checked stock/conditioning
interfaces; none requires full W or D<=Bnew. Local Strassen block widths
remain the unchanged powers of p, unrelated to Bnew. The adjacent arithmetic
receipt explicitly lists every row and verifies its coefficient absorption.

For p>=Bnew^A, A=1400000001, the identical exact inequalities prove each row
below Bnew^-1*n*p^(1-kappa), and their sum below n*p^(1-kappa). Semantic
guard Bnew*p^-delta<=Bnew^-delta is below the same protected width allowance.
Ceilings are bounded by the smooth envelope log2 p+3; only that envelope is
asserted decreasing relative to the positive power gaps. Every original
prime, finite-section, boundary, normalization, bilinear and recovery check
retains its already proved numerical interface.

## 7. Sufficient whole-integer upper and interpretation

With p=256ceil(log2 n), the conditional sufficient eventual upper becomes

```
U_stack = 2^(2^(1400000001*Enew-8)) bits per operand.
```

Throughout the tail the weighted candidate cost is below
(1+rho)n p^(1-kappa). Its ratio to the repaired unbounded optimized-GMP
reference is below256*p^-kappa<1, and the canonical HvH comparison also
holds. The exact positive tariff rho is unrestricted. Baseline semantics,
including the repaired public constants/wide carry continuation, are retained.

The sufficient bound is substantially smaller than the already improved
replication-depth upper, without changing PR4470, its rank or its exponent.
It still is not a realistic hardware cutoff or a narrow interval locating
the first crossing. The literal raw word is not materialized, and the
native source contracts remain assumptions. Lower bounds for the literal
active-core enhancement family must retain that family scope; a chosen
fallback switch is not an intrinsic lower bound.
