#!/usr/bin/env bash
# Recipe: Intent Recognition (Audio Intelligence v1)
#
# Detects speaker intents from audio content by enabling the intents
# parameter alongside transcription. Uses dg api since the CLI does
# not expose --intents directly.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg api -X POST \
  "/v1/listen?model=nova-3&intents=true&smart_format=true" \
  -H "Content-Type: application/json" \
  --input <(printf '{"url":"%s"}' "$AUDIO_URL") \
  --jq '.results.intents'
