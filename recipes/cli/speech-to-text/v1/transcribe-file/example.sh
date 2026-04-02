#!/usr/bin/env bash
# Recipe: Transcribe Local Audio File (STT v1)
#
# Downloads an audio file locally, then sends the local file
# to Deepgram for transcription using the CLI's file mode.

AUDIO_URL="https://dpgr.am/spacewalk.wav"
AUDIO_FILE="/tmp/spacewalk.wav"

curl -sL "$AUDIO_URL" -o "$AUDIO_FILE"

dg listen "$AUDIO_FILE" --model nova-3 --smart-format
