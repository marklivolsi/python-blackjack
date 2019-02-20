import unittest

from cards import Deck


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


if __name__ == '__main__':
    unittest.main()
