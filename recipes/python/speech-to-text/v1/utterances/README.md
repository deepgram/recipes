# Utterances (Speech-to-Text v1)

Split transcript into per-utterance segments with timing, providing natural breakpoints in spoken audio.

## What it does

When `utterances=True`, Deepgram splits the transcript into meaningful segments based on pauses
in speech. Each utterance includes its own transcript text, start/end timestamps, and confidence
score. This is useful for building subtitle tracks, conversation logs, or any UI that needs
timed text segments.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `utterances` | `True` | Enable utterance segmentation |
| `utt_split` | `0.8` | Seconds of silence to trigger a split (optional, default varies) |
| `model` | `"nova-3"` | Best model for utterance accuracy |

## Example output

```
[0.08s - 7.34s] Yeah, as much as it's worth celebrating the 50th anniversary...
[8.19s - 15.02s] We've come a long way since then...
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
