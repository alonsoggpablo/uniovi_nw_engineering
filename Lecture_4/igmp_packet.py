import scapy.contrib.igmp
igmpPacket = scapy.contrib.igmp.IGMP(type=23,gaddr='224.2.3.4')

#https://scapy.readthedocs.io/en/latest/api/scapy.contrib.igmp.html


igmpPacket.show()