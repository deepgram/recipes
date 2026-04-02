# Numerals — Speech-to-Text v1

The numerals feature converts spoken numbers into numeric digit format in the transcript. For example, "nineteen sixty five" becomes "1965" and "ten minutes" becomes "10 minutes".

This provides explicit control over number formatting. While `smart_format` also handles numbers (along with dates, currencies, etc.), `numerals` isolates just the number conversion behavior.

## Key parameters

| Parameter | Type | Description |
|---|---|---|
| `numerals` | `boolean` | Convert spoken numbers to numeric digits |
| `model` | `string` | Speech model to use (e.g., `nova-3`) |
| `punctuate` | `boolean` | Add punctuation to transcript |

## Sample output

```
Yeah, as I recall, it was probably about 10 minutes prior to actually leaving the capsule. It was back in March of 1965.
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
