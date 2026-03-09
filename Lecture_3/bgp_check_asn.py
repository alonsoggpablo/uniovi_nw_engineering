
import requests
import json


def get_bgp_peers(asn):
    """
    Query RIPE Stat API for BGP peers of the given ASN and print them.
    """
    url = f"https://stat.ripe.net/data/bgp-state/data.json?resource={asn}"
    resp = requests.get(url)
    if resp.status_code != 200:
        print(f"Failed to fetch data for AS{asn}")
        return
    data = resp.json()
    print("RIPE Stat API response (beautified):")
    print(json.dumps(data, indent=2, sort_keys=True))


# Example usage:
get_bgp_peers(12430)
