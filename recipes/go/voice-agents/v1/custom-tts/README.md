# Configure TTS Voice (Voice Agents v1)

Choose custom text-to-speech voices for Voice Agent responses.

## What it does

This example demonstrates how to configure different text-to-speech voice models for Deepgram's Voice Agents service. You can customize the voice characteristics, accent, and speaking style to match your brand or user preferences for a more personalized conversational experience.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `speak.provider.model` | `"aura-2-arcas-en"` | Specifies the text-to-speech voice model for agent responses |

## Example output

```
Voice agent with custom TTS connected
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