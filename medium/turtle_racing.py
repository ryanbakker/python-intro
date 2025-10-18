import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'black', 'purple', 'pink', 'brown']


def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racing turtles (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not a number, try again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range (2 - 10)")


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacing_x, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Welcome to Turtle Racing!")


racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(winner.capitalize(), "turtle wins!")
time.sleep(5)
