# Java: Detect Language

Automatically detects the language spoken in audio files without needing to specify the language beforehand.

## Feature

Language detection automatically identifies the primary language in audio content using Deepgram's language identification models. This is particularly useful for processing audio content where the language is unknown or for building multilingual applications.

## Key Parameters

- `detectLanguage`: Enables automatic language detection and identification
- `smartFormat`: Recommended for proper punctuation and formatting
- `model`: Speech model to use (Nova-3 recommended for accuracy)

## Sample Output

```
Detected language: en
Transcript: Spacewalk is a daring journey that takes a lot of training and preparation. It's not just about the technical skills required, but also the mental and physical preparation that astronauts must undergo.
```

For other languages, you might see:
```
Detected language: es
Transcript: Hola, ¿cómo estás hoy?
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