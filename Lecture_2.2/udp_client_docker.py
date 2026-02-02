import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout to avoid waiting forever
sock.settimeout(2)

# Server address
server_address = ('udp-server', 10001)
message = b'This is our message. It will be sent all at once'

print(f'Sending {message!r} to {server_address[0]}:{server_address[1]}')
sock.sendto(message, server_address)

# Wait for response
print('Waiting to receive...')
try:
    data, address = sock.recvfrom(4096)
    print(f'Received {len(data)} bytes from {address}')
    print(f'Data: {data!r}')
except socket.timeout:
    print('Timeout waiting for response')
finally:
    print('Closing socket')
    sock.close()
