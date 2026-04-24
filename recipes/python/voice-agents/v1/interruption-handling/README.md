# Interruption Handling & Silence Detection (Voice Agents v1)

Configure a voice agent that gracefully handles user interruptions (barge-in) and uses custom silence detection thresholds for responsive turn-taking.

## What it does

When a user starts speaking while the agent is talking, Deepgram's Voice Agent API fires a `UserStartedSpeaking` event and automatically stops agent audio playback. This recipe configures the listen provider with custom endpointing (how quickly silence ends a turn), utterance end detection (how long to wait before finalizing), and VAD events (voice activity detection notifications). Together these settings control the agent's responsiveness to interruptions and its silence tolerance before responding.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `listen.provider.endpointing` | `300` | Milliseconds of silence before speech endpoint is detected (lower = faster response, higher = more patience for pauses) |
| `listen.provider.utterance_end_ms` | `1200` | Milliseconds of silence to wait before finalizing an utterance (controls how long the agent waits after user stops speaking) |
| `listen.provider.vad_events` | `true` | Enable Voice Activity Detection events for real-time speech start/stop notifications |

## Agent state flow

```
LISTENING ──(user speaks)──> PROCESSING ──(LLM responds)──> SPEAKING
    ^                                                           │
    │                                                           │
    └──────────(UserStartedSpeaking / barge-in)─────────────────┘
```

When a `UserStartedSpeaking` event fires during the SPEAKING state, the agent stops its current audio output and returns to LISTENING, creating a natural interruption experience.

## Example output

```
Agent configured with interruption handling (endpointing=300ms, utterance_end=1200ms)
Connection opened
Event: SettingsApplied
>> Agent speaking
>> Barge-in: user interrupted — agent speech will stop
>> Agent finished speaking
[user] Can you tell me about—
[assistant] Sure, I can help with that.
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
