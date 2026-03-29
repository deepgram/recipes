# Diarize (Speech-to-Text v1)

Identifies and labels different speakers in multi-speaker audio recordings. Speaker diarization assigns a unique speaker ID to each person speaking, making it easy to distinguish who said what in conversations, interviews, or meetings.

## Feature

The `Diarize` parameter enables speaker identification:
- Automatically detects different speakers in the audio
- Assigns unique integer IDs to each speaker (0, 1, 2, etc.)
- Labels each word or utterance with the corresponding speaker
- Works with both single-speaker audio (all speaker 0) and multi-speaker content

## Key Parameters

- `Diarize: true` - Enables speaker diarization
- `Utterances: true` - Recommended combination for speaker-labeled segments

## Response Structure

When combined with `Utterances=true`, each utterance includes:
- `Speaker` - Integer ID of the speaker (0, 1, 2, etc.)
- `Transcript` - What that speaker said
- `Start` and `End` - Timing information

## Example Output

Without diarization:
```
Hello there, how are you doing today? I'm doing well, thanks for asking.
```

With diarization:
```
Speaker 0: Hello there, how are you doing today?
Speaker 1: I'm doing well, thanks for asking.
```

## Prerequisites

- .NET 8.0 or later
- Deepgram API key set in `DEEPGRAM_API_KEY` environment variable

## Run

```bash
dotnet run
```