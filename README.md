<img src="app/static/socks.png?token=AKIUJNSE5X5HTM4JM2CJV2C5V6NHA" style="width: 100px; background: white; border-radius: 5px" />

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

## Contributing

To start contributing to the project, I highly recommend using a tool like [Pipenv](https://github.com/pypa/pipenv).
All examples here will be given using Pipenv.

1. Clone the repository
2. Install necessary packages
   - `pipenv install`
3. Setup git hooks to auto-format code (consistency is king)
   - `pipenv run autohooks activate`
