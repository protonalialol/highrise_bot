import random
from highrise import *


class Helpers():
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
