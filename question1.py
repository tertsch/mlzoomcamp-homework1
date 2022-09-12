import numpy as np
import pandas

print("Question 1:", np.__version__)

df = pandas.read_csv("data.csv")

print("Question 2:", len(df))

value_counts = df['Make'].value_counts()
top3 = value_counts.head(3)
names = top3.keys().tolist()

print("Question 3:", ", ".join(names))

audis = df[df['Make'] == "Audi"]
print("Question 4:", audis["Model"].nunique())

null_cols = df.columns[df.isnull().any()]
print("Question 5:", len(null_cols))

median = df["Engine Cylinders"].median()
mode = df["Engine Cylinders"].mode()
print("Median:", median)
most_frequent = mode.tolist()
print("Most frequent value:", most_frequent[0])

filled = df["Engine Cylinders"].fillna(most_frequent[0])
print(filled.median())

if filled.median() == df["Engine Cylinders"].median():
    print("Question 6: NO")
else:
    print("Question 6: YES")
