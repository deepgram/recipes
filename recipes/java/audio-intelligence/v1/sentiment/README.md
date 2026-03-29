# Sentiment Analysis (Audio Intelligence v1)

Analyzes the emotional tone of spoken content, classifying each segment of audio as positive, negative, or neutral. This feature helps you understand the speaker's attitude and emotional context throughout your audio content.

## Key Parameters

- **`sentiment`**: Set to `true` to enable sentiment analysis on audio segments

## Prerequisites

- Java 11 or higher
- Maven 3.9 or higher
- `DEEPGRAM_API_KEY` environment variable set

## Run

```bash
cd recipes/java/audio-intelligence/v1/sentiment
mvn exec:java -Dexec.mainClass="Example"
```

## Expected Output

```
[positive] That's one small step for man, one giant leap for mankind.
[neutral] Neil Armstrong speaking from the lunar surface.
[positive] This is an incredible achievement for humanity.
```

The output shows each text segment with its detected sentiment label, helping you understand the emotional tone throughout the audio content.