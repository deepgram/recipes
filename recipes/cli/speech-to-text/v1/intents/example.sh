#!/usr/bin/env bash
# Recipe: Intent Recognition (Speech-to-Text v1)
#
# Detects speaker intents within the audio. Each segment of speech
# is analyzed for its communicative purpose — e.g. informing,
# requesting, describing. This is an Audio Intelligence feature.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

curl -s "https://api.deepgram.com/v1/listen?model=nova-3&intents=true" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$AUDIO_URL\"}" \
  | python3 -c "
import sys, json
r = json.load(sys.stdin)
for seg in r['results']['intents']['segments']:
    for i in seg['intents']:
        print(f'Intent: {i[\"intent\"]} (confidence: {i[\"confidence\"]:.2f})')
"
