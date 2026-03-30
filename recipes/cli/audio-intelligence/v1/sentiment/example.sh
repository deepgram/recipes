#!/usr/bin/env bash
# Recipe: Sentiment Analysis (Audio Intelligence v1)
#
# Performs segment-level sentiment scoring on audio content. Each speech
# segment is classified as positive, negative, or neutral with a
# confidence score. Useful for call center analytics and content analysis.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

curl -s "https://api.deepgram.com/v1/listen?model=nova-3&sentiment=true" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$AUDIO_URL\"}" \
  | python3 -c "
import sys, json
r = json.load(sys.stdin)
avg = r['results']['sentiments']['average']
print(f'Overall sentiment: {avg[\"sentiment\"]} (confidence: {avg[\"sentiment_score\"]:.2f})')
for seg in r['results']['sentiments']['segments']:
    print(f'  {seg[\"sentiment\"]}: {seg[\"text\"][:80]}')
"
