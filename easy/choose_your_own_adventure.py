name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt path, it has come to an end and you can go left or right?").lower()

if answer == "left":
    answer = input("You come to a river, you can swim across or walk downstream, type walk or swim").lower()

    if answer == "walk":
        print("You followed the river and found a settlement, you survive")
    elif answer == "swim":
        print("You swam across and drowned, welp")
    else:
        print("Not a valid option. You lose!")

elif answer == "right":
    answer = input("You come to a river, you can swim across or walk downstream, type walk or swim").lower()

    if answer == "walk":
        print("You followed the river and found a settlement, you survive")
    elif answer == "swim":
        print("You swam across and drowned, welp")
    else:
        print("Not a valid option. You lose!")

else:
    print("Not a valid option. You lose!")

print("Thank you for playing", name)
