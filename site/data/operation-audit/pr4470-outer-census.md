# PR4470: positive outer-circuit counts and the remaining closure interfaces

Source pin: `7c472563474e60185e6ca101a17622133d047e56`. Model: `xag-straightline-v1`, with free size-only constants, fanout, wiring and permutations. This note is a partial, construction-specific operation census. It does **not** give a complete PR4470 multiplier upper constant or a numerical eventual crossover.

## What this model removes

Fixed coordinate routes, tensor transpositions, q-image injection/extraction, CRT permutations, index matching, deterministic grouping/exposure, table synthesis, prime search and circuit generation are free. A fixed monomial's quadratic phase is known at every coordinate; it becomes a fixed real/imaginary swap and at most two real negations per complex coefficient. This does not make general linear transforms free. In particular, Gaussian matrix application, a Hadamard transform and a coefficient-times-data product still consume gates.

The template's BIT tape-routing algorithms need not be implemented merely to move fixed wires. The mathematical all-column endpoint identities, occupied batching, data arithmetic and semantic word bounds still must be respected. The original nine positive power savings are retained as source facts, but their tape-movement cost rows cannot automatically be treated as exact XAG operation counts.

## An explicit complex-word interface

The separately audited compiler inventory bounds the fixed expanded word by `M=K^(4^N)`, `log2 K<33010`, with `W,P,U_raw,R<=M`; see `pr4470-compiler-bound.md/.json`. Put `G=10^9 U_raw+8R`. The source semantic closure gives component width at most `2p` once its explicit precision recipe holds. A real ADD/SUB/NEG primitive then costs at most `8p` of either gate type. Thus the expanded word's nonrecursive arithmetic costs at most

    8 G p / W

per coefficient of a **fully occupied W-output batch**. This division by W is amortization, not permission to discount a partly occupied invocation. For `e=Nf+r`, `0<=r<N`, the r elementary remainder-axis kernels cost at most `40 N p` per coefficient (a normalized complex two-output butterfly uses two real sums and two real differences plus signed half rounding). The resulting candidate supplier interface is

    c_g(e) <= (P/W)c_g(floor(e/N)) + p(8G/W+40N),

for g=AND,XOR, after the source's full-batch and row-reservation conditions have been established. This is a useful numerically specified interface in fixed word counts; it is not yet the complete ordinary supplier bound. The source's normalized moment at the relaxed complex saving is below `2^-45868`, so the tree constant can be bounded sharply once the actual deferred-row schedule and its base regime are bound to this interface.

## Numeric local Toeplitz depth

The source `research/capped-phase-fusion/SHALLOW-TOEPLITZ.md` supplies actual dirty-shear, parity-split triangular and displacement-LU recursions. Its stated constants are asymptotic, but the following safe **round count**, independent of numerical coefficient magnitudes, follows from those recursions. A round here is disjoint invertible complex two-coordinate gates or diagonals; it is not a Boolean gate.

For a dyadic m-wire Toeplitz shear, the two circulant/negacyclic evaluations use forward FFT, a pointwise shear, inverse FFT and twists, hence at most `8(log2 m+1)` rounds (fixed permutations are free). The triangular parity recurrence uses two such shears and parallel children, so its depth is at most `16(log2 m+1)^2`. One bounded-generator term uses two triangular circuits and two dirty shears, hence at most `48(log2 m+1)^2` rounds. At depth j of the full LU recursion the displacement rank is at most `2+j`, and each shear has at most `2j+8` Stein generators. Two shears per LU level and the parallel children therefore give the conservative total

    D_local(B) <= 1024(log2 B+1)^4.

These are explicit depth ceilings for the source algebraic schedule. They do not bound the gate-coefficient heights or the error amplification.

In the present model, route each matching to adjacent pairs by free fixed wiring, tensor the source's common six-H gate word, and restore by wiring. The Beneš routing subnetwork is unnecessary. Hence an axis-circuit depth D needs at most **6D simultaneous H calls and 6D+1 diagonal stages** on the same data volume. This is the circuit-model specialization of `TENSOR-COMPILER.md`; the source's `(8m+2)D` bound pays its routing network. The six-H algebraic identities and bounded-precision qualifications remain necessary.

For R complex data coefficients and a supplied working width w that bounds every live input/output component and coefficient, a diagonal stage takes at most

    R [4 U_HvH(w) +100w]

of either Boolean gate type, by four signed integer products plus signs, real sums and rounding. Its coefficient is fixed and can be synthesized offline, but its multiplication by input-dependent data is charged. The new closed HvH envelope supplies `U_HvH(w)<=C w max(1,log2 w)` with C recorded in `hvh-operation-census.json`. Consequently a dense grouped stage has the positive counted interface

    6D * Supplier_g(h,R,w)
       +(6D+1) R[4Cw max(1,log2 w)+100w].

