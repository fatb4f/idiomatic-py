# AGENTS

## Non-negotiable rules
- Do not invent content. If references are insufficient, emit `status: needs_reference`.
- Every generated section must include `source_refs` (no source-free claims).
- Do not re-sequence CBIA objectives.
- Do not provide full solutions unless explicitly asked.

## Preferred outputs
- SSOT content blocks validating against `ssot/schemas/content-block.schema.json`.
- Minimal Lecture Layer (micro-lecture + key points + pitfalls) around each section.
