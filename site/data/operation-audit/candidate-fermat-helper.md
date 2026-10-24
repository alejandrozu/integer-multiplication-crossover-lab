# An explicit candidate-only Fermat FFT multiplication helper

This is a new, deliberately simple circuit family. It replaces only the integer
multiplication helper inside a new PR4470 realization. It does not change or
claim an upper bound for the optimized GMP comparator. At AND=1 and XOR=rho>0,
each gate type of the helper separately satisfies, for all integer n>=1,

```
M(n) <= 2^48 n (1+log2 n)^8.
```

The model is the public-size, nonuniform straight-line XAG model of MODEL.md.
Constants, fixed routing, copies and permutations are free. Every arithmetic
operation below is charged; no root-of-unity multiplication is treated as a
free modular shift. This elementary construction is inspired by the Fermat
FFT in the [official GMP manual](https://gmplib.org/manual/FFT-Multiplication),
but uses its own power-of-two schedule and schoolbook leaves, rather than GMP
dispatch, native kernels or a finite-state timing bound. The proof below
supplies the constants, rather than importing an unspecified big-O constant.

## Linear elementary circuits

Width-w addition, subtraction, comparison with a public constant and a bitwise
multiplexer each use at most 8w gates of either type. Ripple full adders give
this loose tariff directly: AND<=2w, XOR<=3w for addition; complementing an
operand for subtraction adds at most w XOR. A mux uses one AND and two XOR per
bit. Constant comparison uses the subtraction carry or a ripple comparator.

Let F_p=2^p+1. Represent residues canonically by p+1 bits in [0,2^p]. For p>=2,
one modular add or subtract costs at most 512p of either gate type: add at
width p+2, subtract F_p and select, or add F_p to a negative difference.

There is also a <=512p circuit reducing an arbitrary signed or unsigned 3p-bit
word modulo F_p. Split the word into p-bit chunks X0,X1,X2 and let s be its
two's-complement sign (or zero for unsigned input). Its residue equals
X0-X1+X2+s. Compute this at width p+3. The result lies in [-F_p,2F_p); add F_p
conditionally if negative, then subtract F_p conditionally if at least F_p.
At most five arithmetic operations and two muxes at width p+3 cost
56(p+3)<=140p<512p for p>=2. The input sign term is a one-bit addend.

Multiplication by a public power 2^j modulo F_p also costs <=512p: reduce j
modulo 2p, wire the p+1-bit canonical input into an unsigned 3p-bit word shifted
by 0<=j<2p, then apply the preceding reducer. The largest occupied bit is
p+(2p-1)=3p-1. This covers negative powers through public exponent reduction.

## Recursive ring product and exact FFT identity

For p=2^t, t>20, put k=floor(t/2), K=2^k, b=p/K, p'=4b and F'=2^p'+1.
Then K*p'=4p, K divides p', and t'=log2 p'=ceil(t/2)+2<t. Use negacyclic
length-K convolution over Z/F': twist input coordinate i by psi^i, where
psi=2^(p'/K), transform with root r=psi^2, multiply pointwise recursively,
inverse transform, divide by K, and untwist. All twists and the inverse-K
factor are public powers of two, charged by the linear rotation circuit.

The DFT is invertible even though this ring is not a field. It has odd modulus,
so K is a unit. Also r^(K/2)=-1. For every j not divisible by K, writing
j=2^a u with u odd makes r^(j*K/2^(a+1))=-1. Pairing the terms in the root sum
therefore gives sum_(i=0)^(K-1) r^(ij)=0. For j divisible by K the sum is K.
These identities prove the usual inverse-DFT formula and negacyclic twist.

Canonical input x has a possible top bit alpha, so x=x_lo-alpha modulo F_p;
similarly y=y_lo-beta. FFT only the K b-bit chunks of the low p bits. Correct
the low-part product by -alpha*y_lo-beta*x_lo+alpha*beta modulo F_p. This uses
bit masks and at most four linear modular operations, and is charged below.

The integer convolution coefficients satisfy |c_i|<K*2^(2b)=2^(2b+k).
For t>20, k+1<b, so 2b+k<3b-1 and p'=4b>2b+k+1. Thus the centered residue
modulo F' recovers each coefficient exactly, and each c_i fits signed 3b bits.
Centering uses a comparison, subtraction and selection at width p'+2. The
guaranteed sign bits permit wiring its signed 3b-bit representation.

## Linear recomposition without K full-width additions

Write each signed 3b-bit coefficient as three b-bit chunks C_i0,C_i1,C_i2
and sign s_i. For j=0,1,2, scatter C_ij into bit positions (i+j)b of array U_j.
Within each U_j these intervals are disjoint. Form a sign array V with s_i at
bit (i+3)b. Then exactly

```
sum_i c_i*2^(bi) = U_0+U_1+U_2-V.
```

The arrays fit below p+3b<=2p because K>=4, and their signed sum fits in 3p
bits. Compute three width-3p arithmetic operations and apply the preceding
linear Fermat reducer. This counts every overlapping coefficient contribution
without introducing K*p sign-extension/addition work. Reduction gives precisely
the low-part product modulo F_p; the top-bit corrections give the full ring
product. Extraction, chunk placement and padding are fixed wires.

## Explicit local census and induction

All numbers below bound each gate type separately. A butterfly has one modular
rotation and two modular additions/subtractions, costing <=1536p'. Across two
forward FFTs and one inverse FFT there are exactly 3Kk/2 butterflies. The
additional two input twists, inverse normalization and inverse untwist require
at most 4K rotations. A deliberately rounded ledger is:

| Operation | Per-type gate upper |
| --- | ---: |
| Three FFTs | 9216 p k |
| Four banks of twists/normalization | 8192 p |
| K centered coefficient recoveries | 192 p |
| Recomposition and final ring reduction | 584 p |
| Canonical top-bit correction | 2052 p |

Their sum is at most 2^16 p(t+1). In particular,

```
S(p) <= K*S(p') + 2^16*p*(t+1).
```

At leaves p<=2^20 use explicit (p+1)-bit schoolbook multiplication followed by
the linear reduction. Charging every partial-product bit, every full-width row
addition and the final reduction gives <=512p^2<=2^29p gates of either type.
The exceptional p=1 ring has four Boolean input bits and two output bits. A
sum-of-products truth table uses at most126 AND and64 XOR gates (four shared
input complements, at most16 four-literal minterms and15 ORs per output),
also within the512p^2 bound.

Inductively S(p)<=2^32 p(t+1)^8. For t>=21,
(t'+1)/(t+1)<=7/11 and 4*(7/11)^8<1/2, so the recursive term consumes less
than half this budget. The local term is at most the other half. The leaf
bound is smaller as well. This proves the bound for every power-of-two p.

For arbitrary n-bit unsigned inputs choose p the least power of two >=2n.
Their ordinary product is strictly below 2^p, so the modular output is the
ordinary product. Here p<4n and t+1<=log2 n+3<=3(1+log2 n). Consequently
2^32*p*(t+1)^8 < 2^48*n*(1+log2 n)^8, proving the stated helper bound.

For two signed n-bit operands, compute their absolute values by conditional
two's-complement negation, use the unsigned helper, and conditionally negate
the2n-bit result according to the XOR of their signs. Absolute values fit in
n unsigned bits, including the most negative input. The extra arithmetic is
at most32n+1 gates of either type, so the deliberately loose signed bound
2^50*n*(1+log2 n)^8 is valid. Fixed-point truncation is output wiring; any
requested rounding operation is additional linear arithmetic.

## Scope of the receipt

The accompanying reproducer checks the exact geometry, induction margins,
coefficient intervals, reducer identity, top-bit correction and FFT/convolution
identity on small complete/random instances. It does not synthesize or execute
the astronomical full PR4470 circuit. This is a manual complete construction
and gate-count proof with arithmetic checks, not a Lean formalization or a new
claim about practical GMP speed. Its extra logarithmic powers must still be
charged by the whole-candidate aggregation before using the improved constant.
