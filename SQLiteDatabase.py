import sqlite3
import random
from sqlite3 import Error
from highrise import Position
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

    def _normalize_location(self, location: Position):
        return f'{round(location.x, 1)}_{round(location.y, 1)}_{round(location.z, 1)}'

    def _create_location(self, location: Position):
        area = self.get_random_area()
        self.cursor.execute('''INSERT INTO locations(location, area) VALUES (?, ?)''', (self._normalize_location(location), area))
        self.database_connection.commit()
        self.helper.log_debug(message=f'{self._normalize_location(location)} {area}')
        return area

    def get_area_from_location(self, location: Position):
        if self._is_location_existing(location):
            return self._select_area_from_location(location)[0][0]
        else:
            area = self._create_location(location)
            return area

    def _is_location_existing(self, location: Position):
        if len(self._select_area_from_location(location)) > 0:
            return True
        else:
            return False

    def get_random_area(self):
        return random.choice(self.areas)

    def _select_area_from_location(self, location: Position):
        self.cursor.execute('''SELECT area FROM locations where location = ?''', (self._normalize_location(location),))
        rows = self.cursor.fetchall()
        return rows

    def close(self):
        self.database_connection.close()

