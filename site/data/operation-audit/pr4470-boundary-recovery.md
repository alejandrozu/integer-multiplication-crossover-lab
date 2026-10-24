# PR4470: explicit boundary, halo, normalizer and integer-recovery modules

Source pin: `7c472563474e60185e6ca101a17622133d047e56`. The adjoining JSON and
`pr4470_boundary_recovery.py` contain exact integer counts and executable finite
checks. The explicit cyclic-border solver is closed in this module under
the operator-specific hypotheses below. This is a new explicit realization
of the retained construction. It
uses its actual five-factor identities, original physical bands and concrete
Strassen recursion; it does not treat unspecified source O-constants as numeric.
The upstream analytic identity and precision premises remain visible below.

The arithmetic model is the parent's `xag-straightline-v1`: AND costs one,
XOR costs rho>0, and size-only constants, fanout, wiring and permutations are
free. Bounds called “per type” apply separately to AND and XOR before weighting.
`C_HvH` is the previously proved explicit per-type HvH upper-envelope constant.

## 1. Which source and matrix branch this uses

The live outer package is
`research/kappa-observation-integration/release-work/current/package`, reached
from `research/kappa-rebuild/transfer-audit/outer_transfer_audit.py`. Its vendored
PR1786 fine-prime note is byte-identical to the other cached PR1786 copy:
SHA256 `47d1b1b4df28aadda3cd6bdeb1fbc47290595e9208cd09c1a1f338520d33fdce`.
The selected numerical point is instead the later joint-helper-lattice
`RESULT.json`: kappa=.00302015, delta=1/1400000000, epsilon=1-delta,
beta=1-3delta. Historical numerical examples in the vendor are not substituted.

The selected boundary is **explicit Strassen**, with tau=45/16 and
c=(3-tau)/2=3/32; `7^16<2^45` is an exact integer inequality. The optional
omega<=9/4 branch in an older appended note is not needed. The selected
fine-prime interval gives theta<=p^-2; phase cells have order p^2, and chirp
guards involve a*B^2/p^2. The old linear a*B guard is not reused.

Pinned links and hashes for the five-factor, halo, current composition, union,
fine-prime and gauge-free source files are in
`pr4470-boundary-recovery-source/manifest.json` and the JSON `sources` field.

## 2. Dyadic carving with explicit support counts

Let a physical target line have t coordinates and H holes in its q-image.
Its selected coordinates have at most C=H+1 contiguous phase runs. Let W be
an upper half-bandwidth for either augmented matrix, and choose a dyadic cap
B>=2W. On each selected run reserve W coordinates at both ends. Repeatedly
take an interior of size B followed by W boundary coordinates while it fits.
For the final remainder r<B+W, while r>2W take the largest power of two at
most r-W followed by W boundary coordinates. The remainder then decreases
by at least half. Mark the final remainder boundary. Very short runs are
entirely boundary. Thus every interior is dyadic, at most B, and different
interiors are separated by W physical boundary coordinates.

Writing ell_B=log2 B, the interior count I, boundary size J and sparse active
size E obey

    I <= floor(t/B)+C(ell_B+2),
    J <= H+W[floor(t/B)+C(ell_B+6)],
    E <= J+2WI
      <= H+W[3floor(t/B)+C(3ell_B+10)].

Sizes may always be clipped to t. The active set includes every boundary
coordinate and all interior coordinates incident to a boundary/interior
coupling. The formulas also cover physical period cuts by treating the cut
as the two ends of the line; every core can be carved independently if
desired. Carving may differ from the author's implicit tie conventions,
while implementing the same capped decomposition and retaining its powers.

An eliminated interior couples only its two neighboring W-boundary groups.
Its Schur fill therefore has compressed boundary half-bandwidth at most 2W,
with cyclic wrap across the physical period cut.
The original B_1,C_1 coupling matrices, after compression to E, have
half-bandwidth at most W: deleting coordinates cannot increase index
distance. Put q=2^ceil(log2(2W)); then 2W<=q<4W. Both kinds of matrices are
cyclic block banded at q-coordinate block size, including clipped last blocks.

