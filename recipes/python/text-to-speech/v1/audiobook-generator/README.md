# Audiobook Generator with Chapter Pauses (Flux TTS)

Generate a single audio file from multi-paragraph text with natural pauses between sections using Deepgram's Flux TTS engine and the `TextBuilder` helper.

## What it does

Long-form content — articles, book chapters, documentation — needs pacing to sound natural when read aloud. This recipe splits text on blank lines into paragraphs, then uses `TextBuilder.pause()` to insert a configurable silence gap between each one. Each paragraph is sent to the Flux batch REST endpoint (`/v2/speak`) and the returned audio chunks are concatenated into a single output file.

The pattern scales to any text length: split your source into chunks that fit within the 2 000-character API limit, generate audio for each, and concatenate the results.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"flux-alexis-en"` | Flux voice model (English) |
| `TextBuilder.pause()` | `1000` (ms) | Silence inserted between paragraphs (500–3 000 ms, 100 ms increments, max 8 per request) |

## How pauses work

Flux batch REST supports inline pause markers written as `\{pause:Nms\}`. The SDK's `TextBuilder` generates these automatically when you call `.pause(ms)`. Constraints:

- Duration: 500–3 000 ms in 100 ms steps
- Maximum 8 pauses per request
- Speed must be ≤ 1.15 when pauses are present
- Pauses are **batch-only** — not supported on the Flux WebSocket endpoint

## Example output

```
Generated 4 paragraphs -> output.mp3: 187520 bytes
```

## Prerequisites

- Python 3.10+
- Set `DEEPGRAM_API_KEY` environment variable
- Install: `pip install deepgram-sdk==7.12.0`

## Run

```bash
python example.py
# Produces output.mp3
```

## Test

```bash
pytest example_test.py -v --timeout=120
```
