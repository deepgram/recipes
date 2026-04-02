# Find and Replace

Find and replace specific terms in the transcript output. Useful for expanding abbreviations, correcting commonly misheard words, or standardizing terminology in the final transcript.

## What it does

The replace feature performs text substitution on the transcript after transcription. You provide pairs in the format `"original:replacement"`, and every occurrence of the original term is replaced with the replacement text. This happens at the output level — the underlying model still processes the audio normally.

## Key parameters

- `replace`: List of find-replace pairs in `"original:replacement"` format (e.g., `["NASA:National Aeronautics and Space Administration"]`)

## Example output

```
Yeah, and it's prior to them coming back in at National Aeronautics and Space Administration ...
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
