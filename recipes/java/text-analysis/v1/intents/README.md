# Text Intent Recognition

Detect speaker intents from plain text input using Deepgram's text analysis (Read) API. This works directly on text without requiring audio, making it useful for analyzing chat transcripts, emails, support tickets, or any text content.

## What it does

The intent recognition feature analyzes text segments and identifies the underlying intents expressed by the author. Each segment receives a list of detected intents with confidence scores, helping you understand what actions or requests are being communicated.

## Key parameters

- `intents`: Set to `true` to enable intent recognition on the text input
- `language`: Language code (e.g., `"en"` for English)

## Example output

```
Text: I'd like to return this product and get a refund.
  Intent: Return/Exchange (87%)
  Intent: Refund (82%)
Text: Can you also update my shipping address for future orders?
  Intent: Update Information (79%)
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
