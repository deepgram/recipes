# Topic Detection (Speech-to-Text v1)

Identify the key topics discussed in audio, with confidence scores for each detected topic.

## What it does

When `topics=True`, Deepgram analyzes the transcript and identifies the topics being discussed
in each segment of the audio. Each topic comes with a confidence score. You can also supply
custom topics to look for using the `custom_topic` parameter.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `topics` | `True` | Enable topic detection |
| `custom_topic` | `["topic1"]` | Optional: custom topics to detect |
| `custom_topic_mode` | `"extended"` | Optional: detect custom + auto topics |
| `model` | `"nova-3"` | Best model for transcription quality |

## Example output

```
Topics: space exploration, technology
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
