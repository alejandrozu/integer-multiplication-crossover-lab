# Conditional p7 outer saving 0.00268647

The native p7 construction in `NATIVE.md`, together with the tensor and
target-padding construction in `TENSOR.md`, supports the proposed conditional
bound

```
T(n) = O(n (log n)^(1-kappa)),       kappa = 0.00268647.
```

This raises the exponent saving by `0.00038647` over PR4359's `0.0023`, and
by `0.00000660` over PR4414's p6 point `0.00267987`. These compare exponent
savings, not measured running times. The selected frontier is unchanged.

The result remains conditional on the documented all-column native,
whole-job adapter, spectator, finite compiler, storage, precision, analytic,
fixed-tape, and recovery hypotheses inherited from zxv's PR4359 at
`da637c87c89482bc4c86be36bd0071b3d400dbed`. The p7 Laurent factorization,
geometry and native ownership are checked in this package. Finite checks do
not constitute a formal proof of the full multiplication theorem.

The native source is credited to zxv's PR4359 and integer mixed flow to
Jacob Alan Sussman's Theorem 1G. The outer slack family and executable
ledger are retained from PR4405 at
`873d1b3c96a83b701a5c0bba8e37a861e6672fef`, with its attribution to
@Vlado-V's PR1673, @jeremykothe2's PR1758, @chafreaky's PR1786, and their
cited predecessors. Apache-2.0; substantial OpenAI assistance.

## Native invoice and why target padding is needed

The exact all-fresh p7 invoice is

```
targets = {5:420, 6:270, 7:840, 8:1395, 9:3195,
           25:448, 41:448, 57:448, 121:224},
paid    = {1:37305, 2:10695, 3:3360, 4:1530, 5:300,
           8:1464, 16:448, 32:448, 48:448}.
```

It has 7,688 productive fields, target rank-one moment 131723, and paid
rank-one moment 131115, leaving surplus 608. Its raw paid ranks exceed its
smallest target ranks. Moreover, a rank-one tail bound with cutoff below
the raw minimum target rank does not suffice near this proposed saving.

The new construction tensors the native word `v=6240` times, completes
every productive endpoint of rank smaller than `11^v` to rank `11^v` on
unused disjoint axes, and splits every paid call, including those endpoint
completions, into consecutive pieces of size at most `10^v`. Endpoint
completion occurs only after the whole native tensor word has finished.
It uses the same arbitrary productive array, without new productive credit
for copied inputs or work storage. The ambient rank `121^v` has room for
each completion.

At `C_test=0.00268648`, write `tau=1-C_test` and let `P_tau,T_tau` denote
the raw moments. The certificate proves

```
P_tau/T_tau < 1 - 1/10^8,
131115/(10^C_test*T_tau) < 4991/5000,
7688*11/(10^C_test*T_tau) < 2/3.
```

The first bound controls the original tensor word. The second pays for
splitting its large calls. The third pays for completing small productive
endpoints and splitting those completion calls. For a completion of rank
`D<11^v`, writing `D=q*J+r` with `J=10^v` gives, including `q=0`,

```
q*J^tau+r^tau <= D*J^(-C_test)+J^tau
              < 2*11^v/J^C_test.
```

Thus the complete normalized paid moment is bounded by
`alpha^v+2*gamma^v+2*padding^v`, while the target moment only increases.
The exact block bound `(4991/5000)^390<1/2` gives 16 decay blocks. The
completion tail satisfies `(2/3)^2<1/2`, giving 3120 blocks. Bounding both
tails by `2^-16` yields the simpler sufficient inequality

```
1/(1+6240/10^8) + 4/2^16 < 1.
```

Every paid rank is now at most `10^v`, and target ranks lie between `11^v`
and `121^v`. Rank-one surplus is unchanged: each endpoint completion adds
the same rank to the paid and target totals, and paid splitting preserves
rank. Hence it remains `131723^v-131115^v>0`.

## An explicit uniform rank

Choose

