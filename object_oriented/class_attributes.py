class Person:
    number_of_people = 0
    gravity = -9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_persons(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("John")
p2 = Person("Mike")

print(Person.number_of_persons())
print(Person.gravity)
