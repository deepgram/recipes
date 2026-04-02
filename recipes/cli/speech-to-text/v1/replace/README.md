# Find and Replace (STT v1)

Finds and replaces specific terms in the transcript output.

## What it does

The `replace` parameter performs post-transcription find-and-replace on the output text. Each replacement is specified as `original:replacement`. This is useful for correcting brand name casing, normalizing terminology, or substituting domain-specific terms. Multiple replacements can be applied by repeating the parameter.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Deepgram transcription model |
| `replace` | `shuttle:Shuttle` | Replace "shuttle" with "Shuttle" (repeat for multiple) |
| `smart_format` | `true` | Enables smart formatting |

## Example output

```
Yeah, as much as, it's funny when I think of anything that's related to
outer Space, I think of is the first, the first Shuttle launch...
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
