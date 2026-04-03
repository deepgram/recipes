# Intent Recognition (Text Analysis)

Detects speaker intents from plain text input using Deepgram's Read API. Unlike speech-to-text intent detection which operates on audio, text analysis works directly on text content to identify what actions or outcomes the speaker is trying to achieve.

## What this feature does

Intent recognition analyzes the meaning and context of text to understand the purpose behind the words. For example, a customer support message might contain intents like "return product", "request refund", or "update address". This is valuable for routing, automation, and understanding user needs.

## Key parameters

- **intents=true**: Enables intent recognition on the text input
- **language=en**: Specifies the language of the input text

## Sample output

```
Text: I'd like to return this product and get a refund.
  Intent: Return/Exchange Product (confidence: 0.95)
  Intent: Get Refund (confidence: 0.87)
Text: Can you also update my shipping address for future orders?
  Intent: Update Account Information (confidence: 0.91)
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable

## Run the example

```bash
cargo run
```
