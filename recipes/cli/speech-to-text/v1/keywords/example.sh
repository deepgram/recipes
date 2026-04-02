#!/usr/bin/env bash
# Recipe: Keyword Boosting (STT v1)
#
# Boosts recognition accuracy for specific keywords or proper nouns.
# Uses dg api since the CLI does not expose --keywords directly.
# The :2 suffix sets the boost intensity.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg api -X POST \
  "/v1/listen?model=nova-3&keywords=Deepgram:2&keywords=spacewalk:1.5" \
  -H "Content-Type: application/json" \
  --input <(printf '{"url":"%s"}' "$AUDIO_URL") \
  --jq '.results.channels[0].alternatives[0].transcript'
