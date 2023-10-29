from src.classes.APIService import fetchApi
from src.classes.agritecApi import CulturasPorEstado, CulturaPorId

import os
from dotenv import load_dotenv

load_dotenv()

def getCulturesFromApi():
    headers = {
        "Authorization": "Bearer " + os.environ['AGRITEC_KEY']
    }

    return CulturasPorEstado("SP")

    # response = fetchApi("https://api.cnptia.embrapa.br/agritec/v1/culturas", headers=headers, params={}, verify=True)
    # return response.data

def getCultivationByCultureId(cultureId):
    return CulturaPorId("SP", cultureId)
    # headers = {
    #     "Authorization": "Bearer " + os.environ['AGRITEC_KEY']
    # }

    # response = fetchApi("https://api.cnptia.embrapa.br/agritec/v1/cultivares?safra=2021-2022&idCultura=60&uf=SP", headers=headers, params={}, verify=True)
    # return response.data

# return what to plant based on idCultura (culture selected)
# https://api.cnptia.embrapa.br/agritec/v1/cultivares?safra=2021-2022&idCultura=60&uf=SP
# {
#       "idCultivar": 369028,
#       "idCultura": 60,
#       "safra": "2021-2022",
#       "numeroRnc": "43926",
#       "obtentorMantenedor": "EMBRAPA SOJA",
#       "cultivar": "BRASRR13-12886",
#       "cultura": "SOJA",
#       "potencialProdutivo": 4050,
#       "duracaoCiclo": 115,
#       "uf": "SP",
#       "grupo": "I",
#       "maturacaoFisiologica": 115,
#       "floracao": 37,
#       "dataAtualizacao": "2021-04-23",
#       "regiao": "3",
#       "grupoBioClimatico": "7,4"
#     },