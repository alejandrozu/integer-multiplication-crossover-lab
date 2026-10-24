#!/usr/bin/env python3
"""Regenerate one exact p7 mask with authenticated original factor code."""
from hashlib import sha256
from pathlib import Path
import importlib.util
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PINS = {
    'research/kappa-rebuild/bit/complex_controller_factor.py': '1de9aaf918e6a4f2f5448754c1f3c3da3b85e6257849ebd097af09859c4e5497',
    'research/kappa-rebuild/bit/mixed_productive_bit.py': 'b32291b0db7fc0d332ec444c70746ab0fb03351d2e50546f8bcb64060e3ff95e',
    'research/kappa-0023-productive-jobs/dependencies/kappa-next-regime/bit-compression/carrier-reuse/reference/joint_pair_dag.py': '8a0de761642d21919e969475c3f13e5d01a4bae7343c1e1f37c586d94b676a85',
}
RECEIPT_SHA256 = '6f96f6be5d8441f71cbe6ebb1657c69b543eb085b848b92b591b7ac01d6e6598'


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def run(source_root):
    root = Path(source_root).resolve()
    for relative, expected in PINS.items():
        if sha256((root/relative).read_bytes()).hexdigest() != expected:
            raise AssertionError('Original factor source changed: '+relative)
    paths = list(PINS)
    # Explicit imports avoid the original generator's historical reference path.
    load(root/paths[2], 'joint_pair_dag')
    load(root/paths[1], 'mixed_productive_bit')
    generator = load(root/paths[0], 'original_complex_controller_factor')
    coefficients, events, idles = generator.controller(7, 232127)
    factored = generator.factor(coefficients)
    if factored is None:
        raise AssertionError('The chosen p7 mask has no exact factorization')
    case = generator.serialize_case(7, 232127, coefficients, events, idles, factored)
    receipt = HERE/'P7-FACTOR.json'
    if sha256(receipt.read_bytes()).hexdigest() != RECEIPT_SHA256:
        raise AssertionError('Checked p7 factor receipt changed')
    # JSON normalizes integer histogram keys in the freshly generated case.
    if json.loads(json.dumps(case)) != json.loads(receipt.read_text()):
        raise AssertionError('Fresh exact factorization differs from the receipt')
    return json.loads(receipt.read_text()), dict(PINS)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, default=HERE/'source')
    args = parser.parse_args()
    case, pins = run(args.source_root)
    print(json.dumps({'status': 'PASS_EXACT_FIXED_MASK_REGENERATION',
                      'p': case['pairs'], 'keep': case['keep_idle_mask'],
                      'coefficient_matrices': len(case['coefficient_matrices']),
                      'receipt_sha256': RECEIPT_SHA256, 'source_sha256': pins}, sort_keys=True))
