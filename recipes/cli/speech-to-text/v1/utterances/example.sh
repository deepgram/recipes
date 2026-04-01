#!/usr/bin/env bash
# Recipe: Utterances (STT v1)
#
# Splits the transcript into per-utterance segments, each with start
# and end timestamps. The CLI does not expose --utterances directly,
# so we use dg api.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg api -X POST \
  "/v1/listen?model=nova-3&utterances=true" \
  -H "Content-Type: application/json" \
  --input <(printf '{"url":"%s"}' "$AUDIO_URL") \
  --jq '.results.utterances[] | "[" + (.start|tostring) + "s] " + .transcript'
