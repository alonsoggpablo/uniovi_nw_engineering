#! /usr/bin/python

import re
import sys
import socket
import netaddr
from textwrap import wrap

def convert_multicast_ip_to_mac(ip_address):
    """Convert the Multicast IP to it's equivalent Multicast MAC.
    Source info: https://technet.microsoft.com/en-us/library/cc957928.aspx
    """
    # Convert the IP String to a bit sequence string
    try:
        ip=netaddr.IPAddress(ip_address)
        ip_bit_string = ''.join(ip.bits().split('.'))
    except:
        raise RuntimeError('Invalid IP Address to convert.')

    # The low order 23 bits of the IP multicast address are mapped directly to the low order
    # 23 bits in the MAC-layer multicast address
    lower_order_23 = ip_bit_string[-23:]

    # The high order 25 bits of the 48-bit MAC address are fixed
    high_order_25 = '0000000100000000010111100'

    mac_bit_string = high_order_25 + lower_order_23
    mac_bit_string_list = wrap(mac_bit_string, 8)
    mac_hex_string=[hex(int(x,2)) for x in mac_bit_string_list]
    mac='-'.join(mac_hex_string).upper().replace('0X','')
    mac_EUI=netaddr.EUI(mac)
    # Convert the bit string to the Typical MAC Address String


    return mac_EUI

print(convert_multicast_ip_to_mac('238.119.45.10'))
