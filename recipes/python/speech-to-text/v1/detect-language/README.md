# Language Detection (Speech-to-Text v1)

Automatically detect the dominant spoken language in audio without specifying it upfront.

## What it does

When `detect_language=True`, Deepgram analyzes the audio and identifies the primary language
being spoken. The detected language is returned as a BCP-47 code (e.g., "en", "es", "fr") in
the channel metadata. This is useful when processing multilingual audio or audio of unknown
language origin.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `detect_language` | `True` | Enable automatic language detection |
| `model` | `"nova-3"` | Best model for language detection accuracy |

## Example output

```
Detected language: en
Transcript: Yeah, as much as it's worth celebrating the 50th anniversary...
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
