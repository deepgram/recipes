# Text Summarization (Text Analysis v1)

Generates a concise summary from plain text input without requiring audio.

## What it does

The `--summarize` flag on `dg read` produces a short, readable summary of the input text. This is useful for condensing long documents, articles, meeting notes, or any text content into a brief overview. The summary captures the key points and main ideas from the source material.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--summarize` | flag | Enables text summarization |

## Example output

```
Summary:
  Deepgram is a speech AI company offering transcription, text-to-speech,
  and audio intelligence APIs for developers building voice applications.
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
