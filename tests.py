import unittest
from unittest.mock import patch

from cards import Card, Deck
from helpers import *
from gameplay import Game
from player import Player


class TestDeck(unittest.TestCase):

    def test_num_cards(self):
        """ Test number of cards in deck is correct """
        d1, d13 = Deck(), Deck()
        d1.reload()
        d13.reload(13)
        d1_len, d13_len = len(d1.cards), len(d13.cards)

        self.assertEqual(d1_len, 52)
        self.assertEqual(d13_len, 676)

    def test_draw(self):
        """ Test draw function draws one card and reloads when no cards are left """
        deck = Deck()
        deck.reload()
        draw_pile = []

        for _ in range(0, 52):
            draw_pile.append(deck.draw())
        self.assertEqual(len(draw_pile), 52)

        deck.draw()
        self.assertEqual(len(deck.cards), 51)


class TestPlayer(unittest.TestCase):

    def test_update_points(self):
        """ Test that points are updated to correct value of cards in hand """
        player = Player()
        player.hand = [Card('Ace', 'Spades'), Card('Ace', 'Hearts'), Card('Queen', 'Diamonds')]  # Should be 22
        player.update_points()
        self.assertEqual(player.points, 22)

    def test_set_wager(self):
        """ Test that setting a wager results in correct wager, remaining chips, and returns -1 if bet is too large """
        player = Player()
        self.assertEqual(player.wager, 0)

        a = player.set_wager(25)
        self.assertEqual(player.wager, 25)
        self.assertEqual(player.chips, 975)
        self.assertEqual(a, None)

        b = player.set_wager(976)
        self.assertEqual(player.wager, 25)
        self.assertEqual(player.chips, 975)
        self.assertEqual(b, -1)

    def test_hit(self):
        """ Test that hit function removes one card from deck and places in player hand """
        deck = Deck()
        player = Player()
        player.hit(deck, player.hand)

        self.assertEqual(len(player.hand), 1)
        self.assertEqual(len(deck.cards), 51)

    def test_double_down(self):
        """ Test that double down doubles wager and deducts accordingly from chips """
        player = Player()
        player.set_wager(50)
        player.double_down()

        self.assertEqual(player.chips, 900)
        self.assertEqual(player.wager, 100)

    def test_surrender(self):
        """ Test that surrender returns half of wager to chips, clears hand, and clears wager  """
        deck = Deck()
        player = Player()
        player.hit(deck, player.hand)
        player.set_wager(50)
        player.surrender()

        self.assertEqual(player.wager, 0)
        self.assertEqual(player.chips, 975)
        self.assertEqual(len(player.hand), 0)


class TestGame(unittest.TestCase):

    @patch('gameplay.input', return_value='q')
    def test_set_game_type_quick_game(self, mock_input):
        """ Test quick game is set by default """
        game = Game()
        game.set_game_type()
        self.assertEqual(game.quick_game, True)

    @patch('gameplay.input', return_value='n')
    def test_set_game_type_normal(self, mock_input):
        """ Test normal game type set by user input """
        game = Game()
        game.set_game_type()
        self.assertEqual(game.quick_game, False)

    @patch('gameplay.set_num_players', return_value=7)
    @patch('gameplay.input', return_value='Joe')
    @patch('gameplay.get_int_input', return_value=1234)
    def test_initialize_players(self, mock1, mock2, mock3):
        """ Test the correct number of players are initialized for a normal game """
        game = Game()
        game.quick_game = False
        game.initialize_players()
        self.assertEqual(len(game.player_list), 7)


class TestHelpers(unittest.TestCase):

    def test_sum_points_in_hand(self):
        """ Test that point totals are summed correctly for a given hand """
        ace_spades = Card('Ace', 'Spades')  # 11 or 1 pts, depending on other cards
        ace_hearts = Card('Ace', 'Hearts')
        jack_hearts = Card('Jack', 'Hearts')  # 10 pts
        two_clubs = Card('Two', 'Clubs')  # 2 pts
        nine_diamonds = Card('Nine', 'Diamonds')  # 9 pts

        hand1 = [ace_spades, jack_hearts]  # 21
        hand2 = [jack_hearts, two_clubs]  # 12
        hand3 = [nine_diamonds, two_clubs, jack_hearts]  # 21
        hand4 = [ace_spades, jack_hearts, nine_diamonds, two_clubs]  # 22
        hand5 = [ace_spades, ace_hearts]  # 12

        self.assertEqual(sum_points_in_hand(hand1), 21)
        self.assertEqual(sum_points_in_hand(hand2), 12)
        self.assertEqual(sum_points_in_hand(hand3), 21)
        self.assertEqual(sum_points_in_hand(hand4), 22)
        self.assertEqual(sum_points_in_hand(hand5), 12)


if __name__ == '__main__':
    unittest.main()
