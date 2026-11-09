# Configure Voice Agent Endpointing (Voice Agents v1)

Control when Deepgram's voice agent decides a user has finished speaking by tuning end-of-turn (EOT) detection on the Flux listen provider.

## What it does

Turn-taking quality is the single biggest factor in how natural a voice agent sounds. By default, the Flux listen provider uses a balanced EOT threshold of 0.7 and a 5-second silence timeout. This recipe shows how to adjust those knobs to match your use case — for example, raising `eot_threshold` to let users pause mid-thought without being interrupted, or lowering `eot_timeout_ms` for snappy FAQ-style interactions.

The recipe uses the **V2 (Flux) listen provider** (`AgentV1SettingsAgentListenProvider_V2`), which exposes three endpointing parameters. The V1 (Nova) listen provider does not support these settings.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `listen.provider.type` | `"deepgram"` | Deepgram STT provider |
| `listen.provider.model` | `"flux-general-en"` | Flux model (V2 required for EOT tuning) |
| `listen.provider.eot_threshold` | `0.8` | Confidence required to end a turn (0.5–1.0, default 0.7). Higher = more patient |
| `listen.provider.eager_eot_threshold` | `0.5` | Confidence for an early end-of-turn signal (0.3–0.9). Enables `EagerEndOfTurn` and `TurnResumed` events |
| `listen.provider.eot_timeout_ms` | `3000` | Silence timeout in milliseconds (default 5000). Turn ends after this much silence regardless of EOT confidence |

## Example output

```
Connection opened
Endpointing configured: eot_threshold=0.8, eager_eot=0.5, timeout=3000ms
Event: SettingsApplied
Connection closed
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
