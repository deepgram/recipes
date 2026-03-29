# Named Entity Recognition (Audio Intelligence v1)

Automatically identifies and extracts named entities such as people, organizations, locations, dates, and other important references from the audio transcript. This feature is valuable for contact extraction, content indexing, meeting notes, or understanding key participants and places mentioned in conversations.

## How it works

The named entity recognition feature analyzes the transcript to identify and classify specific entities mentioned in the speech. It recognizes proper nouns and important references, helping you quickly identify who, what, where, and when from the audio content.

## Key Parameters

- `Model = "nova-3"` — Required for entity detection (highest accuracy model)
- `DetectEntities = true` — Enables named entity recognition
- `SmartFormat = true` — Improves entity extraction with proper text formatting

## Example Output

```
Detected Entities:
ORGANIZATION: NASA (0.95)
LOCATION: International Space Station (0.92)
PERSON: astronauts (0.87)
TIME: six-hour (0.89)
EQUIPMENT: solar panel array (0.83)
```

Each detected entity includes:
- **Label**: The entity type (PERSON, ORGANIZATION, LOCATION, DATE, etc.)
- **Value**: The actual entity text found in the transcript
- **Confidence**: Score from 0.0 to 1.0 indicating detection certainty

## Common Entity Types

- **PERSON**: Names of individuals or groups of people
- **ORGANIZATION**: Company names, institutions, agencies
- **LOCATION**: Places, addresses, geographical locations
- **DATE**: Time references, dates, durations
- **EQUIPMENT**: Tools, devices, or technical equipment
- **EVENT**: Meetings, missions, or significant occurrences

## Prerequisites

- .NET 8.0 or later
- Deepgram API Key set as `DEEPGRAM_API_KEY` environment variable

## Run the Example

```bash
dotnet run
```