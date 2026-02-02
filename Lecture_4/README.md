# Lecture 4: Multicast Communication with Docker

This folder contains Python implementations for multicast socket communication using Docker containers.

## Files

- **multicast_sender.py** - Multicast sender (broadcasts messages to group 224.10.10.10:10000)
- **multicast_receiver.py** - Multicast receiver (listens to multicast group, sends acknowledgements)
- **socket_multicast_sender.py** - Alternative multicast sender implementation
- **socket_multicast_receiver.py** - Alternative multicast receiver implementation
- **Dockerfile** - Docker container configuration
- **docker-compose.yml** - Multi-container orchestration

## Quick Start

### Run Multicast Communication (Sender + Receiver)

```bash
docker-compose up --build
```

This will start 2 containers:
1. **Multicast Receiver** - Joins multicast group and waits for messages
2. **Multicast Sender** - Broadcasts messages to the multicast group

### Run Only Receiver

```bash
docker-compose up --build multicast-receiver
```

### Run Only Sender

```bash
docker-compose up --build multicast-sender
```

### View Individual Service Logs

```bash
docker-compose logs -f multicast-sender
docker-compose logs -f multicast-receiver
```

## How It Works

### Multicast Communication Flow

1. **Receiver** joins multicast group `224.10.10.10:10000`
2. **Sender** sends message to the multicast group
3. **Receiver** receives the message from the multicast group
4. **Receiver** sends acknowledgement back to sender
5. **Sender** receives acknowledgement
6. Process repeats

### Key Concepts

#### Multicast Group Address
- Special IPv4 addresses in range `224.0.0.0` to `239.255.255.255`
- Used for one-to-many communication
- All devices on network can listen to the same group

#### Time-To-Live (TTL)
- Controls how far multicast messages travel
- Default TTL of 1 means messages stay on local network only
- Higher values allow messages to cross routers

#### IP_ADD_MEMBERSHIP
- Socket option to join a multicast group
- Tells OS to listen for messages sent to that group address

#### IP_MULTICAST_TTL
- Socket option to set Time-To-Live value
- Packed as single byte using `struct.pack('b', ttl_value)`

## Implementation Details

### Sender Implementation

```python
import socket
import struct

message = b'very important data'
multicast_group = ('224.10.10.10', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(0.2)

# Set TTL to 1 (local network only)
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# Send to multicast group
sent = sock.sendto(message, multicast_group)

# Wait for acknowledgements
while True:
    try:
        data, server = sock.recvfrom(16)
        print(f'received {data!r} from {server}')
    except socket.timeout:
        print('timed out, no more responses')
        break
```

### Receiver Implementation

```python
import socket
import struct

multicast_group = '224.10.10.10'
server_address = ('', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

# Join multicast group
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Listen for messages
while True:
    data, address = sock.recvfrom(1024)
    print(f'received {len(data)} bytes from {address}')
    
    # Send acknowledgement back to sender
    sock.sendto(b'ack', address)
```

## Container Output Examples

### Multicast Receiver Output
```
waiting to receive message
received 19 bytes from ('172.19.0.2', 48290)
b'very important data'
sending acknowledgement to ('172.19.0.2', 48290)

waiting to receive message
```

### Multicast Sender Output
```
sending b'very important data'
waiting to receive
received b'ack' from ('172.19.0.3', 10000)
waiting to receive
received b'ack' from ('172.19.0.3', 10000)
waiting to receive
timed out, no more responses
closing socket
```

## Docker Networking

Both services use a custom bridge network (`multicast-network`) for communication:
- Containers can communicate using service names and multicast addresses
- Multicast group `224.10.10.10:10000` is accessible to both containers

## Differences Between Implementations

### multicast_sender.py / multicast_receiver.py
- Standard multicast implementation from Python documentation
- Clear separation of concerns
- Timeout-based sender waiting for responses

### socket_multicast_sender.py / socket_multicast_receiver.py
- Alternative implementations
- May have different error handling or features
- Good for comparing different approaches

## Use Cases for Multicast

- **Live Streaming** - Send video to multiple clients efficiently
- **Network Announcements** - Broadcast service discovery messages
- **Real-time Data Distribution** - Push updates to multiple subscribers
- **Gaming** - Distribute game state to multiple players
- **IoT Networks** - Sensors broadcasting measurements
- **Time Synchronization** - NTP broadcast messages

## Comparison: TCP vs UDP vs Multicast

| Feature | TCP | UDP | Multicast |
|---------|-----|-----|-----------|
| **Connection** | Required | No | No |
| **Reliability** | Guaranteed | Best effort | Best effort |
| **Ordering** | In-order | No | No |
| **Bandwidth** | Higher | Lower | Lowest |
| **Scalability** | Point-to-point | Point-to-point | One-to-many |
| **Use Case** | Reliable data | Speed | Broadcast |

## Stopping Services

```bash
# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v

# Stop specific service
docker-compose stop multicast-sender
```

## Debugging

### Connect to a Running Container
```bash
docker exec -it multicast-receiver bash
```

### View Container Logs with Timestamps
```bash
docker-compose logs --timestamps
```

### Check Network
```bash
docker network inspect lecture_4_multicast-network
```

### Test Multicast Locally
```bash
# Inside container - test if multicast is working
python3 -c "import socket; print(socket.INADDR_ANY)"
```

## References

- [Python Socket Documentation - UDP and Multicast](https://docs.python.org/3/library/socket.html)
- [Docker Compose Networking](https://docs.docker.com/compose/networking/)
- [Multicast on Wikipedia](https://en.wikipedia.org/wiki/Multicast)
- [RFC 5771 - IANA IPv4 Special-Purpose Address Registry](https://tools.ietf.org/html/rfc5771)

## License

Network Engineering Course - University of Oviedo
