# Select Voice Model (Text-to-Speech v1)

Choose from available aura-2 voice models to control the personality and tone of generated speech.

## What it does

Deepgram provides multiple voice models in the aura-2 family, each with a distinct voice. By changing the `model` parameter, you can select the voice that best fits your use case — e.g., a warm conversational voice, a deep authoritative voice, or a bright energetic voice.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"aura-2-arcas-en"` | Voice model to use. Other options: `aura-2-thalia-en`, `aura-2-luna-en`, `aura-2-asteria-en`, `aura-2-helios-en` |
| `text` | `str` | The text to convert to speech |

## Example output

```
Saved output.mp3 (12480 bytes) using model aura-2-arcas-en
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
