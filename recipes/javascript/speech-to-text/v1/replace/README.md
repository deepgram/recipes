# Find and Replace — Speech-to-Text v1

The find and replace feature substitutes specific terms in the transcript output with replacement text. Each replacement is specified as a "original:replacement" string.

This is useful for normalizing terminology (e.g., brand name variations), correcting consistent misrecognitions, or anonymizing specific words in the output.

## Key parameters

| Parameter | Type | Description |
|---|---|---|
| `replace` | `string[]` | Array of "original:replacement" pairs |
| `model` | `string` | Speech model to use (e.g., `nova-3`) |
| `smart_format` | `boolean` | Apply additional formatting |

## Sample output

```
Yeah, as I recall, it was probably about 10 minutes prior to actually leaving the spacecraft...
```

(Note: "capsule" is replaced with "spacecraft" in the output.)

## Prerequisites

- Node.js 20+
- A [Deepgram API key](https://console.deepgram.com/signup?jump=keys)

## Run

```bash
export DEEPGRAM_API_KEY="your-api-key"
npm install
node example.js
```
