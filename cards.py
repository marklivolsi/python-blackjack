from random import shuffle


point_dict = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.point_value = point_dict[self.value]


class Deck:
    def __init__(self):
        self.cards = []

    def reload(self, num_decks=1):
        for _ in range(0, num_decks):
            for card in point_dict.keys():
                for suit in suits:
                    self.cards.append(Card(card, suit))
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            self.reload()
        return self.cards.pop()
