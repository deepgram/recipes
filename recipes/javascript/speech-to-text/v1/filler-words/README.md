# Filler Words — Speech-to-Text v1

Filler words captures hesitation sounds like "uh", "um", "mhm", and "uh huh" in the transcript output. By default, Deepgram removes these from the transcript. Enabling this feature retains them, which is valuable for verbatim transcription, conversation analysis, or fluency assessment.

## Key parameters

| Parameter | Type | Description |
|---|---|---|
| `filler_words` | `boolean` | Include filler words ("uh", "um", etc.) in the transcript |
| `model` | `string` | Speech model to use (e.g., `nova-3`) |
| `punctuate` | `boolean` | Add punctuation to transcript |

## Sample output

```
Yeah, as I recall, it was, um, probably about ten minutes prior to, uh, actually leaving the capsule...
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
