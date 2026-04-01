#!/usr/bin/env bash
# Recipe: Paragraphs (STT v1)
#
# Uses the Deepgram API paragraphs parameter to group the transcript
# into paragraph blocks based on speech pauses and topic shifts.
# The CLI does not expose --paragraphs directly, so we use dg api.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg api -X POST \
  "/v1/listen?model=nova-3&smart_format=true&paragraphs=true" \
  -H "Content-Type: application/json" \
  --input <(printf '{"url":"%s"}' "$AUDIO_URL") \
  --jq '.results.channels[0].alternatives[0].paragraphs.paragraphs[].sentences[].text'
