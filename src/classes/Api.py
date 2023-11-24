from src.classes.Tables import *
from src.classes.GroundData import *
import operator

def Cultures():
    data = cultures()
    data.sort(key=operator.itemgetter('name'))

    return data

def getCulturesByCity(cityId):
    data = []

    if(cityId): 
        for el in cities_cultures():
            if int(el["city_id"]) == int(cityId):
                culture = getCultureById(el["culture_id"])
                if(culture): 
                    data.append(culture)

        return data
    else:
        return None

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

def filterCities(cultureId, period, filterType):
    data = [] 

    # show all cities that match cultureId by the most cultivated cultures at given period
    if(cultureId and filterType == "comercial"): 
        for row in cities_cultures():
            if (int(row["culture_id"]) == int(cultureId) and row["period"].find(period) != -1):
                city = getCityById(row["city_id"])
                if(city):
                    data.append({"id": city["id"], "slug": city["slug"], "name": city["name"], "state": city["state"], "code": city["code"], "period": row["period"], "cultures": []})
    # api will show all cities that are able to receive selected culture in given period - check ground types
    if(cultureId and filterType == "ground"):
        culture = getCultureById(cultureId)
        groundIds = []

        if(culture):
            for row in getCulturesGroundData():
                if (int(culture["id"]) == int(row["culture_id"])):
                    groundIds.append(row["ground_id"])
            
            for row in getCitiesGroundData():
                if(int(row["ground_id"]) in groundIds):
                    city = getCityById(row["city_id"])

                    if(city):
                        data.append({"id": city["id"], "slug": city["slug"], "name": city["name"], "state": city["state"], "code": city["code"], "period": culture["period"], "cultures": []})
    # return all cities that are able to receive cultures by given period (will show a lot of them)
    else:
        for row in cities_cultures():
            if (row["period"].find(period) != -1):
                city = getCityById(row["city_id"])
                cultures = getCulturesByCity(city["id"])
                if(city):
                    data.append({"id": city["id"], "slug": city["slug"], "name": city["name"], "state": city["state"], "code": city["code"], "period": row["period"], "cultures": cultures})

    return data