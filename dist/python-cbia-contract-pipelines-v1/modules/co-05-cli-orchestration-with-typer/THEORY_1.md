# CLI and I/O Boundaries

## Theory

Command-line interfaces and file I/O are classic boundary layers. They translate human or system input into structured data and translate results back into artifacts or messages.

A clean CLI layer:
- Parses arguments
- Validates inputs
- Calls core logic
- Handles errors and exit codes

The CLI should not contain business logic. Its job is orchestration, not computation. This separation allows you to reuse the same core logic in scripts, services, or tests.

## Key Takeaways
- Treat CLI and I/O as boundary layers.
- Keep core logic reusable and independent.
- Use clear exit codes and error messages.
