import sqlite3
from random import random
from sqlite3 import Error
from highrisehelpers import Helper

class DatabaseHandler():
    def __init__(self, db_file: str, helper: Helper):
        self.helper = helper
        self.database_connection = self._create_connection(db_file)
        self.cursor = self.database_connection.cursor()
        self.areas = ["Grass", "Cave", "Water"]
        self._create_tables()

    def _create_connection(self, db_file: str):
        connection = None
        try:
            connection = sqlite3.connect(db_file)
            self.helper.log_info(message=f'Successfully connected to {db_file}!')
        except Error as e:
            print(e)
            exit(1)

        return connection

    def _create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS locations
                     (location TEXT, area TEXT)''')
        self.database_connection.commit()

    def _create_location(self, location):
        self.cursor.execute('''INSERT INTO locations(location, area) VALUES (?, ?)''', (location, self.get_random_area()))
        self.database_connection.commit()
        return

    def get_area_from_location(self, location: str):
        if self._is_location_existing(location):
            return self._select_area_from_location(location)[1]
        else:
            self._create_location(location)
            self.get_area_from_location(location)

    def _is_location_existing(self, location: str):
        if len(self._select_area_from_location() > 0):
            return True
        else:
            return False

    def get_random_area(self):
        return random.choice(self.areas)

    def _select_area_from_location(self, location: str):
        rows = self.cursor.execute('''SELECT area FROM locations where location = ?''', (location,))
        return rows

    def close(self):
        self.database_connection.close()

