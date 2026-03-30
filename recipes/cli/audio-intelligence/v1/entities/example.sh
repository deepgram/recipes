#!/usr/bin/env bash
# Recipe: Entity Detection (Audio Intelligence v1)
#
# Identifies named entities in the audio — people, organisations,
# locations, dates, and other proper nouns. Each entity is returned
# with its type label and the recognised text value.

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
        print(f'{e[\"label\"]}: {e[\"value\"]}')
"
