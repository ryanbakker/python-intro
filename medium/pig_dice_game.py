import random


def roll_dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


value = roll_dice()

while True:
    players_amount = input("How many players would you like to play? (2-4): ")
    # Check is a valid integer before converting str to int
    if players_amount.isdigit():
        players_amount = int(players_amount)

        if 2 <= players_amount <= 4:
            break
        else:
            print("Please enter a number between 2 and 4")

    else:
        print("Invalid, try again")

max_score = 50
player_scores = [0 for _ in range(players_amount)]

while max(player_scores) < max_score:

    for player_idx in range(players_amount):
        print("\nPlayer", player_idx + 1, "turn to play!\n")
        print("\nYour total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll? (y/n): ").lower()
            if should_roll != "y":
                break

            value = roll_dice()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player", winning_idx + 1, "wins! with total score:", player_scores[winning_idx])
