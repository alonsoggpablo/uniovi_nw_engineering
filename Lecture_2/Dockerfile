FROM python:3.11-slim

WORKDIR /app

# Install required packages
RUN pip install --no-cache-dir netaddr

# Copy the script
COPY rip.py .

# Run the script
CMD ["python3", "rip.py"]
