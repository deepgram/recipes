#!/usr/bin/env bash
# Recipe: Search (Speech-to-Text v1)
#
# Searches for specific words or phrases in the audio and returns matches
# with timing and confidence scores. Useful for finding key moments
# in long recordings without reading the entire transcript.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

curl -s "https://api.deepgram.com/v1/listen?model=nova-3&search=spacewalk&search=moon" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$AUDIO_URL\"}" \
  | python3 -c "
import sys, json
r = json.load(sys.stdin)
for s in r['results']['channels'][0]['search']:
    for hit in s['hits']:
        print(f'Found \"{s[\"query\"]}\" at {hit[\"start\"]:.2f}s-{hit[\"end\"]:.2f}s (confidence: {hit[\"confidence\"]:.2f})')
"
