#!/bin/bash
#
# Scapy Interactive Shell Launcher
# Opens an interactive Python shell with Scapy in the Docker container
#

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   Scapy Interactive Shell Launcher    ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
echo ""

# Check if docker-compose is available
if ! command -v docker-compose &> /dev/null; then
    echo "Error: docker-compose is not installed"
    exit 1
fi

# Check if container is running
if ! docker-compose ps scapy &> /dev/null; then
    echo "Starting Scapy container..."
    docker-compose up -d
fi

echo -e "${GREEN}Launching Scapy shell...${NC}"
echo ""

# Launch Scapy interactive shell
docker-compose exec -it scapy scapy
