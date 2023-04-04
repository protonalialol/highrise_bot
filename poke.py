import asyncio

from enum import Enum

import highrise
from highrise import User, Position

import SQLiteDatabase
import poke
from SQLiteDatabase import DatabaseHandler
from highrisehelpers import Helper
import sqlite3

class PokeCommandHandler():
    def __init__(self, highrise: highrise, helper: Helper, database: DatabaseHandler):
        self.highrise = highrise
        self.helper = helper
        self.database = database
        self.room_users = None

    async def _whisper_help(self, user: highrise.User):
        await self.highrise.send_whisper(user_id=user.id,
                                         message=f'Welcome to PokeBot :)\r\n'
                                                 f'Catch Pokemon and collect them all.\r\n\r\n'
                                                 f'How to play:\r\n'
                                                 f'\t 1. Locate yourself in the room\r\n'
                                                 f'\t 2. Attract Pokemon with "!poke go"\r\n'
                                                 f'\t 3. Throw balls with "!poke ball"\r\n\r\n'
                                                 f'Find more different Pokemon by moving inside the room.')
        return

    async def _whisper_commands(self, user: highrise.User):
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
                                                 )
        return

    async def _go(self, user: User):
        await self._update_user_locations()
        self.helper.log_debug(message=self.room_users)
        location = self.database.get_area_from_location(self._get_current_user_location(current_user=user))
        self.helper.log_debug(f'Searching for Pokemon in {location}...')
        await self.highrise.send_whisper(user_id=user.id, message=f'Searching for Pokemon in {location}...')
        await asyncio.sleep(5)
        await self.highrise.send_whisper(user_id=user.id, message=f'Found a Pikachu!')

        return

    async def _update_user_locations(self):
        self.room_users = await self.highrise.get_room_users()

    def _get_current_user_location(self, current_user: User):
        if self.room_users is None:
            self.helper.log_debug(f'Room users is None!')
            return "dark place"
        else:
            for user in self.room_users.content:
                self.helper.log_debug(f'{user[0]}_{user[1]}')
                if user[0] == current_user:
                    self.helper.log_debug(f'Location found for user {current_user}: {user[1]}!')
                    return user[1]
            self.helper.log_debug(f'Could not find location for user {current_user} in {self.room_users}!')
            return "dark place"

    async def _bag(self, user: User):
        self.database.
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
            case "ball":
                self.helper.log_info(
                    message=f'"!poke ball" initiated with "{poke_command}" by user {user.username} [{user.id}]')
            case "select":
                self.helper.log_info(
                    message=f'"!poke select" initiated with "{poke_command}" by user {user.username} [{user.id}]')
            case "shop":
                self.helper.log_info(
                    message=f'"!poke shop" initiated with "{poke_command}" by user {user.username} [{user.id}]')
            case "buy":
                self.helper.log_info(
                    message=f'"!poke buy" initiated with "{poke_command}" by user {user.username} [{user.id}]')
            case "bag":
                self.helper.log_info(
                    message=f'"!poke bag" initiated with "{poke_command}" by user {user.username} [{user.id}]')
                await self._bag(user=user)
            case "dex":
                self.helper.log_info(
                    message=f'"!poke dex" initiated with "{poke_command}" by user {user.username} [{user.id}]')
            case "help":
                self.helper.log_info(
                    message=f'"!poke help" initiated with "{poke_command}" by user {user.username} [{user.id}]')
                await self._whisper_help(user=user)
            case _:
                self.helper.log_info(
                    message=f'default command (commands) initiated with "{poke_command}" by user {user.username} [{user.id}]')
                await self._whisper_commands(user=user)

        return

