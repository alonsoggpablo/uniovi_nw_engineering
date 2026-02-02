# Network Configuration for RIP Analysis
# This file contains different network scenarios for testing RIP behavior

NETWORKS = {
    "scenario_1": {
        "router_interface_network": "192.168.1.0/27",
        "candidate_network": "172.3.20.0/27",
        "description": "Class C router, Class B candidate (different classes)"
    },
    "scenario_2": {
        "router_interface_network": "192.4.10.0/26",
        "candidate_network": "172.3.20.0/27",
        "description": "Different classes and masks"
    },
    "scenario_3": {
        "router_interface_network": "192.168.1.0/24",
        "candidate_network": "192.168.1.64/26",
        "description": "Same class, same network, different masks"
    },
    "scenario_4": {
        "router_interface_network": "172.24.0.0/16",
        "candidate_network": "180.20.3.0/24",
        "description": "Different classes, different networks"
    },
    "scenario_5": {
        "router_interface_network": "192.168.0.0/24",
        "candidate_network": "192.168.0.0/24",
        "description": "Identical networks"
    },
    "scenario_6": {
        "router_interface_network": "10.0.0.0/8",
        "candidate_network": "10.1.0.0/16",
        "description": "Class A router, same class, different networks and masks"
    },
    "scenario_7": {
        "router_interface_network": "209.16.20.0/24",
        "candidate_network": "209.16.21.0/24",
        "description": "Class C networks, different subnets, same mask"
    }
}

# Default scenario
DEFAULT_SCENARIO = "scenario_1"
