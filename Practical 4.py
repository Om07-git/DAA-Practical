#Numpy
# 1. Create a numpy Array
#Write a python program to create and display a Numpy array
import numpy as np
numbers=np.array([10,20,30,40,50])
print("Array:",numbers)

#Basic Operation on Array
#Write a python program to perform addition,subtraction and multiplication on Numpy array
numbers=np.array([10,20,30,40,50])
print("Original array:",numbers)
print("Addition:",numbers+5)
print("Subtraction:",numbers-5)
print("Multiplication:",numbers*2)
#Find Maximum And minimum
#Write a Python program to find the maximum and minimum value in a NumPy array.
numbers=np.array([25,10,45,30,15])
print("Array",numbers)
print("Maximum:",np.max(numbers))
print("Minimum:",np.min(numbers))

#Slice a numpy Array
#Write a Python program to find the maximum and minimum value in a NumPy array.
numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Original array:", numbers)

print("First five elements:", numbers[0:5])

#Filter Array Values
#Write a python program to display values grater than 50 from numpy array
number=np.array([20,45,50,60,75,30,90])
result=number[number>50]
print("Values greater than 50:",result)
