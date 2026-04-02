#!/usr/bin/env bash
# Recipe: Transcribe Audio from URL (STT v2)
#
# Uses the v2 API with the flux-general-en model for high-accuracy
# English transcription. The CLI automatically routes to v2 when
# a flux-* model is specified.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg listen "$AUDIO_URL" --model flux-general-en
