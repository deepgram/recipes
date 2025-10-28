# Generate Python SDK examples

Generate standalone markdown documents that show how to make a given request to the Deepgram API using the Python SDK. The output must be copy/paste-ready and self-contained, without referring to example files, repository paths, or project-specific run commands.

## Information Architecture (IA)

- Mimic the exact directory structure of the specific examples directory `sources/Python-SDK-Examples/examples`.
- If a doc file already exists at the target path, you MUST update it in place to reflect the latest instructions and SDK behavior. Do not create duplicates.
  1. Ensure it follows ALL rules in this document and the workspace rules.
  2. Ensure the SDK call stack and options match the current source example behavior (examples are the source of truth).
  3. If the example reflects product or model updates, revise the doc accordingly to highlight the change.
  4. Modify existing docs to align with any changes in these instructions, the SDK, the examples, or the rules.

## Code Generation

- Treat the example code as the source of truth for SDK calls and parameters.
- Produce minimal, copy/paste-ready snippets that are self-contained and runnable in a fresh file.
- Do NOT include repository-specific paths, `cd` commands, or `python main.py`-style run steps inside the doc.
- Do NOT instruct the user to open or rely on the example file; replicate the relevant SDK usage directly.
- Briefly indicate where optional or additional request parameters can be provided.
- Focus on the SDK usage and expected outcome of the call.

## Document Generation

- Each doc is a self-contained "how to make this request with the Python SDK" guide.
- Do NOT reference example filenames, directories, or repo layout. Avoid all run steps tied to the examples.
- Include a short prerequisites section only when necessary (e.g., Python version, installing the SDK, setting `DEEPGRAM_API_KEY`).
- Show a single, clear learning objective and a minimal end-to-end code snippet that a user can copy into a new file and run.
- Use semantic markdown rules.
- Use code fencing with language hints (e.g., ```python) — never indentation-based code blocks.

### Prohibited content in the generated docs

- Any mention of example file paths (e.g., `sources/...`, `examples/...`).
- Any repo navigation or run commands (e.g., `cd ...`, `python main.py`).
- Instructions that require modifying the example files.

### Existing docs update policy

- If a doc already exists, revise its content to conform to these rules and to reflect changes in the SDK, examples, or product behavior.
- Preserve the file path and structure, but update headings, narrative, and code to match current best practice and signatures.

## Purpose

- This should provide human-readable markdown examples of interacting with Deepgram.
- It will produce markdown files.
- It will be indexed by an Agentic AI Support service.
- It will likely be published using GitHub pages for additional discovery.
