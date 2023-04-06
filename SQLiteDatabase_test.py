import unittest
import sqlite3
from highrise import User
from highrisehelpers import Helper
from unittest.mock import MagicMock

from SQLiteDatabase import DatabaseHandler


class TestDatabaseHandler(unittest.TestCase):

    def setUp(self):
        self.db_file = ':memory:'
        self.helper = Helper()
        self.handler = DatabaseHandler(db_file=self.db_file, helper=self.helper)

    def tearDown(self):
        self.handler.close()

    def test_create_connection(self):
        connection = self.handler._create_connection(self.db_file)
        self.assertIsInstance(connection, sqlite3.Connection)

    def test_create_tables(self):
        self.handler._create_tables()
        tables = ['locations', 'players', 'bags']
        for table in tables:
            self.assertTrue(table in [i[0] for i in self.handler.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()])

    def test_create_location(self):
        location = (10, 10)
        area = self.handler._create_location(location)
        self.assertTrue(area in self.handler.areas)

    def test_create_user_inventory(self):
        user = User(id="1", username="test")
        self.handler._create_user_inventory(user)
        self.assertEqual(self.handler._select_bag_from_bags(user)[0][1:], (0, 0, 0, 0, 0, 0))

    def test_create_user(self):
        user = User(id="1", username="test")
        self.handler._create_user(user)
        self.assertEqual(self.handler._select_user_from_players(user)[0][1:], (user.username, 0, 0))

    def test_get_or_create_user_bag(self):
        user = User(id="1", username="test")
        bag = self.handler.get_or_create_user_bag(user)
        self.assertEqual(bag[1:], (0, 0, 0, 0, 0, 0))

    def test_get_or_create_user(self):
        user = User(id="1", username="test")
        created_user = self.handler.get_or_create_user(user)
        self.assertEqual(created_user[1:], (user.username, 0, 0))

    def test_get_or_create_area_from_location(self):
        location = (10, 10)
        area = self.handler.get_or_create_area_from_location(location)
        self.assertTrue(area in self.handler.areas)

    def test_is_user_existing(self):
        user = User(id="1", username="test")
        self.assertFalse(self.handler._is_user_existing(user))

    def test_is_user_bag_existing(self):
        user = User(id="1", username="test")
        self.assertFalse(self.handler._is_user_bag_existing(user))

    def test_is_location_existing(self):
        location = (10, 10)
        self.assertFalse(self.handler._is_location_existing(location))
