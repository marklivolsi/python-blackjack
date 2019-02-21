def get_int_input(text):
    while True:
        try:
            value = int(input(text))
            break
        except ValueError:
            print("Sorry, please enter an integer value.")
            continue
    return value


def yes_no_choice(text):
    choice = None
    while choice not in ('y', 'n'):
        choice = input(text)
    if choice == 'y':
        return True
    return False


def set_num_players(max_num):
    num_players = None
    while num_players not in range(1, max_num+1):
        try:
            num_players = int(input("Please enter the desired number of players (max 10): "))
        except ValueError:
            continue
    return num_players


def sum_points_in_hand(hand):
    total = sum(card.point_value for card in hand)
    if total <= 21:
        return total
    elif any(card.value == 'Ace' for card in hand):
        total -= 10
        return total
