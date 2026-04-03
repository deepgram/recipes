# Key Term Prompting

Boosts recognition accuracy for specific terms by providing them to the Nova-3 model as key terms. This works at a deeper model level than keyword boosting, giving the model advance knowledge of important vocabulary to watch for.

## What this feature does

Key term prompting tells the Nova-3 model which terms are important for your use case. The model uses these hints during transcription to improve recognition of domain-specific vocabulary, proper nouns, and technical terms that might otherwise be misrecognized.

## Key parameters

- **keyterms(["term1", "term2"])**: List of terms to prioritize during transcription
- Requires **Nova-3** model for best results

## Sample output

```
NASA, that's one small step for man, one giant leap for mankind.
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable

## Run the example

```bash
cargo run
```
