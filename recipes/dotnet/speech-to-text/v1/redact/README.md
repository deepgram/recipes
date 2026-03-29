# Redact

Automatically removes or masks sensitive information from transcripts using Deepgram's redaction feature.

The redaction feature identifies and replaces sensitive data such as credit card numbers (PCI), social security numbers (SSN), and other personally identifiable information with [REDACTED] placeholders, helping maintain privacy and compliance requirements.

## Key Parameters

- `Redact = new List<string> { "pci", "ssn" }` - Enables redaction for specified data types
- Available redaction types: `"pci"`, `"ssn"`, `"numbers"`, `"banking"`

## Output

The redacted transcript is returned at the standard location with sensitive information replaced:

```
Redacted transcript:
NASA astronaut Kjell Lindgren talks about spacewalks and [REDACTED] for station maintenance.
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable to your Deepgram API key
- .NET 8.0 or later

## Run

```bash
dotnet run
```