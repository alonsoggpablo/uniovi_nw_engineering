# Dockerfile for Lecture_3
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir scapy pandas openpyxl requests
RUN chmod +x start.sh
ENTRYPOINT ["./start.sh"]
