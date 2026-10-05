# Record Voice Agent Audio (Voice Agents v1)

Capture the agent's TTS audio output during a live voice agent session and save it to a file for post-session analysis, quality review, or re-transcription.

## What it does

Connects to Deepgram's voice agent API and intercepts the raw audio frames the agent sends back (its spoken responses). The binary audio chunks are collected in memory during the session and written to a local file when the session ends. The recorded audio can then be replayed, re-transcribed with different settings, or analyzed with Audio Intelligence features like summarization and sentiment analysis.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `audio.output.encoding` | `linear16` | Raw PCM format for lossless capture |
| `audio.output.sample_rate` | `16000` | 16 kHz output sample rate |
| `audio.output.container` | `none` | No container header — raw PCM frames |
| `listen.provider` | `deepgram/nova-3` | Speech recognition model |
| `think.provider` | `open_ai/gpt-4o-mini` | LLM for conversation logic |
| `speak.provider` | `deepgram/aura-2-thalia-en` | TTS voice model |

## How audio capture works

The SDK's high-level `message` event delivers parsed JSON control messages (conversation text, settings applied, etc.). Agent audio arrives as binary WebSocket frames on the underlying socket. This recipe attaches a listener to `connection.socket` to intercept those binary frames and buffer them for later writing.

Setting `container: "none"` ensures the agent sends raw PCM audio without WAV headers, so concatenating chunks produces a valid continuous audio stream.

## Example output

```
Settings applied
Agent started speaking
Agent: Hello! How can I help you today?
User: yeah so uh we just got back from the spacewalk
Agent: That sounds amazing! How did it go?
Recorded 128000 bytes of agent audio to session_audio.raw
```

## Playing the recorded audio

The output file is raw 16-bit PCM at 16 kHz mono. Play it with ffplay or convert to WAV:

```bash
# Play directly
ffplay -f s16le -ar 16000 -ac 1 session_audio.raw

# Convert to WAV
ffmpeg -f s16le -ar 16000 -ac 1 -i session_audio.raw session_audio.wav
```

## Prerequisites

- Node.js 20+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `npm install` (from `recipes/javascript/`)

## Run

```bash
node example.js
```
