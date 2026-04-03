# Filler Words

Preserves filler words like "uh", "um", "mhm", and "uh huh" in the transcript output. By default, Deepgram filters these out for cleaner text, but enabling this feature retains them for verbatim transcription and conversation analysis.

## What this feature does

Filler words are natural speech disfluencies that speakers use while thinking or transitioning between thoughts. Enabling filler word detection includes these in the transcript, which is valuable for linguistic research, speaker behavior analysis, and applications requiring exact verbatim output.

## Key parameters

- **filler_words(true)**: Includes filler words ("uh", "um", etc.) in the transcript output

## Sample output

```
Um, NASA, uh, that's one small step for man, one giant leap for mankind.
```

Note: Filler words appear only if the speaker actually used them in the audio.

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable

## Run the example

```bash
cargo run
```
