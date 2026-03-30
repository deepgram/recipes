# CLI Recipes

Code recipes for the [Deepgram CLI](https://github.com/deepgram/cli) (`dg`).

## Install

```bash
curl -fsSL https://deepgram.com/install.sh | sh
```

Also available via pip: `pip install deepctl`

The CLI installs as `dg`, `deepctl`, and `deepgram` — all the same binary.

## Structure

```
recipes/cli/{product}/{version}/{recipe}/
  example.sh          # Uses dg listen / dg speak / dg read
  example_test.sh     # Runs example.sh, asserts non-empty output
  README.md           # Recipe explanation
```

## Run any recipe

```bash
export DEEPGRAM_API_KEY=your_key
cd recipes/cli/{product}/{version}/{recipe}
bash example.sh
```
