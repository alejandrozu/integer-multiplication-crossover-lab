# Optimized GMP with explicitly unbounded public indices

This audit defines a native optimized GMP source circuit that can be compared at astronomical input sizes. It deliberately removes API, address-space and allocation ceilings. It does not extrapolate the finite machine benchmark, and it does not claim that an existing DLL executes unbounded indices.

The source is the [official GMP 6.3.0 archive](https://gmplib.org/download/gmp/gmp-6.3.0.tar.xz), SHA-256 `a3c2b80201b89e68616f4ad30bc66aee4927c3ce50e33929ca819d5c43538898`. The machine-readable `audit.json` pins the extracted files and all parameter tables. GMP 6.3.0 remains the [official current stable release](https://gmplib.org/). The manual describes [native and fat build selection](https://gmplib.org/manual/Build-Options), the [Fermat FFT algorithm and its size-dependent split parameter](https://gmplib.org/manual/FFT-Multiplication), and the [limb-array interfaces](https://gmplib.org/manual/Low_002dlevel-Functions).

## Main optimized profile

The primary reference is the source profile selected for **Tiger Lake**, rather than the older fat DLL's default fallback. In `configure.ac`, Tiger Lake joins Ice Lake and Rocket Lake, selecting the search path

```
x86_64/icelake x86_64/skylake x86_64/coreibwl x86_64/coreihwl
x86_64/coreisbr x86_64/coreinhm x86_64/core2 x86_64
```

The archive contains no files in `mpn/x86_64/icelake/`. Consequently the first existing machine parameter header is `mpn/x86_64/skylake/gmp-mparam.h`. This is source selection through the configured path, not an invented Ice Lake header. The relevant fixed thresholds are:

| Profile | Full multiplication FFT | Modular FFT | `mulmod_bnm1` | Multiply TABLE3 entries |
|---|---:|---:|---:|---:|
| Tiger Lake native, effective Skylake header | 6,272 limbs | 404 limbs | 15 limbs | 227 |
| Additional Broadwell native reference | 5,760 limbs | 460 limbs | 16 limbs | 219 |

Both native profiles retain all original tuned TABLE3 entries. Their final eight entries are `(2^(k−1), k)` for `k=17,...,24`. We **append the same rule for every integer `k>=25`**. The existing table is unchanged wherever its lookup returns a value. This supplies one precise algorithmic unlimited-index extension; no table-exhaustion limit is used as an objection.

The actual lookup compares `n <= tab_n * 2^last_k`, where `last_k` is the previous row's `k`. Therefore throughout the regular tail, including endpoints,

```
best_k(n) = ceil(log2(n)/2)     for n > 2^32 limbs.
```

For integers this is exactly `((n−1).bit_length()+1)//2`; no floating-point logarithm is required. In particular the continuation does not freeze the split parameter at 11. The audit checks every original table transition on both sides and all regular-tail power-of-two transitions through 2,048-bit logarithmic indices.

## Native addition remains charged

The first `aors_n.asm` on the Tiger Lake search path is `mpn/x86_64/coreihwl/aors_n.asm`. Neither the absent Ice Lake directory, Skylake nor Broadwell supplies a preceding version. Its `OPERATION_add_n` specialization defines `ADCSBB` as `adc`. The routine has eight residue handlers and an eight-limb loop: quotient/remainder scheduling covers every input limb exactly once with a 64-bit carry addition. This changes scheduling and instruction throughput, not the existence of the additions.

There is no native `add_n_sub_n` implementation anywhere in the archive's x86-64 source paths. In the pinned default profile `HAVE_NATIVE_mpn_add_n_sub_n=0` and `WANT_ADDSUB` is undefined. The public exported generic C helper is not evidence for a native replacement. Thus `mul_fft.c` uses the separate `mpn_add_n`/`mpn_sub_n` butterfly branch. Its `K=2` base case calls `add_n` on `nprime+1` limbs; every higher butterfly calls it on `nprime` limbs, unconditionally.

For an auditable circuit definition, retain 64-bit data words and carry flags. Lower each 64-bit data `ADD` or `ADC` to 64 full-adder cells, including the first carry input and final carry output. Each cell uses 2 AND and 3 XOR gates, so this instruction circuit contains **128 AND and 192 XOR**. There is no cross-instruction CSE, constant folding or dead-gate pruning. Public sizes, index arithmetic, unrolling, fixed routing, constants and fanout are free, as in `xag-straightline-v1`. Data-dependent operations and branches receive correct Boolean circuits, and their nonnegative costs cannot reduce a lower bound obtained from the mandatory additions.

This is a concrete optimized-source circuit family. It is not a statement that hardware ADD takes 128 CPU operations or that all equivalent Boolean adders require this count. Even the much weaker retained count of one AND and one XOR per word addition is available for comparisons that prefer a deliberately small coefficient.

## Interface to the whole multiplication lower bound

The full product path is

```
mpn_mul_n -> mpn_nussbaumer_mul -> mpn_mulmod_bnm1
                                      -> CRT plus product -> mpn_mul_fft.
```

For a modular FFT node put `N=64pl`, `K=2^k`, and let `nprime` be the child modulus in limbs. The unchanged source geometry gives `K*nprime >= 2pl`. A non-square product executes two forward FFTs and one inverse FFT, each with `K*k/2` butterflies. Therefore it contains at least

```
3*(K*k/2)*nprime >= 3*k*pl
```

mandatory native word additions, before counting subtractions, corrections, twiddles, pointwise multiplication or descendants. With the stated instruction lowering this gives

```
AND_node >= 6*k*N
XOR_node >= 9*k*N.
```

The unbounded tail has `k` proportional to `log2(pl)`, so the root alone supports a logarithmic lower envelope; a fixed-`k=11` recursive-tree argument is unnecessary for this primary reference. The independent `pr4470-optimized-gmp` comparison certificate supplies the full-root size inequalities and resulting integer-input constants.

The new infinite tail also preserves termination. For every `pl>2^46`, the selected or full-root-aligned split satisfies `sqrt(pl)/2 <= K < 2sqrt(pl)`, giving an initial child smaller than `5sqrt(pl)` limbs. When that child exceeds `2^32`, rounding within a regular-tail interval `(4^(j−1),4^j]` cannot pass `4^j`, which is itself divisible by `2^j`; alignment is stable after one rounding and adds less than twice the square root of the initial child. When the initial child is at most `2^32`, the exact pinned table has `best_k<=17`, verified interval by interval. Any continuing rounding must strictly increase `k`: a rounded multiple for an equal or smaller `k` already satisfies the divisibility test. Thus the total increment is less than `sum_{j=0}^{17}2^j<2^18`, including a possible crossing just above `2^32`. Since `sqrt(pl)>2^23`, either case gives a final child smaller than `6sqrt(pl)<pl`. For `pl<=2^46` the table is unchanged; these original bounded native GMP regimes retain the standard library algorithm's correctness/termination. This audit does not formally verify their complete implementation. The explicit added tail is covered in full.

## The measured wheel is a separate receipt

The benchmarked Windows DLL is SHA-256 `525f5681dc5fb40ef86b1bcb0ee5c40142aec689e0a1ba8c8e40199173366f6a`. Reading its unstripped PE/COFF `mpn_fft_table` data directly gives the legacy multiply table

```
{464,928,1920,3584,10240,40960,0}
```

and the exported `fft_best_k` matches the table at every boundary, reaching 11 from 163,840 limbs. Disassembly of the actual DLL's forward and inverse FFTs calls CPU-vector offset 0 (`add_n`) and offset `0x110` (`sub_n`), confirming the separate butterfly route. The compatible Broadwell benchmark override only changes kernel pointers and five Toom thresholds; it does not install TABLE3. These binary facts are preserved separately and are not substituted for the main native-profile extension.

`audit.py` reproduces source extraction, profile resolution, complete tables, tail checks, the actual DLL table bytes and exported selector calls when the original archive and DLL are available. `python audit.py --offline` uses the packaged pinned sources, archive-member inventory and saved selector receipt without those external binaries. `audit-run.json` explicitly says whether archive reopening and DLL execution occurred during that run; offline validation does not claim to rerun historical DLL calls. `audit.json` has stable mathematical/source bindings in either mode. `dll-instruction-audit.json` retains the decoded binary instruction evidence. This is a manual source proof with executable checks, not a Lean formalization, a generated whole-circuit execution, a CPU-time bound or a universal lower bound for every possible GMP implementation.
