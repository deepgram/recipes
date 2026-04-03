# Text Topic Detection

Identify topics discussed in plain text using Deepgram's text analysis (Read) API. Returns per-segment topic lists with confidence scores, working directly on text without requiring audio.

## What it does

The topic detection feature analyzes text segments and identifies the key topics being discussed. Each segment receives a list of detected topics with confidence scores, helping you categorize and organize text content by subject matter.

## Key parameters

- `topics`: Set to `true` to enable topic detection on the text input
- `language`: Language code (e.g., `"en"` for English)

## Example output

```
Text: The new electric vehicle from Tesla features a range of 400 miles and uses a revolutionary battery technology.
  Topic: Electric Vehicles (92%)
  Topic: Technology (85%)
Text: In healthcare news, a new mRNA vaccine shows promising results in early clinical trials for treating certain types of cancer.
  Topic: Healthcare (94%)
  Topic: Medical Research (88%)
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
