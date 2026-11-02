# STT v2 Streaming with Interim Result Assembly

Assemble a complete transcript from a Deepgram STT v2 (Flux) streaming session by correctly handling interim and final `TurnInfo` events.

## What it does

In the v2 streaming API, Deepgram sends `TurnInfo` messages with an `event` field that describes where the transcription is in the turn lifecycle:

- **`StartOfTurn`** / **`Update`** — interim results. The `transcript` field contains the current best guess for the turn so far. Each message replaces the previous interim text (not additive).
- **`EagerEndOfTurn`** — the system has moderate confidence the speaker is done. Useful for starting to prepare a response in a voice agent.
- **`TurnResumed`** — speech continued after an `EagerEndOfTurn`. The previous eager signal should be discarded.
- **`EndOfTurn`** — the speaker finished. The `transcript` is the final, stable text for this turn.

This recipe demonstrates the canonical pattern: display interim results for real-time feedback, but only use `EndOfTurn` transcripts when assembling the final document. Each turn has a `turn_index` so turns can be ordered correctly.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"flux-general-en"` | v2 English model with turn detection |
| `encoding` | `"linear16"` | Raw PCM audio format |
| `sample_rate` | `"16000"` | Audio sample rate in Hz |

## Example output

```
[interim turn 0] Yeah as much as
[interim turn 0] Yeah as much as it's worth celebrating
[final  turn 0] Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk, ...
[interim turn 1] I think it's
[final  turn 1] I think it's also worth noting ...

--- Assembled transcript ---
Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk, ... I think it's also worth noting ...
```

## Prerequisites

- Python 3.10+
- Set `DEEPGRAM_API_KEY` environment variable
- Install: `pip install deepgram-sdk==7.16.0`

## Run

```bash
python example.py
```

## Test

```bash
pytest example_test.py -v
```
