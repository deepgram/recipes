# Measurements

Converts spoken measurements into their standard abbreviated forms in the transcript. For example, "five kilograms" becomes "5 kg" and "ten miles per hour" becomes "10 mph".

## What this feature does

The measurements feature post-processes the transcript to detect spoken measurement values and units, then converts them into conventional abbreviations. This improves readability for transcripts containing scientific, medical, or technical content with frequent measurement references.

## Key parameters

- **measurements(true)**: Enables conversion of spoken measurements to standard abbreviations

## Sample output

```
NASA, that's one small step for man, one giant leap for mankind.
```

Note: Measurement formatting appears when the audio contains spoken measurement values.

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable

## Run the example

```bash
cargo run
```
