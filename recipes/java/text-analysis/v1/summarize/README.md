# Text Summarization

Generate a concise summary from plain text input using Deepgram's text analysis (Read) API. This works directly on text without requiring audio, making it useful for summarizing articles, documents, chat logs, or any text content.

## What it does

The summarization feature processes the input text and generates a condensed summary capturing the key points and essential information. This is useful for quickly understanding long documents, creating abstracts, or producing content digests.

## Key parameters

- `summarize`: Set to `TextAnalyzeRequestSummarize.V2` to enable the latest summarization model
- `language`: Language code (e.g., `"en"` for English)

## Example output

```
Summary: Deepgram provides AI-powered speech recognition and text-to-speech APIs with high accuracy, along with audio intelligence features accessible through multiple language SDKs.
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
