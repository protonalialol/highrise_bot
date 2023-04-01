import datetime

import highrise
from highrise import BaseBot, User

def now_timestamp():
    return datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")

class Bot(BaseBot):
    async def on_start(self, session_metadata: highrise.SessionMetadata) -> None:
        await self.highrise.chat(message=f'Demo Bot started, have fun :)')
        await self.highrise.chat(message=f'Send me some stuff UwU')

    async def on_chat(self, user: User, message: str):
        print(f'{now_timestamp()} | {user.username} [{user.id}]: "{message}"')
        a = await self.highrise.get_room_users()
        print(a)
        await self.highrise.chat(message=f'You said {message}')

    pass
