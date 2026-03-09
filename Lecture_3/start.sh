#!/bin/bash
set -e
python3 bgp.py
python3 bgp_check_asn.py
