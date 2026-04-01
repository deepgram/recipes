#!/usr/bin/env bash
# Recipe: Intent Recognition (Audio Intelligence v1)
#
# Detects speaker intents — the goals or purposes behind what is
# being said. Each segment is returned with one or more intents
# and a confidence score.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg listen "$AUDIO_URL" \
  --model nova-3 \
  --intents \
  -o json \
  | python3 -c "
import sys, json
r = json.load(sys.stdin)
for seg in r['results']['intents']['segments']:
    for i in seg['intents']:
        print(f'{i[\"intent\"]} (confidence: {i[\"confidence_score\"]:.2f})')
"
