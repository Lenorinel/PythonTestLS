import sqlite3

from providers.__bd_table_provider__ import Connection, get_all_ships_id, initialize_tables, add_data_in_tables
import pytest


@pytest.mark.parametrize("ship_id",  open("file.txt", "r"))  # pylint: disable=no-self-use
def test_compare_weapon(ship_id):
    main = sqlite3.connect('warships.db')
    mainObj = Connection(main)

    rand = sqlite3.connect('warships_2.db')
    randObj = Connection(rand)
    clear_ship_id = ship_id.strip()

    main_base_ship_weapon = Connection.get_ship_weapon(mainObj, clear_ship_id)
    temp_base_ship_weapon = Connection.get_ship_weapon(randObj, clear_ship_id)
    ex, = main_base_ship_weapon
    act, = temp_base_ship_weapon

    pytest.assume(main_base_ship_weapon == temp_base_ship_weapon, clear_ship_id + ", " + ex + "\nExpected: " + ex + ", was: " + act)
    pytest.assume(False)
    # assert main_base_ship_weapon == temp_base_ship_weapon, clear_ship_id + ", " + ex + "\nExpected: " + ex + ", was: " + act

def test_init():
    con = sqlite3.connect('warships.db')
    conObj = Connection(con)
    initialize_tables(conObj)
    add_data_in_tables(conObj)

    copy = sqlite3.connect('warships_2.db')
    con.backup(copy)
    copyObj = Connection(copy)
    Connection.update_ships_table(copyObj)

    ships_id = get_all_ships_id(conObj)
    f = open("file.txt", "w")
    for row in ships_id:
        line = ' '.join(str(x) for x in row)
        f.write(line + '\n')
    f.close()