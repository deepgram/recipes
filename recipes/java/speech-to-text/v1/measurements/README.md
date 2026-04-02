# Measurements

Convert spoken measurements to standard abbreviations in the transcript. Phrases like "five kilometers" become "5 km" and "ten pounds" become "10 lb", producing cleaner and more readable output for technical or scientific content.

## What it does

The measurements feature detects spoken measurement units and converts them to their standard abbreviated forms. This is useful for medical, scientific, engineering, or any domain where measurements are frequently mentioned and need to be displayed concisely.

## Key parameters

- `measurements`: Set to `true` to enable measurement abbreviation conversion

## Example output

```
Yeah, and it's prior to them coming back in, they have to do a suit check ...
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
