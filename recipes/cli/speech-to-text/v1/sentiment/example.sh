#!/usr/bin/env bash
# Recipe: Sentiment Analysis (STT v1)
#
# Analyses sentiment (positive/negative/neutral) per segment.
# Uses the --sentiment flag on dg listen.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg listen "$AUDIO_URL" --model nova-3 --sentiment
