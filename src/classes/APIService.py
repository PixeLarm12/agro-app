import ssl
import requests

class TLSAdapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        ctx = ssl.create_default_context()
        ctx.set_ciphers("DEFAULT@SECLEVEL=1")
        ctx.options |= 0x4
        kwargs["ssl_context"] = ctx

        return super(TLSAdapter, self).init_poolmanager(*args, **kwargs)

with requests.session() as s:
    s.mount("https://", TLSAdapter())

def fetchApi(url, headers, params, verify):
    with requests.session() as s:
        s.mount("https://", TLSAdapter())

        return s.get(url, headers=headers, params=params, verify=verify).json()