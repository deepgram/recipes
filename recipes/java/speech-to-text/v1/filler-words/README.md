# Filler Words

Capture filler words like "uh", "um", and "mhm" in the transcript output. By default, Deepgram omits these disfluencies to produce cleaner text. Enabling filler words is useful for conversation analysis, speaker profiling, or when verbatim accuracy matters.

## What it does

When `filler_words` is enabled, Deepgram includes hesitation markers and filler sounds in the transcript instead of silently removing them. This gives a more faithful representation of what was actually spoken.

## Key parameters

- `filler_words`: Set to `true` to include filler words in the transcript

## Example output

```
Yeah, um, and it's kind of prior to them coming back in, they have to, uh, do a suit check ...
```

## Prerequisites

- Java 11+
- Maven 3.6+
- Deepgram API key set as `DEEPGRAM_API_KEY` environment variable

## Running the example

```bash
mvn compile exec:java -Dexec.mainClass=Example
```

## Running the test

```bash
mvn test
```
