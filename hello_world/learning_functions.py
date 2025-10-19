# Define a function with parameters
def greet(first_name, last_name):
    print(f"Hi, {first_name} {last_name}")
    print("Welcome aboard")


greet("John", "Smith")
greet("John", "Doe")


# Types of functions

# 1) Perform a task
def greeting(name):
    print(f"Hello, {name}")


greeting("John")


# 2) Calculate and return a value
def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("John")


# Keyword Arguments
# by=1 is a keyword argument, that makes the code more readable
def increment(number, by):
    return number + by


print(increment(2, by=1))


# Default Arguments
# Set by=1 in the function argument to prevent inputting it everytime the function is called
# The default parameter can be overridden when calling the function
# Optional arguments must go after required arguments
def increment(number, by=1):
    return number + by


print(increment(2, by=5))
