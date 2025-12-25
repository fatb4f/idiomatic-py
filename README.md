# CBIA Track Tooling Pack (uv + direnv, activated venv)

## Requirements
- `uv`
- `direnv`
- `zellij` (optional)
- `just` (optional, recommended)
- `hx` and `yazi` (optional)

## One-time shell hook
### fish
```fish
direnv hook fish | source
```

### bash
```bash
eval "$(direnv hook bash)"
```

### zsh
```zsh
eval "$(direnv hook zsh)"
```

## Activate project environment
From repo root:
```bash
direnv allow
```

This will:
- create `.venv` using `uv`
- install dependencies
- export `VIRTUAL_ENV` and prepend `.venv/bin` to `PATH`

## Quick commands
### With just
```bash
just bootstrap
just health
just repl
just test
just type
just lint
just fmt
```

### Without just
```bash
python -c "import sys; print(sys.executable)"
pytest -q
ipython
pyright
ruff check .
ruff format .
```

## Zellij layout
```bash
zellij --layout layouts/cbia.kdl
```

If panes warn `VIRTUAL_ENV not set`, run:
```bash
direnv allow
```
and restart the session (or open a new pane).
