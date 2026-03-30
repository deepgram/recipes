#!/usr/bin/env bash
# Recipe: Keyword Boosting (Speech-to-Text v1)
#
# Boosts recognition accuracy for specific keywords or proper nouns.
# The weight (after the colon) controls how much to prioritise each
# keyword. Higher weights mean stronger boosting.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

curl -s "https://api.deepgram.com/v1/listen?model=nova-3&keywords=spacewalk:2&keywords=ISS:1.5" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$AUDIO_URL\"}" \
  | python3 -c "
import sys, json
r = json.load(sys.stdin)
print(r['results']['channels'][0]['alternatives'][0]['transcript'])
"
