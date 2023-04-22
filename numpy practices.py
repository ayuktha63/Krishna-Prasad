# Program to operate arithmetic calculation
#Addition
import numpy as np
first_matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
second_matrix = np.ones((3,3),dtype="int")
print(first_matrix)
print(second_matrix)
sum = first_matrix + second_matrix
print(sum)


# program to multiply two matrix
import numpy as np
a = np.ones((2,2),dtype="int")
b = np.full((2,2),5)
mul = np.matmul(a,b)
print(mul)



