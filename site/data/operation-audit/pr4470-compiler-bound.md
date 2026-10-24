# A source-derived full uniform-supplier inventory bound

This supplements the exact finite census. It gives an explicit upper bound
for a **particular source-permitted uniform compiler**, including batch
replication and smaller-rank suppliers. It does not materialize its word or
prove the inherited native operator contracts. Counts use the declared
nonuniform XOR–AND work model: fixed address/role permutations are wiring,
and a binary monomial's fourth-root phase needs at most two real NEGs per
complex coefficient coordinate. They are not physical tape instructions.

All source references use commit
`7c472563474e60185e6ca101a17622133d047e56` of
[`CrocSwap/integer-mult-bounds`](https://github.com/CrocSwap/integer-mult-bounds/tree/7c472563474e60185e6ca101a17622133d047e56).

## 1. The completed mixed unit has an explicit fixed budget

Put v=1024 and

```
R* = [10^9 v (10928+64620)^v + 239134^v + 10928^v 21^v]
      [10 145^(2v)+10].
```

This is the nonrecursive record bound prescribed by
[`query-thinned-controllers/PROOF.md`, section 5](https://github.com/CrocSwap/integer-mult-bounds/blob/7c472563474e60185e6ca101a17622133d047e56/research/query-thinned-controllers/PROOF.md).
Its exact value has 9,936 decimal digits and log2 approximately
33,004.05451924549. Exact integer comparisons show it also exceeds the
productive width B, the paid count P after completion/splitting, and the
raw-controller instance count U of this completed mixed unit. The source
permits an owned-bank allocation bounded by the expanded record count.
Thus every one of B,P,U,owned and nonrecursive-record counts is at most R*.
The completed unit has minimum productive rank 21^1024 and maximum paid
rank at most 20^1024. Counts and integers are saved in
`pr4470-tensor-counts.json`.

Set `K=32(R*+1)`. The script verifies the concrete bound **log2 K < 33010**.

## 2. Count the exact lockstep flow before clearing denominators

For a top rank n outside the source's finite base range,
[`FINITE-PRECOMPILATION.md`, section 3](https://github.com/CrocSwap/integer-mult-bounds/blob/7c472563474e60185e6ca101a17622133d047e56/research/higher-moment-strictification/vendor/FINITE-PRECOMPILATION.md)
specifies classes indexed by paid-round sequences of length d and target
multi-indices a of length G-d. The number of paid-round sequences is P^d.
The multinomial sum of their unit multiplicities is at most B^(G-d).
Eligibility restrictions only remove units. Since every target rank is at
least two, G<=floor(log2 n). Consequently the total mixed-unit instances I_n
satisfy

```
I_n <= sum_(d=0..G) P^d B^(G-d) <= (B+P)^G <= K^n.
```

The flow's number of missing source jobs S_n is at most B I_n. Its exits
are at most P I_n, because each exit is a paid edge from some unit.
Each source or paid edge needs at most two additional whole-job monomial
maps, one into its destination and one restoring it. Pay at most four real
NEGs per coordinate for that pair. Thus compiler routing contributes at
most `4(B+P)I_n` such records. Initial/final source-role permutations are
fixed wiring in this model. The mixed unit's own charts, completion,
splitting and adapters were already paid by R*.

This adapter budget uses the named whole-job binary-monomial contract in
section 1 of the same source. It would not bound a generic dense linear map
or a physical tape movement implementation.

## 3. A concrete integral batching choice and recurrence

For every rank n, define

```
D_n = 1 + B_n + P_n + owned_n + raw_instances_n + records_n.
```

Here `records_n` includes all nonrecursive scalar/phase records of the
expanded supplier, including compiler adapters. At source-required base
ranks use the ordinary sequential program, B_n=1, P_n=n; other counts are
zero. Define this valid denominator-clearing choice:

```
a_n = product_(1<=e<n) B_e.
```

This is divisible by every smaller program width used for a complementary
source job or exit. Including widths of unused ranks merely increases the
replication. Section 4 of
[`FINITE-PRECOMPILATION.md`](https://github.com/CrocSwap/integer-mult-bounds/blob/7c472563474e60185e6ca101a17622133d047e56/research/higher-moment-strictification/vendor/FINITE-PRECOMPILATION.md)
explicitly permits the product choice.

Let `d=max_(e<n)D_e`. After multiplying by a_n, the number of smaller-program
copies for source complements and exits is at most a_n(B+P)I_n; dividing by
their productive widths only lowers this bound. Fresh productive width,
raw units, owned fields and records, compiler phases, and all smaller
inventories therefore give

```
D_n <= 1 + a_n I_n [B+U+owned+records + 4(B+P) + (B+P)d]
    <= 1 + a_n I_n [12R* + 2R*d]
    <= a_n I_n K d
    <= a_n K^(n+1) max_(e<n)D_e.
```

Every term is charged; discarded child inventories or extra batches only
make the bound looser. Taking logarithms x_n=log_K D_n yields

```
x_n <= sum_(e<n)x_e + max_(e<n)x_e + n+1.
```

Strong induction gives the explicit solution

```
D_n <= M_n = K^(4^n).
```

The numerical inequality used in the induction is
`sum_(e=1..n-1)4^e+4^(n-1)+n+1 <= 4^n` for n>=2. Its remaining margin is
`5*4^n/12+4/3-n-1`, positive at two and increasing thereafter. Sequential
base inventories n+2 also satisfy the bound.

## 4. Substitute the authenticated uniform rank

The current uniform rank is `N=2^H`, H=64,215,200,000,000. Put M=K^(4^N).
Every productive-width, paid-child, raw-unit, owned-field and nonrecursive
record count is at most M, with

```
log2 M < 33010 4^N = 33010 2^(2^(64215200000001)).
```

This immense expression is an explicit finite upper bound derived from the
source's actual batching algorithm. It is not a normalized leaf-count
estimate or an assumed small constant.

The inherited semantic-precision formulas from
[`TENSOR.md`, section 6](https://github.com/CrocSwap/integer-mult-bounds/blob/7c472563474e60185e6ca101a17622133d047e56/research/pr4359-p7-padding/TENSOR.md)
are

```
Z=W+owned, G=10^9 U_raw+8R,
E=64(Z+N+P+G+1)^3,
B_constant=P+E, C0=32 N B_constant^2.
```

Since N<=M and every count is at most M,
`Z+N+P+G+1 < 2^30 M`, so

```
C0 < 2^199 N M^6,
log2 C0 < 199 + H + 198060 4^N.
```

This upper bound can be substituted in the explicit precision recipe. It
does not identify C0 with a runtime coefficient.

## 5. Boolean work and exact dyadic guards for the finite supplier

The compiler composes and copies the emitted scalar lists. It never needs
to synthesize a new dense scalar matrix. Their real coefficients retain
numerator magnitude at most eight and denominator at most eight. Binary
monomial adapters add only fourth-root phases and wiring. A complex scalar
record lowers to at most eight real ADD/NEG macros; the coefficient 7/8,
for instance, needs at most three ADDs and one NEG on each real component.

At column multiplicity f every rank-one paid leaf is the elementary
rank-f Gaussian job. Directly execute its f axes, each at 4 real ADDs and
2 NEGs per complex coordinate. With A_w,N_w as in `pr4470-component.json`,
the **complete finite uniform supplier** has Boolean work at most

```
L M [8(A_w+N_w) + f(4A_w+2N_w)],
```

where the literal complete ambient field has `L=2^(Nf)` complex coordinates.
This includes its owned-field scalar operations, routing phases, and all
paid Gaussian children. The supplier's productive width is already
represented in its instruction count; do not multiply this expression by
B_N again.

For original real inputs on a 2^-q grid with absolute value<2^b, a sufficient
common fractional grid is `q+3R+Pf`. Three denominator bits per scalar
record and one per Gaussian axis suffice. Four magnitude bits per scalar
record and two per Gaussian axis cover all numerator temporaries. Thus

```
w >= b+q+7R+3Pf+1
```

is a sufficient signed width; the explicit bound
`w >= b+q+(7+3f)M+1` is looser. At f=1, denominator exponent<=4M, prefix
magnitude-growth bits<=6M, and coefficient numerator integer bit length
<=10M+1 (the extra bit covers the integer-height convention).
This supplies finite coefficient/guard bounds without treating real
arithmetic as an oracle.

These remain conditional supplier results. The all-column identity,
complete arbitrary spectators, owned-bank discipline and whole-job
monomial contract are inherited. No end-to-end outer encoding,
pointwise-product, approximation/recovery or integer-multiplication
crossover theorem follows from this inventory alone.

## 6. A finite crossover bound for this whole uniform Gaussian supplier

The authenticated result records uniform saving
`eta=528527/175000000` and `P < B N^(1-eta)`; see
[`joint-helper-lattice/RESULT.json`](https://github.com/CrocSwap/integer-mult-bounds/blob/7c472563474e60185e6ca101a17622133d047e56/research/joint-helper-lattice/RESULT.json).
The exact test H eta>1 passes, so `P < BN/2`. The complete independent
B-field direct Gaussian circuit costs `BNf(4A_w+2N_w)L`; the whole compiled
supplier costs at most `[Pf(4A_w+2N_w)+8M(A_w+N_w)]L`.

For every valid w>=2 and rho>=0,
`(A_w+N_w)/(4A_w+2N_w)<=5/16`. Saved rank mass is `BN-P>BN/2>=N/2`.
Consequently the explicit sufficient integer column width

```
f = floor(5M/N)+1,   M=[32(R*+1)]^(4^N)
```

gives strict work savings, including the whole compiler scalar/phase word.
This is a much larger bound than the raw mixed-layer f=271 result, since
it charges a different, fully uniform construction and an extremely loose
inventory envelope. Both comparisons refer to Gaussian transform circuits;
neither is the integer-multiplication crossover requested for the outer
algorithm. The same explicit exact-grid allocation above applies.

`pr4470-compiler-bound.py` checks the exact raw inequalities, K bound, and
induction arithmetic and writes `pr4470-compiler-bound.json`.
