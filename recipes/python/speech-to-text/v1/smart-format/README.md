# Smart Format (Speech-to-Text v1)

Automatically apply formatting to transcripts so numbers, dates, currencies, and addresses appear in their conventional written form.

## What it does

When `smart_format=True`, Deepgram post-processes the raw transcript to convert spoken forms into
readable written forms. For example, "three hundred dollars" becomes "$300", and "january first
twenty twenty five" becomes "January 1st, 2025". This also implies punctuation and capitalization.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `smart_format` | `True` | Enable automatic formatting of numbers, dates, currencies, addresses |
| `model` | `"nova-3"` | Best model for formatting accuracy |

## Example output

```
Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk...
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
