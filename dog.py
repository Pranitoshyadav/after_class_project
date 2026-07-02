class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(Dog.species)

print(dog1.name, dog1.age)
print(dog2.name, dog2.age)
