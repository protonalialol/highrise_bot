import sqlite3
from sqlite3 import Error

class DataBaseHandler():
    def __init__(self, db_file):
        self.database_connection = self._create_connection(db_file)
        self.cursor = self.database_connection.cursor()
        self._create_tables()

    def _create_connection(self, db_file: str):
        connection = None
        try:
            connection = sqlite3.connect(db_file)
            self.helper.log_info(message=f'Successfully connected to {db_file}!')
        except Error as e:
            print(e)
            exit(1)
        finally:
            if connection:
                connection.close()

        return connection

    def _create_tables(self):
        self.cursor.execute('''CREATE TABLE locations
                     (location TEXT, area TEXT)''')
        self.database_connection.commit()

    def _create_location(self):
        return

    def get_area_from_location(self, location: str):
        return

    def _select_area_from_location(self, location: str):
        rows = self.cursor.execute('''SELECT area FROM locations where location = ?''', (location,))
        print(rows)
        return

    def close(self):
        self.database_connection.close()

