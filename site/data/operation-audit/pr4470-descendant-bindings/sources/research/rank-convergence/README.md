# Padding-free adaptive compiler (199.32× smaller rank exponent)

This package proves and certifies a direct compiler for overlapping native
rank profiles that satisfy explicit finite gates. It removes the
chronological tensor product, paid target completion and splitting stage
from the three instantiated constructions. The raw native words and paid
invoices stay unchanged.

For the recent p16 construction, it retains **[PR #4470](https://github.com/CrocSwap/integer-mult-bounds/pull/4470)'s conditional
κ = 0.00302015** and reduces the sufficient uniform rank from
**`2^558100005581` to `2^2800000000`**: a **199.321× reduction in its
exponent**, with **the same uniform saving and outer parameter point** as
[PR #4479](https://github.com/CrocSwap/integer-mult-bounds/pull/4479). The initial supplier uses tensor power **one**, replacing power
682. No new κ or selected-frontier update is claimed.

## What changes mathematically

The old direct flow selected its height using the smallest productive
rank. Later analyses showed that paid leaf paths could saturate its cap;
the near-root saving did not follow from that construction's moment
identity alone. This package changes the stopping geometry.

The new height uses the paid and productive rank distributions. A mixed
layer retains enough unit potential, while a separate lower-tail estimate
pays for small root sources. Exact source/boundary cancellation then
reduces the required surplus from an order-one threshold to
`(1-eta)/(eta-beta)`. A concave shifted-logarithmic majorant uses its
local tangent exponent to close the entire recursive construction.

This supplies a uniform convergence argument for the certified profiles,
rather than inferring convergence from a finite rank scan. The majorant
has a small fractional logarithmic power (`1/10` or `2/5` here). The proof
funds its whole ordinary base range and its final rank explicitly.

[PROOF.md](PROOF.md) gives the theorem and all finite gates. The theorem
does not say that every profile with a favorable moment admits those gates.

## Exact results and fair comparisons

In the table, `H` means the specified sufficient rank is `N=2^H`.

| Raw profile | Retained κ | Prior H | New H | Reduction |
|---|---:|---:|---:|---:|
| P7, same saving as [PR #4480](https://github.com/CrocSwap/integer-mult-bounds/pull/4480)'s unchanged-C witness | .00268647 | 130,200,000,000 | 3,040,000,000 | 42.83× |
| Native4453, same saving as [PR #4480](https://github.com/CrocSwap/integer-mult-bounds/pull/4480)'s main witness | .00300120 | 125,790,000,000 | 4,300,000,000 | 29.25× |
| P16, same saving as [PR #4479](https://github.com/CrocSwap/integer-mult-bounds/pull/4479) | .00302015 | 558,100,005,581 | **2,800,000,000** | **199.32×** |

An additional native4453 certificate uses its original outer point's
weaker required uniform saving, giving `H=1300000000` (96.76× against
[PR #4480](https://github.com/CrocSwap/integer-mult-bounds/pull/4480)'s H at the same κ). That comparison changes the uniform-saving
allocation; the 29.25× row holds it fixed. The exact receipt labels this
distinction and binds every baseline to the same authenticated profile.

Raw initial ambient ranks are **121, 153 and 145**, with their original
7,688, 11,560 and 10,928 productive fields. These replace the enormous
tensor-unit ranks and field counts used before uniform compilation. The
eventual uniform words can still have enormous widths and denominators.
No practical size or runtime factor follows from the ambient-rank bounds.

## The main p16 certificate

The raw profile is authenticated against both [PR #4470](https://github.com/CrocSwap/integer-mult-bounds/pull/4470)'s joint-helper
receipt and [PR #4479](https://github.com/CrocSwap/integer-mult-bounds/pull/4479)'s compact consumer receipt. Choose

```
t0=.99697984, p=2/5, c=133,
M=1024, a=b=1, ell0=650,
s=1/20, lambda=1/10,
n0=145*1024^650,
G(n)=2*floor(log_1024(floor(n/145))).
```

Exact rational intervals certify an exponent cover ending at `.997066`,
the mixed and root Chernoff bounds, every elementary mirror window and
the source capacity. The uniform recurrence certificate gives

```
D > .04854643,
required D < .04306221,
final funded logarithmic margin > .60862507
```

at `H=2800000000`. Monotonicity proves the recurrence at every rank above
the base cutoff and the final saving at every larger rank. All ordinary
base calls below `n0` are paid. The winning word is specified by the
integer algorithm and is not materialized.

## Reproduce and extend

Python 3.12, standard library only:

```sh
python3.12 -B scripts/research_package.py --package research/rank-convergence
python3.12 -I -O -B research/rank-convergence/verify.py
```

The verifier authenticates all live sources, reproduces four witnesses
across three raw profiles, checks uniform exponent and mirror covers,
binds the retained consumer and comparison points, and compares the exact
receipt. It includes literal chronological and independent ordered-word
oracles, empty-root forests, small-root controls, exact rank-invoice
cancellation and rejection of invalid certificates. No native or outer
producer suite is rerun by this command.

[BENCHMARKS.json](BENCHMARKS.json) contains complete rational witnesses.
[compiler.py](compiler.py) accepts `profile.json witness.json`; its output
certifies the conditional inequalities for those inputs. The profile gives
positive integer `targets` and `paid` histograms. Supported profiles have
minimum productive rank at least two, maximum paid rank below the raw
ambient rank, positive rank-one surplus and paid rank-one calls. These
are stronger premises than some parts of the written theorem require.

[flow.py](flow.py) constructs finite arbitrary-height flows and classifies
their root/nonroot sources and boundary/leaf exits. `adaptive_flow` computes
the witness's height with integer arithmetic. The frozen predecessor's
bytes are authenticated before execution. The tests independently rebuild
the same invoice from ordered-word convolutions and exact mirror windows.

For another submission, pin its actual native profile, search for a
feasible geometry and rational guards, certify them, and bind the resulting
uniform saving to its complete consumer. The generic checker does not
admit a native supplier or establish an outer theorem on its own.

## Scope, source retention and validation

Native all-column correctness, complete arbitrary input fields, whole-job
adapters, owned erasure, finite-program closure, physical tape, stock,
precision, analytic decomposition, prime avoidance and exact recovery
remain inherited premises. Numerical full-word scalar, bank and precision
constants require fresh substitution into the retained finite counting
prescriptions; old template counts are not transferred unchanged.

The raw-word and outer producer receipts are inherited. The new arithmetic
proves the changed compiler bound and checks that it supplies the unchanged
consumer points, including their nine margins, current strict/functional
guards and legacy receipt. This is distinct from replaying those producers.
The selected frontier is unchanged. Smaller local template rank does not
establish a smaller eventual multiplication-input threshold.

The successor starts from refreshed canonical main and retains the pending
[PR #4480](https://github.com/CrocSwap/integer-mult-bounds/pull/4480), [PR #4470](https://github.com/CrocSwap/integer-mult-bounds/pull/4470)/[PR #4479](https://github.com/CrocSwap/integer-mult-bounds/pull/4479) and [PR #4436](https://github.com/CrocSwap/integer-mult-bounds/pull/4436) histories. Only the needed new predecessor
directories were imported byte-for-byte. Existing scientific files and frozen
evidence were preserved; shared documentation matches canonical main.
[SOURCES.json](SOURCES.json) pins the exact inputs.
The worktree is sparse because full checkout exhausted disk space.

## Open next questions

- **An actual κ gain.** Replay a changed native warp word or a fully priced
  accumulating interface, then apply the direct compiler. The raw moment
  ceilings here are unchanged. A further κ hill step requires an actual
  paid-profile change with its full native replay.
- **Broader admission gates.** Characterize feasible geometries from tilted
  log means and study profiles where the mirror coefficient approaches
  source capacity. No universal gate-existence theorem is supplied.
- **Full physical constants.** Emit all counts for a small adaptive forest
  before attempting useful bounds on large widths, banks and precision.
  The winning templates remain algorithmic prescriptions.

Structured blockers and first steps are in [TASK.json](TASK.json).

## Attribution and review state

zxv, with substantial OpenAI Codex assistance and three user-requested
**Sol 6.1 medium** subagents. Separate author-side agents audited the
algebra, exponent covers, mirror endpoints, literal chronology and
source/consumer bindings. This is not formal or independent human review.
The user reviewed the local result and authorized publication on October 21,
2026 (America/Detroit).

Credit Jacob Alan Sussman's integer compiler; my [PR #4436](https://github.com/CrocSwap/integer-mult-bounds/pull/4436) direct flow,
[PR #4480](https://github.com/CrocSwap/integer-mult-bounds/pull/4480) rank compiler, my [κ=.0023 construction in PR #4359](https://github.com/CrocSwap/integer-mult-bounds/pull/4359),
and [PR #4453](https://github.com/CrocSwap/integer-mult-bounds/pull/4453) native/controller predecessors;
Ryanson Jonathan's corrected [PR #4459](https://github.com/CrocSwap/integer-mult-bounds/pull/4459) mirror identity; the finite-flow
and leaf analyses in [PR #4456](https://github.com/CrocSwap/integer-mult-bounds/pull/4456), [PR #4465](https://github.com/CrocSwap/integer-mult-bounds/pull/4465), [PR #4467](https://github.com/CrocSwap/integer-mult-bounds/pull/4467) and [PR #4476](https://github.com/CrocSwap/integer-mult-bounds/pull/4476); Cinna Davis's [PR #4470](https://github.com/CrocSwap/integer-mult-bounds/pull/4470) native
construction and prior thinning/helper work; Dugongue's [PR #4479](https://github.com/CrocSwap/integer-mult-bounds/pull/4479) compact
compiler; and all retained BIT, scalar, Clifford, geometry and outer
sources. New work is Apache-2.0.
