# Numerals (STT v1)

Converts spoken numbers to numeric digits in the transcript output.

## What it does

The `numerals` parameter tells Deepgram to convert spoken number words into their numeric digit form. For example, "twenty one" becomes "21", "three hundred forty five" becomes "345", and "two point five" becomes "2.5". This is a more targeted alternative to `smart_format` when you only need number conversion without other formatting changes.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Deepgram transcription model |
| `numerals` | `true` | Converts spoken numbers to digits |

## Example output

```
Yeah, as much as, it's funny when I think of anything that's related to
outer space. I think of is the 1st, the 1st shuttle launch...
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
