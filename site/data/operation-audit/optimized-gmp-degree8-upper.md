# Degree-eight upper on the same optimized GMP source continuation

This module tightens the existing source upper without changing the optimized
Skylake selector, its unbounded TABLE3 continuation, the exact multiword
constant/signed-carry repair, the native instruction lowering, or any finite
GMP entry point. It retains all four data-dependent high-carry length variants.
It is a conditional source-circuit bound, not a measured runtime estimate.

The frozen `optimized-gmp-upper-recurrence.md/.json` supplies the source
geometry, helper-loop census, complete source hashes, and finite compilation
contracts. In particular, for an active FFT of modulus p:

* `K*(np+1)<16p` and `np+1<=(p+1)/2`;
* nonrecursive work in either gate type is at most
  `D(p)=2^65536*(p+1)^8`;
* the number of local finite-leaf positions is at most
  `2^128*(p+1)^4`;
* a finite native leaf at the **unchanged cutoff 2^20 limbs** costs strictly
  less than `B=2^(2^71)` gates per type under the stated finite native
  halting/allocation and transition-circuit contract. This is the sharper
  intermediate bound in that proof, before its convenient allowance
  `L=2^(2^72)` was chosen.

The finite cutoff is not raised. No assumption about executing a larger
finite native operand on the actual machine is added.
The normalized modular representation includes its additional carry limb:
a modulus at the cutoff can use `2^20+1` data limbs. The same original
finite 64-bit state bound covers that guard limb; the cutoff refers to
the modulus/recursion size, not an assertion that every array has exactly
that many limbs.

## Simultaneous induction

Use the same meanings of F (full product, maximum input length m limbs) and
T (active plus-modulus FFT, modulus p limbs). Prove

    T(p) <= L*(p+1)^8,
    F(m) <= 8*L*(m+1)^8,
    L = 2^(2^72).

The sum of the K active coefficient-child potentials is at most
`16/2^7=1/8` of the parent's degree-eight potential. This retains every
coefficient product, rather than counting only the largest one.
Active coefficient products recurse directly through
`mpn_mul_fft_internal`, so their induction coefficient is L, not 8L;
non-FFT coefficients are finite leaves. This is the branch at
`mul_fft.c` lines 474–550 of the pinned source.

For a full product, the sum of the active FFT root potentials along the CRT
minus spine is less than

    [(9/8)*(1+1/2^20)]^8 / (1-2^-8) < 3.

There are at most six large non-FFT full-product restart calls. Charge all
four input-length variants, hence 24 children. Each child is at most
`9(m+1)/16`. Their cost under the induction is less than

    8*24*(9/16)^8 * L*(m+1)^8 < 2*L*(m+1)^8.

The unbalanced FFT-blocking branch has child-length mass at most `3(m+1)`
and maximum child length `(m+1)/2`. Including all four variants, its
degree-eight child potential is at most `12/2^7`; its F-cost is therefore
at most `3/4` of `L*(m+1)^8`. The bounded-size non-FFT chunks remain finite
leaves, exactly as in the frozen proof.

The important finite-leaf slack must be retained. Charging a finite leaf at
B, rather than already at L, gives the normalized local leaf charge

    B*2^128*(x+1)^4 / [L*(x+1)^8]
      <= 2^(2^71+128-2^72) < 1/4.

Likewise `D(x)/[L*(x+1)^8]=2^(65536-2^72)<1/4`.
Consequently the normalized T budget is below `1/8+1/4+1/4<1`;
the ordinary F budget is below `3+2+1/4+1/4<8`; and the blocking F budget
is below `3/4+1/4+1/4<8`. The finite starting cases are already below B<L.
This proves the simultaneous induction under exactly the existing native
compilation and source-correctness contracts.

For n-bit operands, m<=n, hence each gate count of the retained optimized
source circuit is at most

    8*2^(2^72)*(n+1)^8 = 2^(2^72+3)*(n+1)^8.

The looser coefficient `2^(2^73)` may also be used. The exponent 16 in the
previous bound was an avoidable proof allowance, not a source requirement.
The huge finite native coefficient remains a coarse state-compilation bound;
this result does not claim a practical GMP implementation census.

## Consequence for a literal dense p16 supplier

Suppose the separately authenticated literal construction has local rank
`N=2^H` and compulsory per-type work `AND>=c*2^N`, `XOR>=3c*2^N` when
active. Let `j=floor(log2(c))` and let

    q = floor((j-3)/8),
    E = 2^(H-3) - 2^69 + q.

For integer input lengths `n<=2^E-1`, one has `n+1<=2^E`. The logarithm of
the GMP upper is therefore at most `2^72+3+8E=N+8q+3<=N+j`. The candidate's
AND lower is at least this common per-type upper, and its XOR lower is at
least three times as large. Thus the active literal candidate is strictly
more costly for every positive XOR/AND price ratio. No such input length
can be a winning one. The resulting first-possible-size lower bound is
`2^E`, without claiming that a crossing occurs there.

For the authenticated p16 powers, q equals 2045 (v=1024), 1362 (v=682), and
2 (v=1). This is a necessary-work exclusion for the declared unreduced
literal supplier family. It is not a necessary activation threshold for all
possible implementations of the PR's mathematics. No sufficient input cutoff
or exact first crossing is changed by this module.

`optimized_gmp_degree8_upper.py` verifies the exact budget inequalities,
source/certificate hashes, raw coefficient bit lengths, and compressed lower
endpoint arithmetic without forming any astronomical integer.

Status: AI-assisted written proof and exact rational/source-byte checks;
not Lean verification or independent human review.
