#!/usr/bin/env bash
# Recipe: Live Streaming Transcription (STT v2)
#
# Streams audio via ffmpeg to dg listen using the flux-general-en model.
# The CLI automatically routes to the v2 WebSocket endpoint when a
# flux-* model is specified. V2 provides turn-based transcription
# with contextual turn detection.

AUDIO_URL="https://dpgr.am/spacewalk.wav"
AUDIO_FILE="/tmp/spacewalk.wav"

curl -sL "$AUDIO_URL" -o "$AUDIO_FILE"

ffmpeg -i "$AUDIO_FILE" -f s16le -ar 16000 -ac 1 -loglevel quiet - \
  | dg listen --encoding linear16 --model flux-general-en
