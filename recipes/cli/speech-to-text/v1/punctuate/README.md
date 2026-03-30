# Punctuation (Speech-to-Text v1)

Adds punctuation marks to the transcript for improved readability and sentence structure.

## What it does

Enables the `punctuate` parameter which inserts periods, commas, question marks, and other punctuation into the transcript. Without this, the output is a continuous unpunctuated stream of words.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Highest-accuracy transcription model |
| `punctuate` | `true` | Inserts punctuation marks into the transcript |

## Example output

```
Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk, it's also worth noting...
```

## Prerequisites

- `curl` and `python3` installed
- Set `DEEPGRAM_API_KEY` environment variable

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
