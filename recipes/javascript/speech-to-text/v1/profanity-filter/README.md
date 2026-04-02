# Profanity Filter — Speech-to-Text v1

The profanity filter masks profane words in the transcript output by replacing them with asterisks or similar masking characters. This is useful for content moderation, broadcast compliance, subtitle generation, or any scenario where clean language output is required.

Note: the spacewalk demo audio does not contain profanity, so the filter will not visibly alter the transcript for this sample.

## Key parameters

| Parameter | Type | Description |
|---|---|---|
| `profanity_filter` | `boolean` | Mask profanity in the transcript |
| `model` | `string` | Speech model to use (e.g., `nova-3`) |
| `smart_format` | `boolean` | Apply additional formatting |

## Sample output

```
Yeah, as I recall, it was probably about 10 minutes prior to actually leaving the capsule...
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
