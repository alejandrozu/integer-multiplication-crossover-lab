# Conditional κ = 0.00268647 with paid productive-rank padding

This contribution improves the conditional construction of
[PR #4359](https://github.com/CrocSwap/integer-mult-bounds/pull/4359) from
κ = 0.0023 to **κ = 0.00268647**, continuing the native tensor and p6 results
in [PR #4412](https://github.com/CrocSwap/integer-mult-bounds/pull/4412) and
[PR #4414](https://github.com/CrocSwap/integer-mult-bounds/pull/4414).
The proposed conditional multiplication bound is

```
T(n) = O(n (log n)^(1 - 0.00268647)).
```

The new mechanism pays to enlarge small productive transforms **after**
tensor composition. Its cost decays relative to the total productive moment,
allowing a strict paid-rank cutoff above the raw supplier's minimum rank.
This resolves the tail obstruction that prevented direct admission of the
stronger p7 controller.

## Native construction and charged padding

The exact fixed controller is `pairs=7, keep_idle_mask=232127`. The source
Laurent factorization code regenerates this one case. The complete native
audit then binds its actual program on 121 axes, with 15 local calls, all
independent main and fresh helper inputs, original rank-eight centers, and
every full idle window. Coordinate maps, inverses and Z4 phase polynomials
check all main contacts and endpoints. [NATIVE.md](NATIVE.md) gives the
construction and source bindings; a tariff alone is insufficient evidence.

[TENSOR.md](TENSOR.md) first forms a chronological native tensor power.
For each completed productive rank K below `11^6240`, it pays for the
transform on the missing disjoint axes of that same arbitrary input field.
The resulting target has rank `11^6240`. No new input or productive field
is credited. All original and added paid jobs are split at cutoff `10^6240`.
The new minimum target strictly exceeds the maximum paid rank, while the
rank-one surplus is unchanged.

At tested saving **0.00268648**, exact bounds certify the original mixed
moment, the entire original paid rank-one tail, and the entire added padding
bill. These are three separate terms; the padding is never treated as free.
The resulting tensor power is 6,240. [ENDPOINT.md](ENDPOINT.md) specifies
the sufficient uniform ambient rank `N = 2^16201843136005340321` and
verifies every inherited outer cost
using the unchanged ordinary BIT admission of 0.0027.

[RESULT.json](RESULT.json) records exact source authentication, the native
replay, complete padding/cutoff arithmetic, outer checks and rejection
controls. An independent rational interval engine cross-checks the critical
moment and both tails. The enormous tensor and uniform words are defined
by finite algorithms; their instruction lists have not been emitted.

## Reproduction and provenance

Python standard library only. Normal replay reads source exports, regenerates
the fixed native controller and arithmetic, and compares the saved receipt.

```sh
python3 -I -O -B research/pr4359-p7-padding/verify.py
python3.12 -B scripts/research_package.py --package research/pr4359-p7-padding
```

`EXPORTED-SOURCES.json` pins focused unchanged files from PR4359 at
`da637c87c89482bc4c86be36bd0071b3d400dbed`, interval/outer-ledger dependencies
from PR4405 at `873d1b3c96a83b701a5c0bba8e37a861e6672fef`, and the all-fresh
native source gate from PR4412 at `9f0df9bf6f49942faf5f31389e7e387fdfe511b3`.
Each export is compared with the original Git blob and SHA256. Unmerged
source heads are not represented as publication ancestry. The standard
`SOURCES.json` records task and selected-result provenance from canonical
main `12fa8c5`. The new p7 controller receipt is generated from the pinned
factorization code; it is not presented as an old published source artifact.

## Scope and credit

This is a conditional research result awaiting review. It retains the source
all-column arbitrary-input native words, permitted physical operations,
analytic decomposition, fixed-tape model and outer transfer assumptions.
Finite replay does not formally verify the complete multiplication theorem.
No selected-frontier update, practical implementation or global optimum is
claimed.

Controller and native source: @zxv, PR4359. Underlying mixed flow: Jacob Alan
Sussman, Theorem 1G. Earlier attribution and notices remain in copied sources.
New native audit, paid-padding proof, exact arithmetic and integration were
prepared for @1337isnot1337 with substantial OpenAI Codex assistance.
Apache-2.0.

## Bounded continuation

[FOLLOWUP.md](FOLLOWUP.md) and its registered `scan.py` replay check 209
explicit algebraic profiles with pair counts 2 through 20. Only the selected
p7 profile passes at 0.00268648; all fail at 0.00268649. This is a finite
profile result, without native admission of every candidate or global
optimality. Its exact intervals are saved in `FOLLOWUP.json`.

## Open next questions

[TASK.json](TASK.json) records first steps and blockers. Larger or different
controllers require a new complete native audit before their moments support
an exponent claim. Higher-moment tails or tighter padding thresholds could
reduce the sufficient ranks; the current values are not asserted minimal.
The inherited BIT interface must also be revisited if a future complex saving
crosses its admitted value.
