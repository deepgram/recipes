#!/usr/bin/env bash
# Recipe: Topic Detection (STT v1)
#
# Identifies topics discussed in the audio. Uses the --topics
# flag on dg listen to enable topic detection.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg listen "$AUDIO_URL" --model nova-3 --topics
