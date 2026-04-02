# Summarize (STT v1)

Generates a concise summary of the transcript.

## What it does

The `--summarize` flag tells Deepgram to produce a brief text summary of the audio content alongside the full transcript. The CLI displays both the transcript and the summary. This is useful for quickly understanding the gist of long recordings.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--model` | `nova-3` | Deepgram transcription model |
| `--summarize` | flag | Generates a summary of the transcript |

## Example output

```
Yeah, as much as, it's funny when I think of anything that's related to outer space...

Summary: The speakers discuss the history of space exploration, including the first shuttle launch and early spacewalks.
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
