# Function Calling (Voice Agents v1)

Shows how to configure function calling (tool use) for a Deepgram voice agent.

## What it does

Voice agents can invoke tool calls during conversations, allowing the LLM to fetch external data or trigger actions. Function definitions follow the OpenAI function calling format. When the LLM decides to call a function, you receive a `FunctionCallRequest` event and must respond with the result. This recipe displays the JSON configuration and verifies API connectivity.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `think.functions` | array | List of function definitions (OpenAI format) |
| `functions[].name` | `get_weather` | Function name the LLM can invoke |
| `functions[].parameters` | object | JSON Schema for function parameters |

## Example output

```
Checking Deepgram API access...
42 STT models available

Voice Agent function calling configuration (send via WebSocket Settings message):
  "think": {
    "functions": [{
      "name": "get_weather",
      ...
    }]
  }

Use a Deepgram SDK to establish a session with function calling.
```

## Prerequisites

- Deepgram CLI installed (`curl -fsSL https://deepgram.com/install.sh | sh`)
- Set `DEEPGRAM_API_KEY` environment variable

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
