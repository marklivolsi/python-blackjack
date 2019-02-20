import unittest
from unittest.mock import patch

from cards import Deck
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

    @patch('player.input', return_value='1234')
    def test_buy_in(self, mock_input):
        """ Test buy-in function correctly sets player chips """
        player = Player()
        player.buy_in()
        self.assertEqual(player.chips, 1234)


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
    @patch.object(Player, 'buy_in', return_value=1234)
    @patch.object(Player, 'set_name', return_value='Joe')
    def test_initialize_players(self, mock1, mock2, mock3):
        """ Test the correct number of players are initialized for a normal game """
        game = Game()
        game.quick_game = False
        game.initialize_players()
        self.assertEqual(len(game.player_list), 7)

    # @patch('helpers.get_input', return_value='7')
    # @patch.object(Player, 'set_name', 'Joe')
    # @patch.object(Player, 'buy_in', 1234)
    # def test_set_num_players(self):
    #     """ Test the correct number of players are initialized for a normal game """
    #     self.assertEqual()


if __name__ == '__main__':
    unittest.main()
