# PR4470 versus an unbounded optimized GMP source family

The specified optimized-source circuit has, for every public operand width
n>=2^80 bits and every positive XOR tariff rho,

```
AND_GMP(n)>2n log2n,
XOR_GMP(n)>3n log2n,
W_GMP(n,rho)>(2+3rho)n log2n.
```

Combining this with the complete conditional PR4470 upper bound gives

```
W_PR/W_GMP <=[512(1+rho)/(2+3rho)] p^-kappa <256p^-kappa,
p=256ceil(log2n), kappa=60403/20000000.
```

Consequently the existing sufficient input bound
U=2^(M_N^1400000001/256), M_N=2^(9HN), H=64215200000000,N=2^H,
also proves the comparison with this optimized reference for every n>=U.
This is a comparison of full input-dependent circuit costs, using a lower
bound on the full optimized program and an upper bound on the full candidate.
It is not a physical runtime estimate or a universal lower bound for GMP.

## Precisely define the optimized unbounded reference

Use the official GMP6.3.0 archive, pinned by the adjacent source audit.
The native Tiger Lake configure path reaches the Skylake machine parameter
header because this archive has no earlier usable icelake source directory.
Retain all227 entries of its multiplication TABLE3, all other source
thresholds, and the selected optimized kernels. The actual scalar native
addition source is coreihwl/aors_n.asm. HAVE_NATIVE_mpn_add_n_sub_n is0
and WANT_ADDSUB is undefined, so FFT butterflies use separate add/sub paths.

Extend the original tuned tail by entries{2^(k-1),k} for all k>=25.
The original finite data and their lookup convention are unchanged.
Promote public sizes, indices, shifts of indices, table generation and
public loop controls to mathematical unbounded integers. Fixed routing and
generation are free in xag-straightline-v1. Data limbs remain64 bits.
This is an explicit mathematical extension, not a claim that a finite DLL
or address space supports these inputs.

For data arithmetic, mechanically lower each64-bit ADD/ADC to64 unsimplified
full-adder cells, including constant initial carry and final carry:
128AND+192XOR. No cross-instruction CSE, constant folding or gate pruning
is performed. Other arithmetic is implemented by correct nonnegative-cost
circuits. This defines one program-derived circuit family; it does not
claim these counts are necessary in every circuit computing addition.

The source manifest and build/profile facts are bound in
optimized-gmp-unbounded-source/audit.json. The timed installed wheel uses
a different fat dispatch profile; its measurements are not extrapolated
by this proof.

## The full-product call reaches a compulsory FFT root

Take two distinct-address equal public-length limb arrays,
m=ceil(n/64). mul_n selects its FFT path above the pinned6272-limb
threshold. gmp-impl.h maps the full FFT interface to nussbaumer_mul.
That code calls mulmod_bnm1 at next_size(2m). For these sizes its
rounding routine returns2R, where

```
k0=best_k(m), R=ceil(m/2^k0)*2^k0.
```

The even large modulus takes the CRT minus/plus route. Its plus product
calls mul_fft at modulus sizeR limbs, choosing best_k(R) and decreasing
k only until2^k dividesR. The two original input pointers remain distinct;
this root is an ordinary multiplication with two forward transforms,
not a squaring shortcut. The minus product and CRT reconstruction are
additional work which may be omitted from a lower bound.

For m>2^46, the continued TABLE3 lookup gives exactly
k0=ceil(log2m/2). Its endpoint convention is n<=threshold: on
(2^(2j-2),2^(2j)] it returnsj. Also R>=m and R<m+2sqrt(m)<2m.
The tail lookup is monotone, so best_k(R)>=k0. R is divisible by2^k0,
therefore the alignment loop cannot decrease belowk0. Thus the actual
root exponent satisfies k>=log2m/2.

## Count only mandatory native limb additions

Write K=2^k, J=64R and let Nprime=64nprime be the root coefficient width.
The actual source sets

```
M=J/K,
step=max(64,K),
Nprime=step*(1+floor((2M+k+2)/step)).
```

Later rounding can only increase Nprime. In particular
K*Nprime>=2J, or K*nprime>=2R.

Each K-point forward or inverse transform has exactlyK*k/2 butterflies.
Every higher butterfly unconditionally calls native add_n onnprime limbs;
the K=2 case usesnprime+1. The selected native assembly executes one
64-bit ADC per input limb, including all eight residue handlers and
unrolled blocks. Hence the three transforms contain at least

```
3*(K*k/2)*nprime >=3kR
```

