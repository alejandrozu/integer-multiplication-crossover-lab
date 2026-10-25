# Integer multiplication crossover lab

An interactive, source-linked audit of conditional integer-multiplication
constructions and their feasibility against a fixed optimized GMP reference.

**[Public website](https://alejandrozu.github.io/integer-multiplication-crossover-lab/)** ·
**[Methods and assumptions](https://alejandrozu.github.io/integer-multiplication-crossover-lab/methodology.html)** ·
**[Public reproduction downloads](https://github.com/alejandrozu/integer-multiplication-crossover-lab/releases)**

This repository contains the public release export and publication infrastructure.
The working directory and unpublished research are excluded.

## What the frozen 222 checkpoint establishes

The tracked history contains 595 entries:

| Disposition | Entries |
| --- | ---: |
| Conditional numerical bounds | 222 |
| Individually reviewed scope/component dispositions | 196 |
| Cost obligations still open | 177 |

Among the numerical entries, 195 have a sufficient upper endpoint, 62 have a
meaningful necessary lower endpoint, and 35 have both. These are source-specific
conditional bounds in the declared XAG circuit model, compared with the same
repaired GMP6.3/native-Skylake reference. AND costs 1 and XOR costs a fixed positive
tariff rho. They are not measured hardware runtimes.

A sufficient upper proves that a particular counted realization wins above its
verified domain, under its listed source, compiler, native/operator and analytic
assumptions. A necessary lower applies to the explicitly declared realization
family. Neither endpoint locates an exact first crossover. No claim is made
that all implementations of a PR, or all 177 unfinished entries, have been priced.

This update adds 19 entries with numerical bounds while preserving every numerical endpoint from the published 203-entry snapshot. Since the earlier 196-entry snapshot, 26 entries gained bounds and 11 received source-scope dispositions. The smallest sufficient cutoff remains unchanged; these additions do not establish practical feasibility.

The site preserves frozen historical quotations, exact source-head and artifact
hashes, qualifications, proof files, AI peer receipts and reproducible checks.
It distinguishes a source-selected new circuit realization from the historical
implementation when they differ. Source/code checks and AI reviews do not
replace the individual remaining mathematical assumptions, a formal proof or
independent human review.

## Reproduce without a private service

The [frozen public release](https://github.com/alejandrozu/integer-multiplication-crossover-lab/releases/tag/audit-2026-10-25-02) supplies the current `reproduction-package.json`, `restore_reproduction.py`, verification receipt and new archive parts. The manifest links all 26 required `operation-audit-objects-*.zip` parts (43–68). Parts 43–66 retain their original public release URLs; parts 67–68 belong to this update. All downloads are public GitHub assets.
The manifest binds each archive and every restored source/proof path by SHA256;
the restore tool checks those bindings before writing a new output directory.

After downloading every archive linked by the current manifest, the manifest itself and the restore tool into a single directory:

```sh
python restore_reproduction.py --package-dir . --output restored-audit
```

Use Python 3.12 or later. The packages use only standard-library archive support
for restoration, including ZIP-LZMA. Restoration authenticates exact bytes;
the mathematical claims retain their individually stated assumptions. The
release notes identify the checked snapshot and its offline verification result.

The verification receipt records exact reconstruction and offline checks for this snapshot. Unchanged published source jobs are inherited only when their transitive byte bindings match. New cost schedules replay offline. PR646's native construction is reused through its closed prior execution receipt and exact source/output bindings; this publication does not claim a fresh repeat of those native constructors and destructive controls. The retained PR2077 provenance refresh and its correction audit remain available; no scientific bound is changed by that refresh.

The [PR646 authentication tool](tools/authenticate_pr646_native_component.py) checks that historical component against restored bytes. It authenticates the earlier AI review's execution attestation; byte equality alone does not prove that execution occurred. The original full native reconstruction remains available among the restored scripts.

## Publication

`site/` is the static GitHub Pages export. The Pages workflow publishes that
directory only. Large reproduction archives are release assets, rather than
Git history. Every public deployment is tied to its Git commit; release assets
also carry their own exact manifest hashes.

## Attribution and licenses

The audited source constructions originate in
[CrocSwap/integer-mult-bounds](https://github.com/CrocSwap/integer-mult-bounds)
and its cited contributors and dependencies. Original authorship, notices,
licenses and source provenance remain attached to the restored artifacts.
This publication does not relicense those upstream artifacts or imply their
authors endorse this audit. The audit and explanatory interfaces disclose their
AI assistance and conditional scope.
