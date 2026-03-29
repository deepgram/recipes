# Speech-to-Text Keyword Boosting

Improve transcription accuracy for specific keywords by providing boost values. This feature enhances the recognition of domain-specific terms, proper nouns, or technical vocabulary that might be challenging for the model to recognize correctly.

## What it does

Keyword boosting allows you to increase the likelihood that specific terms will be correctly transcribed by providing them with boost values. The boost value (typically between 1 and 4) tells the model to prioritize these terms when making transcription decisions. This is particularly useful for technical jargon, company names, product names, or any specialized vocabulary relevant to your audio content.

## Key parameters

- `keywords`: List of keywords with boost values (e.g., `["NASA:2", "spacewalk:1.5"]`)

Boost value guidelines:
- 1.0: Normal weight (no boost)
- 1.5-2.0: Moderate boost for uncommon terms
- 2.0-3.0: Strong boost for technical terms or proper nouns
- 3.0-4.0: Maximum boost for critical terms

## Example output

```
Enhanced transcript with keyword boosting:
NASA astronauts conducted a spacewalk outside the International Space Station to perform maintenance and upgrades on critical systems.

Note: The keywords 'NASA' and 'spacewalk' have been boosted for improved recognition accuracy.
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