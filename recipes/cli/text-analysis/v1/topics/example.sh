#!/usr/bin/env bash
# Recipe: Topic Detection (Text Analysis v1)
#
# Identifies topics discussed in plain text input using
# Deepgram's text intelligence API.

TEXT="The new electric vehicle models are expected to reduce carbon emissions
significantly. Battery technology has improved with solid-state designs
offering longer range and faster charging times. Government incentives
continue to drive adoption across North America and Europe."

dg read "$TEXT" --topics
