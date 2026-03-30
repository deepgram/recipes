#!/usr/bin/env bash
# Recipe: Transcribe Local Audio File (Speech-to-Text v1)
#
# Downloads a demo audio file locally, then sends the raw binary
# to the Deepgram REST API for pre-recorded transcription.
# This pattern works with any local audio file (wav, mp3, flac, ogg).

AUDIO_URL="https://dpgr.am/spacewalk.wav"
AUDIO_FILE="/tmp/spacewalk.wav"

curl -sL "$AUDIO_URL" -o "$AUDIO_FILE"

curl -s "https://api.deepgram.com/v1/listen?model=nova-3&smart_format=true" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: audio/wav" \
  --data-binary "@$AUDIO_FILE" \
  | python3 -c "
import sys, json
r = json.load(sys.stdin)
print(r['results']['channels'][0]['alternatives'][0]['transcript'])
"

rm -f "$AUDIO_FILE"
