def add_vals(val1, val2):
    val3 = val1 + val2
    return val3

def find_oddoreven(val):
    if val%2 == 0:
        print("even")
    if val%2 == 1:
        print("odd")

def min_or_max(llist):
        maxval = llist[0]
        minval = llist[0]
        for val in llist:
            if val > maxval:
                maxval = val
            if val < minval:
                minval = val
        print(minval)
        print(maxval)       
    
v = 1
find_oddoreven(1)
blist = [9, 3, 2, 6, 5, 2, 1, 4]
min_or_max(blist)
    
