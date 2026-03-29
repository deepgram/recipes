# CLI Samples

Code samples for the [Deepgram CLI](https://github.com/deepgram/cli) (`deepctl`).

## Structure

```
recipes/cli/{product}/v1/{recipe}/
  example.sh          # Shell script using the dg CLI command
  example_test.sh     # Test script that runs example.sh and checks output
  README.md           # Recipe explanation
```

## Requirements

- Python 3.10+
- Deepgram CLI: `pip install deepctl`
- `DEEPGRAM_API_KEY` environment variable

The CLI is also available as `dg`, `deepctl`, or `deepgram` after install.

## Run any example

```bash
export DEEPGRAM_API_KEY=your_key
cd recipes/cli/{product}/v1/{recipe}
bash example.sh
```
