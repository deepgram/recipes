# Transcribe URL with v2 Model (Speech-to-Text v2)

Transcribe audio from a URL using Deepgram's v2 API model (`flux-general-en`). This model is specifically optimized for English language audio and provides enhanced accuracy and performance.

## What this demonstrates

The v2 API introduces the `flux-general-en` model, which is fine-tuned specifically for English language transcription. It offers improved accuracy for conversational speech and better performance on audio with background noise or lower quality.

## Key parameters

- `Model = "flux-general-en"` — Deepgram's v2 English-optimized model
- `SmartFormat = true` — Formats numbers, dates, currencies automatically
- `Punctuate = true` — Adds punctuation to transcripts

## Model comparison

- **v1 models** (nova-3, nova-2): Multi-language support, general purpose
- **v2 model** (flux-general-en): English-only, optimized for conversational speech

## Example output

```
Transcript: Neil Armstrong became the first human to step foot on the moon on July 20th, 1969. UTC.
Confidence: 0.95
```

## Prerequisites

- .NET 8.0 or later
- `DEEPGRAM_API_KEY` environment variable set to your Deepgram API key

## Run the example

```bash
dotnet run
```

The example transcribes the demo spacewalk audio using the v2 model and displays both the transcript and confidence score. The flux-general-en model typically provides higher confidence scores and more accurate transcriptions for English audio compared to general-purpose models.