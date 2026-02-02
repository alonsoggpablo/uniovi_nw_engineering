# Lecture 5 - iperf3 Network Performance Testing

This setup demonstrates network performance testing using iperf3 with Docker containers.

## Components

- **iperf_server.py**: Python-based iperf3 server listening on port 6969
- **iperf_client.py**: Python-based iperf3 client for running TCP/UDP tests
- **Dockerfile**: Container image with iperf3 and Python bindings
- **docker-compose.yml**: Orchestration for server and client containers

## Usage

### Run TCP Test (Default)

```bash
docker-compose up --build
```

This will:
1. Start the iperf3 server
2. Run a TCP client test (10 seconds)
3. Display results

### Run UDP Test (Limited to 1 Mbps)

```bash
docker-compose --profile udp up iperf-server iperf-client-udp-limited
```

### Run UDP Test (Unlimited Bandwidth)

```bash
docker-compose --profile udp up iperf-server iperf-client-udp-unlimited
```

### Check Server Port (from within container)

```bash
docker exec -it iperf-server netstat -an | grep 6969
```

### Manual iperf3 Commands

You can also use the native iperf3 CLI from within containers:

```bash
# TCP test
docker exec -it iperf-client-tcp iperf3 -c iperf-server -p 6969

# UDP test (1 Mbps limit)
docker exec -it iperf-client-tcp iperf3 -c iperf-server -p 6969 -u

# UDP test (unlimited)
docker exec -it iperf-client-tcp iperf3 -c iperf-server -p 6969 -u -b 0
```

## Test Results

The tests will show:
- **TCP**: Throughput, sent/received bytes, duration
- **UDP**: Throughput, jitter, packet loss, sent/received bytes

## Network Configuration

- Network: Custom bridge network (`iperf-network`)
- Server port: 6969
- Protocol: TCP or UDP (configurable)

## Wireshark Capture

Use the built-in tcpdump-capture service with compose profiles to capture network traffic:

### TCP Test with Capture

```bash
# Start capture service + server
docker-compose --profile capture up -d iperf-server tcpdump-capture

# Run TCP test in another terminal
docker-compose up --build iperf-client-tcp

# View captured traffic when complete
wireshark Lecture_5/results/iperf-traffic.pcap
```

### UDP Test with Capture

```bash
docker-compose --profile capture --profile udp up -d iperf-server tcpdump-capture
docker-compose --profile udp up iperf-client-udp-unlimited
wireshark Lecture_5/results/iperf-traffic.pcap
```

### Wireshark Filters

- **TCP traffic:** `tcp.port == 6969`
- **UDP traffic:** `udp.port == 6969`
- **All iperf traffic:** `port 6969`
- **Show packet flow:** `Statistics > Flow Graph`
