import numpy as np
import pandas

print("Question 1:", np.__version__)

data = pandas.read_csv("data.csv")

print("Question 2:", len(data))

value_counts = data['Make'].value_counts()
top3 = value_counts.head(3)
names = top3.keys().tolist()

print("Question 3:", ", ".join(names))
