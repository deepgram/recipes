# Numerals

Convert spoken numbers to numeric digits in the transcript. Phrases like "twenty three" become "23" and "one hundred" become "100", making the output more concise and easier to parse programmatically.

## What it does

The numerals feature converts written-out numbers in the transcript to their digit form. This is useful for financial data, technical content, addresses, phone numbers, and any domain where numeric values appear frequently in speech.

## Key parameters

- `numerals`: Set to `true` to convert spoken numbers to digits

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
