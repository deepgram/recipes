# DTMF IVR with Voice Agent (Voice Agents v1)

Handle dual-tone multi-frequency (DTMF) dial-pad key presses inside a Deepgram voice agent session, enabling traditional IVR menu navigation alongside natural speech.

## What it does

Configures a Deepgram Voice Agent as a telephony IVR that can process both spoken requests and DTMF key presses. When a caller presses a phone key, the telephony provider (Twilio, Telnyx, etc.) delivers the digit as an event. This recipe models that event as a **function call** — the LLM receives a `handle_dtmf` tool invocation containing the digit, looks up the matching department, and speaks the routing confirmation.

Because this example must run without a live phone call, it injects a simulated "Caller pressed 1" message via `send_inject_user_message`. In a production deployment you would instead call `handle_dtmf` from your telephony webhook handler when the SIP provider reports a DTMF event.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `think.functions` | `[handle_dtmf]` | Registers DTMF handler as a callable function |
| `think.prompt` | IVR menu instructions | Tells the LLM to offer a phone menu and use function results |
| `listen.provider.model` | `"nova-3"` | STT model for the listen stage |
| `think.provider.model` | `"gpt-4o-mini"` | LLM for the think stage |
| `speak.provider.model` | `"aura-2-thalia-en"` | TTS voice for the speak stage |

## Example output

```
Connected
IVR ready — simulating DTMF '1'
[user] Caller pressed 1
DTMF '1' -> sales
[assistant] I'm routing you to the sales department now. One moment please.
```

## How DTMF integration works in production

In a real telephony deployment the flow is:

1. SIP provider (Twilio/Telnyx) detects a DTMF tone on the media stream
2. Provider sends a webhook or WebSocket event with the digit
3. Your server calls `agent.send_inject_user_message()` or responds to the `FunctionCallRequest` with the digit
4. The voice agent LLM processes the digit and speaks the appropriate response

## Prerequisites

- Python 3.10+
- Set `DEEPGRAM_API_KEY` environment variable
- Set `OPENAI_API_KEY` environment variable (used by the think stage)
- Install: `pip install -r recipes/python/requirements.txt`

## Run

```bash
python example.py
```

## Test

```bash
pytest example_test.py -v
```
