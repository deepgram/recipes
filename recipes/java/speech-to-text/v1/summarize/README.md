# Speech-to-Text Audio Summarization

Generate an automatic summary of audio content using Deepgram's summarization feature. This feature analyzes the full transcript and produces a concise overview of the key points discussed.

## What it does

The summarization feature processes the entire audio transcript and generates a condensed summary that captures the main topics, key points, and essential information. This is particularly useful for long recordings, meetings, podcasts, or interviews where you need a quick overview of the content.

## Key parameters

- `summarize`: Set to `"v2"` to enable the latest summarization model

## Example output

```
Summary: NASA astronauts conducted a spacewalk outside the International Space Station to perform maintenance and upgrades on critical systems.
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