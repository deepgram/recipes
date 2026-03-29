# Speaker Diarization (Speech-to-Text v1)

Identify and label individual speakers in a multi-speaker audio recording.

## What it does

When `diarize=True`, Deepgram assigns a numeric speaker label (0, 1, 2, ...) to each word
in the transcript. This lets you split the transcript by speaker, useful for call recordings,
interviews, meeting notes, and podcasts.

The speaker labels appear in the `words` array of the response, as a `speaker` field on each word.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `diarize` | `True` | Enable speaker identification |
| `model` | `"nova-3"` | Recommended for best diarization accuracy |

## Example output

```
[Speaker 0] Yeah as much as it's worth celebrating the 50th anniversary...

[Speaker 1] Absolutely and you know the technology has come so far...
```

## Notes

- Speaker numbers are assigned in order of first appearance (Speaker 0 speaks first)
- Not all audio has multiple speakers — single-speaker audio returns only Speaker 0
- For best results, use audio where speakers don't talk over each other

## Prerequisites

- Python 3.10+
- Set `DEEPGRAM_API_KEY` environment variable
- Install: `pip install -r samples/python/requirements.txt`

## Run

```bash
python example.py
```

## Test

```bash
pytest example_test.py -v
```
