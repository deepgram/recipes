# Intent Recognition (Speech-to-Text v1)

Detect speaker intents in audio — what the speaker is trying to accomplish in each segment.

## What it does

When `intents=True`, Deepgram analyzes the transcript and identifies the intents behind what
is being said. Each segment receives one or more intent labels with confidence scores. This is
useful for analyzing customer service calls, voice commands, or any scenario where understanding
speaker goals matters.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `intents` | `True` | Enable intent recognition |
| `custom_intent` | `["inform"]` | Optional: custom intents to detect |
| `custom_intent_mode` | `"extended"` | Optional: detect custom + auto intents |
| `model` | `"nova-3"` | Best model for transcription quality |

## Example output

```
Intents: inform (0.92), educate (0.78)
  Text: Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk...
```

## Prerequisites

- Python 3.10+
- Set `DEEPGRAM_API_KEY` environment variable
- Install: `pip install -r recipes/python/requirements.txt`

## Run

```bash
python example.py
```

## Test

```bash
pytest example_test.py -v
```
