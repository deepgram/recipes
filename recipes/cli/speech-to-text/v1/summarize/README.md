# Summarize (Speech-to-Text v1)

Generates a concise text summary of the transcribed audio content.

## What it does

Enables the `summarize=v2` parameter which runs AI-powered summarization on the transcript after transcription. The response includes a short summary in addition to the full transcript. This is an Audio Intelligence feature.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Required model for summarization |
| `summarize` | `v2` | Enables AI summarization (must be string "v2", not boolean) |

## Example output

```
Summary: A discussion about the 50th anniversary of the first spacewalk and the technological advances since then.
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
