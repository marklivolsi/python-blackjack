def set_num_players():
    num_players = None
    while num_players not in range(1, 11):
        try:
            num_players = int(input("Please enter the desired number of players (max 10): "))
        except ValueError:
            continue
    return num_players
