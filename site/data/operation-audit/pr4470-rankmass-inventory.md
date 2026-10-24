# A pinned-source full inventory bound D_N < 2^(9 H N)

This is a new permitted batching realization of the selected PR4470 mixed
unit, at the unchanged authenticated rank N=2^H, H=64215200000000. It retains
the source all-column native, whole-job monomial, complete spectator,
owned-storage and finite-program contracts. It does not claim a materialized
word, a practical running time or an unconditional theorem. No later-PR
width estimate is imported. The five primary files are copied and hashed
in `pr4470-rankmass-inventory-source/`, pinned to
`7c472563474e60185e6ca101a17622133d047e56`.

## Positive rank mass for the actual strictified unit

The selected joint-helper RESULT gives raw target rank mass 239886 and paid
rank mass 239134, tensor power v=1024, productive floor21 and paid cutoff20.
The chronological tensor rule in TENSOR.md, Section1, multiplies target
rank masses and paid rank masses. Thus the product's surplus is

    Delta_unit=239886^1024-239134^1024 >0.

This is an integer, hence at least one. It is not merely the raw surplus752.
TENSOR.md, Section2, completes a target of rank k<L by adding L-k to the
productive rank and paying the same L-k rank, preserving the difference.
Section3 splits paid jobs on disjoint axes, preserving their total rank.
Consequently the **completed and split unit actually used by the compiler**
has exactly this positive surplus. The selected PROOF binds these general
tensor/completion/splitting rules to its current invoice. The script checks
the exact masses and positivity without constructing N.

## Integral nested batching preserves the saving

FINITE-PRECOMPILATION.md, Section4, requires only that the replication a_n
be divisible by every smaller program width needed for source complements
and exits. Choose

    a_n=B_(n-1),     B_n=a_n S_n,

with ordinary sequential base B_n=1, P_n=n. S_n is a positive integer: the
nonempty root class has top source roles. Inductively B_(n-1) divides B_n,
so every older width divides B_(n-1). All required batches are integral.

The same source gives the exact normalized paid-leaf recurrence

    P_n/B_n=(1/S_n)[sum_s S_s P_(n-s)/B_(n-s)
                       +sum_(exit batches e,t) t P_e/B_e].

The choice a_n cancels. Strong induction from identical base programs shows
that every normalized leaf count is unchanged by this batching choice.
The same source flow, authenticated N, uniform saving and final kappa are
therefore preserved. This is a different permissible finite word; its
inventory and precision constants are recomputed rather than inherited.

## A normalized inventory that retains every child divisor

Use the completed mixed-unit budget R_star from the previously explicit
source recipe, and K=32(R_star+1). Exact integer arithmetic verifies
log2K<33010. That budget covers the unit's productive width, paid count,
raw native instances, owned banks and nonrecursive scalar/phase records.
Let I_n count completed mixed-unit instances in the unreplicated rank-n
integer flow, and let

    D_n=1+B_n+P_n+owned_n+raw_instances_n+records_n,
    Q_n=D_n/B_n,       Q=max_(e<n)Q_e.

Each complementary or exit batch containing t rank-e fields becomes a*t/B_e
copies of the smaller program. Their **full** inventory cost is therefore
a*t*(D_e/B_e). Retaining that divisor is essential. Fresh productive fields,
raw/owned/scalar records and compiler adapters give the same conservative
budget as before:

    D_n <=1+a I_n[12R_star+2R_star Q] <=a I_n K Q.

For the last inequality Q>=1 and aI_n>=1 suffice; indeed
1+12R+2RQ<=32(R+1)Q. Child owned fields and internal records are in D_e;
they have not disappeared through normalization. Per-productive-field
adapters also remain paid: their count is copies*B_e=a*t, covered by the
fixed source/paid-edge budget. One owned bank per expanded live unit is
allowed; no unproved storage reuse is used.

Dividing by B_n=a S_n yields

    Q_n <=K (I_n/S_n) Q.

## Local first-moment telescope

Each integer-flow unit is at a positive integer column count c. Its net
rank potential is Delta_unit*c. Equal-rank internal job matches cancel,
leaving exactly

    Delta_unit * sum_unit_instances(c)
        = sum_top_source_jobs(rank)-sum_exit_jobs(rank).

All exit ranks are nonnegative, all source ranks are <=n, and every c>=1.
Thus

    Delta_unit I_n <=n S_n,       I_n/S_n<=n/Delta_unit<=n.

This is a telescope in the original finite integer flow, before inserting
smaller uniform programs. It uses the completely charged paid inventory
and exact rank matches, rather than a moment-root approximation. Consequently

    Q_n <=K n max_(e<n)Q_e.

In the sequential base Q_n=n+2<=K n<=K N for n<=N. Strong induction gives
Q_n<=(K N)^n throughout 1<=n<=N, hence

    log2Q_N <N(33010+H).                              (1)

## A direct width upper bound from the same source

The source flow's multinomial sum gives

    I_n <=sum_(j=0..G_n)P_raw^j B_raw^(G_n-j)
        <=(B_raw+P_raw)^G_n <=K^G_n,
    S_n <=B_raw I_n <K^(1+G_n).

The completed minimum productive rank is L=21^1024. The exact bit-length
check gives L>=2^4497. Every eligible height obeys L^G_n<=n, so for all
n<=N=2^H,

    G_n<=H/4497.

Nested batching is a product of source counts (base widths are one).
Therefore

    log2B_N <33010 N(1+H/4497).                       (2)

Combining D_N=B_N Q_N with (1) and (2),

    log2D_N <N[33010(2+H/4497)+H] <9HN.

The final strict inequality is an exact rational comparison at the actual
H. Equivalently it is 66020*4497<2966H, verified in the script. Thus

    D_N < Mbar=2^(9HN).

This one inventory ceiling covers productive width, all rank-one paid
children, raw instances, owned fields and nonrecursive scalar/adapter
records. It is not itself a runtime coefficient or semantic guard: those
are recomputed from these counts by their separate formulas.

For comparison only, retaining I_n<=K^floor(log2n) without the mass telescope
also proves D_N<=K^(2q_N), where q_N=(H-1)N+H+2. The new bound improves
that fallback using two additional **pinned-source** facts: positive first
moment for the strictified unit and minimum productive rank21^1024.

`pr4470_rankmass_inventory.py` verifies the five primary hashes, strictified
mass positivity, minimum target rank, exact K bound, 10,000 logarithm-sum
identities, 99 power-of-two formulas, 196 rational fresh-budget inequalities
and the final 9HN comparison. These checks support the written conditional
proof; they are not Lean verification or an emitted huge algorithm.
