# Sentiment Analysis (Text Analysis v1)

Analyzes sentiment (positive, negative, or neutral) on plain text input using Deepgram's Read API. Returns an overall average sentiment score and per-segment sentiment breakdowns, making it useful for customer feedback analysis, review processing, and content monitoring.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `request` | `{"text": "..."}` | The plain text to analyze |
| `language` | `"en"` | Language of the input text |
| `sentiment` | `True` | Enable sentiment analysis |

## Example output

```
Average sentiment: positive (confidence: 0.72)
  [positive] I absolutely love this product! It exceeded all my expectations.
  [negative] However, the shipping was terrible and took three weeks to arrive.
  [positive] Overall, I'm satisfied with my purchase despite the delivery issues.
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
