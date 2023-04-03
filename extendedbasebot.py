import os
import signal

import highrise
from highrise import BaseBot, User

from highrisehelpers import Helpers


class ExtendedBaseBot(BaseBot):
    def __init__(self):
        signal.signal(signal.SIGTERM, self.handler)
        self.initialize_properties()
        self.helpers = Helpers()

    # Initialize base properties
    def initialize_properties(self):
        self.BOT_TYPE = os.getenv('BOT_TYPE')
        self.BOT_VERSION = os.getenv('BOT_VERSION')
        self.ROOM_ID = os.getenv('ROOM_ID')

    # Print out base properties
    def print_properties(self):
        self.helpers.log_debug(message=f'BOT_TYPE: {self.BOT_TYPE}')
        self.helpers.log_debug(message=f'BOT_VERSION: {self.BOT_VERSION}')
        self.helpers.log_debug(message=f'ROOM_ID: {self.ROOM_ID}')

    # SIGTERM handler for pod termination
    def handler(self, signum, frame):
        self.helpers.log_debug(message = f'Signal handler called with signal {signame} ({signum})')
        signame = signal.Signals(signum).name
        exit(0)

    async def on_start(self, session_metadata: highrise.SessionMetadata) -> None:
        self.helpers.log_debug(message="ExtendedBaseBot initialized!")
        pass

    async def on_chat(self, user: User, message: str):
        self.helpers.log_message(user= user, message=message)
        pass

    async def on_whisper(self, user: User, message: str):
        self.helpers.log_whisper(user=user, message=message)
        match message.lower():
            case 'kill':
                exit(0)
        pass    

    pass