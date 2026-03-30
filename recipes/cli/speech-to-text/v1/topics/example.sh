#!/usr/bin/env bash
# Recipe: Topic Detection (Speech-to-Text v1)
#
# Identifies topics discussed in the audio. The API returns a list of
# topic segments, each containing one or more detected topics with
# confidence scores. This is an Audio Intelligence feature.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

curl -s "https://api.deepgram.com/v1/listen?model=nova-3&topics=true" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$AUDIO_URL\"}" \
  | python3 -c "
import sys, json
r = json.load(sys.stdin)
for seg in r['results']['topics']['segments']:
    for t in seg['topics']:
        print(f'Topic: {t[\"topic\"]} (confidence: {t[\"confidence\"]:.2f})')
"
