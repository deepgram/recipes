#!/usr/bin/env bash
# Recipe: Smart Format (Speech-to-Text v1)
#
# Enables automatic formatting of numbers, dates, currencies, and addresses
# in the transcript output. Compare this output against the plain transcribe-url
# recipe to see the difference smart formatting makes.

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
