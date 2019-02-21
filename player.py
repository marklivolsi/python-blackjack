from helpers import sum_points_in_hand

# Dealer can be a player class instead

# class Dealer:
#     def __init__(self):
#         self.name = 'Dealer'
#         self.hand = []
#         self.points = 0


class Player:
    def __init__(self, name='Player 1'):
        self.player_num = 1
        self.name = name
        self.chips = 1000
        self.hand = []
        self.split_hand = []
        self.wager = 0
        self.split_wager = 0
        self.points = 0
        self.split_points = 0

    def __repr__(self):
        return self.name

    def update_points(self):
        self.points = sum_points_in_hand(self.hand)

    def print_hand(self):
        self.update_points()
        print("{}'s hand: {} (point total: {}, bet: {}, remaining chips: {})".format(self.name, self.hand,
                                                                                     self.points, self.wager,
                                                                                     self.chips))

    def set_wager(self, wager):
        if wager <= self.chips:
            self.wager = wager
            self.chips -= wager
        else:
            return -1

    def set_split_wager(self):
        if self.wager <= self.chips:
            self.split_wager = self.wager
            self.chips -= self.wager
        else:
            return -1

    def hit(self, deck):
        self.hand.append(deck.draw())

    def double_down(self):
        # self.hit(deck)  # remove this logic from doubledown, handle in hit only
        self.chips -= self.wager
        self.wager *= 2

    def surrender(self):
        self.hand = []
        self.chips += self.wager / 2
        self.wager = 0

    def split_cards(self):  # split wager will be set separately
        self.split_hand.append(self.hand.pop())

    # def player_turn(self, deck):
    #     self.update_points()
    #     print("{}'s turn. This is your hand: {} (points: {})".format(self.name, self.hand, self.points))


        # self.split_hand.append(self.hand.pop())
        # if self.wager <= self.chips:
        #     self.split_wager = self.wager
        #     self.chips -= self.wager
        # else:
        #     return -1


