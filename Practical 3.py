# 1. Linear Search
a=list(map(int,input().split()))
key=int(input())
f=False
for i in range(len(a)):
    if a[i]==key:
        print("Found at",i)
        f=True
        break
if not f:
    print("Not Found")

# 2. Binary Search
a=sorted(list(map(int,input().split())))
key=int(input())
l=0;r=len(a)-1
while l<=r:
    m=(l+r)//2
    if a[m]==key:
        print("Found")
        break
    elif key<a[m]:
        r=m-1
    else:
        l=m+1
else:
    print("Not Found")

# 3.Bubble Sort
a=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)

# 4.Selection Sort
a=list(map(int,input().split()))
for i in range(len(a)):
    m=i
    for j in range(i+1,len(a)):
        if a[j]<a[m]:
            m=j
    a[i],a[m]=a[m],a[i]
print(a)

# 5 Insertion Sort
a=list(map(int,input().split()))
for i in range(1,len(a)):
    key=a[i]
    j=i-1
    while j>=0 and a[j]>key:
        a[j+1]=a[j]
        j-=1
    a[j+1]=key
print(a)


