# Network Engineering - University of Oviedo

Practical exercises and demonstrations for network programming, protocol analysis, and performance testing using Docker containers and Python.

## 📚 Lectures Overview

### [Lecture 1: Scapy Networking Exercises](Lecture_1/)
**Packet crafting and network analysis with Scapy**

Learn network fundamentals through hands-on exercises:
- Route lookup and routing table queries
- Network configuration (router IP, local IP, MAC addresses)
- Subnetting skills (subnet merging, network splitting, supernet calculations)

**Tech:** Scapy, Docker, Python

---

### [Lecture 2.1: RIP Network Analysis](Lecture_2.1/)
**Routing Information Protocol (RIP) analysis**

Analyze RIP network announcements and CIDR class assignments:
- Router network configuration
- Candidate network evaluation
- CIDR class validation and network comparisons
- Multiple test scenarios for different network topologies

**Tech:** Python, Docker, RIP protocol

---

### [Lecture 2.2: Socket Communication](Lecture_2.2/)
**TCP/UDP socket programming with Docker**

Implement and test network socket communication:
- TCP client-server communication (echo server on port 10000)
- UDP client-server communication (echo server on port 10001)
- Multi-container orchestration with Docker Compose
- Connection-oriented vs connectionless protocols

**Tech:** Python sockets, Docker, TCP/UDP

---

### [Lecture 4: Multicast Communication](Lecture_4/)
**IP multicast socket programming**

Explore multicast networking patterns:
- Multicast sender broadcasting to group 224.10.10.10:10000
- Multicast receiver with group subscription
- One-to-many communication patterns
- Multicast address management

**Tech:** Python multicast sockets, Docker

---

### [Lecture 5: Network Performance Testing](Lecture_5/)
**iperf3 performance measurement and packet capture**

Measure and analyze network throughput:
- TCP and UDP bandwidth testing with iperf3
- Real-time packet capture with tcpdump
- Wireshark analysis workflows
- Performance metrics (throughput, jitter, packet loss)

**Tech:** iperf3, tcpdump, Wireshark, Docker

---

## 🚀 Getting Started

### Prerequisites

- **Docker** and **Docker Compose** installed
- **Python 3.11+** (for local development)
- **Wireshark** (optional, for Lecture 5 packet analysis)

### General Workflow

Each lecture folder contains:
- `docker-compose.yml` - Container orchestration
- `Dockerfile` - Container image definition
- `README.md` - Specific instructions and usage examples
- Python scripts - Implementation code

To run any lecture:

```bash
cd Lecture_X
docker-compose up --build
```

## 📂 Repository Structure

```
uniovi_nw_engineering/
├── Lecture_1/          # Scapy packet crafting
├── Lecture_2.1/        # RIP protocol analysis
├── Lecture_2.2/        # TCP/UDP sockets
├── Lecture_4/          # Multicast communication
├── Lecture_5/          # iperf3 performance testing
└── README.md           # This file
```

## 🛠️ Technologies Used

- **Python 3.11** - Primary programming language
- **Docker** - Containerization and isolation
- **Scapy** - Packet manipulation framework
- **iperf3** - Network performance measurement
- **tcpdump/Wireshark** - Packet capture and analysis
- **Socket API** - Low-level network programming

## 📖 Learning Objectives

By completing these lectures, you will:
- Understand fundamental network protocols (TCP, UDP, RIP, Multicast)
- Master packet crafting and analysis with Scapy
- Implement client-server applications using sockets
- Analyze network performance and troubleshoot issues
- Use Docker for reproducible network environments
- Capture and analyze network traffic with Wireshark

## 🔧 Troubleshooting

### Docker Issues
```bash
# Clean up containers and networks
docker-compose down

# Rebuild from scratch
docker-compose up --build --force-recreate
```

### Network Connectivity
```bash
# Check running containers
docker-compose ps

# View container logs
docker-compose logs -f <service_name>

# Access container shell
docker exec -it <container_name> /bin/bash
```

## 📝 License

Educational material for Network Engineering course at University of Oviedo.

## 👤 Author

University of Oviedo - Network Engineering Course
