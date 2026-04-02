#!/usr/bin/env bash
# Recipe: Stream Audio File for Transcription (STT v1)
#
# Streams a local audio file over WebSocket for transcription.
# Unlike pre-recorded mode, this sends audio incrementally,
# demonstrating how to transcribe a file in real time.

AUDIO_URL="https://dpgr.am/spacewalk.wav"
AUDIO_FILE="/tmp/spacewalk.wav"

curl -sL "$AUDIO_URL" -o "$AUDIO_FILE"

ffmpeg -i "$AUDIO_FILE" -f s16le -ar 16000 -ac 1 -loglevel quiet - \
  | dg listen --encoding linear16 --model nova-3
