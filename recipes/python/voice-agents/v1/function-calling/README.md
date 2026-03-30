# Function Calling (Voice Agents v1)

Inject tool definitions for the LLM to call during a voice agent conversation.

## What it does

Defines functions (tools) in the agent's think settings that the LLM can invoke during a conversation. When the LLM decides to call a function, a `FunctionCallRequest` event arrives with the function name and arguments. Your code executes the function and sends the result back via `send_function_call_response()`, so the LLM can incorporate the result into its spoken response.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `think.functions` | `list[dict]` | Array of function definitions (name, description, parameters) |
| `FunctionCallRequest.name` | `str` | Name of the function the LLM wants to call |
| `FunctionCallRequest.id` | `str` | Unique ID to match response to request |
| `send_function_call_response()` | method | Send function result back to the agent |

## Example output

```
Agent configured with function calling (get_weather)
Connection opened
Event: SettingsApplied
Function call: get_weather
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
