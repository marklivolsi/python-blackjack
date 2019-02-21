from helpers import sum_points_in_hand


class Player:
    def __init__(self, name='Player 1'):
        self.player_num = 1
        self.name = name
        self.chips = 1000
        self.hand = []
        self.wager = 0
        self.points = 0

    def __repr__(self):
        return self.name

    def update_points(self):
        self.points = sum_points_in_hand(self.hand)

    def print_hand(self, hand):
        print("{}'s hand: {} (point total: {}, bet: {}, remaining chips: {})".format(self.name, hand,
                                                                                     self.points, self.wager,
                                                                                     self.chips))

    def set_wager(self, wager):
        if wager <= self.chips:
            self.wager += wager
            self.chips -= wager
        else:
            return -1

    def hit(self, deck, hand):
        hand.append(deck.draw())

    def double_down(self):
        self.chips -= self.wager
        self.wager *= 2

    def surrender(self):
        self.hand = []
        self.chips += self.wager / 2
        self.wager = 0
