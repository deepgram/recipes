#!/usr/bin/env bash
# Recipe: Language Detection (STT v1)
#
# Automatically detects the spoken language in the audio.
# The CLI does not expose --detect-language directly, so we
# use dg api and extract the detected language from the response.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg api -X POST \
  "/v1/listen?model=nova-3&detect_language=true" \
  -H "Content-Type: application/json" \
  --input <(printf '{"url":"%s"}' "$AUDIO_URL") \
  --jq '"Detected: " + .results.channels[0].detected_language + "\nTranscript: " + .results.channels[0].alternatives[0].transcript[:120]'
