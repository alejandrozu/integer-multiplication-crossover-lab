# Counted portable GMP 6.3.0 multiplication kernel

This completes an explicit arithmetic circuit for one actual GMP kernel. It
does **not** complete the GMP dispatcher, a CPU instruction model, HvH, or the
PR4470 construction. In particular the resulting curve must be labelled
**“GMP portable basecase kernel: explicit circuit”**, not “GMP runtime” or
“fastest current multiplication”.

## Primary sources and configuration

The source is the [official GMP 6.3.0 archive](https://gmplib.org/download/gmp/gmp-6.3.0.tar.xz),
SHA-256 `a3c2b80201b89e68616f4ad30bc66aee4927c3ce50e33929ca819d5c43538898`.
The [source manifest](gmp-source-manifest.json) pins every extracted source file
by hash. The selected program consists of
[mul_basecase.c](gmp-sources/mpn/generic/mul_basecase.c),
[mul_1.c](gmp-sources/mpn/generic/mul_1.c),
[addmul_1.c](gmp-sources/mpn/generic/addmul_1.c), and the plain-C `umul_ppmm`
fallback in [longlong.h](gmp-sources/longlong.h) lines 2106–2131.

Use 64-bit limbs, `GMP_NAIL_BITS=0`, `NO_ASM`, no native multi-limb
multiply/addmultiply routines, and no native `umul_ppmm`. Assertions are
preconditions rather than executed diagnostics. Call the basecase routine
directly at every length. This is an allowed selected kernel in version 6.3.0;
ordinary GMP instead dispatches to other algorithms at larger sizes.

Inputs are nonnegative integers represented by two padded, little-endian limb
vectors of public lengths `m >= k >= 1`. The result has `m+k` limbs and does not
overlap either input. Zero and leading zero limbs are allowed. For an `n`-bit
input use `max(1,ceil(n/64))` limbs. Swapping two public vector lengths and
constant-zero padding are wiring choices in the circuit model. This gives a
uniformly generated circuit family for every finite input length; it does not
assert that a physical 64-bit-address GMP process can address arbitrary sizes.

## Exact source operation census

The first output row uses `mul_1` with `m` iterations. The other `k-1` rows use
`addmul_1`, also with `m` iterations. Thus:

| Operation outside the wide-product macro | Count |
|---|---:|
| 64 × 64 → 128 wide products | `mk` |
| 64-bit modular additions | `4mk-2m` |
| Unsigned 64-bit carry comparisons | `2mk-m` |
| Input/result-array loads | `2mk-m+k` |
| Output-array stores, including final row carries | `mk+k` |
| Inner pointer increments | `2mk` |
| Inner count decrements, comparisons, branches, each | `mk` |
| Outer pointer increments | `2k` |
| Outer count decrements, comparisons, branches, each | `k` |
| Address additions for the final carry store | `k` |
| Row calls and returns, each | `k` |

Within each portable wide product there are four 32 × 32 → 64 products, four
unconditional 64-bit additions, one unsigned 64-bit comparison, five fixed
shifts and three masks. A fifth addition executes if the macro's carry branch
is taken. Let `beta` count its taken branches over the `mk` products. Then
`0 <= beta <= mk`, and the fully expanded arithmetic census is

```
half-products = 4mk
64-bit additions = 8mk - 2m + beta
64-bit comparisons = 3mk - m
fixed shifts = 5mk
masks = 3mk
```

This is an exact census of the listed source operations. It deliberately does
not call a source expression a CPU instruction. Register assignment, parameter
passing, compiler scheduling, ABI prologues, allocation, caches, and memory
latencies require another tariff and implementation. The script records actual
`beta` on each evaluated input, separately from the fixed circuit below.

## Complete binary circuit and its cost

Use binary AND gates at cost 1 and binary XOR gates at cost `rho > 0`. A NOT
is XOR with constant 1. Wires, fanout, constants, fixed shifts and masks cost
zero. No constant folding or other gate simplification is applied. A gate's
output write is part of that gate. There is no separate CPU memory charge in
this model.

The gate evaluator fixes every implementation choice:

1. A width-`W` modular addition uses `W` ripple full-adder cells, including the
   unused final carry. Each cell has 2 AND and 3 XOR gates. The two carry terms
   cannot both be 1, so XOR correctly combines them.
2. A width-`W` unsigned comparison runs the carry-only ripple for
   `a + NOT(b) + 1`, then negates its final carry to obtain `a < b`. Its cost is
   `2W` AND and `3W+1` XOR gates.
3. A `q × q` full product forms `q^2` partial-bit ANDs. Its first partial row is
   wired directly; the remaining `q-1` rows each use a width-`2q` ripple add.
   Therefore its cost is `5q^2-4q` AND and `6q^2-6q` XOR gates.
4. The portable `umul_ppmm` macro uses four such `q=32` products. The carry
   branch becomes the equivalent unconditional addition `x3 + (c << 32)`.
   This charges five width-64 additions and one width-64 comparison on every
   input. Shifts and masks are wires. The macro therefore has exactly
   **20,736 AND and 24,961 XOR gates** in this implementation.

The complete basecase circuit consequently has

```
AND(m,k) = 21,504 mk - 384 m
XOR(m,k) = 26,115 mk - 577 m
work(m,k,rho) = AND(m,k) + rho * XOR(m,k).
```

For equal `n`-bit operands, substitute `m=k=max(1,ceil(n/64))`. For example,
256-bit operands require 342,528 AND and 415,532 XOR gates in this particular
unoptimized circuit. These are exact positive integer counts, rather than
unknown asymptotic constants or a wall-clock extrapolation.

## Correctness and verification

For the first row, the usual `mul_1` invariant says the already stored limbs
and the carry together equal the product of the processed prefix of `up` with
the current multiplier limb. Each subsequent `addmul_1` row adds
`up * vp[j] * 2^(64j)` to the accumulated result. The returned carry occupies
the next untouched output limb. Induction on the row number gives
`value(rp) = value(up) * value(vp)`.

The portable macro computes its four half-products and propagates their middle
sum carry into the upper half. Replacing its conditional increment with
`c << 32` preserves the result for both possible carry bits. The ripple
addition/comparison circuits implement exactly the corresponding unsigned
operations, and the partial-row multiplier sums the defining binary product.
These facts prove correctness for all public lengths; tests additionally check
the transcription and counting formulas.

Running `gmp_operation_model.py` passed:

- 272 exhaustive one-limb Boolean-gate evaluations at toy limb widths 2 and 4;
- 576 rectangular source-census/product checks, including zero and all-one
  vectors, at widths 2, 4, 8 and 64;
- 8 complete 64-bit-limb gate evaluations, including multi-row `addmul_1`.

`gmp-operation-model.json` contains the machine-readable formulas, eight sample
input sizes, the primitive tariff, source configuration and verification
results. `python gmp_operation_model.py --m 10 --k 7` returns the exact census
and circuit gate counts for another public size without materializing its
gate list.

## Boundary of the result and next source entry points

The plain generic equal-size dispatcher is `mpn/generic/mul_n.c`. With the
unoverridden defaults in `gmp-impl.h`, it selects basecase below 30 limbs,
Toom-2.2 below 100, Toom-3.3 below 300, Toom-4.4 below 350, Toom-6.5 below 450,
Toom-8.5 below 3000, then FFT. Target-specific parameter headers replace these
thresholds in normal builds. These thresholds describe dispatch choices; they
are not crossovers against PR4470 or a latency law.

The next exact source to cost is `mpn/generic/toom22_mul.c`. Even its balanced
path additionally needs `mpn_cmp`, `mpn_sub_n`, `mpn_add_n`, `mpn_add`,
`MPN_INCR_U` and its early-exit/zero-fill carry case. Odd and unbalanced sizes
also require `mpn_zero_p`, `mpn_sub` and potentially `mpn_toom32_mul`. The saved
source and `gmp-impl.h` expose these dependencies. No GMP-inspired replacement
Karatsuba routine is substituted for them in this report.

This work finishes one positive, numerically costed baseline component. It
does not certify a PR4470-versus-full-GMP or PR4470-versus-HvH crossover.
PR4470 still needs a complete comparable circuit/runtime construction and a
joint input-validity threshold. A model slider must retain that unknown state.

## Reproduction and licensing

`gmp_extract_sources.py` extracts only the audited sources from the pinned
archive and emits per-file SHA-256 hashes. `gmp_operation_model.py` regenerates
the results and executes the checks. No GMP installation or compilation was
needed. Upstream notices remain in all extracted files. The transcription and
its source-derived decomposition are offered under the same LGPLv3-or-later
or GPLv2-or-later options; the applicable upstream license texts are retained
under `gmp-sources/`.
