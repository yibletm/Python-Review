# [] means list
# () means tuple
# {} means set or dictionary
# dictionaries have {key:value} key value pairs in them

# Error handling is "handled" primarily by try-except clauses
print("What kind of 3 element list do you want to make today?")
inpint = int(input("0 for list, 1 for tuple, and 2 for set:"))

if inpint == 0:
    my_list = []
    for i in range(3):
        iter = i+1
        elm = input(f"What should element {i+1} be?:")
        my_list.append(elm)
    struc = my_list
elif inpint == 1:
    my_list = []
    for i in range(3):
        iter = i+1
        elm = input(f"What should element {i+1} be?:")
        my_list.append(elm)
    struc = tuple(my_list)
elif inpint == 2:
    my_list = []
    for i in range(3):
        iter = i+1
        elm = input(f"What should element {i+1} be?:")
        my_list.append(elm)
        struc = set(my_list)    
print(struc)












