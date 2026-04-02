# Bit Rate Control (Text-to-Speech v1)

Controls the output audio bit rate for compressed encodings like mp3. Lower bit rates produce smaller files suited for bandwidth-constrained scenarios, while higher bit rates preserve more audio detail for higher-quality playback.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"aura-2-thalia-en"` | TTS voice model |
| `encoding` | `"mp3"` | Output audio encoding (bit_rate applies to compressed formats) |
| `bit_rate` | `48000` | Audio bit rate in bits per second (48 kbps) |

## Example output

```
Saved output.mp3 (12345 bytes) — encoding: mp3, bit_rate: 48000
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
