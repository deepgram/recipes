# Topic Detection (Text Analysis)

Identifies topics discussed in plain text input using the Deepgram Read API. Returns per-segment topic classifications with confidence scores, without requiring any audio input.

## What this feature does

Topic detection analyzes text content to identify the subjects being discussed. Each segment of text is classified with one or more topics and associated confidence scores. This is useful for content categorization, routing, and understanding what subjects are covered in a document.

## Key parameters

- **topics=true**: Enables topic detection on the text input
- **language=en**: Specifies the language of the input text

## Sample output

```
Text: The new electric vehicle from Tesla features a range of 400 miles and uses a revolutionary battery technology.
  Topic: Electric Vehicles (confidence: 0.94)
  Topic: Technology (confidence: 0.87)
Text: In healthcare news, a new mRNA vaccine shows promising results.
  Topic: Healthcare (confidence: 0.96)
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable

## Run the example

```bash
cargo run
```
