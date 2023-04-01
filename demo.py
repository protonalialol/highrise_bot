import datetime

import highrise
from highrise import BaseBot, User
from highrisehelpers import Helpers


class Bot(BaseBot):
    def __init__(self):
        self.helpers = Helpers()
    async def on_start(self, session_metadata: highrise.SessionMetadata) -> None:
        await self.highrise.chat(message=f'Demo Bot started, have fun :)')
        await self.highrise.chat(message=f'Send me some stuff UwU')

    async def on_chat(self, user: User, message: str):
        print(f'{self.helpers.now_timestamp()} | {user.username} [{user.id}]: "{message}"')
        a = await self.highrise.get_room_users()
        print(a)
        await self.highrise.chat(message=f'You said {message}')

    async def on_whisper(self, user: User, message: str):
        print(f'{self.helpers.now_timestamp()} | {user.username} [{user.id}] [whisper]: "{message}"')

        match message.lower():
            case 'kill':
                exit(0)


    pass
