import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port on all interfaces
server_address = ('0.0.0.0', 10001)
print(f'Starting UDP server on port {server_address[1]}')
sock.bind(server_address)

while True:
    print('Waiting to receive message...')
    data, address = sock.recvfrom(4096)
    
    print(f'Received {len(data)} bytes from {address}')
    print(f'Data: {data!r}')
    
    if data:
        print(f'Sending acknowledgement back to {address}')
        sock.sendto(data, address)
