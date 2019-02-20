class Dealer:
    def __init__(self):
        self.name = 'Dealer'
        self.hand = []
        self.points = 0


class Player:
    def __init__(self):
        self.player_num = 1
        self.name = 'Player 1'
        self.chips = 1000
        self.hand = []
        self.wager = 0
        self.points = 0

    def set_wager(self, wager):
        if wager <= self.chips:
            self.wager = wager
            self.chips -= wager
        else:
            return -1
