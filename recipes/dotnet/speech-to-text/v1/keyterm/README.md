# Key Term Prompting (Speech-to-Text v1)

Boost recognition accuracy for specific key terms and phrases using Nova-3's keyterm prompting feature.

## What it does

Keyterm prompting tells the Nova-3 model to pay special attention to specific terms, improving Keyword Recall Rate (KRR) by up to 90%. This is particularly useful for domain-specific vocabulary, proper nouns, product names, and technical jargon that may not appear frequently in general training data.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `Keyterm` | `["spacewalk", "ISS", "EVA"]` | List of key terms to boost recognition for |
| `Model` | `"nova-3"` | Required — keyterm prompting works with Nova-3 |

## Example output

```
Yeah, as much as it's worth celebrating the 50th anniversary of
the spacewalk, it's also worth noting that we've come a long way...
```

## Prerequisites

- .NET 8.0+
- Set `DEEPGRAM_API_KEY` environment variable
- Install: `dotnet restore`

## Run

```bash
dotnet run
```
