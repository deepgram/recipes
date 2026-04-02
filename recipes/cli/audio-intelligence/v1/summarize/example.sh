#!/usr/bin/env bash
# Recipe: Audio Summarization (Audio Intelligence v1)
#
# Generates a concise text summary of spoken content by enabling
# the --summarize flag alongside transcription.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg listen "$AUDIO_URL" --model nova-3 --summarize
