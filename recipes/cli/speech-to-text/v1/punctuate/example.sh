#!/usr/bin/env bash
# Recipe: Punctuation (Speech-to-Text v1)
#
# Adds punctuation marks to the transcript. Without this flag, the transcript
# is a continuous string with no sentence boundaries. With punctuate=true,
# Deepgram inserts periods, commas, and question marks where appropriate.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

curl -s "https://api.deepgram.com/v1/listen?model=nova-3&punctuate=true" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$AUDIO_URL\"}" \
  | python3 -c "
import sys, json
r = json.load(sys.stdin)
print(r['results']['channels'][0]['alternatives'][0]['transcript'])
"
