#!/usr/bin/env bash
# Recipe: Live Streaming Transcription (STT v1)
#
# Streams a local audio file through ffmpeg and pipes the raw
# audio to dg listen for real-time transcription over WebSocket.
# In production, replace the ffmpeg source with a microphone
# (--mic) or any audio stream.

AUDIO_URL="https://dpgr.am/spacewalk.wav"
AUDIO_FILE="/tmp/spacewalk.wav"

curl -sL "$AUDIO_URL" -o "$AUDIO_FILE"

ffmpeg -i "$AUDIO_FILE" -f s16le -ar 16000 -ac 1 -loglevel quiet - \
  | dg listen --encoding linear16 --model nova-3 --smart-format
