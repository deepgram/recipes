# Connect to Voice Agent (Voice Agents v1)

Establish WebSocket connection to Deepgram Voice Agent for conversational AI.

## What it does

This example demonstrates how to connect to Deepgram's Voice Agents service via WebSocket. Voice Agents enable real-time conversational AI by combining speech-to-text, language model processing, and text-to-speech in a single integrated service for natural voice interactions.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `think.provider.type` | `"open_ai"` | Specifies the LLM provider for conversation processing |
| `speak.provider.model` | `"aura-2-thalia-en"` | Sets the text-to-speech voice model |

## Example output

```
Voice agent connected successfully
Voice agent session ended
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