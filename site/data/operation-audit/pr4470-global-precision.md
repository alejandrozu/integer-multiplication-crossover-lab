# PR4470: an explicit global Gaussian precision envelope

This is an AI-assisted written mathematical audit of the selected PR4470 realization at pinned
commit `7c472563474e60185e6ca101a17622133d047e56`. It gives a numeric precision
and validity envelope, retaining the source native identities and the named
compiler/boundary contracts. It is not a Lean formalization, an implemented
integer multiplier, or, by itself, a whole-integer crossover certificate.

The cost model is the nonuniform `xag-straightline-v1` circuit model: constants,
fixed permutations and precomputation are free. Input-dependent fixed-point
operations must still be lowered to the stated AND/XOR circuits. In this note
`rho_shape=t/s=1+theta` is geometric, and has no connection to the positive
XOR/AND cost slider `rho_cost`.

## Statement and interfaces

Put

```
delta = 1/1400000000,
epsilon = 1-delta, beta = 1-3delta,
d = floor(p^epsilon), g <= floor(p^beta), ell = ceil(log2 p), u = ell+1,
N = 2^64215200000000,
Mbar = 2^(33010*4^N), p0 = Mbar^1000000000000000.
```

Require `p>=p0`, `1/(4p^2)<theta<=1/p^2`, the source choice
`alpha=ceil(sqrt((4/pi) ln(16p)))`, and source/target axis periods at least
`p^256`. Preserve the source physical period cut as a cell boundary. Interior
caps have dyadic length `B<=p`, are subdivided with width-W separators exactly
as in the source, and use their own source anchor and fractional shift.

The explicit common working parameters are

```
W = 2ceil(sqrt(256p ell))+2,
P_setup = 512p +128p^2 u,
q = 32p,
A_ext = 2^23 p^beta u^5 +2048u +6144p^epsilon u +2log2T,
Delta = C0 d <= Mbar^8 p^epsilon.
```

Also require the proved input-mapping bound `log2T<=p/128`. At this gate
`A_ext<7p/256<p/16`, `Delta<p/256`, and the signed words holding
individual real components require

```
w = q+2A_ext+2Delta+3 <= 33p.
```

Raw scalar multiplication temporaries may have up to `2w+O(1)` bits; the full
width must be charged to the multiplication helper. The `33p` claim concerns
stored components and exact native supplier intermediate words, not those
full products. No numerical rounding occurs inside the native supplier.

The interfaces used here are: the exact source Gaussian resampling identity;
the source all-column native C/H identity and owned-storage discipline; the
shallow displacement circuit algebra, with depth made explicit in
`pr4470-outer-census.md`; the all-size occupied-batching supplier's semantic
guard `C0*d`; and the boundary error module in
`pr4470-boundary-recovery.md`. The latter module assumes physical reference
norm and inverse bounds which are supplied in Section 3 below. The whole
integer encoding, pointwise product, carry and input-size ledger remains a
separate assembly interface.

## 1. Shifted Toeplitz kernels at fine padding

The selected package is `outer/GAUGEFREE-INTERIORS.md`, modified by
`outer/FINE-PADDING-COMPOSITION.md` and `vendor/pr1786`. The historical
`theta~1/d` gauge and historical Neumann approximation restriction are not
used. The exact resampling identity is valid for every positive theta; the
new direct finite-matrix circuits replace that old approximation.

Let `a=pi alpha^2` and `b0=pi/alpha^2`. For `p>=2^20`, the elementary bounds
`3<pi<22/7`, `ln2>1/2` and `ell<=3 ln(p)/2+1` give

```
a <=8 ln(16p)+2pi <=8ell+40 <=10ell,
alpha^2 <=4ell.
```

For the broad shifted kernel the source chooses
`gamma=b0/rho_shape` and `s=-anchor_delta*(1-theta)`, giving
`1-2|s|>=theta`. For the narrow kernel
`gamma=a*rho_shape`, `s=-beta_anchor/rho_shape`, giving
`1-2|s|>=theta/2`. Both therefore satisfy

```
gamma >=1/(4ell),  1-2|s| >=1/(8p^2).
```

