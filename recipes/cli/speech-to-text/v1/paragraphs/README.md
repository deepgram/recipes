# Paragraphs (STT v1)

Groups transcript text into paragraph blocks based on speech pauses and topic shifts.

## What it does

Enabling the `paragraphs` parameter tells Deepgram to split the transcript into logical paragraph blocks. Each paragraph contains one or more sentences. This is useful for generating readable documents from spoken content. Since the CLI does not expose a `--paragraphs` flag directly, this example uses `dg api` to pass the parameter.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Deepgram transcription model |
| `smart_format` | `true` | Enables smart formatting |
| `paragraphs` | `true` | Groups output into paragraphs |

## Example output

```
Yeah, as much as, it's funny when I think of anything that's related to outer space, I think of is the first, the first shuttle launch.
If you think about it, it was amazing that people were able to even put a shuttle together.
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
