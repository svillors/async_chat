# Async chat
Async chat client with a Tkinter UI.

## Requirements
Tkinter is part of standard Python on most platforms. But if you have a problem [No module named ‘Tkinter’](https://stackoverflow.com/questions/25905540/importerror-no-module-named-tkinter)

Install python dependencies using:
```bash
pip install -r requirements.txt
```

## Usage
### Main chat
Run the chat client:
```bash
python3 chat.py \
  --host 127.0.0.1 \
  --port-read 5000 \
  --port-write 5001 \
  --token YOUR_TOKEN \
  --path chat.history
```
#### Arguments
- -H, --host — server hostname or IP
- -r, --port-read — port for the read connection
- -w, --port-write — port for the write connection
- -t, --token — user token for authorization
- -P, --path — path to history file (default: chat.history)

### Regestration window
To use main chat you should register and get your token.
After registration script will create `your_token.txt` where you can find your token.

Run regestration window:
```bash
python3 gui_reg.py \
  --host 127.0.0.1 \
  --port 5000
```
#### Arguments
- -H, --host — server hostname or IP
- -p, --port — port for connection