The exact normalized kernel is `k(h)=exp(-gamma*(h^2-2sh))`, with diagonal
one. The source triple-product/accretivity proof gives

```
mu >= (1-exp(-gamma*(1-2|s|))) exp(-pi^2/(3gamma)),
Lambda <=3+sqrt(2pi/gamma).
```

The first factor is at least `1/(64ell p^2)>=p^-3`: if its argument is at
most one use `1-e^-x>=x/2`, otherwise use `1-e^-1>1/2`. The second factor
is at least `exp(-(40/3)ell)>=p^-21`. Consequently `mu>=p^-24` and
`Lambda<=p`.

Distinguish the raw kernel truncation radius
`J0=ceil(sqrt(256p ell))` from the physical augmented bandwidth
`W=2J0+2`. Fine padding gives `rho_shape<3/2`, so in fact
`gamma>=pi/(4ell*rho_shape)>1/(2ell)` for the broad kernel; the narrow
kernel has the same stronger bound. For `|h|>=2`,
`h^2-2sh>=h^2/2`. The tail beyond J0 is therefore at most
`4exp(-J0^2/(4ell))<=4e^-64p`. Also `W<=36sqrt(p ell)<=p` at the
common gate. Truncate and round both signed raw offsets, retaining the
diagonal one exactly. A `512p`-fractional-bit grid produces induced
1 and infinity perturbations below `p*2^-512p+4e^-64p`, much less than `mu/2`.
Thus the rounded kernels have `mu_hat>=p^-24/2`, `Lambda_hat<=2p`.

Every recursive leading-section Schur descendant has inverse 2-norm at most
`2p^24`; the principal-submatrix inverse identity supplies this bound.
Converting to induced infinity norm costs at most `sqrt(B)<=sqrt(p)`,
so its inverse infinity norm is below `p^25`. Its 2-norm is at most
`2p+(2p)^2*(2p^24)`; the same conversion bounds its infinity norm by `p^30`.
To avoid using the original
matrix norm for a descendant block, bound its shear by `p^30*p^25=p^55`.
This is a deliberately safe replacement of the shorter source bound.

Stein displacement generators can be chosen with one column orthonormal and
the paired column norm at most `2p^55`; converting to l1 adds at most
`sqrt(B)<=sqrt(p)`, so `||h||_1<=p^57`. In the source generator compiler take
its scaling `Gamma=4p^58`. Then the triangular `P=I+U(h)/Gamma` and its inverse
have norm at most two. The companion diagonal FFT factor has magnitude at
most `4p^58.5<=p^61`. All exact elementary gate matrices and their inverse
matrices have entries bounded by `p^64`, including leaf pivots, near-I
triangular P leaves, unitary FFT butterflies and dirty shears. This does
not bound the reciprocal of every nonzero off-diagonal entry: a shear
parameter may be arbitrarily tiny. Such entries are never reciprocated;
the six-H replacement below supplies an explicit safe nonzero denominator.

## 2. Explicit word depth, tensor groups and prefixes

The parity-split triangular recursion and bounded-rank block-LU recursion in
the source give the explicit local matching depth
`D<=1024(log2 B+1)^4<=1024u^4`, as derived in the companion outer census.

The three-H identity for a shear is

```
U(t) = diag(-t/10,-1/6) H diag(2,1) H diag(-3,1) H diag(5/(4t),1).
```

It is valid for nonzero t. For arbitrary `|t|<=p^64`, set
`c=2p^64+1` and apply `U(t)=U(t+c)U(-c)`. Both arguments have magnitude
between `p^64` and `4p^64`. This uses six H calls and avoids a tiny
denominator even if t=0. Each scalar factor and its inverse is bounded by
`2^8 p^64<=p^72`; merging adjacent diagonals gives `p^144`. Fixed matching
routes are free wiring in this model. Swaps and diagonal gates have the
same or smaller fixed-word envelope.

There are at most `K=6D<=6144u^4` Hadamard calls and `K+1` diagonal stages
per tensor group. With h axes, the coefficient and inverse range of a
diagonal tensor is at most `p^(144h)`. Include the source whole-factor
normalization `p^(-100h)`, and use the safe range `p^(256h)`. A raw H tensor
has infinity norm `2^h`, and inverse norm at most one. Counting even these
crude gatewise norms yields prefix and suffix logarithmic ranges at most

