# Dictation Mode

Format transcript output using dictation-style spoken punctuation commands. When enabled, spoken cues like "period", "comma", and "new paragraph" are converted into actual punctuation marks and formatting in the transcript.

## What it does

Dictation mode interprets verbal punctuation commands as their written equivalents. This is useful for scenarios where speakers dictate text and explicitly say punctuation, such as medical dictation, legal transcription, or note-taking. Instead of seeing "Hello period How are you question mark", the transcript reads "Hello. How are you?"

## Key parameters

- `dictation`: Set to `true` to enable dictation mode

## Example output

```
Yeah, and it's kind of prior to them coming back in, they have to do a suit check ...
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
