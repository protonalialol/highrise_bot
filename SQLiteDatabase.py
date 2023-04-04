import sqlite3
import random
from sqlite3 import Error
from highrise import User, Position
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
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS locations (
                        location TEXT, 
                        area TEXT
                        )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS players (
                        userid TEXT UNIQUE,
                        username TEXT,
                        amountTipped REAL,
                        affectionFactor REAL
                        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS bags (
                        userid TEXT,
                        pokeballs INTEGER NOT NULL, 
                        superballs INTEGER NOT NULL, 
                        hyperballs INTEGER NOT NULL, 
                        masterballs INTEGER NOT NULL, 
                        baits INTEGER NOT NULL, 
                        stones INTEGER NOT NULL,
                        FOREIGN KEY (userid) REFERENCES players(userid)
                        )''')

        self.database_connection.commit()

    def _create_location(self, location: Position):
        area = self.get_random_area()
        self.cursor.execute('''INSERT INTO locations(location, area) VALUES (?, ?)''', (self.helper.normalize_location(location), area))
        self.database_connection.commit()
        self.helper.log_debug(message=f'Inserted: {self.helper.normalize_location(location)} {area}')
        return area

    def _create_user_inventory(self, user: User):
        self.cursor.execute('''INSERT INTO bags(userid, pokeballs, superballs, hyperballs, masterballs, baits, stones) VALUES (?, ?, ?, ?, ?, ?, ?)''', (user.id, 0, 0, 0, 0, 0, 0))
        self.database_connection.commit()
        self.helper.log_debug(message=f'Created inventory for user {user.id} [{user.username}]')
        return

    def _create_user(self, user: User):
        self.cursor.execute('''INSERT INTO players(userid, username, amountTipped, affectionFactor) VALUES (?, ?, ?, ?)''', (user.id, user.username, 0, 0))
        self.database_connection.commit()
        self.helper.log_debug(message=f'Created user {user.id} [{user.username}]')
        return

    def get_user_bag(self, user: User):
        if self._is_user_existing(user=user):
            if self._is_user_bag_existing(user=user):
                return self._select_bag_from_bags(user=user)[0]
            else:
                self._create_user_inventory(user=user)
                self.get_user_bag(user=user)
        else:
            self._create_user(user=user)
            self.get_user_bag(user=user)


    def get_area_from_location(self, location: Position):
        if self._is_location_existing(location=location):
            return self._select_area_from_location(location)[0][0]
        else:
            area = self._create_location(location=location)
            return area


    def _is_user_existing(self, user: User):
        if len(self._select_user_from_players(user)) > 0:
            return True
        else:
            return False

    def _is_user_bag_existing(self, user: User):
        if len(self._select_bag_from_bags(user)) > 0:
            return True
        else:
            return False

    def _is_location_existing(self, location: Position):
        if len(self._select_area_from_location(location)) > 0:
            return True
        else:
            return False

    def get_random_area(self):
        return random.choice(self.areas)

    def _select_area_from_location(self, location: Position):
        self.cursor.execute('''SELECT area FROM locations where location = ?''', (self.helper.normalize_location(location),))
        rows = self.cursor.fetchall()
        return rows

    def _select_user_from_players(self, user: User):
        self.cursor.execute('''SELECT * FROM players where userid = ?''', (user.id,))
        rows = self.cursor.fetchall()
        return rows

    def _select_bag_from_bags(self, user: User):
        self.cursor.execute('''SELECT * FROM bags where userid = ?''', (user.id,))
        rows = self.cursor.fetchall()
        return rows

    def close(self):
        self.database_connection.close()