The exact number of dense stages, h, and R must still be taken from the chosen full Gaussian five-factor/group schedule, not from an unrelated old numeric example. The 6D+1 ceiling assumes adjacent diagonal stages are merged into one fixed coefficient before evaluation.

## A counted boundary arithmetic kernel

For a dyadic m=2^k square matrix product, canonical Strassen has `7^k` complex scalar products and exactly `6(7^k-4^k)` complex additions/subtractions, from its 18 block sums per node. One matrix may be fixed; retaining even its constant-only additions is a valid conservative upper. Padding a boundary block to the next power of two changes m by a factor below two. With a supplied sufficient working width w, each complex sum costs at most 16w gates per type, and each complex product at most `4Cw max(1,log2 w)+100w`. Thus an explicit per-type matrix-kernel upper is

    7^k[4Cw max(1,log2 w)+100w]
       +96w(7^k-4^k).

This is a complete arithmetic bound for this one matrix kernel. To obtain the whole Gaussian boundary bill one must count its invocations in the band-Schur solver, grouped couplings, and halo repairs, and prove the common sufficient w. Merely multiplying an O(W)-bandwidth by the record count is not enough: the source's latest exponent requires its batched fast-matrix implementation.

## A fully numeric prime-existence gate

The original outer prime supply uses Baker–Harman–Pintz with an unspecified eventual starting point. That particular unknown can be removed without changing the prime windows: Dudek's explicit theorem gives a prime in `(m^3,(m+1)^3)` for every integer `m>=exp(exp(33.3))`. The arXiv v1 proves the stronger 33.217; using 33.3 is conservative and agrees with the published article.

For an integer axis size x and integer d>=2, consider the desired window

    [(1-1/(2d))x, (1-1/(4d))x].

If

    x >= max(2^(2^54), 2^18 d^6),

it contains at least d distinct primes. Indeed, at x>=64 each consecutive cube gap below x is at most `4x^(2/3)`. At most two partially intersecting cube cells are lost, so the number of full cube cells in the window is at least `x^(1/3)/(16d)-2`. Since `x^(1/3)>=64d^2`, this is at least `4d-2>=d`. Their cube indices exceed Dudek's starting point: `log(2)>2/3` implies `exp(33.3)<2^50`, and `log2(x/2)/3>= (2^54-1)/3` is greater than `log2(exp(exp(33.3))+1)`. Each full cube interval supplies a different prime. The two original r/2 and r windows are disjoint, so primes for those groups are distinct too.

This is a source-supported mathematical replacement for the prime-existence estimate, not a bound on prime-search runtime. Search is outside our nonuniform arithmetic metric. It does not discharge other fine-prime denominator exclusions or analytic approximation conditions. Mapping this x gate to n requires the chosen outer t_i(n) definitions; it cannot be renamed an input-bit threshold.

## Exact remaining interfaces

1. **Numeric Gaussian word/error guard.** `phase_fusion_note.tex`, `SHALLOW-TOEPLITZ.md`, `CAPPED-INTERIORS.md`, and `LOG-A-PHASE-SCHUR-AUDIT.md` bound coefficients and prefix/suffix amplification by polynomials or `exp(O(g log^2 p)+O(g a B))`. Their proofs are constructive, but a numeric common w(p), rounding budget per stage, and an effective joint input range have not yet been extracted. Hardwiring their constants removes synthesis cost, not data precision or error amplification.
2. **Complete counted Gaussian/boundary schedule.** The five factors, capped blocks, broad/narrow operators, band Schur matrices, fast batched solves and halo repairs must be turned into exact loop ceilings feeding the counted H, diagonal and Strassen kernels. The historical uncapped `OUTER-AUDIT.md` explicitly labels itself a historical snapshot; it cannot supply the current near-critical PR4470 row multiplicities by substitution alone.
3. **Occupied batching and deferred-row base case.** The complex amortized recurrence above needs a numeric full-row reserve, one-time padding bound, shrinking-phase schedule and elementary-tail cutoff for the complete single integer invocation. This may be simpler than the original tape model, but dropping it would incorrectly turn W simultaneous outputs into a W-fold discount for one output.
4. **Outer exact-recovery/packing width and call counts.** Bind the preceding resampling error to the actual integer chunk scale, primes, polynomial product lengths, and final rounding. The original HvH recovery lemma cannot be transplanted unchanged after the dimension and normalization have changed.

Under the retained community assumptions there is a conditional exponent statement. The still-uninstantiated interfaces above prevent an independently verified numeric complete XAG upper constant and common start gate. They are narrower obligations than 'the exponent hides constants': several actual modules and one previously implicit prime gate have now been bounded explicitly. No finite whole-algorithm crossover is certified by this partial census.
