# Transcribe Audio from URL (STT v1)

Transcribes a publicly hosted audio file by passing its URL directly to the Deepgram CLI. The CLI sends the URL to the Deepgram API, which fetches and transcribes the audio server-side — no local download required.

## What it does

The `dg listen` command accepts a URL pointing to an audio file. Deepgram downloads the file from that URL and returns a transcript. This is the simplest way to transcribe audio when files are already hosted (S3, CDN, web server, etc.).

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--model` | `nova-3` | Deepgram's latest and most accurate STT model |
| `--smart-format` | (flag) | Applies automatic formatting: punctuation, numbers, dates |

## Example output

```
Yeah, as much as, it's funny when I think about it. Like, I realize I can't even imagine
what it would be like to be mass. You know, the first mass space walk. And he went out there
and it, you know, he's doing summersaults and...
```

## Prerequisites

- Deepgram CLI installed (`curl -fsSL https://deepgram.com/install.sh | sh`)
- Set `DEEPGRAM_API_KEY` environment variable

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
