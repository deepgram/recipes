#!/usr/bin/env bash
# Recipe: Generate Audio to File (Text-to-Speech v1)
#
# Converts text to speech using Deepgram's TTS API and saves the
# resulting audio to a file. Uses the aura-2-thalia-en voice model
# which produces natural-sounding English speech.

OUTPUT_FILE="/tmp/deepgram_tts_output.mp3"

curl -s "https://api.deepgram.com/v1/speak?model=aura-2-thalia-en" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello from Deepgram. This is a text-to-speech demonstration using the aura-2 voice model."}' \
  -o "$OUTPUT_FILE"

SIZE=$(wc -c < "$OUTPUT_FILE")
echo "Audio saved to $OUTPUT_FILE ($SIZE bytes)"

rm -f "$OUTPUT_FILE"
