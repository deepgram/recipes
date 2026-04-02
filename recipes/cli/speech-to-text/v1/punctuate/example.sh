#!/usr/bin/env bash
# Recipe: Punctuation (STT v1)
#
# Enables automatic punctuation insertion so the raw transcript
# includes periods, commas, and question marks.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg listen "$AUDIO_URL" --model nova-3 --punctuate
