# Measurements — Speech-to-Text v1

The measurements feature converts spoken measurement values into standard abbreviations in the transcript output. For example, "five feet six inches" becomes "5 ft 6 in", and "twenty degrees celsius" becomes "20°C".

This is particularly useful for technical, medical, engineering, or scientific transcription where consistent and standardized measurement formatting matters.

## Key parameters

| Parameter | Type | Description |
|---|---|---|
| `measurements` | `boolean` | Convert spoken measurements to standard abbreviations |
| `model` | `string` | Speech model to use (e.g., `nova-3`) |
| `smart_format` | `boolean` | Apply additional formatting (numbers, dates, etc.) |

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
