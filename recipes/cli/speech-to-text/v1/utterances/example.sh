#!/usr/bin/env bash
# Recipe: Utterances (Speech-to-Text v1)
#
# Splits the transcript into per-utterance segments with start/end
# timestamps, useful for subtitle generation and speaker analysis.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg listen "$AUDIO_URL" --model nova-3 --utterances