# Utterances (Speech-to-Text v1)

Splits transcription output into individual utterance segments with timing information.

## What it does

The `--utterances` flag tells Deepgram to segment the transcript into discrete utterances — natural units of speech separated by pauses. Each utterance includes start and end timestamps. This is useful for generating subtitles, analyzing conversation flow, or processing speech turn-by-turn.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--model` | `nova-3` | Specifies the Nova 3 transcription model |
| `--utterances` | (flag) | Enables utterance segmentation with timestamps |

## Example output

```
[0.00 - 4.56] Yeah, as confirmed, I'd like to inform you that we have had temporary loss of communication with the ISS.
[5.12 - 8.94] The crew has been working on repairs to the communication system.
```

## Prerequisites

- Deepgram CLI installed (`curl -fsSL https://deepgram.com/install.sh | sh`)
- Set `DEEPGRAM_API_KEY` environment variable

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```