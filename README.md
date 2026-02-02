# Network Engineering - University of Oviedo

Practical exercises and demonstrations for network programming, protocol analysis, and performance testing using Docker containers and Python.

## 🚀 Getting Started

### Prerequisites

#### Docker Installation

**Windows:**
```powershell
# 1. Enable WSL 2 (required for Docker Desktop)
wsl --install

# Restart your computer, then:

# 2. Install Docker Desktop
winget install Docker.DockerDesktop

# Or download Docker Desktop from:
# https://www.docker.com/products/docker-desktop/

# Note: Docker Desktop uses WSL 2 backend by default (recommended)
# Requirements: Windows 10/11 with WSL 2 enabled
```

**Mac:**
```bash
# Using Homebrew
brew install --cask docker

# Or download Docker Desktop from:
# https://www.docker.com/products/docker-desktop/
```

**Linux (Ubuntu/Debian):**
```bash
# Update package index
sudo apt-get update

# Install dependencies
sudo apt-get install ca-certificates curl gnupg lsb-release

# Add Docker's official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Set up repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Add user to docker group (optional, to run without sudo)
sudo usermod -aG docker $USER
```

#### Other Prerequisites

- **Python 3.11+** (for local development, optional)
- **Wireshark** (optional, for Lecture 5 packet analysis)
  - Windows: `winget install WiresharkFoundation.Wireshark`
  - Mac: `brew install --cask wireshark`
  - Linux: `sudo apt-get install wireshark`

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

---

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
- Wireshark analysis workflows (Windows/Mac/Linux compatible)
- Performance metrics (throughput, jitter, packet loss)

**Opening pcap files:**
- Windows: `& "C:\Program Files\Wireshark\Wireshark.exe" results/iperf-traffic.pcap`
- Mac: `open -a Wireshark results/iperf-traffic.pcap`
- Linux: `wireshark results/iperf-traffic.pcap`

**Tech:** iperf3, tcpdump, Wireshark, Docker

---

##  Repository Structure

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

Dr. Pablo Alonso García

Telecom Engineering PhD

University of Oviedo

