# Intent Recognition — Text Analysis v1

Intent recognition detects speaker intents from plain text input using Deepgram's Read API. Unlike the speech-to-text intents feature which operates on audio, this works directly on text — no audio required.

The API identifies intents like requests, complaints, questions, and more, returning per-segment intent labels with confidence scores.

## Key parameters

| Parameter | Type | Description |
|---|---|---|
| `intents` | `boolean` | Enable intent recognition |
| `language` | `string` | Language of the text (e.g., `en`) |

## Sample output

```
Text: I'd like to return this product and get a refund.
  Intent: Return/Exchange Product (confidence: 0.9512)
Text: Can you also update my shipping address for future orders?
  Intent: Update Account Information (confidence: 0.8734)
```

## Prerequisites

- Node.js 20+
- A [Deepgram API key](https://console.deepgram.com/signup?jump=keys)

## Run

```bash
export DEEPGRAM_API_KEY="your-api-key"
npm install
node example.js
```
