#!/usr/bin/env bash
# Recipe: Select Audio Encoding (Text-to-Speech v1)
#
# Demonstrates choosing the output audio encoding format. Deepgram TTS
# supports mp3, linear16, flac, mulaw, alaw, opus, and aac. The
# container parameter controls the wrapping format (none, wav, ogg).

OUTPUT_FILE="/tmp/deepgram_tts_encoding.wav"

curl -s "https://api.deepgram.com/v1/speak?model=aura-2-thalia-en&encoding=linear16&container=wav" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello from Deepgram. This audio uses linear sixteen encoding in a WAV container."}' \
  -o "$OUTPUT_FILE"

SIZE=$(wc -c < "$OUTPUT_FILE")
echo "Audio saved as WAV with linear16 encoding ($SIZE bytes)"

rm -f "$OUTPUT_FILE"
