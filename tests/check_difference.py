import sqlite3

from helpers.__data_for_tables__ import get_weapons_param
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

#Перед прогоном тестов прогнать test_init закоммитив parametrized
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