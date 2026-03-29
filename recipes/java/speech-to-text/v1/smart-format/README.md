# Java: Smart Format

Applies automatic formatting to transcriptions including punctuation, capitalization, and number formatting for natural-looking text output.

## Feature

Smart formatting automatically applies punctuation marks, proper capitalization, and converts spoken numbers to digits. This makes transcripts much more readable without manual post-processing.

## Key Parameters

- `smartFormat`: Enables automatic punctuation, capitalization, and number formatting
- `model`: Speech model to use (Nova-3 recommended for accuracy)
- `url`: Audio file URL to transcribe

## Sample Output

```
Smart formatted transcript:
Spacewalk is a daring journey that takes a lot of training and preparation. It's not just about the technical skills required, but also the mental and physical preparation that astronauts must undergo.
```

Without smart formatting, the same audio would output:
```
spacewalk is a daring journey that takes a lot of training and preparation its not just about the technical skills required but also the mental and physical preparation that astronauts must undergo
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