class Player:
    def __init__(self, player_num=1, name='Player 1', chips=1000):
        self.player_num = player_num
        self.name = name
        self.chips = chips
        self.hand = []
        self.wager = 0
        self.points = 0


class Dealer:
    def __init__(self):
        self.name = 'Dealer'
        self.hand = []
        self.points = 0
