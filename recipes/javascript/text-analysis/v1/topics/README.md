# Topic Detection — Text Analysis v1

Topic detection identifies the key topics discussed in plain text input using Deepgram's Read API. No audio is required — the API works directly on text.

The response includes per-segment topic labels with confidence scores, making it useful for categorizing content, routing support tickets, or understanding what a document is about.

## Key parameters

| Parameter | Type | Description |
|---|---|---|
| `topics` | `boolean` | Enable topic detection |
| `language` | `string` | Language of the text (e.g., `en`) |

## Sample output

```
Text: The new electric vehicle from Tesla features a range of 400 miles and uses a revolutionary battery technology.
  Topic: Electric Vehicles (confidence: 0.9312)
  Topic: Battery Technology (confidence: 0.8456)
Text: In healthcare news, a new mRNA vaccine shows promising results...
  Topic: Healthcare (confidence: 0.9178)
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
