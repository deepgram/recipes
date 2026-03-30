#!/usr/bin/env bash
# Recipe: Stream Audio Response (Text-to-Speech v1)
#
# Streams TTS audio as it generates, writing chunks to a file. Uses
# linear16 encoding for raw PCM audio. The streaming approach lets
# you start playback before the full response is complete.

OUTPUT_FILE="/tmp/deepgram_tts_stream.raw"

curl -sN "https://api.deepgram.com/v1/speak?model=aura-2-thalia-en&encoding=linear16" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello from Deepgram. This is a streaming text-to-speech example using linear sixteen encoding."}' \
  -o "$OUTPUT_FILE"

SIZE=$(wc -c < "$OUTPUT_FILE")
echo "Streamed audio saved to $OUTPUT_FILE ($SIZE bytes, linear16 PCM)"

rm -f "$OUTPUT_FILE"
