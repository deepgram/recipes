# Find and Replace (Speech-to-Text v1)

Finds and replaces specific terms in the transcript output. Each replacement rule uses the format "original:replacement" to swap one term for another in the final transcript.

## What it does

The replace feature performs post-processing text substitution on the transcript. This is useful for normalizing brand names, correcting common misrecognitions, updating terminology, or censoring specific words without using the full profanity filter.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `replace` | `["mankind:humankind", "man:person"]` | List of find:replace pairs to apply to the transcript |
| `model` | `nova-3` | High-accuracy speech recognition model |

## Example output

```
Transcript (with replacements): That's one small step for person, one giant leap for humankind.
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```
