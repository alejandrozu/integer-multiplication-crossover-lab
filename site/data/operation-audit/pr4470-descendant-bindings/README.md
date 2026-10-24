# Authenticated p16 compiler descendants

This package binds three conditional compiler witnesses to the unchanged PR4470 raw p16 word. It supplies inputs for a separate comparison proof; it does not transfer PR4470's full runtime upper bound by substituting a smaller rank.

| PR | GitHub mergedAt (UTC) | Retained κ | Uniform rank `2^H` | Initial tensor power |
|---|---|---:|---:|---:|
| [4479](https://github.com/CrocSwap/integer-mult-bounds/pull/4479) | 2026-10-22 02:49:06 | .00302015 | H=558,100,005,581 | 682 |
| [4483](https://github.com/CrocSwap/integer-mult-bounds/pull/4483) | 2026-10-22 02:49:06 | .00302015 | H=2,800,000,000 | 1 |
| [4533](https://github.com/CrocSwap/integer-mult-bounds/pull/4533) | 2026-10-22 19:19:24 | .00302015 | H=1,587,000,000 | 1 |

These are **no-new-κ** compiler contributions. The dates are GitHub merge events, not proof-assistant or independent-human mathematical acceptance. [4480](https://github.com/CrocSwap/integer-mult-bounds/pull/4480) is retained as an exclusion: its main native4453 witness has κ=.00300120, raw ambient153,11,560 fields and power260. It is not a rank-only PR4470 witness.

All sources are pinned at main commit `7c472563474e60185e6ca101a17622133d047e56`. The decisive historical PR-head files were separately downloaded and found byte-identical to these main-snapshot files. Their URLs, head hashes, dates and SHA-256 values are recorded in `historical-head-bindings.json` and `bindings.json`.

## PR4479: exact source and fresh arithmetic

The [proof](https://github.com/CrocSwap/integer-mult-bounds/blob/035008ddc2cea4949829d309770e67479e696d9e/research/compact-joint-compiler/PROOF.md) and [arithmetic receipt](https://github.com/CrocSwap/integer-mult-bounds/blob/035008ddc2cea4949829d309770e67479e696d9e/research/compact-joint-compiler/arithmetic/RESULT.json) retain all raw productive/paid/native data. Its SOURCE pins match the five original PR4470 `CONTROLLER.json`, `NATIVE.json.gz`, `PATCH.json`, `RESULT.json` and `native_joint.py` files; the arithmetic controller is byte-identical to PR4470's literal controller. The raw invoice remains10,928 productive fields,64,620 paid jobs and rank surplus752.

The new tensor uses power682, paid cutoff17, productive floor21, tail offset1/8 and logarithmic majorant power143. Its compiler test is `(100000001*5581+1)^143 < 2^5581`, with preceding integer failure. The positive uniform saving is exactly

```
eta_uniform = 471898442219 / 156250001562500.
```

The compiler's different contraction quantity called `eta` lies between `.000035221718023643756209805039` and `.000035221718023643756209805040`; it must not be confused with that exponent saving.

The outer point changes: `delta=1/60000000600000000`, `epsilon=1−delta`, grouping `beta=1−3delta`, and `stop=delta`. Its exact cap is

```
xi = 363708067274161256350671866465323 /
     400000008000000040000000000000000.
```

The eight owned arithmetic inputs were authenticated, then the source's standalone arithmetic gate was freshly replayed. It reproduces the full receipt, including p16 event accounting, both tails, majorant,54 current strict predicates, four functional guards and63 legacy predicates. This does not claim a fresh native/operator/all-column replay. Run `python -B audit.py` to repeat the bindings and this arithmetic gate offline.

## PR4483 and PR4533: same raw word, different compiler

[PR4483's proof](https://github.com/CrocSwap/integer-mult-bounds/blob/fb0c208864e6b24e3473318a058aa5b2dbd5764b/research/rank-convergence/PROOF.md) explicitly changes the height of the finite integer flow while retaining its chronological native productive/paid word. Each flow unit has positive integer column multiplicity; whole jobs, complements and rank-one paid exits remain charged. It removes the chronological tensor, completion and splitting stage. Its p16 receipt has power1,H=2,800,000,000, the same positive uniform saving as PR4479, and a positive final funding margin greater than .60862507. The p16 benchmark source is PR4479's authenticated arithmetic receipt.

[PR4533's witness](https://github.com/CrocSwap/integer-mult-bounds/blob/e9e9f244108ab4c21f0293cbfca9cfc3206e772a/research/adaptive-witness-retune/WITNESS-p16.json) retains this compiler theorem and uniform saving while changing its finite geometry, producing H=1,587,000,000. Its native and outer producer receipts are inherited. Its complete source verifier was not freshly rerun for this binding task; this is an authenticated witness/theorem binding, not an additional replay claim.

In each case the conditional uniform theorem is `P_N/W_N < N^(1−eta_uniform) < N`. For a complete chronological realization, telescope rank mass: complement/splitting/elementary operations conserve it, while each positive-column raw p16 occurrence contributes752 times its column multiplicity. Strict `P_N<NW_N` therefore requires at least one such raw occurrence. A separate lower-bound proof may combine that fact with the unchanged literal raw scalar word. The source bindings alone do not establish the resulting whole-integer cost inequality.

## Transfer boundary

None of these is a valid **H-only substitution** into PR4470's existing full upper certificate. PR4479 changes tensor, cutoff, compiler and outer slack; PR4483 changes the compiler itself; PR4533 changes its geometry. In particular the outer delta here is not PR4470's `1/1,400,000,000`. The sources themselves disclaim a smaller whole-multiplication input threshold or practical speedup. Lower-only bounds can be developed separately with the unchanged raw word and the same optimized-GMP upper reference, preserving every stated condition.

`bindings.json` contains compact exact parameters, raw source hashes, historical head comparisons and replay scope. `source_manifest` includes all saved inputs; optional failed filename probes in `download-manifest.json` are not required source inputs. No original PR4470 certificate or website files were modified.
