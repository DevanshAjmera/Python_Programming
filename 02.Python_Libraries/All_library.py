#Numpy -> Dataset Code
#Pandas -> Dataset Represent
#Matplotlib -> Graphically data display

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

years = np.array([2020,2021,2022,2024])
grade = np.array([96.4,91.2,80.5,81.5])

plt.plot(years,grade,marker = 'o')
plt.title("My Academic Grades")
plt.xlabel("Years")
plt.ylabel("Grades")
plt.grid()
plt.show()




x = np.array([90, 75, 80, 65])
name = ["Python", "Java", "React", "C"]
plt.pie(x)
plt.title("Pie Chart")
plt.legend(name, title="Languages")
plt.show()



plt.bar(years,grade)
plt.title("Bar-Graph")
plt.show()

plt.scatter(years,grade)
plt.grid()
plt.title("Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

