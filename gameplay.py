# from cards import Deck
from player import Player #, Dealer
from helpers import *


max_players = 10


class Game:
    def __init__(self, quick_game=True):
        self.num_players = 1
        self.quick_game = quick_game
        self.player_list = []
        # self.deck = Deck()  # Deck doesn't need to be a game member. Move player methods to player class
        # self.deck.reload()
        self.dealer = Player(name='Dealer')  # Dealer()

    def print_instructions(self): pass

    def print_table(self, show_dealer=False):
        if show_dealer:
            print("Dealer's hand: {} (point total: {})".format(self.dealer.hand, self.dealer.points))
        else:
            print("Dealer's hand: [{}, ???]".format(self.dealer.hand[0]))
        for player in self.player_list:
            player.print_hand()

    def set_game_type(self):
        print("Would you like to play a quick game or a normal game? Quick games are one player versus the dealer,\n"
              "and the player starts off with $1,000 in chips. Normal games allow you to set the number of players,\n"
              "player names, chip amounts for each player, and number of decks in the dealer's shoe.\n")

        game_type = None
        while game_type not in ('q', 'n'):
            game_type = input("Please choose a game type. Type 'q' for a quick game, or 'n' for a normal game: ").lower()
            print()
        if game_type == 'n':
            self.quick_game = False

    def initialize_players(self):
        if self.quick_game:
            self.player_list = [Player()]
            return
        else:
            num_players = set_num_players(max_players)
            for player_num in range(num_players):
                player = Player()
                player.player_num = player_num + 1

                name = input("Hi, Player {}! Please enter your name: ".format(player.player_num))
                chips = get_int_input("Thanks {}! Now, please enter a buy-in amount (e.g. 1000): ".format(name))

                player.name = name
                player.chips = chips
                self.player_list.append(player)

    def draw_hands(self, deck):
        for _ in range(2):
            self.dealer.hit(deck)
            for player in self.player_list:
                player.hit(deck)

    # def update_all_points(self):
    #     for player in self.player_list:
    #         player.points = sum_points_in_hand(player.hand)

    def player_turn_loop(self, player, deck):
        for player in self.player_list:
            player.update_points()
            print("{}'s turn...".format(player.name))
            player.print_hand()

            double_down, split, split_check = False

            while True:
                # If player drew a pair, offer choice to split hand.
                if player.hand[0] == player.hand[1] and not split_check:
                    split_choice = yes_no_choice("You got a pair. Would you like to split your hand? Type 'y' or 'n': ")
                    if split_choice:
                        split_wager = player.set_split_wager()
                        if split_wager == -1:
                            print("Sorry, you don't have enough chips to set a split wager.")
                        else:
                            split = True
                            player.split_cards()
                    split_check = True
                    continue





            if split: pass
                # run loop a second time if split is true

            #
            # while True:
            #     if player.points == 21:
            #         print("Congratulations, {}! You got Blackjack.".format(player))
            #         break
            #     elif player.points > 21:
            #         print("BUST! Sorry {}, your turn is over.".format(player))
            #         break
            #     elif double_down:
            #         break






    # def player_turn(self, player):
    #     double_down, split = False
    #     while True:
    #         if player.points == 21:
    #             print("Congratulations, {}! You got Blackjack.".format(player.name))
    #             break
    #         elif player.points > 21:
    #             print("BUST! Sorry {}, your turn is over.".format(player.name))
    #             break
    #         elif double_down:
    #             break
    #
    #         if not split and player.hand[0] == player.hand[1]:
    #             text = """You drew a pair. Would you like to split and play two hands? You must wager the same amount
    #                       on your second hand. Type 'y' for yes, or 'n' for no: """
    #             split = yes_no_choice(text)
    #             if split:
    #                 player.split()

    # def play_hand(self, player, deck):
    #     double_down, split = False
