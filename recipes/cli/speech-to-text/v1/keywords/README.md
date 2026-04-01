# Keyword Boosting (STT v1)

Boosts accuracy for specific keywords or proper nouns.

## What it does

The `keywords` parameter tells Deepgram to increase recognition accuracy for specified terms. Each keyword can include a boost intensity suffix (e.g. `:2` for strong boost). This is useful for domain-specific vocabulary, brand names, or technical terms that might otherwise be misrecognised.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Deepgram transcription model |
| `keywords` | `Deepgram:2`, `spacewalk:1.5` | Keywords with boost intensity |

## Example output

```
Yeah, as much as, it's funny when I think of anything that's related to outer space...
```

## Prerequisites

- Deepgram CLI installed (`curl -fsSL https://deepgram.com/install.sh | sh`)
- `DEEPGRAM_API_KEY` environment variable set

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
