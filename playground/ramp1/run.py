"""Ramp 1 runner: proves 'pure core, I/O at edges'.

Usage:
  python playground/ramp1/run.py --in data/in.json --out data/out.json
"""

from __future__ import annotations

import argparse
from pathlib import Path

from operators.core_ops import normalize_numbers, summarize
from operators.io_json import dump_json, load_json, parse_numbers


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="in_path", required=True, help="Input JSON file")
    ap.add_argument("--out", dest="out_path", required=True, help="Output JSON file")
    args = ap.parse_args()

    raw = load_json(args.in_path)
    xs = parse_numbers(raw)

    ys = normalize_numbers(xs)
    report = summarize(ys)

    dump_json(args.out_path, {"normalized": ys, "summary": report})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
