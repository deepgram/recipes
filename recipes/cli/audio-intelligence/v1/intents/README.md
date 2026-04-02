# Intent Recognition (Audio Intelligence v1)

Detects speaker intents from audio content alongside transcription.

## What it does

The `intents` parameter tells Deepgram to analyze the transcribed audio for speaker intents. Intent recognition identifies what the speaker is trying to accomplish — such as asking a question, making a request, expressing a complaint, or providing information. Each detected intent includes a confidence score. This is useful for call center analytics, chatbot training, and conversation routing.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Deepgram transcription model |
| `intents` | `true` | Enables intent recognition on the audio |
| `smart_format` | `true` | Enables smart formatting |

## Example output

```json
{
  "segments": [
    {
      "text": "Yeah, as much as, it's funny when I think of...",
      "intents": [
        {
          "intent": "Sharing a personal experience",
          "confidence_score": 0.85
        }
      ]
    }
  ]
}
```

## Prerequisites

- Deepgram CLI installed (`curl -fsSL https://deepgram.com/install.sh | sh`)
- `DEEPGRAM_API_KEY` environment variable set

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
