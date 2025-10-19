class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and {self.age} years old.")

    def speak(self):
        print("I don't know")


# Inheriting the upper level class = Pet
class Cat(Pet):
    def __init__(self, name, age, color):
        # Calling the init from the parent / super class
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print(f"Meow, I am a {self.color}")


# If a child class has the same named method as parent class, child class's method will override
class Dog(Pet):
    def speak(self):
        print("Bark")


p = Pet("Tim", 20)
p.speak()

c = Cat("Mark", 18, "tabby")
c.speak()

d = Dog("Bob", 13)
d.speak()
