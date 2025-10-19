# Else-If Statement
temperature = 35
if temperature > 30:
    print("Temperature is too high")
    print("Drink some water")
elif temperature > 20:
    print("Temperature perfect")
else:
    print("Temperature is cold")
print("Outside conditional statement")

# Ternary Operator
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)
# Above can be written as:
message = "Eligible" if age >= 18 else "Not Eligible"

# Logical Operators: and, or, not
high_income = True
good_credit = True
student = True

if (high_income and good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

# Chaining Comparison Operators
# Age should be between 18 and 65
age = 22
# if age >= 18 and age < 65
if 18 <= age < 65:
    print("Eligible")

# For loops
# Print attempt 1 to 3
for number in range(3):
    print("Attempt", number + 1)

# Print 1 to 9 with steps of 2
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

# For Else
# When successful break out of loop
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempt failed")

# Nested Loops
for x in range(5):
    for y in range(3):
        print(f"{x}, {y}")

# Iterables
for x in "Python":
    print(x)
    # This will print each character through iterations

for x in [1, 2, 3]:
    print(x)
    # This will iterate through the "list" printing 1 to 3

# While Loops
number = 100
while number > 0:
    print(number)
    number //= 2
    # divide number by 2 into an integer if number is greater than 0

# While Loop Example
# By using lower() it doesn't matter which way the user types Quit
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
