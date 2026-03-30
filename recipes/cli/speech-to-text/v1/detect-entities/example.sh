#!/usr/bin/env bash
# Recipe: Entity Detection (Speech-to-Text v1)
#
# Identifies named entities in the audio — people, places, organisations,
# dates, and more. Each entity includes a label, value, and confidence
# score. This is an Audio Intelligence feature.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

curl -s "https://api.deepgram.com/v1/listen?model=nova-3&detect_entities=true" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$AUDIO_URL\"}" \
  | python3 -c "
import sys, json
r = json.load(sys.stdin)
for seg in r['results']['entities']['segments']:
    for e in seg['entities']:
        print(f'{e[\"label\"]}: {e[\"value\"]} (confidence: {e[\"confidence\"]:.2f})')
"
