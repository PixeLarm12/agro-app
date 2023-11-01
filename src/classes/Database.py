from src.classes.Tables import *

def Cultures():
    return cultures()

def getCultureById(id):
    cultures = cultures()

    for culture in cultures:
        if int(culture["id"]) == int(id):
            return culture
    return None

def citiesByCulture(id):
    relationship = cities_cultures()
    cities = []

    for row in relationship:
        if int(row["culture_id"]) == int(id):
            cities.append(row)

    return cities

# def Culturas():
#      return {
#         "SP": [
#             {"idCultura": 41, "cultura": "Cana-de-açúcar", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 42, "cultura": "Café", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 43, "cultura": "Laranja", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 44, "cultura": "Milho", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 45, "cultura": "Soja", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 46, "cultura": "Tomate", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 47, "cultura": "Batata", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 48, "cultura": "Citros", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 49, "cultura": "Algodão", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 50, "cultura": "Feijão", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 51, "cultura": "Hortaliças", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 52, "cultura": "Flores", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 53, "cultura": "Alface", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 54, "cultura": "Maracujá", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 55, "cultura": "Morango", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 56, "cultura": "Banana", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 57, "cultura": "Abóbora", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 58, "cultura": "Mandioca", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 59, "cultura": "Uva", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 60, "cultura": "Manga", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 61, "cultura": "Goiaba", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#             {"idCultura": 62, "cultura": "Maçã", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
#         ],
#     }

# def Cidades():
#     return [
#         {"id": 1, "nome": "São Paulo", "idCultura": 51},
#         {"id": 1, "nome": "Guarulhos", "idCultura": 52},
#         {"id": 1, "nome": "Campinas", "idCultura": 42},
#         {"id": 1, "nome": "São Bernardo do Campo", "idCultura": 50},
#         {"id": 1, "nome": "Santo André", "idCultura": 53},
#         {"id": 1, "nome": "Osasco", "idCultura": 54},
#         {"id": 1, "nome": "São José dos Campos", "idCultura": 55},
#         {"id": 1, "nome": "Ribeirão Preto", "idCultura": 41},
#         {"id": 1, "nome": "Sorocaba", "idCultura": 44},
#         {"id": 1, "nome": "Santos", "idCultura": 56},
#         {"id": 1, "nome": "Mogi das Cruzes", "idCultura": 57},
#         {"id": 1, "nome": "Diadema", "idCultura": 58},
#         {"id": 1, "nome": "Jundiaí", "idCultura": 59},
#         {"id": 1, "nome": "Piracicaba", "idCultura": 41},
#         {"id": 1, "nome": "Carapicuíba", "idCultura": 60},
#         {"id": 1, "nome": "Bauru", "idCultura": 43},
#         {"id": 1, "nome": "São Vicente", "idCultura": 61},
#         {"id": 1, "nome": "Itaquaquecetuba", "idCultura": 50},
#         {"id": 1, "nome": "Franca", "idCultura": 42},
#         {"id": 1, "nome": "Pindamonhangaba", "idCultura": 62},
#     ]