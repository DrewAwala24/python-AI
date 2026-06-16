import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("students.csv")
df = pd.DataFrame(data)
df.dropna()#remove missing data: NaN 
df["name"] = df["name"].fillna("Unknown")
students = df["name"]
marks = df["Marks"]
print (students)

#plt.bar(students,marks)bar
#plt.line(student,marks)line
#plt.scatter(student,marks)scatter

#plt.scatter(students,marks) 
#plt.title("Student Marks")
#plt.xlabel("Students")
#plt.ylabel("Marks")
 #plt.show()

#plt.pie(marks,labels=students)
 #plt.show()