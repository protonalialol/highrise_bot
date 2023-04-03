import highrise
from highrise import User

from extendedbasebot import ExtendedBaseBot
from poke import PokeCommandHandler

import sqlite3
from sqlite3 import Error

class PokeBot(ExtendedBaseBot):
    def __init__(self):
        super().__init__()

    async def on_start(self, session_metadata: highrise.SessionMetadata) -> None:
        await super().on_start(session_metadata=highrise.SessionMetadata)
        self.PokeCommandHandler = PokeCommandHandler(highrise=self.highrise, helper=self.helper, database_connection = self.database_connection)
        await self.highrise.chat(message=f'{self.BOT_TYPE} {self.BOT_VERSION} started, have fun :)')
        pass

    async def on_chat(self, user: User, message: str):
        await super().on_chat(user=user, message=message)
        await self.chat_handler(user=user, message=message)
        pass

    async def on_whisper(self, user: User, message: str):
        await super().on_whisper(user=user, message=message)
        match message.lower():
            case 'kill':
                exit(0)
        pass

    async def chat_handler(self, user: User, message: str):
        self.helper.log_debug(message=f'chat_handler called with "{message}" by user {user.username} [{user.id}]')

        # Ignore other messages
        if message[0] != '!':
            self.helper.log_debug(message=f'Not handling message "{message}" by {user.username} [{user.id}]')
            return

        command = message.split(' ')

        match command[0]:
            case "!poke":
                self.helper.log_debug(message=f'!poke command invoked via "{command}" by user {user.username} [{user.id}]')
                await self.PokeCommandHandler.command_handler(user=user, message=message)
            case _:
                self.helper.log_debug(message=f'Unrecognized command "{command}" by user {user.username} [{user.id}]')
                await self.highrise.send_whisper(user_id=user.id, message=f'Say !poke help to me!')

    pass
