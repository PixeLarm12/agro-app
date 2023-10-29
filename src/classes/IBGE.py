from src.classes.APIService import fetchApi

def getCitiesByState():
    return fetchApi("https://servicodados.ibge.gov.br/api/v1/localidades/estados/35/municipios")