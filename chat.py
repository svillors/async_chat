import asyncio
import datetime

import aiofiles


async def connect_chat():
    reader, writer = await asyncio.open_connection('minechat.dvmn.org', 5000)
    async with aiofiles.open('chat_messages.txt', 'a') as f:
        await f.write(
            f'{datetime.datetime.now().strftime("[%d.%m.%y %H:%M]")}'
            + ' Connection established\n')
        while True:
            raw_line = await reader.readline()
            line = raw_line.decode()
            current_time = datetime.datetime.now().strftime('[%d.%m.%y %H:%M]')
            print(current_time, line)
            await f.write(f'{current_time} {line}')


if __name__ == '__main__':
    asyncio.run(connect_chat())
