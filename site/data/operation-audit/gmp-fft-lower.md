# A lower envelope for the full generic GMP FFT-dispatch circuit

For one precisely pinned generic GMP 6.3.0 source expansion, this note proves

```
AND(n) > n log2(n)
XOR(n) > (3/2)n log2(n)                    for integer n >= 2^26 bits.
```

It also proves the stronger, profile-specific bounds

```
AND(n) > 4n^(11/10)
XOR(n) > 6n^(11/10)                       for integer n >= 2^26 bits.
```

At the common tariff these give lower bounds
`(1+(3/2)rho)n log2(n)` and `(4+6rho)n^(11/10)`. They are lower bounds on
**one full multiplication circuit derived from the generic source**, rather
than on all GMP builds, all circuits, machine time, or the multiplication problem.
An upper bound for another whole multiplier below one of these lower bounds
would establish superiority to this specific circuit. No PR4470 crossover is
established by this note alone.

## Pin the program before counting

Use the [official GMP 6.3.0 source archive](https://gmplib.org/download/gmp/gmp-6.3.0.tar.xz),
SHA-256 `a3c2b80201b89e68616f4ad30bc66aee4927c3ce50e33929ca819d5c43538898`.
The [source manifest](gmp-fft-source-manifest.json) pins the extracted files.

The profile is 64-bit limbs, no nails, generic C kernels, no native assembly
replacements or combined native add/sub kernel, no `WANT_ADDSUB`, no tuning
build, and no FFT `TABLE3`. Use the unoverridden generic defaults:

```
MUL_FFT_THRESHOLD = 3000 limbs
MUL_FFT_MODF_THRESHOLD = 300 limbs
MULMOD_BNM1_THRESHOLD = 16 limbs
FFT_FIRST_K = 4
MUL_FFT_TABLE = {400,800,1600,3200,9600,28800,0}.
```

The source's legacy `best_k` has `4 <= k <= 11` for every positive public size,
and returns 11 for sizes at least 115200 limbs. This finite fallback table's
unbounded extension is deliberately part of the selected reference program.
It explains the polynomial lower bound; that bound must not be transferred to
an optimized target-specific parameter table or hardware GMP binary.

Inputs are two distinct-address, public equal-length arrays of
`m=ceil(n/64)` limbs; their values may coincide. The whole product is computed
by `mpn_mul_n`; high padding bits can be omitted by output wiring. Public index
and size arithmetic is idealized as exact and unbounded. Otherwise a literal
finite-address machine would have no arbitrarily large input domain. Public
size calculations, circuit generation, constants, fanout and fixed routing are
free in `xag-straightline-v1`.

Each source `sl = ul + vl` in generic `mpn_add_n` is expanded into **64
unsimplified full-adder cells**, including the first cell and unused final
carry. It has exactly 128 AND and 192 XOR gates. There is no constant folding,
CSE, dead-gate removal, replacement by a hardware instruction, or substitution
of a cheaper adder. Other operations use ordinary correct bit circuits;
input-dependent branches can compute both branches and select, with loops
unrolled to their public bounds. Their nonnegative gate costs are unnecessary
for the lower bound. Thus this is a particular source circuit, not a
compiler-independent statement about generic C.

## The actual full-product path

The important entrypoint is not the obsolete `mpn_mul_fft_full`:

1. [mul_n.c](gmp-fft-sources/mpn/generic/mul_n.c) selects `mpn_fft_mul` for
   `m >= 3000`.
2. [gmp-impl.h](gmp-fft-sources/gmp-impl.h), lines 5305–5308, sets
   `mpn_fft_mul = mpn_nussbaumer_mul`; the old-full-FFT alias is in `#if 0`.
3. [nussbaumer_mul.c](gmp-fft-sources/mpn/generic/nussbaumer_mul.c) calls
   `mpn_mulmod_bnm1` with `rn=next_size(2m)` for distinct input addresses.
4. [mulmod_bnm1.c](gmp-fft-sources/mpn/generic/mulmod_bnm1.c) uses CRT with
   one minus and one plus product. For this range,
   `rn=2R`, where `R=fft_next_size(m,best_k(m)) >= m` and `R<m+2048`.
   Its plus product calls `mpn_mul_fft` at `pl=R`. It starts with
   `k=best_k(R)` and decreases `k` only until `2^k` divides `R`.
   Since `R` is a multiple of at least 16, the resulting `k` is at least 4.
   Also `R<2m`, so the required public size preconditions hold.

All further work in the minus product, CRT reconstruction and other stages is
additional. We need only the full FFT subtree rooted at this plus product.

## An FFT node's compulsory additions

For a node in [mul_fft.c](gmp-fft-sources/mpn/generic/mul_fft.c), let `pl` be
its modulus size in limbs, `N=64pl`, `K=2^k`, and `M=N/K`. The source sets

```
maxLK = max(64,K)
Nprime = maxLK * (1 + floor((2M+k+2)/maxLK))
nprime = Nprime/64.
```

If `nprime >= 300`, the source rounds it upward until it is divisible by
`2^best_k(nprime)`. This only increases its size. Therefore

```
Nprime >= 2N/K,
K*Nprime >= 2N,
Nprime >= N/1024.                 [K <= 2048]
```

The non-square internal routine executes two forward FFTs and one inverse
FFT. Their input arrays remain distinct through every recursive pointwise
product, so none of these transforms disappears through a square shortcut.

An FFT on `K=2^k` entries has exactly `Kk/2` butterflies: its count satisfies
`b(2)=1` and `b(K)=2b(K/2)+K/2`. For `K=2` each butterfly unconditionally calls
`mpn_add_n` on `nprime+1` limbs. Higher butterflies call `mpn_fft_add_modF`,
which unconditionally calls `mpn_add_n` on `nprime` limbs. In either case the
low `nprime` limb iterations execute their initial `sl=ul+vl`.

Counting just those first additions across the three transforms gives

```
AND_node >= 3*(Kk/2)*nprime*128 = 3KkNprime >= 6kN >= 24N
XOR_node >= 3*(Kk/2)*nprime*192 = (9/2)KkNprime >= 9kN >= 36N.
```

This omits subtraction, carry comparisons, the second limb addition, modular
correction, twiddle rotations, decomposition, all multiplication leaves and
every other stage. The omitted work cannot invalidate a lower bound on this
unsimplified circuit.

## Count the recursive levels

If `nprime >= 300`, `mpn_fft_mul_modF_K` recursively performs all `K`
pointwise products through the same FFT core. The children have bit size
`Nprime`. Their total bit mass is at least `2N`; each has at least `N/1024`
bits. These bounds hold for every subsequent FFT node.

Write

```
D = floor(log_1024(pl/300)).
```

For levels `j=0,...,D`, every node has at least 300 limbs, so all these levels
execute the FFT core. Their total bit mass is at least `2^j N`. Consequently

```
AND_subtree >= 24N * (2^(D+1)-1)
XOR_subtree >= 36N * (2^(D+1)-1).
```

For the weaker logarithmic envelope, discard this mass growth and keep
`D+1` copies of the root mass. Put `ell=log2(pl)`. If `pl >= 2^20`, then

```
D+1 > (ell-log2(300))/10
    > (ell-9)/10
    > (ell+6)/24 = log2(N)/24.
```

The last strict inequality follows from `14ell>276`, true for `ell>=20`.
Thus the subtree costs more than `N log2(N)` AND and
`(3/2)N log2(N)` XOR gates. For original input size `n >= 2^26`,
`m>=2^20`, `pl=R>=m`, and `N=64R>=n`. Monotonicity proves the stated
whole-product logarithmic lower bound.

For the stronger envelope put `x=(pl/300)^(1/10)`. Here `x>2`, and
`2^(D+1)>x`; hence `2^(D+1)-1>x/2`. The mass-growth sums imply

```
AND_subtree > 12N * (N/19200)^(1/10)
XOR_subtree > 18N * (N/19200)^(1/10).
```

Since `3^10=59049>19200`, these exceed `4N^(11/10)` and `6N^(11/10)`,
respectively. Again use `N>=n`.

## Termination and verification

No change of the source's integer-size semantics may silently introduce
nontermination. The initial child satisfies `nprime <=2pl/K+33`. At each
alignment round `best_k` either increases or the next test stops. The total
possible increase is below `16+32+...+2048=4080`. Thus for `pl>=8192`,

```
nprime <= pl/8+4113 < pl.
```

The remaining public range `300<=pl<8192`, for all divisible `K=2^k` with
`4<=k<=11`, is checked exhaustively by the reproduction script. The finite
table and monotone rounding prove that all larger and smaller eligible
recursive nodes terminate. Input-dependent normalization does not change
these public sizes.

[gmp_fft_lower.py](gmp_fft_lower.py) checks 978 small parameter cases, 147001
full-dispatch input limb sizes, all eleven butterfly recurrences, FFT-table
boundaries, and arbitrary-precision examples. It also emits exact mandatory
addition-subtree lower counts at several finite sizes. The inequalities are
proved above; the checks catch transcription and arithmetic errors. This is
a new manual source-counting argument with executable checks, not a Lean
formalization or an execution of a complete generated GMP circuit.

The [machine-readable certificate](gmp-fft-lower.json) retains the profile,
thresholds, hashes, formulas, examples and scope restrictions. The original
source licenses apply to the saved GMP sources; license texts are included in
the companion `gmp-sources` directory. The counting script and source-derived
decomposition use the same LGPLv3-or-later or GPLv2-or-later options.
