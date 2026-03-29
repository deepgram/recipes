# Multichannel (Speech-to-Text v1)

Processes each audio channel independently, providing separate transcripts for stereo or multi-track recordings. This is useful for recordings where different speakers are on different channels, or for analyzing left/right stereo content separately.

## Feature

The `Multichannel` parameter enables per-channel transcription:
- Processes each audio channel as a separate stream
- Returns independent transcripts for each channel
- Useful for stereo recordings with speakers on different sides
- Works with mono audio (returns single channel) and multi-channel audio

## Key Parameters

- `Multichannel: true` - Enables independent processing of audio channels

## Response Structure

When `Multichannel=true`, the response structure becomes:
```
response.Results.Channels[0].Alternatives[0].Transcript  // First channel
response.Results.Channels[1].Alternatives[0].Transcript  // Second channel (if exists)
```

## Example Output

Single-channel audio:
```
Found 1 audio channel(s):

Channel 0: Yeah, as much as it's worth, I mean, you know...
```

Stereo audio:
```
Found 2 audio channel(s):

Channel 0: Speaker on the left side discussing topic A.
Channel 1: Speaker on the right side discussing topic B.
```

## Use Cases

- Stereo interview recordings with interviewer/interviewee on separate channels
- Multi-track studio recordings
- Phone call recordings with separate channels for each party
- Podcast recordings with distinct left/right audio sources

## Prerequisites

- .NET 8.0 or later
- Deepgram API key set in `DEEPGRAM_API_KEY` environment variable

## Run

```bash
dotnet run
```