from gameplay import Game
from player import Player
from cards import Deck


def main():
    game = Game()
    while True:
        game.set_game_type()
        game.initialize_players()
        deck = Deck()
        while True:
            game.set_all_wagers()
            print("Dealing cards...")
            game.draw_hands(deck)
            for player in game.player_list:
                player.update_points()
            game.print_table()
            game.player_turn_loop(deck)

            for player in game.player_list:
                print(player, player.chips, player.wager, player.hand)
            break
        break


if __name__ == '__main__':
    main()
