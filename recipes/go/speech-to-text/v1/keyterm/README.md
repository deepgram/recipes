# Key Term Prompting (Speech-to-Text v1)

Boosts recognition of specific key terms using Nova-3's native prompting capability. Unlike keyword boosting which uses numeric weights, key term prompting simply tells the model which terms to prioritize without requiring a boost value.

## What it does

Key term prompting improves transcription accuracy for domain-specific vocabulary, proper nouns, or technical terms. The model uses these hints to better recognize the specified terms when they appear in the audio.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `keyterm` | `["spacewalk", "NASA", "ISS"]` | List of terms to boost recognition for |
| `model` | `nova-3` | Required — key term prompting is a Nova-3 feature |

## Example output

```
Transcript (with key terms): That's one small step for man, one giant leap for mankind.
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```
