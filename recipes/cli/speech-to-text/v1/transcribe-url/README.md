# Transcribe Audio from URL (Speech-to-Text v1)

Send a URL pointing to a hosted audio file for transcription using the Deepgram REST API.

## What it does

Makes a single REST API call to Deepgram's `/v1/listen` endpoint with a JSON body containing the audio URL. Deepgram downloads the audio, transcribes it with the nova-3 model, and returns the full transcript with smart formatting applied.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Highest-accuracy transcription model |
| `smart_format` | `true` | Formats numbers, dates, currencies automatically |
| `url` | `"https://..."` | URL of the hosted audio file |

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
