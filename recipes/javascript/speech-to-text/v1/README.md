# JavaScript / Speech-to-Text / v1

## Recipes

| Recipe | Description |
|--------|-------------|
| [transcribe-url](transcribe-url/) | Send a URL pointing to a hosted audio file for transcription using the Deepgram REST API. |
| [transcribe-file](transcribe-file/) | Read a local audio file and send it to Deepgram for transcription. |
| [smart-format](smart-format/) | Automatically format transcript output with proper numbers, dates, currencies, and addresses. |
| [punctuate](punctuate/) | Add punctuation marks to the transcript output. |
| [paragraphs](paragraphs/) | Group transcript output into paragraph blocks based on natural speech pauses. |
| [utterances](utterances/) | Split the transcript into per-utterance segments with start and end timing. |
| [diarize](diarize/) | Identify and label individual speakers in audio. |
| [multichannel](multichannel/) | Transcribe each audio channel independently for multi-track recordings. |
| [detect-language](detect-language/) | Automatically detect the spoken language in audio. |
| [summarize](summarize/) | Generate a concise summary of the transcript. |
| [topics](topics/) | Identify topics discussed in the audio. |
| [intents](intents/) | Detect speaker intents in the transcript. |
| [sentiment](sentiment/) | Analyze sentiment (positive, negative, neutral) per segment of the transcript. |
| [detect-entities](detect-entities/) | Identify named entities such as people, places, and organisations in the audio. |
| [redact](redact/) | Redact sensitive information like credit card numbers and SSNs from the transcript. |
| [search](search/) | Find specific words or phrases in the audio with confidence scores and timing. |
| [keywords](keywords/) | Boost accuracy for specific keywords or proper nouns. |
| [streaming](streaming/) | WebSocket-based real-time transcription from live audio. |
| [streaming-file](streaming-file/) | Stream a local audio file over WebSocket for incremental transcription. |

## Notes

All recipes in this directory require `DEEPGRAM_API_KEY` to be set in the environment.
