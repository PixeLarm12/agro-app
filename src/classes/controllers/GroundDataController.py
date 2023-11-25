from src.classes.GroundData import *

def getAllGrounds():
    return allGrounds()

def getCitiesGroundRelation():
    return relationCitiesGround()

def getCulturesGroundRelation():
    return relationCulturesGrounds()

def getGroundsByCity(cityId):
    data = []

    if(cityId): 
        for el in getCitiesGroundRelation():
            if int(el["city_id"] == cityId):
                ground = getGroundById(el["ground_id"])
                if(ground): 
                    data.append(ground)

    return data

def getGroundById(id):
    if(id): 
        for ground in getAllGrounds():
            if int(ground["id"]) == int(id):
                return ground
    else:
        return None