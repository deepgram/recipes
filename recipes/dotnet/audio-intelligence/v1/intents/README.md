# Intent Recognition (Audio Intelligence v1)

Detects and identifies speaker intents from conversational context, understanding what the speaker is trying to accomplish or communicate. This feature is valuable for customer service analysis, call routing, conversation insights, or understanding user goals in voice interactions.

## How it works

The intent recognition feature analyzes the conversational context and tone to identify what the speaker is trying to achieve. It goes beyond just understanding the words to comprehend the underlying purpose or goal of the communication.

## Key Parameters

- `Model = "nova-3"` — Required for intent recognition (highest accuracy model)
- `Intents = true` — Enables AI-powered intent detection
- `SmartFormat = true` — Improves intent analysis with proper text formatting

## Example Output

```
Detected Intents:
Intent: inform
  Confidence: 0.89
  Context: NASA announces a successful spacewalk mission where astronauts completed repairs

Intent: report_status
  Confidence: 0.84
  Context: The six-hour operation involved two crew members working outside the station

Intent: confirm_success
  Confidence: 0.91
  Context: The mission restored full power generation capability to the space station
```

Each detected intent includes:
- **Intent**: The identified goal or purpose (e.g., inform, request, complain, confirm)
- **Confidence**: Score from 0.0 to 1.0 indicating detection certainty
- **Context**: The relevant text segment where the intent was identified

## Common Intent Types

- **inform**: Sharing information or updates
- **request**: Asking for something or making a request
- **complain**: Expressing dissatisfaction or problems
- **confirm**: Verifying or confirming information
- **question**: Seeking information or clarification

## Prerequisites

- .NET 8.0 or later
- Deepgram API Key set as `DEEPGRAM_API_KEY` environment variable

## Run the Example

```bash
dotnet run
```