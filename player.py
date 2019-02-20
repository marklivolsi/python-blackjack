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

    def set_name(self):
        player_name = input("Hi, Player {}! Please enter your name: ".format(self.player_num))
        self.name = player_name

    def buy_in(self):
        while True:
            try:
                chips = int(input("Thanks {}! Now, please enter a buy-in amount (e.g. 1000): ".format(self.name)))
                break
            except ValueError:
                continue
        self.chips = chips
