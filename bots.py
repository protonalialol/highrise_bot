import os
import highrise
from highrise import BaseBot, User
from highrisehelpers import Helpers

import signal, os



class DemoBot(BaseBot):
    def __init__(self):
        signal.signal(signal.SIGTERM, self.handler)
        self.initialize_properties()
        self.helpers = Helpers()

    def initialize_properties(self):
        self.BOT_TYPE = os.getenv('BOT_TYPE')
        self.BOT_VERSION = os.getenv('BOT_VERSION')
        self.ROOM_ID = os.getenv('ROOM_ID')

    def handler(signum, frame):
        signame = signal.Signals(signum).name
        print(f'Signal handler called with signal {signame} ({signum})')
        exit(0)

    async def on_start(self, session_metadata: highrise.SessionMetadata) -> None:
        await self.highrise.chat(message=f'{self.BOT_TYPE} {self.BOT_VERSION} started, have fun :)')

    async def on_chat(self, user: User, message: str):
        self.helpers.log_message(user= user, message=message)
        a = await self.highrise.get_room_users()
        print(a)
        await self.highrise.chat(message=f'You said {message}')

    async def on_whisper(self, user: User, message: str):
        self.helpers.log_whisper(user=user, message=message)

        match message.lower():
            case 'kill':
                exit(0)


    pass
