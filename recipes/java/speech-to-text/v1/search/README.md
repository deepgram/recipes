# Speech-to-Text Search Terms

Search for specific words or phrases within audio content and get their exact timing and location. This feature helps you quickly find mentions of particular terms without having to read through the entire transcript.

## What it does

The search feature allows you to specify terms or phrases to look for in the audio content. When those terms are found, the API returns their exact timestamps, confidence scores, and contextual information. This is particularly useful for finding specific topics, keywords, or phrases within long recordings, meetings, or interviews.

## Key parameters

- `search`: List of terms to search for (e.g., `["NASA", "spacewalk"]`)

## Example output

```
Query: "NASA"
  Found at 2.15 - 2.87 seconds: confidence 0.94

Query: "spacewalk"
  Found at 15.32 - 16.48 seconds: confidence 0.89
  Found at 28.76 - 29.52 seconds: confidence 0.92
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