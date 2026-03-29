# Summarize (Speech-to-Text v1)

Generate a concise text summary of the transcribed audio content.

## What it does

When `summarize="v2"`, Deepgram analyzes the full transcript and produces a short summary
capturing the key points. This is an Audio Intelligence feature that processes the transcript
after transcription. It returns both an overall summary and per-segment summaries for longer
audio.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `summarize` | `"v2"` | Enable summarization (must be the string "v2", not a boolean) |
| `model` | `"nova-3"` | Best model for transcription quality |

## Example output

```
Summary: A discussion about the 50th anniversary of the spacewalk and advances in space technology.
  Segment: The speakers discuss the significance of the spacewalk anniversary...
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
