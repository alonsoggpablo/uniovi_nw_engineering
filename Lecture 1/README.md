# Scapy Networking Exercises

This project provides a Docker-based environment for running Scapy networking exercises as part of the Network Engineering course at the University of Oviedo.

## Overview

The project includes three main exercises:
1. **Exercise 1**: Route Lookup - Query routing information for a specific IP
2. **Exercise 2**: Network Configuration - Retrieve router IP, local IP, and MAC addresses
3. **Exercise 3**: Subnetting Skills - Merge subnets, split networks, and find supernets

## Prerequisites

- Docker and Docker Compose installed on your system
- Linux/macOS or Windows with WSL

## Quick Start

### 0. Start the Docker Container

First, navigate to the `Lecture 1` directory and start the Docker containers:

```bash
cd Lecture 1
docker-compose up -d
```

Wait a moment for the container to start. You can check the status with:

```bash
docker-compose ps
```

### 1. Run the Exercises Script

Execute all exercises at once:

```bash
docker-compose exec -T scapy python3 scapy_exercises.py
```

Output will be saved to `scapy_results.txt`:

```bash
docker-compose exec -T scapy python3 scapy_exercises.py > scapy_results.txt 2>&1
```

### 2. Open Interactive Scapy Shell

Launch the Scapy interactive shell:

```bash
./scapy_shell.sh
```

This opens a full Scapy shell where you can run commands interactively:

```
>>> conf.route.route("8.8.8.8")
>>> get_if_addr(conf.iface)
>>> packet = IP(dst='8.8.8.8')/ICMP()
>>> send(packet)
```

## Files in This Project

- **docker-compose.yml** - Container configuration with Scapy and netaddr
- **scapy_exercises.py** - Main exercises script with all three exercises
- **scapy.txt** - Exercise descriptions and code snippets
- **scapy_results.txt** - Output results from running the exercises
- **scapy_shell.sh** - Script to launch interactive Scapy shell
- **README.md** - This file

## Exercise Details

### Exercise 1: Route Lookup
Query routing information for a specific IP address (8.8.8.8):

```python
conf.route.route("8.8.8.8")
```

### Exercise 2: Network Configuration
Retrieve network interface information:

- Gateway IP: `conf.route.route("0.0.0.0")[2]`
- Local IP: `get_if_addr(conf.iface)`
- Local MAC: `get_if_hwaddr(conf.iface)`
- MAC by IP: `getmacbyip("10.0.0.1")`

### Exercise 3: Subnetting Skills

**3a) Merge subnets:**
```python
from netaddr import IPNetwork, cidr_merge
ip1 = IPNetwork('192.0.4.0/25')
iplist = [ip for ip in ip1]
iplist.append(IPNetwork('192.0.4.128/25'))
cidr_merge(iplist)  # Returns [IPNetwork('192.0.4.0/24')]
```

**3b) Split networks:**
```python
ip = IPNetwork('172.24.0.0/16')
subnets = list(ip.subnet(23))  # 128 /23 subnets
```

**3c) Find supernets:**
```python
ip = IPNetwork('192.0.2.114')
supernets = ip.supernet(16)  # All supernets from /16 to /31
```

## Container Information

- **Image**: Python 3.11 slim
- **Network Mode**: Host (allows packet capture)
- **Capabilities**: NET_ADMIN, NET_RAW (required for Scapy)
- **Volumes**: Current directory mounted at `/app`

## Troubleshooting

### Service "scapy" is not running
You need to start the Docker containers first:
```bash
docker-compose up -d
```

### Container won't start
Try restarting:
```bash
docker-compose restart
```

Or view logs to diagnose:
```bash
docker-compose logs scapy
```

### Permission denied errors
Ensure you have proper permissions to run Docker. On Linux, you may need:
```bash
sudo docker-compose up -d
```

### Can't find scapy_exercises.py
Make sure you're running commands from the `Lecture 1` directory (same location as docker-compose.yml):
```bash
cd "Lecture 1"
docker-compose exec -T scapy python3 scapy_exercises.py
```

### Version warning in output
The warning about the obsolete `version` attribute is harmless and can be ignored, or remove the `version:` line from docker-compose.yml to suppress it.

## Dependencies

- Scapy 2.7.0
- netaddr
- Python 3.11

## License

Network Engineering Course - University of Oviedo

## References

- [Scapy Documentation](https://scapy.readthedocs.io/)
- [netaddr Documentation](https://netaddr.readthedocs.io/)
