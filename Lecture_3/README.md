# Lecture 3: BGP Exercises

## Deployment

This folder contains scripts for BGP exercises. You can deploy the environment using Docker.

### Build and Run with Docker Compose

1. Build and start the container:
   ```bash
   docker-compose up --build
   ```

2. The main service runs both `bgp.py` and `bgp_check_asn.py`.
   - Note: `bgp_check_asn.py` requires internet access to reach api.bgpview.io.

### Manual Docker Build

1. Build the image:
   ```bash
   docker build -t bgp_lecture3 .
   ```
2. Run the container:
   ```bash
   docker run --rm -it bgp_lecture3
   ```

## Files
- `bgp.py`: Main BGP script
- `bgp_check_asn.py`: ASN checking utility (requires internet access)

## Requirements
- Python 3.11
- scapy, pandas, openpyxl, requests (installed in container)
- Internet access for ASN queries

---
For more details, see the scripts and comments within each file.
