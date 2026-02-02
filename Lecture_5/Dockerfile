FROM python:3.11-slim

# Install iperf3 and tcpdump for network capture
RUN apt-get update && \
    apt-get install -y iperf3 net-tools tcpdump && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python iperf3 library
RUN pip install --no-cache-dir iperf3

# Set working directory
WORKDIR /app

# Copy scripts
COPY iperf_server.py .
COPY iperf_client.py .

# Default command (can be overridden in docker-compose)
CMD ["python", "iperf_server.py"]
