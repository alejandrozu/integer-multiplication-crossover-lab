# Integer multiplication crossover lab

An interactive, source-linked audit of conditional integer-multiplication
constructions and their feasibility against a fixed optimized GMP reference.

**[Public website](https://alejandrozu.github.io/integer-multiplication-crossover-lab/)** ·
**[Methods and assumptions](https://alejandrozu.github.io/integer-multiplication-crossover-lab/methodology.html)** ·
**[Public reproduction downloads](https://github.com/alejandrozu/integer-multiplication-crossover-lab/releases)**

This repository contains the public release export and publication infrastructure.
The working directory and unpublished research are excluded.

## What the frozen 196 checkpoint establishes

The tracked history contains 595 entries:

| Disposition | Entries |
| --- | ---: |
| Conditional numerical bounds | 196 |
| Individually reviewed scope/component dispositions | 185 |
| Cost obligations still open | 214 |

Among the numerical entries, 183 have a sufficient upper endpoint, 42 have a
meaningful necessary lower endpoint, and 29 have both. These are source-specific
conditional bounds in the declared XAG circuit model, compared with the same
repaired GMP6.3/native-Skylake reference. AND costs 1 and XOR costs a fixed positive
tariff rho. They are not measured hardware runtimes.

A sufficient upper proves that a particular counted realization wins above its
verified domain, under its listed source, compiler, native/operator and analytic
assumptions. A necessary lower applies to the explicitly declared realization
family. Neither endpoint locates an exact first crossover. No claim is made
that all implementations of a PR, or all 214 unfinished entries, have been priced.

The site preserves frozen historical quotations, exact source-head and artifact
hashes, qualifications, proof files, AI peer receipts and reproducible checks.
It distinguishes a source-selected new circuit realization from the historical
implementation when they differ. Source/code checks and AI reviews do not
replace the individual remaining mathematical assumptions, a formal proof or
independent human review.

## Reproduce without a private service

The [frozen public release](https://github.com/alejandrozu/integer-multiplication-crossover-lab/releases/tag/audit-196-2026-10-24) contains twenty
`operation-audit-objects-*.zip` parts (43–62), `reproduction-package.json`,
`restore_reproduction.py` and the offline verification receipt. All downloads
are public GitHub assets.
The manifest binds each archive and every restored source/proof path by SHA256;
the restore tool checks those bindings before writing a new output directory.

After downloading every asset from one release into a single directory:

```sh
python restore_reproduction.py --package-dir . --output restored-audit
```

Use Python 3.12 or later. The packages use only standard-library archive support
for restoration, including ZIP-LZMA. Restoration authenticates exact bytes;
the mathematical claims retain their individually stated assumptions. The
release notes identify the checked snapshot and its offline verification result.

The final receipt passes 103 recorded checks, authenticates 20,096 restored paths
and compares 470 certificate files. It explicitly records published inheritance
and a separately reviewed four-field PR2077 provenance refresh. It does not
claim every unchanged job was rerun after that refresh. The site links the
exact correction audit and preserves the scientific bounds.

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
