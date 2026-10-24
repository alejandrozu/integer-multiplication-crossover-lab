# Exact constant and carry semantics for the unbounded GMP reference

This is an explicit algorithmic extension of the pinned optimized GMP 6.3.0 source, with64-bit data limbs and unlimited public sizes. It is not a change to an installed library or a claim of native execution at unlimited sizes. The source file SHA-256 is `c1aa6ad5544be3694d50076c4937b30affdcd73c7c9d9b7cb11b5690cb3f5518`, from the official archive already bound by the source audit. The new extension identifier is `gmp-630-native-skylake-unbounded-exact-constants-v2`.

## A public integer is stored in a data limb

The original `mul_fft.c`, line866, contains

    T[2*l]=i+1; /* T=(i+1)*2^(2*M) */

Widening only sizes and indices does not make that single64-bit limb store exact when K=2^k exceeds2^64. The intended constant can require k+1bits. An index-only extension is therefore incomplete at the unlimited sizes used by the comparison.

Retain the source selector, recursive geometry and algorithm. Replace this store by the complete base-2^64 encoding of the **public** integer i+1 at limbs starting with T[2l]. Zero pad its full reserved constant field on every iteration, including any high digits left by the preceding iteration; keep all other T limbs zero. These are fixed constants in the arithmetic circuit model.

The source has M=64l and Nprime>2M+k+2, including the analogous formula in the recursive coefficient path. With nprime=Nprime/64,

    64(nprime-2l)>k+2.

Hence the k+1bits of i+1<=K fit entirely below limb nprime, and T[nprime]=0. The declared nprime+1-limb buffer already suffices. No FFT child width or selector change is necessary. The permutation-index arrays `fft_l` and their integer element types are also exact unbounded **public** indices.

## Preserve exact signed carry, retaining64-bit native kernels

Only the recomposition accumulator cc is given an explicit signed width

    w_cc=2k+128.

Implement it in64-bit chunks; this does not widen the native input limbs or their stipulated64-bit ADD/ADC instructions. Each of the K reconstruction iterations increments cc by one addition carry and subtracts two borrows. All three returned values are0or1. The loose bound `|cc|<=2K+2` at every elementary update fits this signed width. Interpret comparisons with-1,0,1 as exact signed integer comparisons, rather than a comparison against a truncated unsigned64-bit-1. A later assignment from `mpn_add_1` inserts its exact carry bit.

There is also a stronger endpoint check. `mpn_fft_div_2exp_modF` explicitly normalizes each coefficient, so its integer value V_j lies in `[0,B^nprime]`, where B=2^64. After complete iterations the represented true integer is

    X=sum_i [V_j-e_i(B^nprime+1)] B^(li),    e_i in{0,1}.

Let pla=l(K-1)+nprime+1. Since l>=1, nprime>=1 and B>=4, the geometric series gives

    |X| <[(B+1)/(B-1)] B^(pla-1) <B^pla.

Every add/borrow update preserves `X=R+cc B^pla`, with the physical pla-limb array R in `[0,B^pla)`. Thus cc is-1or0 after each completed iteration. This validates exact final sign conversion. The original defensive cc=1branch can be retained; its `while(add_1carry)` loop has at most two iterations, because the first carry1zeroes its entire target and adding1to that zero cannot carry again.

The geometric endpoint argument avoids assuming that K independent carries can accumulate unchecked in a64-bit word. The wider explicit accumulator gives a simple conservative implementation and an honest finite gate tariff.

## Additional work is charged

At most3K updates of a signed bit on w_cc bits cost at most `6K w_cc` AND and `12K w_cc` XOR using fixed ripple circuits. Three comparisons against constants cost at most `3w_cc` AND and `9w_cc` XOR. For an active modulus p>=400, k<=p and w_cc<=3p, so these totals are at most

    AND:18Kp+9p,    XOR:36Kp+27p.

This is polynomial local work and leaves the mandatory native butterfly additions and their previously proved lower bound intact. Child geometry, termination and the TABLE3 selector also remain unchanged. A global upper certificate must explicitly absorb this charge, not just cite the old index-only reference.

The adjacent reproducer hashes the exact source, tests k beyond64, checks multiword encoding/capacity and signed-carry bounds, and independently exercises the complete-prefix invariant at small radices with seeded data. Those checks support the displayed general written proof; they do not close the separate global helper-loop census or provide Lean verification.
