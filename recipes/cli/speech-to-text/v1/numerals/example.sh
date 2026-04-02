#!/usr/bin/env bash
# Recipe: Numerals (STT v1)
#
# Converts spoken numbers to numeric digits in the transcript,
# e.g. "twenty one" becomes "21" and "three hundred" becomes "300".

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg api -X POST \
  "/v1/listen?model=nova-3&numerals=true" \
  -H "Content-Type: application/json" \
  --input <(printf '{"url":"%s"}' "$AUDIO_URL") \
  --jq '.results.channels[0].alternatives[0].transcript'
