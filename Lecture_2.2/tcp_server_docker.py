import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port on all interfaces
server_address = ('0.0.0.0', 10000)
print(f'Starting TCP server on port {server_address[1]}')
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('Waiting for a connection...')
    connection, client_address = sock.accept()
    try:
        print(f'Connection from {client_address}')

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print(f'Received: {data!r}')
            if data:
                print(f'Sending data back to client')
                connection.sendall(data)
            else:
                print(f'No more data from {client_address}')
                break

    finally:
        # Clean up the connection
        print("Closing connection")
        connection.close()
