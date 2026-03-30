#!/usr/bin/env bash
# Recipe: Multichannel (Speech-to-Text v1)
#
# Transcribes each audio channel independently. For stereo or multi-track
# recordings, each channel gets its own transcript — useful when different
# speakers are on different channels (e.g. call center recordings).

AUDIO_URL="https://dpgr.am/spacewalk.wav"

curl -s "https://api.deepgram.com/v1/listen?model=nova-3&multichannel=true" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$AUDIO_URL\"}" \
  | python3 -c "
import sys, json
r = json.load(sys.stdin)
for i, ch in enumerate(r['results']['channels']):
    print(f'[Channel {i}] {ch[\"alternatives\"][0][\"transcript\"]}')
"
