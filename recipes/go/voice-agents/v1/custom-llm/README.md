# Configure LLM Provider (Voice Agents v1)

Use custom LLM providers for Voice Agent conversations.

## What it does

This example demonstrates how to configure different Large Language Model providers (OpenAI, Anthropic, etc.) for Deepgram's Voice Agents service. You can customize the LLM provider to control conversation logic, personality, and response generation according to your application's needs.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `think.provider.type` | `"open_ai"` or `"anthropic"` | Specifies which LLM provider to use for conversation processing |

## Example output

```
Voice agent with custom LLM connected
Session ended
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Set `OPENAI_API_KEY` environment variable (required for OpenAI provider)
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```