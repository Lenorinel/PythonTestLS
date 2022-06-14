
from providers.__bd_table_provider__ import initialize_tables, add_data_in_tables, delete_all_tables, Connection

import sqlite3

def prepare_base():
    connections_array = []
    con = sqlite3.connect('warships.db')
    conObj = Connection(con)
    #initialize_tables(conObj)
    # add_data_in_tables(conObj)
    connections_array.append(conObj)

    copy = sqlite3.connect(':memory:')
    con.backup(copy)
    copyObj = Connection(copy)
    Connection.update_ships_table(copyObj)
    connections_array.append(copyObj)

    return connections_array


if __name__ == '__main__':
    #before_all
    connections = prepare_base()

    #test
    first_db_result = Connection.get_all_rows(connections[0])
    second_db_result = Connection.get_all_rows(connections[1])

    first_db_result.sort()
    second_db_result.sort()

    print(first_db_result == second_db_result)
    #assert(compare_two_db()) -
    #1. Получить запрос со всеми данными из начальной таблицы
    #2. Для каждого кортежа из п1 взять ship и отправить select по этому ключу во временную бд
    #3. Сравнить исходный кортеж со временным, вывести несовпадающие элементы
