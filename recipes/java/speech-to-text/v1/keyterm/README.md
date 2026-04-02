# Key Term Prompting

Boost recognition of specific key terms using Nova-3's prompt-based guidance. This is different from keyword boosting — keyterm prompting tells the model to watch for specific vocabulary without numeric boost scores, producing more natural and accurate results for domain-specific terms.

## What it does

Key term prompting provides the model with a list of terms it should pay special attention to during transcription. This is especially useful for proper nouns, technical jargon, brand names, or acronyms that the model might otherwise misinterpret. The model uses these terms as contextual hints rather than hard overrides.

## Key parameters

- `keyterm`: List of key terms to prompt the model with (e.g., `["NASA", "ISS", "spacewalk"]`)

## Example output

```
Yeah, and it's prior to them coming back in, they have to do a suit check on the ISS ...
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
