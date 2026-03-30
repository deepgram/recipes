# Keyword Boosting (Speech-to-Text v1)

Boosts transcription accuracy for specific keywords or proper nouns using custom weights.

## What it does

Enables the `keywords` parameter which increases recognition accuracy for specified terms. Each keyword has a weight (after the colon) that controls the boost strength — higher weights mean stronger boosting. Useful for domain-specific vocabulary, brand names, or technical terms.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Highest-accuracy transcription model |
| `keywords` | `spacewalk:2` | Boost "spacewalk" with weight 2.0 |
| `keywords` | `ISS:1.5` | Boost "ISS" with weight 1.5 |

## Example output

```
Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk...
```

## Prerequisites

- `curl` and `python3` installed
- Set `DEEPGRAM_API_KEY` environment variable

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
