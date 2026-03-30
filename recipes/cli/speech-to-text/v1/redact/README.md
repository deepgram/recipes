# Redaction (Speech-to-Text v1)

Redacts sensitive information like credit card numbers and social security numbers from the transcript.

## What it does

Enables the `redact` parameter with PCI and SSN redaction types. Any payment card numbers or social security numbers spoken in the audio are replaced with redaction markers in the transcript. Essential for compliance in financial and healthcare audio processing.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Highest-accuracy transcription model |
| `redact` | `pci` | Redacts payment card industry data |
| `redact` | `ssn` | Redacts social security numbers |

## Example output

```
My credit card number is [REDACTED] and my social is [REDACTED].
```

## Prerequisites

- `curl` and `python3` installed
- Set `DEEPGRAM_API_KEY` environment variable

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
