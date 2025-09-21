import asyncio
import argparse
import json

from utils import log


async def reg_user(host, port, nickname):
    reader, writer = await asyncio.open_connection(host, port)
    writer.write(b'\n')
    await writer.drain()
    writer.write(f'{nickname}\n'.encode())
    await writer.drain()
    while True:
        raw_line = await reader.readline()
        line = raw_line.decode().strip()
        if line.startswith('{') and line.endswith('}'):
            response = json.loads(line)
            break
    await log(response, './your_token.txt')
    print(response)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='async chat register')
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
        '-n', '--nickname',
        help='user token',
    )
    args = parser.parse_args()
    asyncio.run(reg_user(args.host, args.port, args.nickname))
