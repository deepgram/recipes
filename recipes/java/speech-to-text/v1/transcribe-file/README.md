# Java: Transcribe File

Transcribes local audio files by uploading the file data as bytes to Deepgram. Useful when you have audio files stored locally or need to process uploaded files.

## Feature

File transcription sends raw audio data directly to Deepgram's API. This method works with any audio format supported by Deepgram and doesn't require the files to be publicly accessible via URL.

## Key Parameters

- `body`: Raw audio file data as byte array
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