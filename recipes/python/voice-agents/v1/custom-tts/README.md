# Configure TTS Voice (Voice Agents v1)

Choose a specific aura-2 voice model for the agent's spoken responses.

## What it does

The voice agent's "speak" stage converts LLM-generated text into speech. By changing the `model` parameter in the speak provider, you select different voice personalities. This lets you match the agent's voice to your brand or use case — e.g., a warm conversational voice for customer support or a deep authoritative voice for information delivery.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `speak.provider.type` | `"deepgram"` | TTS provider |
| `speak.provider.model` | `"aura-2-arcas-en"` | Voice model. Options: `aura-2-thalia-en`, `aura-2-luna-en`, `aura-2-asteria-en`, `aura-2-helios-en`, etc. |

## Example output

```
Agent configured with aura-2-arcas-en voice
Connection opened
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
