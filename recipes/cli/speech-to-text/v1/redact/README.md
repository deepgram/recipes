# Redaction (STT v1)

Redacts sensitive information from the transcript.

## What it does

The `redact` parameter tells Deepgram to replace sensitive information in the transcript with placeholder characters. Supported redaction types include `pci` (credit card numbers), `ssn` (social security numbers), and other PII patterns. Redacted values appear as `[REDACTED]` or similar placeholders.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Deepgram transcription model |
| `redact` | `pci`, `ssn` | Types of sensitive data to redact |

## Example output

```
Yeah, as much as, it's funny when I think of anything that's related to outer space...
```

## Prerequisites

- Deepgram CLI installed (`curl -fsSL https://deepgram.com/install.sh | sh`)
- `DEEPGRAM_API_KEY` environment variable set

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
