# Topic Detection (Audio Intelligence v1)

Identifies key topics discussed in audio content.

## What it does

The `--topics` flag enables topic detection which scans the transcript and identifies the main topics being discussed. Each topic is returned with a confidence score. This is useful for categorising recordings, building content indexes, and understanding conversation themes.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--model` | `nova-3` | Required model for audio intelligence |
| `--topics` | flag | Enables topic detection |

## Example output

```
Yeah, as much as, it's funny when I think of anything that's related to outer space...

Topics: space exploration, shuttle launch, spacewalk
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
