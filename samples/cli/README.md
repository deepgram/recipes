# CLI Samples

Code samples for the [Deepgram CLI](https://github.com/deepgram/deepgram-cli).

## Structure

```
samples/cli/{product}/v1/{recipe}/
  example.sh          # Shell script using the deepgram CLI
  example_test.sh     # Test script
  README.md           # Recipe explanation
```

## Requirements

- Deepgram CLI installed: `brew install deepgram/tap/deepgram` (macOS/Linux)
- `DEEPGRAM_API_KEY` environment variable

## Run any example

```bash
cd samples/cli/{product}/v1/{recipe}
bash example.sh
```
