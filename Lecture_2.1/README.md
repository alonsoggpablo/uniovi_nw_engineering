# Lecture 2.1: RIP Network Analysis

This folder contains a Python script that analyzes RIP (Routing Information Protocol) network announcements and CIDR class assignments.

## Files

- **rip.py** - Main script for RIP network analysis
- **networks_config.py** - Configuration file with different network scenarios
- **Dockerfile** - Docker container definition
- **docker-compose.yml** - Docker Compose configuration

## Prerequisites

- Docker and Docker Compose installed
- Linux/macOS or Windows with WSL

## Quick Start

### Run with Docker

Run with default scenario (scenario_1):

```bash
docker-compose run --rm rip python3 rip.py
```

Run with a specific scenario:

```bash
docker-compose run --rm rip python3 rip.py scenario_1
docker-compose run --rm rip python3 rip.py scenario_5
```

## Available Scenarios

All scenarios are defined in `networks_config.py`:

| Scenario | Router Network | Candidate Network | Description |
|----------|---|---|---|
| **scenario_1** | 192.168.1.0/27 | 172.3.20.0/27 | Class C router, Class B candidate (different classes) |
| **scenario_2** | 192.4.10.0/26 | 172.3.20.0/27 | Different classes and masks |
| **scenario_3** | 192.168.1.0/24 | 192.168.1.64/26 | Same class, same network, different masks |
| **scenario_4** | 172.24.0.0/16 | 180.20.3.0/24 | Different classes, different networks |
| **scenario_5** | 192.168.0.0/24 | 192.168.0.0/24 | Identical networks |
| **scenario_6** | 10.0.0.0/8 | 10.1.0.0/16 | Class A router, same class, different networks |
| **scenario_7** | 209.16.20.0/24 | 209.16.21.0/24 | Class C networks, different subnets, same mask |

## Script Overview

The `rip.py` script performs the following analysis:

1. **CIDR Class Detection** - Identifies whether networks belong to Class A, B, or C
2. **Network Comparison** - Compares router interface networks with candidate networks
3. **Mask Analysis** - Checks if networks have the same subnet masks
4. **RIP Announcement Logic** - Determines if candidate networks should be announced based on:
   - Network class matching
   - Subnet mask compatibility
   - CIDR class networks

## Configuration

Add new test scenarios to `networks_config.py` in the `NETWORKS` dictionary:

```python
NETWORKS = {
    "scenario_8": {
        "router_interface_network": "10.0.0.0/8",
        "candidate_network": "10.1.1.0/24",
        "description": "Your scenario description"
    }
}
```

## Example Output

Scenario 1 (Different classes):
```
============================================================
Scenario: scenario_1
Description: Class C router, Class B candidate (different classes)
============================================================

Router Class: Class C
Router Network: 192.168.1.0/27
Candidate Class: Class B
Candidate Network: 172.3.20.0/27

Router and Candidate are different networks
Router and Candidate belong to different Class
Announced network: 172.3.0.0/16

============================================================
```

Scenario 5 (Identical networks):
```
============================================================
Scenario: scenario_5
Description: Identical networks
============================================================

Router Class: Class C
Router Network: 192.168.0.0/24
Candidate Class: Class C
Candidate Network: 192.168.0.0/24

Same Network
Same Mask
Announced network: 192.168.0.0/24

============================================================
```

## Build Docker Image Manually

```bash
docker build -t rip-analyzer .
```

## Run Container Manually

```bash
docker run --rm -v $(pwd):/app rip-analyzer python3 rip.py scenario_1
## License

Network Engineering Course - University of Oviedo
