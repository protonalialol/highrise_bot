import logging
import os
import signal
import sqlite3
import SQLiteDatabase
import highrise

from sqlite3 import Error
from highrise import BaseBot, User

from SQLiteDatabase import DatabaseHandler

from highrisehelpers import Helper


class ExtendedBaseBot(BaseBot):
    def __init__(self):
        self.BOT_TYPE = os.getenv('BOT_TYPE')
        self.BOT_VERSION = os.getenv('BOT_VERSION')
        self.BOT_ADMINISTRATOR = os.getenv('BOT_ADMINISTRATOR')
        self.BOT_ADMINISTRATOR_ID = os.getenv('BOT_ADMINISTRATOR_ID')
        self.ROOM_ID = os.getenv('ROOM_ID')
        self.helper = Helper()
        #self.database = DatabaseHandler(db_file =f'/data/{self.BOT_TYPE}_sqlite.db', helper=self.helper)
        self.database = DatabaseHandler(db_file=f'D:\\temp\\{self.BOT_TYPE}_sqlite.db', helper=self.helper)
        signal.signal(signal.SIGTERM, self.sigterm_handler)
        self._print_environment_variables()

    def _print_environment_variables(self):
        self.helper.log_debug(message=f'BOT_TYPE: {self.BOT_TYPE}')
        self.helper.log_debug(message=f'BOT_VERSION: {self.BOT_VERSION}')
        self.helper.log_debug(message=f'BOT_ADMINISTRATOR: {self.BOT_ADMINISTRATOR}')
        self.helper.log_debug(message=f'BOT_ADMINISTRATOR_ID: {self.BOT_ADMINISTRATOR_ID}')
        self.helper.log_debug(message=f'ROOM_ID: {self.ROOM_ID}')

    # SIGTERM handler for pod termination
    def sigterm_handler(self, signum, frame):
        signame = signal.Signals(signum).name
        self.helper.log_debug(message=f'Signal handler called with signal {signame} ({signum})')
        self.database.close()
        exit(0)

    async def on_start(self, session_metadata: highrise.SessionMetadata) -> None:
        self.helper.log_debug(message=f'{__class__.__name__} initialized!')
        pass

    async def on_chat(self, user: User, message: str):
        self.helper.log_message(user=user, message=message)
        pass

    async def is_admin(self, user: User):
        if user.id == self.BOT_ADMINISTRATOR_ID and user.username == self.BOT_ADMINISTRATOR:
            return True
        if user.id == '63c08fb2d0187c1745407651' and user.username == 'Limamora':
            return True
        return False

    async def on_whisper(self, user: User, message: str):
        self.helper.log_whisper(user=user, message=message)
        match message.lower():
            case 'kill':
                if await self.is_admin(user=user):
                    exit(0)
                else:
                    self.helper.log_info(message=f'{user.username} [{user.id}] tried to kill me :(')
        pass

    pass