## 3. Full boundary kernel invocation ceiling

For the block decomposition Q=[A B_1; C_1 D_1], F=D_1-C_1 A^-1 B_1, the source
identities are

    Q^-1 = diag(A^-1,I) E_-B_1 diag(A,F^-1) E_-C_1 diag(A^-1,I),
    Q    = diag(A,I) E_C_1 diag(A^-1,F) E_B_1 diag(A,I).

The broad forward identity uses F as an application, not an inverse. The
narrow compression identity uses F^-1. All coefficient factorization is
size-only synthesis in the selected model. A q-wide batch is paid in full
even when the final batch is partly occupied. Let m be the actual number of
right-hand-side fibers, z=ceil(J/q), e=ceil(E/q), r=ceil(m/q).

For the **narrow** F^-1, retain the first and last W physical coordinates
as a border until the last elimination. There are at most 2W<=q such
coordinates. This is essential: merely labeling the period cut “boundary”
does not remove its significant cyclic couplings. With this border last,
the other boundary coordinates form an ordinary block tridiagonal matrix
A_0. Each border coupling touches at most three q-blocks (the first block
and the last two possibly clipped blocks).

An ordinary block tridiagonal solve on z blocks uses 3z-2 products and
2z-2 additions: forward substitution costs z-1 products, and backward
substitution costs 1+2(z-1), using fixed diagonal inverses. Solve the bordered
system by (i) y=A_0^-1 Y_A, (ii) solve its at-most-q border Schur matrix
against Y_B-Cy, and (iii) x_A=A_0^-1(Y_A-Bx_B). This costs at most 6z+3
products and 4z+2 additions, after charging both border couplings and both
ordinary solves. For z=0 the border is solved directly and the bound below
still covers it.

The **broad** F is only applied, never inverted. Its cyclic half-bandwidth
2W has at most five nonzero q-blocks per block row, hence at most 5z
products and 5z additions. Each original B_1 or C_1 shear has cyclic
half-bandwidth W and at most five nonzero q-blocks per row, including clipped
end blocks; it costs at most 5e products and 5e additions including its
accumulation. There are four such shears across forward plus compression.
Conservative combined counts, when E>0, are consequently

    matrix products <= r[12(z+1)+20e],
    matrix additions <= r[10(z+1)+20e].

Since 1<=z<=e, both are at most 48re. If E=0 there is no sparse work.

In this circuit realization, apply one sparse axis factor to all its
other-coordinate fibers, batching by fixed wiring and then restoring their
locations. Axis factors at the same tensor stage commute, so doing them
one axis at a time is valid. Consequently m=R/t is the whole-array RHS
count, not the size of one union-flag class. No claim that every flag class
has q RHS is required. The source's tape union scheduling can be omitted
because its movement is fixed wiring in this model.

These are counts of q-by-q products on complete q-RHS batches, not per-entry
scalar products. The source's fast boundary exponent is preserved. The
three dense A stages in each five-factor identity are a separate bill;
this module does not silently charge or discount them here.

Canonical Strassen on q=2^k has exactly 7^k complex scalar products and
6(7^k-q^2) complex sums/subtractions. The previously counted fixed-width
complex product/sum interfaces consequently give per-type cost

    Product(q,w) <= 7^k[4 C_HvH w max(1,log2w)+100w]
                    +96w(7^k-q^2),
    MatrixAdd(q,w) <= 16w q^2.

### An explicit simplified boundary row

Let ell=ceil(log2p), p>=2^20, and choose Gaussian truncation bandwidth
J_0=ceil(sqrt(256p ell)). The augmented physical half-bandwidth
W=2J_0+2 satisfies W<=36sqrt(p ell) and W<=p. Assume

    p^xi/2 <= B <= p^xi <= p^2,  B>=2W,
    t>=p^4,  m>=q,  theta<=p^-2.

In any interval, H<=t/p^2+2 and C<=H+1. The previous exact count implies

    (E+q)/t <= 32(ell+2) W/B.

