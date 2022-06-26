from random import randint

def get_engine_data():
    engines_date = []
    i = 1
    while i < 7:
        cort = 'engine' + str(i), randint(1, 20), randint(1, 20)
        engines_date.append(cort)
        i += 1

    return engines_date

def get_hull_data():
    hulls_data = []
    i = 1
    while i < 6:
        cort = 'hull' + str(i), randint(1, 20), randint(1, 20), randint(1, 2)
        hulls_data.append(cort)
        i += 1

    return hulls_data

def get_weapon_data():
    weapons_data = []
    i = 1
    while i < 21:
        cort = 'weapon' + str(i), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20)
        weapons_data.append(cort)
        i += 1

    return weapons_data

def get_ship_data():
    ships_data = []
    i = 1
    while i < 201:
        cort = 'ship' + str(i), 'weapon' + str(randint(1, 20)), 'hull' + str(randint(1, 5)), 'engine' + str(randint(1,6))
        ships_data.append(cort)
        i += 1

    return ships_data

def get_ship_data_change():
    ship_parts = ['weapon', 'hull', 'engine']
    ship_data_change = []
    i = 1
    while i < 201:
        ship_part = ship_parts[randint(0, 2)]
        cort = ship_part, ship_part + str(randint(1, 20)), 'ship' + str(i)
        ship_data_change.append(cort)
        i += 1
    return ship_data_change

def get_weapons_data_change():
    weapons_param = get_weapons_param()
    weapons_data_change = []
    i = 1
    while i < 21:
        weapon_param = weapons_param[randint(0, 4)]
        cort = weapon_param, randint(1, 20), 'weapon' + str(i)
        weapons_data_change.append(cort)
        i += 1
    return weapons_data_change

def get_hulls_data_change():
    hulls_param = get_hulls_param()
    hull_data_change = []
    i = 1
    while i < 6:
        hull_param = hulls_param[randint(0, 2)]
        cort = hull_param, randint(1, 20), 'hull' + str(i)
        hull_data_change.append(cort)
        i += 1
    return hull_data_change

def get_engines_data_change():
    engine_params = get_engines_param()
    engine_data_change = []
    i = 1
    while i < 7:
        engine_param = engine_params[randint(0, 1)]
        cort = engine_param, randint(1, 20), 'engine' + str(i)
        engine_data_change.append(cort)
        i += 1
    return engine_data_change


def get_engines_param():
    return ["power", "type"]

def get_hulls_param():
    return ["armor", "type", "capacity"]

def get_weapons_param():
    return ["reload_speed", "rotational_speed", "diameter", "power_volley", "count"]