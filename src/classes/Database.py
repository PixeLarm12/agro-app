def CulturasPorEstado(uf):
    data = Culturas()

    if uf in data.keys():
        return data[uf]
    return None

def CulturaPorId(uf, id):
    data = CulturasPorEstado(uf)

    for culture in data:
        if int(culture["idCultura"]) == int(id):
            return culture
    return None

def CidadesPorCultura(cultureId):
    data = Cidades()
    cities = []

    for city in data:
        if int(city["idCultura"]) == int(cultureId):
            cities.append(city)

    return cities

def Culturas():
     return {
        "MT": [
            {"idCultura": 1, "cultura": "Soja-de-açúcar", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 2},
            {"idCultura": 2, "cultura": "Milho", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 2},
            {"idCultura": 3, "cultura": "Algodão", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 2},
            {"idCultura": 4, "cultura": "Cana-de-açúcar", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 2},
            {"idCultura": 5, "cultura": "Girassol", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 2},
            {"idCultura": 6, "cultura": "Arroz", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 2},
            {"idCultura": 7, "cultura": "Feijão", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 2},
            {"idCultura": 8, "cultura": "Sorgo", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 2},
            {"idCultura": 9, "cultura": "Trigo", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 2},
            {"idCultura": 10, "cultura": "Café", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 2},
        ],
        "BA": [
            {"idCultura": 11, "cultura": "Cacau", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 3},
            {"idCultura": 12, "cultura": "Coco-da-baía", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 3},
            {"idCultura": 13, "cultura": "Mamão", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 3},
            {"idCultura": 14, "cultura": "Banana", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 3},
            {"idCultura": 15, "cultura": "Feijão", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 3},
            {"idCultura": 16, "cultura": "Milho", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 3},
            {"idCultura": 17, "cultura": "Laranja", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 3},
            {"idCultura": 18, "cultura": "Manga", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 3},
            {"idCultura": 19, "cultura": "Abacaxi", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 3},
            {"idCultura": 20, "cultura": "Cana-de-açúcar", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 3},
        ],
        "RS": [
            {"idCultura": 21, "cultura": "Soja", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 4},
            {"idCultura": 22, "cultura": "Milho", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 4},
            {"idCultura": 23, "cultura": "Arroz", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 4},
            {"idCultura": 24, "cultura": "Trigo", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 4},
            {"idCultura": 25, "cultura": "Uva (para vinho)", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 4},
            {"idCultura": 26, "cultura": "Tabaco", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 4},
            {"idCultura": 27, "cultura": "Erva-mate", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 4},
            {"idCultura": 28, "cultura": "Maçã", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 4},
            {"idCultura": 29, "cultura": "Pêssego", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 4},
            {"idCultura": 30, "cultura": "Citrus (laranja, bergamota, etc.)", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 4},
        ],
        "MG": [
            {"idCultura": 31, "cultura": "Café", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 5},
            {"idCultura": 32, "cultura": "Cana-de-açúcar", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 5},
            {"idCultura": 33, "cultura": "Milho", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 5},
            {"idCultura": 34, "cultura": "Feijão", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 5},
            {"idCultura": 35, "cultura": "Tomate", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 5},
            {"idCultura": 36, "cultura": "Laranja", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 5},
            {"idCultura": 37, "cultura": "Limão", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 5},
            {"idCultura": 38, "cultura": "Abacate", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 5},
            {"idCultura": 39, "cultura": "Banana", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 5},
            {"idCultura": 40, "cultura": "Mandioca", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 5},
        ],
        "SP": [
            {"idCultura": 41, "cultura": "Cana-de-açúcar", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 42, "cultura": "Café", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 43, "cultura": "Laranja", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 44, "cultura": "Milho", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 45, "cultura": "Soja", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 46, "cultura": "Tomate", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 47, "cultura": "Batata", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 48, "cultura": "Citros", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 49, "cultura": "Algodão", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 50, "cultura": "Feijão", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 51, "cultura": "Hortaliças", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 52, "cultura": "Flores", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 53, "cultura": "Alface", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 54, "cultura": "Maracujá", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 55, "cultura": "Morango", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 56, "cultura": "Banana", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 57, "cultura": "Abóbora", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 58, "cultura": "Mandioca", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 59, "cultura": "Uva", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 60, "cultura": "Manga", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 61, "cultura": "Goiaba", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
            {"idCultura": 62, "cultura": "Maçã", "safra": "2022-2023", "inicioPlantio": "setembro", "ciclo": "90", "regiao": 1},
        ],
    }

def Regioes():
    return [
        {"id": 1, "regiao": "Mata Atlantica"},
        {"id": 2, "regiao": "Pantanal"},
        {"id": 3, "regiao": "Caatinga"},
        {"id": 4, "regiao": "Pampas"},
        {"id": 5, "regiao": "Cerrado"},
    ]

def Cidades():
    return [
        {"id": 1, "nome": "São Paulo", "idCultura": 51},
        {"id": 1, "nome": "Guarulhos", "idCultura": 52},
        {"id": 1, "nome": "Campinas", "idCultura": 42},
        {"id": 1, "nome": "São Bernardo do Campo", "idCultura": 50},
        {"id": 1, "nome": "Santo André", "idCultura": 53},
        {"id": 1, "nome": "Osasco", "idCultura": 54},
        {"id": 1, "nome": "São José dos Campos", "idCultura": 55},
        {"id": 1, "nome": "Ribeirão Preto", "idCultura": 41},
        {"id": 1, "nome": "Sorocaba", "idCultura": 44},
        {"id": 1, "nome": "Santos", "idCultura": 56},
        {"id": 1, "nome": "Mogi das Cruzes", "idCultura": 57},
        {"id": 1, "nome": "Diadema", "idCultura": 58},
        {"id": 1, "nome": "Jundiaí", "idCultura": 59},
        {"id": 1, "nome": "Piracicaba", "idCultura": 41},
        {"id": 1, "nome": "Carapicuíba", "idCultura": 60},
        {"id": 1, "nome": "Bauru", "idCultura": 43},
        {"id": 1, "nome": "São Vicente", "idCultura": 61},
        {"id": 1, "nome": "Itaquaquecetuba", "idCultura": 50},
        {"id": 1, "nome": "Franca", "idCultura": 42},
        {"id": 1, "nome": "Pindamonhangaba", "idCultura": 62},
    ]