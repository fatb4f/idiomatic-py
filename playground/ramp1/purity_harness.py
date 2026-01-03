"""Ramp 1 purity harness.

Run:
  python playground/ramp1/purity_harness.py
"""

from __future__ import annotations

from operators.core_ops import normalize_numbers, summarize


def assert_pure() -> None:
    xs = [3, -1, 2, 2, 0]
    xs_before = list(xs)

    a1 = normalize_numbers(xs)
    a2 = normalize_numbers(xs)

    assert a1 == a2
    assert xs == xs_before  # input unchanged

    s1 = summarize(a1)
    s2 = summarize(a2)

    assert s1 == s2
    assert xs == xs_before


if __name__ == "__main__":
    assert_pure()
    print("OK: purity verified")
