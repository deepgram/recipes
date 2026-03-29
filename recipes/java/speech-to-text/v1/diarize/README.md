# Java: Diarize

Identifies and labels different speakers in audio recordings for multi-speaker conversation analysis.

## Feature

Speaker diarization automatically detects speaker changes and assigns labels (Speaker 0, Speaker 1, etc.) to different voices in the audio. This is essential for meeting transcription, interview analysis, and conversation processing.

## Key Parameters

- `diarize`: Enables speaker diarization and labeling
- `smartFormat`: Recommended for proper punctuation and formatting  
- `model`: Speech model to use (Nova-3 recommended for accuracy)

## Sample Output

```
Words with speaker labels:
Speaker 0: Spacewalk is a daring journey that takes a lot of training and preparation. It's not just about the technical skills required, but also the mental and physical preparation that astronauts must undergo.
```

For multi-speaker audio, you might see:
```
Speaker 0: Hello, how are you today?
Speaker 1: I'm doing well, thank you for asking.
Speaker 0: That's great to hear.
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