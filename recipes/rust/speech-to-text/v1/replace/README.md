# Find and Replace

Finds specific words or phrases in the transcript and replaces them with alternative text. This is useful for correcting brand names, standardizing terminology, or removing unwanted words from the output.

## What this feature does

The find and replace feature performs string substitution on the transcript after recognition. Each replacement rule specifies a `find` term and an optional `replace` term. If no replacement is provided, the found term is simply removed. This runs server-side, so no post-processing is needed.

## Key parameters

- **replace([Replace { find, replace }])**: List of find/replace pairs to apply to the transcript

## Sample output

With replacements "NASA" -> "Space Agency" and "mankind" -> "humankind":

```
Space Agency, that's one small step for man, one giant leap for humankind.
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable

## Run the example

```bash
cargo run
```
