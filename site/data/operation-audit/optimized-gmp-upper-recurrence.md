# Explicit optimized-GMP upper-bound recurrence

This is a new upper-bound module for the **same** native Tiger Lake / effective
Skylake TABLE3 profile and its previously declared unbounded tail. It does not
replace the profile by schoolbook multiplication. It separates the exact
recursive-potential argument from the native compilation interface that must
also be closed before a complete numerical upper is advertised.

Write F(m) for the cost, in either gate type, of an arbitrary full product
whose two operand lengths are at most m limbs. Write T(p) for an **active
FFT** product modulo B^p+1, with valid exponent k>=5, including its
normalized representation. Small terminal coefficient products have their
own finite-leaf allowance. An odd non-FFT modular product is not silently
included in T. Here B in B^p is the radix2^64; below, the symbol L
denotes the enormous **cost** constant, to avoid confusing the two.

## Required repair of the mathematical continuation

The earlier index-only continuation needs two explicit repairs before it
is a correct arbitrary-size multiplication program. In mul_fft.c's
reconstruction loop, T[2*l]=i+1 must encode the **whole public integer**
i+1, rather than truncate it to one64-bit limb when K>2^64. At each
iteration set T to the public constant (i+1)*2^(128l), using all needed
limbs and zeros elsewhere. This uses fixed wires. It fits: M=64l and
Nprime>2M+k+2, whereas bitlength(i+1)<=k+1.

The reconstruction accumulator cc must be an exact signed accumulator.
Each of its K iterations changes it by an integer in[-2,1]; hence
|cc|<=2K throughout, and a signed2k+128-bit buffer is more than sufficient.
Its updates are explicit64-bit-limb arithmetic. Later normalization still
uses the source's final mathematical value in{-1,0,1}. No claim is made
that retaining a wrapping64-bit cc would implement the continuation.

These repairs preserve the native array add_n/sub_n calls used by the
earlier lower bound. They are part of the **repaired mathematical source
continuation**, not a claim that the original finite binary has unlimited
sizes. Their public constants and O(k)-bit scalar arithmetic fit the
nonrecursive census below.

## Exact FFT sizes and potential

On every original finite MUL and SQR selector interval, the adjacent
reproducer checks

    32 <= K_best(p) <= p/8,       K_best(p)^2 <= 256p.

All three inequalities persist in the appended tail because
K_best(p)<=2sqrt(p). Decreasing the exponent to obtain a divisor of p
preserves both upper inequalities. For an active FFT K>=32 still holds.

The initial coefficient width satisfies

    np0 <= 2p/K + K/64 + (k+2)/64 + 1.

Since k+2<=K for K>=32, multiplication by K gives

    K*np0 <=2p +K^2/64 +K^2/64 +K <11p.

The source's alignment loop was proved terminating in the prior comparison:
np<(4/3)np0<p/3. Consequently

    K*(np+1) <16p.

This also gives a source-space result: the two coefficient arrays contain
less than32p limbs. Their pointer/index arrays, the temporary coefficient,
and the optional one-input decomposition buffer bring the local FFT
payload below64p limbs. Successive active coefficient widths are less than
one third of their parent, so their live FFT payload is below96p limbs,
apart from the separately bounded finite native leaves and scalar/control
stack.

For the degree16 potential, np+1 <=(p+1)/2 for p>=400. Thus

    sum over K children (np+1)^16
       <=16/2^15 * (p+1)^16.

This is a genuine mass bound, not a bound obtained by counting only the
largest child. It includes all K independent coefficient products.

## CRT and general full multiplication

For total operand length s<=2m, the Nussbaumer wrapper chooses
nh=ceil(s/2)<=m, k0=best_k(nh), and
R=ceil(nh/2^k0)2^k0. The minus modulus is2R. For nh in the active
selector domain,

    R+1 <=(9/8)(m+1).

The minus recursion halves its modulus. Therefore its active plus FFT
roots have sizes R,R/2,R/4,..., and

    sum (root_size+1)^16 <7(m+1)^16.

For this displayed inequality, roots at or below the finite-leaf cutoff
are charged to the finite leaf budget instead. For every remaining root,
root_size+1 <=(1+1/m0)R/2^j. The exact fraction
[(9/8)(1+1/m0)]^16/(1-2^-16) is less than7. One may instead
use the looser bound8(m+1)^16, which is also sufficient below.

