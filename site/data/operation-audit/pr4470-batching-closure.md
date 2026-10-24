# Occupied batching and an all-size Gaussian supplier bound

This closes the batching/stock and stopping-base costs for one completed
canonical selected-axis Gaussian operation in the declared XOR–AND circuit
model. **It is an explicit circuit-work bound, not just a field inventory.**
It applies to one coefficient array, including an array encoded from one
integer input: the supplier's productive roles are existing row fibers of
that array. They do not require multiple unrelated integer inputs.

The source all-column operator identity, arbitrary complete spectators,
owned-bank discipline, and whole-job binary monomial interface remain
assumptions. This argument does not independently verify them or complete
the remaining outer phase/encoding/recovery proof.

## Parameters and the counted model

Use the fixed source rank N=2^H, H=64,215,200,000,000, and the complete
uniform program's W productive roles and P rank-one paid children. The
authenticated endpoint has

```
eta = 528527/175000000,
sigma = 1-eta,
P/W < N^sigma.
```

Set `beta=1/1400000000`, the current stopping parameter, and

```
s = sigma + beta*(1-sigma)
  = 244260062200528527/245000000000000000.
```

Thus the Gaussian-axis saving is exactly
`1-s=739937799471473/245000000000000000`.
The source result and rank are pinned in
[`joint-helper-lattice/RESULT.json`](https://github.com/CrocSwap/integer-mult-bounds/blob/7c472563474e60185e6ca101a17622133d047e56/research/joint-helper-lattice/RESULT.json).

Let M=`[32(R*+1)]^(4^N)` be the fully charged inventory upper bound proved
in `pr4470-compiler-bound.md`. Put

```
A = 33010*4^N >= ceil(log2 W),
G = 10^9 U_raw + 8R < 2^30 M.
```

Here G bounds real scalar/phase primitives in the whole finite word.
The component width w includes all guards. If w<=2p, a real ADD or NEG
uses at most 8p gates of either type, and one Gaussian axis uses at most
40p gates per complex coefficient position. These are conservative bounds
from the explicit macros. Fixed wiring, copying, fanout, public index
arithmetic and circuit generation are free. Scalar data arithmetic and
fourth-root signs are charged. XOR costs rho>=0; AND costs one.

## The original array supplies occupied productive rows

The source stock construction is in
[`FINITE-TEMPLATE-CLOSURE.md`, section 5](https://github.com/CrocSwap/integer-mult-bounds/blob/7c472563474e60185e6ca101a17622133d047e56/research/kappa-rebuild/transfer-audit/FINITE-TEMPLATE-CLOSURE.md).
For d selected Gaussian bits define

```
D(d)=0 if d<N, otherwise1+D(floor(d/N)),
a=ceil(log2 W), q0=a D(d).
```

Reserve q0 selected row coordinates, leaving their Gaussian kernels
unfinished. A complete neighborhood chunk may contain additional spectator
bits; it still contains just one of these selected Gaussian bits. If a
chunk has K>=1 bits, its row-field cardinality is
`R0=2^(q0 K)>=W^D(d)`.

These rows already occur in the complete coefficient array. At the root,
group them into W distinct physical role streams. At the next level each
child uses one of these streams and its remaining row fibers. Values in
different rows may be correlated functions of one integer input, or zero;
the native identity accepts every assignment to distinct slots and does
not require statistical independence. Calls on an owned center are covered
by that same arbitrary-input identity and its separately allocated bank.

Pad the complete row count once to the next multiple of W^D(d). Since the
old count is at least W^D(d), padding has factor below two. Every descendant
then has exactly 1/W of its parent's productive coefficient volume and
enough divisibility for its remaining depth. The final block-diagonal
Gaussian endpoint returns every appended zero row to zero, so padding can
be removed before an external diagonal or another phase.

No statistical input copy receives productive credit. No padding factor
accumulates at every recursive level.

## An explicit reserve threshold

Since N>=2, `D(d)<=log2 d`, whence `q0<=A log2 d`. For every

```
d >= 64(A+1)^2
```

this is strictly less than d/4. At the endpoint, use
`log2[64(A+1)^2]=6+2log2(A+1)<=6+2A`; its product with A is smaller than
`16(A+1)^2`. The function `d/log2 d` increases beyond this endpoint, proving
the claim for every larger d, not just sampled sizes.

Also require `d^beta>=2N` to ensure every internal floor child has positive
width. Define the concrete integer cutoff

```
d0 = max(64(A+1)^2, (2N)^1400000000).
```

Both terms are at most M. Indeed log2K>=5 gives log2M>=5*4^N. The first
term has logarithm below `40+4N<5*4^N`. For the second, H>=32 and
1400000000<2^31 give `(H+1)1400000000< N^2<=4^N`. Thus **d0<=M**.

## Count the stopped tree with its actual occupied volume

Fix the original d throughout the invocation and stop a node of selected
width e when `e<d^beta`, equivalently `e<ceil(d^beta)`. Reserve stock outside
the active e=d-q0 coordinates. All descendants use the already reserved
global row field; they do not reserve another fraction of their target axes.

Normalize circuit work by `p(1+rho)` times the node's complete productive
coefficient volume. An internal call costs

```
c(e) <= (P/W)c(floor(e/N)) + 8G/W + 40N.
```

The first term accounts for **all** P children, each of volume 1/W.
The whole finite scalar/phase word has volume-normalized cost 8G/W.
At most N-1 remainder axes receive ordinary kernels, charged by 40N.
Owned-bank work is included in G and paid children on those banks are in P.
An elementary leaf has `c(e)<=40e`.

Put q=N^sigma>2. Replacing P/W by q is an upper bound. If the stopped tree
has depth J, its last internal width is at least d^beta, so

```
q^J <= q d^(sigma*(1-beta)).
```

The weighted internal-node sum is at most q^J and each leaf has width less
than d^beta. Since q<=N, their total normalized work is at most

```
N(8G+40N+40) d^s.
```

The reserved Gaussian kernels must also be completed. Perform their q0
elementary selected-bit kernels after the active completed endpoint, within
the same full canonical Gaussian job and **before** any external diagonal.
Canonical Gaussian factors on disjoint coordinates commute. The other
neighborhood bits remain spectators. This charges at most40q0; using
`log2 d<=2sqrt(d)` and s>1/2 gives `40q0<=80A d^s`.
There is no free deferral across an uncommuted external phase.

Including the one-time padding factor below two gives coefficient

```
C_active = 2[N(8G+40N+40)+80A].
```

For d<d0, use all individual Gaussian kernels. Their 40d charge is at most
`40d0^(1-s)d^s<=40M d^s`. This explicitly covers every stopping/base size.

## A uniform numerical coefficient

Because `G<2^30 M` and N,A<=M,

```
C_active <2^35 M^2,
40M <=2^35 M^2.
```

Let V be the number of complex coefficient positions in the original
complete array, before padding. For **every integer d>=1** the completed
Gaussian operation has

```
AND <=2^35 M^2 p V d^s,
XOR <=2^35 M^2 p V d^s,
weighted work <=2^35 M^2 p(1+rho) V d^s,
```

provided the global precision construction guarantees w<=2p and the common
fine grid is sufficient for exact native arithmetic.

There is also a version avoiding that width condition: for any sufficient
working width w>=2, real primitives cost at most4w per gate type and a
Gaussian axis at most20w. These halve the earlier 8p/40p tariffs, so the
same proof gives the stronger width-based coefficient

```
weighted work <=2^34 M^2 w(1+rho) V d^s.
```

One can substitute an explicit external-phase width w(p) into this version.
This is a runtime coefficient derived from counted gates; C0 remains a
separate semantic-precision constant.

The ordinary unnormalized Walsh–Hadamard operation H_d is also covered.
Writing S=diag(1,i), direct 2-by-2 multiplication gives
`S C S=((1+i)/2)H_1`; tensoring gives the same identity with scalar power d.
Thus H_d uses two fixed fourth-root diagonal maps and global factor
`(1-i)^d` around C_d. That global factor is a fixed shift and fourth-root
phase, with one additional factor1-i when d is odd. It adds at most two
real ADDs and seven NEGs per coefficient coordinate, costing at most20w
of either gate type. A sufficient bound for each gate count is therefore

```
(2^34 M^2+20) w V d^s.
```

For the new protected precision width w<=33p, this is less than
`2^40 M^2 p V d^s`, since `33(2^34+20)<2^40` and M>=1. This includes the
conversion arithmetic and its fixed numerator shifts; their precision
guard must be included in the common 33p allocation.

The proof completes the single-array canonical Gaussian interface. It does
not equate d, V or w with the integer input length n. The remaining whole
multiplier requires its total Gaussian-stage count, external coefficients
and approximation/recovery guards, boundary arithmetic and other outer
operations. Those interfaces cannot be supplied by multiplying this bound
by an unspecified asymptotic constant.

The same source semantic guard C0*d applies to this all-size realization.
Let B_constant=P+E>=64. The source completed-child recurrence
`A(e)<=A(floor(e/N))+P floor(e/N)+E`, with elementary leaves A(e)<=8e,
proves A(e)<=2B_constant e for any stopping threshold whose internal floor
children are positive. Zero-row padding and repacking change neither
magnitude nor denominator exponents. After the active C_(d-q0) returns,
its completed excess in either measure is at most d-q0. Direct stock
completion adds at most8q0 temporary excess, bounded by8d<=2B_constant d.
The small-d direct fallback has the same bound. Finally the two S phase
maps preserve exponents; the collapsed integer factor(1-i)^d adds no
denominator and at most d+1 temporary magnitude bits. After completed C_d
this is at most2d+1<=3d<=2B_constant d. Thus both the all-size C_d and H_d
calls remain below `(2B_constant+18)d<C0d` relative to their incoming
common fine grid and magnitude. This justifies using the same C0*d inside
the separate global precision calculation; no child is rounded at return.

`pr4470-batching-closure.py` writes the JSON certificate and checks exact
parameters, 140 occupied-row divisibility/padding cases, and27 exact
rational stopped-tree examples. The displayed general inequalities are
the proof; these checks detect transcription errors.
