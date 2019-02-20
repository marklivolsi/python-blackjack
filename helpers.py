def get_int_input(text):
    while True:
        try:
            value = int(input(text))
            break
        except ValueError:
            print("Sorry, please enter an integer value.")
            continue
    return value


def set_num_players(max_num):
    num_players = None
    while num_players not in range(1, max_num+1):
        try:
            num_players = int(input("Please enter the desired number of players (max 10): "))
        except ValueError:
            continue
    return num_players
