# Testing and Determinism

## Theory

Testing is easiest when code is deterministic. Deterministic code produces the same result every time for the same input, making failures meaningful and reproducible.

Unit tests should target operators, not pipelines. When operators are pure, tests are fast, isolated, and expressive. Integration tests can then focus on verifying wiring and boundaries.

In operational systems, determinism is also a safety feature. It allows you to reproduce failures, reason about changes, and trust automation.

## Key Takeaways
- Test pure operators first.
- Favor many small tests over few large ones.
- Determinism makes failures diagnosable.
