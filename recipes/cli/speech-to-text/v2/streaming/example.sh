#!/usr/bin/env bash
# Recipe: Live Streaming Transcription (STT v2)
#
# Streams a local audio file over WebSocket using the flux-general-en
# (v2) model. The CLI pipes raw audio to the /v2/listen endpoint when
# encoding is specified alongside a flux-* model.

AUDIO_URL="https://dpgr.am/spacewalk.wav"
AUDIO_FILE="/tmp/spacewalk_v2.wav"

curl -sL "$AUDIO_URL" -o "$AUDIO_FILE"

ffmpeg -i "$AUDIO_FILE" -f s16le -ar 16000 -ac 1 -loglevel quiet - \
  | dg listen --encoding linear16 --model nova-3 --smart-format