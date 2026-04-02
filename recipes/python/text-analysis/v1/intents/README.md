# Intent Recognition (Text Analysis v1)

Detects speaker intents from plain text input using Deepgram's Read API. The model identifies what the speaker is trying to accomplish — such as requesting a refund, asking a question, or making a complaint — and returns confidence scores for each detected intent.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `request` | `{"text": "..."}` | The plain text to analyze |
| `language` | `"en"` | Language of the input text |
| `intents` | `True` | Enable intent recognition |

## Example output

```
Text: I'd like to return this product and get a refund.
  Intent: Return/Exchange (confidence: 0.92)
Text: The item arrived damaged and I'm very disappointed with the quality.
  Intent: Complaint (confidence: 0.88)
Text: Can you also update my shipping address for future orders?
  Intent: Update Information (confidence: 0.85)
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
