from src.classes.ComercialData import *
import operator

def getAllCultures():
    return allCultures()

def getCulturesAlphaOrdered():
    data = getAllCultures()
    data.sort(key=operator.itemgetter('name'))

    return data

def getCultureById(id):
    if(id): 
        for culture in getAllCultures():
            if int(culture["id"]) == int(id):
                return culture
    else:
        return None

def getCulturesIdsByPeriod(period):
    data = []

    if(period): 
        for culture in getAllCultures():
            if culture["period"].find(period) != -1:
                data.append(culture["id"])
    
    return data

def getCulturesByIdsAndCity(cultureIds, cityId):
    data = []

    if(len(cultureIds) > 0):
        for el in getCitiesCulturesRelation():
            if (el['culture_id'] in cultureIds and el['city_id'] == cityId):
                data.append(getCultureById(el["culture_id"]))

    return data

def getAllCities():
    return allCities()

def getCitiesCulturesRelation():
    return relationCitiesCultures()

def getCityById(id):
    for city in getAllCities():
        if int(city["id"]) == int(id):
            return city
    return None

def citiesByCulture(id):
    citiesIds = []
    data = []

    for row in getCitiesCulturesRelation():
        if int(row["culture_id"]) == int(id):
            citiesIds.append(row["city_id"])

    for city in getAllCities():
        if int(city["id"]) in citiesIds:
            data.append(city)
            
    return data

def getCulturesByCity(cityId):
    data = []

    if(cityId): 
        for el in getCitiesCulturesRelation():
            if int(el["city_id"]) == int(cityId):
                culture = getCultureById(el["culture_id"])
                if(culture): 
                    data.append(culture)

        return data
    else:
        return None