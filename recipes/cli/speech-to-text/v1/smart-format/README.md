# Smart Format (STT v1)

Automatically formats transcript output for readability — numbers, dates, currencies, and punctuation.

## What it does

The `--smart-format` flag enables Deepgram's smart formatting engine. It converts spoken numbers to digits ("twenty one" → "21"), formats dates, adds currency symbols, applies proper punctuation, and capitalizes sentences. This produces a much more readable transcript without any post-processing.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--model` | `nova-3` | Deepgram transcription model |
| `--smart-format` | flag | Enables smart formatting (on by default in the CLI) |

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
