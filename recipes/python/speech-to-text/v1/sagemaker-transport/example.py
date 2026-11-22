"""
Recipe: SageMaker Transport — Self-Hosted STT (Speech-to-Text v1)
Stream audio to a self-hosted Deepgram on AWS SageMaker.
Same SDK interface as cloud — only the transport layer changes.
"""

import asyncio
import os
import urllib.request

from deepgram import AsyncDeepgramClient
from deepgram.core.events import EventType
from deepgram.listen.v1.types import ListenV1Results
from deepgram_sagemaker import SageMakerTransportFactory

AUDIO_URL = "https://dpgr.am/spacewalk.wav"

factory = SageMakerTransportFactory(
    endpoint_name=os.environ.get("SAGEMAKER_ENDPOINT_NAME", "deepgram-nova-3"),
    region=os.environ.get("AWS_REGION", "us-west-2"),
)

client = AsyncDeepgramClient(api_key="unused", transport_factory=factory)


async def main():
    audio_data = urllib.request.urlopen(AUDIO_URL).read()

    async with client.listen.v1.connect(model="nova-3") as conn:
        def on_message(msg):
            if isinstance(msg, ListenV1Results):
                text = msg.channel.alternatives[0].transcript
                if text:
                    print(text)

        conn.on(EventType.MESSAGE, on_message)
        task = asyncio.create_task(conn.start_listening())
        await asyncio.sleep(1)

        for i in range(0, len(audio_data), 8000):
            await conn.send_media(audio_data[i : i + 8000])
            await asyncio.sleep(0.1)

        await conn.send_finalize()
        await asyncio.sleep(3)
        task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
