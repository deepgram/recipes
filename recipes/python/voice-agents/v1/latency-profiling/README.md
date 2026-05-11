# Latency Profiling (Voice Agents v1)

Measure time-to-first-byte (TTFB) for each stage of the voice agent pipeline — think (LLM) and speak (TTS) — to identify bottlenecks and optimize end-to-end response time.

## What it does

Opens a voice agent WebSocket session and injects a text message. As the agent processes the turn through its listen → think → speak pipeline, the example timestamps each stage event (`AgentThinking`, first audio byte, `AgentStartedSpeaking`, `AgentAudioDone`) and prints a per-component latency breakdown.

This profiling pattern helps developers:
- Identify which pipeline stage contributes the most latency
- Compare latency across different model configurations (swap `gpt-4o-mini` for another LLM, or change the TTS voice)
- Establish baseline metrics for production voice agent deployments

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `listen.provider.model` | `"nova-3"` | STT model for the listen stage |
| `think.provider.model` | `"gpt-4o-mini"` | LLM model for the think stage |
| `think.prompt` | `"Reply in one short sentence."` | Short prompt to keep responses fast |
| `speak.provider.model` | `"aura-2-thalia-en"` | TTS model for the speak stage |

## Measured events

| Metric | What it measures |
|--------|-----------------|
| **Think TTFB** | Time from user message injection to `AgentThinking` event |
| **TTS TTFB** | Time from `AgentThinking` to first audio byte received |
| **Speak duration** | Time from `AgentStartedSpeaking` to `AgentAudioDone` |
| **Total turn** | End-to-end time from injection to audio completion |

## Example output

```
Think TTFB:        312 ms
TTS TTFB:          245 ms
Speak duration:    987 ms
Total turn:       1544 ms
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
