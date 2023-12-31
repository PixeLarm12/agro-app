def allGrounds():
    return [
        {"id": 1, "title": "Afloramento Rochoso"},
        {"id": 2, "title": "Argissolo Amarelo"},
        {"id": 3, "title": "Argissolo Vermelho-Amarelo"},
        {"id": 4, "title": "Argissolo Vermelho"},
        {"id": 5, "title": "Cambissolo Húmico"},
        {"id": 6, "title": "Cambissolo Háplico"},
        {"id": 7, "title": "Chernossolo Argilúvico"},
        {"id": 8, "title": "Espodossolo Humilúvico"},
        {"id": 9, "title": "Gleissolo Háplico"},
        {"id": 10, "title": "Gleissolo Melânico"},
        {"id": 11, "title": "Gleissolo Sálico"},
        {"id": 12, "title": "Gleissolo Tiomórfico"},
        {"id": 13, "title": "Latossolo Amarelo"},
        {"id": 14, "title": "Latossolo Bruno"},
        {"id": 15, "title": "Latossolo Vermelho-Amarelo"},
        {"id": 16, "title": "Latossolo Vermelho"},
        {"id": 17, "title": "Luvissolo Háplico"},
        {"id": 18, "title": "Neossolo Flúvico"},
        {"id": 19, "title": "Neossolo Litólico"},
        {"id": 20, "title": "Neossolo Quartzarênico"},
        {"id": 21, "title": "Nitossolo Vermelho"},
        {"id": 22, "title": "Organossolo Háplico"},
        {"id": 23, "title": "Organossolo Tiomórfico"},
        {"id": 24, "title": "Planossolo Háplico"},
        {"id": 25, "title": "Plintossolo Pétrico"},
    ]

def relationCulturesGrounds():
    return [
        { "id": 1, "culture_id": 1, "ground_id": 18}, 
        { "id": 2, "culture_id": 1, "ground_id": 9}, 
        { "id": 3, "culture_id": 2, "ground_id": 15}, 
        { "id": 4, "culture_id": 2, "ground_id": 16}, 
        { "id": 5, "culture_id": 3, "ground_id": 10}, 
        { "id": 6, "culture_id": 3, "ground_id": 18}, 
        { "id": 7, "culture_id": 4, "ground_id": 13}, 
        { "id": 8, "culture_id": 4, "ground_id": 14}, 
        { "id": 9, "culture_id": 5, "ground_id": 16}, 
        { "id": 10, "culture_id": 5, "ground_id": 3},
        { "id": 11, "culture_id": 5, "ground_id": 4}, 
        { "id": 12, "culture_id": 6, "ground_id": 16}, 
        { "id": 13, "culture_id": 6, "ground_id": 5}, 
        { "id": 14, "culture_id": 7, "ground_id": 5}, 
        { "id": 15, "culture_id": 7, "ground_id": 6}, 
        { "id": 16, "culture_id": 7, "ground_id": 18}, 
        { "id": 17, "culture_id": 8, "ground_id": 18}, 
        { "id": 18, "culture_id": 8, "ground_id": 9}, 
        { "id": 19, "culture_id": 9, "ground_id": 18}, 
        { "id": 20, "culture_id": 9, "ground_id": 9}, 
        { "id": 21, "culture_id": 10, "ground_id": 9}, 
        { "id": 22, "culture_id": 10, "ground_id": 22}, 
        { "id": 23, "culture_id": 11, "ground_id": 16},
        { "id": 24, "culture_id": 11, "ground_id": 3},
        { "id": 25, "culture_id": 11, "ground_id": 4}, 
        { "id": 26, "culture_id": 12, "ground_id": 16},
        { "id": 27, "culture_id": 12, "ground_id": 3}, 
        { "id": 28, "culture_id": 13, "ground_id": 15},
        { "id": 29, "culture_id": 13, "ground_id": 16}, 
        { "id": 30, "culture_id": 14, "ground_id": 5,},
        { "id": 31, "culture_id": 14, "ground_id": 6,},
        { "id": 32, "culture_id": 14, "ground_id": 18}, 
        { "id": 33, "culture_id": 15, "ground_id": 5,},
        { "id": 34, "culture_id": 15, "ground_id": 18}, 
        { "id": 35, "culture_id": 16, "ground_id": 5,},
        { "id": 36, "culture_id": 16, "ground_id": 6,},
        { "id": 37, "culture_id": 16, "ground_id": 18}, 
        { "id": 38, "culture_id": 17, "ground_id": 16},
        { "id": 39, "culture_id": 17, "ground_id": 3},
        { "id": 40, "culture_id": 17, "ground_id": 4}, 
        { "id": 41, "culture_id": 18, "ground_id": 10},
        { "id": 42, "culture_id": 18, "ground_id": 18}, 
        { "id": 43, "culture_id": 19, "ground_id": 15},
        { "id": 44, "culture_id": 19, "ground_id": 16}, 
        { "id": 45, "culture_id": 20, "ground_id": 16},
        { "id": 46, "culture_id": 20, "ground_id": 3}, 
    ]  

