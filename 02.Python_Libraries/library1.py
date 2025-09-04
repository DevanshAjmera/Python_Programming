
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=np.array([1,7,8,11,9,3,2,20])
print("The mean is ",x.mean())
print("The maximum is ",x.max())
print("The minimum is ",x.min())
# x.sort()
# print(x)
for i in x:
    print(i)
print(x[-6:-2])   #Array slicing to get data from array

#We need to sort the data without using sort function....




#Shape, Reshape
#print(x.shape)
mydata=x.reshape(2,4)
print(mydata)

y=np.array([3,1,7,9,2,11,8,10])
z=x+y
print(z)