<img src="https://raw.githubusercontent.com/awtrimpe/socks-chat/master/app/static/socks.png" style="width: 100px; background: white; border-radius: 5px" />

# Socks Chat Application

## Socks

Socks is [Python](https://www.python.org/) based instant messaging application that uses [Flask](https://palletsprojects.com/p/flask/) & [SocketIO](https://socket.io/).

To run this application install the requirements in a virtual environment, run `python chat.py` and visit `http://localhost:5000` on one or more browser tabs.

    $ python chat.py

## Technologies Used

| Project      | Version | Usage                                    |
| ------------ | :-----: | ---------------------------------------- |
| Socket.IO    |  1.3.6  | Sending messages                         |
| markdown-it  | 10.0.0  | Rendering Markdown sent in messages      |
| Highlight.js | 9.15.10 | Highlighting syntax in markdown messages |

## Formatting

Please copy the file `formatting/pre-commit` to your `.git/hooks/` directory to preserve autopep8 formatting
