import iperf3

server = iperf3.Server()
server.bind_address = '0.0.0.0'  # Listen on all interfaces for Docker
server.port = 6969
server.protocol = 'tcp'
server.verbose = True

print(f"iperf3 server listening on {server.bind_address}:{server.port}")
print(f"Protocol: {server.protocol}")

while True:
    result = server.run()
    if result:
        output = []
        output.append("\n" + "="*60)
        output.append("Test completed - All available attributes:")
        output.append("="*60)
        
        # Print all non-private attributes
        for attr in dir(result):
            if not attr.startswith('_'):
                try:
                    value = getattr(result, attr)
                    if not callable(value):
                        line = f"  {attr}: {value}"
                        output.append(line)
                except Exception as e:
                    pass
        output.append("="*60 + "\n")
        
        # Print to console
        for line in output:
            print(line)
        
        # Write to file
        protocol = getattr(result, 'protocol', 'unknown')
        filename = f"/app/results/results_server_{protocol}.txt"
        with open(filename, 'a') as f:
            f.write("\n".join(output) + "\n")
        print(f"Results appended to {filename}")
