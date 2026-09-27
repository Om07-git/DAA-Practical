#Recursion
#1.Factorial
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)
num=int(input("Enter number:"))
print("Factorial:",factorial(num))

#2. Fibboacci Series
def fibboacci(n):
    if n<=1:
        return n
    return fibboacci(n-1)+fibboacci(n-2)
n=int(input("Enter number of terms:"))
for i in range(n):
    print(fibboacci(i),end="")
#Dictionary
# 1. Dictionary as Key-Value Data Structure


student = {
   "RollNo": 101,
   "Name": "Rahul",
   "Marks": 85
}


print("Roll No:", student["RollNo"])
print("Name:", student["Name"])
print("Marks:", student["Marks"])


# 2. Count Frequency of Elements


numbers = [10, 20, 10, 30, 20, 10]


frequency = {}


for number in numbers:
   if number in frequency:
       frequency[number] += 1
   else:
       frequency[number] = 1


print(frequency)


# 3. Word Frequency


text = "python data science python data"


words = text.split()


frequency = {}


for word in words:
   if word in frequency:
       frequency[word] += 1
   else:
       frequency[word] = 1


print(frequency)


#Set operation


A = {10, 20, 30, 40}
B = {30, 40, 50, 60}


print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)
