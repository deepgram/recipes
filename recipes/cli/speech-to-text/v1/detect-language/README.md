# Language Detection (Speech-to-Text v1)

Automatically detects the spoken language in audio without requiring language specification.

## What it does

Enables the `detect_language` parameter which tells Deepgram to identify the spoken language before transcribing. The response includes the detected language code (e.g. "en" for English) alongside the transcript. Useful when processing audio in unknown or mixed languages.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Highest-accuracy transcription model |
| `detect_language` | `true` | Enables automatic spoken language detection |

## Example output

```
Detected language: en
Transcript: Yeah, as much as it's worth celebrating the 50th anniversary...
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
