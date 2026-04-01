#!/usr/bin/env bash
# Recipe: Topic Detection (Audio Intelligence v1)
#
# Identifies key topics discussed in audio content using
# the --topics flag alongside transcription.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg listen "$AUDIO_URL" --model nova-3 --topics
