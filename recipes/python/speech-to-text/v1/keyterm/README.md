# Key Term Prompting (Speech-to-Text v1)

Boosts recognition accuracy for specific terms, brand names, or specialized vocabulary using Nova-3's prompt-based key term system. Unlike the older `keywords` feature which uses weighted biasing, key term prompting gives the model contextual hints about expected terminology.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"nova-3"` | Required — key term prompting is only compatible with Nova-3 |
| `keyterm` | `["Deepgram", "spacewalk", "ISS"]` | List of terms to boost recognition for |
| `smart_format` | `True` | Auto-format numbers, dates, and addresses |

## Example output

```
Yeah, as much as it's worth celebrating the 50th anniversary of
the spacewalk, it's also worth noting that we've come a long way
since then...
```

## Prerequisites

- Python 3.10+
- Set `DEEPGRAM_API_KEY` environment variable
- Install: `pip install -r recipes/python/requirements.txt`

## Run

```bash
python example.py
```

## Test

```bash
pytest example_test.py -v
```