class PokemonCollection():
    def __init__(self):
        self.pokemon_dict = {}
        self.pokemon = []
        self._initialize_pokemon_dict()
        self._initialize_pokemon()

    def _initialize_pokemon(self):
        for dict_pokemon in self.pokemon_dict:
            self.pokemon.append("test")

    def _initialize_pokemon_dict(self):
        self.pokemon_dict = {
            'Bulbasaur': {'location': 'Grass', 'weight': 5.0},
            'Ivysaur': {'location': 'Grass', 'weight': 4.5},
            'Venusaur': {'location': 'Grass', 'weight': 4.0},
            'Charmander': {'location': 'Grass', 'weight': 5.0},
            'Charmeleon': {'location': 'Grass', 'weight': 4.5},
            'Charizard': {'location': 'Grass', 'weight': 4.0},
            'Squirtle': {'location': 'Water', 'weight': 5.0},
            'Wartortle': {'location': 'Water', 'weight': 4.5},
            'Blastoise': {'location': 'Water', 'weight': 4.0},
            'Caterpie': {'location': 'Grass', 'weight': 9.0},
            'Metapod': {'location': 'Grass', 'weight': 8.0},
            'Butterfree': {'location': 'Grass', 'weight': 4.0},
            'Weedle': {'location': 'Grass', 'weight': 9.0},
            'Kakuna': {'location': 'Grass', 'weight': 8.0},
            'Beedrill': {'location': 'Grass', 'weight': 4.0},
            'Pidgey': {'location': 'Grass', 'weight': 9.0},
            'Pidgeotto': {'location': 'Grass', 'weight': 8.0},
            'Pidgeot': {'location': 'Grass', 'weight': 4.0},
            'Rattata': {'location': 'Grass', 'weight': 9.0},
            'Raticate': {'location': 'Grass', 'weight': 8.0},
            'Spearow': {'location': 'Grass', 'weight': 9.0},
            'Fearow': {'location': 'Grass', 'weight': 8.0},
            'Ekans': {'location': 'Grass', 'weight': 9.0},
            'Arbok': {'location': 'Grass', 'weight': 8.0},
            'Pikachu': {'location': 'Grass', 'weight': 6.0},
            'Raichu': {'location': 'Grass', 'weight': 3.0},
            'Sandshrew': {'location': 'Cave', 'weight': 8.0},
            'Sandslash': {'location': 'Cave', 'weight': 4.0},
            'Nidoran♀': {'location': 'Grass', 'weight': 6.0},
            'Nidorina': {'location': 'Grass', 'weight': 4.5},
            'Nidoqueen': {'location': 'Grass', 'weight': 1.0},
            'Nidoran♂': {'location': 'Grass', 'weight': 6.0},
            'Nidorino': {'location': 'Grass', 'weight': 4.5},
            'Nidoking': {'location': 'Grass', 'weight': 1.0},
            'Clefairy': {'location': 'Moon', 'weight': 4.0},
            'Clefable': {'location': 'Cave', 'weight': 40.0},
            'Vulpix': {'location': 'Grass', 'weight': 9.9},
            'Ninetales': {'location': 'Grass', 'weight': 19.9},
            'Jigglypuff': {'location': 'Grass', 'weight': 5.5},
            'Wigglytuff': {'location': 'Grass', 'weight': 12.0},
            'Zubat': {'location': 'Cave', 'weight': 7.5},
            'Golbat': {'location': 'Cave', 'weight': 55.0},
            'Oddish': {'location': 'Grass', 'weight': 5.4},
            'Gloom': {'location': 'Grass', 'weight': 8.6},
            'Vileplume': {'location': 'Grass', 'weight': 18.6},
            'Paras': {'location': 'Grass', 'weight': 5.4},
            'Parasect': {'location': 'Grass', 'weight': 29.5},
            'Venonat': {'location': 'Grass', 'weight': 30.0},
            'Venomoth': {'location': 'Grass', 'weight': 12.5},
            'Diglett': {'location': 'Cave', 'weight': 0.8},
            'Dugtrio': {'location': 'Cave', 'weight': 33.3},
            'Meowth': {'location': 'Grass', 'weight': 4.2},
            'Persian': {'location': 'Grass', 'weight': 32.0},
            'Psyduck': {'location': 'Water', 'weight': 19.6},
            'Golduck': {'location': 'Water', 'weight': 76.6},
            'Mankey': {'location': 'Grass', 'weight': 28.0},
            'Primeape': {'location': 'Grass', 'weight': 32.0},
            'Growlithe': {'location': 'Grass', 'weight': 19.0},
            'Arcanine': {'location': 'Grass', 'weight': 155.0},
            'Poliwag': {'location': 'Water', 'weight': 12.4},
            'Poliwhirl': {'location': 'Water', 'weight': 20.0},
            'Poliwrath': {'location': 'Water', 'weight': 54.0},
            'Abra': {'location': 'Grass', 'weight': 19.5},
            'Kadabra': {'location': 'Grass', 'weight': 56.5},
            'Alakazam': {'location': 'Grass', 'weight': 48.0},
            'Machop': {'location': 'Grass', 'weight': 19.5},
            'Machoke': {'location': 'Grass', 'weight': 70.5},
            'Machamp': {'location': 'Grass', 'weight': 130.0},
            'Bellsprout': {'location': 'Grass', 'weight': 4.0},
            'Weepinbell': {'location': 'Grass', 'weight': 6.4},
            'Victreebel': {'location': 'Grass', 'weight': 15.5},
            'Tentacool': {'location': 'Water', 'weight': 45.5},
            'Tentacruel': {'location': 'Water', 'weight': 55.0},
            'Geodude': {'location': 'Cave', 'weight': 20.0},
            'Graveler': {'location': 'Cave', 'weight': 105.0},
            'Golem': {'location': 'Cave', 'weight': 300.0},
            'Ponyta': {'location': 'Grass', 'weight': 30.0},
            'Rapidash': {'location': 'Grass', 'weight': 95.0},
            'Slowpoke': {'location': 'Water', 'weight': 36.0},
            'Slowbro': {'location': 'Water', 'weight': 78.5},
            'Magnemite': {'location': 'Cave', 'weight': 6.0},
            'Magneton': {'location': 'Cave', 'weight': 60.0},
            'Farfetch"d': {'location': 'Grass', 'weight': 15.0},
            'Doduo': {'location': 'Grass', 'weight': 39.2},
            'Dodrio': {'location': 'Grass', 'weight': 85.2},
            'Seel': {'location': 'Water', 'weight': 90.0},
            'Dewgong': {'location': 'Water', 'weight': 120.0},
            'Grimer': {'location': 'Cave', 'weight': 30.0},
            'Muk': {'location': 'Cave', 'weight': 30.0},
            'Shellder': {'location': 'Water', 'weight': 4.0},
            'Cloyster': {'location': 'Water', 'weight': 132.5},
            'Gastly': {'location': 'Cave', 'weight': 0.1},
            'Haunter': {'location': 'Cave', 'weight': 0.1},
            'Gengar': {'location': 'Cave', 'weight': 40.5},
            'Onix': {'location': 'Cave', 'weight': 210.0},
            'Drowzee': {'location': 'Grass', 'weight': 32.4},
            'Hypno': {'location': 'Grass', 'weight': 75.6},
            'Krabby': {'location': 'Water', 'weight': 6.5},
            'Kingler': {'location': 'Water', 'weight': 60.0},
            'Voltorb': {'location': 'Cave', 'weight': 10.4},
            'Electrode': {'location': 'Cave', 'weight': 66.6},
            'Exeggcute': {'location': 'Grass', 'weight': 2.5},
            'Exeggutor': {'location': 'Grass', 'weight': 120.0},
            'Cubone': {'location': 'Cave', 'weight': 6.5},
            'Marowak': {'location': 'Cave', 'weight': 45.0},
            'Hitmonlee': {'location': 'N/A', 'weight': 49.8},
            'Hitmonchan': {'location': 'N/A', 'weight': 50.2},
            'Lickitung': {'location': 'Grass', 'weight': 65.5},
            'Koffing': {'location': 'Cave', 'weight': 1.0},
            'Weezing': {'location': 'Cave', 'weight': 9.5},
            'Rhyhorn': {'location': 'Grass', 'weight': 115.0},
            'Rhydon': {'location': 'Grass', 'weight': 120.0},
            'Chansey': {'location': 'Grass', 'weight': 34.6},
            'Tangela': {'location': 'Grass', 'weight': 35.0},
            'Kangaskhan': {'location': 'Grass', 'weight': 80.0},
            'Horsea': {'location': 'Water', 'weight': 8.0},
            'Seadra': {'location': 'Water', 'weight': 25.0},
            'Goldeen': {'location': 'Water', 'weight': 15.0},
            'Seaking': {'location': 'Water', 'weight': 39.0},
            'Staryu': {'location': 'Water', 'weight': 34.5},
            'Starmie': {'location': 'Water', 'weight': 80.0},
            'Mr. Mime': {'location': 'Grass', 'weight': 54.5},
            'Scyther': {'location': 'Grass', 'weight': 56.0},
            'Jynx': {'location': 'Cave', 'weight': 40.6},
            'Electabuzz': {'location': 'Grass', 'weight': 30.0},
            'Magmar': {'location': 'Cave', 'weight': 44.5},
            'Pinsir': {'location': 'Grass', 'weight': 55.0},
            'Tauros': {'location': 'Grass', 'weight': 88.4},
            'Magikarp': {'location': 'Water', 'weight': 10.0},
            'Gyarados': {'location': 'Water', 'weight': 235.0},
            'Lapras': {'location': 'Water', 'weight': 220.0},
            'Ditto': {'location': 'Grass', 'weight': 4.0},
            'Eevee': {'location': 'Grass', 'weight': 6.5},
            'Vaporeon': {'location': 'Water', 'weight': 29.0},
            'Jolteon': {'location': 'Cave', 'weight': 24.5},
            'Flareon': {'location': 'Grass', 'weight': 25.0},
            'Porygon': {'location': 'Cave', 'weight': 36.5},
            'Omanyte': {'location': 'Water', 'weight': 7.5},
            'Omastar': {'location': 'Water', 'weight': 35.0},
            'Kabuto': {'location': 'Water', 'weight': 11.5},
            'Kabutops': {'location': 'Water', 'weight': 40.5},
            'Aerodactyl': {'location': 'Cave', 'weight': 59.0},
            'Snorlax': {'location': 'Grass', 'weight': 460.0},
            'Articuno': {'location': 'N/A', 'weight': 55.4},
            'Zapdos': {'location': 'N/A', 'weight': 52.6},
            'Moltres': {'location': 'N/A', 'weight': 60.0},
            'Dratini': {'location': 'Water', 'weight': 3.3},
            'Dragonair': {'location': 'Water', 'weight': 16.5},
            'Dragonite': {'location': 'Water', 'weight': 210.0},
            'Mewtwo': {'location': 'N/A', 'weight': 122.0},
            'Mew': {'location': 'N/A', 'weight': 4.0}
    }

class Pokemon():
    def __init__(self, name: str, location: str, weight: float, legendary : bool = False):
        self.name = name
        self.location = location
        self.weight = weight
        self.legendary = legendary

    def isLegendary(self):
        return self.legendary
class PokemonLocation(Enum):
    GRASS = 1
    CAVE = 2
    DEEP_CAVE = 3
    BEACH = 4
    WATER = 5
    DEEP_WATER = 6
    CITY = 7
    VOLCANO = 8
    ICE_MOUNTAIN = 9
    THUNDER_HILL = 10
    MOON = 11
    SECRET_CAVE = 12


