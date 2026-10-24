# PR4470: an explicit whole-integer circuit instantiation and comparison

This new conditional whole-integer upper bound binds the separately reviewed precision, occupied-batching, periodic-boundary and recovery modules. The adjacent JSON records their hashes and executable arithmetic checks. No first-crossing estimate is inferred from an exponent. The native operator contracts listed below remain premises.

## The exact problem and retained premises

Inputs are two unsigned n-bit binary integers, including leading zeroes. Output is their exact 2n-bit product. The metric is the fixed nonuniform XOR–AND straight-line circuit model: AND costs one, XOR costs rho>0, NOT is XOR with one, and constants, fixed wiring, copying, fanout, permutations and size-only circuit/coefficient synthesis are free. All input-dependent arithmetic, word widths, rounding, signs and recovery are charged. This differs from elapsed time or a uniform multitape implementation.

The source is PR4470 at pinned repository main 7c472563474e60185e6ca101a17622133d047e56, using its selected joint-helper RESULT, not numerical examples in historical vendor notes. Its native all-column endpoint, whole-job binary monomial, arbitrary-input spectator and owned-bank contracts remain explicit premises. The new work derives a numerical conditional upper bound from these contracts. It does not claim an independent human proof review, a Lean theorem, a materialized uniform word or a practical implementation.

Write

    H=64215200000000, N=2^H,
    m=33010*4^N, Mbar=2^m,
    A=10^15, kappa=60403/20000000,
    delta=1/1400000000, epsilon=1-delta, beta=1-3delta,
    xi=1782169498195771787/1960000000000000000.

The complete finite uniform compiler inventory is at most Mbar. Let eta=528527/175000000 and a=eta(1-delta). The independently counted ordinary supplier has axis exponent s=1-a and per-gate bound 2^40 Mbar^2 p V d^s at sufficient working width at most 33p.

## A concrete integer algorithm

Set b=ceil(log2 n), p=256b, L=ceil(n/b), and let T be the least power of two at least 8L. Set d=floor(p^epsilon). Distribute the log2 T target exponent as evenly as possible among d axes, so t_i is one of two neighboring powers of two. The effective fine-prime module supplies distinct odd s_i in

    (1-1/(2p^2))t_i<s_i<=(1-1/(4p^2))t_i.

At the common starting gate, every target side exceeds 2^64 p^1024 and T/2<S=product(s_i)<T. In particular 2L-1<S. Also T p<=8192n and log2 S<=b+5. The common gate implies d<=log2 T, so all axis exponents are positive.

Split each integer into L radix-2^b digits, append zeroes to S positions, and scale each digit by 2^(-b-2). Index the array by the CRT bijection j mapped to (j mod s_i). This is fixed wiring. Evaluate the Gaussian source transform U=R F, where F is the tensor product of normalized negative-sign Fourier transforms. On axis i the retained permutation is (R_i z)_j=z_(t_i j mod s_i). Since s_i is odd and t_i is dyadic, multiplication by t_i is a unit-index group automorphism. Evaluate U on both input arrays. Multiply the S output pairs pointwise and apply the opposite source transform U+=R F+ to the products. The actual fast circuit uses the counted Gaussian five-factor decomposition, exact dyadic supplier and charged diagonal products, not a dense Fourier oracle.

The identities F+R=R^-1 F+ and (Ra)(Rb)=R(ab), followed by Fourier orthogonality and CRT, give

    U+[(Uu)(Uv)]=(u*v)/S^2.

This is ordinary coefficient convolution because 2L-1<S. Track every additional dyadic normalizer and postpone its restoration to exact recovery. The total exponent is Gamma=2Gamma_forward+Gamma_inverse, since multiplying the two forward outputs adds their exponents. It is at most 6144d(ell+1), ell=ceil(log2 p), including the inherited Gaussian gains. The global precision module proves the computed coefficient is within 1/(4K) of c_j/K, K=S^2*2^(2b+4+Gamma).

Recover c_j by a charged exact multiplication of its fixed-point numerator by S^2, the fixed dyadic shift, and nearest integer rounding. Propagate carries through 2L radix positions using v=2b+ceil(log2 L) bit additions. The adjacent boundary/recovery module proves this circuit correct under the stated strict error inequality. The integer product fits in 2n bits, so known leading high zeroes may be discarded by wiring.

