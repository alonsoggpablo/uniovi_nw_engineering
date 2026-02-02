# Lecture 2.2: Socket Communication with Docker

This folder contains Python socket implementations for TCP and UDP communication using Docker containers.

## Files

- **tcp_server_docker.py** - TCP server (listens on port 10000)
- **tcp_client_docker.py** - TCP client (connects to server)
- **udp_server_docker.py** - UDP server (listens on port 10001)
- **udp_client_docker.py** - UDP client (sends to server)
- **Dockerfile** - Docker container configuration
- **docker-compose.yml** - Multi-container orchestration
- **Python_Socket_Communication.html** - Reference article (print as PDF)

## Quick Start

### Run All Services (TCP + UDP)

```bash
docker-compose up --build
```

This will start 4 containers in the correct order:
1. TCP Server (waits for connections)
2. TCP Client (connects, sends data, receives echo)
3. UDP Server (waits for messages)
4. UDP Client (sends message, receives echo)

### Run Only TCP

```bash
docker-compose up --build tcp-server tcp-client
```

### Run Only UDP

```bash
docker-compose up --build udp-server udp-client
```

### View Individual Service Logs

```bash
docker-compose logs -f tcp-server
docker-compose logs -f tcp-client
docker-compose logs -f udp-server
docker-compose logs -f udp-client
```

## How It Works

### TCP Communication Flow

1. **Server** listens on `0.0.0.0:10000`
2. **Client** connects to `tcp-server:10000` (uses Docker DNS)
3. **Client** sends message: `"This is our message..."`
4. **Server** receives data in 16-byte chunks
5. **Server** echoes each chunk back
6. **Client** receives all chunks and verifies completion
7. Both close the connection

### UDP Communication Flow

1. **Server** listens on `0.0.0.0:10001`
2. **Client** sends message to `udp-server:10001`
3. **Server** receives the complete message at once
4. **Server** sends message back to client
5. **Client** receives and displays the echo
6. Sockets close (UDP is connectionless)

## Docker Networking

Both services use a custom bridge network (`socket-network`) for communication:
- Containers can communicate using service names as hostnames
- `tcp-server` container is accessible at hostname `tcp-server`
- `udp-server` container is accessible at hostname `udp-server`

## Container Output Examples

### TCP Server Output
```
Starting TCP server on port 10000
Waiting for a connection...
Connection from ('172.19.0.3', 43892)
Received: b'This is our mess'
Sending data back to client
Received: b'age. It is very '
Sending data back to client
...
```

### TCP Client Output
```
Connecting to tcp-server port 10000
sending b'This is our message. It is very long but will only be transmitted in chunks of 16 at a time'
received b'This is our mess'
received b'age. It is very '
...
closing socket
```

### UDP Server Output
```
Starting UDP server on port 10001
Waiting to receive message...
Received 48 bytes from ('172.19.0.4', 39451)
Data: b'This is our message. It will be sent all at once'
Sending acknowledgement back to ('172.19.0.4', 39451)
```

### UDP Client Output
```
Sending b'This is our message. It will be sent all at once' to udp-server:10001
Waiting to receive...
Received 48 bytes from ('172.19.0.2', 10001)
Data: b'This is our message. It will be sent all at once'
Closing socket
```

## TCP vs UDP Comparison

| Aspect | TCP | UDP |
|--------|-----|-----|
| **Connection** | Establishes connection | Connectionless |
| **Reliability** | Guaranteed delivery | Best effort |
| **Ordering** | In-order delivery | No ordering guarantee |
| **Speed** | Slower (connection overhead) | Faster |
| **Use Cases** | File transfer, Email, HTTP | Streaming, DNS, Gaming |
| **Data Flow** | Stream (chunked) | Datagram (whole message) |

## Stopping Services

```bash
# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v

# Stop specific service
docker-compose stop tcp-server
```

## Rebuilding Containers

```bash
# Rebuild and restart all services
docker-compose up --build

# Rebuild specific service
docker-compose up --build tcp-server
```

## Debugging

### Connect to a Running Container
```bash
docker exec -it tcp-server bash
```

### View Container Logs with Timestamps
```bash
docker-compose logs --timestamps
```

### Check Network
```bash
docker network inspect lecture_3_socket-network
```

## References

- [Python Socket Documentation](https://docs.python.org/3/library/socket.html)
- [Docker Compose Networking](https://docs.docker.com/compose/networking/)
- Medium Article: Python Socket Communication (saved as HTML)

## License

Network Engineering Course - University of Oviedo
