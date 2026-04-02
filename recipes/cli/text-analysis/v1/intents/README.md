# Intent Recognition (Text Analysis v1)

Detects intents from plain text input without requiring audio.

## What it does

The `--intents` flag on `dg read` analyzes text to identify what the speaker or author is trying to accomplish. Intent recognition detects goals such as making a request, asking a question, filing a complaint, or seeking information. Each detected intent includes a confidence score. This is useful for routing customer messages, analyzing feedback, and building text-based automation.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--intents` | flag | Enables intent recognition on the text |

## Example output

```
Intents:
  - Cancel subscription (0.92)
  - Request refund (0.88)
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
