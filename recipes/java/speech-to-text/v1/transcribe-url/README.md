# Java: Transcribe URL

Transcribes audio from a URL using Deepgram's Nova-3 speech-to-text model. This is the simplest way to get started with speech recognition.

## Feature

URL transcription allows you to send audio file URLs directly to Deepgram without downloading files locally. Perfect for web applications and remote audio processing.

## Key Parameters

- `url`: The audio file URL to transcribe
- `model`: Speech model to use (Nova-3 recommended for accuracy)
- `smartFormat`: Applies punctuation, capitalization, and number formatting

## Sample Output

```
Spacewalk is a daring journey that takes a lot of training and preparation. It's not just about the technical skills required, but also the mental and physical preparation that astronauts must undergo.
```

## Prerequisites

1. Java 11+
2. Maven 3.6+
3. Set `DEEPGRAM_API_KEY` environment variable

## Run

```bash
mvn exec:java -Dexec.mainClass=Example
```

## Test

```bash
mvn test
```