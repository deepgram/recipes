# WebSocket Streaming

Real-time, low-latency text-to-speech streaming using WebSocket connections for optimal performance.

## How it works

This recipe demonstrates WebSocket-based streaming TTS, which provides the lowest latency for real-time applications. The WebSocket connection allows for bidirectional communication, enabling immediate audio chunk delivery as text is processed. This approach is ideal for interactive applications, live streaming, or any scenario where minimal delay is crucial.

## Key parameters

- **Encoding**: `linear16` - Uncompressed PCM for fastest processing
- **SampleRate**: `48000` - High-quality audio sampling rate
- **WebSocket Events**: Real-time audio chunk delivery
- **Streaming**: Text sent incrementally, audio received as chunks

## What you'll see

The example will establish a WebSocket connection and display:

```
Connecting to WebSocket...
WebSocket connection opened
Sending text: This is a WebSocket streaming text-to-speech example for low-latency audio generation.
Received audio chunk: 1024 bytes
Received audio chunk: 1024 bytes
Received audio chunk: 512 bytes
Total audio bytes received: 2560
WebSocket streaming completed successfully!
WebSocket connection closed
```

## Prerequisites

- .NET 8.0 or later
- `DEEPGRAM_API_KEY` environment variable set

## Run the example

```bash
dotnet run
```

The example collects audio chunks in real-time and reports the total bytes received, demonstrating the streaming capabilities of the WebSocket API.