full-word additions. Counting only their fixed ripple-cell expansions gives
AND_root>=6kJ and XOR_root>=9kJ. Ignoring subtraction, carry correction,
twiddle rotations, leaf products, other optimized kernels and reconstruction
only weakens this lower bound on the specified full source circuit.

Since J>=n, m>=n/64 and k>=log2m/2, put x=log2n to obtain

```
AND_GMP >=3n(x-6),
XOR_GMP >=(9/2)n(x-6).
```

For x>=80 these are strictly greater than2nx and3nx. The same domain
also implies m>2^46 and all finite dispatch thresholds used above.

## The unbounded FFT remains a terminating algorithm

For every active multiplication selector argument x>=404, and every
active squaring selector argument x>=400, the pinned tables and their
continuation satisfy

```
32<=K_best(x)=2^best_k(x)<=x/8.
```

The reproducer checks each finite constant-selector interval at its left
endpoint. In the continued tail, K_best(x)<=2sqrt(x)<=x/8 for x>=256.
This supplies the bound throughout the complete selector domain rather
than only at the extremely large input used for the comparison.

For a parent FFT of pl limbs, let np0 be its initial child limb width,
before the repeated child-size alignment. The source formula above gives

```
np0<=2pl/K+K/64+(k+2)/64+1
    <=pl/16+pl/512+pl/8
    =97pl/512<pl/4.
```

Here K>=32, K<=pl/8, k<=pl, and pl>=400 imply
(k+2)/64+1<=pl/8. A nonterminal alignment step rounds np upward to a
multiple of its selected power of two. After that rounding, the same
or any lower exponent would already divide np. Therefore exponents at
successive nonterminal steps strictly increase. At every finite prefix
of this loop, the total increase is less than twice its largest selected
power Kmax. Since Kmax was selected at an earlier argument no larger
than the current np, Kmax<=np/8. Consequently every finite prefix has

```
np<np0+np/4, hence np<(4/3)np0<=97pl/384<pl/3.
```

An increasing sequence of integer widths with this fixed upper bound
cannot continue indefinitely. The alignment loop terminates, and its
final recursive child is strictly smaller than the parent. Repeating
this argument makes the recursive FFT tree finite. Below the original
mod-F thresholds the original finite base algorithms apply. The
unbounded public-index extension therefore introduces neither an
infinite alignment loop nor an infinite recursive FFT branch.

## Combine the complete upper and lower bounds

The nested PR4470 certificate proves each candidate gate count is at most
n*p^(1-kappa) for p>=P=M_N^1400000001, retaining its stated native
contracts. For n>=2^80, log2n>=p/512. Dividing the candidate weighted
upper by the optimized reference lower gives the ratio on the first page.
For every positive rho,
512(1+rho)/(2+3rho)<256. Also A*kappa>1 and M_N>256, so
256p^-kappa<1 throughout p>=M_N^A. All size domains are included there.
The official source profile and its circuit lowering do not add a new
native hypothesis to the candidate; the candidate's original native
contracts remain explicit.

## What is and is not a first-crossing result

Define the first-crossing question here on the explicit input-width
domain n>=2. The one-bit elementary case is outside this convention;
no lower bound of2 would follow for a domain including n=1.

The smallest integer input width covered by this precision theorem is

```
L=2^(M_N^1400000001/256-1)+1.
```

Indeed ceil(log2n)>=P/256 is equivalent to n>2^(P/256-1), since P/256
is an integer. L is well above2^80. The comparison holds for all n>=L;
U=2^(P/256) is the convenient conservative displayed upper bound.

Without evaluating or proving the candidate's earlier cost, the natural
first strict crossing and natural first eventual threshold remain unknown.
For either threshold, the only general displayed interval is2<=N_star<=U.
No substantial lower cutoff follows from the validity gate or template rank.

A distinct hybrid circuit can be defined to run this exact optimized GMP
reference belowL and the candidate at/aboveL. Its modeled cost equals
GMP belowL and is strictly smaller at every input n>=L. Its first strict
and first eventual crossing is therefore exactlyL **by that branch
definition**. This is a legitimate explicit hybrid construction, not an
intrinsic lower bound on the original candidate's crossover.

The reproducer checks exact table boundaries, root divisibility, mandatory
word counts, rational prices and proof bindings. These are AI-assisted
written source-counting proofs and exact checks, not Lean formalization,
independent human review, a hardware forecast or a lower bound for every
equivalent optimized implementation. The optimized program's full upper
cost is not derived by this comparison module; it is unnecessary for
the strict upper-versus-lower comparison proved here.
