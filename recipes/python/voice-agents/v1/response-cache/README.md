# Voice Agent with LLM Response Cache (Voice Agents v1)

Reduce latency and LLM API costs by caching voice agent responses for repeated questions.

## What it does

Wraps a Deepgram Voice Agent session with an in-memory TTL-based cache. When a user question arrives, the cache is checked first using a normalized SHA-256 hash of the question text. On a cache hit the LLM round-trip is skipped entirely, delivering the stored response immediately. On a miss the question flows through the normal listen-think-speak pipeline, and the LLM response is stored for future reuse.

This pattern is essential for production voice agents handling FAQ-style traffic (customer service, information hotlines) where a significant percentage of questions are repeated verbatim or near-verbatim.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `TTL` | `300` (seconds) | Time-to-live for cached responses before expiry |
| `_key()` | SHA-256 of normalized text | Lowercased, whitespace-collapsed hash for cache lookup |
| `think.provider.model` | `"gpt-4o-mini"` | LLM used on cache miss |
| `listen.provider.model` | `"nova-3"` | STT model for the listen stage |
| `speak.provider.model` | `"aura-2-thalia-en"` | TTS model for agent speech |

## Example output

First run (cache miss — full LLM round-trip):
```
Connection opened
[MISS] The first all-female spacewalk symbolizes a milestone in gender equality...  (misses=1)
Cache: 1 entries, hits=0, misses=1, ttl=300s
```

Subsequent run with warm cache (cache hit — no LLM call):
```
Connection opened
[HIT] The first all-female spacewalk symbolizes a milestone in gender equality...  (hits=1)
Cache: 1 entries, hits=1, misses=0, ttl=300s
```

## Adapting for production

- **Redis/Memcached:** Replace the `CACHE` dict with a Redis client for persistence across restarts and multi-process deployments
- **Semantic matching:** Replace `_key()` with an embedding-based similarity lookup for fuzzy matching of paraphrased questions
- **Cache warm-up:** Pre-populate the cache from an FAQ list at startup
- **Metrics:** Export `stats["hits"]` and `stats["misses"]` to your observability stack

## Prerequisites

- Python 3.10+
- Set `DEEPGRAM_API_KEY` environment variable
- Install: `pip install -r recipes/python/requirements.txt`

## Run

```bash
python example.py
```

## Test

```bash
pytest example_test.py -v
```
