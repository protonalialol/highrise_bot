from highrise import User
class Player():
    def __init__(self, user: User):
        self.userid = user.id
        self.username = user.username
        self.amountTipped = 0.0
        self.affectionFactor = 0.0
