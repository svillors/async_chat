import aiofiles


async def log(line, path):
    if path is None:
        return
    async with aiofiles.open(path, 'a') as f:
        await f.write(str(line))
