class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


dog = Dog("Gary", 14)
print(f"{dog.name} is currently {dog.age} years old")

dog.set_age(20)
print(f"Garry is now {dog.get_age()} years old")
