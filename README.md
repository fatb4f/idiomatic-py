# CBIA Course Repo (Content-Generation Ready)

This is a **contentless** course repo skeleton:
- course structure is declared in SSOT (`ssot-input/course.json`)
- references are declared (`ssot-input/references.json`)
- LLM generates SSOT content blocks into `ssot-input/content/`
- CGP (as git submodule) validates + renders into `dist/`

## Layout
```
.
├─ AGENTS.md
├─ ssot/                      # git submodule (ssot-template CGP v0)
├─ ssot-input/
│  ├─ course.json
│  ├─ references.json
│  └─ content/
├─ snapshots/                 # optional
└─ dist/
```

## Quick start
1) Add the SSOT submodule:

```bash
git submodule add <SSOT_TEMPLATE_REPO_URL> ssot
```

2) Create a virtualenv and install CGP from the submodule:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e "./ssot[dev]"
```

3) Generate content blocks (LLM) into `ssot-input/content/` following:
- `ssot/docs/generation-prompt-contract.md`
- `ssot/schemas/content-block.schema.json`

4) Validate + build:

```bash
make validate
make build
```
