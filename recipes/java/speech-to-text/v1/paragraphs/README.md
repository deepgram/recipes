# Java: Paragraphs

Organizes transcriptions into structured paragraphs and sentences for better document formatting and content organization.

## Feature

Paragraph grouping analyzes speech patterns to automatically break transcriptions into logical paragraphs and sentences. This provides structured output perfect for document creation and content analysis.

## Key Parameters

- `paragraphs`: Enables automatic paragraph and sentence segmentation
- `smartFormat`: Recommended for proper punctuation and formatting
- `model`: Speech model to use (Nova-3 recommended for accuracy)

## Sample Output

```
Paragraph 1:
  Spacewalk is a daring journey that takes a lot of training and preparation.
  It's not just about the technical skills required, but also the mental and physical preparation that astronauts must undergo.

```

## Prerequisites

1. Java 11+
2. Maven 3.6+
3. Set `DEEPGRAM_API_KEY` environment variable

## Run

```bash
mvn exec:java -Dexec.mainClass=Example
```

## Test

```bash
mvn test
```