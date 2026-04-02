#!/usr/bin/env bash
# Recipe: Redaction (STT v1)
#
# Redacts sensitive information such as PCI data (credit card numbers)
# and SSNs from the transcript. Uses dg api since the CLI does not
# expose --redact directly.

AUDIO_URL="https://dpgr.am/spacewalk.wav"

dg api -X POST \
  "/v1/listen?model=nova-3&redact=pci&redact=ssn" \
  -H "Content-Type: application/json" \
  --input <(printf '{"url":"%s"}' "$AUDIO_URL") \
  --jq '.results.channels[0].alternatives[0].transcript'
