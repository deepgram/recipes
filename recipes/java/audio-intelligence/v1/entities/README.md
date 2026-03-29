# Entity Detection (Audio Intelligence v1)

Identifies and extracts named entities from audio content, including people, organizations, locations, and other important entities mentioned in speech. This feature helps you automatically catalog key entities discussed in your audio.

## Key Parameters

- **`detectEntities`**: Set to `true` to enable named entity recognition on audio content

## Prerequisites

- Java 11 or higher
- Maven 3.9 or higher
- `DEEPGRAM_API_KEY` environment variable set

## Run

```bash
cd recipes/java/audio-intelligence/v1/entities
mvn exec:java -Dexec.mainClass="Example"
```

## Expected Output

```
PERSON: Neil Armstrong (95%)
ORGANIZATION: NASA (88%)
LOCATION: Moon (92%)
MISSION: Apollo 11 (85%)
```

The output shows detected entities with their type labels and confidence percentages, making it easy to identify key people, places, and organizations mentioned in your audio content.