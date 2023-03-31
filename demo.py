import datetime
import random
import time
import highrise

from random_word import RandomWords
from highrise import Highrise, BaseBot, User
from highrisehelpers import Helpers
from dataclasses import dataclass


def read_attribute_file(filepath):
    with open(filepath, 'r') as f_object:
        word_lst = f_object.read().split()
    return word_lst


def now_timestamp():
    return datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")


async def getweather(city):
    async with python_weather.Client(format=python_weather.METRIC) as client:
        weather = await client.get(city)
    return f'Right now we got {weather.current.temperature}°C in {city}.'


class Bot(BaseBot):
    def __init__(self):
        self.helpers = Helpers()
        self.random_word = RandomWords()
        self.attributes = read_attribute_file('attributelist')

    async def random_teleport(self):
        randPos = self.helpers.getRandomPosition()
        print("Teleport to " + str(randPos))
        await self.highrise.teleport(user_id="641c3e64538ad317478ed48e", dest=randPos)

    async def offer(self):
        item = self.random_word.get_random_word()
        price = random.randint(50000, 10000000)
        await self.highrise.chat(message=f'Selling my precious {item} for {price} gold only!')

    async def on_start(self, session_metadata: highrise.SessionMetadata) -> None:
        await self.highrise.chat(message=f'Demo Bot started, have fun :)')
        await self.highrise.chat(message=f'Send me some stuff UwU')

    async def on_chat(self, user: User, message: str):
        print(f'{now_timestamp()} | {user.username} [{user.id}]: "{message}"')
        a = await self.highrise.get_room_users()
        print(a)
        await self.offer()


    async def on_whisper(self, user: User, message: str) -> None:
        print(f'{now_timestamp()} | {user.username} [{user.id}] [whisper]: "{message}"')

        match message.lower():
            case 'i love you':
                await self.highrise.send_whisper(user_id=user.id, message=f'I love you too <3')
            case 'weather':
                await self.highrise.send_whisper(user_id=user.id, message=await getweather("Rio de Janeiro"))
            case 'dice':
                await self.highrise.send_whisper(user_id=user.id, message=f'You got a {random.randint(1, 6)}!')
            case 'move':
                await self.highrise.walk_to(dest=self.helpers.getRandomPosition(), facing="FrontRight")
            case 'teleport':
                await self.highrise.teleport(user_id="641c3e64538ad317478ed48e", dest=self.helpers.getRandomPosition())
            case 'kill':
                exit(0)
            case 'teleportme':
                await self.highrise.teleport(user_id=user.id, dest=self.helpers.getRandomPosition())
            case 'userinfo':
                await self.highrise.send_whisper(user_id=user.id,
                                                 message=f'You are "{user.username}" with ID: \r\n{user.id}')
            case 'help':
                await self.highrise.send_whisper(user_id=user.id,
                                                 message=f'Supported Commands: \r\n - Weather \r\n - Dice \r\n - Move  \r\n - Teleport   \r\n - TeleportMe \r\n - UserInfo')
            case _:
                await self.highrise.send_whisper(user_id=user.id, message=f'I saw you whispered {message} to me!')
                await self.highrise.send_whisper(user_id=user.id, message=f'Whisper "help" to see what I can do...')

    async def on_user_join(self, user: User) -> None:
        print(f'{now_timestamp()} | {user.username} [{user.id}] joined the room!')
        await self.highrise.chat(message=f'Welcome {user.username}, looking {random.choice(self.attributes)} today!')

    pass
