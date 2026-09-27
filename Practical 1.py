#1. Write a program to insert an Element in an array
# Program to insert an element in an array

arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

print("Original Array:", arr)

position = int(input("Enter position to insert (1 to {}): ".format(n + 1)))
element = int(input("Enter element to insert: "))

arr.insert(position - 1, element)

print("Array after insertion:")
print(arr)

# 2.Write a program to aceess a matrix using Recursive Call
# Program display a matrix using recursion 

def display(matrix,rows,cols,i,j):
    if i==rows:
        return
    print(matrix[i][j],end="")

    if j == cols-1:
        print()
        display(matrix,rows,cols,i+1,0)
    else:
        display(matrix,rows,cols,i,j+1)

rows=int(input("Enter number of rows:"))
cols=int(input("Enter number of column:"))
matrix=[]
print("Enter matrix elements:")

for i in range(rows):
    row=[]
    for j in range (cols):
        row.append(int(input()))
    matrix.append(row)

print("Matrix:")

display(matrix,rows,cols,0,0)

# 3. Program to Perform Addition And multiplication of Two 2D Array
# Matrix Addition and Multiplication

rows=int(input("Enter number of rows: "))
cols=int(input("Enter number of columns:")) 

A=[]
B=[]

print("Enter elements of Matrix A")
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    A.append(row)
print("Enter element of Matrix B")

for i in range (rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    B.append(row)

print("Addition of Matrices")

for i in range (rows):
    for j in range(cols):
        print(A[i][j]+B[i][j],end="")
    print()

print("Multiplication of Matrices")

result=[]

for i in range(rows):
    row=[]
    for j in range(cols):
        total=0
        for k in range(cols):
            total= total+A[i][k]*B[i][j]
        row.append(total)
    result.append(row)

for i in range(rows):
    for j in range(cols):
        print(result[i][j],end="")
    print()

#4. Write a program to calculate the Transpse of a 2D Array
#program to find transpose of matrix

rows=int(input("Enter number of rows:"))
cols=int(input("Enter number of columns:"))

matrix=[]
print("Enter matrix elements")
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)
print("Original Matrix")

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end="")
    print()


print("\nTranspose Matrix")

for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=" ")
    print()
