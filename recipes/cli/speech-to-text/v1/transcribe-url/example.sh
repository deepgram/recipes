#!/usr/bin/env bash
# Recipe: Transcribe Audio from URL (Speech-to-Text v1)
#
# Sends a URL pointing to a hosted audio file to the Deepgram REST API
# for pre-recorded transcription. This is the most basic STT operation
# and the foundation for all other speech-to-text feature recipes.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

curl -s "https://api.deepgram.com/v1/listen?model=nova-3&smart_format=true" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$AUDIO_URL\"}" \
  | python3 -c "
import sys, json
r = json.load(sys.stdin)
print(r['results']['channels'][0]['alternatives'][0]['transcript'])
"
