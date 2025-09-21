import argparse
import asyncio
import datetime

from utils import log


async def connect_chat(host, port, path):
    reader, writer = await asyncio.open_connection(host, port)
    current_time = datetime.datetime.now().strftime("[%d.%m.%y %H:%M]")
    await log(f'{current_time} Connection established\n', path)
    while True:
        raw_line = await reader.readline()
        current_time = datetime.datetime.now().strftime('[%d.%m.%y %H:%M]')
        line = f'{current_time} {raw_line.decode()}'
        print(current_time, line)
        await log(line, path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='async chat connection')
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
        '-l', '--log_path',
        help='path to file for saving history',
        default=None
    )
    args = parser.parse_args()
    asyncio.run(connect_chat(args.host, args.port, args.log_path))
