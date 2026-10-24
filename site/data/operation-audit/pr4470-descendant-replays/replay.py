"""Bounded, p16-only replays of unchanged upstream finite arithmetic gates.

No native huge word is generated. The runner never invokes --write and never
changes the frozen descendant bindings. Each PR worker has a 90-second limit.
"""
import argparse
import copy
import datetime
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE / "sources"


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def worker(pr):
    cases = json.loads((ROOT / "research/rank-convergence/BENCHMARKS.json").read_text(encoding="utf-8"))["cases"]
    case = next(c for c in cases if c["name"] == "p16")
    data = json.loads((ROOT / case["source"]).read_text(encoding="utf-8"))
    if case["profile_key"]:
        data = data[case["profile_key"]]
    comp = module("rank_convergence_compiler", ROOT / "research/rank-convergence/compiler.py")
    output = {"pr": pr, "profile": "p16", "word_materialized": False, "native_producers_replayed": False}
    if pr == 4483:
        output["compiler"] = comp.certify({"targets": data["targets"], "paid": data["paid"]}, case["witness"])
        assert output["compiler"]["H"] == 2800000000
    else:
        case = copy.deepcopy(case)
        case["witness"] = json.loads((ROOT / "research/adaptive-witness-retune/WITNESS-p16.json").read_text(encoding="utf-8"))
        check = module("adaptive_witness_retune", ROOT / "research/adaptive-witness-retune/verify.py")
        output["retune_gate"] = check.check(case)
        # Emit progress so a bounded timeout can preserve an already-completed
        # independent retune gate without reporting the compiler as complete.
        print(json.dumps({"completed_stage": "retune_gate", "result": output["retune_gate"]}), flush=True)
        output["compiler"] = comp.certify({"targets": data["targets"], "paid": data["paid"]}, case["witness"])
        assert output["compiler"]["H"] == 1587000000
    assert output["compiler"]["status"] == "PASS_ADAPTIVE_HEIGHT_DIRECT_COMPILER"
    print(json.dumps({"completed_stage": "all_requested_gates", "result": output}), flush=True)


def run(pr):
    start = time.monotonic()
    command = [sys.executable, "-B", str(Path(__file__).resolve()), "--worker", str(pr)]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONUTF8="1")
    result = {"pr": pr, "timeout_seconds": 90, "command": command, "writes_upstream_sources": False,
              "frozen_bindings_modified": False, "native_word_materialized": False}
    try:
        p = subprocess.run(command, cwd=HERE, capture_output=True, text=True, encoding="utf-8", timeout=90, env=env)
        result.update(status="PASS" if p.returncode == 0 else "FAIL", returncode=p.returncode,
                      stdout=p.stdout, stderr=p.stderr)
    except subprocess.TimeoutExpired as exc:
        def text(value):
            return value.decode("utf-8", errors="replace") if isinstance(value, bytes) else (value or "")
        result.update(status="TIMEOUT_NOT_CERTIFIED", stdout=text(exc.stdout), stderr=text(exc.stderr))
    result["elapsed_seconds"] = round(time.monotonic() - start, 6)
    (HERE / f"replay-{pr}.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k not in ("stdout", "stderr")}), flush=True)
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--worker", type=int, choices=(4483, 4533))
    args = ap.parse_args()
    if args.worker:
        worker(args.worker)
        return
    manifest = json.loads((HERE / "source-manifest.json").read_text(encoding="utf-8"))
    for row in manifest["files"]:
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["sha256"], row["path"]
    results = [run(4483), run(4533)]
    receipt = {"schema_version": 1, "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
               "scope": "Original finite p16 arithmetic gates only; conditional source contracts remain unchanged.",
               "source_manifest_sha256": hashlib.sha256((HERE / "source-manifest.json").read_bytes()).hexdigest(),
               "source_file_hashes_checked": len(manifest["files"]), "results": results}
    (HERE / "replay-results.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
