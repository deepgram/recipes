# Profanity Filter

Masks profane words in the transcript by replacing them with asterisks or symbols. This produces clean, family-friendly output suitable for broadcast, content moderation, and public-facing applications.

## What this feature does

The profanity filter detects profane or offensive words during transcription and replaces them with masked characters (e.g., "****"). This allows applications to safely display transcripts without exposing inappropriate language, while preserving the rest of the content accurately.

## Key parameters

- **profanity_filter(true)**: Enables masking of profane words in the transcript

## Sample output

```
NASA, that's one small step for man, one giant leap for mankind.
```

Note: Profanity masking only appears when the audio contains profane language. The demo audio produces clean output.

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable

## Run the example

```bash
cargo run
```
