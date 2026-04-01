#!/usr/bin/env bash
# Recipe: Transcribe Audio from URL (STT v1)
#
# Sends a publicly hosted audio URL to Deepgram for transcription
# using the nova-3 model with smart formatting enabled.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg listen "$AUDIO_URL" --model nova-3 --smart-format
