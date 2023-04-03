from highrise import User, SessionMetadata

from extendedbasebot import ExtendedBaseBot
from highrisehelpers import Helpers
from poke import PokeCommandHandler

class PokeBot(ExtendedBaseBot):
    def __init__(self):
        super().__init__()
        self.PokeCommandHandler = PokeCommandHandler()

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        await super().on_start(session_metadata= SessionMetadata)
        super().print_properties()
        await self.highrise.chat(message=f'{self.BOT_TYPE} {self.BOT_VERSION} started, have fun :)')
        pass

    async def on_chat(self, user: User, message: str):
        await super().on_chat(user= user, message= message)
        await self.chat_handler(user=user, message=message)
        pass

    async def on_whisper(self, user: User, message: str):
        await super().on_whisper(user= user, message= message)
        match message.lower():
            case 'kill':
                exit(0)
        pass

    async def _whisper_help(self, user: User):
        await self.highrise.send_whisper(user_id=user.id, message= f'Help command!\r\n!poke help - Show this help')
        return

    
    async def chat_handler(self, user: User, message: str):
        self.helpers.log_debug(message=f'chat_handler called with {message} by user {user.username} [{user.id}]')

        # Ignore other messages
        if message[0] != '!':
            self.helpers.log_debug(message=f'Not handling message {message} by {user.username} [{user.id}]')
            return

        command = message.split(' ')

        match command[0]:
            case "!poke":
                await self.poke_handler(user=user, message=message)        
            case _:
                self.helpers.log_debug(message=f'Unrecognized command {command} by user {user.username} [{user.id}]')
                await self.highrise.send_whisper(user_id=user.id, message= f'Say !poke to me!')

    pass
