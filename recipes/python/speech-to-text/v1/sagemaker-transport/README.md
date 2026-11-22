# SageMaker Transport — Self-Hosted STT (Speech-to-Text v1)

Run Deepgram speech-to-text on a self-hosted AWS SageMaker endpoint using the same Python SDK interface as Deepgram Cloud. The `deepgram-sagemaker` package provides a drop-in transport layer — swap the transport factory at initialization and your application code, STT parameters, and response handling remain identical.

This pattern eliminates the rewrite cost when migrating from Deepgram Cloud to a self-hosted deployment, which is common in regulated industries (healthcare, finance, government) with data residency requirements.

## How it works

The Deepgram Python SDK accepts a `transport_factory` parameter that controls how audio is sent and results are received. By default, the SDK uses HTTPS/WebSocket to communicate with Deepgram Cloud. The `deepgram-sagemaker` package replaces this with HTTP/2 bidirectional streaming to a SageMaker endpoint — but the SDK interface (`client.listen.v1.connect(...)`) stays the same.

```python
# Cloud (default transport — no factory needed)
client = AsyncDeepgramClient()

# SageMaker (swap transport, keep everything else identical)
factory = SageMakerTransportFactory(endpoint_name="deepgram-nova-3", region="us-west-2")
client = AsyncDeepgramClient(api_key="unused", transport_factory=factory)
```

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `endpoint_name` | `"deepgram-nova-3"` | Name of the SageMaker endpoint running Deepgram |
| `region` | `"us-west-2"` | AWS region where the endpoint is deployed |
| `model` | `"nova-3"` | Deepgram model to use (same as cloud) |
| `transport_factory` | `SageMakerTransportFactory(...)` | Passed to `AsyncDeepgramClient` to route traffic to SageMaker |

## Example output

```
Yeah, as much as it's worth celebrating the 50th anniversary of
the spacewalk, it's also worth noting that we've come a long way
since then...
```

## Prerequisites

- Python 3.10+
- A deployed SageMaker endpoint running Deepgram (see [Deepgram on SageMaker docs](https://developers.deepgram.com))
- AWS credentials configured (`AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` env vars, `~/.aws/credentials`, or an IAM role)
- Set `SAGEMAKER_ENDPOINT_NAME` environment variable (defaults to `deepgram-nova-3`)
- Set `AWS_REGION` environment variable (defaults to `us-west-2`)
- Install dependencies: `pip install -r requirements.txt`

### Required AWS IAM permissions

The IAM user or role must have:

- `sagemaker:InvokeEndpoint` on the target endpoint
- `sagemaker:InvokeEndpointWithResponseStream` on the target endpoint

## Run

```bash
export SAGEMAKER_ENDPOINT_NAME=deepgram-nova-3
export AWS_REGION=us-west-2
python example.py
```

## Test

```bash
pytest example_test.py -v --timeout=120
```

## Notes

- The SageMaker transport is **async-only** — use `AsyncDeepgramClient`, not `DeepgramClient`
- `api_key="unused"` is required syntactically but not used; authentication is handled by AWS credentials
- All STT features (smart_format, diarize, paragraphs, etc.) work identically across both transports
