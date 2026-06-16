import pandas as pd
import numpy as np

students = pd.read_csv("students.csv")
#DataFrame
df=pd.DataFrame(students)
# print(df)

# print(df.head())
# print(df.tail())

average = np.mean(df["age"])
print(average)
student_above_20 =df[df["age"]>20]
print(student_above_20)
