import requests
import json

class pyscry:

    def __init__(self, pub, priv, acc):
        self.public_key = pub
        self.private_key = priv
        self.access_token = acc
        self.bearer_token = get_bearer_token(pub, priv, acc)
        self.version = 'v1.9.1'
        self.api_url = "http://api.tcgplayer.com/"

    def categories(self, *, offset=0, limit=10, sortOrder='categoryId', sortDesc=False):
        url = resource_builder(self.api_url, self.version, "/catalog/categories")

        headers = {"Authorization" : 'bearer ' + self.bearer_token}
        
        payload = {"offset" : offset,
        "limit" : limit,
        "sortOrder" : sortOrder,
        "sortDesc": sortDesc}

        r  = requests.get(url, headers=headers, params=payload)

        return r.text

def get_bearer_token(pub, priv, acc):
    url = "https://api.tcgplayer.com/token"
    headers = {"X-Tcg-Access-Token": acc,
               "Content-Type": "application/x-www-form-urlencoded"}

    data = {"grant_type" : "client_credentials",
            "client_id" : pub,
            "client_secret" : priv}

    r = requests.post(
        url, 
        data=data,
        headers=headers,
        verify=False)

    return json.loads(r.text)["access_token"]

def resource_builder(api, version, resource):
    return api+version+resource