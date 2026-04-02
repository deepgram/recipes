#!/usr/bin/env bash
# Recipe: Smart Format (STT v1)
#
# Enables smart formatting which automatically applies punctuation,
# capitalization, number formatting, dates, and currency symbols
# to make the transcript more readable.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg listen "$AUDIO_URL" --model nova-3 --smart-format
