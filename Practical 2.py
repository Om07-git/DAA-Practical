# 1.Insert element in array 

arr=list(map(int,input("Enter element:").split()))

pos=int(input("Position:"))
val=int(input("Value:"))
arr.insert(pos-1,val)
print(arr)

# 2. Access Matrix Recursively
def show(a,i,j):
    if i==len(a): return
    print(a[i][j],end=" ")
    if j==len(a[0])-1:
        print()
        show(a,i+1,0)
    else:
        show(a,i,j+1)

r,c=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(r)]
show(a,0,0)
# 3.Matrix Addition and Multiplication
r,c=map(int,input().split())
A=[list(map(int,input().split()))for _ in range(r)]
B=[list(map(int,input().split())) for _ in range(r)]
print("Addition")
for i in range (r):
    row=[]
    for j in range(c):
        row.append(A[i][j]+B[i][j])
    print(row)
print("Multiplication")
for i in range(r):
    row=[]
    for j in range(c):
        s=0
        for k in range(c):
            s+=A[i][k]*B[k][j]
        row.append(s)
    print(row)

#4. Transpose Matrix
r,c=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(r)]
for j in range(c):
    for i in range(r):
        print(a[i][j],end=" ")
    print()
 
#5. Stack Using List
stack=[]
stack.append(10)
stack.append(20)
print(stack)
print("Pop:",stack.pop())
print(stack)

# 5 Linked List Insertion
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
temp=head
while temp:
    print(temp.data,end=" ")
    temp=temp.next

