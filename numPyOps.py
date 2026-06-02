import numpy as np
import sys


def getMean(arr1): #returns a float and obtains the mean
    fullval = 0
    for i in arr1:
        fullval += i
    size = np.size(arr1) # obtains the size of the array
    Mean = fullval/size
    return Mean

def getMax(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            print(i)
            max = i
    
    return max



arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr2 = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

arr3 = np.add(arr1,arr2) #adds the two arrays together
print(arr3)

arr4 = arr1 / arr2
print(arr4)

arr5 = np.divide(arr2, arr1)

print(arr5)

mean = getMean(arr1)
print(mean)

max = getMax(arr2)
print(max)




