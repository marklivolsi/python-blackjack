from cards import Deck
from player import Player, Dealer
from helpers import set_num_players


class Game:
    def __init__(self, quick_game=True):
        self.num_players = 1
        self.quick_game = quick_game
        self.player_list = []
        self.deck = Deck()
        self.dealer = Dealer()

    def print_instructions(self): pass

    def set_game_type(self):
        print("Would you like to play a quick game or a normal game? Quick games are one player versus the dealer,\n"
              "and the player starts off with $1,000 in chips. Normal games allow you to set the number of players,\n"
              "player names, chip amounts for each player, and number of decks in the dealer's shoe.")

        game_type = None
        while game_type not in ('q', 'n'):
            game_type = input("Please choose a game type. Type 'q' for a quick game, or 'n' for a normal game: ").lower()

        if game_type == 'n':
            self.quick_game = False

    def initialize_players(self):
        if self.quick_game:
            self.player_list = [Player()]
            return
        else:
            num_players = set_num_players()
            for player_num in range(num_players):
                player = Player()
                player.player_num = player_num + 1
                player.set_name()
                player.buy_in()
                self.player_list.append(player)

    def initialize_deck(self): pass
