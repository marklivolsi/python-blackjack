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
            print("Dealing cards...")
            game.draw_hands(deck)
            # game.update_all_points()
            game.print_table()
            for player in game.player_list:
                pass  # player_turn
            break
        break


if __name__ == '__main__':
    main()
