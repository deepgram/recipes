#!/usr/bin/env bash
# Recipe: Intent Recognition (Audio Intelligence v1)
#
# Detects speaker intents from audio context. Each speech segment is
# analysed for communicative purpose — informing, requesting, describing,
# etc. Useful for understanding caller needs in contact centres.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

curl -s "https://api.deepgram.com/v1/listen?model=nova-3&intents=true" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$AUDIO_URL\"}" \
  | python3 -c "
import sys, json
r = json.load(sys.stdin)
seen = set()
for seg in r['results']['intents']['segments']:
    for i in seg['intents']:
        if i['intent'] not in seen:
            seen.add(i['intent'])
            print(f'Intent: {i[\"intent\"]} (confidence: {i[\"confidence\"]:.2f})')
"
