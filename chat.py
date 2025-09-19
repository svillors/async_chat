import asyncio


async def connect_chat():
    reader, writer = await asyncio.open_connection('minechat.dvmn.org', 5000)
    while True:
        line = await reader.readline()
        print(line.decode())


if __name__ == '__main__':
    asyncio.run(connect_chat())
