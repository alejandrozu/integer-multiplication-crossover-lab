# Bounded fresh p16 arithmetic replays

`replay.py` authenticates the seven source files in `source-manifest.json`, then
runs separate PR4483 and PR4533 workers, each with a hard 90-second limit.
Run with Python 3.12 or later: `python -B replay.py`.

The PR4483 worker calls the upstream `rank-convergence/compiler.py::certify`
on the original p16 profile and original p16 witness. The PR4533 worker first
calls `adaptive-witness-retune/verify.py::check` on the retuned p16 witness,
then calls that same original compiler gate. These are finite rational-interval
checks. They do not form `2**H`, construct a uniform word, or replay the native
producer. Neither source has been modified. No upstream `--write` option is
invoked. The runner saves new receipts only in this directory.

`replay-results.json` contains full captured output and timing. `PASS` means
all gates requested in that worker completed successfully; a
`TIMEOUT_NOT_CERTIFIED` receipt means this bounded replay did not finish and
does not establish the unfinished gate. A completed-stage record in captured
output establishes only that named stage.

These replays do not strengthen or discharge the original native-word,
physical realization, all-column, or outer-algorithm contracts. The frozen
`../pr4470-descendant-bindings/bindings.json` is intentionally unchanged; its
bound SHA-256 is
`01ea6378adf40105e105acabd86a05e6810120a1a61b28c822002ebd1cafbd02`.
