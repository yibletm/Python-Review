class Car:

    def __new__(cls, *args):
        print("Creating instance")
        return super(Car, cls).__new__(cls)
    
    def __init__(self, brand="Default Brand", name="Default Name", type="Default Type"):
        self.brand = brand
        self.name = name
        self.type = type
    
    def printBrand(self):
        print(self.brand)
        
    def printName(self):
        print(self.name)
    
    def printType(self):
        print(self.type)

car1 = Car("Print", "The", "Files")
car2 = Car("Print")

car1.printBrand()
car1.printName()
car1.printType()

car2.printBrand()
car2.printName()
car2.printType()

    
