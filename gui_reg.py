import asyncio
import argparse
import json
import tkinter as tk
from tkinter import messagebox

import aiofiles


async def reg_user(host, port, nickname):
    try:
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
        async with aiofiles.open('./your_token.txt', 'a') as f:
            await f.write(str(response))
    except ValueError:
        messagebox.showwarning("Внимание", "Не указан хост или порт.")
    finally:
        try:
            writer.close()
            await writer.wait_closed()
        except UnboundLocalError:
            raise


def on_register(host, port, nick):
    if not nick:
        messagebox.showwarning("Внимание", "Введите ник.")
        return
    try:
        asyncio.run(reg_user(host, port, nick))
        messagebox.showinfo("Готово", "Регистрация завершена. Токен записан в файл.")
    except UnboundLocalError:
        pass


def main():
    parser = argparse.ArgumentParser(description='async chat register')
    parser.add_argument(
        '-H', '--host',
        help='ip or link to host',
    )
    parser.add_argument(
        '-p', '--port',
        help='port for connnection',
        type=int,
    )
    args = parser.parse_args()
    root = tk.Tk()
    root.title("Регистрация")

    tk.Label(root, text="Ник:").grid()
    entry = tk.Entry(root, width=30)
    entry.grid(row=0, column=1)

    button = tk.Button(root, text="Зарегистрироваться", command=lambda: on_register(
        args.host, args.port, entry.get().strip()))
    button.grid(row=1, column=0, columnspan=2, sticky="ew")

    root.bind("<Return>", lambda event: on_register(
        args.host, args.port, entry.get().strip()))

    root.mainloop()


if __name__ == "__main__":
    main()
