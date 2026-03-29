# Paragraphs (Speech-to-Text v1)

Group transcript output into paragraph blocks based on natural pauses and topic shifts in speech.

## What it does

When `paragraphs=True`, Deepgram analyzes natural breaks in speech — pauses, topic shifts,
and sentence flow — and organizes the transcript into discrete paragraph blocks, each containing
one or more sentences with timing metadata.

This makes long-form audio content (interviews, lectures, calls) much easier to read and process.
Each sentence in a paragraph includes `start`, `end`, and `text` fields.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `paragraphs` | `True` | Enable paragraph segmentation |
| `smart_format` | `True` | Recommended alongside paragraphs for consistent output |
| `model` | `"nova-3"` | Best model for paragraph quality |

## Example output

```
[Paragraph 1]
Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk...

[Paragraph 2]
We've come a long way since then. The technology that...
```

## Without paragraphs

Without this feature, the transcript is a single continuous string with no structure.

## Prerequisites

- Python 3.10+
- Set `DEEPGRAM_API_KEY` environment variable
- Install: `pip install -r samples/python/requirements.txt`

## Run

```bash
python example.py
```

## Test

```bash
pytest example_test.py -v
```
