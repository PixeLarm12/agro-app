from src.classes.APIService import fetchApi
import os
from dotenv import load_dotenv

load_dotenv()

def getTypesOfCulture():
    return [
        {"id": 1,  "name": "Feijão"},
        {"id": 2,  "name": "Milho"},
        {"id": 3,  "name": "Arroz"},
        {"id": 4,  "name": "Café"},
        {"id": 5,  "name": "Laranja"},
        {"id": 6,  "name": "Limão"},
        {"id": 7,  "name": "Banana"},
        {"id": 8,  "name": "Abacaxi"},
        {"id": 9,  "name": "Mandioca"},
        {"id": 10, "name": "Batata"},
        {"id": 11, "name": "Tomate"},
        {"id": 12, "name": "Alface"},
        {"id": 13, "name": "Cenoura"},
        {"id": 14, "name": "Beterraba"},
        {"id": 15, "name": "Chuchu"},
        {"id": 16, "name": "Pimentão"},
        {"id": 17, "name": "Cebola"},
        {"id": 18, "name": "Pêssego"},
        {"id": 19, "name": "Uva"},
        {"id": 20, "name": "Maracujá"},
    ]

def getCulturesFromApi():
    headers = {
        "Authorization": "Bearer " + os.environ['AGRITEC_KEY']
    }

    response = fetchApi("https://api.cnptia.embrapa.br/agritec/v1/culturas", headers=headers, params={}, verify=True)
    return response.data
# To get all 'municipios' to filter.
# https://api.cnptia.embrapa.br/agritec/v1/municipios?uf=SP

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

def getCultivationByCultureId():
    