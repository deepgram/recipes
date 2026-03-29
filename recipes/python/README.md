# Python Samples

12 recipe(s) covering 2 product(s).

## Recipes

### Speech-to-Text

| Version | Recipe | Description |
|---------|--------|-------------|
| v1 | [transcribe-url](speech-to-text/v1/transcribe-url/) | Send a URL pointing to a hosted audio file for transcription using the Deepgram REST API. |
| v1 | [smart-format](speech-to-text/v1/smart-format/) | Automatically apply formatting to transcripts so numbers, dates, currencies, and addresses appear in their conventional written form. |
| v1 | [punctuate](speech-to-text/v1/punctuate/) | Add punctuation and capitalization to transcript output for improved readability. |
| v1 | [paragraphs](speech-to-text/v1/paragraphs/) | Group transcript output into paragraph blocks based on natural pauses and topic shifts in speech. |
| v1 | [utterances](speech-to-text/v1/utterances/) | Split transcript into per-utterance segments with timing, providing natural breakpoints in spoken audio. |
| v1 | [diarize](speech-to-text/v1/diarize/) | Identify and label individual speakers in a multi-speaker audio recording. |
| v1 | [detect-language](speech-to-text/v1/detect-language/) | Automatically detect the dominant spoken language in audio without specifying it upfront. |
| v1 | [summarize](speech-to-text/v1/summarize/) | Generate a concise text summary of the transcribed audio content. |
| v1 | [topics](speech-to-text/v1/topics/) | Identify the key topics discussed in audio, with confidence scores for each detected topic. |
| v1 | [intents](speech-to-text/v1/intents/) | Detect speaker intents in audio — what the speaker is trying to accomplish in each segment. |
| v1 | [sentiment](speech-to-text/v1/sentiment/) | Analyze the emotional tone of spoken audio, scoring each segment as positive, negative, or neutral. |

### Text-to-Speech

| Version | Recipe | Description |
|---------|--------|-------------|
| v1 | [generate-audio](text-to-speech/v1/generate-audio/) | Convert text to speech using an aura-2 voice model and save the audio to a file. |

## Running Tests

```bash
pip install -r requirements.txt
pytest . -v --timeout=60
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` in your environment
- Python 3.9+
