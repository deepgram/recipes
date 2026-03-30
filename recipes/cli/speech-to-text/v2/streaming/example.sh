#!/usr/bin/env bash
# Recipe: Live Streaming Transcription (Speech-to-Text v2)
#
# Streams audio over WebSocket using the v2 flux-general-en model
# for high-accuracy English real-time transcription.

AUDIO_URL="https://dpgr.am/spacewalk.wav"
TEMP_FILE=$(mktemp /tmp/deepgram-XXXXXX.wav)
trap "rm -f $TEMP_FILE" EXIT

curl -sL "$AUDIO_URL" -o "$TEMP_FILE"

ffmpeg -i "$TEMP_FILE" -f s16le -ar 16000 -ac 1 -loglevel quiet - \
  | dg listen --encoding linear16 --model flux-general-en