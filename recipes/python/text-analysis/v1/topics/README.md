# Topic Detection (Text Analysis v1)

Identifies topics discussed in plain text input using Deepgram's Read API. The model analyzes text segments and returns detected topics with confidence scores, useful for content categorization, tagging, and routing.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `request` | `{"text": "..."}` | The plain text to analyze |
| `language` | `"en"` | Language of the input text |
| `topics` | `True` | Enable topic detection |

## Example output

```
Text: The new electric vehicle from Tesla features a range of 400 miles...
  Topic: Electric Vehicles (confidence: 0.94)
  Topic: Technology (confidence: 0.87)
Text: In healthcare news, a new mRNA vaccine shows promising results...
  Topic: Healthcare (confidence: 0.91)
  Topic: Medical Research (confidence: 0.85)
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
