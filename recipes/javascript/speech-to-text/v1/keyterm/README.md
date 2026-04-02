# Key Term Prompting — Speech-to-Text v1

Key term prompting boosts recognition accuracy for specific terms when using the Nova-3 model. Unlike the older `keywords` feature which requires boost values, `keyterm` simply takes an array of strings and the model automatically improves recognition for those terms.

This is especially useful for proper nouns, brand names, technical jargon, or any domain-specific vocabulary that the model might not recognize accurately by default.

## Key parameters

| Parameter | Type | Description |
|---|---|---|
| `keyterm` | `string[]` | List of terms to boost recognition for (Nova-3 only) |
| `model` | `string` | Must be `nova-3` for keyterm support |
| `smart_format` | `boolean` | Apply automatic formatting |

## Sample output

```
Yeah, as I recall, it was probably about 10 minutes prior to actually leaving the capsule. It was back in March of 1965, and Leonov did the first spacewalk...
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
