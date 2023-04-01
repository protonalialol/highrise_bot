import os
import highrise
from highrise import BaseBot, User
from highrisehelpers import Helpers

import signal, os

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
        print(f'BOT_TYPE: {self.BOT_TYPE}')
        print(f'BOT_VERSION: {self.BOT_VERSION}')
        print(f'ROOM_ID: {self.ROOM_ID}')

    # SIGTERM handler for pod termination
    def handler(signum, frame):
        signame = signal.Signals(signum).name
        print(f'Signal handler called with signal {signame} ({signum})')
        exit(0)

    async def on_start(self, session_metadata: highrise.SessionMetadata) -> None:
        print(f'ExtendedBaseBot initialized!')
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

class InstanceBot(ExtendedBaseBot):
    async def on_start(self, session_metadata: highrise.SessionMetadata) -> None:
        await super().on_start(session_metadata= highrise.SessionMetadata)
        super().print_properties()
        await self.highrise.chat(message=f'{self.BOT_TYPE} {self.BOT_VERSION} started, have fun :)')
        pass

    async def on_chat(self, user: User, message: str):
        await super().on_chat(user= user, message= message)
        await self.highrise.chat(message=f'Custom implementation here!')
        pass

    async def on_whisper(self, user: User, message: str):
        await super().on_whisper(user= user, message= message)
        match message.lower():
            case 'kill':
                exit(0)
        pass
        
    pass
