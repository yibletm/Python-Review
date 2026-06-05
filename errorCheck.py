try:
    div = int(input("Enter a Number: "))
    quotient = 100/div #If flipped then put in "Type" where "Value" is at.
except ZeroDivisionError:
    print("Error, can't divide by 0")    
except ValueError:
    print("Error, can only accept numbers not letters")    
else:
    print(quotient)