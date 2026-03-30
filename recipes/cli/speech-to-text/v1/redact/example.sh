#!/usr/bin/env bash
# Recipe: Redaction (Speech-to-Text v1)
#
# Redacts sensitive information from the transcript. PCI data (credit card
# numbers) and SSNs are replaced with redaction markers. Useful for
# compliance in call center and financial audio processing.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

curl -s "https://api.deepgram.com/v1/listen?model=nova-3&redact=pci&redact=ssn" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$AUDIO_URL\"}" \
  | python3 -c "
import sys, json
r = json.load(sys.stdin)
print(r['results']['channels'][0]['alternatives'][0]['transcript'])
"
