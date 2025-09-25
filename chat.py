import argparse
import asyncio
import gui


async def read_msgs(host, port, queue):
    reader, writer = await asyncio.open_connection(host, port)
    try:
        while True:
            raw_line = await reader.readline()
            line = raw_line.decode().strip()
            queue.put_nowait(line)
    finally:
        writer.close()
        await writer.wait_closed()


async def main():
    parser = argparse.ArgumentParser(description='chat')
    parser.add_argument(
        '-H', '--host',
        help='ip or link to host',
        default='minechat.dvmn.org'
    )
    parser.add_argument(
        '-p', '--port',
        help='port for connnection',
        type=int,
        default=5000
    )
    parser.add_argument(
        '-t', '--token',
        help='user token',
    )
    parser.add_argument(
        '-m', '--message',
        help='message to send',
    )
    parser.add_argument(
        '-n', '--nickname',
        help='user token',
    )
    args = parser.parse_args()

    messages_queue = asyncio.Queue()
    sending_queue = asyncio.Queue()
    status_updates_queue = asyncio.Queue()

    await asyncio.gather(
        gui.draw(messages_queue, sending_queue, status_updates_queue),
        read_msgs(args.host, args.port, messages_queue)
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='chat')
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
    parser.add_argument(
        '-n', '--nickname',
        help='user token',
    )
    args = parser.parse_args()
    asyncio.run(main())
