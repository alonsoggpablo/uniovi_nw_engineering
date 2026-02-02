import iperf3
import sys
import time

# Wait for server to be ready
time.sleep(2)

client = iperf3.Client()
client.server_hostname = 'iperf-server'
client.port = 6969
client.duration = 10
client.verbose = True

# Get test type from command line argument
test_type = sys.argv[1] if len(sys.argv) > 1 else 'tcp'

if test_type == 'udp':
    client.protocol = 'udp'
    # Get bandwidth limit from command line (0 for unlimited)
    bandwidth = sys.argv[2] if len(sys.argv) > 2 else '1M'
    if bandwidth == '0':
        client.bandwidth = 0  # Unlimited
    else:
        client.bandwidth = int(bandwidth.rstrip('M')) * 1000000  # Convert to bits/sec
    print(f"Running UDP test with bandwidth: {bandwidth}")
else:
    client.protocol = 'tcp'
    print("Running TCP test")

print(f"Connecting to {client.server_hostname}:{client.port}")

result = client.run()

if result:
    output = []
    output.append("\n" + "="*60)
    output.append("Test Results - All available attributes:")
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
    filename = f"/app/results/results_client_{protocol}_{test_type}.txt"
    with open(filename, 'a') as f:
        f.write("\n".join(output) + "\n")
    print(f"\nResults saved to {filename}")
else:
    print("Error: Test failed")
    if client.error:
        print(f"Error message: {client.error}")
