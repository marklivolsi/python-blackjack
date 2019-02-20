from cards import Deck
from player import Player, Dealer


def get_input(text):
    return input(text)


class Game:
    def __init__(self, num_players=1, quick_game=True):
        self.num_players = num_players
        self.quick_game = quick_game
        self.player_list = []
        self.deck = Deck()
        self.dealer = Dealer()

    def print_instructions(self): pass

    def set_game_type(self):
        print("Would you like to play a quick game or a normal game? Quick games are one player versus the dealer, \n",
              "and the player starts off with $1,000 in chips. Normal games allow you to set the number of players, \n",
              "player names, chip amounts for each player, and number of decks in the dealer's shoe.\n")

        game_type = None
        while game_type not in ('q', 'n'):
            game_type = get_input("Please choose a game type. Type 'q' for a quick game, or 'n' for a normal game: ")

        if game_type == 'n':
            self.quick_game = False

    def initialize_players(self): pass

    def initialize_deck(self): pass
