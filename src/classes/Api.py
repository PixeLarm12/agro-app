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
    
def getGroundsByCity(cityId):
    data = []

    if(cityId): 
        for el in getCitiesGroundData():
            if int(el["city_id"] == cityId):
                ground = getGroundById(el["ground_id"])
                if(ground): 
                    data.append(ground)

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

def getGroundById(id):
    if(id): 
        for ground in getGroundsData():
            if int(ground["id"]) == int(id):
                return ground
    else:
        return None

def getCulturesIdsByPeriod(period):
    data = []

    if(period): 
        for culture in cultures():
            if culture["period"].find(period) != -1:
                data.append(culture["id"])
    
    return data

def getCulturesByIdsAndCity(cultureIds, cityId):
    data = []

    if(len(cultureIds) > 0):
        for el in cities_cultures():
            if (el['culture_id'] in cultureIds and el['city_id'] == cityId):
                data.append(getCultureById(el["culture_id"]))

    return data

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

def fetchCultureComercialPerCulture(culture):
    data = []

    for row in cities_cultures():
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

    for row in getCulturesGroundData():
        # get specifics types of grounds to plant the given culture
        if(row["culture_id"] == culture["id"]):
            groundTypesIds.append(row["ground_id"])

    for row in getCitiesGroundData():    
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

    for row in cultures():
        if(row["period"].find(period) != -1 or period is "ano todo"):
            culturesIds.append(row["id"])

    for row in cities_cultures():
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

    for row in cultures():
        if(row["period"].find(period) != -1 or period is "ano todo"):
            culturesIds.append(row["id"])

    for row in getCulturesGroundData():
        if(row["culture_id"] in culturesIds):
            groundsIds.append(row["ground_id"])

    for row in getCitiesGroundData():
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

