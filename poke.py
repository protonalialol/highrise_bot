import highrise
from highrise import User, Position

import SQLiteDatabase
from SQLiteDatabase import DatabaseHandler
from highrisehelpers import Helper
import sqlite3

class PokeCommandHandler():
    def __init__(self, highrise: highrise, helper: Helper, database: DatabaseHandler):
        self.highrise = highrise
        self.helper = helper
        self.database = database
        self.room_users = None

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
        await self._update_user_locations()
        self.helper.log_debug(message=self.room_users)
        location = self.database.get_area_from_location(self._get_current_user_location(current_user=user))
        self.helper.log_debug(location)
        return

    async def _update_user_locations(self):
        self.room_users = await self.highrise.get_room_users()

    def _get_current_user_location(self, current_user: User):
        if self.room_users is None:
            self.helper.log_debug(f'Room users is None!')
            return "dark place"
        else:
            self.helper.log_debug(type(self.room_users))
            for user in self.room_users.content:
                self.helper.log_debug(f'{user[0]}_{user[1]}')
                if user[0] == current_user:
                    self.helper.log_debug(f'Location found for user {current_user}: {user[1]}!')
                    return user[1]
            self.helper.log_debug(f'Could not find location for user {current_user} in {self.room_users}!')
            return "dark place"

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
                return
            case _:
                self.helper.log_info(
                    message=f'default command (commands) initiated with "{poke_command}" by user {user.username} [{user.id}]')
                await self._whisper_commands(user=user)

        return
