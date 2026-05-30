fruits = ["apple, blueberry, strawberry, mangos"]
numbers = [1,2,3,4,5,6,7,8]

print(fruits)
print(numbers)

i = 0

while i<5:
    if i == 3:
        break
    print("Hello people")
    i=i+1

for i in range(1,20, 2):
    print(i)



#Tuples, sets, and dictionaries
#List = [], Set = {}, Tuple = () dictionary {Key,Value}

naturalseq = {1,2,3,4,5,6,7,8,9}
importantThings = ("work", "passion", "communication", "etc")
flavorOfFood = {"Apple":"sweet", "Lemon":"sour", "Jalapeño":"spicy", "Marmalade Orange":"Bitter", "Turkey":"Dry" }
print(flavorOfFood.get("Apple"))
