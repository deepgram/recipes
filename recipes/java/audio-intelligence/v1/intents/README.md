# Intent Recognition (Audio Intelligence v1)

Detects speaker intents from audio context, identifying the purpose or goal behind what is being said. This feature analyzes the speaker's underlying intentions, such as making requests, providing information, expressing emotions, or taking actions.

## Key Parameters

- **`intents`**: Set to `true` to enable intent recognition on audio segments

## Prerequisites

- Java 11 or higher
- Maven 3.9 or higher
- `DEEPGRAM_API_KEY` environment variable set

## Run

```bash
cd recipes/java/audio-intelligence/v1/intents
mvn exec:java -Dexec.mainClass="Example"
```

## Expected Output

```
Intent: inform (92%)
Intent: celebrate (85%)
Intent: describe (78%)
```

The output shows detected intents with confidence percentages, helping you understand what the speaker was trying to accomplish with their words.