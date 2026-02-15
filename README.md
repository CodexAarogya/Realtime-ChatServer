# Real-Time Chat Server

A lightweight WebSocket-based chat application built with Python and Redis. Messages sync instantly across multiple browser tabs and clients—no page refresh needed.


## What It Does

Opens two tabs. Type in one, see it appear in the other. That's it—simple real-time communication using WebSockets and Redis pub/sub.

The server handles bidirectional connections and broadcasts messages to all connected clients through Redis channels. Perfect for learning how WebSocket communication works or as a starting point for more complex chat features.

## Tech Stack

- **Backend**: Python (Flask/FastAPI)
- **Real-time**: WebSocket protocol
- **Message Broker**: Redis (pub/sub pattern)
- **Frontend**: HTML/CSS/JavaScript

## Quick Start

### Prerequisites

Make sure you have these installed:
- Python 3.8+
- Redis server

### Installation

Clone the repo:
```bash
git clone https://github.com/CodexAarogya/Realtime-ChatServer.git
cd Realtime-ChatServer
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Start Redis (if not already running):
```bash
redis-server
```

Run the server:
```bash
cd chatServer
python app.py
```

Open your browser and go to `http://localhost:8000/chat/`

## How It Works

1. Client opens a WebSocket connection to the server
2. Server subscribes to a Redis channel for that client
3. When a message is sent, it's published to the Redis channel
4. Redis broadcasts the message to all subscribed clients
5. Server pushes the message to connected WebSocket clients

This architecture lets you scale horizontally—multiple server instances can share the same Redis instance, and messages will still reach all clients.

## Project Structure

```
Realtime-ChatServer/
├── chatServer/
│   ├── app.py              # Main server file
│   ├── static/             # CSS, JS files
│   └── templates/          # HTML templates
├── requirements.txt
└── README.md
```

## Features

- ✅ Real-time bidirectional communication
- ✅ Multi-tab support (open multiple tabs, all stay in sync)
- ✅ Simple, clean UI
- ✅ Redis-backed message broadcasting
- ✅ Low latency message delivery

## What's Next

This is a foundation. Here's what could make it better:

- User authentication and unique usernames
- Chat rooms/channels
- Message persistence (store history in a database)
- Typing indicators
- Read receipts
- File/image sharing
- Better error handling and reconnection logic

## Deployment

Currently deployed on Vercel with Redis Cloud for the message broker. Works well for demos and small-scale usage.

For production deployments, consider:
- Setting up proper WebSocket load balancing
- Using a managed Redis service (Redis Cloud, AWS ElastiCache, etc.)
- Adding rate limiting and authentication
- Implementing proper logging and monitoring

## Known Issues

- No message persistence yet—refresh the page and history is gone
- Single chat room (no support for multiple rooms)
- Minimal error handling
- No user identity management

Feel free to open an issue if you find bugs or have feature suggestions.

## Contributing

This is a learning project, but contributions are welcome. If you want to add features or fix issues:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/something-cool`)
3. Commit your changes (`git commit -m 'Add something cool'`)
4. Push to the branch (`git push origin feature/something-cool`)
5. Open a Pull Request

## License

MIT License - feel free to use this however you want.

## Connect

Built this as a weekend project to understand WebSocket communication and Redis pub/sub patterns better. If you're building something similar or have questions, feel free to reach out.

---

⭐ Star this repo if you found it helpful!