```
h*[K+(256ell+1)*(K+1)] <= 2^21 h*u^5.
```

The source exact anchored chirps add at most
`4hu+6haB^2/p^2` bits of range. For `B<=p`, `a<=10ell`, and `h<=p^beta`,
the combined range is below `2^23 p^beta u^5`. This also bounds the inverse
prefixes needed to reverse an inverse-interior circuit.

Each axis uses the same pattern: five completed factors for forward square
completion, five for compression/inversion, the selected-row normalization
and extraction, and (if separately charged) the factor /4. Padding with
identities synchronizes these into **12 global tensor rounds**. Within a
round, axes are partitioned into groups of at most g. Factors on different
axes commute. There is no extra multiplicative d after counting the groups
in these 12 rounds. This statement does not collapse a one-dimensional
radix-2^d DFT into one H_d; that would be false.

## 3. Physical reference sections and boundary module

The reference matrices remain the source global rounded Gaussian matrices.
They are compared with the actual anchored shifted-kernel circuits, rather
than silently identified with them. The broad forward and narrow inverse
have different conditioning obligations.

For a broad interior, the source finite-origin LDU calculation in
FORWARD-SMALL-A-AUDIT.md, Section 1, gives

~~~
||K^-1||_infinity <= alpha exp(3b/4) exp(a*rho_shape/3)
                         /(1-exp(-b*rho_shape*theta))^2,
b=pi/(alpha^2*rho_shape^2).
~~~

It requires successive selected coordinates separated by at least one and
beta values in [-1/2,1/2]. Apply it only to the nonwrapping contiguous
interior sections inside one physical phase cell. Here alpha<=p,
exp(3b/4)<=p, b*rho_shape>=1/(4ell), and the gap is at least
1/(32ell p^2)>=p^-3. Also exp(a*rho_shape/3)<=exp((20/3)ell)<=p^11.
Hence each such inverse is at most p^19. These are the A blocks of the
broad forward five-factor formula. That formula applies its Schur map F;
it NEVER inverts broad F or claims a broad periodic LU-prefix bound.
Its boundary norm is at most p+p^2*p^32<=p^35.

For narrow compression, use the stronger source-exact row dominance proof
on the periodic matrix itself. Pairing its two nearest directions gives

~~~
||N-I||_infinity <=exp(-2a theta)+5exp(-2a).
~~~

Since theta>=1/(4p^2) and a>=4ln(16p)>=1, the first deficit is at least
1/(4p^2), while 5exp(-2a)<1/(8p^2). Thus N has row gap at least
1/(8p^2). Tiny periodic diagonal aliases are removed with the tail
allowance to preserve diagonal exactly one. Rounding retains gap at least
1/(16p^2). Every principal section inherits this gap and therefore has
inverse infinity norm <=16p^2<=p^3. This includes periodic sections,
boundary prefixes and the final cyclic-border Schur inverse. The completed
narrow operator EHC+(I-EC) is permutation-similar to H directsum I, so
identity hole coordinates preserve the conclusion.

Both physical unrounded matrices have row and column norm at most five.
For the narrow column bound, the offsets q_i-q_j in a fixed column are
distinct integers. Offsets 0,+1,-1 contribute at most 2+exp(-2a), and the
remaining tail at most 3exp(-2a); their sum is at most three. The broad
bound is the Gaussian lattice sum after alpha^-1 normalization.

For broad interiors the sections stay W away from their phase-cell and
period cuts; omitted images are genuine Gaussian tails there. Period
length alone does NOT make the row0/column(t-1) wrap entry small. Narrow
cyclic inverses use the row-gap argument, without dropping wrap entries.
The explicit boundary solver holds the first and last W physical
coordinates as a border until its final Schur solve, leaving a block
tridiagonal middle matrix. The broad F operation is a cyclic block-banded
APPLICATION and needs no such inverse.

