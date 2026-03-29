# Java: Multichannel

Processes multi-channel audio files to transcribe each channel separately, ideal for stereo recordings or multi-microphone setups.

## Feature

Multi-channel transcription processes each audio channel independently, providing separate transcriptions for left/right channels in stereo audio or individual microphone feeds. This is useful for recording setups where speakers are on different channels.

## Key Parameters

- `multichannel`: Enables separate transcription of each audio channel
- `smartFormat`: Recommended for proper punctuation and formatting
- `model`: Speech model to use (Nova-3 recommended for accuracy)

## Sample Output

```
Multi-channel transcription results:
Channel 0:
  Spacewalk is a daring journey that takes a lot of training and preparation. It's not just about the technical skills required, but also the mental and physical preparation that astronauts must undergo.

Channel 1:
  (no speech detected)

```

For true stereo recordings with different speakers on each channel:
```
Channel 0:
  Hello, this is the interviewer speaking.

Channel 1:
  Hi there, this is the guest responding.
```

## Prerequisites

1. Java 11+
2. Maven 3.6+
3. Set `DEEPGRAM_API_KEY` environment variable

## Run

```bash
mvn exec:java -Dexec.mainClass=Example
```

## Test

```bash
mvn test
```