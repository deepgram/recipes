"""
Recipe: Search (Speech-to-Text v1)
===================================
Demonstrates the `search` feature, which finds specific words or phrases
in the audio and returns their locations with confidence scores.

This is not a text search over the transcript — it searches the audio
signal itself. Results include start/end times and a confidence score
for each match.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        search="spacewalk",  # <-- THIS searches for the term in the audio.
    )

    if response.results and response.results.channels:
        transcript = response.results.channels[0].alternatives[0].transcript
        print(transcript[:200])

    # Search results are in response.results.channels[0].search
    if response.results and response.results.channels:
        search_results = getattr(response.results.channels[0], "search", None)
        if search_results:
            print("\nSearch results:")
            for result in search_results:
                query = getattr(result, "query", "")
                hits = getattr(result, "hits", [])
                print(f'  Query: "{query}" — {len(hits)} hit(s)')
                for hit in hits:
                    confidence = getattr(hit, "confidence", 0)
                    start = getattr(hit, "start", 0)
                    end = getattr(hit, "end", 0)
                    print(f"    [{start:.2f}s - {end:.2f}s] confidence: {confidence:.2f}")


if __name__ == "__main__":
    main()
