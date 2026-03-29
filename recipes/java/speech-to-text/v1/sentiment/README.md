# Speech-to-Text Sentiment Analysis

Analyze the emotional tone and attitude expressed in spoken words. This feature detects whether the sentiment is positive, negative, or neutral, along with confidence scores for each segment of text.

## What it does

Sentiment analysis examines the emotional context of speech to determine the speaker's attitude or feelings. It classifies text segments as positive (expressing satisfaction, happiness, approval), negative (expressing dissatisfaction, anger, criticism), or neutral (factual, objective statements). This is valuable for customer service analysis, feedback processing, and understanding speaker emotions.

## Key parameters

- `sentiment`: Set to `true` to enable sentiment analysis

## Example output

```
Text: "NASA astronauts conducted a successful spacewalk"
Sentiment: positive (confidence: 0.87)

Text: "The mission faced several challenges"
Sentiment: neutral (confidence: 0.92)
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