<img src="app/static/socks.png" width="100" style="background: white; border-radius: 5px"/>

[![Coverage Status](https://coveralls.io/repos/github/awtrimpe/socks-chat/badge.svg?branch=master)](https://coveralls.io/github/awtrimpe/socks-chat?branch=master)

# Socks Chat Application

## Socks

Socks is [Python](https://www.python.org/) based instant messaging application that
uses [Flask](https://palletsprojects.com/p/flask/) & [SocketIO](https://socket.io/).

To run this application install the requirements in a virtual environment, run `python chat.py`
and visit `http://localhost:5000` on one or more browser tabs.

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

## Formatting

#### Autohooks

To ensure a consistent format for all systems, [Autohooks](https://pypi.org/project/autohooks/)
has been used. In order to automatically install the necessary git pre-commit hook,
simply run the command:

    $ pipenv run autohooks activate

#### Manual autopep8

If Autohooks does not work for you (it may not work on all operating systems yet),
please copy the file `formatting/pre-commit` to your `.git/hooks/` directory to preserve
autopep8 formatting.

_\*\*Note: You must have autopep8 installed globally for Python 3.6_
