# Topic Detection (STT v1)

Identifies topics discussed in the audio.

## What it does

The `--topics` flag enables Deepgram's topic detection which scans the transcript and identifies the key topics being discussed. Each topic is returned with a confidence score. This is useful for categorising and indexing audio content.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--model` | `nova-3` | Deepgram transcription model |
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
