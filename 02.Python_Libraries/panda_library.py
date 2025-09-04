import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=np.array([1,2,3,4])
mydataframe=pd.DataFrame(x)
print(mydataframe)
print(" ")
mydata = pd.DataFrame(data=np.arange(0,100).reshape(10,10))
print(mydata.head()) #head -> top 5 rows
print("")
print(mydata.tail()) #tail -> last 5 rows

empsalary=pd.DataFrame(data=np.arange(0,100).reshape(10,10))
print(empsalary+1000)
print(empsalary.describe())

print("Mean is:")
print(mydata.mean(),"\n")
print(mydata.median(),"\n")
print(mydata.mode(),"\n")

print(empsalary.loc[[0,]]) #rows (print data in no. of rows.)
# iloc used for specific data 




