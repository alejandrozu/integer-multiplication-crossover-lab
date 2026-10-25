# Contribute to the crossover lab

Help refine the analysis, complete an open entry, or improve the explanation and charts.

The audit is incomplete. Its published endpoints are conditional bounds for specified circuit realizations, not measured runtimes or exact first crossovers. The current snapshot has 222 numerical entries and 177 open cost analyses.

## Start with an issue

[Report an error or propose an analysis](https://github.com/alejandrozu/integer-multiplication-crossover-lab/issues/new/choose). A short report is useful. Include the upstream PR number, the source-card or file link, what you think needs changing, and any supporting calculation or source. You do not need a completed proof or a local build to open a discussion.

Check the [current history](https://alejandrozu.github.io/integer-multiplication-crossover-lab/#pr=4470&tab=frontier) and [methods](https://alejandrozu.github.io/integer-multiplication-crossover-lab/methodology.html) first. Entries without bounds are open work, not zero-cost constructions.

## Submit a pull request

Fork this repository and open a pull request against `main`. GitHub's web editor is enough for documentation changes. For a new cost analysis, add a small folder under `contributions/pr-NUMBER/` with your explanation, source links and reproducible calculation. Draft pull requests are welcome.

A useful analysis identifies the exact upstream commit, the counted realization, the computation model and every remaining assumption. Distinguish an upper schedule, a lower bound for a declared family, and an exact crossover. Explain any difference from the construction originally submitted upstream. Compare against the same documented reference, or clearly label a different comparison.

For a new two-sided range, show that both endpoints apply to the same realization or declared family. An improved upper alone does not establish a real-world speedup or a lower bound on the crossover.

## Keep the frozen evidence reproducible

Existing source, proof and certificate files have SHA256 bindings. Propose a new revision with a new filename and identify what it supersedes. Avoid rewriting historical evidence or regenerating release archives for an initial contribution. The maintainer can integrate an accepted analysis into the bound data and both graphs.

For chart or interface changes, describe how you checked the affected behavior. Documentation-only changes do not require the mathematical replay suite.

The static website is in `site/`. To preview it locally, run `python -m http.server 8000 --directory site` from this repository, then visit `http://localhost:8000`.

## Review and attribution

Issues and pull requests are public. Contributions are reviewed before they appear in the published graphs. Include attribution for ideas and sources, disclose material AI assistance and preserve third-party licenses and notices. Submission does not imply review or endorsement by an upstream author.

Original code and explanatory material are licensed under [Apache 2.0](LICENSE). Intentionally submitted contributions are covered by its contribution terms unless explicitly stated otherwise. Identify any third-party material and preserve its original license. See [NOTICE](NOTICE) for scope and attribution.
