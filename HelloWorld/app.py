import math

# Formatted Strings
first = "Ryan"
last = "Bakker"
full = f"{first} {last}"
print(full)

# String Methods
course = "Python Programming"
course_capital = course.upper()
print(course_capital)
print(course.strip())  # Remove whitespace from string
print(course.find("pro"))  # Find index of pro
print(course.replace("p", "j"))  # Replace p with j
print("pro" in course)  # Return true if found in string

# Numbers
x = 1 + 2j  # Represents a complex number (a + bi)
y = 10 / 3  # Divide to a float
a = 10 // 3  # Divide to an integer
b = 10 ** 3  # Exponent - Left to the power of right

# Augmented Assignment Operator
c = 10
c = c + 3
c += 3  # Shorthand version

# Number Methods
# For complicated equations, we import the math object at the top
round(2.9)  # Round to 3
math.ceil(2.2)  # Get the ceiling = 3

# Type Conversion
# Convert options: int(x), float(x), bool(x), str(x)
# Get Type: type(x)
d = input("d: ")
e = int(d) + 1
print(f"d: {d}, e: {e}")
