# Dictation Mode

Formats transcripts by converting spoken punctuation commands into actual punctuation characters. When a speaker says "period", "comma", or "new paragraph", those words are replaced with the corresponding punctuation marks instead of being transcribed literally.

## What this feature does

Dictation mode is designed for workflows where users dictate text and speak punctuation aloud. For example, a speaker saying "send the report period please review it comma thanks" would produce "send the report. Please review it, thanks" instead of transcribing "period" and "comma" as words.

## Key parameters

- **dictation(true)**: Enables dictation mode to interpret spoken punctuation commands
- **punctuate(true)**: Recommended alongside dictation for best results

## Sample output

```
NASA, that's one small step for man, one giant leap for mankind.
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable

## Run the example

```bash
cargo run
```
