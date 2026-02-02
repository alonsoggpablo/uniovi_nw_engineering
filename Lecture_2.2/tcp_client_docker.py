import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('tcp-server', 10000)
print(f'Connecting to {server_address[0]} port {server_address[1]}')

try:
    sock.connect(server_address)
    
    # Send data
    message = b'This is our message. It is very long but will only be transmitted in chunks of 16 at a time'
    print(f'sending {message!r}')
    sock.sendall(message)
    
    # Receive data
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print(f'received {data!r}')

finally:
    print('closing socket')
    sock.close()
