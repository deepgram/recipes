# Python / Speech-to-Text / v1

## Recipes

| Recipe | Description |
|--------|-------------|
| [transcribe-url](transcribe-url/) | Send a URL pointing to a hosted audio file for transcription using the Deepgram REST API. |
| [smart-format](smart-format/) | Automatically apply formatting to transcripts so numbers, dates, currencies, and addresses appear in their conventional written form. |
| [punctuate](punctuate/) | Add punctuation and capitalization to transcript output for improved readability. |
| [paragraphs](paragraphs/) | Group transcript output into paragraph blocks based on natural pauses and topic shifts in speech. |
| [utterances](utterances/) | Split transcript into per-utterance segments with timing, providing natural breakpoints in spoken audio. |
| [diarize](diarize/) | Identify and label individual speakers in a multi-speaker audio recording. |
| [detect-language](detect-language/) | Automatically detect the dominant spoken language in audio without specifying it upfront. |
| [summarize](summarize/) | Generate a concise text summary of the transcribed audio content. |
| [topics](topics/) | Identify the key topics discussed in audio, with confidence scores for each detected topic. |
| [intents](intents/) | Detect speaker intents in audio — what the speaker is trying to accomplish in each segment. |
| [sentiment](sentiment/) | Analyze the emotional tone of spoken audio, scoring each segment as positive, negative, or neutral. |

## Notes

All recipes in this directory require `DEEPGRAM_API_KEY` to be set in the environment.
