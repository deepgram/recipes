#!/usr/bin/env bash
# Recipe: Language Detection (Speech-to-Text v1)
#
# Automatically detects the spoken language in the audio. The response
# includes the detected language code (e.g. "en") in addition to the
# transcript. Useful when the input language is unknown.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

curl -s "https://api.deepgram.com/v1/listen?model=nova-3&detect_language=true" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$AUDIO_URL\"}" \
  | python3 -c "
import sys, json
r = json.load(sys.stdin)
ch = r['results']['channels'][0]
print(f'Detected language: {ch[\"detected_language\"]}')
print(f'Transcript: {ch[\"alternatives\"][0][\"transcript\"]}')
"
