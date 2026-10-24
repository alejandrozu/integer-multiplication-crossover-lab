# A fixed, reproducible arithmetic-work model

Model identifier: `xag-straightline-v1`.

This investigation fixes one model rather than claiming an implementation-independent crossover. There are infinitely many possible cost models and tariffs. A published model and a pinned circuit make the comparison objective and reproducible within that model.

An input consists of two unsigned n-bit integers, including leading zeroes. The output is their exact 2n-bit product. A computation is an explicitly specified finite, acyclic straight-line Boolean program over two-input AND and XOR gates. Constants 0 and 1, wires, fixed permutations and fanout are free. A NOT is one XOR with 1. A data-dependent selection must be lowered to gates. Program construction and physical memory traffic are outside this arithmetic-work metric. They must be included separately before making a runtime or practical impact claim.

For a pinned program let M(n) be its number of AND gates and A(n) its number of XOR gates. Neither number is a count of arbitrary-width integer operations. At tariff rho > 0 its work is

    W(n; rho) = M(n) + rho * A(n).

The slider changes rho, the cost of one binary XOR relative to one binary AND. It does not change the gate counts or silently refit either algorithm. Source-level integer additions and multiplications retain their operand widths and must be lowered through a specified circuit before entering M and A.

For each candidate and each fixed baseline, the desired threshold is

    N*(rho) = min { N : for all integer n >= N, W_candidate(n;rho) < W_baseline(n;rho) }.

The value is infinity if this set is empty. A source gap is recorded as unknown, not as infinity. The first observed crossing is not an eventual threshold. An upper bound for the candidate must be compared with a lower bound for the baseline to prove a sufficient threshold. Two upper envelopes alone do not establish actual superiority.

## Canonical adder lowering

For an n-bit ripple adder with both the n-bit sum and carry output, the first cell computes s=x XOR y and c=x AND y. Each remaining cell computes p=x XOR y, s=p XOR c, and c'=(x AND y) XOR (p AND c). The two carry terms are disjoint, so XOR equals their logical OR. This particular circuit has exactly

    M_add(n) = 2*n - 1
    A_add(n) = 3*n - 2.

Counts are for this explicit circuit, not a claim of minimum gate complexity. Unoptimized full-adder cells with an explicit carry input have 2 AND and 3 XOR gates per bit; source lowerings using that convention must say so. A scalar arithmetic ADD is therefore not one binary XOR.

## Publication and extension contract

A full crossover series requires complete gate-count functions or proved upper/lower count envelopes for two programs that compute the same whole-integer product. Every certificate records the subject, bit/limb widths, input range, source hashes, circuit-lowering convention, retained hypotheses and all omitted work. Controller calls, transform ranks, leaf counts, coefficient heights and asymptotic exponent savings do not enter as full multiplication counts.

The current PR4470 investigation retains the repository's native/all-column, analytic and recovery hypotheses. A conditional source-level operation census is useful, but is not a fully generated Boolean multiplier. Likewise a counted GMP basecase kernel is a real component count, not the cost of GMP's complete tuned dispatch.

## Open next questions

1. Produce a countable realization of each retained PR4470 primitive and its complete compiled word, including coefficient widths and recovery.
2. The canonical HvH datapath now has a derived numerical envelope. Keep its nonuniform exclusion of parameter/coefficient generation explicit, and formalize the full circuit proof if a machine-checked theorem is required.
3. The pinned full generic GMP dispatcher now has a derived numerical lower envelope. Exact total counts and other tuned parameter profiles remain separate work.
4. Only then populate full-crossover graph points and carry the same certificate interface to other PRs.