The counted candidate circuits are specified for the certified tail of input sizes. A correct reference multiplier handles the finite excluded range. A chosen fallback switch is a design choice, so it is not reported as an intrinsic first crossing of PR4470’s construction. The theorem below concerns every input size in the certified tail.

## Counting the complete input-dependent circuit

All rows below are upper bounds for each gate type separately. Fixed scalar coefficient products are charged with the explicit HvH helper envelope, whose per-type constant C_HvH is less than Mbar. The 33p ceiling concerns stored data and native operands. A charged exact w-bit integer multiplication helper returns a full 2w-bit product before truncation, so its product wires may reach 66p bits. Its envelope already includes those wires and operations. Write ell=ceil(log2 p). The following deliberately loose common prefixes exceed the independently reconstructed numeric coefficients.

| Work | Per-type upper bound | Saving relative to n p |
|---|---|---|
| Three target tensor FFTs, Hadamard parts | 2^60 Mbar^2 n p^(1-epsilon a) | epsilon a |
| FFT twiddle diagonals | 2^70 Mbar n p^(1-epsilon) (ell+2)^2 | epsilon |
| Dense Gaussian Hadamard circuits | 2^90 Mbar^2 n p^(epsilon-beta a) (ell+2)^4 | 1-epsilon+beta a |
| Dense Gaussian diagonals and completed scalar maps | 2^90 Mbar n p^(epsilon-beta) (ell+2)^5 | 1-epsilon+beta |
| Batched Strassen boundary and coupling applications | 2^60 Mbar n p^(29/32+epsilon-xi) (ell+2)^3 | 3/32+xi-epsilon |
| Halo and core-face correction arithmetic | 2^50 Mbar n p^(epsilon+beta-79) (ell+2)^2 | 80-epsilon-beta |
| Pointwise products, S^2 recovery products and carries | 2^70 Mbar n (ell+2)^2 | 1 |

The main tensor FFT count does not identify a one-dimensional Fourier transform with a Hadamard transform. At each binary level it combines one butterfly bit from each *different* tensor axis into an ordinary Hadamard operation, followed by the combined charged twiddle diagonal. There are h=ceil(log2 T/d) levels. Consecutive stages within an axis remain separated by twiddles. The all-size supplier bound covers a final partial subset of axes without an unpaid elementary tail. The raw target transform has prefix/suffix growth at most T. Its final exact 1/T shift and q-grid rounding cost at most ten w-bit macros per coefficient, absorbed in the displayed twiddle row. The global precision guard explicitly includes 2log2 T, so this normalization and the unnormalized Fourier prefixes are not assumed free of word-width or error consequences.

For Gaussian groups choose dyadic g with p^beta/2<=g<=p^beta and balanced group sizes between g/2 and g. There are at most 4d/g groups. At most twelve completed factor types per axis can be synchronized across axes by tensor commutation. Each dense factor uses at most D=1024(ell+1)^4 two-wire rounds, at most 6D simultaneous Hadamard calls and 6D+1 diagonal stages. Diagonal products use a specified fast integer multiplier on the actual word width. Constant-only coefficient synthesis and matching permutations are free; diagonal-times-data arithmetic is not.

The boundary row uses the actual counted q-RHS Strassen batches, including a partly filled final batch at full cost. The halo row uses its explicit copied input volume, band-LU invocations and single-face partition. Neither row extrapolates an old asymptotic snapshot. Source routing, public membership, tags and CRT order need no gates in this model, since their locations depend only on n and the chosen circuit. Input-dependent values are never used as addresses.

## The common effective starting gate

The common gate is p>=Mbar^A. The precision, boundary, batching and prime modules establish the listed validity conditions under this gate. They give sufficient nonzero weight setup precision, finite-section conditioning, exact native grid guard C0d<p/256, global chirp/circuit prefix guard below p/256, Gamma<p/256, complete row batches, sufficient axis and RHS sizes, Gaussian tail bounds and final recovery error.

