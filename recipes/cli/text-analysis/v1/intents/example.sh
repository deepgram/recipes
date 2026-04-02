#!/usr/bin/env bash
# Recipe: Intent Recognition (Text Analysis v1)
#
# Detects intents from plain text input using Deepgram's text
# intelligence API via the dg read command.

TEXT="I need to cancel my subscription and get a refund for last month."

dg read "$TEXT" --intents
