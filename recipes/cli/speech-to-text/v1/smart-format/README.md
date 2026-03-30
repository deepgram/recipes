# Smart Format (Speech-to-Text v1)

Automatically formats numbers, dates, currencies, and addresses in the transcript for improved readability.

## What it does

Enables the `smart_format` parameter which post-processes the transcript to convert spoken numbers into digits, format dates, currencies, and addresses. Without smart format, "twenty five dollars" stays as text; with it, it becomes "$25".

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Highest-accuracy transcription model |
| `smart_format` | `true` | Formats numbers, dates, currencies, addresses automatically |

## Example output

```
Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk...
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
