# Secure Temporary Key for Voice Agent (Voice Agents v1)

Use short-lived JWTs instead of your API key when connecting to a voice agent from the browser.

## What it does

Deepgram's `auth.v1.tokens.grant()` endpoint creates a temporary JSON Web Token (JWT) with `usage::write` scope — enough to open a Voice Agent WebSocket, but not to access the Manage API. The token has a configurable time-to-live (default 30 seconds, this recipe uses 60 seconds).

In production you expose a lightweight `/token` endpoint on your backend that calls `grant()` and returns the JWT. The browser client creates a `DeepgramClient({ accessToken })` and connects directly to `wss://agent.deepgram.com` — the main API key never leaves your server.

This recipe demonstrates the full pattern in a single file: mint a token, create a second client with it, and run a voice agent session end-to-end.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `ttl_seconds` | `60` | Token lifetime in seconds (default 30) |
| `accessToken` | JWT string | Pass to `DeepgramClient` instead of an API key |
| `listen.provider` | `deepgram/nova-3` | Speech recognition model |
| `think.provider` | `open_ai/gpt-4o-mini` | LLM for conversation logic |
| `speak.provider` | `deepgram/aura-2-thalia-en` | TTS voice model |

## Example output

```
Temporary token granted (expires in 60s)
Settings applied
Agent: Hello! How can I help you today?
```

## Prerequisites

- Node.js 20+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `npm install`

## Run

```bash
node example.js
```
