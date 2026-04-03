# Text Summarization (Text Analysis)

Generates a concise summary from plain text input using the Deepgram Read API. This works directly on text without requiring audio, making it useful for condensing articles, documents, or conversation transcripts.

## What this feature does

Text summarization extracts the key points from a body of text and produces a shorter version that captures the essential information. This is different from audio summarization, which first transcribes audio before summarizing.

## Key parameters

- **summarize=v2**: Enables text summarization (v2 is the summarization engine version)
- **language=en**: Specifies the language of the input text

## Sample output

```
Summary: Deepgram provides AI-powered speech recognition and text-to-speech APIs with their Nova-3 model, offering audio intelligence features and SDKs for multiple programming languages.
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable

## Run the example

```bash
cargo run
```
