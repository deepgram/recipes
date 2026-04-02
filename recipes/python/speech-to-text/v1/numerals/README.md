# Numerals (Speech-to-Text v1)

Converts spoken numbers from their written-out word form into numeric digits. For example, "fifty" becomes "50" and "three hundred and twenty one" becomes "321". This feature is useful when you need consistent numeric formatting without applying all of `smart_format`'s other transformations.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"nova-3"` | Transcription model |
| `numerals` | `True` | Convert spoken numbers to digits |

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
