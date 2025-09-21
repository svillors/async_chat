# Async chat
Several scripts for interacting with the chat

## Requirements
Install python dependencies using:
```bash
pip install -r requirements.txt
```

## Usage
There are 3 main scripts:

- `read_chat.py` - stream chat to terminal and also can write can write chat history to file
    ```bash
    python3 read_chat.py -h   
    usage: read_chat.py [-h] [-H HOST] [-p PORT] [-l LOG_PATH]
    ```
  - `-H`, `--host` - Ip or link to host
  - `-p`, `--port` - Port for connection
  - `-l`, `--log_path` - Path to file for saving chat history

- `reg_new_user.py` - register new user to a chat
    ```bash
    python3 reg_new_user.py -h
    usage: reg_new_user.py [-h] [-H HOST] [-p PORT] [-n NICKNAME]
    ```
  - `-H`, `--host` - Ip or link to host
  - `-p`, `--port` - Port for connection
  - `-n`, `--nickname` - Nickname for new user

- `send_msg_chat.py` - sends message to chat
    ```bash
    python3 send_msg_chat.py -h
    usage: send_msg_chat.py [-h] [-H HOST] [-p PORT] [-t TOKEN] [-m MESSAGE]
    ```
  - `-H`, `--host` - Ip or link to host
  - `-p`, `--port` - Port for connection
  - `-t`, `--token` - Users token (to get it use `reg_new_user.py`)
  - `-m`, `--message` - Your message to send

