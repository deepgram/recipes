# Numerals

Converts spoken numbers into their numeric digit equivalents in the transcript. For example, "forty two" becomes "42" and "three hundred" becomes "300".

## What this feature does

The numerals feature transforms word-form numbers into digit form during transcription. This is particularly useful for financial data, technical specifications, addresses, and any content where numeric readability matters. Note that `smart_format` also handles numeral conversion along with other formatting — use `numerals` alone when you only need number conversion.

## Key parameters

- **numerals(true)**: Enables conversion of spoken numbers to digit form

## Sample output

```
NASA, that's 1 small step for man, 1 giant leap for mankind.
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable

## Run the example

```bash
cargo run
```
