#!/usr/bin/env bash
# Recipe: Multichannel (STT v1)
#
# Transcribes each audio channel independently. Useful for stereo
# recordings where each channel carries a different speaker.
# The CLI does not expose --multichannel directly, so we use dg api.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg api -X POST \
  "/v1/listen?model=nova-3&multichannel=true" \
  -H "Content-Type: application/json" \
  --input <(printf '{"url":"%s"}' "$AUDIO_URL") \
  --jq '.results.channels[] | "Channel " + (.channel_index|tostring) + ": " + .alternatives[0].transcript[:120]'
