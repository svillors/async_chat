import argparse
import asyncio
import json

import aiofiles

import gui


def escape(string):
    string.replace('\n', '\\n')
    return string


async def authorize(host, port, token):
    reader, writer = await asyncio.open_connection(host, port)
    await reader.readline()

    writer.write(f'{token}\n'.encode())
    await writer.drain()

    raw_text = await reader.readline()
    text = raw_text.decode()
    response = json.loads(text)

    if response is None:
        return
    return (reader, writer)


async def enter_chat(host, port, token):
    if token:
        reader, writer = await authorize(host, port, token)
        return (reader, writer)


async def send_message(host, port, token, sending_queue):
    reader, writer = await enter_chat(host, port, token)
    while True:
        message = await sending_queue.get()
        writer.write(f'{escape(message)}\n\n'.encode())
        await writer.drain()
        sending_queue.task_done()


async def load_history(path, messages_queue):
    try:
        async with aiofiles.open(path, 'r') as f:
            async for line in f:
                await messages_queue.put(line.strip())
    except FileNotFoundError:
        return


async def save_msg(path, save_queue):
    async with aiofiles.open(path, 'a') as f:
        while True:
            line = await save_queue.get()
            await f.write(line)
            await f.flush()


async def read_msgs(host, port, messages_queue, save_queue):
    reader, writer = await asyncio.open_connection(host, port)
    try:
        while True:
            raw_line = await reader.readline()
            line = raw_line.decode()
            await messages_queue.put(line.strip())
            await save_queue.put(line)
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
        '-P', '--path',
        help='path to chat history file',
        default='chat.history'
    )
    parser.add_argument(
        '-t', '--token',
        help='user token',
        default=None
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
    file_write_queue = asyncio.Queue()

    gui_task = asyncio.create_task(
        gui.draw(messages_queue, sending_queue, status_updates_queue))

    await load_history(args.path, messages_queue)

    send_task = asyncio.create_task(
        send_message(args.host, 5050, args.token, sending_queue))
    read_task = asyncio.create_task(
        read_msgs(args.host, args.port, messages_queue, file_write_queue))
    save_task = asyncio.create_task(save_msg(args.path, file_write_queue))

    await asyncio.gather(gui_task, read_task, save_task, send_task)


if __name__ == "__main__":
    asyncio.run(main())
