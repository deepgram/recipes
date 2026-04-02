#!/usr/bin/env bash
# Recipe: Speaker Diarization (STT v1)
#
# Identifies and labels individual speakers in the audio.
# The output prefixes each segment with a speaker label
# like [Speaker 0], [Speaker 1], etc.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg listen "$AUDIO_URL" --model nova-3 --diarize
