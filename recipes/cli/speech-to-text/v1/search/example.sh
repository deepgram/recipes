#!/usr/bin/env bash
# Recipe: Search (STT v1)
#
# Searches for specific words or phrases in the audio and returns
# matches with confidence scores. Uses dg api since the CLI does
# not expose --search directly.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg api -X POST \
  "/v1/listen?model=nova-3&search=space&search=shuttle" \
  -H "Content-Type: application/json" \
  --input <(printf '{"url":"%s"}' "$AUDIO_URL") \
  --jq '.results.search.channels[0].hits[] | .query + " found at " + (.start|tostring) + "s (confidence: " + (.confidence|tostring) + ")"'