One explicit reference-accuracy choice is as follows. A source positive
cell weight has -log2(weight)<=a/(4theta ln2)<=20p^2 ell.
A P_setup=512p+128p^2u grid gives relative error below 2^-512p.
Retained neighboring weight ratios have logarithmic change at most aW;
at the common gate 2aW<p/16. The physical Gaussian tails are at most
4exp(-64p). Rounding at most 2W+1<=3p retained coefficients per row/column
then gives the deliberately loose induced norm perturbation

~~~
||Q-Q_ideal||_(1,infinity) <=2^-60p.
~~~

The inverse perturbation identity preserves each broad interior inverse
below 2p^19<=p^20. For narrow sections the row-gap proof already applies
to Q itself. Thus the actual boundary hypotheses, with their correct
operator-specific scopes, are discharged:

~~~
Both:   ||Q||_infinity <=p.
Broad:  ||A_interior^-1||_infinity <=p^32.
Narrow: ||Q[E,E]^-1||_infinity <=p^32 for every required principal E.
~~~

The interior circuit applies a rounded shifted kernel, not Q verbatim.
Its difference from Q is charged using the same tail/reference error,
the anchored chirp range and the explicit circuit prefixes of Section 2.
Inversion adds at most two section inverse factors, each <=p^32.

The companion boundary module now supplies, including its explicit cyclic
border, completed-solve error p^1024*(1+X)*2^-F for F>=1024ell and data
temporary magnitude p^512*(1+X). The bound is independent of the number
of global windows. These are residual bounds for the specified Strassen
and block-LU realization, not assumptions about floating-point stability.

## 4. All scalar gains, working width and error propagation

Normalize **each entire completed square factor**, including its identity
block, by `2^-ceil(100ell)`. Normalizing only its active block changes the
operator and is invalid. The boundary/Schur coefficient bounds give norm
at most `p^35`, so this has ample contractive headroom. The forward and
compression factors contribute at most `1200d ell` gain bits per DFT.
The original exact Gaussian identity also has gain `2^(2alpha^2)` per
axis; since `alpha^2<=4ell`, this is at most `8d ell` bits. The safe total
per DFT is `2048d u`; for two forward transforms and one inverse it is

```
Gamma_total <=6144d u.
```

Defer every such scalar restoration to final integer recovery. The
`6144p^epsilon u` term of A_ext includes all three calls. The `2048u` term
covers the boundary `p^1024` error and `p^512` magnitude allowances.

The target tensor FFT is normalized by its final factor1/T. Before that
normalization its raw Hadamard butterfly prefixes can grow by T; this is
not automatically covered by the smaller dense-Gaussian chirp guard.
The explicit additional `2log2T` bits cover both raw target-FFT
prefix/suffix growth and the extra fractional positions exposed by the
final exact dyadic division. Charge a final return to the q-bit grid
by at most10w gates of either type per coordinate; this is included in
the whole ledger's FFT twiddle/rounding row. The normalization is not
silently counted as a free arbitrary-precision arithmetic operation:
its fixed wire shift is free in this model, its finite grid rounding
and full available word width are explicit. Each completed normalized
target FFT has norm at most one, so this T-range allowance is reused
within each source transform rather than accumulated as3log2T.

The all-size native supplier guard needs no numerical approximation.
The source recurrence `A(e)<=A(f)+P*f+E`, together with the direct leaves,
gives `A(e)<=2(P+E)e`. Zero row padding is wiring. Finishing q0 reserved C
axes directly costs at most `8q0` bits of semantic growth; conversion of
C_d to H_d via the fourth-root phase and global `(1-i)^d` costs at most
`d+1`. Both lie within the source enlarged `C0*d` guard. Thus the same
`Delta=C0*d` covers the composed occupied-batching recursion and the direct
small-d fallback, not just one uniform template call.

At q fractional bits a scalar coefficient multiplication and final grid
rounding introduce at most `8*2^(A_ext-q)` absolute error per component
when the data magnitude is at most `2^A_ext`. Propagating through a suffix
of magnitude at most `2^A_ext` gives at most
`8*2^(2A_ext-q)` per diagonal stage. H calls and native field operations
are exact; full product temporaries are charged separately.

