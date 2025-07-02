from random import randint

def roll_dice():
    min_value = 1
    max_value = 6
    return randint(min_value, max_value)

while True:    # loop till you get the correct input
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():    # to check if the entererd values are digits
        players = int(players)
        if players>=2 and players<=4:    # to check if the correct number of player is entered
            break
        else:
            print("Wrong number of players!!")
    else:
        print("INVALID INPUT!!")

max_score = 50    # total score that can be achieved by any player
players_score = [0 for _ in range(players)]    # will give a list of zeros for the number of players, inital score of each player

while max(players_score) < max_score:
    for player in range(players):
        print(f"\n=== PLAYER {player+1} ===\n".center(25))
        print(f"Turn of player {player+1} to roll the dice: ")
        current_score = 0    # score at the starting of each round

        while True:
            confirmation = input("\nEnter 'y' to roll dice: ").lower()

            if confirmation != 'y':
                break

            value = roll_dice()
            if value == 1:
                print("You have rolled a one!!")
                break
            else:
                current_score += value
                print("You rolled a ", value)
            
            print("You score in this round is", current_score)

        players_score[player] += current_score    # to update the score

        print(f"\n=== SCOREBOARD === \n".center(25))
        for i in range(players):    # to print score of all the player after each round
           print(f"Total score of player {i+1} is {players_score[i]}")
