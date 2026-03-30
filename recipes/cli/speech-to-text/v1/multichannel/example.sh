#!/usr/bin/env bash
# Recipe: Multichannel (Speech-to-Text v1)
#
# Transcribes each audio channel independently, useful for
# stereo recordings where each speaker is on a separate channel.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg listen "$AUDIO_URL" --model nova-3 --multichannel