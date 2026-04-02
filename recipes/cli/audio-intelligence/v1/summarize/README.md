# Audio Summarization (Audio Intelligence v1)

Generates a concise text summary of spoken content.

## What it does

The `--summarize` flag enables Deepgram's summarization engine which produces a brief text summary alongside the full transcript. This is useful for generating meeting notes, podcast summaries, and quick overviews of long recordings.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--model` | `nova-3` | Required model for audio intelligence |
| `--summarize` | flag | Enables audio summarization |

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
