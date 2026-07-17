class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

    def info(self):
        print("Dog name:", self.name)

d = Dog("Buddy")
# Inherited method
d.info()     
d.sound()

class Cat(Animal):
    def sound(self):
        print(self.name, "meows")
    
    def info(self):
        print("Cat name:", self.name)

c = Cat("Friend")
# Inherited method
c.info()     
c.sound()

