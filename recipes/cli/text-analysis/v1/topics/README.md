# Topic Detection (Text Analysis v1)

Identifies topics discussed in plain text input without requiring audio.

## What it does

The `--topics` flag on `dg read` analyzes text to identify the key topics being discussed. Each detected topic includes a confidence score. This is useful for categorizing content, tagging articles, routing customer messages to the right department, and understanding what subjects are covered in a document.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--topics` | flag | Enables topic detection on the text |

## Example output

```
Topics:
  - Electric vehicles (0.95)
  - Battery technology (0.90)
  - Government policy (0.72)
```

## Prerequisites

- Deepgram CLI installed (`curl -fsSL https://deepgram.com/install.sh | sh`)
- `DEEPGRAM_API_KEY` environment variable set

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
