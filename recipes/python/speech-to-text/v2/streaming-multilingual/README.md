# Flux Multilingual Streaming — Speech-to-Text v2

Deepgram's Flux Multilingual model (`flux-general-multi`) provides real-time streaming transcription across 10 languages with per-turn language detection. Unlike single-language models, Flux Multilingual automatically identifies which language is being spoken on every turn and handles mid-sentence code-switching without requiring language pre-selection or reconnection.

Supported languages: English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch.

## Key Parameters

| Parameter | Value | Description |
|---|---|---|
| `model` | `flux-general-multi` | Flux multilingual model with turn-aware language detection |
| `encoding` | `linear16` | Audio encoding format |
| `sample_rate` | `16000` | Audio sample rate in Hz |
| `language_hint` | *(optional)* | BCP-47 code (e.g. `es`) to bias toward a specific language — pass via `request_options={"additional_query_parameters": {"language_hint": "es"}}` |

## Response Fields

Each `TurnInfo` event includes:

| Field | Description |
|---|---|
| `transcript` | Transcribed text for the current turn |
| `turn_index` | Index of the current conversational turn |
| `languages` | List of detected languages sorted by word count (e.g. `["en", "es"]`) |
| `languages_hinted` | The language hints active for this turn (if configured) |
| `event` | Turn event type: `StartOfTurn`, `Update`, `EagerEndOfTurn`, `TurnResumed`, `EndOfTurn` |

## Prerequisites

1. A [Deepgram API key](https://console.deepgram.com/)
2. Python 3.8+

```bash
export DEEPGRAM_API_KEY="your-api-key"
pip install -r recipes/python/requirements.txt
```

## Run

```bash
python recipes/python/speech-to-text/v2/streaming-multilingual/example.py
```

## Example Output

```
[turn 0] (en) Yeah, as we were saying, the spacewalk was a success.
[turn 1] (en) The crew reported everything went as planned.
```

## Mid-Stream Language Hint Reconfiguration

You can update language hints during a stream using the Configure control message — no reconnection needed:

```python
connection.send_configure({
    "type": "Configure",
    "language_hint": ["es", "en"]
})
```

This is useful for detect-then-lock patterns: start without hints, detect the caller's language from the first turn, then lock to that language for improved accuracy.
