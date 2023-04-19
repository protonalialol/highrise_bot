import highrise
from highrise import User

from EnhancedBaseBot import ExtendedBaseBot
from PokeBot.PokeCommandHandler import PokeCommandHandler

class PokeBot(ExtendedBaseBot):
    def __init__(self):
        super().__init__()
        self.helper.log_debug(f"{self.__class__.__name__} initialized!")

    async def on_start(self, session_metadata: highrise.SessionMetadata) -> None:
        await super().on_start(session_metadata=highrise.SessionMetadata)
        self.poke_cmd_handler = PokeCommandHandler(highrise=self.highrise, helper=self.helper, database=self.database)
        await self.highrise.chat(f"{self.BOT_TYPE} {self.BOT_VERSION} started, have fun :)")

    async def on_chat(self, user: User, message: str):
        await super().on_chat(user=user, message=message)
        await self.chat_handler(user=user, message=message)

    async def on_whisper(self, user: User, message: str):
        await super().on_whisper(user=user, message=message)
        await self.chat_handler(user=user, message=message)

    async def chat_handler(self, user: User, message: str):
        lowered_message = message.lower()

        if not message.startswith("!"):
            self.helper.log_debug(f"Not handling message '{lowered_message}' by {user.username} [{user.id}]")
            return

        command = lowered_message.split(" ")

        if command[0] == "!poke":
            self.helper.log_debug(f"!poke command invoked via '{command}' by user {user.username} [{user.id}]")
            await self.poke_cmd_handler.command_handler(user=user, message=lowered_message)
        else:
            self.helper.log_debug(f"Unrecognized command '{command}' by user {user.username} [{user.id}]")
            await self.highrise.send_whisper(user_id=user.id, message="Say !poke help to me!")
