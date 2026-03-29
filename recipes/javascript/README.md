# JavaScript Samples

35 recipe(s) covering 4 product(s).

## Recipes

### Speech-to-Text

| Version | Recipe | Description |
|---------|--------|-------------|
| v1 | [transcribe-url](speech-to-text/v1/transcribe-url/) | Send a URL pointing to a hosted audio file for transcription using the Deepgram REST API. |
| v1 | [transcribe-file](speech-to-text/v1/transcribe-file/) | Read a local audio file and send it to Deepgram for transcription. |
| v1 | [smart-format](speech-to-text/v1/smart-format/) | Automatically format transcript output with proper numbers, dates, currencies, and addresses. |
| v1 | [punctuate](speech-to-text/v1/punctuate/) | Add punctuation marks to the transcript output. |
| v1 | [paragraphs](speech-to-text/v1/paragraphs/) | Group transcript output into paragraph blocks based on natural speech pauses. |
| v1 | [utterances](speech-to-text/v1/utterances/) | Split the transcript into per-utterance segments with start and end timing. |
| v1 | [diarize](speech-to-text/v1/diarize/) | Identify and label individual speakers in audio. |
| v1 | [multichannel](speech-to-text/v1/multichannel/) | Transcribe each audio channel independently for multi-track recordings. |
| v1 | [detect-language](speech-to-text/v1/detect-language/) | Automatically detect the spoken language in audio. |
| v1 | [summarize](speech-to-text/v1/summarize/) | Generate a concise summary of the transcript. |
| v1 | [topics](speech-to-text/v1/topics/) | Identify topics discussed in the audio. |
| v1 | [intents](speech-to-text/v1/intents/) | Detect speaker intents in the transcript. |
| v1 | [sentiment](speech-to-text/v1/sentiment/) | Analyze sentiment (positive, negative, neutral) per segment of the transcript. |
| v1 | [detect-entities](speech-to-text/v1/detect-entities/) | Identify named entities such as people, places, and organisations in the audio. |
| v1 | [redact](speech-to-text/v1/redact/) | Redact sensitive information like credit card numbers and SSNs from the transcript. |
| v1 | [search](speech-to-text/v1/search/) | Find specific words or phrases in the audio with confidence scores and timing. |
| v1 | [keywords](speech-to-text/v1/keywords/) | Boost accuracy for specific keywords or proper nouns. |
| v1 | [streaming](speech-to-text/v1/streaming/) | WebSocket-based real-time transcription from live audio. |
| v1 | [streaming-file](speech-to-text/v1/streaming-file/) | Stream a local audio file over WebSocket for incremental transcription. |
| v2 | [transcribe-url](speech-to-text/v2/transcribe-url/) | Transcribe audio using the v2 API with the flux-general-en model for high-accuracy English transcription. |
| v2 | [streaming](speech-to-text/v2/streaming/) | WebSocket streaming with the v2 listen endpoint using flux-general-en. |

### Text-to-Speech

| Version | Recipe | Description |
|---------|--------|-------------|
| v1 | [generate-audio](text-to-speech/v1/generate-audio/) | Convert text to audio and save as a file using the Deepgram TTS REST API. |
| v1 | [stream-audio](text-to-speech/v1/stream-audio/) | Stream TTS audio as it generates via the REST API. |
| v1 | [websocket-streaming](text-to-speech/v1/websocket-streaming/) | Low-latency text-to-speech via WebSocket for real-time use cases. |
| v1 | [select-model](text-to-speech/v1/select-model/) | Choose from available aura-2 voice models for speech synthesis. |
| v1 | [select-encoding](text-to-speech/v1/select-encoding/) | Choose the output audio encoding format for TTS audio. |

### Audio Intelligence

| Version | Recipe | Description |
|---------|--------|-------------|
| v1 | [summarize](audio-intelligence/v1/summarize/) | Generate a concise text summary of spoken content. |
| v1 | [sentiment](audio-intelligence/v1/sentiment/) | Segment-level positive/negative/neutral sentiment scoring. |
| v1 | [topics](audio-intelligence/v1/topics/) | Identify key topics discussed in audio content. |
| v1 | [intents](audio-intelligence/v1/intents/) | Detect caller/speaker intents from audio context. |
| v1 | [entities](audio-intelligence/v1/entities/) | Identify named entities: people, organisations, locations in audio. |

### Voice Agents

| Version | Recipe | Description |
|---------|--------|-------------|
| v1 | [connect](voice-agents/v1/connect/) | Establish a WebSocket voice agent session with default settings. |
| v1 | [custom-llm](voice-agents/v1/custom-llm/) | Use a custom LLM provider for the voice agent's "think" step. |
| v1 | [custom-tts](voice-agents/v1/custom-tts/) | Choose a specific aura-2 voice model for the agent's speech output. |
| v1 | [function-calling](voice-agents/v1/function-calling/) | Inject tool calls for the LLM to use during a voice agent conversation. |

## Running Tests

```bash
npm install && npm test
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` in your environment
- Node 20+
