#!/usr/bin/env bash
# Recipe: Transcribe Local Audio File (STT v1)
#
# Downloads a sample audio file and transcribes it locally
# using the Deepgram CLI with the nova-3 model.

AUDIO_URL="https://dpgr.am/spacewalk.wav"
AUDIO_FILE="spacewalk.wav"

curl -sL "$AUDIO_URL" -o "$AUDIO_FILE"

dg listen "$AUDIO_FILE" --model nova-3 --smart-format

rm -f "$AUDIO_FILE"
