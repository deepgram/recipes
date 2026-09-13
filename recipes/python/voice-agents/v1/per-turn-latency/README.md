# Per-Turn Latency (Voice Agents v1)

Measure the server-side latency breakdown for each voice agent conversational turn.

## What it does

After every agent response, the Deepgram Voice Agent API sends a `LatencyReport` event containing the time spent in each pipeline stage: speech-to-text (STT), LLM time-to-first-text-token, text-to-speech (TTS), and the total end-to-end latency from user utterance end to first audio byte. This recipe prints that breakdown for each turn, giving you production-grade latency visibility without any external instrumentation.

## Key parameters

| Field | Type | Description |
|-------|------|-------------|
| `stt_latency` | `float` | Time from audio received to transcript produced (seconds) |
| `ttt_text_latency` | `float` | Time to first text token from the LLM (seconds) |
| `tts_latency` | `float` | Time from first text token to first audio byte (seconds) |
| `total_latency` | `float` | End-to-end time from user utterance end to first audio byte (seconds) |

Additional fields available on `LatencyReport`: `ttt_token_latency` (first token of any type), `ttt_tool_latency` (first tool-call token), `ttt_thinking_latency` (first thinking token).

## Example output

```
STT  latency: 0.182s
LLM  latency: 0.347s
TTS  latency: 0.091s
Total latency: 0.620s
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
