# Redaction (Speech-to-Text v1)

Automatically remove sensitive information like credit card numbers and social security numbers from transcripts.

## What it does

Scans the transcript for patterns matching sensitive data types and replaces them with redacted placeholders. This helps protect privacy and comply with data protection regulations by automatically removing potentially sensitive information from speech transcripts.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `Redact` | `[]string{"pci", "ssn"}` | List of data types to redact (PCI for credit cards, SSN for social security numbers) |

## Example output

```
Redacted Transcript (PCI/SSN removed): Yeah, as as much as it's worth celebrating, the first, spacewalk, with an all female team, I think many of us are looking forward to it just being normal and I think if it signifies anything, it is to honour the the women who came before us who were skilled and qualified, but didn't have the same opportunities that we have today.

Note: This demo audio doesn't contain PCI or SSN data, so no redaction occurs.
In audio with sensitive information, those patterns would be replaced with [REDACTED].
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```