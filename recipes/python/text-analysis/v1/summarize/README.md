# Text Summarization (Text Analysis v1)

Generates a concise summary from plain text input using Deepgram's Read API. The model distills the key points from the provided text into a shorter summary, useful for processing articles, meeting notes, support tickets, and other long-form content.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `request` | `{"text": "..."}` | The plain text to analyze |
| `language` | `"en"` | Language of the input text |
| `summarize` | `"v2"` | Enable text summarization |

## Example output

```
Summary: Deepgram provides AI-powered speech recognition and text-to-speech
APIs with audio intelligence features, accessible through multiple language SDKs.
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
