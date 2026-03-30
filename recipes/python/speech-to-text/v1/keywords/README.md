# Keyword Boosting (Speech-to-Text v1)

Boost recognition accuracy for specific words or phrases that the model might otherwise miss or mishear.

## What it does

Keyword boosting lets you provide a list of words with intensity values. Positive intensity makes the model more likely to recognise that word; negative intensity suppresses it. This is especially useful for proper nouns, brand names, technical jargon, or uncommon words.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `keywords` | `"Deepgram:2"` | Word(s) to boost with intensifier (-10 to 10). Pass a list for multiple keywords. |
| `model` | `"nova-3"` | Transcription model |
| `smart_format` | `True` | Format numbers, dates, etc. |

## Example output

```
Yeah, as much as it's worth celebrating the 50th anniversary of
the spacewalk, it's also worth noting that we've come a long way
since then...
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
