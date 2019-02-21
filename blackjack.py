from gameplay import Game
from player import Player
from cards import Deck


def main():
    game = Game()
    while True:
        game.set_game_type()
        game.initialize_players()
        while True:
            deck = Deck()
            game.draw_hands(deck)

            break
        break


if __name__ == '__main__':
    main()
