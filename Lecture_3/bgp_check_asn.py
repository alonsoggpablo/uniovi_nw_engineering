
import requests
import json


def get_bgp_peers(asn):
    """
    Query RIPE Stat API for BGP peers of the given ASN and print them.
    """
    url = f"https://stat.ripe.net/data/bgp-state/data.json?resource=AS{asn}"
    resp = requests.get(url)
    if resp.status_code != 200:
        print(f"Failed to fetch data for AS{asn}")
        return
    data = resp.json()
    peers = set()
    # The peers are in data['data']['bgp_state'][*]['peer_asn']
    for entry in data.get('data', {}).get('bgp_state', []):
        peer = entry.get('peer_asn')
        if peer:
            peers.add(peer)
    print(f"BGP peers for AS{asn}:")
    for peer in sorted(peers):
        print(peer)
    if not peers:
        print("No peers found.")

def get_ipv4_upstreams(asn):
    HOST = "api.bgpview.io"
    RESOURCE = "asn"
    url = 'https://{0}/{1}/{2}/upstreams'.format(HOST,
                                             RESOURCE,
                                             asn
                                             )
    headers = {'content-type': 'application/json'}
    neighbors_resp = requests.get(url,
                                  headers=headers,
                                  )

    ipv4_peers = json.loads(neighbors_resp.text)['data']['ipv4_upstreams']

    asn_peers = []
    name_peers=[]
    country_peers=[]

    for peer in ipv4_peers:
        try:
            asn_peers.append(peer['asn'])
            name_peers.append(peer['description'])
            country_peers.append(peer['country_code'])
        except:
            pass

    dict={'asn':asn_peers,'name':name_peers,'country_peers':country_peers}
    df=pd.DataFrame(dict)
    df.to_excel('asn_upstreams.xlsx',index=False)

    return


def get_ipv4_downstreams(asn):
    HOST = "api.bgpview.io"
    RESOURCE = "asn"
    url = 'https://{0}/{1}/{2}/downstreams'.format(HOST,
                                             RESOURCE,
                                             asn
                                             )
    headers = {'content-type': 'application/json'}
    neighbors_resp = requests.get(url,
                                  headers=headers,
                                  )

    ipv4_peers = json.loads(neighbors_resp.text)['data']['ipv4_downstreams']

    asn_peers = []
    name_peers=[]
    country_peers=[]

    for peer in ipv4_peers:
        try:
            asn_peers.append(peer['asn'])
            name_peers.append(peer['description'])
            country_peers.append(peer['country_code'])
        except:
            pass

    dict={'asn':asn_peers,'name':name_peers,'country_peers':country_peers}
    df=pd.DataFrame(dict)
    df.to_excel('asn_downstreams.xlsx',index=False)

    return


# Example usage:
get_bgp_peers(12430)