At the common gate, `6145u^4<=p`, and three calls with 12 completed factors
and at most d groups/axis stages have no more than `100p^2<=p^3` logical
rounded stages. Here a whole banded solve is one error module, because
its local-residual theorem already covers its entire loop independently
of the number of windows. This is not a bound on the number of scalar
operations. Boundary solves contribute at most
`2p^1024*2^(2A_ext-q)` per stage. This dominates the scalar-rounding term.
Matrix reference/shifted-kernel perturbations contribute at most
`p^66*2^(2A_ext-60p)`, smaller still. A norm conversion through the full
volume can be bounded, very conservatively, by T at each of its two ends.
These estimates bound each completed source-transform error by
`e=p^1030*T^2*2^(4A_ext-32p)`, on the bounded inputs used here.

The intervening pointwise multiplication is bilinear and must also be
counted and checked. Charge four full real products of the actual operand
width and the real additions/rounding, separately from coefficient
diagonals. The exact completed normalized forward outputs have complex
magnitude at most one (indeed the digit inputs are below1/4). With forward
errors at most e<=1/8,
`|(z+dz)(v+dv)-zv|<=2e+e^2`; the final complex product grid contributes
at most `8*2^-q`. Since the displayed e dominates this last term, the
pointwise error is at most4e. The completed normalized inverse has norm
at most one, and its own error on this perturbed bounded input is at
most2e by the `(1+X)` module contract. Thus the three transforms plus
the variable products have error at most6e. The extra ten polynomial
powers below more than absorb this numerical factor and the stated
constant allowances. Combining these gives the common envelope

```
error <= p^1040 *T^2 *2^(4A_ext-32p).
```

The exponent 1040 includes the boundary 1024, three powers for the number
of logical stages, one for constant factors and four spare powers for
the stated matrix-comparison/tensor sums. It does not hide a number
depending on N or p. With `log2T<=p/128`, `1040ell<=p/16` and
`A_ext<p/16`, the error is below `2^-16p`.

For the proposed outer choice `p=256b`, `b=ceil(log2n)`,
`log2S<=b+5`, the final scale
`K=S^2*2^(2b+4+Gamma_total)` has `log2K<p/32` at the common gate.
The recovered coefficient error is therefore below `2^-15p<1/4`.
This conclusion still uses the stated integer encoding and pointwise
product interfaces; it does not assert that this note alone supplies
their operation counts or proves a first actual crossover.

## 5. Why the common gate implies every numerical guard

Let `A0=10^15`, `x=log2p`, `L=log2Mbar>=128` and `x0=A0*L`.
At x0, `x0+2<=Mbar`. The function
`(x+2)^k*2^(-c*x)` decreases for `x>=x0`, for `k<=5`, `c>=delta`:
its logarithmic derivative is `k/(x+2)-c ln2<0`.
Consequently, at and beyond the gate,

```
(2^23 p^beta u^5)/p <=2^23 Mbar^(5-3delta*A0),
2048u/p <=2^11 Mbar^(1-A0),
6144p^epsilon u/p <=2^13 Mbar^(1-delta*A0),
Delta/p <=Mbar^(8-delta*A0).
```

Here `delta*A0=5000000/7`; every displayed ratio is smaller than 1/256.
Thus the first three terms of A_ext sum to less than3p/256.
With `2log2T<=p/64`, `A_ext<7p/256<p/16`, `Delta<p/256` and
`Gamma_total<p/256<p/64`. The same monotonicity proves `1040ell<=p/16`,
`6145u^4<=p`, `W<=p`, `2aW<p/16` and `q>=1024ell` at this gate.
The script reproduces the exact rational comparisons without constructing
N, Mbar or p0 as integers. It also verifies all cached source hashes.

## Reproduction and scope

Run `pr4470_global_precision.py`. It emits
`pr4470-global-precision.json`. The script certifies only its exact arithmetic
and source-hash checks; the prose proofs are AI-assisted written derivations
without independent human review. In particular,
the community's native all-column hypotheses remain explicit assumptions.
This is a useful closure of a numerical interface in the proposed whole
algorithm. A whole-integer gate ledger and a comparison with the selected
HvH/GMP circuits must reference this interface and complete their own proofs.
