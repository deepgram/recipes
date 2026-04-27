# Audio Intelligence Pipeline (Audio Intelligence v1)

Combine all five Audio Intelligence features in a single pre-recorded transcription request: sentiment analysis, entity detection, topic detection, summarization, and PII redaction.

## What it does

Deepgram's Audio Intelligence features are applied as parameters on a standard transcription call. Instead of making separate requests for each capability, you can enable all of them at once. The API returns a single response containing the transcript alongside sentiment scores, detected entities, topics, a summary, and redacted content — making it ideal for compliance pipelines, content analytics, and data enrichment workflows.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `sentiment` | `True` | Per-segment positive/negative/neutral scoring |
| `detect_entities` | `True` | Extract named entities (people, places, organisations) |
| `topics` | `True` | Identify key topics discussed in the audio |
| `summarize` | `"v2"` | Generate a concise summary of the content |
| `redact` | `"pci"` | Redact payment card information from the transcript |
| `model` | `"nova-3"` | Transcription model |
| `smart_format` | `True` | Format numbers, dates, currencies |

## Example output

```
Transcript: Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk and...

Summary: The conversation discusses the 50th anniversary of the spacewalk...

Sentiment segments: 4
  [positive] Yeah, as much as it's worth celebrating the 50th ann
  [neutral] it's also worth noting that we've come a long way
  [positive] and I think that's really exciting

Topic segments: 3
  Space Exploration
  Anniversary, History
  Technology

Entities: 2
  [DATE] 50th anniversary
  [EVENT] spacewalk
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
