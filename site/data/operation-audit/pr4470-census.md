# PR4470: explicit finite arithmetic census

The finite controller can be counted much more closely than its published
`10^9` scalar-operation allowance. The reconstruction below yields **630,412
real ADDs and at most 353,492 real NEGs per common coefficient coordinate**,
before paid Gaussian transforms and monomial phases. There are no
variable-by-variable real multiplications in this scalar core. This is an
arithmetic-work census, not an integer-multiplication running-time constant.

## Pinned sources and reproduction

The main source commit is
`7c472563474e60185e6ca101a17622133d047e56` in
[`CrocSwap/integer-mult-bounds`](https://github.com/CrocSwap/integer-mult-bounds/tree/7c472563474e60185e6ca101a17622133d047e56).
The controller and local emitter are
[`research/joint-helper-lattice/CONTROLLER.json`](https://github.com/CrocSwap/integer-mult-bounds/blob/7c472563474e60185e6ca101a17622133d047e56/research/joint-helper-lattice/CONTROLLER.json)
and
[`native_joint.py`](https://github.com/CrocSwap/integer-mult-bounds/blob/7c472563474e60185e6ca101a17622133d047e56/research/joint-helper-lattice/native_joint.py).
The cached source files and SHA256 digests are recorded in `pr4470-census.json`.

Run `python pr4470-census.py`, then `python pr4470-component.py` in this
directory. The first script extracts selected pure construction functions
from the pinned emitter, reconstructs the literal forward and backward
programs, and cross-checks their counts and conservative primitive allowance
against the published native receipt. It does not run the full proof replay.
The second verifies the chosen Boolean arithmetic circuits exhaustively for
working widths 2 through 8 (87,376 ADD input pairs), checks the Gaussian pair
identity, and verifies the exact component threshold arithmetic.

## Finite scalar programs

| Local direction | Complex ADD | SCALE | COPY | CLEAR | Paid jobs | Real ADD lowering | Real NEG upper |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Forward | 16,265 | 1,164 | 8 | 16 | 3,310 | 32,694 | 18,074 |
| Backward | 16,273 | 1,164 | 0 | 16 | 3,310 | 32,710 | 18,224 |

Both contain 240 warp records and 448 adapter records. Every scale is a
signed power of two. The ADD coefficients have numerator magnitudes only
1, 2, 3, 4, 5, 7, 8 and power-of-two denominators. Their exact histograms are
in the JSON. The lowering uses fixed shifts and explicit shift/add
multiplication by those small integer constants; each subtraction is an ADD
with an explicit NEG. It is deliberately conservative about sign sharing.

The raw p16 controller contains 2 forward and 16 backward local calls,
90 controller ADDs, 15 thin QUERY_SHEARs, 16 SIGNED_SWAPs, and two boundary
words totalling 81 ADDs, 7 negative SCALEs and 57 SWAPs. Controller operations
act over 112 ports. The query recipe copies an arbitrary input to owned
storage, pays its rank-one Gaussian operation, adds into the target, and
erases the owned storage. This supplies a further 15 × 112 complex ADDs.
After these scalar events are included, the census is 630,412 real ADDs and
at most 353,492 real NEGs per coefficient coordinate.

## A completely stated Boolean work tariff

AND costs 1 and XOR costs `rho >= 0`. Fixed wiring, constants, fanout, copies,
and routing permutations are free. NOT is XOR with 1. This is nonuniform
Boolean circuit work; it does not price tape or memory movement.

For `w >= 2`, choose the tested modulo-`2^w` ripple circuits

```
A_w = (2w-3) + rho (3w-3)       real ADD
N_w = (w-2)  + rho (2w-3)       real NEG.
```

The scalar core therefore has the upper counts

```
XOR <= 2,598,220 w - 2,951,712
AND <= 1,614,316 w - 2,598,220.
```

These circuits themselves are exact modulo `2^w`. To interpret them as the
rational scalar program, **w must contain all integer and fractional guard
bits required by the whole selected computation**. Every dyadic shift must
be exact on that grid, without overflow or input-dependent truncation. An
output division by two cannot be treated as a free right shift on an
arbitrary fixed-point word. The circuit tests do not prove this precision
precondition, and w is not the multiplication input length.

For this isolated raw layer, the precondition can be made constructive for
dyadic inputs. Suppose every original real component is an integer multiple
of `2^-q` and has absolute value `<2^b`, with `b>=1`, `q>=0`, and owned storage
starts at zero. The exact scalar coefficient census gives total denominator
exponent 212,958, 313,730 complex scalar ADDs, and 21,736 SCALEs. Four
magnitude bits per ADD cover numerator magnitudes up to eight and their
temporary shift/add results; two per SCALE suffice. Each paid Gaussian
rank-one axis needs one further denominator bit and at most two magnitude
bits including its numerator temporaries. Thus a conservative sufficient
common exact grid and signed working width are

```
fractional_bits = q + 212958 + 239134 f,
w >= b + q + 1511351 + 717402 f.
```

This gives `w >= b+q+195927293` at f=271. With that allocation all divisions
discard only known zero bits and the chosen modulo-word circuits have no
overflow. This new guard bound assumes the declared dyadic-Gaussian and
monomial lowering for the raw layer; it does not prove the native operator
identity, and it is not a precision bound for the integer algorithm. It
demonstrates that exact raw-layer arithmetic does not need an unspecified
real-arithmetic oracle.

## A conditional, explicit mixed-layer crossover

This comparison evaluates the raw controller as a family of independently
specified Gaussian transforms, not the final integer multiplication.
The raw productive rank mass is 239,886, whereas its paid rank mass is
239,134: it saves 752 rank-one axes. All fields have a common number `L` of
complex coefficient coordinates and complete spectators.

The pinned exact Clifford implementation defines the elementary Gaussian
pair by `C=((1+i)I+(1-i)X)/2`. For each complex pair z,w it can be computed as
`s=z+w`, `t=z-w`, then `(s+i t)/2,(s-i t)/2`. This requires eight real ADDs
and four NEGs per pair, hence **4 ADDs + 2 NEGs per complex coordinate per
axis**. See
[`clifford_exact.py`](https://github.com/CrocSwap/integer-mult-bounds/blob/7c472563474e60185e6ca101a17622133d047e56/research/t74-native-fast/vendor/native/new/code/borrow/vendor/clifford/clifford_exact.py).

Fixed binary monomial maps lift by coordinate permutation and fourth-root
phases under the retained all-column contract. A fourth-root phase requires
at most two real NEGs per complex coordinate; its real/imaginary exchange is
wiring. Conservatively pay for two monomial factors around every productive
and paid transform, all local warp and adapter events, and each physical
query route:

```
extra_NEG <= 4(64,620 + 10,928)
             + 2[18(240 + 448) + 1,680]
          = 330,320.
```

This intentionally overcounts overlapping or annotation-only records. It
uses the explicit binary-monomial/fourth-root-phase implementation contract,
not an independent verification of arbitrary-width physical execution; see
[`FINITE-TEMPLATE-CLOSURE.md`, sections 2–3](https://github.com/CrocSwap/integer-mult-bounds/blob/7c472563474e60185e6ca101a17622133d047e56/research/higher-moment-strictification/vendor/FINITE-TEMPLATE-CLOSURE.md).

Consequently, at column width f the independent Gaussian baseline costs

```
239886 f (4 A_w + 2 N_w) L,
```

whereas the mixed layer has the conditional upper cost

```
[239134 f (4 A_w + 2 N_w) + 630412 A_w + 683812 N_w] L.
```

An explicit sufficient integer threshold is therefore

```
f(w,rho) = floor[(630412 A_w + 683812 N_w)
                 / (752 (4 A_w + 2 N_w))] + 1.
```

Since `N_w/A_w <= 2/3` for every `w >= 2, rho >= 0`, the fraction is at most
`814715/3008 = 270.84940159574468...`. Thus **f >= 271** suffices under the
stated operator, monomial, precision, ownership and free-wiring assumptions.
At f=271 the saving is at least `604 A_w L > 0`.

For a slider that does not assume a particular working width, an explicit
threshold sufficient for **every valid w** is

```
F(rho) = floor[(3258860 rho + 1944636)/(12032 rho + 7520)] + 1.
```

Indeed `N_w/A_w` increases with w: the derivative has positive numerator
`3 rho^2+3 rho+1`, and the limiting ratio is `(2 rho+1)/(3 rho+2)`. The
threshold fraction increases with `N_w/A_w`. Thus `F(.001)=259`, `F(1)=267`,
and `F(1000)=271`. A corresponding uniform-in-width work-ratio upper bound is

```
239134/239886
 + (3258860 rho + 1944636)/[239886 f (16 rho+10)].
```

These are strict sufficient thresholds for the conditional component
comparison. Their native/phase/precision assumptions remain essential.

This is a finite component result, not merely an asymptotic exponent.
For example w=32 and rho=1 give f=266. It is still an enormous mathematical
object: the literal binary ambient lift at f=271 has 145f=39,295 axes and
`L=2^39295` complex coordinates per field. It does not establish a crossover
against HvH, GMP, or a complete integer multiplication circuit. It also does
not equate this raw template with the later uniform rank-N compiler.

## Tensor-product counts are also explicit

Let `B=10928`, `P=64620`, `v=1024`. The chronological product's number of
raw controller instances satisfies

```
U_1=1, U_(j+1)=B U_j + P^j,
U_v=(P^v-B^v)/(P-B).
```

It has exactly `B^v` productive fields, `P^v` paid children before completion
and splitting, and `18 U_v` local native calls. Its scalar core contains
`630412 U_v` real ADDs and at most `353492 U_v` NEGs per common coefficient
coordinate. `U_v` has 4,922 decimal digits and log2 approximately
16,347.493345751278. The full exact integers, hashes and log-space values
are in `pr4470-tensor-counts.json`.

There is also a source-derived finite *record-count upper bound*, rather
than an assumed small compiler constant. With raw scalar allowance
`L0=10^9`, `m=145`, raw paid rank mass `J=239134`, and floor rank `b=21`, the
bound in
[`query-thinned-controllers/PROOF.md`, section 5](https://github.com/CrocSwap/integer-mult-bounds/blob/7c472563474e60185e6ca101a17622133d047e56/research/query-thinned-controllers/PROOF.md)
gives

```
R_sep <= [10^9 v (B+P)^v + J^v + B^v 21^v] [10 m^(2v)+10].
```

The evaluated upper bound has 9,936 decimal digits and log2 approximately
33,004.05451924549. A record can denote a whole-field operation, so this
number is not a Boolean gate count or a runtime coefficient.

## Correct parent comparison

The published PR4447 predecessor, pinned at
`322e0ec764aa7ef7801383feb1f656e460dd8bed`, has 69,273 raw paid jobs,
11,560 productive fields, and 19 full local calls (p17). PR4470 has 64,620,
10,928, and 18 respectively (p16). The local tariff falls from 3,363 to 3,310;
the reconstructed local scalar ADD/SCALE coefficient histograms are unchanged.
Thus this improvement is genuinely in the recursive-job invoice while
retiming local contacts; it does not reduce the local scalar core.

The number 65,574 is **only** the counterfactual old local tariff on the new
p16 geometry (`64620 + 18*53`), not the published parent raw paid count. The
published parent and child have different geometry, so subtracting their
totals is not by itself a same-input runtime comparison.

## What remains for an integer-multiplication crossover

The native replay certificate is not a complete bit-arithmetic execution:
[`native_extensions.literal_replay`](https://github.com/CrocSwap/integer-mult-bounds/blob/7c472563474e60185e6ca101a17622133d047e56/research/kappa-rebuild/complex/native_extensions.py)
updates rational rows and abstract free-warp symbols, while paid `climb` and
`center` events update frames/profiles rather than evaluating the Gaussian
arithmetic. The retained all-column operator, whole-job matcher, owned
erasure and physical-tape contracts are explicitly inherited in the source
proof. Their distinction matters even though finite Gaussian arithmetic can
be lowered to Boolean gates after a precise width is chosen.

A full integer circuit would additionally require a concrete complete
uniform compiler expansion, working widths/rounding at every stage, and
numeric implementations/counts for the outer encoding, transforms,
pointwise products, recovery and recursion/base cases. A source record
bound and an eventual precision cut-off do not supply these counts. The
new finite census and conditional layer threshold are usable pieces of
that derivation; they do not supply an end-to-end numerical crossing point.
