# A smaller crossover upper using PR4470's unchanged core

This certificate constructs a different **finite-size outer schedule** around
PR4470's unchanged fixed native supplier. It does not claim a new exponent.
The core rank remains N=2^64215200000000, with its authenticated uniform saving
eta=528527/175000000 and the same full native word. Its literal-core/GMP-inactive
family is unchanged. The source native/compiler/owned and parameterized analytic
contracts remain conditional. This is AI-assisted written mathematics and exact
checks, not Lean, a human theorem review or a hardware crossover estimate.

## Deliberately larger outer slack

The original record construction uses kappa_record=60403/20000000 and very
small outer slack. Earlier crossover does not require realizing that saving
at every finite input width. Choose instead

```
kappa_effective=1/500=.002, Q=10000, delta=1/Q,
epsilon=1-delta, beta=1-3delta,
b=kappa_effective+5delta, a=kappa_effective+4delta,
q=kappa_effective+3delta, r0=delta/10, stop=layout=delta.
```

The **actual core saving remains eta**, not kappa_effective+6delta. It exceeds
that requested slack saving. The generic source outer evaluator is copied
with its exact hash in pr4535-upper-source/endpoint.py. This is the same
credited PR4359 parameter ledger, now evaluated freshly with the new schedule
and the unchanged admitted core. All54 strict predicates, four functional
guards and nine source cost margins are checked as exact rationals. Choosing
.002 also preserves its existing improvement-over-old-baseline predicate.
No positivity check is removed. The actual xi is
epsilon*(1+q)-3/32+delta.

The new explicit circuit uses the same fine-prime p^-2, Strassen, five-factor
Gaussian and48/128 halo construction, at these freshly checked parameters.
The signed Fermat integer helper remains exact, including full temporary
products and charged external rounding. Native all-column C/H calls still
use ADD/NEG only.

## Own guard, work and common gate

The already reviewed whole-word cancellation and Clifford-prefix argument
concern the fixed supplier itself; changing the stopping/base threshold does
not change those exact word identities. Thus Eguard=73475 still bounds its
semantic guard by2^Eguard*d, and G/W<K^2N with K<2^33010. Its actual width
still obeys log2W<9HN. With the **new** Q the occupied-row and ordinary-base
calculation gives

```
d0<=2^(Q(H+1)),
native active log-coefficient <=48+66020+2H,
native fallback log-coefficient <=12+Q(H+1).
```

Every old ordinary base and all row/owned work are paid. Define

```
A=Q+1=10001,
E=Q(H+1)+2H+66020+73475+179200000000+1048576+1000,
B0=2^E, p>=B0^A, X=AE, Y=AE-8.
```

The seven per-type rows have coefficient powers60,198,90,218,188,178,198,
powers of B0 equal2,1,2,1,1,1,1, and log degrees0,10,4,13,11,10,10. Their
savings, computed from the **actual** eta and new epsilon/beta/xi, are

```
epsilon*eta*(1-delta); epsilon;
1-epsilon+beta*eta*(1-delta); 1-epsilon+beta;
3/32+xi-epsilon; 80-epsilon-beta; 1.
```

The receipt checks each residual relative to kappa_effective:
`power_B0+(degree+1)/1024-A*(saving-kappa_effective)<-1`. Consequently the
full candidate has each gate count below n*p^(1-kappa_effective). It does
not assert that effective finite-size bound with kappa_record substituted.

E is smaller than2^64. No old base inequality E>=2^64 is copied: the actual
integer envelope `bit_length(E)+bit_length(A)+3<E/1024` and the decreasing
smooth log ratio directly prove all required logarithm bounds. In addition,
1040/(AE)<delta/2. The semantic guard has A*delta=1+delta and delta*E>44,
so it fits the same q=32p/stored-width33p/rounding allocation. Full helper
products may be wider and are separately charged.

Fresh capacity checks p^delta>=1024(65+1024log2p), log2p>128Q and
log2p>=2^54 supply the side lengths and analytic prime-window domains.
The direct Gaussian/Boolean realization has dyadic native coefficients and
fixed binary routes; no optional BIT finite-field wrapper or unsupported
bad-prime census is inserted. All source analytic conditioning and exact
recovery hypotheses remain separately retained.

## An eventual win and the original record tail

Let U_early=2^(2^Y) bits per operand. For every n>=U_early the retuned exact
multiplier is valid and has weighted cost below
(1+rho)n*p^(1-kappa_effective), p=256ceil(log2n). Therefore its ratio to the
unchanged repaired optimized-GMP reference is below256*p^-kappa_effective<1
for every positive tariff. The canonical HvH reference also loses; its
domain is checked at the correct logarithmic level Y>=bit_length(1729^12).

To retain the original asymptotic record, define one size-specialized family:

* below U_early use the unchanged reference multiplier;
* from U_early until the already proved original-record upper U_record,
  use this retuned multiplier;
* at and above U_record use the frozen PR4470 record-tail circuit from
  pr4470-fermat-helper-upper.json.

Both constructions win throughout their stated regions, and U_early<U_record.
Hence this family wins at every width from U_early onward. Its eventual
asymptotic saving is still kappa_record, since its final tail is exactly the
original record circuit; the weaker effective prefix occupies a fixed finite
range of widths. This uses a size-only construction choice and adds no data
branch cost. A chosen switch is not reported as a natural **lower** bound.

The literal fixed supplier is unchanged in either active schedule; in this
certified range the target selected dimension exceeds the recomputed active
cutoff, so the raw core is actually invoked. This family is within the same
unreduced-core/unchanged-GMP-when-inactive class of the independent lower.
No conclusion follows for all possible compressed or simplified algorithms.

This proves a smaller sufficient eventual upper for that conditional family.
It does not locate its first crossing, certify practical execution, or promote
kappa_effective into a new state-of-the-art exponent. The original record
upper remains separately archived as a backup witness.
