# Paragraphs (Speech-to-Text v1)

Groups transcript output into paragraph blocks based on natural pauses and topic shifts in speech.

## What it does

Enables the `paragraphs` parameter which structures the transcript into logical paragraphs. Each paragraph contains one or more sentences with timing information. This is useful for creating readable documents from spoken content.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Highest-accuracy transcription model |
| `paragraphs` | `true` | Enables paragraph segmentation |
| `smart_format` | `true` | Improves formatting within paragraphs |

## Example output

```
[Paragraph 1]
Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk...

[Paragraph 2]
And there were other things happening at the same time...
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
