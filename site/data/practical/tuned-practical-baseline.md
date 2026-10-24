# The installed GMP baseline, measured directly

The actual installed backend is GMP 6.3.0 in the gmpy2 2.3.2 Windows x64 wheel, running on an Intel Core i7-1185G7 (Tiger Lake, CPUID family 6/model 140). It has 64-bit limbs and a fat binary containing multiple assembly implementations. Its actual initialized CPU vector nevertheless selects generic `x86_64` assembly kernels with Toom thresholds 20 and 130 limbs. This is consistent with the official GMP 6.3.0 `fat.c` CPU switch lacking Tiger Lake model `0x8c`. Generic x86-64 assembly is distinct from the old proof reference's `--disable-assembly` generic C build.

We also measured an explicitly declared, process-local **compatible Broadwell profile**: exported core2/Nehalem/Sandy Bridge/Haswell/Broadwell kernels are selected in that order, and the five dynamic thresholds use the official Broadwell header (26/73/34/117/22). CPUID confirms AVX2, BMI2 and ADX. This is an experimental override, not an upstream Tiger Lake build, an optimal tuning result, or a change to the installed DLL. The original CPU vector and affinity are restored at exit.

The direct native `mpz_mul` measurement reuses a preinitialized output. A second measurement calls `mpn_mul_n` with preallocated output limbs. Native Windows x64 batch loops eliminate a Python or ctypes transition for every multiplication; their argument passing and exact call counts are independently tested. GMP internal scratch allocations remain included. A third series retains the ordinary allocating Python `a*b` interface for comparison. Inputs, conversion, expected products and checks are outside the timers.

There are 13 input sizes from 256 through 16,777,216 bits per operand, three seeded independent positive operand pairs per size, and seven shuffled rounds (21 samples per profile/method/size; 1,638 raw samples total). Each timed batch's full final result is checked against Python's independent integer multiplication. Operands are distinct, not squarings. Batches repeat hot inputs; sizes, profiles, methods and pairs are shuffled between batches. The process is pinned to one available logical processor, with default priority. Clock frequency, thermals and background work are uncontrolled. IQRs describe this run; they are not confidence or guaranteed latency bounds.

Representative native `mpz_mul` medians are:

| Bits per operand | Actual default | Compatible profile |
|---:|---:|---:|
| 1,024 | 0.231 microseconds | 0.157 microseconds |
| 4,096 | 2.143 microseconds | 1.458 microseconds |
| 65,536 | 134.723 microseconds | 96.950 microseconds |
| 262,144 | 0.781 milliseconds | 0.661 milliseconds |
| 1,048,576 | 3.979 milliseconds | 3.158 milliseconds |
| 4,194,304 | 20.950 milliseconds | 15.464 milliseconds |
| 16,777,216 | 111.078 milliseconds | 90.155 milliseconds |

The complete JSON and CSV retain every measured size. No fit or extrapolation is used, and no internal algorithm transition is inferred from size or timing. GMP's practical multiplication dispatch includes basecase, Karatsuba, Toom variants and a Fermat FFT following Schönhage–Strassen; this is not a measured Harvey–van der Hoeven implementation. The official manual explains both [CPU-dependent fat dispatch](https://gmplib.org/manual/Build-Options) and [FFT threshold/padding effects](https://gmplib.org/manual/FFT-Multiplication). The [low-level API contract](https://gmplib.org/manual/Low_002dlevel-Functions) specifies the non-overlapping `2n`-limb result required for `mpn_mul_n`.

The DLL SHA-256 remains `525f5681dc5fb40ef86b1bcb0ee5c40142aec689e0a1ba8c8e40199173366f6a`. Its embedded compiler string says GCC 16.2.0/MSYS2 Rev4. Complete compiler flags and a full wheel build manifest are unavailable, so that string is not treated as complete build provenance. The official current stable release is [GMP 6.3.0](https://gmplib.org/), released July 30, 2023.

## The finite ABI limit

The official `gmp-h.in` defines `_mp_alloc` and `_mp_size` as `int`. Actual-DLL imports of 1-, 65- and 1,024-bit values confirm the 16-byte structure layout: two 32-bit integers at offsets 0/4 and a 64-bit pointer at offset 8. Consequently a positive `mpz` value cannot represent more than `64(2^31−1) = 137,438,953,408` bits in this installation. That is a necessary representation ceiling, not a guarantee that every value up to it can be allocated or safely processed. A full product must also fit. Equal-bit-length positive operands therefore have a necessary output-size ceiling of 68,719,476,704 bits each. Here `mp_size_t` is Windows `long`, also 32 bits; the `mpn` interface is not an unlimited-size escape hatch.

This ceiling is installation/ABI-specific, not a universal mathematical limitation of arbitrary-precision multiplication. The PR4470 certified asymptotic region is far outside this installed implementation's domain. These finite timings cannot establish a practical crossover with PR4470, which has no executable multiplier in this benchmark. A Boolean XOR–AND work parameter also cannot be calibrated by equating it to these machine timings: hardware carry chains, multiplication instructions, memory traffic and operand widths differ.

## Reproduction and data contract

Run `tuned-inspect.py`, then `tuned-benchmark.py`, using the pinned Python and dependency directory recorded in the JSON. The benchmark does not modify the DLL on disk. Source members are extracted individually from the locally pinned [official GMP archive](https://gmplib.org/download/gmp/gmp-6.3.0.tar.xz); `tuned-installation-audit.json` records their SHA-256 hashes, ABI checks and observed CPU dispatch.

`tuned-practical-baseline.json` contains:

- `rows[]`: `profile`, `method`, `input_bits_each`, `samples`, `independent_operand_pairs`, `median_ns`, `q25_ns`, `q75_ns`, `min_ns`, `max_ns`, `median_cpu_ns`, and pair medians.
- `raw_samples[]`: profile, method, input bits, operand pair, round, iterations, wall/process CPU totals and per-multiplication values.
- `profiles`: complete selected runtime function symbols and thresholds for the actual default and the compatible override.
- `environment`: CPU, CPUID features, binary hash, affinity and its restoration, Python/platform and compiler-string evidence.
- `method`: exact benchmark conventions and auditable native wrapper assembly/bytes.

Profile keys are `default` and `compatible_broadwell_profile`. Method keys are `native_mpz_reuse`, `native_mpn_preallocated`, and `gmpy2_allocating`. Nanoseconds are per multiplication. Chart uncertainty should show observed IQR or sample range with the corresponding label, and should stop at the measured size range.
