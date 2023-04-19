from highrise import User
class Bag():
    def __init__(self, user: User):
        self.userid = user.id
        self.pokeballs = 0
        self.superballs = 0
        self.hyperballs = 0
        self.masterballs = 0
        self.baits = 0
        self.stones = 0