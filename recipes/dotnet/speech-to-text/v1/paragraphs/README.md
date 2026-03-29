# Paragraphs (Speech-to-Text v1)

Intelligently segments long audio transcripts into semantic paragraph blocks based on natural speech patterns and topic changes. This makes long-form content much more readable and organized.

## Feature

The `Paragraphs` parameter enables intelligent paragraph segmentation:
- Analyzes speech patterns to identify natural breaks
- Groups related sentences into paragraph units
- Provides structured paragraph data in the response
- Especially useful for interviews, lectures, and long-form content

## Key Parameters

- `Paragraphs: true` - Enables paragraph segmentation

## Response Structure

When `Paragraphs=true`, the response includes paragraph data at:
```
response.Results.Channels[0].Alternatives[0].Paragraphs.Paragraphs
```

Each paragraph contains:
- `Sentences` - Array of sentence objects with `Text` field

## Example Output

Without paragraphs:
```
One continuous block of text with all sentences together making it harder to read and understand the content structure and flow.
```

With paragraphs:
```
Paragraph 1:
First topic or section of the conversation.

Paragraph 2:
Next logical section based on topic change or natural break.
```

## Prerequisites

- .NET 8.0 or later
- Deepgram API key set in `DEEPGRAM_API_KEY` environment variable

## Run

```bash
dotnet run
```