#!/usr/bin/env python3
"""
Scapy and Network Exercises
Network Engineering Training - University of Oviedo
"""

from scapy.all import conf, get_if_addr, get_if_hwaddr
from netaddr import IPNetwork, cidr_merge


def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def exercise_1_route_lookup():
    """Exercise 1: Get the route for a specific IP."""
    print("\n1. Route for 8.8.8.8:")
    try:
        result = conf.route.route("8.8.8.8")
        print(f"   Route: {result}")
        print(f"   Interface: {result[0]}")
        print(f"   Destination: {result[1]}")
        print(f"   Gateway: {result[2]}")
    except Exception as e:
        print(f"   Error: {e}")


def exercise_2_network_config():
    """Exercise 2: Get router and local network information."""
    print("\n2. Network Configuration:")
    
    try:
        gw = conf.route.route("0.0.0.0")[2]
        print(f"   Gateway (Router IP): {gw}")
    except Exception as e:
        print(f"   Error getting gateway: {e}")

    try:
        ip = get_if_addr(conf.iface)
        print(f"   Local IP: {ip}")
    except Exception as e:
        print(f"   Error getting local IP: {e}")

    try:
        mac = get_if_hwaddr(conf.iface)
        print(f"   Local MAC: {mac}")
    except Exception as e:
        print(f"   Error getting local MAC: {e}")


def exercise_3_subnetting():
    """Exercise 3: Subnetting exercises using netaddr."""
    print("\n3. Subnetting Exercises:")

    # 3a: Merge two /25 subnets
    print("\n   a) Merge two /25 subnets (192.0.4.0/25 + 192.0.4.128/25):")
    try:
        ip1 = IPNetwork('192.0.4.0/25')
        iplist = [ip for ip in ip1]
        iplist.append(IPNetwork('192.0.4.128/25'))
        merged = cidr_merge(iplist)
        print(f"      Input subnet 1: 192.0.4.0/25 ({len(list(ip1))} hosts)")
        print(f"      Input subnet 2: 192.0.4.128/25 (128 hosts)")
        print(f"      Merged result: {list(merged)}")
    except Exception as e:
        print(f"      Error: {e}")

    # 3b: Split a large class B network in smaller /23 subnets
    print("\n   b) Split class B network (172.24.0.0/16) into /23 subnets:")
    try:
        ip = IPNetwork('172.24.0.0/16')
        subnets = list(ip.subnet(23))
        print(f"      Parent network: 172.24.0.0/16")
        print(f"      Number of /23 subnets: {len(subnets)}")
        print(f"      First 5 subnets: {subnets[:5]}")
        print(f"      Last 5 subnets: {subnets[-5:]}")
    except Exception as e:
        print(f"      Error: {e}")

    # 3c: Get supernets for an IP starting from /16
    print("\n   c) Supernets for 192.0.2.114 (starting from /16):")
    try:
        ip = IPNetwork('192.0.2.114')
        supernets = ip.supernet(16)
        print(f"      IP Address: 192.0.2.114")
        print(f"      Number of supernets: {len(supernets)}")
        print(f"      Supernets:")
        for i, supernet in enumerate(supernets, 1):
            print(f"        {i}. {supernet}")
    except Exception as e:
        print(f"      Error: {e}")


def main():
    """Run all exercises."""
    print_header("SCAPY NETWORKING EXERCISES")
    
    exercise_1_route_lookup()
    exercise_2_network_config()
    exercise_3_subnetting()
    
    print("\n" + "=" * 60)
    print("Exercises completed successfully!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
