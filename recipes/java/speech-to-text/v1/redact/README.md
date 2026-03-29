# Speech-to-Text PII Redaction

Automatically detect and redact personally identifiable information (PII) from audio transcriptions. This feature protects sensitive data by replacing it with [REDACTED] markers in the transcript.

## What it does

PII redaction automatically identifies and removes sensitive information from transcripts to protect privacy and comply with data protection regulations. It can detect and redact various types of PII including credit card numbers (PCI), social security numbers (SSN), phone numbers, email addresses, and other sensitive data patterns. The redacted information is replaced with [REDACTED] markers in the final transcript.

## Key parameters

- `redact`: List of PII types to redact (e.g., `["pci", "ssn"]`)

Available redaction types:
- `pci`: Credit card numbers
- `ssn`: Social security numbers
- `numbers`: General numeric sequences
- `true`: All supported PII types

## Example output

```
Redacted transcript: NASA astronauts conducted a spacewalk outside the International Space Station.
```

If PII was detected and redacted:
```
Redacted transcript: My credit card number is [REDACTED] and my SSN is [REDACTED].
Note: PII has been automatically redacted from the transcript
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