```
kappa   = 0.00268647,
d       = (C_test-kappa)/7 = 1/700000000,
uniform = kappa+6*d = 376107/140000000,
t       = 1-C_test,
z       = 1-uniform,
z0      = (t+z)/2,
delta   = z0-t = 1/1400000000.
```

The source compiler now has `m=121^v`, `k_min=11^v`, and `r_max<=10^v`.
The exact integer inequality `10^26<11^25` gives exit exponent below
`25/26`, so use `h=1/26`. For ambient rank `x>=m`,

```
m E(x)/x < m^h*r_max*x^(-h)
          < 2^B*x^(-h),              B=(111/26)*v=26640.
```

This follows from `10<2^4` and `121<2^7`. The exact complement coefficient
is `eta=z0*m^(z0-1)`. Since `z0>1/2`,

```
-log2(eta) < 1+7*v*(1-z0) = 147931769/1250000.
```

The entirely rational sufficient formulas

```
H0 = ceil((B*delta+1+7*v*(1-z0))/(h*delta)),
H1 = floor(H0*(1-z0)/(z-z0))+1
```

therefore give

```
H0 = 4307773805920,
H1 = 16201843136005340321,
N  = 2^16201843136005340321.
```

The verifier checks `H0>=7*v`, covering the entire finite base range.
Below `2^H0`, the rank-one surplus gives `L(x)<=x`; above it the exit
coefficient is below the complement coefficient. Strong induction yields
`L(x)<=A*x^z0`, with `A=(2^H0)^(1-z0)`, for every positive integer rank.
The strict final power gap is `1/1400000000`, proving
`P_N/B_N<N^(1-uniform)`.

This is a specified finite exact program with very large constants. Neither
the tensorized and padded word nor the uniform compiled word has been
materialized. Their complete instructions, integer batch factors, paid
leaves, scalar operations, and owned banks are defined by the finite
recipes. The one-less-integer controls only concern these sufficient
formulas; no minimal-rank claim is made. The initial sufficient choice
`v=30000`, paid cutoff `7^v` and target floor `8^v` gave
`H1=47613655221424910001`; the final parameters reduce both the tensor
power and this rank exponent while preserving the same tested saving.

## Outer parameters and changed constants

Use the same strict outer family:

```
b=kappa+5*d,  a=kappa+4*d,  q=kappa+3*d,
epsilon=1-d, beta=1-3*d, r0=d/10, stop=d, layout=d.
```

Retain the ordinary BIT saving `0.0027`, atom exponent `0.003`, Strassen
exponent `45/16`, theta power `2`, halo power `48`, and core power `128`.
The effective saving remains strictly below both the new complex saving
and the admitted BIT saving. The frozen ledger recomputes all nine outer
cost rows, all 54 named predicates, and three additional functional
predicates at this point. The limiting main-transform margin is exactly
`524529867/122500000000000000 > 0`.

The inherited 63-row ledger was compared with this current predicate set
in PR4405: all 50 common predicates and all nine costs agreed, and the
13 omitted rows were historical endpoint comparisons. The larger kappa
preserves those comparisons; this package reruns the current 54 plus three
functional predicates.

Apply the source precision and stock theorem using the new p7 word,
tensor/padding recipe, compiler counts, scalar word, and owned storage.
No p3 or p6 raw scalar constant is substituted for the new word. Its new
fixed constants and denominators are absorbed after an effective threshold
by the positive semantic, support, stopping, and fine-prime spare powers.
The unchanged BIT template retains its separately compiled and covered
construction.

## Replay and remaining work

```
python3 -I -O -B research/pr4359-p7-padding/endpoint.py
```

The integrated command checks the native p7 invoice and geometry, the
tensor/cutoff/padding moment, the specified uniform rank, and every outer
predicate. Mutation controls reject closing the precision or uniform gap,
requesting the unfunded tested endpoint as kappa, and reducing BIT below
the required effective saving. Complete source authentication is a separate
package-verifier stage.

Next questions include independently formalizing the native tensor and
endpoint-completion construction, improving the controller family, and
reducing the tensor power and sufficient rank. The bounded controller
search does not establish global optimality. The inherited all-size
analytic and native hypotheses remain conditional premises.
