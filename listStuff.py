inp1 = input("Enter your first number: ")
inp2 = input("Enter your second number: ")
inp3 = input("Enter your third number: ")
inp4 = input("Enter your fourth number: ")
inp5 = input("Enter your fifth number: ")
inp1 = float(inp1)
inp2 = float(inp2)
inp3 = float(inp3)
inp4 = float(inp4)
inp5 = float(inp5)
li = [inp1,inp2,inp3,inp4,inp5]
sum = inp1+inp2+inp3+inp4+inp5
average = sum/5

print(f"the sum is equal to {sum}")
print(f"the average is equal to {average}")

def max(li):
    maxi = li[1]
    for i in li:
        if i > maxi:
            maxi = i

    return maxi

maxi = max(li)
print(f"the maximum is equal to {maxi}")

