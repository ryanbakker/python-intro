print("Welcome to my computer quiz!")

playing = input("Do you want to play a game? ")

if playing.lower() != "yes":
    quit()

print("Let's play")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of NZ ")
if answer.lower() == "wellington":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct")
print("Pass rate " + str((score / 2) * 100) + "%")
