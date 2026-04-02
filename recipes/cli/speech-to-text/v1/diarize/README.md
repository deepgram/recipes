# Speaker Diarization (STT v1)

Identifies and labels individual speakers in the audio.

## What it does

The `--diarize` flag enables speaker diarization which assigns a speaker label to each segment of the transcript. The CLI automatically formats the output with `[Speaker 0]`, `[Speaker 1]`, etc. prefixes. This is useful for meeting transcripts, interviews, and multi-speaker recordings.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--model` | `nova-3` | Deepgram transcription model |
| `--diarize` | flag | Enables speaker identification |

## Example output

```
[Speaker 0] Yeah, as much as, it's funny when I think of anything that's related to outer space...
[Speaker 1] If you think about it, it was amazing that people were able to even put a shuttle together.
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
