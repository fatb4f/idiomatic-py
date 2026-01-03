# Ramp 1 — ptpython execution surface (repo-local)

## Scope lock (do this first)
Ramp 1 scope is **co-01 only**. Modules **co-02+ are locked** until Ramp 1 is complete.

Definition of “complete”:
- You can run `normalize_numbers` and `summarize` in a REPL without friction
- You can prove purity (deterministic output + no input mutation)
- You can run the JSON edge runner end-to-end

## Quickstart

### 1) Install deps (uv)
```bash
uv sync
```

### 2) Start ptpython (from repo root)
```bash
ptpython
```

### 3) REPL reps (copy/paste)
```python
from operators.core_ops import normalize_numbers, summarize

xs = [3, -1, 2, 2, 0]
ys = normalize_numbers(xs)
ys, xs  # confirm new list + input unchanged

summarize(ys)
```

### 4) Purity harness (repeatable)
```bash
python playground/ramp1/purity_harness.py
```

### 5) JSON boundary runner (I/O at edges)
Create input:
```bash
mkdir -p playground/ramp1/data
cat > playground/ramp1/data/in.json <<'JSON'
{"numbers":[3,-1,2,2,0]}
JSON
```

Run:
```bash
python playground/ramp1/run.py --in playground/ramp1/data/in.json --out playground/ramp1/data/out.json
cat playground/ramp1/data/out.json
```

## Rules (enforced by convention)
- Operators in `operators/core_ops.py` remain **pure** (no I/O, no prints, no env)
- JSON parsing and file operations stay in `operators/io_json.py`
- `playground/` is **non-canonical**: execution-only, not rendered into `dist/`
