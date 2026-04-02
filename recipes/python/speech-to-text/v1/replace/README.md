# Find and Replace (Speech-to-Text v1)

Searches for specific terms in the transcript output and replaces them with alternative text. Each replacement rule is a `"find:replace"` pair. This is useful for correcting brand names, normalizing terminology, or customizing transcript output without post-processing.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"nova-3"` | Transcription model |
| `replace` | `["spacewalk:space walk", "NASA:N.A.S.A."]` | Find-and-replace pairs in `"original:replacement"` format |
| `smart_format` | `True` | Auto-format numbers, dates, and addresses |

## Example output

```
Yeah, as much as it's worth celebrating the 50th anniversary of
the space walk, it's also worth noting that we've come a long way
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
