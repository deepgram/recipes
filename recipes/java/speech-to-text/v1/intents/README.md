# Speech-to-Text Intent Recognition

Detect and classify the underlying intent or purpose behind spoken words. This feature analyzes the context and meaning of speech to identify what the speaker is trying to accomplish or communicate.

## What it does

Intent recognition goes beyond simple transcription to understand the purpose behind the words. It identifies whether the speaker is making a request, providing information, asking a question, giving instructions, or expressing other types of communicative intent. This is particularly useful for customer service, voice assistants, and conversational AI applications.

## Key parameters

- `intents`: Set to `true` to enable intent recognition

## Example output

```
Intent: Informational (confidence: 0.92)
Intent: Descriptive (confidence: 0.88)
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