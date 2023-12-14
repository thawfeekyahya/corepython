# Numpy is a package for scientific calculations in python also by default python does not support multidimensional array
# Numpy package provides the multidimensional support

import numpy as Numpy

arr = Numpy.array([5,4,3,2,1],int)
for i in arr:
    print(i)

# array using linespace function
arr = Numpy.linspace(0,10,5)
print(arr)

# array using arrange function

array =  Numpy.arange(0,10,1.5)
print(array)


# individual operations like for each style

print("for each style")
array = Numpy.array([0,1,2,3,4,5,6,7,8,9],int)
print("Orignal array",array)
array2 = array % 2
print("Modified for modulo operator on each element",array2)

# Comparision

array1 = Numpy.array([1,2,3,4,6,8,9,10],int)
array2 = Numpy.array([0,3,5,8,1,2,3,0],int)

result = array1 < array2
print(result)


# Conditional For each
array = Numpy.array([1,2,3,4,5,6,7,8,9],int)
result = Numpy.where(array%2 == 0, array,0)
print(result)

# array slicing

print("--Slicing---")
array=Numpy.array([0,1,2,3,4,5,6],int)
print(array[1:4:2])
print("---Reverse slice----")
print(array[-1:0:-1])


# multidimensional array

multidarray = Numpy.array([
    [0,1],
    [2,3]
    ])
print(multidarray)
print("Element at 2,2 is ",multidarray[0:1])

# Create multi-dimensional array using reshape and arrange
print("multi-dimensional array using arrange and reshape")
array = Numpy.reshape(Numpy.arange(11,36,1),(5,5))
print(array)

# Print a random number
print(Numpy.random.rand())
