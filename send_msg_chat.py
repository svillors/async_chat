import asyncio


async def send_message():
    reader, writer = await asyncio.open_connection('minechat.dvmn.org', 5050)
    writer.write('hash\n'.encode())
    await writer.drain()
    writer.write('qweqweqweqweqwe\n\n'.encode())
    await writer.drain()


if __name__ == '__main__':
    asyncio.run(send_message())
