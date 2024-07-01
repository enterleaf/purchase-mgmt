import asyncio
import uuid
import logging
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


async def publisher(message_type, message_content):
    # Connect to NATS server
    nc = NATS()
    await nc.connect(servers=["nats://localhost:4222"])

    # Generate a unique ID for the message
    message_id = str(uuid.uuid4())
    message = f"ID: {message_id}, Type: {message_type}, Message: {message_content}"

    try:
        await nc.publish(message_type, message.encode())
        logger.info(f"Published message with ID: {message_id}")
    except (ErrConnectionClosed, ErrTimeout) as e:
        logger.error(f"Failed to publish message: {e}")

    # Close connection
    await nc.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(publisher())
    loop.close()
