# Redaction (Speech-to-Text v1)

Automatically redact sensitive information such as credit card numbers and Social Security Numbers from transcripts.

## What it does

When `redact` is set, Deepgram scans the transcript for sensitive data patterns and replaces them with redaction markers. This is critical for compliance in industries like healthcare, finance, and call centres where PCI-DSS or PII regulations apply.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `redact` | `"pci"` | Redact payment card information. Also supports `"ssn"` and `"numbers"`. |
| `model` | `"nova-3"` | Transcription model |
| `smart_format` | `True` | Format numbers, dates, etc. |

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
