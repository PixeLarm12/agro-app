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

def getCitiesByState():
    # The '35' param is for state = Sao Paulo
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/35/municipios"

    with requests.session() as s:
        s.mount("https://", TLSAdapter())

        return s.get(url).json()