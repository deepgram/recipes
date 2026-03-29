# Function Calling (Voice Agents v1)

Enable tool calls and function execution in Voice Agent conversations.

## What it does

This example demonstrates how to implement function calling capabilities in Deepgram's Voice Agents service. Function calling allows the LLM to execute external tools and APIs during conversation, enabling more dynamic and interactive voice experiences with access to real-time data and services.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `FunctionCallRequestResponse` | events | Handles function call requests and responses between the agent and external tools |

## Example output

```
Voice agent with function calling connected
Session ended
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Set `OPENAI_API_KEY` environment variable (required for the think provider)
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```