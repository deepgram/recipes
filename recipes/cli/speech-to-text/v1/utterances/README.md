# Utterances (STT v1)

Splits the transcript into per-utterance segments with timing information.

## What it does

Enabling the `utterances` parameter tells Deepgram to return the transcript broken into discrete utterances, each with start and end timestamps. This is useful for subtitle generation and conversational analysis. Since the CLI does not expose a `--utterances` flag directly, this example uses `dg api` to pass the parameter.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Deepgram transcription model |
| `utterances` | `true` | Splits transcript into timed utterances |

## Example output

```
[0.08s] Yeah, as much as, it's funny when I think of anything that's related to outer space...
[15.64s] If you think about it, it was amazing that people were able to even put a shuttle together.
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
