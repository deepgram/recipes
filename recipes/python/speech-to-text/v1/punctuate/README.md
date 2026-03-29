# Punctuation (Speech-to-Text v1)

Add punctuation and capitalization to transcript output for improved readability.

## What it does

When `punctuate=True`, Deepgram inserts commas, periods, question marks, and other punctuation
into the transcript. It also applies proper capitalization at sentence boundaries. This is a
lighter-weight option than `smart_format`, which also formats numbers, dates, and currencies.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `punctuate` | `True` | Enable punctuation and capitalization |
| `model` | `"nova-3"` | Best model for punctuation accuracy |

## Example output

```
Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk,
it's also worth noting that we've come a long way since then.
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
