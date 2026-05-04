# Background Tool Execution with Filler Speech (Voice Agents v1)

Eliminate conversational silence during tool execution by sending filler speech while tools run in background threads.

## What it does

When the LLM decides to call a tool (e.g., a weather API or database query), the agent immediately speaks a filler phrase like "Let me check the weather..." using `send_inject_agent_message()`. Meanwhile, the tool executes in a background thread. Once the tool completes, the result is sent back via `send_function_call_response()` so the LLM can incorporate it into the next spoken response — all without any dead silence.

This pattern is critical for production voice agents where tools take more than ~500ms. Users interpret silence as a disconnection or error.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `think.functions` | `list[dict]` | Tool definitions the LLM can invoke |
| `send_inject_agent_message()` | method | Inject filler speech while tool runs |
| `send_function_call_response()` | method | Return tool result to the LLM |
| `FunctionCallRequest.functions` | `list` | Functions the LLM wants to call (with id, name, arguments) |
| `threading.Thread` | stdlib | Run tool execution in background |

## Example output

```
Agent configured with background tool execution
Connection opened
Event: SettingsApplied
Tool called: get_weather — sending filler speech
Tool get_weather done — sending result
Tool called: search_db — sending filler speech
Tool search_db done — sending result
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
