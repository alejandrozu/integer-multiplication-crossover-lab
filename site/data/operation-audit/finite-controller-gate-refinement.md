# Integer gate refinement at the absolute fine-prime floor

This is a new parameter instance for five already checked finite-controller
early branches: corrected PR147 and own PR531,535,741,799. All original source
words, finite covers, moment inequalities, source-specific native work/height,
stopped-child stock correction, exact-grid endpoints and conditional analytic
contracts are retained. Frozen certificates are not edited.

The earlier instances set the umbrella B=2^E with E=2^41. No primitive or source
construction requires E itself to be a power of two. B must be a power of two;
this holds for every integer E. With A=10001, an integral gate satisfying the
absolute fine-prime floor is

    E_new = ceil(2^54/10001),  X_new=10001*E_new >= 2^54.

For clarity, the native recurrence tariff c(e) is **per complex coefficient**,
with component word width factored out. It is not the total cost of an e by e
matrix. C_e=C_1 tensor e has 2^e coefficient coordinates; applying its e binary
axis kernels costs at most40*e*w per coordinate. A direct C_1 output uses at
most six real ADD/SUBs, two real NEGs and dyadic shifts: per-type counts are
at most28w XOR and14w AND, below40w. Thus ordinary completion below d0 really
costs at most40*d0*w per coordinate, and the stated normalized fallback
40*d0*w*d^s is safe because d^s>=1. There is no omitted extra e factor or a
required doubling of the reserve log degree.

All E-dependent interfaces are rechecked, rather than applying the old theorem
outside its verified domain. The own native coefficient and stopped-base work
are paid by the larger p^delta/B margin, where delta=1/10000 and
(A*delta-1)*E=delta*E. The check includes the own finite work exponent, native
semantic guard, 1040 precision log powers and a constant allowance. The source
stopped reserve remains u^(70000Q) for PR147 and u^(1000000Q) for the other
controllers. Its complete cost remains in every outer row; it is not discarded
when E changes. The source's exact native operations and completed-return grid
contract introduce no new operation-by-operation rounding.

At p=2^X_new, the explicit numerical guards checked anew are:

* source work/height and exact-helper coefficients fit the umbrella margin;
* A*delta>1, 1040/X_new<delta/2 and the three body/normalization/boundary
  protection inequalities remain strict;
* X_new>=2^54 and X_new>128Q, including the absolute analytic prime floor;
* 2^(delta*X_new) dominates the typed-axis/prime capacity polynomial;
* 2^(delta*X_new-10) dominates the source stock-layout polynomial;
* the counted canonical HvH and repaired unlimited optimized-GMP input domains
  and the positive-tariff cost comparison hold.

For each own row with saving s, coefficient2^c B^r and log degree j, the new
certificate verifies exactly

    E_new*r + c + j*bit_length(X_new+3)
      - X_new*(s-1/5000) <= -3,
    4*j/X_new < s-1/5000.

The smooth envelope therefore decreases at every larger log2 p; all seven rows
sum below the required per-type budget. These checks use each own closed source
row, not an average native saving. PR147 retains its eight exact-division helper
powers and conservative stopped-stock correction.
The stock check is deliberately stronger than the original layout test: its
right side in logarithmic units includes the entire inflated reserve log degree
times bit_length(X_new+3), rather than merely a small source coefficient.

The general derivation only used E through these source-interface, numerical
precision/domain and seven-row inequalities. Its other parameter predicates and
typed arbitrary-column/whole-owner hypotheses are E-independent and stay bound
to each original certificate. Thus this is a fresh smaller sufficient gate, not
an interpolation of the earlier numerical result.

For p(n)=256ceil(log2 n), the new sufficient input upper is

    U_new = 2^(2^(10001*ceil(2^54/10001)-8)).

The reproducer records the exact integer E_new and log2log2 U_new. This does not
mean a percentage reduction in input n, locate the actual first crossing or
change any kappa record. The effective early saving remains1/5000 and the fixed
XAG/GMP comparator and positive XOR tariff are unchanged. Meaningful lowers stay
null for these finite controllers.

PR531/535/741/799 retain their separately quantified own record tails; the
piecewise early-to-record construction still preserves their source exponent.
PR147 retains only its explicitly optional, unquantified original-record
same-model compatibility hypothesis. The stronger new upper is independent of
that optional hypothesis. This is conditional AI-assisted written mathematics
and exact checks, not Lean or independent human verification.
