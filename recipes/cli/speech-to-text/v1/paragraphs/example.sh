#!/usr/bin/env bash
# Recipe: Paragraphs (Speech-to-Text v1)
#
# Groups the transcript into paragraph blocks based on natural pauses
# and topic shifts in speech. Each paragraph contains one or more
# sentences with timing information.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

curl -s "https://api.deepgram.com/v1/listen?model=nova-3&paragraphs=true&smart_format=true" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$AUDIO_URL\"}" \
  | python3 -c "
import sys, json
r = json.load(sys.stdin)
paras = r['results']['channels'][0]['alternatives'][0]['paragraphs']['paragraphs']
for i, p in enumerate(paras, 1):
    sentences = ' '.join(s['text'] for s in p['sentences'])
    print(f'[Paragraph {i}]')
    print(sentences)
    print()
"
