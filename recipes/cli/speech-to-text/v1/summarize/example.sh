#!/usr/bin/env bash
# Recipe: Summarize (STT v1)
#
# Generates a concise summary of the transcript alongside the
# full transcription. Uses the --summarize flag on dg listen.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg listen "$AUDIO_URL" --model nova-3 --summarize
