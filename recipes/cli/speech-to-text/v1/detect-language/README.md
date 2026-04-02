# Language Detection (STT v1)

Automatically detects the spoken language in the audio.

## What it does

Enabling the `detect_language` parameter tells Deepgram to identify the language being spoken before transcribing. The detected language code is returned in the response alongside the transcript. This is useful when processing audio from unknown or multilingual sources.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Deepgram transcription model |
| `detect_language` | `true` | Enables automatic language detection |

## Example output

```
Detected: en
Transcript: Yeah, as much as, it's funny when I think of anything that's related to outer space...
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
