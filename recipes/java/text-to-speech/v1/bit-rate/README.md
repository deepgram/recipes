# Bit Rate Control

Control the output audio bit rate for compressed encodings like mp3 in Deepgram's Text-to-Speech API. Lower bit rates produce smaller files suitable for bandwidth-constrained environments, while higher bit rates improve audio quality.

## What it does

The bit rate parameter controls the compression level of the output audio when using lossy encodings like mp3. By default, Deepgram uses a standard bit rate, but you can override it to balance file size against audio quality for your specific use case — for example, using a lower bit rate for telephony or a higher one for media production.

## Key parameters

- `bit_rate`: Output bit rate in bits per second (e.g., `48000` for 48 kbps)
- `encoding`: Must be set to a compressed encoding like `"mp3"` for bit rate to apply

## Example output

```
Audio saved: output.mp3 (12345 bytes, bit rate: 48 kbps)
```

## Prerequisites

- Java 11+
- Maven 3.6+
- Deepgram API key set as `DEEPGRAM_API_KEY` environment variable

## Running the example

```bash
mvn compile exec:java -Dexec.mainClass=Example
```

## Running the test

```bash
mvn test
```
