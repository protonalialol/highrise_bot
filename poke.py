import highrise
from highrise import User

import SQLiteDatabase
from SQLiteDatabase import DatabaseHandler
from highrisehelpers import Helper
import sqlite3

class PokeCommandHandler():
    def __init__(self, highrise: highrise, helper: Helper, database: DatabaseHandler):
        self.highrise = highrise
        self.helper = helper
        self.database = database

    async def _whisper_help(self, user: User):
        await self.highrise.send_whisper(user_id=user.id,
                                         message=f'Welcome to PokeBot :)\r\n'
                                                 f'Catch Pokemon and collect them all.\r\n\r\n'
                                                 f'How to play:\r\n'
                                                 f'\t 1. Locate yourself in the room\r\n'
                                                 f'\t 2. Attract Pokemon with "!poke go"\r\n'
                                                 f'\t 3. Throw balls with "!poke ball"\r\n\r\n'
                                                 f'Find more different Pokemon by moving inside the room."\r\n')
        return

    async def _whisper_commands(self, user: User):
        await self.highrise.send_whisper(user_id=user.id,
                                         message=f'Commands:\r\n'
                                                 f'\t!poke go - Find Pokemon\r\n'
                                                 f'\t!poke ball - Throw Pokeball\r\n'
                                                 f'\t!poke select - Select Pokeball Type\r\n'
                                                 f'\t!poke shop - Show offers\r\n'
                                                 f'\t!poke buy - Buy items\r\n'
                                                 f'\t!poke bag - Show inventory\r\n'
                                                 f'\t!poke dex - Inspect Pokedex\r\n'
                                                 f'\t!poke help - Explain the game\r\n'
                                                 f'\t!poke commands - Show commands\r\n')
        return

    async def _go(self, user: User):

        return


    async def command_handler(self, user: User, message: str):
        self.helper.log_debug(message=f'command_handler called with "{message}" by user {user.username} [{user.id}]')
        poke_command = message.replace("!poke", "").strip(' ')

        self.helper.log_debug(message=f'poke_command: "{poke_command}" by user {user.username} [{user.id}]')

        match poke_command.lower():
            case "go":
                self.helper.log_info(
                    message=f'"!poke go" initiated with "{poke_command}" by user {user.username} [{user.id}]')
                await self._go(user=user)
            case "shop":
                self.helper.log_info(
                    message=f'"!poke shop" initiated with "{poke_command}" by user {user.username} [{user.id}]')
            case "bag":
                self.helper.log_info(
                    message=f'"!poke bag" initiated with "{poke_command}" by user {user.username} [{user.id}]')
            case "buy":
                self.helper.log_info(
                    message=f'"!poke buy" initiated with "{poke_command}" by user {user.username} [{user.id}]')
            case "help":
                self.helper.log_info(
                    message=f'"!poke help" initiated with "{poke_command}" by user {user.username} [{user.id}]')
                await self._whisper_help(user=user)
            case "commands":
                self.helper.log_info(
                    message=f'"!poke commands" initiated with "{poke_command}" by user {user.username} [{user.id}]')
                await self._whisper_commands(user=user)
            case "test":
                self.helper.log_info(
                    message=f'"!poke test" initiated with "{poke_command}" by user {user.username} [{user.id}]')
                a = await self.database.get_area_from_location("locationtest")
                self.helper.log_info(a)
            case _:
                self.helper.log_info(
                    message=f'default command (commands) initiated with "{poke_command}" by user {user.username} [{user.id}]')
                await self._whisper_commands(user=user)

        return
