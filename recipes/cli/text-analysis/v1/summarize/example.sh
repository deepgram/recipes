#!/usr/bin/env bash
# Recipe: Text Summarization (Text Analysis v1)
#
# Generates a concise summary from plain text input using
# Deepgram's text intelligence API.

TEXT="Deepgram is a speech AI company that provides real-time transcription
and text intelligence APIs. Their Nova-3 model offers high accuracy for
speech-to-text. They also provide text-to-speech with natural sounding
voices and audio intelligence features like sentiment analysis and topic
detection. The platform is designed for developers building voice
applications and supports multiple programming languages through SDKs."

dg read "$TEXT" --summarize
