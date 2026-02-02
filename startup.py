from scapy.all import *
from netaddr import IPNetwork, cidr_merge

# Welcome message
print("=" * 60)
print("Scapy Interactive Shell")
print("=" * 60)
print("\nScapy and netaddr are already imported!")
print("\nAvailable commands:")
print("  - conf.route.route('8.8.8.8')  # Route lookup")
print("  - get_if_addr(conf.iface)      # Local IP")
print("  - get_if_hwaddr(conf.iface)    # Local MAC")
print("  - IPNetwork('192.0.4.0/25')    # Network object")
print("\nType help() for more information or exit() to quit.")
print("=" * 60 + "\n")
