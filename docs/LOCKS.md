# Locks and progression gates

## Ramp 1 lock
- Allowed module: **co-01**
- Locked modules: **co-02, co-03, co-04, co-05, co-06, co-07**

Unlock condition: Ramp 1 completion criteria in `docs/RAMP1_PTPYTHON.md`.

## Why
Prevent scope creep. Ramp 1 is REPL fluency + purity + boundary I/O only.
