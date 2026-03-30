# Transcribe Audio from URL (Speech-to-Text v1)

Sends a publicly accessible audio URL to Deepgram's pre-recorded transcription API and returns the full transcript text.

## What it does

Makes a POST request to the `/v1/listen` endpoint with a JSON body containing the audio URL. Deepgram downloads the audio, transcribes it using the specified model, and returns the transcript in the response.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Latest and most accurate Deepgram model |
| `smart_format` | `true` | Auto-formats numbers, dates, and punctuation |

## Example output

```
Yeah, as much as, you know, it's worth celebrating the fact that we have more tools at our disposal...
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
