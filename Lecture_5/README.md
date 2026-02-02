# Lecture 5 - iperf3 Network Performance Testing

Network performance testing using iperf3 with Docker containers and packet capture.

## Quick Start

### Basic TCP Test

```bash
docker-compose up --build
```

### TCP Test with Packet Capture

```bash
# 1. Start server and capture
docker-compose --profile capture up -d --build iperf-server tcpdump-capture

# 2. Run TCP client test (10 seconds)
docker-compose up --no-deps iperf-client-tcp

# 3. Stop and finalize capture
docker-compose --profile capture down

# 4. Open capture file
# Windows: & "C:\Program Files\Wireshark\Wireshark.exe" results/iperf-traffic.pcap
# Linux/Mac: wireshark results/iperf-traffic.pcap
```

### UDP Test with Capture

```bash
# 1. Start server and capture
docker-compose --profile capture --profile udp up -d --build iperf-server tcpdump-capture

# 2. Run UDP client (unlimited bandwidth)
docker-compose --profile udp up --no-deps iperf-client-udp-unlimited

# 3. Stop and finalize
docker-compose --profile capture --profile udp down
```

## Wireshark Analysis

**Useful Filters:**
- TCP traffic: `tcp.port == 6969`
- UDP traffic: `udp.port == 6969`
- All iperf traffic: `port 6969`

**Flow visualization:** Statistics > Flow Graph

## Components

- **iperf_server.py** - Server listening on port 6969
- **iperf_client.py** - Client for TCP/UDP tests
- **tcpdump-capture** - Packet capture service (capture profile)
- **results/iperf-traffic.pcap** - Captured network traffic