def relationCitiesGround():
    return [
        {"id": 1, "ground_id": 3, "city_id": 1},
        {"id": 2, "ground_id": 3, "city_id": 2},
        {"id": 3, "ground_id": 15, "city_id": 2},
        {"id": 4, "ground_id": 6, "city_id": 2},
        {"id": 5, "ground_id": 6, "city_id": 3},
        {"id": 6, "ground_id": 6, "city_id": 4},
        {"id": 7, "ground_id": 6, "city_id": 5},
        {"id": 8, "ground_id": 3, "city_id": 5},
        {"id": 9, "ground_id": 3, "city_id": 6},
        {"id": 10, "ground_id": 6, "city_id": 6},
        {"id": 11, "ground_id": 13, "city_id": 6},
        {"id": 12, "ground_id": 3, "city_id": 7},
        {"id": 13, "ground_id": 6, "city_id": 7},
        {"id": 14, "ground_id": 16, "city_id": 7},
        {"id": 15, "ground_id": 3, "city_id": 8},
        {"id": 16, "ground_id": 6, "city_id": 8},
        {"id": 17, "ground_id": 15, "city_id": 8},
        {"id": 18, "ground_id": 3, "city_id": 9},
        {"id": 19, "ground_id": 16, "city_id": 9},
        {"id": 20, "ground_id": 3, "city_id": 10},
        {"id": 21, "ground_id": 16, "city_id": 10},
        {"id": 22, "ground_id": 15, "city_id": 10},
        {"id": 23, "ground_id": 3, "city_id": 11},
        {"id": 24, "ground_id": 3, "city_id": 12},
        {"id": 25, "ground_id": 15, "city_id": 12},
        {"id": 26, "ground_id": 3, "city_id": 13},
        {"id": 27, "ground_id": 3, "city_id": 14},
        {"id": 28, "ground_id": 15, "city_id": 14},
        {"id": 29, "ground_id": 16, "city_id": 14},
        {"id": 30, "ground_id": 4, "city_id": 14},
        {"id": 31, "ground_id": 3, "city_id": 15},
        {"id": 32, "ground_id": 3, "city_id": 16},
        {"id": 33, "ground_id": 16, "city_id": 16},
        {"id": 34, "ground_id": 15, "city_id": 17},
        {"id": 35, "ground_id": 3, "city_id": 17},
        {"id": 36, "ground_id": 6, "city_id": 17},
        {"id": 37, "ground_id": 3, "city_id": 18},
        {"id": 38, "ground_id": 6, "city_id": 18},
        {"id": 39, "ground_id": 15, "city_id": 18},
        {"id": 40, "ground_id": 3, "city_id": 19},
        {"id": 41, "ground_id": 15, "city_id": 19},
        {"id": 42, "ground_id": 3, "city_id": 20},
        {"id": 43, "ground_id": 15, "city_id": 20},
        {"id": 44, "ground_id": 16, "city_id": 20},
        {"id": 45, "ground_id": 21, "city_id": 20},
        {"id": 46, "ground_id": 3, "city_id": 21},
        {"id": 47, "ground_id": 15, "city_id": 21},
        {"id": 48, "ground_id": 16, "city_id": 21},
        {"id": 49, "ground_id": 3, "city_id": 22},
        {"id": 50, "ground_id": 16, "city_id": 22},
        {"id": 51, "ground_id": 4, "city_id": 22},
        {"id": 52, "ground_id": 3, "city_id": 23},
        {"id": 53, "ground_id": 15, "city_id": 23},
        {"id": 54, "ground_id": 16, "city_id": 23},
        {"id": 55, "ground_id": 9, "city_id": 23},
        {"id": 56, "ground_id": 3, "city_id": 24},
        {"id": 57, "ground_id": 16, "city_id": 24},
        {"id": 58, "ground_id": 15, "city_id": 24},
        {"id": 59, "ground_id": 21, "city_id": 24},
        {"id": 60, "ground_id": 16, "city_id": 25},
        {"id": 61, "ground_id": 20, "city_id": 25},
        {"id": 62, "ground_id": 3, "city_id": 25},
        {"id": 63, "ground_id": 16, "city_id": 26},
        {"id": 64, "ground_id": 15, "city_id": 26},
        {"id": 65, "ground_id": 20, "city_id": 26},
        {"id": 66, "ground_id": 3, "city_id": 27},
        {"id": 67, "ground_id": 16, "city_id": 27},
        {"id": 68, "ground_id": 3, "city_id": 28},
        {"id": 69, "ground_id": 16, "city_id": 28},
        {"id": 70, "ground_id": 21, "city_id": 28},
        {"id": 71, "ground_id": 16, "city_id": 29},
        {"id": 72, "ground_id": 21, "city_id": 29},
        {"id": 73, "ground_id": 16, "city_id": 30},
        {"id": 74, "ground_id": 21, "city_id": 30},
        {"id": 75, "ground_id": 15, "city_id": 30},
        {"id": 76, "ground_id": 3, "city_id": 31},
        {"id": 77, "ground_id": 25, "city_id": 31},
        {"id": 78, "ground_id": 16, "city_id": 32},
        {"id": 79, "ground_id": 21, "city_id": 32},
        {"id": 80, "ground_id": 15, "city_id": 32},
        {"id": 81, "ground_id": 3, "city_id": 32},
        {"id": 82, "ground_id": 3, "city_id": 33},
        {"id": 83, "ground_id": 16, "city_id": 33},
        {"id": 84, "ground_id": 16, "city_id": 34},
        {"id": 85, "ground_id": 13, "city_id": 34},
        {"id": 86, "ground_id": 13, "city_id": 35},
        {"id": 87, "ground_id": 16, "city_id": 35},
        {"id": 88, "ground_id": 19, "city_id": 35},
        {"id": 89, "ground_id": 16, "city_id": 36},
        {"id": 90, "ground_id": 13, "city_id": 36},
        {"id": 91, "ground_id": 3, "city_id": 37},
        {"id": 92, "ground_id": 16, "city_id": 37},
        {"id": 93, "ground_id": 15, "city_id": 37},
        {"id": 94, "ground_id": 14, "city_id": 37},
        {"id": 95, "ground_id": 16, "city_id": 38},
        {"id": 96, "ground_id": 3, "city_id": 38},
        {"id": 97, "ground_id": 14, "city_id": 38},
        {"id": 98, "ground_id": 16, "city_id": 39},
        {"id": 99, "ground_id": 16, "city_id": 40},
        {"id": 100, "ground_id": 3, "city_id": 40},
        {"id": 101, "ground_id": 14, "city_id": 40},
        {"id": 102, "ground_id": 3, "city_id": 41},
        {"id": 103, "ground_id": 16, "city_id": 41},
        {"id": 104, "ground_id": 3, "city_id": 42},
        {"id": 105, "ground_id": 3, "city_id": 43},
        {"id": 106, "ground_id": 16, "city_id": 43},
        {"id": 107, "ground_id": 3, "city_id": 44},
        {"id": 108, "ground_id": 16, "city_id": 44},
        {"id": 109, "ground_id": 21, "city_id": 45},
        {"id": 110, "ground_id": 16, "city_id": 45},
        {"id": 111, "ground_id": 3, "city_id": 45},
        {"id": 112, "ground_id": 3, "city_id": 46},
        {"id": 113, "ground_id": 16, "city_id": 46},
        {"id": 114, "ground_id": 4, "city_id": 47},
        {"id": 115, "ground_id": 3, "city_id": 47},
        {"id": 116, "ground_id": 3, "city_id": 48},
        {"id": 117, "ground_id": 16, "city_id": 48},
        {"id": 118, "ground_id": 4, "city_id": 48},
        {"id": 119, "ground_id": 20, "city_id": 48},
        {"id": 120, "ground_id": 24, "city_id": 48},
        {"id": 121, "ground_id": 3, "city_id": 49},
        {"id": 122, "ground_id": 16, "city_id": 49},
        {"id": 123, "ground_id": 3, "city_id": 50},
        {"id": 124, "ground_id": 16, "city_id": 50},
        {"id": 125, "ground_id": 16, "city_id": 51},
        {"id": 126, "ground_id": 3, "city_id": 51},
        {"id": 127, "ground_id": 3, "city_id": 52},
        {"id": 128, "ground_id": 16, "city_id": 52},
        {"id": 129, "ground_id": 21, "city_id": 52},
        {"id": 130, "ground_id": 3, "city_id": 53},
        {"id": 131, "ground_id": 16, "city_id": 53},
        {"id": 132, "ground_id": 24, "city_id": 53},
        {"id": 133, "ground_id": 16, "city_id": 54},
        {"id": 134, "ground_id": 3, "city_id": 54},
        {"id": 135, "ground_id": 24, "city_id": 54},
        {"id": 136, "ground_id": 3, "city_id": 55},
        {"id": 137, "ground_id": 16, "city_id": 55},
        {"id": 138, "ground_id": 3, "city_id": 56},
        {"id": 139, "ground_id": 15, "city_id": 56},
    ]