Above the finite-leaf cutoff, a plus branch can fail to use the FFT only
when its modulus has fewer than five factors of2. There are at most five
such plus branches. Put a=oddpart(R). The largest modulus among them is
16a. Their maximum full-product input length is at most

    16a+1 <=m/2+17.

The final odd minus branch contributes one further full product of no
larger size. Thus there are at most six large full-product restart calls,
each bounded by9(m+1)/16 when m>=2^20. For each call, the two source
operand lengths may each differ by one input-dependent high carry. To
compile a single fixed-length straightline circuit, instantiate and select
among all four public length variants. We therefore charge **24** large
F-children in the circuit potential, rather than identify worst-path
runtime with circuit size. The active FFT root's modulus and coefficient
geometry are independent of these high-carry length choices; its
nonrecursive decomposition branches are included in D below. Branches
whose sizes are below
the cutoff are charged as finite leaves, rather than as additional large
recursive children.

The general mul.c dispatcher also permits highly unbalanced inputs. If it
avoids FFT because3vn<6272 while un is large, it processes bounded-size
Toom/basecase chunks; their maximum input lengths are below2^14. The
number of chunks is at most a linear function of m. If it uses its FFT
blocking branch un>=8vn, each block has maximum length3vn, and the
remainder maximum is below3.5vn. Including an endpoint allowance, their
total (child_length+1) is at most3(m+1), and each is at most(m+1)/2.
Charging four variants here as well, even where the individual branch
has public fixed lengths, its degree16 child potential is at most

    12/2^15 * (m+1)^16.

These statements follow from the actual decrement-by2vn and
decrement-by3vn loops in mul.c. They do not assume that an extremely
unbalanced product takes the same branch as an equal-length product.

## Finite native compilation interface

The intended finite-leaf cutoff is m0=2^20 limbs. The finite class includes
the original full/modular product, Toom and native helper entry points
with all operand-size parameters below this cutoff, on their declared
workspace preconditions. Below this cutoff use
the original selected64-bit native source with the explicit finite
wide-cc wrapper above (only a few extra64-bit words at these sizes),
with successful private scratch
allocation and its standard GMP halting/correctness contracts. All selected
tables remain within their original finite entries there; no new infinite
table rule is involved. The finite original machine has at most2^64
addressed bytes. Including registers, flags, the program counter, the
private allocator and the stack, fewer than2^68 state bits suffice.

A halting deterministic run cannot repeat a complete configuration. Its
number of steps is less than2^(2^68). A canonical Boolean transition
table, followed by an output mux, costs fewer than2^(2^70) gates of either
type over the complete run. Explicitly retaining the stipulated
128AND+192XOR ADD/ADC subnetworks, with no pruning or CSE, fits below
2^(2^71). Hence the proposed common leaf allowance

    L =2^(2^72)

is sufficient **when that finite native execution/compilation contract is
adopted**. This is not a practical compiler or a measured execution count.

Complete the instruction lowering by retaining ADD/ADC as already fixed.
For every other fixed-width data instruction use its canonical Boolean
truth table. A source instruction reading/writing at most4096 data bits
has fewer than2^8192 gates of each type. Public index arithmetic remains
free as in the original circuit model. Data-dependent selection among
array locations is charged by explicit muxes.

The nonrecursive envelope is

    D(x)=2^65536 (x+1)^8.

The following census supplies its structural derivation. The transitive
selected source bodies are copied into optimized-gmp-upper-source and
hashed in the receipt. Function names generated by a common assembly
template are grouped together.

| Source operation class | Bounded control and calls |
|---|---|
| coreihwl/aors_n.asm: add_n,add_nc,sub_n,sub_nc | Eight residue handlers enter one loop; its counter decreases by eight limbs. No arithmetic helper calls. |
| coreisbr/rsh1aors_n.asm: rsh1add_n,rsh1add_nc and subtract variants | A bounded residue prefix and one loop decreasing n by four; no helper calls. |
| fastsse/lshift-movdqu2.asm,lshiftc-movdqu2.asm,rshift-movdqu2.asm | Bounded alignment/tail cases; the only backedge changes the remaining limb cursor by eight. No helper calls. |
| fastsse/com-palignr.asm | Alternative aligned, unaligned and scalar loops change n by8,16 or4. The alternatives are sequentially entered/exited; none is recursive. |
| gmp-h.in add/sub wrappers and add_1/sub_1 macros | One native n-limb pass plus a monotone carry/borrow cursor and optional remaining copy pass. |
| gmp-h.in cmp,neg,zero_p and gmp-impl.h INCR/DECR macros | A monotone array cursor; neg may make one subsequent complement pass. Valid operand/carry preconditions bound the cursor by the supplied array. |
| coreibwl/mul_basecase.asm when the shorter operand is bounded but the longer one is large | The row/column product loops have at most two array-length cursor factors; native MULX/ADCX/ADOX are charged by the fixed-width opcode rule. |

