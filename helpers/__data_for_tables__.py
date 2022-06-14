from random import randint

def get_engine_data():
    engines_date = []
    i = 1
    while i < 7:
        cort = 'engine' + str(i), randint(1,20), randint(1,20)
        engines_date.append(cort)
        i += 1

    return engines_date

def get_hull_data():
    hulls_data = []
    i = 1
    while i < 6:
        cort = 'hull' + str(i), randint(1,20), randint(1,20), randint(1,2)
        hulls_data.append(cort)
        i += 1

    return hulls_data

def get_weapon_data():
    weapons_data = []
    i = 1
    while i < 21:
        cort = 'weapon' + str(i), randint(1,20), randint(1,20), randint(1,20), randint(1,20), randint(1,20)
        weapons_data.append(cort)
        i += 1

    return weapons_data

def get_ship_data():
    ships_data = []
    i = 1
    while i < 201:
        cort = 'ship' + str(i), 'weapon' + str(randint(1,20)), 'hull' + str(randint(1,5)), 'engine' + str(randint(1,6))
        ships_data.append(cort)
        i += 1

    return ships_data

#можно добавить изменение рандомного поля черех объявление массива с полями, типа
# cort = ship_fields[randint(0,3)] + ...
def get_ship_data_change():
    ship_data_change = []
    i = 1
    while i < 201:
        cort = 'weapon' + str(randint(1, 20)), 'ship' + str(i)
        ship_data_change.append(cort)
        i += 1
    return  ship_data_change
