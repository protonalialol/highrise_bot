import os
import highrise
from highrise import BaseBot, User
from highrisehelpers import Helpers


class DemoBot(BaseBot):
    def __init__(self):
        self.helpers = Helpers()
        self.test()

    def test(self):
        print("Env vairables now:")
        print(os.getenv('BOT_TYPE'))
        print(os.getenv('ROOM_ID'))
        print(os.getenv('API_KEY'))

    async def on_start(self, session_metadata: highrise.SessionMetadata) -> None:
        await self.highrise.chat(message=f'Demo Bot started, have fun :)')
        await self.highrise.chat(message=f'Send me some stuff UwU')

    async def on_chat(self, user: User, message: str):
        self.helpers.log_message(user= user, message=message)
        a = await self.highrise.get_room_users()
        print(a)
        await self.highrise.chat(message=f'You said {message}')

    async def on_whisper(self, user: User, message: str):
        print(f'Whisper heard')
        self.helpers.log_whisper(user=user, message=message)

        match message.lower():
            case 'kill':
                exit(0)


    pass
