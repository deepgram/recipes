#!/usr/bin/env bash
# Recipe: Intent Recognition (STT v1)
#
# Detects speaker intents in the transcript. The CLI does not
# expose --intents directly, so we use dg api.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg api -X POST \
  "/v1/listen?model=nova-3&intents=true" \
  -H "Content-Type: application/json" \
  --input <(printf '{"url":"%s"}' "$AUDIO_URL") \
  --jq '.results.intents.segments[] | .intent + " (confidence: " + (.confidence|tostring) + ")"'
