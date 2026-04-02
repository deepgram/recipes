# Profanity Filter

Mask profanity in the transcript output. When enabled, offensive or inappropriate words are replaced with masking characters, making the transcript safe for display in public-facing applications or content moderation workflows.

## What it does

The profanity filter detects profane language in the audio and replaces those words in the transcript with asterisks or equivalent masking. This is useful for broadcasting, content moderation, customer-facing displays, or any scenario where explicit language should be censored.

## Key parameters

- `profanity_filter`: Set to `true` to mask profanity in the transcript

## Example output

```
Yeah, and it's prior to them coming back in, they have to do a suit check ...
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
