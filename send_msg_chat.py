import logging
import asyncio
import json


logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logger = logging.getLogger(__name__)


async def log_msg(reader):
    raw_text = await reader.readline()
    text = raw_text.decode()
    logger.debug(text)
    return text


async def send_message():
    reader, writer = await asyncio.open_connection('minechat.dvmn.org', 5050)
    await log_msg(reader)
    writer.write('hash\n'.encode())
    await writer.drain()
    response = await log_msg(reader)
    if json.loads(response) is None:
        logger.error('Unknown token. Check it or register again.')
        return
    writer.write('qweqweqweqweqwe\n\n'.encode())
    await writer.drain()
    await log_msg(reader)


if __name__ == '__main__':
    asyncio.run(send_message())
