# Java: Punctuate

Adds automatic punctuation marks to transcriptions for improved readability and natural text flow.

## Feature

Punctuation feature automatically inserts periods, commas, question marks, and other punctuation based on audio cues like pauses and intonation. This makes transcripts much easier to read.

## Key Parameters

- `punctuate`: Enables automatic punctuation insertion
- `model`: Speech model to use (Nova-3 recommended for accuracy)
- `url`: Audio file URL to transcribe

## Sample Output

```
Punctuated transcript:
Spacewalk is a daring journey that takes a lot of training and preparation. It's not just about the technical skills required, but also the mental and physical preparation that astronauts must undergo.
```

Without punctuation, the same audio would output:
```
Spacewalk is a daring journey that takes a lot of training and preparation Its not just about the technical skills required but also the mental and physical preparation that astronauts must undergo
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