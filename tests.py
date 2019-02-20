import unittest
from unittest.mock import patch

from cards import Deck
from gameplay import Game


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


class TestGame(unittest.TestCase):

    @patch('gameplay.get_input', return_value='q')
    def test_set_game_type_quick_game(self, mock_input):
        game = Game()
        game.set_game_type()
        self.assertEqual(game.quick_game, True)

    @patch('gameplay.get_input', return_value='n')
    def test_set_game_type_normal(self, mock_input):
        game = Game()
        game.set_game_type()
        self.assertEqual(game.quick_game, False)


if __name__ == '__main__':
    unittest.main()
