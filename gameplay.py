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
            player.print_hand(player.hand)
            # if player.split_hand:
            #     player.print_hand(player.split_hand)
        print()

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
            self.dealer.hit(deck, self.dealer.hand)
            for player in self.player_list:
                player.hit(deck, player.hand)

    # def update_all_points(self):
    #     for player in self.player_list:
    #         player.points = sum_points_in_hand(player.hand)

    def set_all_wagers(self):
        for player in self.player_list:
            wager = get_int_input('{}, please set your wager (remaining chips: {}): '.format(player, player.chips))
            player.set_wager(wager)

    def player_turn_loop(self, deck):
        for player in self.player_list:
            print("{}'s turn...".format(player.name))

            # double_down, split, split_check = False, False, False
            double_down = False
            while True:
                player.update_points()
                player.print_hand(player.hand)
                print()
                # # If player drew a pair, offer choice to split hand.
                # if player.hand[0] == player.hand[1] and not split_check:
                #     split_choice = yes_no_choice("You got a pair. Would you like to split your hand? Type 'y' or 'n': ")
                #     if split_choice:
                #         split_wager = player.set_split_wager()
                #         if split_wager == -1:
                #             print("Sorry, you don't have enough chips to set a split wager.")
                #         else:
                #             split = True
                #             player.split_cards()
                #             player.hit(deck, player.hand)
                #             player.hit(deck, player.split_hand)
                #     split_check = True  # Ensure we only offer split option once
                #     continue

                # Main loop functionality

                if player.points == 21:
                    print("Congratulations, {}! You got Blackjack.".format(player))
                    break
                elif player.points > 21:
                    print("BUST! Sorry {}, your turn is over.".format(player))
                    break
                elif double_down:
                    break
                else:
                    choice = player_choice(double_down)
                    if choice == 'stand':
                        print('{} chose stand. Next turn...'.format(player))
                        break
                    elif choice == 'hit':
                        print('{} chose hit. Dealing another card...'.format(player))
                        player.hit(deck, player.hand)
                        continue
                    elif choice == 'doubledown':
                        print('{} chose doubledown. Doubling wager and dealing one more card...'.format(player))
                        double_wager = player.set_wager(player.wager)
                        if double_wager == -1:
                            print("Sorry, you don't have enough chips to double your wager.")
                        else:
                            player.hit(deck, player.hand)
                        double_down = True
                        continue
                    elif choice == 'surrender':
                        print('{} chose surrender. Discarding hand and returning half your wager.'.format(player))
                        player.surrender()
                        break
