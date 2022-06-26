import sqlite3

from helpers.__data_for_tables__ import get_ship_data, get_hull_data, get_weapon_data, get_engine_data, \
    get_ship_data_change, get_weapons_data_change, get_engines_data_change, get_hulls_data_change


class Connection:

    def __init__(self, connection):
        self.connection = connection


    def get_all_rows(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM ships;")
        results = cursor.fetchall()
        return results

    def get_ship_weapon(self, ship_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT weapon FROM ships WHERE ship = \'" + ship_id + "\';")
        result = cursor.fetchone()
        return result

    def get_weapon_param(self, weapon_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM weapons WHERE weapon = \'" + weapon_id + "\';")
        result = cursor.fetchone()
        return result

    def get_ship_hull(self, ship_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT hull FROM ships WHERE ship = \'" + ship_id + "\';")
        result = cursor.fetchone()
        return result

    def get_hull_param(self, hull_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM hulls WHERE hull = \'" + hull_id + "\';")
        result = cursor.fetchone()
        return result

    def get_ship_engine(self, ship_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT engine FROM ships WHERE ship = \'" + ship_id + "\';")
        result = cursor.fetchone()
        return result

    def get_engine_param(self, engine_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM engines WHERE engine = \'" + engine_id + "\';")
        result = cursor.fetchone()
        return result

    def create_ships_table(self):
        self.connection.cursor().execute("""CREATE TABLE IF NOT EXISTS ships(
        ship TEXT PRIMARY KEY,
        weapon TEXT,
        hull TEXT,
        engine TEXT)
        """)
        self.connection.commit()

    def create_weapons_table(self):
        self.connection.cursor().execute("""CREATE TABLE IF NOT EXISTS weapons(
        weapon TEXT PRIMARY KEY,
        reload_speed INT,
        rotational_speed INT,
        diameter INT,
        power_volley INT,
        count INT)
        """)
        self.connection.commit()

    def create_hulls_table(self):
        self.connection.cursor().execute("""CREATE TABLE IF NOT EXISTS hulls(
        hull TEXT PRIMARY KEY,
        armor INT,
        type INT,
        capacity INT)
        """)
        self.connection.commit()

    def create_engines_table(self):
        self.connection.cursor().execute("""CREATE TABLE IF NOT EXISTS engines(
        engine TEXT PRIMARY KEY,
        power INT,
        type INT)
        """)
        self.connection.commit()

    def insert_ships_data(self, list):
        self.connection.cursor().executemany("INSERT INTO ships VALUES(?,?,?,?);", list)
        self.connection.commit()

    def insert_weapons_data(self, list):
        self.connection.cursor().executemany("INSERT INTO weapons VALUES(?,?,?,?,?,?);", list)
        self.connection.commit()

    def insert_hulls_data(self, list):
        self.connection.cursor().executemany("INSERT INTO hulls VALUES(?,?,?,?);", list)
        self.connection.commit()


    def insert_engines_data(self, list):
        self.connection.cursor().executemany("INSERT INTO engines VALUES(?,?,?);", list)
        self.connection.commit()

    def drop_ships_table(self, tables_list):
        for table_name in tables_list:
            self.connection.cursor().execute("DROP TABLE IF EXISTS " + table_name + ";")

    def update_ships_table(self):
        pair_for_change = get_ship_data_change()
        for pair in pair_for_change:
            param_for_update, param_value, ship_id = pair
            self.connection.cursor().execute("UPDATE ships SET " + param_for_update + " = \'" + param_value + "\' WHERE ship = \'" + ship_id + "\';")
            self.connection.commit()

    def update_weapons_table(self):
        pair_for_change = get_weapons_data_change()
        for pair in pair_for_change:
            param_for_update, param_value, weapon_id = pair
            self.connection.cursor().execute("UPDATE weapons SET " + param_for_update + " = \'" + str(param_value) + "\' WHERE weapon = \'" + weapon_id + "\';")
            self.connection.commit()

    def update_hulls_table(self):
        data_for_change = get_hulls_data_change()
        for pair in data_for_change:
            param_for_update, param_value, hull_id = pair
            self.connection.cursor().execute("UPDATE hulls SET " + param_for_update + " = \'" + str(
                param_value) + "\' WHERE hull = \'" + hull_id + "\';")
            self.connection.commit()

    def update_engine_table(self):
        data_for_change = get_engines_data_change()
        for pair in data_for_change:
            param_for_update, param_value, engine_id = pair
            self.connection.cursor().execute("UPDATE engines SET " + param_for_update + " = \'" + str(
                param_value) + "\' WHERE engine = \'" + engine_id + "\';")
            self.connection.commit()

    def select_ships_id(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT ship FROM ships;")
        results = cursor.fetchall()
        return results


def initialize_tables(conObj):
    Connection.create_ships_table(conObj)
    Connection.create_engines_table(conObj)
    Connection.create_hulls_table(conObj)
    Connection.create_weapons_table(conObj)


def add_data_in_tables(conObj):
    Connection.insert_ships_data(conObj, get_ship_data())
    Connection.insert_hulls_data(conObj, get_hull_data())
    Connection.insert_weapons_data(conObj, get_weapon_data())
    Connection.insert_engines_data(conObj, get_engine_data())

def randomize_temp_table(con):
    Connection.update_weapons_table(con)
    Connection.update_ships_table(con)
    Connection.update_engine_table(con)
    Connection.update_hulls_table(con)

def get_all_ships_id(conObj):
   result = Connection.select_ships_id(conObj)
   return result

def delete_all_tables(conObj):
    tables_list = ['ships', 'weapons', 'engines', 'hulls']
    Connection.drop_ships_table(conObj, tables_list)
