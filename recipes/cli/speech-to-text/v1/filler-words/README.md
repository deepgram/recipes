# Filler Words (STT v1)

Preserves filler words like "uh", "um", and "mhm" in the transcript output.

## What it does

The `filler_words` parameter tells Deepgram to keep filler words in the transcript rather than removing them. By default, Deepgram filters out hesitation sounds. Enabling this is useful for conversation analysis, linguistic research, or any use case where speech disfluencies carry meaning.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Deepgram transcription model |
| `filler_words` | `true` | Preserves filler words (uh, um, mhm) in output |
| `smart_format` | `true` | Enables smart formatting |

## Example output

```
Yeah, as much as, um, it's funny when I think of, uh, anything that's
related to outer space, I think of is the first, the first shuttle launch...
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