The exact arithmetic companion proves the following useful compressed comparisons, without constructing N or Mbar. For N>=1024, m=33010*4^N satisfies m>4096N and log2(A m)<4N. At p=Mbar^A, (ell+2)^1024 is smaller than p^(nu/2), where nu=4195771787/1960000000000000000 is a conservative lower bound on all relevant small positive exponent gaps. The ratio log(log p)/log p decreases for larger p, so the inequality holds throughout the tail. Also A delta>700000 and A nu>2000000. Consequently the fixed inventory, helper and polynomial-logarithm coefficients have a very large absorption margin.

Here are the remaining explicit interface checks. Since p>=Mbar^A exceeds the fine-prime lemma's 2^179200000000 gate, each target t_i>=2^64 p^1024 and each source s_i>t_i/2>=p^256. With epsilon>1/2, d>=2. Thus a sparse-axis call has at least one other complete target axis as spectators, and its RHS count m_i=T/t_i exceeds p^1024>=4W. These are complete fixed-wiring fibers; no small flag class is assumed to fill a batch.

For B the largest dyadic integer below p^xi, B>=p^xi/2 and W<=36sqrt(p ell). The positive gap xi-1/2 exceeds nu. At the common gate, 2^32(ell+2)^1024<=p^nu, by applying the preceding logarithm bound twice. Hence p^(xi-1/2)>144sqrt(ell), proving B>=2W. Also B<=p, so the interior precision bound applies. Balanced groups exist since beta<epsilon and p^(epsilon-beta)>=Mbar^(A(epsilon-beta))>2. The copied-halo condition 4g p^48<=p^128 follows from g<=p and p>=2. This also bounds the total halo extension by a constant multiple of the counted volume.

Finally, T<16ceil(n/b)<=32n/b, so T p<=8192n and log2 T<=b+5<=p/128. The final recovery scale has log2 K<=4b+14+Gamma_total<5p/256+14<p/32 at the gate. All these checks concern actual algorithm parameters; a column count, axis length or prime-existence threshold is not substituted for n.

Under the retained native contracts, summing the seven counted rows and applying the reviewed analytic/counting modules yields the simple common per-type envelope

    Mbar^100 n p^(1-kappa).

This numerical coefficient is separate from the semantic precision constant C0. It is derived from charged module bounds and explicit exponent absorption, not set equal to an unspecified O-constant.

## Comparing with the two full reference circuits

The previously specified HvH reference circuit has weighted lower bound (216+378rho)n log2 n for n>=2^(1729^12). The pinned generic GMP 6.3.0 reference has weighted lower bound (1+3rho/2)n log2 n for n>=2^26. The GMP reference is generic 64-bit C with no assembly/native replacements, no TABLE3, WANT_ADDSUB undefined and idealized unbounded public indices. This is not a lower bound for all tuned GMP implementations or the fastest possible algorithm on hardware.

For b>=2, log2 n>=b/2=p/512. Thus the candidate-to-baseline ratios are bounded respectively by

    [512(1+rho)/(216+378rho)] Mbar^100 p^(-kappa),
    [512(1+rho)/(1+3rho/2)] Mbar^100 p^(-kappa).

For every positive tariff the bracketed factors are below 512. Since A kappa>3*10^12, at p>=Mbar^A both ratios are strictly below one, with enormous slack. The effective prime, precision and batching gates establish the remaining input conditions there. Both baseline domains also hold since Mbar exceeds their explicit starting constants.

Consequently the conditional sufficient upper bound on the eventual crossover is

    N*(rho) <= U = 2^(Mbar^A)
                  = 2^(2^(33010000000000000000 * 2^(2*2^64215200000000))) bits.

Equivalently log2 log2 U=33010000000000000000*2^(2*2^64215200000000). The number refers to bits in each operand, not numerical operand value. It is an explicit and extremely loose sufficient bound for the specified circuit instantiation. It is not the smallest or realistic crossover, and it supplies no informative numerical lower bound on an intrinsic first crossing of the source construction. The same validity-dominated bound works for every positive slider value. The slider still changes the exact priced comparison factors above.

The graph should shade the region below U as uncertified by this bound. It must not extend a candidate curve into that region and label an extrapolated crossing as a theorem. For input-size coordinate x=(log2 log2 n)/m, the common rigorous ratio ceiling is Mbar^(101-kappa*x), valid for x>=A. The factor 512 is below Mbar. Exact price-dependent factors are displayed separately because their effect is smaller than the precision of this giant-scale plot.
