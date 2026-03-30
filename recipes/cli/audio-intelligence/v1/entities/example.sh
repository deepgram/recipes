#!/usr/bin/env bash
# Recipe: Entity Detection (Audio Intelligence v1)
#
# Identifies named entities in audio — people, organisations, locations,
# dates, and more. Each entity includes a label (type), value (text),
# and confidence score.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

curl -s "https://api.deepgram.com/v1/listen?model=nova-3&detect_entities=true" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$AUDIO_URL\"}" \
  | python3 -c "
import sys, json
r = json.load(sys.stdin)
seen = set()
for seg in r['results']['entities']['segments']:
    for e in seg['entities']:
        key = f'{e[\"label\"]}:{e[\"value\"]}'
        if key not in seen:
            seen.add(key)
            print(f'{e[\"label\"]}: {e[\"value\"]} (confidence: {e[\"confidence\"]:.2f})')
"
