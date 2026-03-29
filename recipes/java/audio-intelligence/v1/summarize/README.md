# Audio Summarization (Audio Intelligence v1)

Generates a concise text summary of spoken audio content using AI. This feature extracts the key points and main topics discussed in your audio files or streams, producing a brief summary without requiring you to read the full transcript.

## Key Parameters

- **`summarize`**: Set to `"v2"` to enable audio summarization using the latest model

## Prerequisites

- Java 11 or higher
- Maven 3.9 or higher
- `DEEPGRAM_API_KEY` environment variable set

## Run

```bash
cd recipes/java/audio-intelligence/v1/summarize
mvn exec:java -Dexec.mainClass="Example"
```

## Expected Output

```
Summary: Neil Armstrong and Buzz Aldrin made historic first steps on the moon during the Apollo 11 mission, with Armstrong becoming the first human to walk on the lunar surface.
```

The summary condenses the audio content into essential information, making it easy to quickly understand what was discussed without listening to or reading the entire transcript.