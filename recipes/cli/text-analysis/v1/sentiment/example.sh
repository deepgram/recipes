#!/usr/bin/env bash
# Recipe: Sentiment Analysis (Text Analysis v1)
#
# Analyzes sentiment (positive, negative, or neutral) on plain text
# input using Deepgram's text intelligence API.

TEXT="The product is amazing and works perfectly. Best purchase I have made this year."

dg read "$TEXT" --sentiment