Using r<=2m/q, z,e<=E/q+1, q<4W, tau=45/16 and R=tm, the whole per-axis
boundary bill is at most

    2^26 R(ell+2)^2 p^(29/32-xi)
          [4 C_HvH w log2w+212w].                       (B1)

For example if the upstream precision audit supplies w<=256p, then

    (B1) <= 2^39 C_HvH R p^(61/32-xi)(ell+2)^3.       (B2)

Summing over d<=p^epsilon axes yields the expected saving
3/32+xi-epsilon relative to R*p*p. Constants 2^26 and 2^39 are explicit
ceil/Strassen/width ceilings, not guessed O-constants. Parent capacity bounds
give R*p<=8192n for its proposed outer instantiation. Its common giant
starting gate must separately establish t>=p^4, m>=q and w<=256p.

## 4. Numeric precision bound for the local boundary and halo solves

This module needs the following analytic premises for p>=2^20. Both broad
and narrow reference matrices have induced-infinity norm <=p. For the broad
forward map only the **nonwrapping contiguous interior A blocks** require
inverse norm <=p^32; the period cut is excluded from interiors, so finite
LDU applies. No inverse or LU-prefix bound for a full periodic broad matrix
is required or asserted. For the narrow compression, every periodic or
principal restriction inherits row gap >=1/(16p^2), hence inverse norm
<=16p^2<=p^32. This covers all its prefix, separated-interior and border
Schur inverse obligations. It also covers the full periodized endpoint.

Every relevant Schur matrix has norm <=p+p^2*p^32<=p^35, and its inverse
is a principal block of an inverse and has norm <=p^32. For block LU,

    ||L||,||L^-1|| <= p^68,     ||U^-1|| <= p^100.

For L^-1 the exact j-th partial RHS is
Y_j-F_{j,left} F_left^-1 Y_left; its row norm is at most
1+p^35*p^32<=p^68. L itself is bounded from its identity and multipliers
F_j,j-1 U_j-1^-1. Finally U^-1=F^-1 L. These bounds are independent of the
number of block rows. Fixed boundary coefficient entries are at most p^68.

Suppose all stored coefficient entries and all rounded real results have
absolute error <=2^-F. Hardwire Strassen's fixed-operand linear forms to
this precision. The data forms have at most q original terms and the
recombination has at most q^2 signed leaf occurrences. Direct summation
of coefficient, data-form, product-rounding and recombination errors gives

    product entry error <=16 q^4 p^68(1+X)2^-F
                        <=p^90(1+X)2^-F,

when every input data component is bounded by X; q<=4p and p>=2^20.
Converting the back-update's output error to its triangular-system residual
multiplies by a pivot norm <=p^35. Include block sums and complex components
in the conservative common local residual ceiling p^128(1+X)2^-F.

