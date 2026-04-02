# Measurements (Speech-to-Text v1)

Converts spoken measurement phrases into their standard abbreviated written forms. When enabled, phrases like "five feet ten inches" become "5 ft 10 in" and "twenty degrees celsius" becomes "20°C".

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"nova-3"` | Transcription model |
| `measurements` | `True` | Convert spoken measurements to standard abbreviations |
| `smart_format` | `True` | Auto-format numbers, dates, and addresses |

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
