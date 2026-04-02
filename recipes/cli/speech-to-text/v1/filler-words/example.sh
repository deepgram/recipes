#!/usr/bin/env bash
# Recipe: Filler Words (STT v1)
#
# Enables filler word detection so that words like "uh", "um", "mhm"
# are preserved in the transcript instead of being removed.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg api -X POST \
  "/v1/listen?model=nova-3&filler_words=true&smart_format=true" \
  -H "Content-Type: application/json" \
  --input <(printf '{"url":"%s"}' "$AUDIO_URL") \
  --jq '.results.channels[0].alternatives[0].transcript'
