# One complete, scoped circuit comparison

Combining the proved upper in `hvh-operation-census.md` and the lower in `gmp-fft-lower.md` yields an actual sufficient whole-algorithm inequality. For every positive XOR/AND tariff rho_cost, the specified canonical HvH circuit has fewer weighted gates than the specified generic GMP6.3.0 circuit for every integer input length

    n >= 2^7137398073256634897664758526207831208357 bits per operand.

This is a sufficient eventual bound for **these two programs**. It is not the first crossing, a PR4470 comparison, a bound for other/tuned GMP configurations, or a physical runtime prediction. The generic GMP program deliberately retains its fixed fallback FFT table with k<=11, idealized public-size arithmetic and unsimplified 64-bit adders. The HvH program and its nonuniform free-constant/wiring conventions are also specified in its note. Both source-counting proofs are manual mathematical arguments with executable checks, not Lean formalizations.

Let E=1729^12 and C=Pref*2^E be the per-gate HvH constant, with Pref=22193164471003774976. The candidate upper is C(1+rho_cost)nlog2(n); the generic-GMP lower is (4+6rho_cost)n^(11/10). Since `(1+rho_cost)/(4+6rho_cost)<1/4`, it suffices to show `(C/4)log2(n)<n^(1/10)`. Put `L*=10E+t`. Cancelling 2^E and raising both positive sides to the tenth power gives the exact integer test

    (Pref*(10E+t))^10 <4^10*2^t.

This passes at t=1947 and fails at t=1946, entirely in integer arithmetic. Thus L*=10E+1947 is the exact exponent displayed above. The failed predecessor concerns this sufficient envelope test, not the programs' actual first crossover.

The ratio `2^(L/10)/L` increases for L>10/ln2<15, proving the inequality for every L>=L*. Also L*>E and L*>26, so both component validity ranges hold. For a rational positive tariff rho_cost=a/b the sharper exact test is

    [Pref*(a+b)*(10E+t)]^10 <(4b+6a)^10*2^t.

For tariffs 1/1000,1/10,1,10,1000 the first passing offsets of this envelope test are respectively 1947,1946,1944,1942,1941. Each previous offset fails. The reproducer `hvh_vs_generic_gmp.py` checks these integer inequalities and binds the exact two JSON inputs by SHA-256. This illustrates a completed upper-versus-lower comparison in a fixed circuit model while the requested PR4470 whole-program envelope remains unfinished.
