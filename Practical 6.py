#1. 2D Array using numpy
import numpy as np
arr=np.array([
    [10,20,30],
    [40,50,60]
])
print(arr)
print("Shape:",arr.shape)

# Reshape an Array
arr=np.array([1,2,3,4,5,6])
new_arr=arr.reshape(2,3)
print(new_arr)

#Generate Random Numbers
numbers=np.random.randint(1,100,10)
print(numbers)

#Calculate Mean,Median, & Standard Deviation
marks=np.array([60,70,80,90,75])
print("Mean:",np.mean(marks))
print("Median:",np.median(marks))
print("Standard Deviation:",np.std(marks))

#2. Group Student According to Course
import pandas as pd
data={
    "Name":["Rahul","Priya","Amit","Sneha"],
    "Course":["Bsc","BCA","Bsc","BCA"],
    "Marks":[80,90,70,85]
}
df=pd.DataFrame(data)
result=df.groupby("Course")["Marks"].mean()
print(result)

#Count Student in Each Course
data={
    "Name":["Rahul","Priya","Amit","Sneha"],
    "Course":["Bsc","BCA","Bsc","BCA"]
}
df=pd.DataFrame(data)
print(df["Course"].value_counts())

#Find Top 3 Students
data={
    "Name":["Rahul","Priya","Amit","Sneha","Kiran"],
    "Marks":[75,95,65,90,85]
}
df=pd.DataFrame(data)
result=df.sort_values("Marks",ascending=False)
print(result.head(3))

# Add a result Column
data={
    "Name":["Rahul","Priya","Amit","Sneha"],
    "Marks":[75,35,65,90]
}
df=pd.DataFrame(data)
df["Result"]=df["Marks"].apply(
    lambda x:"Pass" if x>=40 else "Fail"
)
print(df)

#Simple Bar Chart 
import matplotlib.pyplot as plt

names=["Rahul","Priya","Amit","Sneha"]
marks=[75,90,65,85]
plt.bar(names,marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks:")
plt.show()

#Simple Line Graph

months=["Jan","Feb","Mar","Apr"]
sales=[100,150,130,180]
plt.plot(months,sales)
plt.xlabel("Month")
plt.ylable("Sales")
plt.title("Monthly Sales")
plt.show()

#Simple Line Graph

months=["Jan","Feb","Mar","Apr"]
sales=[100,150,130,180]
plt.plot(months,sales)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()

#Simple Histogram
marks=[50,60,65,70,70,75,80,85,90,95]
plt.hist(marks)
plt.xlabel("marks")
plt.ylabel("Number of students")
plt.title("Distribution of marks")
plt.show()