Here is a short absorption proof, rather than multiplying a local error by
the global number of windows. Let delta_f be the largest forward block
residual, delta_b the backward residual, X the initial RHS magnitude. Using
the exact triangular inverse bounds,

    ||y'|| <= p^68(X+delta_f),
    delta_f <=p^128 2^-F(1+||y'||),
    ||x|| <=p^100(||y'||+delta_b),
    delta_b <=p^128 2^-F(1+||x||+||y'||).

When F>=512ell these inequalities absorb their small self terms, giving
delta_f<=p^199(1+X)2^-F, delta_b<=p^300(1+X)2^-F and ||y'||<=p^70(1+X),
||x||<=p^172(1+X). Consequently

    ||x_computed-F^-1Y||
       <=p^100[p^68*p^199+p^300](1+X)2^-F
       <=p^512(1+X)2^-F.                              (P1)

The largest Strassen temporary in this ordinary solve is at most
q^4*p^68*p^172(1+X)<=p^256(1+X).

For the narrow cyclic border, all coefficient/coupling norms are <=p^35,
and both A_0^-1 and the final border Schur inverse are <=p^32 by the narrow
principal/periodic premise. Taking F>=1024ell, the first computed solve y
has magnitude <=p^33(1+X), its boundary RHS <=p^69(1+X), the computed border
solution <=p^102(1+X), and the second interior RHS <=p^138(1+X). Propagating
the preceding p^512 error bound through these three operations gives,
successively, boundary-RHS error <=p^548(1+X)2^-F, border-solution error
<=p^581(1+X)2^-F, second-RHS error <=p^617(1+X)2^-F and final error
<=p^652(1+X)2^-F. Intermediate scalar products are bounded by
p^256*p^138(1+X)<=p^394(1+X). Therefore the common conservative module bounds
are

    complete cyclic solve error <=p^1024(1+X)2^-F,
    all intermediate magnitudes <=p^512(1+X),
    sufficient extra fractional/magnitude guards: 1024ell and 512ell.

The 512ell/256ell ordinary-solve bounds above remain useful internally.
These are deliberately loose polynomial bounds, in addition to global
inter-factor amplification; they are not a whole-pipeline precision proof.

## 5. Completed normalizers and halo invocation counts

Forward Q has five completed factors; compression Q^-1 has five and then
one selected-row diagonal normalization. Count /4 separately if desired:
at most twelve completed maps per axis. Their square-map norms are at most
p^35 under the preceding premises, including direct sums and identities.
Divide the **entire map**, including identity banks, by
2^ceil(100log2p) and record the scale. This gives an extra exact shift

    Gamma_extra <=1200 d ell.

Scaling only an active block and leaving its identity bank unscaled would
change the matrix identity and is not permitted. This bound covers these
new normalizers only; an inherited Gaussian recovery scalar is additional.
These counts are for **one completed source FFT**. Ordinary cyclic integer
convolution uses two forward and one inverse source FFT, so its boundary and
halo bills below are multiplied by three. If their normalizers are all
postponed until final recovery, the extra shift is <=3600dell: the two
forward scalings multiply and the inverse scaling contributes the third.
Under the retained old scalar identity 2^(2alpha^2) per axis and the new
M/4 rather than S/2, the inherited part is <=51dell across all three
transforms, since alpha^2<=8ell. Then Gamma<=4000dell is conservative.
This last scalar identity in the fine-prime domain is an upstream obligation.

Let core side L_c=2^ceil(128log2p), halo A=p^48, group size h, and R the
full complex coefficient volume. The source first-exceptional-axis face
partition has copied input volume exactly

    M =3R[(1+2A/L_c)^h-1] <=12RhA/L_c,

provided 4hA<=L_c. All corner duplication is already counted. Position
dependent coefficients use the actual destination windows and physical
period cuts, as the capped note explicitly prescribes.

An explicit sparse one-axis implementation can use precomputed ordinary
banded LU on the original reference principal window, instead of invoking
the fast dense boundary engine. Forward substitution, back substitution
and diagonal inverses use at most (2W+1) complex products and 2W complex
sums per coordinate. Broad forward application has the same ceiling.
Successive cropped h-axis passes process volume at most M at every pass:

    complex products <=(2W+1)hM,
    complex additions <=2WhM.

Thus a group costs per type at most

    36R h^2 A W/L_c [4C_HvH wlog2w+212w].             (H1)

With w<=256p, W<=p and sum_group h=d, h<=g, the total is at most

    2^19 C_HvH R d g p^-78 ell.                      (H2)

The original fine-prime p^48 halo remains sufficient here because **only
the narrow inverse** needs inverse locality: its row gap >=1/(16p^2),
row norm<2 and inverse row norm <=16p^2<=p^3. Write H=I-E. Directly in
induced-infinity norm, ||E||<=1-1/(16p^2). The first J=p^6 Neumann terms
leave tail at most 16p^2 exp(-p^4/16)<2^(-p^2) for p>=2^20. Their
physical bandwidth is at most JW<=p^7, well inside p^48. This argument
does not infer a spectral norm bound from a row norm.
The broad forward map is already truncated banded. One must not derive
p^48 locality by incorrectly reusing the old p^10 generic norm estimate
for a larger current broad inverse. The local solve's numerical errors
are bounded by (P1); locality truncation is a separate upstream budget.

## 6. Exact normalization and carry recovery for a specified FFT interface

The parent proposes a concrete instantiation: b=ceil(log2n),
p=256b, L_in=ceil(n/b), radix B=2^b, dyadic target T>=8L_in and distinct
prime product S>T/2>2L_in. Input digits are scaled by 2^(-b-2). This
section is an exact recovery module **conditional on** the resampler really
delivering normalized cyclic convolution. It does not transplant the old
finite Gaussian proof's parameter domain into the fine-prime domain.

Let c_j be the ordinary integer convolution coefficients, j<2L_in-1, and
let Gamma>=0 be the total tracked additional dyadic normalization. Suppose
the final real output satisfies

    z_j=c_j/K+e_j,  K=S^2*2^(2b+4+Gamma).

The cyclic product is ordinary because its degree is <2L_in-1<S. Allocate
analytic error <=1/(8K) and final grid error <=1/(8K). A sufficient grid is

    F>=2ceil(log2S)+2b+Gamma+8.

Then nearest integer to K*z_j is exactly c_j, with a strict quarter-unit
margin. Recover this by a **charged exact multiplication by integer S^2**,
the fixed dyadic wiring shift, adding one half, and an arithmetic right
shift. S is generally odd: multiplication by S^2 is not a free dyadic
shift. The imaginary part is unused after the upstream error guarantee.

If w bounds the signed fixed-point numerator and S^2, unsigned HvH supplies
the full 2w-bit product. Conditional absolute value uses at most w AND and
2w XOR; final conditional negation at width 2w uses 2w AND and 4w XOR.
The half-add at width 2w uses at most 4w AND and 6w XOR. Hence recovery
costs at most U_HvH,g(w)+12w of either type per retained coefficient.

For a sufficient explicit word condition take
w>=max(F+1,v+1,2ceil(log2S)+1), with v as below. The correct coefficient
range and D=2b+4+Gamma>=6 then leave ample signed headroom for the half-add
in the full 2w-bit product. The 33p upstream guard bounds operands and
native data words; it does not assert that the multiplier helper's full
product or every internal helper wire is restricted to 33p bits.

Set v=2b+ceil(log2 L_in). Because c_j<=L_in(B-1)^2 and induction gives
carry<=L_in(B-1), every c_j+carry is <L_in B^2<=2^v. Sweep 2L_in positions,
using c_{2L_in-1}=0: add the v-bit carry, emit the low b bits, and use
the remaining bits as the next carry. Final carry is zero because the
product is <B^(2L_in). The last unused high output bits may be discarded
by fixed wiring. The total is bounded by

    AND <=(2L_in-1)[U_HvH,AND(w)+12w]+4L_in*v,
    XOR <=(2L_in-1)[U_HvH,XOR(w)+12w]+6L_in*v.        (R1)

Packing input chunks is fixed wiring, not data arithmetic in this model.
The exact test script checks perturbed rational recoveries, including zero
coefficients and negative approximate zero, then reconstructs full products.

## 7. What these results establish and what is upstream

The exact integer invocation counts, halo geometry, concrete Strassen
arithmetic, conditional finite-width residual lemma and coefficient/carry
recovery are now specified numerically. The run reports 8,192 carvings,
448 halo geometries, 1,728 exact recoveries, 11 Strassen recurrences,
281 bandwidth inequalities, 24 exact rational cyclic-border solves and
13,520 cyclic block-row counts: 24,204 arithmetic checks, plus 12 cached
primary-source SHA256 checks. These are finite checks, not formal proofs of
the analytic premises.

To form a complete PR4470 whole-multiplier certificate, the parent must bind
this module to (i) the new fine-prime Gaussian identity and its admissible
domain, (ii) the physical finite-section norm premise, (iii) the full global
precision and inherited recovery scalar, (iv) occupied dense supplier
batching and (v) an effective common n gate. The boundary counts and exact
recovery circuit are useful positive modules even if one of those remaining
source premises needs repair. No finite PR4470-vs-HvH/GMP crossover is claimed
by this note alone.
