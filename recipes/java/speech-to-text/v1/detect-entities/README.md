# Speech-to-Text Entity Detection

Automatically identify and extract named entities from spoken audio. This feature recognizes people, organizations, locations, dates, and other important entities mentioned in the audio content.

## What it does

Entity detection uses natural language processing to identify and classify specific named entities within the transcribed text. It can recognize various types of entities including person names, organization names, locations, dates, monetary amounts, and other significant entities. This is particularly useful for content analysis, information extraction, and automated metadata generation.

## Key parameters

- `detectEntities`: Set to `true` to enable entity detection

## Example output

```
Entity: NASA (ORGANIZATION) - confidence: 0.95
Entity: International Space Station (LOCATION) - confidence: 0.88
Entity: spacewalk (EVENT) - confidence: 0.82
```

## Prerequisites

- Java 11+
- Maven 3.6+
- Deepgram API key set as `DEEPGRAM_API_KEY` environment variable

## Running the example

```bash
mvn compile exec:java -Dexec.mainClass=Example
```

## Running the test

```bash
mvn test
```