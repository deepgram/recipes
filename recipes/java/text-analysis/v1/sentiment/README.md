# Text Sentiment Analysis

Analyze sentiment (positive, negative, neutral) on plain text using Deepgram's text analysis (Read) API. Returns both an overall average sentiment and per-segment breakdowns, working directly on text without requiring audio.

## What it does

The sentiment analysis feature evaluates each text segment and assigns a sentiment label (positive, negative, or neutral) along with a confidence score. It also provides an overall average sentiment for the entire input. This is useful for analyzing customer feedback, reviews, support tickets, or any text where emotional tone matters.

## Key parameters

- `sentiment`: Set to `true` to enable sentiment analysis on the text input
- `language`: Language code (e.g., `"en"` for English)

## Example output

```
Average: positive (0.65)
[positive] I absolutely love this product! It exceeded all my expectations.
[negative] However, the shipping was terrible and took three weeks to arrive.
[positive] Overall, I'm satisfied with my purchase despite the delivery issues.
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
