# State Machine with Function Calling (Voice Agents v1)

Build a voice agent whose conversation follows a strict, deterministic workflow by combining function calling with dynamic prompt updates.

## What it does

Defines an explicit state machine (GREET → COLLECT_INFO → CONFIRM → DONE) where the LLM can only advance the workflow by calling an `advance_state` function. On each transition the agent's system prompt is replaced via `send_update_prompt()`, constraining the LLM to the current step's behavior. Invalid transitions (e.g., skipping from GREET to DONE) are impossible because the transition map enforces the order.

This pattern is essential for production voice agents handling structured workflows like appointment booking, order management, or technical support triage — where the agent must not skip steps or drift from the process.

## State diagram

```
GREET ──advance_state──▶ COLLECT_INFO ──advance_state──▶ CONFIRM ──advance_state──▶ DONE
```

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `think.functions` | `[advance_state]` | Registers the state-transition function for the LLM |
| `send_update_prompt()` | `AgentV1UpdatePrompt` | Replaces the system prompt on each state change |
| `send_function_call_response()` | `AgentV1SendFunctionCallResponse` | Returns the new state to the LLM |
| `send_inject_user_message()` | `AgentV1InjectUserMessage` | Simulates user input for deterministic testing |

## Example output

```
Connection opened
State -> greet
[assistant] Hello! Welcome! I'd be happy to help you book an appointment.
State -> collect_info
[user] Hi, book an appointment. Name: Jane Doe, date: October 5th.
[assistant] Thank you, Jane! Let me confirm — October 5th?
State -> confirm
[assistant] Your appointment is confirmed for October 5th. You're all set!
State -> done
Final state: done
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
