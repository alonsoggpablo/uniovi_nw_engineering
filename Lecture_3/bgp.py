from scapy.layers.inet import IP, TCP
from scapy.contrib.bgp import BGPHeader, BGPUpdate, BGPPathAttr, BGPNLRI_IPv4, BGPPALocalPref

src_ipv4_addr = '10.110.99.2'  # eth0
dst_ipv4_addr = '10.110.99.50'
established_port = 1223
expected_seq_num=1000 # ack
current_seq_num=1500 # seq
NLRI_PREFIX = '10.110.99.0/24'

base = IP(src=src_ipv4_addr, dst=dst_ipv4_addr, proto=6, ttl=255)  # proto=6 represents that, TCP will be travelling above this layer. This is simple IPV4 communication.
tcp = TCP(sport=established_port, dport=179, seq=current_seq_num, ack=expected_seq_num, flags='PA')  # dport=179 means, we are communicating with bgp port of the destination router/ host. sport is a random port over which tcp is established. seq and ack are the sequence number and acknowledgement numbers. flags = PA are the PUSH and ACK flags.
hdr = BGPHeader(type=2, marker=0xffffffffffffffffffffffffffffffff)  # type=2 means UPDATE packet will be the BGP Payload, marker field is for authentication. max hex int (all f) are used for no auth.
up = BGPUpdate(path_attr=[BGPPathAttr(type_flags=64, type_code=5, attribute=
BGPPALocalPref(local_pref=100))], nlri=BGPNLRI_IPv4(prefix=NLRI_PREFIX))      # update packet consist of path attributes and NLRI (Network layer reachability information),  type_code in path attributes is for which type of path attribute it is. [more][3]

packet = base / tcp / hdr / up
packet.show2()