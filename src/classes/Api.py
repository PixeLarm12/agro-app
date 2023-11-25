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

def fetchCultureComercial(culture, period):
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

def fetchCultureGround(culture, period):
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

def filterCities(cultureId, period, filterType):
    data = [] 

    # show all cities that match cultureId by the most cultivated cultures at given period
    if(isinstance(cultureId, int) and filterType.find("comercial") != -1): 
        data = fetchCultureComercial(getCultureById(cultureId), period)
    
    # show all cities that are able to plant the selected culture thinking about ground types
    if(isinstance(cultureId, int) and filterType.find("ground") != -1): 
        data = fetchCultureGround(getCultureById(cultureId), period)
        

    # # filter all cultures able in each cities based on comercial data
    # elif(not isinstance(cultureId, int) and filterType.find("comercial") != -1):
    #     avoidDuplicatedCities = []

    #     for row in cities_cultures():
    #         culturesId = getCulturesIdsByPeriod(period)
            
    #         if (row["culture_id"] in culturesId and row["city_id"] not in avoidDuplicatedCities):
    #             city = getCityById(row["city_id"])
                
    #             if(city):
    #                 avoidDuplicatedCities.append(city["id"])
    #                 data.append({
    #                      "id": city["id"], 
    #                      "slug": city["slug"], 
    #                      "name": city["name"], 
    #                      "state": city["state"], 
    #                      "code": city["code"], 
    #                      "period": period,
    #                      "cultures": getCulturesByIdsAndCity(culturesId, city["id"]),
    #                      "grounds": []
    #                 })

    # # filter all cultures able in each cities based on grounds data
    # elif(not isinstance(cultureId, int) and filterType.find("ground") != -1):
    #     groundIds = []
    #     avoidDuplicatedCities = []

    #     for row in getCulturesGroundData():
    #         culturesId = getCulturesIdsByPeriod(period)
            
    #         if (row["culture_id"] in culturesId):
    #             ground = getGroundById(row["ground_id"])
                
    #             if(ground):
    #                 groundIds.append(ground["id"])

    #     for row in getCitiesGroundData():
    #         if (row["ground_id"] in groundIds and row["city_id"] not in avoidDuplicatedCities):
    #             city = getCityById(row["city_id"])

    #             if(city):
    #                 avoidDuplicatedCities.append(city["id"])

    #                 data.append({
    #                      "id": city["id"], 
    #                      "slug": city["slug"], 
    #                      "name": city["name"], 
    #                      "state": city["state"], 
    #                      "code": city["code"], 
    #                      "period": period,
    #                      "cultures": getCulturesByIdsAndCity(culturesId, city["id"]),
    #                      "grounds": getGroundsByCity(city["id"])
    #                 })

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

