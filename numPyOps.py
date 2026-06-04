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
arr4 = arr1 / arr2
arr5 = np.divide(arr2, arr1)
mean = getMean(arr1)
max = getMax(arr2)

twarr1 = np.array([["John Stein", 90, 70, 80], #90, 70, 80, 60,50,75, 70, 65, 90, 85, 75, 80, 100, 80,85
                  ["Carl Johnson", 60,50,75], 
                  ["Pearl Mariner", 70, 65, 90], 
                  ["Carly Anderson", 85, 75, 80], 
                  ["Ken Barley",100, 80,85]], dtype=object)
print(np.ndim(twarr1))
print(twarr1)

arr = twarr1[0]

def meanScore(twarr1):
    aoa = twarr1.shape[0]
    div = aoa*3
    sum = 0
    for arr in twarr1:
        for ind in arr:
            if not isinstance(ind, str):
                sum = sum + ind
    return sum/div


print(meanScore(twarr1))




