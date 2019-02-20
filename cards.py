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
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.cards = []

    def new_deck(self):
        for card in point_dict.keys():
            for suit in suits:
                self.cards.append(Card(card, suit))
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            self.new_deck()
        return self.cards.pop()

# deck = Deck()
# deck.new_deck()
# for i in deck.cards:
#     print(i.value+" of "+i.suit," : Value: ",i.point_value)
#
# print(len(deck.cards))
