class Dog1:
    sound = "bark"

dog1 = Dog1()
print(dog1.sound)

class Dog2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."
    species = "Canine"
        
dog1 = Dog2("Buddy", 3)
dog2 = Dog2("Charlie", 5)

print(dog1)  
print(dog2)

print(dog2.name)
print(dog2.age)
print(dog2.species)
