#!/usr/bin/env bash
# Recipe: Entity Detection (STT v1)
#
# Identifies named entities — people, organisations, locations,
# dates — in the transcript. Uses dg api since the CLI does not
# expose --detect-entities directly.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg api -X POST \
  "/v1/listen?model=nova-3&detect_entities=true" \
  -H "Content-Type: application/json" \
  --input <(printf '{"url":"%s"}' "$AUDIO_URL") \
  --jq '.results.entities.segments[].entities[] | .label + ": " + .value'
