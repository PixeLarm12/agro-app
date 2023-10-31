from src.classes.Database import CulturasPorEstado, CulturaPorId

def getCulturesFromApi():
    return CulturasPorEstado("SP")

def getCultivationByCultureId(cultureId):
    return CulturaPorId("SP", cultureId)