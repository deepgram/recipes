# Multichannel Contact Center Analytics (Audio Intelligence v1)

Post-call analytics for dual-channel (stereo) contact center recordings, combining multichannel transcription with sentiment analysis, topic detection, and summarization.

## What it does

Contact centers typically record calls in stereo — agent on one channel, customer on the other. This recipe transcribes each channel independently using `multichannel=True`, then applies Audio Intelligence features across the full conversation:

- **Per-channel transcription** with word counts and talk-time estimates
- **Sentiment trajectory** showing how the emotional tone shifts through the call
- **Topic detection** identifying the subjects discussed
- **Summarization** producing a concise call summary

All of this is done in a single API call by combining Deepgram's multichannel transcription with Audio Intelligence parameters.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `multichannel` | `True` | Transcribe each audio channel independently |
| `sentiment` | `True` | Analyse sentiment (positive/negative/neutral) per segment |
| `topics` | `True` | Detect topics discussed in the audio |
| `summarize` | `"v2"` | Generate a concise summary of the conversation |
| `model` | `"nova-3"` | Transcription model |
| `smart_format` | `True` | Format numbers, dates, etc. |

## Example output

```
[Agent ch0] Yeah, as much as it's worth celebrating the 50th anniversary of the...
  Talk time: 42.3s | Words: 312
[Customer ch1] ...
  Talk time: 0.0s | Words: 0

Sentiment segments: 4
  [positive] Yeah, as much as it's worth celebrating the 50th anniversary
  [neutral] it's also worth noting that we've come a long way since then
  [positive] And this is really exciting stuff

Topics detected: space, spacewalk, technology

Summary: The conversation discusses the 50th anniversary of the spacewalk...
```

Note: The demo audio (`spacewalk.wav`) is mono, so channel 1 will be empty. With a real stereo contact center recording, both channels would contain independent transcripts.

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
