from src.classes.Tables import *
import operator

def Cultures():
    data = cultures()
    data.sort(key=operator.itemgetter('name'))

    return data

def getCityById(id):
    for city in cities():
        if int(city["id"]) == int(id):
            return city
    return None

def getCultureById(id):
    if(id): 
        for culture in cultures():
            if int(culture["id"]) == int(id):
                return culture
    else:
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

def filterCities(cultureId, period):
    data = [] 

    if(cultureId): 
        for row in cities_cultures():
            if (int(row["culture_id"]) == int(cultureId) and row["period"].find(period) != -1):
                city = getCityById(row["city_id"])
                data.append({"id": city["id"], "slug": city["slug"], "name": city["name"], "state": city["state"], "code": city["code"], "period": row["period"]})
    else:
        for row in cities_cultures():
            if (row["period"].find(period) != -1):
                city = getCityById(row["city_id"])
                data.append({"id": city["id"], "slug": city["slug"], "name": city["name"], "state": city["state"], "code": city["code"], "period": row["period"]})

    return data