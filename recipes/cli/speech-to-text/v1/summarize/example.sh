#!/usr/bin/env bash
# Recipe: Summarize (Speech-to-Text v1)
#
# Generates a concise text summary of the transcribed audio content.
# This is an Audio Intelligence feature — the API transcribes the audio
# and then runs a summarization pass over the transcript.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

curl -s "https://api.deepgram.com/v1/listen?model=nova-3&summarize=v2" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$AUDIO_URL\"}" \
  | python3 -c "
import sys, json
r = json.load(sys.stdin)
print(f'Summary: {r[\"results\"][\"summary\"][\"short\"]}')
"
