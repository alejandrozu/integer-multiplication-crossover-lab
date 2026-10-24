# An explicit HvH circuit envelope

This note derives bounds for **one specified, unoptimized circuit realization** of Sections 2–5 of Harvey–van der Hoeven, [*Integer multiplication in time O(n log n)*](https://www.texmacs.org/joris/nlogn/nlogn.pdf). It is a new counting argument, not a constant stated in that paper, a minimum-complexity claim, a count of a practical HvH implementation, or a PR4470 crossover certificate. The accompanying script checks exact arithmetic and small realizations of the helper algorithms. This is a mathematical derivation with executable checks, not a Lean proof or an emitted circuit at astronomical sizes.

## Model and result

Use `xag-straightline-v1`: size-specialized Boolean straight-line circuits; two-input AND costs 1 and XOR costs rho>0. Literal constants, wires, fanout, and fixed permutations are free. All coefficients depending only on input length are hardwired to the same fixed-point values prescribed by the source algorithms. Circuit generation, finding the primes, transcendental constant generation, routing, memory, and uniform Turing-machine overhead are excluded. Input-dependent arithmetic, clipping, comparisons, selections, division and square root are included.

To make the lower bound reproducible, every adder uses full cells, including the first cell and the unused final carry. On w bits:

* ADD: 2w AND, 3w XOR.
* SUB (invert the second input, then ADD with carry 1): 2w AND, 4w XOR.
* MUX(a,b,c)=a XOR ((a XOR b) AND c): w AND, 2w XOR.
* Conditional two's-complement negation: x XOR sign-mask followed by ADD(carry=sign), at most 2w AND, 4w XOR.
* OR-reduction/zero-test: at most w AND, 2w XOR, since OR(a,b)=(a XOR b) XOR (a AND b).

Set d=1729, E=d^12=713739807325663489766475852620783120641, n0=2^E. Below n0 use schoolbook multiplication. For n>=n0 use the paper's main construction (not its Section 5.4 optimization sketch). Let L=log2(n), b=ceil(L), p=6b, choose T and r as the unique powers of two in [4n/b,8n/b) and [T^(1/d),2T^(1/d)), and Q=T/r. The paper supplies distinct primes s_i and powers of two t_i with product(s_i)=S, product(t_i)=T, t_d=r and T/2<S<T (pp.36–39).

For each gate type g independently, a constructive upper envelope U_g satisfies

    U_g(n) <= 5n^2 (AND) or 6n^2 (XOR),              1<=n<n0;
    U_g(n) <= 12Q U_g(3rp)
              +1024 d^2 T ceil(p^(3/4)) U_g(4p+8)
              +10^6 d^2 T p^2,                      n>=n0.

Unused helper-call slots may be omitted; the recurrence is an upper bound, not an exact count. Both child lengths are strictly smaller than n. A closed bound resulting from this recurrence is

    U_AND(n), U_XOR(n) <= C n max(1,log2(n)),
    C = 6914 * 2^30 * d^2 * 2^E.

Consequently this fixed realization has weighted work at most C(1+rho)n max(1,log2(n)). For n>=n0, its unsimplified FFT core also gives the lower envelope

    AND(n) >=216 n log2(n),  XOR(n)>=378 n log2(n).

The upper and lower bounds refer to the same canonical realization, but are very far apart. The lower bound does not apply to every possible HvH optimization. These bounds do not yet compare PR4470 with HvH: a complete PR4470 upper envelope in this model is still needed.

## Typed source-level census

Each main multiplication uses three prime-size transforms (two forward, one inverse), their pointwise products, and scaling (Prop.5.3, p.40). Each prime transform uses Gaussian maps A,B around one power-of-two transform (Prop.5.2, p.39). Bluestein converts that transform into one complex convolution; twisting converts this into a ring convolution (pp.21–22). Each ring convolution has three synthetic FFTs and Q ring products (pp.19–21). Lemma2.5 implements each ring product by four integer products at length 3rp (p.14). Thus the main node contains:

* **9** synthetic multidimensional ring FFTs;
* **3Q** ring products;
* **12Q** unsigned integer products with padded operand length **3rp**;
* **15T+S** scalar complex products outside Gaussian maps (2T chirps and 3T twists per power-of-two transform, then S outer pointwise products);
* **3T+4S<7T** scalar clipping/scaling calls (T per ring convolution, S per prime transform, S outer rescaling);
* at most **S** additional unsigned integer products for recovery, padded to **4p+8**.

Input arrays containing constants are still passed through the specified transforms. Constant-folding entire FFTs is not part of this canonical realization. Constants themselves can be hardwired and need not be generated at run time.

### Gaussian maps: exact loop counts and bounds

Apply tensor axes in increasing order. Define

    a_i=product_{j<i}t_j product_{j>i}s_j,
    b_i=product_{j<i}s_j product_{j>i}t_j,
    m_A=alpha ceil(sqrt(p)), m_E=ceil(sqrt(p)/(2alpha)),
    nu_i=ceil[p s_i/(alpha^2(t_i-s_i))].

These are respectively the number of slices applying A_i and B_i. Lemma4.9 (pp.30–31) evaluates the strict interval |j-s_i k/t_i|<m_A. Since gcd(s_i,t_i)=1, only row k=0 has an integral center; the exact total term count is 2m_A t_i-1. Lemmas4.11–4.12 (pp.31–33) use exactly 2m_E terms per row, nu_i-1 E-iterations and an alternating sum. Lemma4.8 (pp.29–30) applies one diagonal product per row. Across the three prime transforms set

    C_S=3 sum_i a_i(2m_A t_i-1),
    C_E=3 sum_i b_i [2m_E s_i(nu_i-1)],
    C_D=3 sum_i b_i s_i.

There are at most 2C_S+C_E+C_D scalar complex products and at most C_S+C_E complex additions/subtractions. The extra C_S covers the paper's beta*x coefficient products even though they are constant-only and can be hardwired. For E and J combined, the E inner sums cost (2m_E-1)s_i(nu_i-1) additions, and the J alternating sum costs s_i(nu_i-1), giving exactly C_E. Accumulators use signed words of width at most 2p+4: at most 2m_A<3p unit-disk summands, at most 2m_E<2p, or at most nu_i<=p, and p>=100. **No additional Gaussian clipping is omitted**: Lemma4.9 explicitly proves its computed sum has magnitude below 16p*2^(-p)+3/4<1; Lemma4.11 proves the E sum has magnitude below 13p*2^(-p)+0.42<1; Lemma4.12 proves the J alternating sum has norm below (3p^2/4)*2^(-p)+7/8<1 (pp.31–33). These are the raw fixed-point sums prescribed there, not post-projection values. D' uses ordinary Lemma2.4 unit-disk multiplication, already counted. Corollary2.8 adds error bounds for composition without introducing an arithmetic projection.

Here alpha=ceil((2d^2p)^(1/4)), theta_i>1/(4d), and alpha<sqrt(p), as proved on pp.37,39. Therefore

    alpha<=3sqrt(d)p^(1/4), m_A<=4sqrt(d)p^(3/4),
    nu_i-1<4dp/alpha^2, m_E<=3sqrt(p)/(2alpha),
    C_S<=24d^(3/2)T p^(3/4),
    C_E<=24sqrt(d)T p^(3/4), C_D<=3dT.

Including all chirps, twists and outer pointwise products, the scalar complex product count is at most 100d^2 T p^(3/4) for d>=2. Each scalar complex product takes four unsigned integer products on at most p+2 bits, padded to u=4p+8, plus at most 100p AND and 100p XOR for signed absolute values, restoration of product signs, two real sums, and truncation toward zero. This 100p allowance follows by at most four conditional negations at width p+2, four at width 2p+4, two ADD/SUB at width 2p+4, and two shift-with-negative-remainder corrections. Each correction OR-reduces the p discarded bits (<=p AND,2p XOR), gates that nonzero result with the sign, and increments the shifted signed result using an ADD at width p+2. At p>=100 the per-type sum is below 100p. Each complex Gaussian sum costs at most 24p gates of each type (two real ADD/SUB words <=2p+4, rounded allowance included).

The scalar complex products therefore require at most 400d^2T p^(3/4) small integer products. Clipping contributes fewer than 28T and recovery at most T. Together they are less than 512d^2T p^(3/4), hence are covered by 1024d^2T ceil(p^(3/4)). No arbitrary-width multiplication is charged as one gate.

The initialization v^(0)=rho(u/2) in each J' evaluation (Lemma4.12) also requires signed half-rounding, even when nu_i=1. There are at most 3dT such complex initializations, each costing fewer than 24p gates per type, hence at most 72dTp. These are counted separately below rather than hidden in the E-iteration additions.

## Explicit input-dependent helpers

### Restoring division

For a positive w-bit denominator and w-bit numerator, start remainder R=0. Process the numerator bits high to low. Form V=2R+bit by wires, compute D=V-denominator with a (w+1)-bit SUB, and select D when there is no borrow, otherwise V. The quotient bit is the no-borrow bit. After w rounds this is exact unsigned quotient/remainder division. Each round has one SUB and one MUX of width w+1 and at most one control NOT, so the totals are at most 6w^2 AND and 12w^2 XOR for w>=2. Division by zero in a branch that will later be discarded is prevented by a zero-test and replacing denominator 0 with 1.

### Restoring integer square root

Process the bits of a w-bit nonnegative integer in ceil(w/2) pairs from high to low. Maintain R and root q. Append a pair to R by wires, set trial=4q+1, subtract trial from the enlarged R, retain the subtraction iff nonnegative, and append that success bit to q. The standard invariant is processed_prefix=q^2+R with 0<=R<2q+1 after every round. This computes floor(sqrt(a)) and its exact remainder. Words of width w+2 suffice; one SUB and MUX per round give at most 6w^2 AND and 12w^2 XOR for w>=4. A zero-test of the remainder and one ADD give ceil(sqrt(a)), with at most 3w AND and 5w XOR extra. The script checks both restoring recurrences exhaustively at small widths, including perfect squares and zero.

### Unit-disk clipping (Lemma2.2, pp.10–11)

For a p-bit complex input and known c<=2^p compute x=c*a and y=c*b (two unsigned integer products after sign extraction), then norm=x^2+y^2 (two products and one ADD). A width w=4p+8 accommodates all magnitudes and carries. Compute ceil(sqrt(norm)); replace 0 with 1 for the discarded zero branch. Compute floor(2^p|x|/denominator), floor(2^p|y|/denominator), restore signs, and select this result only if norm>2^(2p). Thus exactly four small unsigned integer products suffice, plus one ISQRT, two DIVs and linear sign/control arithmetic. All products are padded to u=4p+8. Numerators fit within w because |x|,|y|<=2^(2p). The three restoring algorithms cost at most 36w^2 XOR and 18w^2 AND; allow another 100w gates per type for ceil, zero protection, signs, norm ADD, comparison and final selections. Since w<=5p for p>=100, this is below 1000p^2+500p, and **10000p^2 of each type** is a conservative complete helper allowance outside the four products. Both branches are computed, so the worst-case count is input independent.

## Packing, FFT, recovery and the nonrecursive ledger

**Ring packing/unpacking (p.14).** Put k=3p. To pack a signed coefficient stream into base 2^k, sign-extend each coefficient to a k-bit block and add the previous 0/-1 carry; extract the next carry from its sign. At most one k-bit ADD per coefficient is needed. Convert the resulting kr-bit signed word to magnitude before the unsigned recursive product, and restore the product sign afterward. To unpack balanced coefficients, add an incoming 0/1 carry to the next raw unsigned k-bit block, read the resulting block as a balanced signed coefficient, and set the outgoing carry to (addition-carry XOR coefficient-sign). Those bits are disjoint: an addition carry can occur only when the resulting block is zero. At most 2r k-bit ADDs and 2r extra XORs suffice per product. Four products and their sign conversions, followed by 6r-4 real coefficient sums/folds of width at most 3p+3 and 2r power-of-two divisions rounded toward zero, cost fewer than **1000rp** gates of each type. For example the pack, product-sign, unpack, combine and round allowances are respectively at most 28rk,32rk,(24rk+8r),96rp,60rp XOR; their sum is below 409rp for p>=100, with endpoint/sign slack below 1000rp. This linear-block construction avoids an uncharged quadratic Horner loop.

**Synthetic FFT (pp.18–20).** Its exact butterfly count over all nine transforms is B=(9Q/2)log2(Q). A butterfly has 2r real ADDs and 2r real SUBs on **w=p+3** bits, sufficient for the positive endpoint +2^(p+1) before division by two; it may also negate up to 2r real words for its signed permutation, and perform four-r normalized half/truncation corrections. Each correction is an AND plus ADD at width w. Since w<=2p and log2(Q)<p, these operations cost at most **1000Tp^2** gates of each type over all nine transforms. Wires and interleavings are free in this model.

**Recovery (pp.40–41).** Multiplication by S uses at most S additional unsigned products at u, already counted; shifts implement the 2^(2b) scale, and signs and nearest rounding cost at most 100Sp per type. After the fixed CRT permutation, a coefficient stream is evaluated by maintaining a carry, adding each <=3b-bit coefficient to it in a <=3b+1-bit word, writing the low b bits and retaining the remaining carry. There are 2ceil(n/b)-1<=T coefficients, so this costs at most 4Tp per type. Zero padding and input splitting are wires.

The following are *upper allowances* in units of d^2Tp^2 for each gate type:

| Component | Allowance | Reason |
|---|---:|---|
| Scalar complex signs, sums and rounding | 10000 | 100p times <=100d^2Tp^(3/4), and p>=1 |
| Gaussian accumulation | 1152 | <=48d^2Tp^(3/4) complex sums, <=24p each |
| J' initial normalized halves | 72 | <=3dT complex halves, <=24p each |
| Synthetic FFT including signs and half rounding | 1000 | Explicit butterfly lowering above |
| 3Q ring product pack/unpack/fold overhead | 3000 | 3Q times 1000rp; p>=1 |
| Input-dependent clipping excluding its products | 70000 | Fewer than 7T calls times 10000p^2 |
| Final recovery excluding its products | 104 | <=100Tp+4Tp |
| **Sum** | **85328** | **Less than 10^6** |

All input-dependent helpers are now charged. Every source omission listed at the beginning is size-only generation or free wiring under this model. The construction still uses the source's error guarantees and prime-existence proof; the counting argument does not change their numerical precision.

## Closing the explicit recurrence

Let A=2^30 d^2 n0 and C=6914A. The large branch has normalized coefficient

    lambda=36Tp/n * log2(3rp)/log2(n)
          <1728/(d-1/2)=3456/3457,

by Cor.5.5 (p.42). For p>=6E we have p>=2^64 and log2(5p)<=p^(1/8). Also T/n<48/p, L>=p/7, u<=5p and ceil(p^(3/4))<=2p^(3/4). Thus the normalized coefficient of the small recursive branch is

    mu <=3440640 d^2 p^(-1/8).

If u>=n0, then p>=n0/8 and mu<=1/6914. This follows from the exact inequality

    8(6914*3440640*d^2)^8 < 2^E,

which the script proves by comparing bit lengths without materializing 2^E. Hence both recursive branches together have coefficient at most 1-1/6914.

If u<n0 instead, bound its calls by 6u^2. Their total normalized work is at most 103219200 d^2 p^(3/4), hence below 103219200 d^2 n0. The nonrecursive ledger contributes at most 336000000 d^2. Their sum is below A since 103219200+336000000<2^30. The base range has normalized gate count at most 6n0<=C. Strong induction therefore gives U_g(n)<=C n max(1,log2(n)) for both gate types. This replaces rather than ignores the paper's O(p^(1+delta)) small arithmetic estimates.

## A lower envelope for the same canonical program

The nine FFTs execute exactly 9Tlog2(Q) real ADDs and the same number of real SUBs at width w=p+3. Their gate counts alone are 36wTlog2(Q) AND and 63wTlog2(Q) XOR. At n>=n0, Tp>=24n. Also log2(b)<=(b-1)/4<=L/4 and log2(r)<1+log2(T)/d give log2(Q)>3L/8>=L/4. This proves the stated 216nL AND and 378nL XOR lower bounds. Signed rotations, rounding, products and every other operation only add gates. The bound is on this fully specified unsimplified realization, not a lower bound on the mathematical multiplication problem.

## Verification and limits

`hvh_operation_census.py` emits the JSON certificate, records source hashes, checks rational contraction constants and ceiling bounds, exhaustively checks division and square root at small widths, and verifies a toy Gaussian term census. This independently checks arithmetic and helper behavior; it is not a formal verification of the analytic HvH proof or a full generated circuit. A source-derived family together with the explicit lowering and bounds above is available for comparison; no exact HvH total count function or numerical PR4470 eventual crossover is asserted here.
