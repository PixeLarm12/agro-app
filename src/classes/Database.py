from src.classes.Tables import *
import operator

def Cultures():
    data = cultures()
    data.sort(key=operator.itemgetter('name'))

    return data

def getCultureById(id):
    for culture in cultures():
        if int(culture["id"]) == int(id):
            return culture
    return None

def citiesByCulture(id):
    citiesIds = []
    data = []

    for row in cities_cultures():
        if int(row["culture_id"]) == int(id):
            citiesIds.append(row["city_id"])

    for city in cities():
        if int(city["id"]) in citiesIds:
            data.append(city)
            
    return data