import datetime
import random

from highrise import User, Position

class Helper():
    def log_message(self, user: User, message: str):
        print(f'{self.now_timestamp()} ;;; [INFO ] ;;; {user.username} [{user.id}] ;;; >>>{message}<<<')

    def log_whisper(self, user: User, message: str):
        print(f'{self.now_timestamp()} ;;; [INFO ] ;;; {user.username} [{user.id}] [whisper] ;;; >>>{message}<<<')

    def log_debug(self, message: str):
        print(f'{self.now_timestamp()} ;;; [DEBUG] ;;; {message}')

    def log_info(self, message: str):
        print(f'{self.now_timestamp()} ;;; [INFO ] ;;; {message}')

    def log_error(self, message: str):
        print(f'{self.now_timestamp()} ;;; [ERROR] ;;; {message}')

    def now_timestamp(self):
        return datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")

    def getRandomPosition(self):
        return tuple[random.random() * 10, random.random() * 10, random.random() * 10]

    def getLeftMostPosition(self):
        return (0.0, 0.0, 0.0)

    def getRightMostPosition(self):
        return (7.5, 0.0, 7.5)

    def getBottomMostPosition(self):
        return (1.0, 0.0, 7.0)

    def getTopMostPosition(self):
        return (8.0, 0.0, 0.0)

    def getRandomPosition(self):
        return (random.uniform(0.0,7.5), 1.0, random.uniform(0.0,7.5))

    def normalize_location(self, location: Position):
        return f'{round(location.x, 1)}_{round(location.y, 1)}_{round(location.z, 1)}'