The selected arithmetic helper graph has no cycle. Its actual runtime
call depth is at most four: wrapper/inline operation to native pass or
cursor scan, with native bodies making no further arithmetic helper
calls. Static include_mpn templates are not runtime calls. There are
fewer than64 named bodies. Each path has at most two sequential array scans and at most two nested
cursor factors when wide data-dependent index updates are expanded into
64-bit limbs; the basecase product has its two row/column factors.
Use the uniform upper bound128(x+1) for every current cursor/visible
array region, including the complete coefficient arrays and their local
payload, rather than confuse a single coefficient with its containing
array.

The recursive fft_fft/fft_fftinv functions are counted separately: each
transform has2K-1 recursion-tree nodes and Kk/2 butterflies. There are at
most three transforms. Their total is polynomial even though their depth
log2K is unbounded; they are **not** included under the acyclic-helper
depth statement. Each butterfly makes a constant number of the linear
helper calls above. The decomposition has K iterations, optional public
normalization decreases dif by Kl>=1, and reconstruction has K iterations
of at most a constant number of linear scans of lengths below2(x+1).
The only data-dependent repeated carry-correction loop can run at most
twice: after an add_1 overflows, its complete target segment is zero, and
the next add_1 cannot overflow. The wide cc buffer adds a scan of O(k)
64-bit chunks, already bounded by the same cursor allowance. The minus
CRT spine has at most log2(x)+1 levels, and general unbalanced product
loops decrease the remaining input by2vn or3vn at each iteration.

These bounds give at most2^128(x+1)^4 nonrecursive helper/scalar-call
positions after treating each recursive product as a hole and charging
the finitely many source length variants. To see the coefficient, use
at most2^64 fixed instruction/control sites, four array-cursor factors
each below128(x+1), and at most16 static case variants: their product
is at most2^96(x+1)^4, below the stated2^128 allowance. A fixed native program has
at most2^64 instruction addresses. Unrolling its bounded cursor passes,
helper cases and control selection costs less than
2^256(x+1)^2 word-instruction positions per such call. The standard
data instruction truth-table cost is below2^8192. Explicit local memory
read/write muxes add a factor below2^32(x+1)^2; this also charges
input-dependent carry cursors rather than declaring them public.
Therefore their product is at most

    2^(128+256+8192+32) (x+1)^(4+2+2)
      =2^8608 (x+1)^8 < D(x).

The code/decoder allowance deliberately refers to64-bit-addressable
instruction text, not a claim that public data addresses remain64 bits.
Unbounded public index arithmetic remains free; input-dependent cursor
arithmetic and all local data selections have been charged. No OS
allocation or circuit-generation time is charged in this circuit model.

## Conditional closure once that interface is checked

The degree16 inequalities give the simultaneous induction

    T(p)<=L(p+1)^16,        F(m)<=16L(m+1)^16.

The active FFT child mass is at most1/2048 of its potential. For a full
product, the summed active FFT-root potential is below8; the six large
restart variants contribute at most16*24*(9/16)^16<1/4; and the blocking
branch contracts by12/2^15. Finite chunk leaves grow only linearly in m.
D(x) and finite-leaf costs are absorbed by the remaining allowance for
m>m0. More explicitly, even charging2^128(m+1)^4 finite leaf positions
gives at most L(m+1)^16/4 there, since
2^130<(m0+1)^12. Also D(m)<L(m+1)^16/4 follows from
65536+2<2^72 and m>=1. The finite starting cases are covered
by L. Therefore, for n-bit input operands,

    each gate count <=2^(2^73) (n+1)^16.

This final numerical theorem is conditional on the explicit native
compilation completion and the original finite GMP halting/allocation
contracts above. It is an
upper on the retained optimized source algorithm, not an assertion about
the minimum circuit for multiplication, another GMP profile, physical
runtime, or an intrinsic PR4470 crossover by itself.

All work here is AI-assisted written mathematical derivation plus exact
integer/rational checks. It is not Lean formalization or independent human
review.
