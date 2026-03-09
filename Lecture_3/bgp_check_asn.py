import requests
import json
import pandas as pd
import openpyxl


def get_ipv4_neighbors(asn):
    HOST = "api.bgpview.io"
    RESOURCE = "asn"
    url = 'https://{0}/{1}/{2}/peers'.format(HOST,
                                             RESOURCE,
                                             asn
                                             )
    headers = {'content-type': 'application/json'}
    neighbors_resp = requests.get(url,
                                  headers=headers,
                                  )

    ipv4_peers = json.loads(neighbors_resp.text)['data']['ipv4_peers']

    asn_peers = []
    name_peers=[]
    country_peers=[]

    for peer in ipv4_peers:
        try:
            asn_peers.append(peer['asn'])
            name_peers.append(peer['name'])
            country_peers.append(peer['country_code'])
        except:
            pass

    dict={'asn':asn_peers,'name':name_peers,'country_peers':country_peers}
    df=pd.DataFrame(dict)
    df.to_excel('asn_peers.xlsx',index=False)

    return

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

#get_ipv4_neighbors(12430)
#get_ipv4_upstreams(12430)
get_ipv4_downstreams(12430)
