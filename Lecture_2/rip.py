from netaddr import IPNetwork, IPAddress
import sys
from networks_config import NETWORKS, DEFAULT_SCENARIO

# Get scenario from command line argument or use default
scenario = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SCENARIO

if scenario not in NETWORKS:
    print(f"Error: Scenario '{scenario}' not found")
    print(f"Available scenarios: {', '.join(NETWORKS.keys())}")
    sys.exit(1)

config = NETWORKS[scenario]
router_interface_network = IPNetwork(config["router_interface_network"])
candidate_network = IPNetwork(config["candidate_network"])

print(f"\n{'='*60}")
print(f"Scenario: {scenario}")
print(f"Description: {config['description']}")
print(f"{'='*60}\n")

def cidr_class(network):
    class_A_networks= IPNetwork('0.0.0.0/1')
    class_B_networks = IPNetwork('128.0.0.0/2')
    class_C_networks = IPNetwork('192.168.0.0/3')

    if network in class_A_networks:
        return('Class A',8)
    if network in class_B_networks:
        return ('Class B',16)
    if network in class_C_networks:
        return ('Class C',24)
    else:
        return ('-')

router_class=cidr_class((router_interface_network))[0]
candidate_class=cidr_class(candidate_network)[0]

router_base_mask=cidr_class((router_interface_network))[1]
candidate_base_mask=cidr_class(candidate_network)[1]

try:
    router_cidr_class_network=router_interface_network.supernet(router_base_mask)[0]
except:
    router_cidr_class_network = router_interface_network

try:
    candidate_cidr_class_network=candidate_network.supernet(candidate_base_mask)[0]
except:
    candidate_cidr_class_network = candidate_network


print ('Router Class: ' + router_class)
print ('Router Network: ' + str(router_interface_network))

print ('Candidate Class: ' + candidate_class)
print ('Candidate Network: ' + str(candidate_network))

print()



#Check if candidate network and router network are the same



if candidate_cidr_class_network==router_cidr_class_network:
    same_network=True
else:
    same_network=False

#Check if candidate and router networks belong to the same class

if candidate_class==router_class:
    same_class=True
else:
    same_class=False

#Check if candidate and router networks have the same mask

if candidate_network.prefixlen==router_interface_network.prefixlen:
    same_mask=True
else:
    same_mask=False

#Decide wether router announces candidate network

if same_network:
    print ('Same Network')
    if same_mask:
        print ('Same Mask')
        announce=True
        announced_network=candidate_network
    if same_mask==False:
        print ('Different Mask')
        announce=False
else:
    print ('Router and Candidate are different networks')
    if router_class!=candidate_class:  #Different networks and different class
        print ('Router and Candidate belong to different Class')
        announce=True
        try:
            announced_network = candidate_network.supernet(candidate_base_mask)[0]
        except:
            announced_network = candidate_network
    else: #Different networks and same class
        print ('Router and Candidate belong to the same Class')
        if router_interface_network.prefixlen==candidate_network.prefixlen: #Diff nw, same class, same mask
            print('Router and Candidate have the same mask')
            announce=True
            announced_network=candidate_network
        else: #Diff nw, same class, diff mask
            print('Router and Candidate have different masks')
            announce=True
            if candidate_network.prefixlen == candidate_base_mask:
                announced_network = candidate_network
            else:
                announced_network = candidate_network.supernet(candidate_base_mask)[0]
if announce:
    print('Announced network: ' + str(announced_network))
else:
    print ('Network not announced')

print(f"\n{'='*60}\n")


