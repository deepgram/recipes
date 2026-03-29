# Speech-to-Text Topic Detection

Automatically detect and identify key topics discussed in audio content. This feature analyzes the transcript to extract main themes, subjects, and discussion points with confidence scores.

## What it does

The topic detection feature uses AI to analyze the content of your audio and identify the main topics being discussed. It provides topic labels along with confidence scores, helping you understand what subjects are covered in the audio without having to listen to the entire recording.

## Key parameters

- `topics`: Set to `true` to enable topic detection

## Example output

```
Topic: Space exploration (confidence: 0.95)
Topic: NASA (confidence: 0.88)
Topic: International Space Station (confidence: 0.92)
Topic: Spacewalk (confidence: 0.87)
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