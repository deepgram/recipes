# Detect Language (Speech-to-Text v1)

Automatically identifies the spoken language in audio without requiring manual specification. This is particularly useful for applications processing content in unknown or multiple languages, eliminating the need to pre-determine the language setting.

## Feature

The `DetectLanguage` parameter enables automatic language identification:
- Analyzes audio to determine the spoken language
- Returns ISO language codes (e.g., "en", "es", "fr", "de")
- Eliminates need to manually specify language parameter
- Supports all languages available in Deepgram's models

## Key Parameters

- `DetectLanguage: true` - Enables automatic language detection

## Response Structure

When `DetectLanguage=true`, the detected language is available at:
```
response.Results.Channels[0].DetectedLanguage
```

Common language codes:
- `en` - English
- `es` - Spanish  
- `fr` - French
- `de` - German
- `ja` - Japanese
- `zh` - Chinese

## Example Output

```
Detected Language: en
Transcript: Yeah, as much as it's worth, I mean, you know, from a scientific standpoint...
```

For Spanish audio:
```
Detected Language: es
Transcript: Sí, en cuanto a su valor, quiero decir, desde un punto de vista científico...
```

## Use Cases

- Processing user-uploaded content in unknown languages
- Multi-language customer support systems
- International content moderation
- Educational platforms with diverse language content

## Prerequisites

- .NET 8.0 or later
- Deepgram API key set in `DEEPGRAM_API_KEY` environment variable

## Run

```bash
dotnet run
```