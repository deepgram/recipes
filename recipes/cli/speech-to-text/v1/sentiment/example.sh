#!/usr/bin/env bash
# Recipe: Sentiment Analysis (Speech-to-Text v1)
#
# Analyzes the emotional tone of speech segments, classifying each as
# positive, negative, or neutral with a confidence score. This is an
# Audio Intelligence feature applied during transcription.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

curl -s "https://api.deepgram.com/v1/listen?model=nova-3&sentiment=true" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$AUDIO_URL\"}" \
  | python3 -c "
import sys, json
r = json.load(sys.stdin)
for seg in r['results']['sentiments']['segments']:
    print(f'{seg[\"sentiment\"]}: {seg[\"text\"]}')
"
