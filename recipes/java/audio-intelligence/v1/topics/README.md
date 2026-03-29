# Topic Detection (Audio Intelligence v1)

Identifies and extracts key topics discussed in audio content with confidence scores. This feature automatically categorizes the subject matter of your audio, making it easy to understand what topics are covered and how prominently they feature.

## Key Parameters

- **`topics`**: Set to `true` to enable topic detection on audio content

## Prerequisites

- Java 11 or higher
- Maven 3.9 or higher
- `DEEPGRAM_API_KEY` environment variable set

## Run

```bash
cd recipes/java/audio-intelligence/v1/topics
mvn exec:java -Dexec.mainClass="Example"
```

## Expected Output

```
Topic: space exploration (95%)
Topic: apollo missions (88%)
Topic: lunar surface (82%)
Topic: historical achievements (75%)
```

The output shows detected topics with confidence percentages, helping you quickly understand the main subjects discussed in your audio content.