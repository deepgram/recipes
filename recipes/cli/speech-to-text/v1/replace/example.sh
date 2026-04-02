#!/usr/bin/env bash
# Recipe: Find and Replace (STT v1)
#
# Replaces specific terms in the transcript output. Uses the format
# "original:replacement" to swap words after transcription, useful
# for correcting brand names or normalizing terminology.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg api -X POST \
  "/v1/listen?model=nova-3&replace=shuttle:Shuttle&replace=space:Space&smart_format=true" \
  -H "Content-Type: application/json" \
  --input <(printf '{"url":"%s"}' "$AUDIO_URL") \
  --jq '.results.channels[0].alternatives[0].transcript'
