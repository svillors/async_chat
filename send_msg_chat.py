import logging
import asyncio


logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logger = logging.getLogger(__name__)


async def log_msg(reader):
    text = await reader.readline()
    logger.debug(text.decode())


async def send_message():
    reader, writer = await asyncio.open_connection('minechat.dvmn.org', 5050)
    await log_msg(reader)
    writer.write('hash\n'.encode())
    await writer.drain()
    await log_msg(reader)
    writer.write('qweqweqweqweqwe\n\n'.encode())
    await writer.drain()
    await log_msg(reader)


if __name__ == '__main__':
    asyncio.run(send_message())
