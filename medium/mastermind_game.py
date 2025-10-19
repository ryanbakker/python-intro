import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4


def generate_code():
    code = []

    # Repeat amount of times as code length
    for _ in range(CODE_LENGTH):
        # Select color
        color = random.choice(COLORS)
        # Add to code list
        code.append(color)

    return code


def guess_code():
    while True:
        # Convert to upper and put in a list of 4 elements to compare against generated code
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break
        # Break out of while loop if guessed colors are valid then return
        else:
            break

    return guess


def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    # Takes two arguments and combines them into a list of two items each containing two elements to compare
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            # Remove correct color from color count
            color_counts[guess_color] -= 1

    # Identify colors left in counts and are in the correct code to add to incorrect pos
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            # Remove incorrect color from color count
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos


def game():
    print("Welcome to the Mastermind Game!\n")
    print(f"You have {TRIES} tries to guess the secret code. Example: Y Y Y Y\n")
    print("The valid colors are", *COLORS)

    code = generate_code()

    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guess the code in {attempts} tried!")
            break

        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")

    else:
        print("You rand out of tries, the code was:", *code)


if __name__ == "__main__":
    game()
