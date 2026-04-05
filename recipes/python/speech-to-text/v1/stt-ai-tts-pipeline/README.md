# STT → Audio Intelligence → TTS Pipeline (Python)

A complete end-to-end Deepgram pipeline in a single script: transcribe audio with Speech-to-Text, analyse the transcript with Audio Intelligence (sentiment, topics, summarization), then convert the summary to spoken audio with Text-to-Speech.

## What it does

This recipe chains three Deepgram capabilities together without any third-party services:

1. **Speech-to-Text** — transcribes audio using Nova-3 with smart formatting
2. **Audio Intelligence** — runs sentiment analysis, topic detection, and summarization on the transcript in the same API call
3. **Text-to-Speech** — speaks the generated summary aloud using Aura-2 and saves it as an MP3

This pattern is useful for meeting recap pipelines, podcast highlight generators, or any workflow that needs to understand audio content and produce a spoken summary.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"nova-3"` | STT transcription model |
| `smart_format` | `True` | Auto-format numbers, dates, currencies |
| `summarize` | `"v2"` | Generate a concise summary of the audio |
| `sentiment` | `True` | Score each segment as positive/negative/neutral |
| `topics` | `True` | Detect key topics in the audio |
| `model` (TTS) | `"aura-2-thalia-en"` | Voice model for the spoken summary |

## Example output

```
=== Stage 1: Speech-to-Text + Audio Intelligence ===
Transcript: Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk...
Sentiment segments: 6
  [positive] Yeah, as much as it's worth celebrating the 50th anniversary
  [neutral] And it's, of course, an incredible feat
  [positive] But the technology has come so far
  Topics: Space exploration, Technology advancement
  Topics: Astronauts, Spacewalk history

Summary: The discussion covers the 50th anniversary of the first spacewalk and highlights how space technology has advanced significantly since then.

=== Stage 2: Text-to-Speech ===
Saved spoken summary: output.mp3 (24576 bytes)
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
