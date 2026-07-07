
try:
    num = input("Enter the numerator:")
    denom = input("Enter the denominator:")
    num = int(num)
    denom = int(denom)
    res = (int)(num/denom)
except ValueError:
    print("Error, inputed a letter when you're supposed to input numbers")
except ZeroDivisionError:
    print("Error, inputed 0 as the denominator")
else:
    res = str(res)
    with open("results.txt",'w') as rd:
     rd.write(res)
    rd.close