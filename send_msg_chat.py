import logging
import asyncio
import argparse
import json


logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logger = logging.getLogger(__name__)


def escape(string):
    string.replace('\n', '\\n')
    return string


async def log_msg(reader):
    raw_text = await reader.readline()
    text = raw_text.decode()
    logger.debug(text)
    return text


async def send_message(host, port, token, msg):
    reader, writer = await asyncio.open_connection(host, port)
    await log_msg(reader)
    writer.write(f'{token}\n'.encode())
    await writer.drain()
    response = await log_msg(reader)
    if json.loads(response) is None:
        logger.error('Unknown token. Check it or register again.')
        return
    writer.write(f'{escape(msg)}\n\n'.encode())
    await writer.drain()
    await log_msg(reader)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='async chat message sender')
    parser.add_argument(
        '-H', '--host',
        help='ip or link to host'
    )
    parser.add_argument(
        '-p', '--port',
        help='port for connnection',
        type=int
    )
    parser.add_argument(
        '-t', '--token',
        help='user token',
    )
    parser.add_argument(
        '-m', '--message',
        help='message to send',
    )
    args = parser.parse_args()
    asyncio.run(send_message(args.host, args.port, args.token, args.message))
