import sqlite3

from helpers.__data_for_tables__ import get_weapons_param, get_hulls_param, get_engines_param
from providers.__bd_table_provider__ import Connection, get_all_ships_id, initialize_tables, add_data_in_tables, \
    randomize_temp_table
import pytest


@pytest.mark.parametrize("ship_id",  open("file.txt", "r"))
def test_compare_weapon(ship_id):
    weapons_param = get_weapons_param()
    main = sqlite3.connect('warships.db')
    mainObj = Connection(main)

    rand = sqlite3.connect('warships_2.db')
    randObj = Connection(rand)
    clear_ship_id = ship_id.strip()

    main_base_ship_weapon = Connection.get_ship_weapon(mainObj, clear_ship_id)
    temp_base_ship_weapon = Connection.get_ship_weapon(randObj, clear_ship_id)
    ex, = main_base_ship_weapon
    act, = temp_base_ship_weapon

    main_weapon_param = Connection.get_weapon_param(mainObj, ex)
    temp_weapon_param = Connection.get_weapon_param(randObj, ex)
    expected_actual_weapon = []

    main.close()
    rand.close()

    i = 0
    for param in main_weapon_param:
        if param not in temp_weapon_param:
            expected_actual_weapon.append(param)
            expected_actual_weapon.append(temp_weapon_param[i])
            expected_actual_weapon.append(i)
        i += 1
    if len(expected_actual_weapon) != 0:
        assert expected_actual_weapon[1] == expected_actual_weapon[0], clear_ship_id + ", " + ex + "\n" + weapons_param[expected_actual_weapon[2]-1] + ": expected " + str(expected_actual_weapon[0]) + ", actual " + str(expected_actual_weapon[1])
    assert temp_base_ship_weapon == main_base_ship_weapon , clear_ship_id + ", " + ex + "\nExpected: " + ex + ", was: " + act

@pytest.mark.parametrize("ship_id",  open("file.txt", "r"))
def test_compare_hull(ship_id):
    hulls_param = get_hulls_param()
    main = sqlite3.connect('warships.db')
    mainObj = Connection(main)

    rand = sqlite3.connect('warships_2.db')
    randObj = Connection(rand)
    clear_ship_id = ship_id.strip()

    main_base_ship_hull = Connection.get_ship_hull(mainObj, clear_ship_id)
    temp_base_ship_hull = Connection.get_ship_hull(randObj, clear_ship_id)
    ex, = main_base_ship_hull
    act, = temp_base_ship_hull

    main_hull_param = Connection.get_hull_param(mainObj, ex)
    temp_hull_param = Connection.get_hull_param(randObj, ex)
    expected_actual_hull = []

    main.close()
    rand.close()

    i = 0
    for param in main_hull_param:
        if param not in temp_hull_param:
            expected_actual_hull.append(param)
            expected_actual_hull.append(temp_hull_param[i])
            expected_actual_hull.append(i)
        i += 1
    if len(expected_actual_hull) != 0:
        assert expected_actual_hull[1] == expected_actual_hull[0], clear_ship_id + ", " + ex + "\n" + hulls_param[expected_actual_hull[2]-1] + ": expected " + str(expected_actual_hull[0]) + ", actual " + str(expected_actual_hull[1])
    assert temp_base_ship_hull == main_base_ship_hull, clear_ship_id + ", " + ex + "\nExpected: " + ex + ", was: " + act

@pytest.mark.parametrize("ship_id",  open("file.txt", "r"))
def test_compare_engine(ship_id):
    engines_param = get_engines_param()
    main = sqlite3.connect('warships.db')
    mainObj = Connection(main)

    rand = sqlite3.connect('warships_2.db')
    randObj = Connection(rand)
    clear_ship_id = ship_id.strip()

    main_base_ship_engine = Connection.get_ship_engine(mainObj, clear_ship_id)
    temp_base_ship_engine = Connection.get_ship_engine(randObj, clear_ship_id)
    ex, = main_base_ship_engine
    act, = temp_base_ship_engine

    main_engine_param = Connection.get_engine_param(mainObj, ex)
    temp_engine_param = Connection.get_engine_param(randObj, ex)
    expected_actual_engine = []

    main.close()
    rand.close()

    i = 0
    for param in main_engine_param:
        if param not in temp_engine_param:
            expected_actual_engine.append(param)
            expected_actual_engine.append(temp_engine_param[i])
            expected_actual_engine.append(i)
        i += 1
    if len(expected_actual_engine) != 0:
        assert expected_actual_engine[1] == expected_actual_engine[0], clear_ship_id + ", " + ex + "\n" + engines_param[expected_actual_engine[2]-1] + ": expected " + str(expected_actual_engine[0]) + ", actual " + str(expected_actual_engine[1])
    assert temp_base_ship_engine == main_base_ship_engine, clear_ship_id + ", " + ex + "\nExpected: " + ex + ", was: " + act

#?????????? ???????????????? ???????????? ???????????????? test_init ???????????????????? parametrized
def test_init():
    con = sqlite3.connect('warships.db')
    conObj = Connection(con)
    initialize_tables(conObj)
    add_data_in_tables(conObj)

    copy = sqlite3.connect('warships_2.db')
    con.backup(copy)
    copyObj = Connection(copy)
    randomize_temp_table(copyObj)

    ships_id = get_all_ships_id(conObj)
    f = open("file.txt", "w")
    for row in ships_id:
        line = ' '.join(str(x) for x in row)
        f.write(line + '\n')
    f.close()