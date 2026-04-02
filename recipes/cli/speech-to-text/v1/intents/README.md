# Intent Recognition (STT v1)

Detects speaker intents in the transcript.

## What it does

Enabling the `intents` parameter tells Deepgram to analyse the transcript and identify the speaker's intents for each segment. Each intent is returned with a confidence score. This is useful for call centre analytics and customer service automation.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Deepgram transcription model |
| `intents` | `true` | Enables intent recognition |

## Example output

```
inform_about_experience (confidence: 0.92)
share_opinion (confidence: 0.87)
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
