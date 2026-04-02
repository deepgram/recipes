# Punctuation (STT v1)

Adds punctuation marks to the transcript automatically.

## What it does

The `--punctuate` flag tells Deepgram to insert periods, commas, question marks, and other punctuation into the transcript based on speech patterns and pauses. This is enabled by default in the CLI but shown explicitly here.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--model` | `nova-3` | Deepgram transcription model |
| `--punctuate` | flag | Enables automatic punctuation |

## Example output

```
Yeah, as much as, it's funny when I think of anything that's related to
outer space, I think of is the first, the first shuttle launch...
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
