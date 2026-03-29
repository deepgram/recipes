# Java: Utterances

Segments transcriptions into logical utterances with precise timing information for detailed speech analysis.

## Feature

Utterance segmentation automatically identifies natural speech breaks and pauses to create meaningful speech segments. Each utterance includes start/end timestamps, making it ideal for creating timed captions or analyzing speech patterns.

## Key Parameters

- `utterances`: Enables utterance segmentation with timing
- `smartFormat`: Recommended for proper punctuation and formatting
- `model`: Speech model to use (Nova-3 recommended for accuracy)

## Sample Output

```
Utterances with timing:
Utterance 1 (0.00s - 7.34s): Spacewalk is a daring journey that takes a lot of training and preparation.
Utterance 2 (7.34s - 15.67s): It's not just about the technical skills required, but also the mental and physical preparation that astronauts must undergo.
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