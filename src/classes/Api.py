from src.classes.controllers.ComercialDataController import *
from src.classes.controllers.GroundDataController import *

def fetchCultureComercialPerCulture(culture):
    data = []

    for row in getCitiesCulturesRelation():
        if (row["culture_id"] is culture["id"]):
            city = getCityById(row["city_id"])
            
            if(city):
                data.append({
                    "id": city["id"], 
                    "slug": city["slug"], 
                    "name": city["name"], 
                    "state": city["state"], 
                    "code": city["code"], 
                    "period": culture["period"],
                    "cultures": [],
                    "grounds": [],
                })

    return data

def fetchCultureGroundPerCulture(culture):
    data = []
    groundTypesIds = []
    avoidDuplicatedCities = []

    for row in getCulturesGroundRelation():
        # get specifics types of grounds to plant the given culture
        if(row["culture_id"] == culture["id"]):
            groundTypesIds.append(row["ground_id"])

    for row in getCitiesGroundRelation():    
        if (row["ground_id"] in groundTypesIds and row["city_id"] not in avoidDuplicatedCities):
            city = getCityById(row["city_id"])

            if(city):
                avoidDuplicatedCities.append(city["id"])
                
                data.append({
                    "id": city["id"], 
                    "slug": city["slug"], 
                    "name": city["name"], 
                    "state": city["state"], 
                    "code": city["code"], 
                    "period": culture["period"],
                    "cultures": [],
                    "grounds": getGroundsByCity(city["id"])
                })

    return data

def fetchCulturesComercialPerPeriod(period):
    data = []
    culturesIds = []
    avoidDuplicatedCities = []

    
    if(period == "ano todo"):
        for row in getAllCultures():
            culturesIds.append(row["id"])
    else: 
        for row in getAllCultures():
            if(row["period"].find(period) != -1 or row["period"] is "ano todo"):
                culturesIds.append(row["id"])

    for row in getCitiesCulturesRelation():
        if(row["culture_id"] in culturesIds and row["city_id"] not in avoidDuplicatedCities):
            city = getCityById(row["city_id"])

            if(city):
                culturesAux = []
                avoidDuplicatedCities.append(city["id"])

                for el in getCulturesByCity(city["id"]):
                    if(el["id"] in culturesIds):
                        culturesAux.append(el)

                data.append({
                    "id": city["id"], 
                    "slug": city["slug"], 
                    "name": city["name"], 
                    "state": city["state"], 
                    "code": city["code"], 
                    "period": period,
                    "cultures": culturesAux,
                    "grounds": []
                })

    return data

def fetchCulturesGroundPerPeriod(period):
    data = []
    culturesIds = []
    groundsIds = []
    avoidDuplicatedCities = []

    if(period == "ano todo"):
        for row in getAllCultures():
            culturesIds.append(row["id"])
    else:
        for row in getAllCultures():
            if(row["period"].find(period) != -1 or row["period"] is "ano todo"):
                culturesIds.append(row["id"])

    for row in getCulturesGroundRelation():
        if(row["culture_id"] in culturesIds):
            groundsIds.append(row["ground_id"])

    for row in getCitiesGroundRelation():
        if(row["ground_id"] in groundsIds and row["id"] not in avoidDuplicatedCities):
            city = getCityById(row["id"])

            if(city):
                avoidDuplicatedCities.append(city["id"])

                culturesAux = []

                for el in getCulturesByCity(city["id"]):
                    if(el["id"] in culturesIds):
                        culturesAux.append(el)

                data.append({
                    "id": city["id"], 
                    "slug": city["slug"], 
                    "name": city["name"], 
                    "state": city["state"], 
                    "code": city["code"], 
                    "period": period,
                    "cultures": culturesAux,
                    "grounds": getGroundsByCity(city["id"])
                })
    return data

def filterCities(cultureId, period, filterType):
    data = [] 

    # Show all cities that corresponds to comercial production of culture by given cultureId
    if(cultureId and filterType.find("comercial") != -1): 
        data = fetchCultureComercialPerCulture(getCultureById(cultureId))
    
    # Select all cities that the ground are able to plant the given culture based on researches
    if(cultureId and filterType.find("ground") != -1): 
        data = fetchCultureGroundPerCulture(getCultureById(cultureId))

    # Show all cities and his possible cultures with the given period
    if(not cultureId and filterType.find("comercial") != -1):
        data = fetchCulturesComercialPerPeriod(period)

    # Select all cities that are able to plant whatever culture in given period based on his ground types 
    if(not cultureId and filterType.find("ground") != -1):
        data = fetchCulturesGroundPerPeriod(period)

    return data

def isBestPeriod(cultureId, period):
    if(not cultureId):
        return False
    else: 
        culture = getCultureById(cultureId)

        if(culture):
            return bool(culture["period"].find(period) != -1)
        else:
            return False

